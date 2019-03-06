DESCRIPTION = "This is a Makefile for my Thesis"
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEXMK = latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode"  #-use-make
#TEXMK = latexmk -f -pdf -pdflatex="xelatex -interaction=nonstopmode"  #-use-make
BIB = bibtex
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"

BASH = /bin/bash
PANDOC = pandoc
SUBBER = $(BASH) scripts/build/replace-abb.sh

BDIR = _build

ORG_FILES=$(wildcard chapters/*/*.org)
ORG_BIB=$(wildcard bibliography/*.org)
INT_FILES=$(ORG_FILES:.org=.int_tex)
TEX_FILES=$(ORG_FILES:.org=.tex)
INT_BIBS=$(ORG_BIB:.org=.intbib)
BIB_FILES=$(ORG_BIB:.org=.bib)
#$(patsubst chapters/%.org,$(BDIR)/org/%.int_tex,$(ORG_FILES))
#TEX_FILES=$(patsubst chapters/%.org,$(BDIR)/tex/%.tex,$(ORG_FILES))
HTML_FILES=$(patsubst chapters/%.org,$(BDIR)/html/%.html,$(ORG_FILES))
.PHONY: document.pdf all clean glossary pdf help tex figures scripts

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

document.pdf : document.tex git-info.tex chapters/glossary/glossary.tex $(BIB_FILES) $(TEX_FILES) figures
	$(TEXMK) $<
	biber document
	$(TEXMK) $<

figures: scripts
	cd figures && $(MAKE)

scripts:
	cd scripts && $(MAKE)

glossary: chapters/glossary/glossary.tex ## Convert the org table to a glossary

git-info.tex :
	git describe --tags --long --always --dirty='-*' 2>/dev/null > $@

chapters/glossary/glossary.org:
chapters/glossary/glossary.tex_int: chapters/glossary/glossary.org
chapters/glossary/glossary.tex : chapters/glossary/glossary.int_tex
	python scripts/build/glossary.py $< > $@

%.int_tex : %.org 
	@mkdir -p $(@D)
	$(SUBBER) $< > $@

%.tex : %.int_tex
	emacs $< -Q --batch --eval "(require 'org)" --eval "(setq org-latex-caption-above nil)" --eval "(setq org-latex-prefer-user-labels t)"  --eval "(org-latex-export-to-latex nil nil nil t)"  --kill

%.intbib : %.org
	$(SUBBER) $< > $@
%.bib : %.org
	echo "Producing $@ at $(notdir $@)"
	emacs $< -Q --batch --eval "(require 'org-bibtex)"   --eval '(org-bibtex "$(notdir $@)")' --kill

$(HTML_FILES) : $(ORG_FILES)
	@mkdir -p $(@D)	
	$(PANDOC) -f org -t html -o $@ $*



#glossary : tex/glossaries.tex ## Convert the glossary into a format acceptable to one of the languages supported.

clean:	## Remove all of the temporary files which the various compilation steps produce
	latexmk -CA
	cd scripts && make clean && cd -
	rm $(TEX_FILES)
	rm $(INT_FILES)
	rm -rf *.glo *.glg *.ist *.acn *.xdy *.acr *.alg
	rm -rf *.bbl *.gls *.glsdefs
	rm -rf *.mtc*
