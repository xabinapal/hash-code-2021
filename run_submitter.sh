#!/usr/bin/env bash

for file in {a,b,c,d,e,f}.txt; do
    echo "Executing for file ${file}"
    python -m hash_code_2021 submit < ${file} > ${file}.out
done