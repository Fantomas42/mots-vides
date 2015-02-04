#!/bin/bash
# Rebuild all collections of stop words

path=${1-mots_vides/datas/}

for lang in $(ls $path)
do
  file=$(echo $lang | cut -f1 -d.)
  lang=$(echo $file | cut -f2 -d-)
  ./bin/merge-stop-words $lang $path$file.txt
done
