import xml.etree.ElementTree as ET
import os
from datetime import datetime

# Get the current working directory before changing it
original_directory = os.getcwd()

# Get the current date in MM-DD-YYYY format
current_date = datetime.now().strftime("%m-%d-%Y")  # Keep MM-DD-YYYY format
folder_name = os.path.join(os.getcwd(), current_date)

# Construct the path to the XML file
xml_file_path = os.path.join(folder_name, "inventory.xml")

# Check if the folder and XML file exist
if os.path.exists(folder_name) and os.path.exists(xml_file_path):
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find the location element
    location_element = root.find('.//Location')
    if location_element is not None:
        location = location_element.text.strip()

        # Define keywords for different locations
        location_keywords = {
            'Nessus': 'https://cdn.discordapp.com/attachments/738810722875736195/1061128350455836672/Nessus.png?ex=654ef8c9&is=653c83c9&hm=d3de711dedb82982abe79fccc97a40091edbe74f0721498df3b27135ca53da82&',
            'EDZ': 'https://cdn.discordapp.com/attachments/738810722875736195/1066053966514880552/EDZ.jpg?ex=654e6f1f&is=653bfa1f&hm=ae8205147bc023e0cd4fe1a9d567cc645b2206eba4529cccfe1c76572c63c77c&',
            'Tower': 'https://cdn.discordapp.com/attachments/738810722875736195/1064697385994956891/Tower-Hanger.jpg?ex=65497fb5&is=65370ab5&hm=eed350910d1d13914a4380cb0fc9ba2a9f76cd3b37c471e83b0e846829657d44&'
        }

        # Check if any keyword exists in the location
        matched_keywords = [keyword for keyword in location_keywords if keyword.lower() in location.lower()]

        if matched_keywords:
            # Take the first matched keyword
            matched_keyword = matched_keywords[0]
            location_phrase = location_keywords[matched_keyword]

            # Export location_phrase to location.txt
            location_txt_file = os.path.join(folder_name, "location.txt")
            with open(location_txt_file, "w", encoding="utf-8") as txt_file:
                txt_file.write(location_phrase)

            print(f"Location phrase for '{matched_keyword}' saved as location.txt in {folder_name}")
        else:
            print(f"No recognized location keywords found in '{location}'.")
    else:
        print("Location not found in the XML file.")
else:
    print("Folder or XML file not found for the current date.")

# Change back to the original working directory
os.chdir(original_directory)
