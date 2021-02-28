#!/usr/bin/env bash

if [[ "$#" -ne 1 || ! -f "${1}" ]]; then
    echo "Usage: ${0} [filename]" >&2
    exit 1
fi

file="${1}"

python -m hash_code_2021 simulate < "${file}"