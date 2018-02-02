DESCRIPTION = "This is a Makefile for my Thesis"
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEXMK = latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" #-use-make
BIB = bibtex
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"

.PHONY: document.pdf all clean glossary pdf help

#all : document.pdf

help :  ## Show this help message.
# This code snippet came from https://gist.github.com/prwhite/8168133
	@echo $(DESCRIPTION)
	@echo "---"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

view :  ## View the output PDF file.
	evince document.pdf &

pdf :	document.pdf ## Produce a PDF output

document.pdf : document.tex tex/glossaries.tex
	$(TEXMK) $<

document.gls :
	makeglossaries document.tex

tex/glossaries.tex :
	python scripts/build/glossary.py chapters/glossary/glossary.org > tex/glossaries.tex

glossary : tex/glossaries.tex ## Convert the glossary into a format acceptable to one of the languages supported.

clean:	## Remove all of the temporary files which the various compilation steps produce
	latexmk -CA
	rm tex/glossaries.tex
	rm -rf *.glo *.glg *.ist *.acn *.xdy
	rm -rf *.bbl *.gls *.glsdefs
