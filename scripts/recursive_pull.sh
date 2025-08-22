#!/bin/bash

# Loop through each subfolder
for folder in */; do
    # Check if the subfolder is a git repository
    if [ -d "$folder/.git" ]; then
        echo "Updating $folder"
        # Navigate into the git repository and perform a git pull
        (cd "$folder" && git pull)
    fi
done