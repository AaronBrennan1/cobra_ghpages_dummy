import sys
import os
from bs4 import BeautifulSoup
import shutil

def main():
    # Get file path from command line argument
    file_path = sys.argv[1]

    # Open the file and parse it with Beautiful Soup
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Print the file location
    print(f"File Location: {file_path}")

    # Find the h1 span tag and print its contents
    heading = soup.find('h1').find('span').text
    print(f"Heading: {heading}")

    # Compute the new file location by removing the first two directories
    new_file_location = '/'.join(file_path.split('/')[2:])
    print(f"New File Location: {new_file_location}")

    # Read the HOLDER_TEMPLATE.html file
    with open('stable/tutorials/HOLDER_TEMPLATE.html', 'r') as template_file:
        template = template_file.read()

    # Replace the placeholder string with the new file location
    template = template.replace('IFRAMETUTORIAL.html', new_file_location)

    # Create a new file with the same name as the changed file in the stable/tutorials directory
    new_file_name = file_path.split('/')[-1]
    new_file_path = f'stable/tutorials/{new_file_name}'

    # Write the modified template to the new file
    with open(new_file_path, 'w') as new_file:
        new_file.write(template)

    print(f"Created new file: {new_file_path}")

if __name__ == "__main__":
    main()
