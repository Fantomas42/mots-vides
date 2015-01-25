#!/bin/bash
# Rebuild all collections of stop words

for lang in $(ls ./mots_vides/datas/)
do
  lang=$(echo $lang | cut -f1 -d.)
  ./bin/merge-stop-words $lang mots_vides/datas/$lang.txt
done
