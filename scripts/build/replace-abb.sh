#!/bin/sh

sed 's/[\[\[]*abbr:\([a-z0-9]*\)[\]\]]*/\\gls\{\1\}/g' < $1 | \
sed 's/gls:\([a-z0-9]*\)/\\gls\{\1\}/g' | \
sed 's/cite:\([A-Za-z0-9,:\.\-]*[A-Za-z0-9]\)*/\\cite\{\1\}/g' | \
sed 's/ref:\([A-Za-z0-9,:\.]*[A-Za-z0-9]\)*/\\ref\{\1\}/g'
