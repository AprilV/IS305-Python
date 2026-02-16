# Section 3: Beautiful Soup - Practice

# Q1: First install Beautiful Soup by running this in terminal: python -m pip install beautifulsoup4
# Then import requests and bs4 modules
# WHAT IT DOES: requests downloads pages; bs4 (Beautiful Soup) parses HTML to extract data
import requests
import bs4



# Q2: Use requests.get() to download 'https://autbor.com/example3.html' and store in variable named res, then call raise_for_status()
# WHAT IT DOES: Downloads the example HTML page we'll parse with Beautiful Soup
# ┌─ EXAMPLE ─────────────
# │
# │ page = requests.get('https://nostarch.com')
# │ page.raise_for_status()
# └───────────────────────
res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()



# Q3: Create variable named soup using bs4.BeautifulSoup() with res.text and 'html.parser' as arguments
# WHAT IT DOES: BeautifulSoup() creates an object that can search and extract HTML elements
# ┌─ EXAMPLE ─────────────
# │ parsed = bs4.BeautifulSoup(page.text, 'html.parser')
# └───────────────────────

soup = bs4.BeautifulSoup(res.text, 'html.parser')



# Q4: Use soup.select() with '#author' to find element with id="author" and store in variable named author_elem, then print str() of author_elem[0]
# WHAT IT DOES: select() finds elements using CSS selectors; # symbol finds by id attribute
# ┌─ EXAMPLE ─────────────
# │ title_elem = soup.select('#main')
# │ print(str(title_elem[0]))
# └───────────────────────
author_elem = soup.select('#author')
print(str(author_elem[0]))



# Q5: Call get_text() on author_elem[0] and print the result
# WHAT IT DOES: get_text() extracts just the text content between HTML tags, removing the tags themselves
# ┌─ EXAMPLE ─────────────
# │ content = title_elem[0].get_text()
# │ print(content)
# └───────────────────────
content = author_elem[0].get_text()
print(content)



# Q6: Print author_elem[0].attrs to see the element's attributes
# WHAT IT DOES: attrs attribute contains a dictionary of all HTML attributes (like id, class, href)
# ┌─ EXAMPLE ─────────────
# │ print(title_elem[0].attrs)
# └───────────────────────
print(author_elem[0].attrs)



# Q7: Use soup.select() with 'p' to find all paragraph elements and store in variable named paragraphs, then print len() of paragraphs
# WHAT IT DOES: Selecting by tag name (like 'p') finds all elements with that tag
# ┌─ EXAMPLE ─────────────
# │ headers = soup.select('h1')
# │ print(len(headers))
# └───────────────────────
paragraphs = soup.select('p')
print(len(paragraphs))



# Q8: Use a for loop with variable name p to iterate through paragraphs list, and print p.get_text() for each element
# WHAT IT DOES: Loops through list of elements to extract text from each one
# ┌─ EXAMPLE ─────────────
# │ for header in headers:
# │     print(header.get_text())
# └───────────────────────

for p in paragraphs:
    print(p.get_text())



# Q9: Use soup.select() with 'a' to find all link elements, store in variable named links, then print get() with 'href' argument for links[0]
# WHAT IT DOES: get() method retrieves specific attribute values; 'href' contains the URL in link elements
# ┌─ EXAMPLE ─────────────
# │ images = soup.select('img')
# │ print(images[0].get('src'))
# └───────────────────────
links = soup.select('a')
print(links[0].get('href'))



# Q10: Use soup.select() with '.slogan' to find elements with class="slogan" and print get_text() of the first result
# WHAT IT DOES: . symbol finds elements by CSS class attribute
# ┌─ EXAMPLE ─────────────
# │ warnings = soup.select('.notice')
# │ print(warnings[0].get_text())
# └───────────────────────
slogan = soup.select('.slogan')
print(slogan[0].get_text())


