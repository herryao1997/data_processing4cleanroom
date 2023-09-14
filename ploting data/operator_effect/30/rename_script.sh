#!/bin/bash

# Loop through all .py files in the current directory
for file in *.py; do
    # Extract the file name without extension
    filename=$(basename "$file" .py)
    # Replace "20" with "30" in the filename
    new_filename="${filename//40/30}"
    # Create the new file name with .py extension
    new_file="$new_filename.py"
    # Rename the file
    mv "$file" "$new_file"
    echo "Renamed: $file -> $new_file"
done
