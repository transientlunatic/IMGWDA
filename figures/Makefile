FIGURES=(gw-spectum)

FILETYPE=".pdf"

INTRO_FIGURES="gw-spectrum"


.PHONY: all clean

all : intro/gw-spectrum.pdf sources/aligo-cbc.pdf gp-training-data.pdf gp-example-prior-draws.pdf probability-structured-example-dense-1.pdf probability-structured-example-dense-2.pdf probability-structured-example-dense-3.pdf

%.py :
	cd ../scripts & make

intro/gw-spectrum.pdf : ../scripts/intro/Spectrum.py
	python $<

sources/aligo-cbc.pdf : ../scripts/intro/sensitivity-curves.py #cbc-aligo.py
	python $<

# Sources

sources/minke-adhoc.pdf : ../scripts/sources/minke-waveforms.py
	python $<

gp-training-data.pdf gp-example-prior-draws.pdf: ../scripts/gp-example-plots.py
	python $<

probability-structured-example-dense-1.pdf: ../scripts/probability-structured-example-dense-1.dot
	circo -Gsize=6,2\! -Tpdf $< > $@

probability-structured-example-dense-2.pdf: ../scripts/probability-structured-example-dense-2.dot
	circo -Tpdf $< > $@

probability-structured-example-dense-3.pdf: ../scripts/probability-structured-example-dense-3.dot
	circo -Tpdf $< > $@

# clean :
# 	rm $(INTRO_FIGURES)
