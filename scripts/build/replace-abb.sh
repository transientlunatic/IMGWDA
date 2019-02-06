#!/bin/sh

sed 's/[\[\[]*abbr:\([a-z0-9]*\)[\]\]]*/\\gls\{\1\}/g' < $1 | \
    sed 's/gls:\([a-z0-9\-]*\)/\\gls\{\1\}/g' | \
    sed 's/abbr:\([a-z0-9\-]*\)/\\gls\{\1\}/g' | \
    sed 's/abb:\([a-z0-9\-]*\)/\\gls\{\1\}/g' | \
    sed 's/abpl:\([a-z0-9\-]*\)/\\glspl\{\1\}/g' | \
    sed 's/abbp:\([a-z0-9\-]*\)/\\glspl\{\1\}/g' | \
    sed 's/\s*cite:\([A-Za-z0-9,:\.\-\&]*[A-Za-z0-9]\)*/\\nbsp\{\}\\cite\{\1\}/g' | \
    sed 's/\s*ref:\([A-Za-z0-9,:\.\-]*[A-Za-z0-9]\)*/\\nbsp\{\}\\ref\{\1\}/g' | \
    sed 's/\s*unit:\([A-Za-z]*\)/\,\{\1\}/g' # Right now this does nothing except remove the unit prefix
