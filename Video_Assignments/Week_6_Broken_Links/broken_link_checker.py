import requests
from bs4 import BeautifulSoup

while True:
    url = input("Enter website URL (example: https://example.com): ")
    
    if url.startswith('http://') or url.startswith('https://'):
        try:
            response = requests.get(url, timeout=10)
            break
        except:
            print("Error: Could not connect to that URL. Try again.\n")
    else:
        print("Error: URL must start with http:// or https://\n")

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
broken_links = []
working_links = []
other_links = []

print(f"\nChecking {len(links)} links...\n")

for tag in links:
    link = tag.get('href')
    
    if link and link.startswith('http'):
        try:
            link_response = requests.get(link, timeout=5)
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
            broken_links.append(link)
            print(f"BROKEN (Connection Failed): {link}")

print(f"\n{'='*60}")
print(f"Total working links: {len(working_links)}")
print(f"Total broken links: {len(broken_links)}")
print(f"Total other links: {len(other_links)}")
print(f"{'='*60}")












#https://www.python.org