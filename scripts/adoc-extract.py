import os
import re
import sys


def find_th_lines(starting_dir):
    # Compile the regular expression for the lines we're interested in
    pattern = re.compile(r'^==== th')

    # Walk through the directory tree starting at the given directory
    for root, dirs, files in os.walk(starting_dir):
        # Only process folders that start with 'xthead'
        dirs[:] = [d for d in dirs if d.startswith('xthead')]
        
        for file in files:
            if file.endswith('.adoc'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if pattern.match(line):
                            # Print the matched line followed by the file path
                            print(f"{line.strip()} {root}/{file}")


if __name__ == '__main__':
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    find_th_lines(directory)
