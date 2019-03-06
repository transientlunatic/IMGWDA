# Convert notebooks to easy-to-execute scripts
# Right now I'm only doing this for the intro scripts, and should change this
# in due course when I remove spaces from the names of the other notebooks.

SCRIPT_DIR=./intro
NOTEBOOK_DIR=../notebooks/intro
NB_FILES=$(wildcard $(NOTEBOOK_DIR)/*.ipynb)
PY_FILES=$(NB_FILES:.ipynb=.py)
PY_DESTS=$(PY_FILES:$(NOTEBOOK_DIR)/%.py=$(SCRIPT_DIR)/%.py)

.PHONY : clean all

all : python

python : $(PY_FILES)

%.py : %.ipynb
	jupyter nbconvert --to python $<
	@mkdir -p $(@D:$(NOTEBOOK_DIR)=$(SCRIPT_DIR))	
	cp $@ $(@:$(NOTEBOOK_DIR)/%.py=$(SCRIPT_DIR)/%.py)

clean:
	rm $(PY_FILES)
	rm $(PY_DESTS)
