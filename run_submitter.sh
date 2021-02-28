#!/usr/bin/env bash

set -euo pipefail

if [[ "$#" -eq 2 && "${1}" = "optimize" ]]; then
    optimize="--optimize"
    scheduler_type="${2}"
elif [[ "$#" -eq 1 ]]; then
    optimize="--no-optimize"
    scheduler_type="${1}"
else
    echo "Usage: ${0} [optimize] scheduler_type" >&2
    exit 1
fi

for file in {a,b,c,d,e,f}.txt; do
    echo "Executing for file ${file}"
    python -m hash_code_2021 ${optimize} --scheduler ${scheduler_type} submit < "${file}" > "${file%.txt}.out.txt"
done