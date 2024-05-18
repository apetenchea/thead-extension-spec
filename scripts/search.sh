#!/usr/bin/env bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <keywords_file> <directory>"
    exit 1
fi

keywords_file="$1"
directory="$2"

# Loop through each keyword
while IFS= read -r keyword; do
    # Use ripgrep to find files containing the keyword
    files=$(rg --files-with-matches -l "$keyword" "$directory" | tr '\n' ' ')

    # Check if files were found
    if [ -z "$files" ]; then
        echo "$keyword"
    else
        echo "$keyword $files"
    fi
done < "$keywords_file"
