#!/us/bin/env bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <keywords_file> <dump_file>"
    exit 1
fi

keywords_file="$1"
dump_file="$2"

# Loop through each keyword
while IFS= read -r keyword; do
    # Use ripgrep to find files containing the keyword
    samples=$(rg -m 2 "\s+\s+$keyword\s+" "$dump_file")

    # Check if files were found
    if [ -z "$samples" ]; then
        echo "!!! $keyword"
    else
        printf "+++ $keyword\n$samples\n"
    fi
done < "$keywords_file"
