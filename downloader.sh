#!/bin/bash

# Define the URL of the website
url="https://whereisxur.com/"

# Get the current date in MM-DD-YYYY format
current_date=$(date +'%m-%d-%Y')

# Create the output directory
output_directory="$current_date"
mkdir -p "$output_directory"

# Change to the output directory
cd "$output_directory" || exit 1

# Create the output filename
output_filename="index.html"

# Use curl to download the HTML content
curl -o "$output_filename" "$url"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "HTML content saved as $output_filename in $output_directory/"
else
  echo "Failed to download HTML content from $url"
fi

# Move back to the parent directory
cd ..
