import requests
from bs4 import BeautifulSoup

# Using the test page
url = "http://localhost:8000/test_page.html"

print(f"Checking: {url}\n")

try:
    response = requests.get(url, timeout=10)
    print(f"✓ Page loaded successfully\n")
except:
    print("ERROR: Could not connect. Make sure server is running:")
    print('Run: cd "Video_Assignments\\Week_6_Broken_Links"; python -m http.server 8000')
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a')
broken_links = []

print(f"Found {len(links)} links on the page")
print(f"Checking each link...\n")
print("="*70)

for tag in links:
    link = tag.get('href')
    
    if link and link.startswith('http'):
        try:
            link_response = requests.get(link, timeout=5)
            if link_response.status_code == 404:
                broken_links.append(link)
                print(f"❌ BROKEN (404): {link}")
            else:
                print(f"✅ WORKING ({link_response.status_code}): {link}")
        except Exception as e:
            print(f"⚠️  ERROR: {link}")

print("="*70)
print(f"\n📊 RESULTS:")
print(f"   Total links checked: {len(links)}")
print(f"   Working links: {len(links) - len(broken_links)}")
print(f"   Broken links (404): {len(broken_links)}")
