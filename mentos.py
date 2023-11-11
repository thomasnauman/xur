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

        # Get Xur's location
        xur_location = root.find('.//Location').text

        # Define keywords for different locations
        location_keywords = {
            'Nessus': 'Hello Guardians! Today, Xûr is on Nessus at Watchers Grave.',
            'EDZ': 'Hello Guardians! Today, Xûr is on the EDZ at Winding Cove.',
            'Tower': 'Hello Guardians Today, Xûr is at the Tower in the Hangar.'
            # Add more locations and custom messages as needed
        }

        # Check if any keyword exists in the Xur location
        matched_keywords = [keyword for keyword in location_keywords if keyword.lower() in xur_location.lower()]

        if matched_keywords:
            # Take the first matched keyword
            matched_keyword = matched_keywords[0]
            custom_message = location_keywords[matched_keyword]

            # Create a message with the specified format
            message = f"{custom_message}\n\nHere is what he is selling:\n\n"

            # Initialize armor_type as "Exotic" by default
            armor_type = "Exotic"

            # Iterate through the ExoticItem elements
            exotic_items = root.findall('.//ExoticItem')
            for i, item in enumerate(exotic_items):
                item_name = item.find('Name').text
                item_description = item.find('Description').text

                # Determine armor type based on index
                if i == 1:
                    armor_type = "Hunter"
                elif i == 2:
                    armor_type = "Titan"
                elif i == 3:
                    armor_type = "Warlock"
                else:
                    armor_type = "Exotic"

                # Exclude the armor type for the first item (index 0)
                if i == 0:
                    armor_type = ""

                # Split the item_description into words
                description_words = item_description.split()

                # Insert the armor type as the second word
                description_words.insert(1, armor_type)

                # Recreate the item_description
                new_description = ' '.join(description_words)

                message += f"{item_name}\n{new_description}\n\n"

            # Save the output to "inventory.txt"
            txt_file_path = os.path.join(folder_path, "inventory.txt")
            with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(message)

            print(f"Inventory details saved as 'inventory.txt' in the folder for {current_date}")
        else:
            print(f"No recognized location keywords found in '{xur_location}'.")
    else:
        print(f"'inventory.xml' not found in the folder for {current_date}")
else:
    print(f"Folder for {current_date} not found.")
