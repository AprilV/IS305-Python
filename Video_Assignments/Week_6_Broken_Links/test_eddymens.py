import requests
from bs4 import BeautifulSoup

url = "https://www.eddymens.com/blog/page-with-broken-pages-for-testing-53049e870421"

print(f"Testing: {url}\n")

try:
    response = requests.get(url, timeout=10)
    print(f"Page loaded: Status {response.status_code}\n")
except Exception as e:
    print(f"Error loading page: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

print(f"Found {len(links)} links\n")
print("="*60)

for tag in links[:20]:  # Check first 20
    link = tag.get('href')
    
    if link and link.startswith('http'):
        try:
            link_response = requests.get(link, timeout=5)
            print(f"{link_response.status_code}: {link}")
        except Exception as e:
            print(f"ERROR: {link} - {str(e)[:40]}")
