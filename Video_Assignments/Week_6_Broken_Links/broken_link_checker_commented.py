# Import the requests module to download web pages
import requests
# Import BeautifulSoup to parse HTML
from bs4 import BeautifulSoup

# Keep asking for URL until we get a valid one that connects
while True:
    url = input("Enter website URL (example: https://example.com): ")
    
    # Check if URL starts with http:// or https://
    if url.startswith('http://') or url.startswith('https://'):
        try:
            # Try to download the page
            response = requests.get(url, timeout=10)
            break
        except:
            print("Error: Could not connect to that URL. Try again.\n")
    else:
        print("Error: URL must start with http:// or https://\n")

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <a> anchor tags (which contain links)
links = soup.find_all('a')
# Create empty list to store broken links
broken_links = []
# Create empty list to store working links
working_links = []
# Create empty list to store other status code links
other_links = []

print(f"\nChecking {len(links)} links...\n")

# Loop through each link tag
for tag in links:
    # Get the href attribute (the actual URL)
    link = tag.get('href')
    
    # Only check if link exists and starts with http
    if link and link.startswith('http'):
        try:
            # Try to download the link
            link_response = requests.get(link, timeout=5)
            # Check the status code
            if link_response.status_code == 404:
                broken_links.append(link)
                print(f"BROKEN (404): {link}")
            elif link_response.status_code == 200:
                working_links.append(link)
                print(f"WORKING (200): {link}")
            else:
                other_links.append(link)
                print(f"OTHER ({link_response.status_code}): {link}")
        except:
            # Connection failed (timeout, unreachable, etc.) - also a broken link
            broken_links.append(link)
            print(f"BROKEN (Connection Failed): {link}")

# Print the results with separators
print(f"\n{'='*60}")
print(f"Total working links: {len(working_links)}")
print(f"Total broken links: {len(broken_links)}")
print(f"Total other links: {len(other_links)}")
print(f"{'='*60}")

