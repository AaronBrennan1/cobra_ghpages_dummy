import sys
from bs4 import BeautifulSoup

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

if __name__ == "__main__":
    main()
