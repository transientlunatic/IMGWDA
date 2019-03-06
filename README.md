# Topics in Gravitational Wave Astronomy
Daniel Williams

This repository contains the text and code necessary to produce my thesis.

* The `chapters` directory contains the text of the thesis in `org-mode` format. 
  These can be converted to numerous other formats using scripts in the `scripts/build` directory, with the makefile capable of producing these itself.

* The `figures` directory contains a number of the figures from the document, although many need to be generated (via the makefile in this directory).

* The `notebooks` directory contains a number of Jupyter notebooks which can be used to generate the figures from this work.

* The `scripts` directory contains scripts used to generate figures from this work, and a makefile which can generate a number of these scripts from jupyter notebooks in the `notebooks` directory.

* The `bibliography` directory contains org files which describe the bibliography of the thesis, along with my notes on these works. `.bib` files can be generated via the main project makefile.

