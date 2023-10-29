import os
from bs4 import BeautifulSoup
from datetime import datetime

def extract_xur_location(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    location_element = soup.find('h4', class_='title')
    
    if location_element:
        location = location_element.text.strip()
        return location
    else:
        return "Xur's location not found on the page."

if __name__ == "__main__":
    # Get the current date in MM-DD-YYYY format
    current_date = datetime.now().strftime("%m-%d-%Y")
    
    # Create the output directory based on the current date
    output_directory = os.path.join(os.getcwd(), current_date)
    os.makedirs(output_directory, exist_ok=True)

    # Change to the output directory
    os.chdir(output_directory)

    # Try to read the "index.html" file in the current date directory
    html_file_path = os.path.join(output_directory, "index.html")

    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        xur_location = extract_xur_location(html_content)

        if xur_location:
            print(f"Xur's location: {xur_location}")
        else:
            print("Xur's location not found on the page.")
    else:
        print(f"index.html not found in the {current_date} directory.")

    # Change back to the parent directory
    os.chdir("..")

