import requests
from bs4 import BeautifulSoup

url = "http://localhost:8000/test_page.html"

print(f"Testing broken link checker with: {url}\n")

try:
    response = requests.get(url, timeout=10)
    print(f"✓ Successfully loaded test page\n")
except:
    print("✗ Could not connect to test page. Is the server running?")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
broken_links = []

print(f"Found {len(links)} links to check\n")
print("="*60)

for tag in links:
    link = tag.get('href')
    
    if link and link.startswith('http'):
        try:
            link_response = requests.get(link, timeout=5)
            if link_response.status_code == 404:
                broken_links.append(link)
                print(f"✗ BROKEN (404): {link}")
            else:
                print(f"✓ OK ({link_response.status_code}): {link}")
        except Exception as e:
            print(f"⚠ ERROR: {link} - {str(e)[:50]}")

print("="*60)
print(f"\n✓ TEST COMPLETE")
print(f"Total broken links found: {len(broken_links)}")
print(f"Expected: 2 broken links")

if len(broken_links) == 2:
    print("\n✓✓✓ SUCCESS! The broken link checker works correctly! ✓✓✓")
else:
    print(f"\n✗ PROBLEM: Found {len(broken_links)} but expected 2")
