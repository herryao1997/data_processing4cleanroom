#!/bin/bash

for file in *.out; do
    if [ -f "$file" ]; then
        newname="${file%.out}.txt"
        mv "$file" "$newname"
        echo "Renamed $file to $newname"
    fi
done
