# Section 1: webbrowser Module - Practice

# Q1: Import webbrowser module
# WHAT IT DOES: webbrowser module opens URLs in your web browser




# Q2: Use webbrowser.open() to open 'https://nostarch.com'
# WHAT IT DOES: webbrowser.open() launches a new browser tab to the specified URL
# ┌─ EXAMPLE ─────────────
# │ import webbrowser
# │ webbrowser.open('https://example.com')
# └───────────────────────




# Q3: Create variable named search_term with value 'Python programming', then use webbrowser.open() to open Google search for that term using URL 'https://www.google.com/search?q=' + search_term
# WHAT IT DOES: Opens a Google search by building the search URL with your search term
# ┌─ EXAMPLE ─────────────
# │ query = 'web scraping'
# │ webbrowser.open('https://www.google.com/search?q=' + query)
# └───────────────────────




# Q4: Create variable named street_address with value '123 Main St, Boston, MA', then use webbrowser.open() to open OpenStreetMap search using URL 'https://www.openstreetmap.org/search?query=' + street_address
# WHAT IT DOES: Opens OpenStreetMap to show the location of an address
# ┌─ EXAMPLE ─────────────
# │ location = '456 Oak Ave, Seattle, WA'
# │ webbrowser.open('https://www.openstreetmap.org/search?query=' + location)
# └───────────────────────




# Q5: Use webbrowser.open() with file:// prefix to open a local file at 'C:/Users/YourName/Documents/test.html'
# WHAT IT DOES: Opens a local HTML file from your hard drive in the browser using file:// scheme
# ┌─ EXAMPLE ─────────────
# │ webbrowser.open('file:///C:/Users/YourName/Desktop/info.html')
# └───────────────────────




