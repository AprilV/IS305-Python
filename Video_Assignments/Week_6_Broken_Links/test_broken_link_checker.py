import requests
from bs4 import BeautifulSoup

# Test with httpbin.org which has a known 404 endpoint
url = "https://httpbin.org/links/10/0"

print(f"Testing with: {url}\n")

response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
broken_links = []

print(f"Checking {len(links)} links...\n")

for tag in links:
    link = tag.get('href')
    
    if link and link.startswith('http'):
        try:
            link_response = requests.get(link, timeout=5)
            if link_response.status_code == 404:
                broken_links.append(link)
                print(f"BROKEN: {link}")
            else:
                print(f"OK: {link} (Status: {link_response.status_code})")
        except Exception as e:
            print(f"ERROR: {link} - {e}")

print(f"\nTotal broken links: {len(broken_links)}")

# Now test with a page that SHOULD have a 404
print("\n" + "="*60)
print("Testing direct 404 link...")
print("="*60 + "\n")

test_404 = "https://httpbin.org/status/404"
try:
    response = requests.get(test_404, timeout=5)
    print(f"URL: {test_404}")
    print(f"Status code: {response.status_code}")
    if response.status_code == 404:
        print("✓ Successfully detected 404!")
    else:
        print(f"✗ Expected 404 but got {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")
