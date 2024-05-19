#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <file_with_filenames>"
    exit 1
fi

mkdir -p dumps

while IFS= read -r file
do
    if [ -f "$file" ]; then
        # Run objdump and save the output to the dumps folder
        ./build/bin/riscv64-unknown-linux-gnu-objdump -D -d "$file" > "dumps/$(basename "$file").dump"
    else
        echo "File not found: $file"
    fi
done < "$1"
