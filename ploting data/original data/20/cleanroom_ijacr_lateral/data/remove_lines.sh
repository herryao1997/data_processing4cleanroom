#!/bin/bash

for file in *.out; do
    if [ -f "$file" ]; then
        echo "Processing file: $file"
        sed -i '1,3d' "$file"
        echo "Removed first three lines from: $file"
    fi
done

