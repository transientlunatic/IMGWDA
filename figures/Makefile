FIGURES=(gw-spectum)

all : gw-spectrum.pdf aligo-cbc.pdf gp-training-data.pdf gp-example-prior-draws.pdf probability-structured-example-dense-1.pdf probability-structured-example-dense-2.pdf probability-structured-example-dense-3.pdf

gw-spectrum.pdf : ../scripts/spectrum.py
	python $<

aligo-cbc.pdf : ../scripts/cbc-aligo.py
	python $<

gp-training-data.pdf gp-example-prior-draws.pdf: ../scripts/gp-example-plots.py
	python $<

probability-structured-example-dense-1.pdf: ../scripts/probability-structured-example-dense-1.dot
	circo -Gsize=6,2\! -Tpdf $< > $@

probability-structured-example-dense-2.pdf: ../scripts/probability-structured-example-dense-2.dot
	circo -Tpdf $< > $@

probability-structured-example-dense-3.pdf: ../scripts/probability-structured-example-dense-3.dot
	circo -Tpdf $< > $@
