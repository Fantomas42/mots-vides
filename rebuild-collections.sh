#!/bin/bash
# Rebuild all collections of stop words

path=${1-mots_vides/datas/}

for lang in $(ls $path)
do
  lang=$(echo $lang | cut -f1 -d.)
  ./bin/merge-stop-words $lang $path$lang.txt
done
