===============================================================================
IS 305 - CHAPTER 13: WEB SCRAPING - COMPLETE STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: February 15, 2026

===============================================================================
CHAPTER OVERVIEW
===============================================================================

WHY THIS CHAPTER MATTERS:

Web scraping is the process of using a program to download and process content
from the web. This chapter teaches you to automate web tasks that would be
tedious or time-consuming to do manually, such as:

- Downloading files and web pages from the internet
- Extracting specific information from HTML
- Automatically filling out forms
- Clicking links and navigating websites
- Accessing weather APIs and other online services
- Automating repetitive web-based tasks

Much of modern computer work happens on the internet. Learning to programmatically
interact with websites extends your automation capabilities beyond your local
computer to the entire web.

MODULES COVERED IN THIS CHAPTER:

1. webbrowser - Opens a browser to a specific page (comes with Python)
2. requests - Downloads files and web pages from the internet
3. Beautiful Soup (bs4) - Parses HTML to extract information
4. Selenium - Launches and controls a web browser (fills forms, clicks)
5. Playwright - Newer browser automation with additional features

===============================================================================
HTTP AND HTTPS - THE WEB'S PROTOCOL
===============================================================================

CONCEPT: HTTP (HyperText Transfer Protocol) and HTTPS (secure version) are how
your web browser communicates with web servers.

WHAT IS A URL?

A URL (Uniform Resource Locator) is a web address like:
https://autbor.com/example3.html

URL STRUCTURE BREAKDOWN:

https://          - Scheme (protocol name + ://)
autbor.com       - Domain name of the web server
/example3.html   - Path to the specific page

HTTPS vs HTTP:

HTTP:  Unencrypted - others can view your traffic
HTTPS: Encrypted - protects your privacy

WHY HTTPS MATTERS:

- Without encryption, identity thieves, intelligence agencies, and ISPs can see:
  * What websites you visit
  * Passwords you enter
  * Credit card information you submit
  * Content of web pages you view

- With HTTPS, content is encrypted and hidden
- However, the identity of the website can still be known
  * Others know you visited CatPhotos.com
  * But they can't see WHICH cat photos you viewed

IMPORTANT NOTES:

- Most modern websites use HTTPS for all pages
- Older sites used HTTPS only for login/payment pages
- Even with HTTPS, website identity is visible (not content)
- For true anonymity, use Tor Browser from https://www.torproject.org/download/

===============================================================================
MODULE 1: WEBBROWSER - OPENING URLS IN THE BROWSER
===============================================================================

CONCEPT: The webbrowser module opens your web browser to a specified URL.
This is useful for automating the step of manually typing URLs or clicking
bookmarks.

IMPORTING THE MODULE:

import webbrowser

PRIMARY FUNCTION - webbrowser.open():

SYNTAX: webbrowser.open(url)

WHAT IT DOES:
- Launches a new browser tab
- Navigates to the specified URL
- Returns immediately (doesn't wait for browser to close)

EXAMPLE 1: Open a Website

import webbrowser
webbrowser.open('https://inventwithpython.com/')

RESULT: Browser opens a new tab to https://inventwithpython.com

PRACTICAL USE CASE - MAP LAUNCHER PROJECT:

PROBLEM: Copying addresses to OpenStreetMap is tedious
SOLUTION: Script that opens map automatically from clipboard/command line

HOW IT WORKS:

1. Get street address from command line arguments OR clipboard
2. Build OpenStreetMap URL with the address
3. Call webbrowser.open() to launch the map

URL STRUCTURE FOR OPENSTREETMAP:

https://www.openstreetmap.org/search?query=<ADDRESS_HERE>

EXAMPLE: For "777 Valencia St, San Francisco, CA 94110"
URL becomes: https://www.openstreetmap.org/search?query=777%20Valencia%20St%2C%20San%20Francisco%2C%20CA%2094110

NOTE: Browser automatically handles URL encoding (spaces become %20)

CODE PATTERN - COMMAND LINE ARGUMENTS:

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.openstreetmap.org/search?query=' + address)

HOW IT WORKS:

- sys.argv is a list of command line arguments
- sys.argv[0] is the program name
- sys.argv[1:] are the actual arguments
- ' '.join() combines them into a single string
- If no arguments, use clipboard instead

USAGE COMPARISON:

MANUAL PROCESS:
1. Highlight address
2. Copy address
3. Open web browser
4. Go to OpenStreetMap
5. Click search field
6. Paste address
7. Press ENTER

WITH SCRIPT:
1. Highlight address
2. Copy address
3. Run script

OTHER USES FOR webbrowser MODULE:

- Open all links on a page in separate tabs
- Open local weather website
- Open multiple social networking sites you check daily
- Open local .html help files on your hard drive

OPENING LOCAL FILES:

Use file:// prefix instead of https://

WINDOWS: file:///C:/Users/al/Desktop/help.html
MACOS: file:///Users/al/Desktop/help.html

===============================================================================
MODULE 2: REQUESTS - DOWNLOADING FROM THE WEB
===============================================================================

CONCEPT: The requests module downloads files and web pages from the internet
without worrying about network errors, connection routing, or data compression.

INSTALLATION:

This module doesn't come with Python. Install it with:
pip install requests

IMPORTING THE MODULE:

import requests

PRIMARY FUNCTION - requests.get():

SYNTAX: response = requests.get(url)

WHAT IT DOES:
- Downloads content from the specified URL
- Returns a Response object
- Handles network complexities automatically

EXAMPLE 1: Download a Web Page

import requests
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(response)  # <class 'requests.models.Response'>

RESPONSE OBJECT ATTRIBUTES:

response.status_code  - HTTP status code (200 means OK)
response.text         - Downloaded content as a string
response.content      - Downloaded content as bytes

CHECKING FOR SUCCESS:

METHOD 1 - Check status_code:

response.status_code == requests.codes.ok  # Returns True if successful

EXPLANATION:
- HTTP status code 200 means "OK" (successful)
- HTTP status code 404 means "Not Found"
- requests.codes.ok is a constant equal to 200

METHOD 2 - Use raise_for_status():

response.raise_for_status()

WHAT IT DOES:
- Raises an exception if download failed
- Does nothing if download succeeded
- ALWAYS use this after requests.get()

EXAMPLE 2: Error Handling

import requests

response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

OUTPUT:
There was a problem: 404 Client Error: Not Found for url:
https://inventwithpython.com/page_that_does_not_exist.html

WHY raise_for_status() IS IMPORTANT:

- Ensures download actually worked before continuing
- Without it, program continues with bad/empty data
- With it, program stops immediately if download fails

BEST PRACTICE:

ALWAYS call raise_for_status() immediately after requests.get()

SAVING DOWNLOADED FILES TO HARD DRIVE:

REQUIREMENT: Must open file in write binary mode ('wb')

WHY BINARY MODE:
- Maintains Unicode encoding of text
- Even for plaintext, write as binary to preserve encoding
- Prevents corruption of downloaded content

PROCESS FOR SAVING FILES:

1. Call requests.get() to download
2. Call raise_for_status() to check success
3. Open file in 'wb' (write binary) mode
4. Loop over response.iter_content()
5. Write each chunk to file

EXAMPLE 3: Download and Save Romeo and Juliet

import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as play_file:
    for chunk in response.iter_content(100000):
        play_file.write(chunk)

HOW iter_content() WORKS:

response.iter_content(100000)

WHAT IT DOES:
- Returns chunks of content on each iteration
- Each chunk is bytes data type
- Argument specifies bytes per chunk (100000 is good default)
- Prevents loading entire file into memory at once

EXAMPLE OUTPUT:

100000  # First chunk (100,000 bytes written)
78978   # Second chunk (remaining 78,978 bytes written)

DOWNLOAD AND SAVE REVIEW (THE COMPLETE PROCESS):

import requests

# Step 1: Download the file
response = requests.get(url)

# Step 2: Check for errors
response.raise_for_status()

# Step 3: Open file in write binary mode
with open('filename.ext', 'wb') as file_obj:
    # Step 4: Loop over chunks
    for chunk in response.iter_content(100000):
        # Step 5: Write each chunk
        file_obj.write(chunk)

FOR VIDEO FILES:

Use the yt-dlp module (covered in Chapter 24) for downloading from:
- YouTube
- Facebook
- X (Twitter)
- Other video sites

===============================================================================
MODULE 3: APIS - ACCESSING ONLINE SERVICES
===============================================================================

CONCEPT: An API (Application Programming Interface) is how your Python program
can communicate with other software, such as web servers. APIs let you access
online services programmatically.

WHAT IS AN API?

API = Specification for how software communicates with other software

EXAMPLES OF WHAT APIs CAN DO:
- Post to social media accounts
- Download new photos
- Get weather information
- Retrieve stock prices
- Access database information

API KEYS:

WHAT IS AN API KEY?
- A password that identifies your account in API requests
- Almost all online services require API keys
- Even free APIs often require registration

WHY API KEYS EXIST:
- Track usage per account
- Enforce rate limits (e.g., 60 requests per minute)
- Identify you for billing (if using paid tier)

SECURITY WARNING:

- Keep API keys secret!
- Anyone with your key can make requests under your account
- Can exhaust your request limits
- Better practice: Read key from text file, not hardcoded in source

EXAMPLE - OPENWEATHER API:

FREE TIER LIMITS: 60 API requests per minute

API KEY EXAMPLE (FAKE): '30ee784a80d81480dab1749d33980112'

IMPORTANT: Don't use fake example keys - they won't work!

JSON RESPONSES:

CONCEPT: Most HTTP APIs return responses as large strings formatted in JSON

WHAT IS JSON?
- JavaScript Object Notation
- A data format that looks like Python dictionaries
- Stores lists, dictionaries, strings, numbers

CONVERTING JSON TO PYTHON:

import json
response_data = json.loads(response.text)

WHAT IT DOES:
- json.loads() converts JSON string to Python data structure
- Returns lists and dictionaries
- Now you can access data like response_data[0]['lat']

API ENDPOINTS:

ENDPOINT = The specific URL used to make an API request

EXAMPLE ENDPOINT STRUCTURE:

https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}

BREAKDOWN OF ENDPOINT URL:

https://                     - Scheme (protocol)
api.openweathermap.org      - Domain name of API server
/geo/1.0/direct             - Path of the API
?q=...&appid=...            - Query string (parameters)

QUERY STRING STRUCTURE:

?parameter1=value1&parameter2=value2

RULES:
- Starts with ?
- Parameter name and value separated by =
- Multiple parameters separated by &
- Think of parameters like function arguments

OPENWEATHER API - GETTING LATITUDE/LONGITUDE:

ENDPOINT:
https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}

EXAMPLE CODE:

import requests, json

city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
API_key = 'YOUR_REAL_API_KEY_HERE'

response = requests.get(f'https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}')

response_data = json.loads(response.text)
lat = response_data[0]['lat']
lon = response_data[0]['lon']

OUTPUT:
lat = 37.7790262
lon = -122.419906

OPENWEATHER API - GETTING CURRENT WEATHER:

ENDPOINT:
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}

EXAMPLE CODE:

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
response_data = json.loads(response.text)

temp_kelvin = response_data['main']['temp']
temp_celsius = round(temp_kelvin - 273.15, 1)
temp_fahrenheit = round(temp_kelvin * (9 / 5) - 459.67, 1)

KEY INFORMATION YOU CAN GET:

response_data['weather'][0]['main']         - 'Clear', 'Rain', 'Snow'
response_data['weather'][0]['description']  - 'light rain', 'extreme rain'
response_data['main']['temp']               - Temperature in Kelvin
response_data['main']['feels_like']         - Feels like temp in Kelvin
response_data['main']['humidity']           - Humidity percentage

TEMPERATURE CONVERSIONS:

Kelvin to Celsius:  celsius = kelvin - 273.15
Kelvin to Fahrenheit: fahrenheit = kelvin * (9/5) - 459.67

API VERSIONING:

WHY VERSION NUMBERS IN URLs?
- APIs change over time
- New features added
- Old versions deprecated
- Version in URL (like /geo/1.0/) prevents breaking old code

EXAMPLE: /data/2.5/weather means version 2.5 of weather API

BEST PRACTICE:
- When API updates, update your code's endpoint URL
- Check documentation for current version
- Old versions eventually stop working

EXPLORING OTHER APIS:

- https://weather.gov - US National Weather Service
- https://www.weatherapi.com - Alternative weather API
- Search https://pypi.org for third-party Python packages
- Third-party packages often make APIs easier to use

===============================================================================
HTML BASICS - UNDERSTANDING WEB PAGES
===============================================================================

CONCEPT: HTML (HyperText Markup Language) is the format web pages are written in.
CSS (Cascading Style Sheets) control the appearance of HTML elements.

WHAT IS HTML?

HTML = Plaintext file with .html extension containing tags and content

HTML TAGS:

STRUCTURE: <tagname>content</tagname>

COMPONENTS:
- Starting tag: <b>
- Content: Hello
- Closing tag: </b>
- Together = Element: <b>Hello</b>

EXAMPLE 1: Bold Text

<b>Hello</b>, world!

RENDERED IN BROWSER: **Hello**, world!

EXPLANATION:
- <b> tag makes text bold
- </b> tag ends the bold formatting
- Text between tags is affected
- Text outside tags is normal

HTML ATTRIBUTES:

CONCEPT: Extra properties inside the opening tag

SYNTAX: <tagname attribute="value">content</tagname>

EXAMPLE 2: Link Tag

<a href="https://inventwithpython.com">This text is a link</a>

BREAKDOWN:
- <a> = anchor tag (for links)
- href = attribute specifying the URL
- "https://inventwithpython.com" = attribute value
- Clicking "This text is a link" goes to that URL

THE ID ATTRIBUTE:

CONCEPT: Uniquely identifies an element in the page

EXAMPLE:
<span id="author">Al Sweigart</span>

WHY ID IS IMPORTANT:
- Used to find specific element in web scraping
- Must be unique on the page
- Easy to target with Beautiful Soup or Selenium

VIEWING PAGE SOURCE:

HOW TO VIEW:
- Right-click any web page
- Select "View Source" or "View page source"
- Shows the HTML your browser receives

WHY VIEW SOURCE?
- See HTML structure before scraping
- Find element tags and IDs
- Understand page layout
- No mastery needed - just enough to find data

BROWSER DEVELOPER TOOLS:

HOW TO OPEN:
- Press F12 in Firefox, Chrome, Edge
- Press F12 again to close

INSPECT ELEMENT FEATURE:

HOW TO USE:
1. Right-click any part of web page
2. Select "Inspect Element"
3. Developer Tools shows HTML for that part

WHY THIS IS USEFUL:
- Quickly find HTML for specific content
- See element's tags and attributes
- Essential for web scraping
- Helps identify CSS selectors

IMPORTANT WARNING - DON'T USE REGEX FOR HTML:

WHY NOT USE REGULAR EXPRESSIONS?

- HTML can be formatted many different ways
- Still valid HTML even with different formatting
- Regex becomes complex and error-prone
- Too many edge cases to handle

BETTER SOLUTION:
- Use Beautiful Soup module
- Purpose-built for parsing HTML
- Handles format variations automatically
- Less likely to have bugs

CSS SELECTORS:

CONCEPT: Patterns that specify which HTML elements to retrieve

COMMON PATTERNS:

'div'               - All <div> elements
'#author'           - Element with id="author"
'.notice'           - Elements with class="notice"
'div span'          - <span> inside <div>
'div > span'        - <span> directly inside <div>
'input[name]'       - <input> with name attribute
'input[type="button"]' - <input> with type="button"

COMBINING SELECTORS:

'p #author'  - Element with id="author" inside <p> tag

HOW TO GET CSS SELECTOR FROM BROWSER:

1. Open Developer Tools (F12)
2. Right-click element in inspector
3. Select "Copy" → "CSS Selector"
4. Use the copied string in your code

===============================================================================
MODULE 4: BEAUTIFUL SOUP - PARSING HTML
===============================================================================

CONCEPT: Beautiful Soup (bs4) extracts information from HTML pages. It parses
(analyzes and extracts parts of) HTML to get the data you need.

INSTALLATION:

pip install beautifulsoup4

IMPORTING:

import bs4

NOTE: Install with "beautifulsoup4" but import as "bs4"

CREATING A BEAUTIFULSOUP OBJECT:

FROM WEB PAGE:

import requests, bs4

res = requests.get('https://autbor.com/example3.html')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

FROM LOCAL FILE:

import bs4

with open('example3.html') as example_file:
    soup = bs4.BeautifulSoup(example_file, 'html.parser')

SYNTAX EXPLANATION:

bs4.BeautifulSoup(html_content, 'html.parser')

PARAMETERS:
- html_content: String of HTML or file object
- 'html.parser': Tells Beautiful Soup to parse HTML format

FINDING ELEMENTS WITH select():

CONCEPT: The select() method finds elements using CSS selectors

SYNTAX: elements_list = soup.select('css_selector')

RETURNS: List of Tag objects (even if only one match)

COMMON CSS SELECTORS:

soup.select('div')              # All <div> elements
soup.select('#author')          # id="author"
soup.select('.notice')          # class="notice"
soup.select('div span')         # <span> inside <div>
soup.select('div > span')       # <span> directly in <div>
soup.select('input[name]')      # <input> with name attribute
soup.select('input[type="button"]')  # <input> type="button"

EXAMPLE 1: Finding Element by ID

import bs4
soup = bs4.BeautifulSoup(open('example3.html'), 'html.parser')
elems = soup.select('#author')

type(elems)      # <class 'bs4.element.ResultSet'>
len(elems)       # 1
type(elems[0])   # <class 'bs4.element.Tag'>

EXPLANATION:
- select() returns a ResultSet (list-like)
- Even one match returns a list
- Individual items are Tag objects

TAG OBJECT METHODS:

str(tag)         - HTML as a string
tag.get_text()   - Just the text content
tag.attrs        - Dictionary of attributes

EXAMPLE 2: Getting Text from Element

elems = soup.select('#author')
str(elems[0])       # '<span id="author">Al Sweigart</span>'
elems[0].get_text() # 'Al Sweigart'
elems[0].attrs      # {'id': 'author'}

EXAMPLE 3: Finding All Paragraphs

p_elems = soup.select('p')

str(p_elems[0])
# '<p>This <p> tag puts <b>content</b> into a <i>single</i> paragraph.</p>'

p_elems[0].get_text()
# 'This <p> tag puts content into a single paragraph.'

str(p_elems[1])
# '<p> <a href="https://inventwithpython.com/">This text is a link</a> to books by <span id="author">Al Sweigart</span>.</p>'

p_elems[1].get_text()
# 'This text is a link to books by Al Sweigart.'

GETTING ATTRIBUTE VALUES:

METHOD: tag.get('attribute_name')

RETURNS: Attribute value as string, or None if doesn't exist

EXAMPLE 4: Getting href from Link

span_elem = soup.select('span')[0]
str(span_elem)          # '<span id="author">Al Sweigart</span>'
span_elem.get('id')     # 'author'
span_elem.get('nonexistent_attr') == None  # True
span_elem.attrs         # {'id': 'author'}

PRACTICAL EXAMPLE - FINDING SPECIFIC DATA:

GOAL: Find weather forecast text on weather.gov

PROCESS:
1. Use browser Developer Tools to inspect element
2. Find CSS class or ID of forecast element
3. Use select() with that selector

EXAMPLE HTML:
<div class="col-sm-10 forecast-text">Sunny, with a high near 64.</div>

CODE:
elems = soup.select('.forecast-text')
forecast = elems[0].get_text()
# 'Sunny, with a high near 64.'

===============================================================================
MODULE 5: SELENIUM - CONTROLLING THE BROWSER
===============================================================================

CONCEPT: Selenium lets Python directly control the browser, clicking links
and filling forms like a human user. More advanced than requests + Beautiful
Soup, but slower because it launches actual browser.

WHEN TO USE SELENIUM:

USE SELENIUM WHEN:
- Need to interact with JavaScript-powered pages
- Need to log in to websites
- Need to fill out forms
- Need to click buttons/links
- Page content loads dynamically

USE REQUESTS + BEAUTIFUL SOUP WHEN:
- Just downloading static pages
- No forms or interaction needed
- Want faster, background execution

WHY SELENIUM OVER REQUESTS:

- Many e-commerce sites detect and block scrapers
- Selenium looks like real browser to websites
- Has same user-agent string as regular browser
- Downloads images, ads, cookies like real browser
- Still can be detected, but less likely

INSTALLATION:

pip install selenium

IMPORTING:

from selenium import webdriver

NOTE: Not "import selenium", use "from selenium import webdriver"

STARTING SELENIUM-CONTROLLED BROWSER:

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)  # <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('https://inventwithpython.com')

WHAT HAPPENS:
- Firefox browser window opens
- Navigates to specified URL
- Returns WebDriver object

IF YOU GET GECKODRIVER ERROR:

Error: "geckodriver executable needs to be in PATH"
Solution: Manually download Firefox web driver OR use webdriver-manager package

ALTERNATIVE: Use webdriver-manager package from https://pypi.org/project/webdriver-manager/

BROWSER BUTTON METHODS:

browser.back()      # Clicks Back button
browser.forward()   # Clicks Forward button
browser.refresh()   # Clicks Refresh button
browser.quit()      # Clicks Close Window button

FINDING ELEMENTS - THE By OBJECT:

FIRST, IMPORT:

from selenium.webdriver.common.by import By

FIND METHODS:

browser.find_element(By.CONSTANT, 'value')   # Returns single WebElement
browser.find_elements(By.CONSTANT, 'value')  # Returns list of WebElements

BY CONSTANTS:

By.CLASS_NAME           # CSS class name
By.CSS_SELECTOR         # CSS selector
By.ID                   # id attribute
By.LINK_TEXT            # <a> text (exact match)
By.PARTIAL_LINK_TEXT    # <a> text (partial match)
By.NAME                 # name attribute
By.TAG_NAME             # Tag name like 'a' or 'div'

EXAMPLE 1: Finding Elements

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')

ERROR HANDLING:

If element not found: Selenium raises NoSuchElement exception

BEST PRACTICE: Use try/except to handle missing elements

try:
    elem = browser.find_element(By.ID, 'nonexistent')
except Exception as exc:
    print(f'Element not found: {exc}')

WEBELEMENT ATTRIBUTES AND METHODS:

tag_name                 # Tag name like 'a'
get_attribute(name)      # Attribute value (like 'href')
get_property(name)       # Property value (like 'innerHTML')
text                     # Text content inside element
clear()                  # Clear text in text field
is_displayed()           # True if visible
is_enabled()             # True if enabled
is_selected()            # True if checkbox/radio selected
location                 # Dictionary with 'x' and 'y' position
size                     # Dictionary with 'width' and 'height'

EXAMPLE 2: Getting Text and Properties

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
elems = browser.find_elements(By.CSS_SELECTOR, 'p')

print(elems[0].text)
# 'This <p> tag puts content into a single paragraph.'

print(elems[0].get_property('innerHTML'))
# 'This <p> tag puts <b>content</b> into a <i>single</i> paragraph.'

CLICKING ELEMENTS:

METHOD: element.click()

WHAT IT DOES:
- Simulates mouse click on element
- Follows links
- Clicks buttons
- Selects radio buttons/checkboxes

EXAMPLE 3: Clicking a Link

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')
link_elem = browser.find_element(By.LINK_TEXT, 'This text is a link')
link_elem.click()  # Follows the link

FILLING OUT FORMS:

METHOD: element.send_keys('text')

WHAT IT DOES:
- Types text into <input> or <textarea> fields
- Simulates keyboard typing

METHOD: element.submit()

WHAT IT DOES:
- Submits the form containing the element
- Same as clicking Submit button

EXAMPLE 4: Logging In

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://autbor.com/example3.html')

user_elem = browser.find_element(By.ID, 'login_user')
user_elem.send_keys('your_username')

password_elem = browser.find_element(By.ID, 'login_pass')
password_elem.send_keys('your_password')
password_elem.submit()

SECURITY WARNING:

NEVER put real passwords in source code!
- Easy to accidentally leak passwords
- Others can see them in your files
- Better: Read password from separate file

SENDING SPECIAL KEYS:

IMPORT:

from selenium.webdriver.common.keys import Keys

AVAILABLE KEY CONSTANTS:

Keys.ENTER        Keys.PAGE_UP      Keys.DOWN
Keys.RETURN       Keys.ESCAPE       Keys.LEFT
Keys.HOME         Keys.BACK_SPACE   Keys.RIGHT
Keys.END          Keys.DELETE       Keys.TAB
Keys.PAGE_DOWN    Keys.UP           Keys.F1 to Keys.F12

EXAMPLE 5: Scrolling with Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://nostarch.com')
html_elem = browser.find_element(By.TAG_NAME, 'html')
html_elem.send_keys(Keys.END)   # Scrolls to bottom
html_elem.send_keys(Keys.HOME)  # Scrolls to top

WHY USE <html> TAG:
- Base tag of HTML file
- Good place to send page-level keys
- Affects whole page, not specific field

SELENIUM ADDITIONAL FEATURES:

- Modify browser cookies
- Take screenshots of web pages
- Run custom JavaScript
- Full documentation: https://selenium-python.readthedocs.io

===============================================================================
MODULE 6: PLAYWRIGHT - MODERN BROWSER AUTOMATION
===============================================================================

CONCEPT: Playwright is newer than Selenium with additional features. Most
notable: headless mode (browser runs invisibly in background).

PLAYWRIGHT VS SELENIUM:

ADVANTAGES:
- Headless mode by default (no browser window)
- Easier web driver installation
- Better for automated tests
- Better for background scraping

DISADVANTAGES:
- Newer, smaller community
- May have fewer tutorials/examples

INSTALLATION:

pip install playwright
python -m playwright install  # Windows
python3 -m playwright install  # macOS/Linux

WHAT THE INSTALL COMMAND DOES:
- Downloads web drivers for Firefox, Chrome, Safari
- Easier than Selenium's driver installation

IMPORTING:

from playwright.sync_api import sync_playwright

STARTING PLAYWRIGHT:

METHOD 1: With Statement (Recommended)

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    print(page.title())
    browser.close()

HOW WITH STATEMENT WORKS:
- Automatically calls start() when entering block
- Automatically calls stop() when exiting block
- Cleaner than manual start/stop

METHOD 2: Manual Control (For Interactive Shell)

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')
browser.close()
playwright.stop()

LAUNCH OPTIONS:

headless=False   # Show browser window (default is True/hidden)
slow_mo=50       # Add 50ms delay to operations (easier to watch)

OTHER BROWSERS:

playwright.chromium.launch()  # Chrome
playwright.webkit.launch()    # Safari
playwright.firefox.launch()   # Firefox

PAGE OBJECT:

CONCEPT: Represents a browser tab/window

page = browser.new_page()  # Create new tab

MULTIPLE TABS:
- Can have multiple Page objects open
- Each represents different tab
- All controlled by one Browser object

BROWSER BUTTON METHODS:

page.go_back()     # Back button
page.go_forward()  # Forward button
page.reload()      # Refresh button
page.close()       # Close tab

FINDING ELEMENTS - LOCATORS:

CONCEPT: Locators represent possible HTML elements. Unlike Selenium, doesn't
immediately fail if element doesn't exist - waits up to 30 seconds.

COMMON LOCATORS:

page.get_by_role(role, name=label)     # ARIA role + label
page.get_by_text(text)                 # Contains text
page.get_by_label(label)               # <label> text
page.get_by_placeholder(text)          # Placeholder attribute
page.get_by_alt_text(text)             # Image alt attribute
page.locator(selector)                 # CSS/XPath selector

EXAMPLE LOCATORS:

page.get_by_role('heading', name='Welcome')  # <h1>Welcome</h1>
page.get_by_text('is a link')                # Partial text match
page.get_by_label('Username')                # <label>Username:</label>
page.get_by_placeholder('admin')             # placeholder="admin"
page.get_by_alt_text('cat photo')            # alt="cat photo"
page.locator('#author')                      # id="author"

LOCATOR METHODS:

get_attribute(name)    # Get attribute value
count()                # Number of matching elements
nth(index)             # Get element at index
first                  # First matching element
last                   # Last matching element
all()                  # List of all Locator objects
inner_text()           # Text content
inner_html()           # HTML source
click()                # Click element
is_visible()           # True if visible
is_enabled()           # True if enabled
is_checked()           # True if checked (checkbox/radio)
bounding_box()         # Position and size dictionary

EXAMPLE: Getting Text

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto('https://autbor.com/example3.html')
    
    elems = page.locator('p')
    print(elems.nth(0).inner_text())    # Text only
    print(elems.nth(0).inner_html())    # HTML with tags
    
    browser.close()

OUTPUT:
This <p> tag puts content into a single paragraph.
This <p> tag puts <b>content</b> into a <i>single</i> paragraph.

CLICKING ELEMENTS:

PAGE METHODS:

page.click(selector)              # Click element
page.check(selector)              # Check checkbox
page.uncheck(selector)            # Uncheck checkbox
page.set_checked(selector, bool)  # Set checkbox state

LOCATOR METHODS:

element.click()           # Click this element
element.check()           # Check checkbox
element.uncheck()         # Uncheck checkbox
element.set_checked(bool) # Set checkbox state

EXAMPLE: Clicking

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')

page.click('input[type=checkbox]')  # Checks checkbox
page.click('input[type=checkbox]')  # Unchecks checkbox

checkbox = page.get_by_role('checkbox')
checkbox.check()              # Checks it
checkbox.uncheck()            # Unchecks it
checkbox.set_checked(True)    # Checks it
checkbox.set_checked(False)   # Unchecks it

browser.close()
playwright.stop()

WHY check() AND uncheck() ARE BETTER:

click() - toggles state (unpredictable if already checked/unchecked)
check() - ensures checked state
uncheck() - ensures unchecked state
set_checked() - set specific state with True/False

FILLING FORMS:

METHOD: locator.fill(text)

WHAT IT DOES:
- Fills <input> or <textarea> with text
- Clears existing text first

METHOD: locator.clear()

WHAT IT DOES:
- Erases all text in element

EXAMPLE: Login Form

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')

page.locator('#login_user').fill('your_username')
page.locator('#login_pass').fill('your_password')
page.locator('input[type=submit]').click()

browser.close()
playwright.stop()

NOTE: No submit() method in Playwright - use click() on Submit button

SENDING SPECIAL KEYS:

METHOD: locator.press(key)

WHAT IT DOES:
- Simulates keyboard key press
- Can combine keys with +

KEY STRINGS:

Single characters: 'a', 'z', '?'
Modified keys: 'Control+A', 'Shift+End'
Special keys: 'Enter', 'Escape', 'Tab', 'Backspace', 'Delete'
Arrow keys: 'ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'
Function keys: 'F1' to 'F12'
Number keys: 'Digit0' to 'Digit9'
Letter keys: 'KeyA' to 'KeyZ'

EXAMPLE: Scrolling

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False, slow_mo=50)
page = browser.new_page()
page.goto('https://autbor.com/example3.html')

page.locator('html').press('End')   # Scroll to bottom
page.locator('html').press('Home')  # Scroll to top

browser.close()
playwright.stop()

PLAYWRIGHT ADDITIONAL FEATURES:

Full documentation: https://playwright.dev/python/docs/intro

===============================================================================
PRACTICAL PROJECTS
===============================================================================

PROJECT 1: MAP LAUNCHER (launchmap.py)

PURPOSE: Automatically open OpenStreetMap for an address

HOW IT WORKS:
1. Get address from command line arguments or clipboard
2. Build OpenStreetMap URL with address
3. Open browser to that URL

PROJECT 2: PYPI SEARCH OPENER (searchpypi.py)

PURPOSE: Open first 5 PyPI search results in browser tabs

HOW IT WORKS:
1. Get search terms from command line
2. Download PyPI search results page
3. Use Beautiful Soup to find result links
4. Open first 5 links in browser tabs

CODE PATTERN:
soup.select('.package-snippet')  # Find all result links
link_elems[i].get('href')        # Get URL from link
webbrowser.open(url)             # Open in browser

PROJECT 3: XKCD COMIC DOWNLOADER (downloadXkcdComics.py)

PURPOSE: Download all XKCD comics automatically

HOW IT WORKS:
1. Load XKCD home page
2. Download the comic image
3. Follow "Previous Comic" link
4. Repeat until reaching first comic

KEY TECHNIQUES:
- Use Beautiful Soup to find image URL
- Use Beautiful Soup to find Previous link
- Save images with iter_content()
- Add time.sleep(1) to avoid hammering server

===============================================================================
BEST PRACTICES AND IMPORTANT NOTES
===============================================================================

WHEN TO USE EACH MODULE:

webbrowser:
- Opening URLs in browser
- Simple tasks, no downloading needed
- Opening local HTML help files

requests:
- Downloading files/pages
- Accessing APIs
- Static web pages (no JavaScript interaction)

Beautiful Soup:
- Parsing HTML
- Extracting data from downloaded pages
- Works with requests module

Selenium:
- Need to interact with JavaScript pages
- Filling out forms
- Clicking buttons
- Looking like a real user

Playwright:
- Headless automation
- Background tasks
- Modern alternative to Selenium
- Better for automated tests

SECURITY BEST PRACTICES:

1. Never hardcode passwords in source code
2. Keep API keys secret
3. Read sensitive data from files
4. Don't share code with API keys in it
5. Use environment variables for secrets

WEB SCRAPING ETHICS:

1. Check website's robots.txt file
2. Add delays between requests (time.sleep())
3. Don't hammer servers with rapid requests
4. Respect rate limits
5. Use APIs when available (better than scraping)

ERROR HANDLING:

1. Always use raise_for_status() after requests.get()
2. Use try/except for element finding
3. Check if element exists before accessing
4. Handle network errors gracefully

===============================================================================
TEXTBOOK PRACTICE QUESTIONS
===============================================================================

QUESTION 1:
Briefly describe the differences between the webbrowser, requests, and bs4 modules.

ANSWER:
The webbrowser module opens a web browser to a specific URL but doesn't download
any content. The requests module downloads web pages and files from the internet.
The bs4 (Beautiful Soup) module parses HTML content to extract specific information
from downloaded web pages. Typically, you'd use requests to download a page, then
bs4 to extract data from it, while webbrowser is for opening URLs in the browser.

QUESTION 2:
What type of object is returned by requests.get()? How can you access the
downloaded content as a string value?

ANSWER:
requests.get() returns a Response object. You can access the downloaded content
as a string by using the Response object's text attribute. For example:
response = requests.get(url)
content = response.text

QUESTION 3:
What requests method checks that the download worked?

ANSWER:
The raise_for_status() method. Call it on the Response object immediately after
requests.get(). If the download failed, it raises an exception. If successful,
it does nothing. Example: response.raise_for_status()

QUESTION 4:
How can you get the HTTP status code of a requests response?

ANSWER:
Use the status_code attribute of the Response object. For example:
response = requests.get(url)
print(response.status_code)  # Prints 200 for OK, 404 for Not Found, etc.

You can also compare it to requests.codes.ok to check for success:
if response.status_code == requests.codes.ok:
    print("Download successful")

QUESTION 5:
How do you save a requests response to a file?

ANSWER:
Open a file in write binary mode ('wb'), then loop over the response's
iter_content() method and write each chunk:

response = requests.get(url)
response.raise_for_status()
with open('filename.ext', 'wb') as file:
    for chunk in response.iter_content(100000):
        file.write(chunk)

QUESTION 6:
What two formats do most online APIs return their responses in?

ANSWER:
JSON (JavaScript Object Notation) and XML (eXtensible Markup Language). JSON is
more common for modern web APIs and looks similar to Python dictionaries. Use
json.loads(response.text) to convert JSON responses to Python data structures.

QUESTION 7:
What is the keyboard shortcut for opening a browser's Developer Tools?

ANSWER:
Press F12 in Firefox, Chrome, and Microsoft Edge.
Press F12 again to close the Developer Tools.

QUESTION 8:
How can you view (in the Developer Tools) the HTML of a specific element on a
web page?

ANSWER:
Right-click (or CTRL-click on macOS) on the element in the web page and select
"Inspect Element" from the context menu. This opens the Developer Tools and
highlights the HTML code for that specific element.

QUESTION 9:
What CSS selector string would find the element with an id attribute of main?

ANSWER:
'#main'

The # symbol indicates an id selector. Example usage:
elem = soup.select('#main')

QUESTION 10:
What CSS selector string would find the elements with a CSS class attribute of
highlight?

ANSWER:
'.highlight'

The . symbol indicates a class selector. Example usage:
elems = soup.select('.highlight')

QUESTION 11:
Say you have a Beautiful Soup Tag object stored in the variable spam for the
element <div>Hello, world!</div>. How could you get a string 'Hello, world!'
from the Tag object?

ANSWER:
Use the get_text() method:
text = spam.get_text()

Or use the text attribute:
text = spam.text

Both return 'Hello, world!'

QUESTION 12:
How would you store all the attributes of a Beautiful Soup Tag object in a
variable named link_elem?

ANSWER:
Use the attrs attribute, which contains a dictionary of all attributes:
attributes = link_elem.attrs

For example, if link_elem represents <a href="https://example.com" id="link1">,
then link_elem.attrs would be {'href': 'https://example.com', 'id': 'link1'}

QUESTION 13:
Running import selenium doesn't work. How do you properly import Selenium?

ANSWER:
Use: from selenium import webdriver

Then you can create a browser object:
browser = webdriver.Firefox()

QUESTION 14:
What's the difference between the find_element() and find_elements() methods
in Selenium?

ANSWER:
find_element() returns a single WebElement object representing the FIRST matching
element on the page. It raises NoSuchElement exception if no match is found.

find_elements() returns a LIST of WebElement objects for EVERY matching element
on the page. It returns an empty list if no matches are found (doesn't raise
an exception).

QUESTION 15:
What methods do Selenium's WebElement objects have for simulating mouse clicks
and keyboard keys?

ANSWER:
click() - Simulates a mouse click on the element
send_keys(text) - Simulates typing text (for keyboard input)
submit() - Submits a form containing the element
clear() - Clears text from a text field

Example:
elem.click()               # Click element
elem.send_keys('hello')    # Type 'hello'
elem.send_keys(Keys.ENTER) # Press Enter key
elem.submit()              # Submit form

QUESTION 16:
In Playwright, what locator method call simulates pressing CTRL-A to select all
the text on the page?

ANSWER:
page.locator('html').press('Control+A')

Or more specifically:
page.keyboard.press('Control+A')

This sends the Control+A key combination to select all text.

QUESTION 17:
How can you simulate clicking a browser's Forward, Back, and Refresh buttons
with Selenium?

ANSWER:
browser.back()     # Click Back button
browser.forward()  # Click Forward button
browser.refresh()  # Click Refresh/Reload button

Where browser is the WebDriver object returned by webdriver.Firefox()

QUESTION 18:
How can you simulate clicking a browser's Forward, Back, and Refresh buttons
with Playwright?

ANSWER:
page.go_back()     # Click Back button
page.go_forward()  # Click Forward button
page.reload()      # Click Refresh/Reload button

Where page is the Page object returned by browser.new_page()

===============================================================================
END OF CHAPTER 13 SUMMARY
===============================================================================

This chapter covered web scraping fundamentals: downloading content with requests,
parsing HTML with Beautiful Soup, and controlling browsers with Selenium and
Playwright. These tools let you automate tedious web-based tasks and extract data
from websites.

Key takeaways:
- Use webbrowser for simple URL opening
- Use requests for downloading files/pages
- Use Beautiful Soup for parsing HTML
- Use Selenium for interactive browser control
- Use Playwright for headless/modern automation
- Always respect website terms of service
- Add delays to avoid hammering servers
- Use APIs when available instead of scraping
