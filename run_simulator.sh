#!/usr/bin/env bash

set -euo pipefail

if [[ "$#" -eq 2 && -f "${2}" ]]; then
    optimize="--no-optimize"
    scheduler_type="${1}"
    file="${2}"
elif [[ "$#" -eq 3 && "${1}" = "optimize" && -f "${3}" ]]; then
    optimize="--optimize"
    scheduler_type="${2}"
    file="${3}"
else
    echo "Usage: ${0} [optimize] scheduler_type filename" >&2
    exit 1
fi

python -m hash_code_2021 ${optimize} --scheduler ${scheduler_type} simulate < "${file}"