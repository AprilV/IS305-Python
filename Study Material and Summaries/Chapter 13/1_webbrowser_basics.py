# Section 1: webbrowser Module - Reference Examples

import webbrowser

# Opening a website in the browser
webbrowser.open('https://inventwithpython.com/')

# Opening a search on OpenStreetMap
address = '1600 Pennsylvania Ave NW, Washington, DC 20500'
webbrowser.open('https://www.openstreetmap.org/search?query=' + address)

# Opening multiple sites
sites = ['https://python.org', 'https://nostarch.com', 'https://github.com']
for site in sites:
    webbrowser.open(site)

# Opening a local HTML file
webbrowser.open('file:///C:/Users/YourName/Desktop/help.html')
