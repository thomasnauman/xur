#!/bin/bash

required_libraries=("discord" "discord.py" "beautifulsoup4")

echo "This script will install Python3 and the following Python libraries:"
for library in "${required_libraries[@]}"; do
    echo "- $library"
done

read -p "Do you want to proceed with the installation? (y/n): " choice

if [[ $choice =~ ^[Yy]$ ]]; then
    # Install Python3
    sudo apt-get update
    sudo apt-get install -y python3

    for library in "${required_libraries[@]}"; do
        # Ensure Python library names are correct
        if [[ $library == "discord.py" ]]; then
            library="discord"
        fi

        pip install "$library"
        if [ $? -eq 0 ]; then
            echo "Successfully installed: $library"
        else
            echo "Error installing $library"
        fi
    done
else
    echo "Installation aborted."
fi
