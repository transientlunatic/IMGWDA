TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEXMK = latexmk -f -pdf -pdflatex="pdflatex -interaction=nonstopmode" #-use-make
BIB = bibtex
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"

.PHONY: document.pdf all clean

all : document.pdf

view :
	evince document.pdf &

document.pdf : document.tex
	$(TEXMK) $<

document.gls :
	makeglossaries document.tex

clean:
	latexmk -CA
	rm -rf *.glo *.glg *.ist *.acn *.xdy
	rm -rf *.bbl *.gls *.glsdefs
