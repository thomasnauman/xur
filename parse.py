import os
from bs4 import BeautifulSoup
from datetime import datetime
import xml.etree.ElementTree as ET

def extract_xur_location(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    location_element = soup.find('h4', class_='title')

    if location_element:
        location = location_element.text.strip()
        return location
    else:
        return "Xur's location not found on the page."

def extract_exotic_items(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    root = ET.Element("XurInventory")

    item_containers = soup.find_all('div', class_='et_pb_blurb_content')

    for container in item_containers:
        item_name = container.find('h4', class_='et_pb_module_header').text.strip()
        
        # Check if the item_name is "Hawkmoon" and skip it
        if item_name.lower() == "hawkmoon":
            continue

        item_description = container.find('div', class_='et_pb_blurb_description').text.strip()

        item_element = ET.SubElement(root, "ExoticItem")
        name_element = ET.SubElement(item_element, "Name")
        name_element.text = item_name
        description_element = ET.SubElement(item_element, "Description")
        description_element.text = item_description

    return root

if __name__ == "__main__":
    current_date = datetime.now().strftime("%m-%d-%Y")
    output_directory = os.path.join(os.getcwd(), current_date)
    os.makedirs(output_directory, exist_ok=True)
    os.chdir(output_directory)

    html_file_path = os.path.join(output_directory, "index.html")

    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        xur_location = extract_xur_location(html_content)

        if xur_location:
            print(f"Xur's location: {xur_location}")
        else:
            print("Xur's location not found on the page.")

        exotic_items_root = extract_exotic_items(html_content)

        # Change the XML filename to "inventory.xml"
        xml_filename = "inventory.xml"

        # Create the final XML tree containing both the location and inventory
        final_xml = ET.Element("XurData")
        final_xml.append(exotic_items_root)

        xur_location_element = ET.Element("Location")
        xur_location_element.text = xur_location
        final_xml.append(xur_location_element)

        tree = ET.ElementTree(final_xml)
        tree.write(xml_filename, encoding="utf-8", xml_declaration=True)

        print(f"Xur's location and exotic items saved as {xml_filename} in {output_directory}")
    else:
        print(f"index.html not found in the {current_date} directory.")

    os.chdir("..")
