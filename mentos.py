import os
import xml.etree.ElementTree as ET
from datetime import datetime

# Define the date format
date_format = "%m-%d-%Y"

# Get today's date in the specified format
current_date = datetime.now().strftime(date_format)

# Create the folder path based on today's date
folder_path = os.path.join(os.getcwd(), current_date)

# Check if the folder exists
if os.path.exists(folder_path):
    xml_file_path = os.path.join(folder_path, "inventory.xml")

    # Check if "inventory.xml" exists in the folder
    if os.path.exists(xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Create a message to save to "inventory.txt"
        message = ""

        # Iterate through the ExoticItem elements
        for item in root.findall('.//ExoticItem'):
            item_name = item.find('Name').text
            item_description = item.find('Description').text

            message += f"Name: {item_name}\n"
            message += f"Description: {item_description}\n\n"

        # Get Xur's location
        xur_location = root.find('.//Location').text

        # Append the location to the message
        message = f"{message}\nLocation: {xur_location}\n"

        # Save the output to "inventory.txt"
        txt_file_path = os.path.join(folder_path, "inventory.txt")
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(message)

        print(f"Inventory details saved as 'inventory.txt' in the folder for {current_date}")
    else:
        print(f"'inventory.xml' not found in the folder for {current_date}")
else:
    print(f"Folder for {current_date} not found.")

