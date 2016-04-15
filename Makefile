TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEXMK = latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make
BIB = bibtex
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"

.PHONY: document.pdf all clean

all : document.pdf

view :
	evince document.pdf

document.pdf : document.pdf
	$(TEXMK) $<

clean:
	latexmk -CA
