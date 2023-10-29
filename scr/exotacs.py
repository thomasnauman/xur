import argparse
from bs4 import BeautifulSoup
import os
from datetime import datetime

def extract_exotic_items(html_file):
    with open(html_file, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    exotic_items = []
    item_containers = soup.find_all('div', class_='et_pb_column_1_5 et_pb_column')

    for container in item_containers:
        item_name = container.find('h4', class_='et_pb_module_header').text.strip()
        item_description = container.find('div', class_='et_pb_blurb_description').text.strip()
        exotic_items.append({
            'name': item_name,
            'description': item_description
        })

    return exotic_items

if __name__ == "__main__":
    # Get the current date in MM-DD-YYYY format
    current_date = datetime.now().strftime("%m-%d-%Y")
    
    # Create the output directory based on the current date
    output_directory = os.path.join(os.getcwd(), current_date)
    os.makedirs(output_directory, exist_ok=True)

    # Change to the output directory
    os.chdir(output_directory)

    # Process the XML file with today's date as an argument
    xml_file = f"{current_date}.xml"

    exotic_items = extract_exotic_items(xml_file)

    for item in exotic_items:
        print(f"Name: {item['name']}")
        print(f"Description: {item['description']}")
        print()

    # Change back to the parent directory
    os.chdir("..")
