DESCRIPTION = "This is a Makefile for my Thesis"
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEXMK = latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode"  #-use-make
BIB = bibtex
xPRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"

BDIR = _build

ORG_FILES=$(wildcard chapters/*/*.org)
INT_FILES=$(ORG_FILES:.org=.int_tex)
TEX_FILES=$(ORG_FILES:.org=.tex)
#$(patsubst chapters/%.org,$(BDIR)/org/%.int_tex,$(ORG_FILES))
#TEX_FILES=$(patsubst chapters/%.org,$(BDIR)/tex/%.tex,$(ORG_FILES))
HTML_FILES=$(patsubst chapters/%.org,$(BDIR)/html/%.html,$(ORG_FILES))
.PHONY: document.pdf all clean glossary pdf help tex

help :  ## Show this help message.
# This code snippet came from https://gist.github.com/prwhite/8168133
	@echo $(DESCRIPTION)
	@echo "---"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

view :  ## View the output PDF file.
	evince document.pdf &

tex :	$(TEX_FILES)
html : $(HTML_FILES)

pdf :	document.pdf ## Produce a PDF output

document.pdf : document.tex  chapters/glossary/glossary.tex $(TEX_FILES)
	$(TEXMK) $< 


chapters/glossary/glossary.tex : chapters/glossary/glossary.int_tex
	python scripts/build/glossary.py $< > $@

%.int_tex : %.org 
	@mkdir -p $(@D)
	bash scripts/build/replace-abb.sh $< > $@

%.tex : %.int_tex
	emacs $< -Q --batch --eval "(require 'org)"  --eval "(org-latex-export-to-latex nil nil nil t)" --eval "(setq org-latex-caption-above nil)" --kill

#$(INT_FILES) : %.int_tex : $(ORG_FILES)
#	@mkdir -p $(@D)
#	bash scripts/build/replace-abb.sh $< > $@

#$(TEX_FILES) : $(INT_FILES)
#	@mkdir -p $(@D)
#	

$(HTML_FILES) : $(ORG_FILES)
	@mkdir -p $(@D)	
	pandoc -f org -t html -o $@ $*



glossary : tex/glossaries.tex ## Convert the glossary into a format acceptable to one of the languages supported.

clean:	## Remove all of the temporary files which the various compilation steps produce
	latexmk -CA
	rm $(TEX_FILES)
	rm $(INT_FILES)
	rm -rf *.glo *.glg *.ist *.acn *.xdy *.acr *.alg
	rm -rf *.bbl *.gls *.glsdefs
	rm -rf *.mtc*
