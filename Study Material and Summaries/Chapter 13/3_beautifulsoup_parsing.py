# Section 3: Beautiful Soup - Reference Examples

import requests
import bs4

# Download and parse a page
res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find element by ID
elems = soup.select('#author')
print(str(elems[0]))
print(elems[0].get_text())
print(elems[0].attrs)

# Find all paragraphs
p_elems = soup.select('p')
print(str(p_elems[0]))
print(p_elems[0].get_text())

# Find all links
link_elems = soup.select('a')
for link in link_elems:
    print(link.get('href'))

# Find by class
slogan_elems = soup.select('.slogan')
print(slogan_elems[0].get_text())

# Load from local file
with open('example.html') as file:
    soup = bs4.BeautifulSoup(file, 'html.parser')
    print(soup.select('p')[0].get_text())
