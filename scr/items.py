import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from datetime import datetime
import os

def extract_exotic_items(html_file):
    with open(html_file, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    root = ET.Element("XurInventory")
    
    # Find all <div class="et_pb_blurb_content"> elements
    item_containers = soup.find_all('div', class_='et_pb_blurb_content')

    for container in item_containers:
        # Within each container, find the item name and description
        item_name = container.find('h4', class_='et_pb_module_header').text.strip()
        item_description = container.find('div', class_='et_pb_blurb_description').text.strip()
        
        item_element = ET.SubElement(root, "ExoticItem")
        name_element = ET.SubElement(item_element, "Name")
        name_element.text = item_name
        description_element = ET.SubElement(item_element, "Description")
        description_element.text = item_description

    return ET.tostring(root, encoding='unicode')

if __name__ == "__main__":
    # Get the current date in MM-DD-YYYY format
    current_date = datetime.now().strftime("%m-%d-%Y")
    
    # Create the output directory based on the current date
    output_directory = os.path.join(os.getcwd(), current_date)
    os.makedirs(output_directory, exist_ok=True)

    # Change to the output directory
    os.chdir(output_directory)

    # Process "index.html" without requiring it as an argument
    exotic_items_xml = extract_exotic_items("index.html")

    xml_filename = f"{current_date}.xml"

    with open(xml_filename, 'w', encoding='utf-8') as xml_file:
        xml_file.write(exotic_items_xml)

    print(f"Exotic items saved as {xml_filename} in {output_directory}")

    # Change back to the parent directory
    os.chdir("..")
