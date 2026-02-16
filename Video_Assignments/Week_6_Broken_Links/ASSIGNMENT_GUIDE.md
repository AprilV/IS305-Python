# Video Assignment Guide - Broken Link Checker

## 📹 What You Need to Do in Your Video (Under 5 minutes)

### Part 1: Demonstrate the Code (2-3 minutes)
1. **Show your face and intro** (10 seconds)
   - "Hi, I'm [name], and today I'm demonstrating a broken link checker program"
   
2. **Explain what the program does** (20 seconds)
   - "This program takes a URL, downloads the web page, finds all the links on that page, and tests each link to see if it gives a 404 error, which means it's broken"

3. **Show and run the code** (1-2 minutes)
   - Open `broken_link_checker.py` on screen
   - Run the program: `python broken_link_checker.py`
   - Enter a URL (use https://automatetheboringstuff.com or any site)
   - Show it checking links and finding any broken ones

4. **Walk through the key parts** (1 minute)
   - **requests.get()**: "This downloads the web page"
   - **BeautifulSoup**: "This parses the HTML so we can search through it"
   - **soup.find_all('a')**: "This finds all the anchor tags, which are links"
   - **tag.get('href')**: "This extracts the actual URL from each link"
   - **The status code check**: "If status_code equals 404, that's a broken link"

### Part 2: Discuss a Bug You Encountered (1-2 minutes)

**Bug Examples You Can Talk About:**

**Option 1: Relative Links Bug**
- "When I first wrote this, the program crashed on relative links - links that start with a slash like '/about' instead of 'https://...' "
- "I fixed it by checking if the link starts with '/' and converting it to an absolute URL by adding the base domain"
- Show the code section that handles this (lines 47-51)

**Option 2: Timeout Bug**
- "Some links took forever to load and the program would hang for minutes"
- "I fixed it by adding a timeout parameter to requests.get() - now it only waits 5 seconds max"
- Show the `timeout=5` parameter (line 58)

**Option 3: Non-HTTP Links Bug**
- "My program crashed when it hit email links (mailto:) or JavaScript links"
- "I fixed it by checking if the link starts with 'http' before testing it"
- Show the code that skips non-http links (lines 52-54)

---

## 🎯 How the Code Works - Simple Explanation

### Step-by-Step Breakdown:

**Step 1: Download the Page** (Lines 17-22)
```python
response = requests.get(url)
response.raise_for_status()
```
- Uses `requests` library to download the web page
- `raise_for_status()` checks if download succeeded

**Step 2: Parse the HTML** (Line 25)
```python
soup = BeautifulSoup(response.text, 'html.parser')
```
- Creates a BeautifulSoup object that understands the HTML structure
- Now we can search for specific tags

**Step 3: Find All Links** (Lines 28-29)
```python
link_tags = soup.find_all('a')
```
- Finds every `<a>` tag (anchor tag = link)
- Returns a list of Tag objects

**Step 4: Extract and Test Each Link** (Lines 35-69)
```python
for tag in link_tags:
    link = tag.get('href')
    # ... handle relative links ...
    link_response = requests.get(link, timeout=5)
    if link_response.status_code == 404:
        broken_links.append(link)
```
- Loop through each link
- Get the `href` attribute (the URL)
- Make a request to that URL
- Check if status code is 404 (Not Found)

**Step 5: Print Results** (Lines 71-81)
- Shows which links are broken
- Shows summary count

---

## 🎬 Recording Tips

### Before Recording:
1. **Practice running the program** - make sure it works!
2. **Pick a good test URL** - use https://automatetheboringstuff.com (has ~50 links, runs in ~30 seconds)
3. **Rehearse your explanation** - don't read from notes on camera!
4. **Test your microphone** - make sure audio is clear
5. **Set up screen + face recording** - use OBS, Zoom, or similar

### During Recording:
- **Look at the camera** when explaining (not at your notes!)
- **Show your screen** when demonstrating
- **Keep it under 5 minutes** - be concise
- **Speak clearly** - imagine explaining to a classmate

### After Recording:
1. Upload to Youtube as **Unlisted** (not private, not public)
2. Test the link in an incognito browser window
3. Make sure video is under 5 minutes
4. Check that audio and video are clear

---

## 💡 What Libraries Are Used?

1. **requests**: Downloads web pages from the internet
   - `requests.get(url)` - downloads a page
   - `response.status_code` - HTTP status (200=OK, 404=Not Found)
   - `response.text` - HTML content as text

2. **BeautifulSoup (bs4)**: Parses and searches through HTML
   - `BeautifulSoup(html, 'html.parser')` - creates soup object
   - `soup.find_all('a')` - finds all anchor tags
   - `tag.get('href')` - gets the link URL from a tag

---

## ✅ Common Questions You Might Get Asked

**Q: Why use Beautiful Soup instead of just searching the text for 'href'?**
A: Beautiful Soup understands HTML structure. Just searching text could find 'href' in comments or other places that aren't actual links.

**Q: What does status code 404 mean?**
A: It's the HTTP code for "Not Found" - the server couldn't find the page at that URL.

**Q: Could this program check for other types of broken links?**
A: Yes! You could check for status codes in the 400s (client errors) or 500s (server errors), not just 404.

**Q: What's the difference between 'html.parser' and other parsers?**
A: Beautiful Soup can use different parsers. 'html.parser' is built into Python. Others like 'lxml' are faster but need to be installed.

---

## 🚀 Quick Test Before Your Video

Run these commands to make sure everything works:

```powershell
# Make sure libraries are installed
python -m pip install requests beautifulsoup4

# Run your program
python broken_link_checker.py

# When prompted, just press Enter to use the default URL
```

Expected result: Should check ~50 links and show which ones are OK or broken. Takes about 30-60 seconds.

---

Good luck with your video! Remember: demonstrate confidence, explain clearly, and show you understand the code even if AI helped you write it initially. 🎓
