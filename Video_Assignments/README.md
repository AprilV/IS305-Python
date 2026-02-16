# IS305 Video Assignments

Weekly video demonstrations showing skills learned in class.

## 📂 Folder Organization

All video assignments are organized in the `Video_Assignments/` folder with consistent naming:
- `Week_X_Topic/` format
- Each week contains the code, requirements, and guide

---

## Completed Assignments

### Week 3 - Minecraft Crafting
**Topic:** Functions and Data Structures  
**Location:** `Week_3_Minecraft/`  
**File:** `minecraft_crafting.py`  
**Concepts:** Function definitions, dictionaries, lists

---

### Week 4 - Chat Command Parser  
**Topic:** Pattern Matching and String Manipulation  
**Location:** `Week_4_Chat_Parser/`  
**Files:**
- `chat_command_parser_SOLUTION.py` - Working solution
- `chat_command_vid chap 4.py` - Original assignment code
- `ASSIGNMENT Instructions.md` - Assignment details
- `ASSIGNMENT_REQUIREMENTS.md` - Requirements checklist

**Concepts:** String methods, pattern matching, command parsing

---

### Week 6 - Broken Link Checker (THIS WEEK) 🔥
**Due:** Wednesday  
**Duration:** Less than 5 minutes  
**Topic:** Web Scraping - Finding 404 Broken Links  
**Location:** `Week_6_Broken_Links/`

**Files:**
- `broken_link_checker.py` - Main program (working solution)
- `ASSIGNMENT_REQUIREMENTS.md` - Official assignment from professor
- `ASSIGNMENT_GUIDE.md` - Step-by-step guide for your video recording

**Concepts:** 
- `requests` module (downloading web pages, checking HTTP status codes)
- `beautifulsoup4` module (parsing HTML, finding links with CSS selectors)
- Error handling (try/except blocks for network issues)
- HTTP status codes (404 = Not Found, 200 = OK)

**Video Requirements:**
- ✅ Show face on camera (no reading from notes!)
- ✅ Demonstrate code working
- ✅ Explain how it works (walk through key sections)
- ✅ Discuss at least 1 bug encountered and how you fixed it
- ✅ Under 5 minutes
- ✅ Upload to YouTube as **Unlisted**
- ✅ Test link in incognito browser before submitting

---

## Quick Start for Week 6

### 1. Install Required Libraries
```bash
python -m pip install requests beautifulsoup4
```

### 2. Test the Program
```bash
cd Video_Assignments/Week_6_Broken_Links
python broken_link_checker.py
```
(Press Enter to use default URL: https://automatetheboringstuff.com)

### 3. Prepare for Recording
- ✅ Read `ASSIGNMENT_GUIDE.md` for detailed instructions
- ✅ Practice explaining the code out loud (don't memorize a script!)
- ✅ Test your microphone and camera setup
- ✅ Choose a bug story to tell (3 examples provided in guide)
- ✅ Run the program a few times to understand the output

### 4. Record Your Video
- ✅ Under 5 minutes total
- ✅ Show your face when explaining concepts
- ✅ Show your screen when running/demonstrating code
- ✅ Don't read from notes (pretend it's an oral exam!)
- ✅ Explain like you're teaching a classmate

### 5. Upload and Submit
- ✅ Upload to YouTube as "Unlisted" (NOT private!)
- ✅ Test the link in an incognito/private browser window
- ✅ Verify:
  - Video plays correctly
  - Audio is clear
  - Under 5 minutes
  - Face and screen are visible
- ✅ Submit link to Canvas

---

## Video Recording Tips

### Setup
- **Software:** OBS Studio, Zoom, or built-in screen recorder
- **Layout:** Split screen (face + code) or picture-in-picture
- **Audio:** Test microphone beforehand - must be clearly audible
- **Environment:** Quiet room, close unnecessary windows/notifications

### During Recording
- **Explaining:** Look at camera, speak naturally, teach don't recite
- **Demonstrating:** Show screen, run code, point out key parts
- **Time Management:** Keep under 5 minutes (practice timing!)
- **Confidence:** Act like you know this stuff (because you do!)

### After Recording
1. Upload to YouTube:
   - Click "Upload" → Select video
   - Visibility: **Unlisted** (not private, not public)
   - Title: "IS305 Week 6 - Broken Link Checker"
2. Test in incognito browser - make sure it plays
3. Check quality:
   - Audio clear?
   - Face visible when explaining?
   - Screen visible when demonstrating?
   - Under 5 minutes?
4. Submit link to Canvas assignment

---

## Common Mistakes to Avoid

### ❌ Don't Do This
- Reading from notes on camera (professor notices!)
- Uploading as "Private" (professor can't view!)
- Video over 5 minutes (will be asked to resubmit)
- No face shown (requirement not met)
- Poor/no audio (can't be graded)
- Forgetting to discuss a bug
- Using smartphone recording (not allowed)
- Uploading as YouTube Short (not allowed)

### ✅ Do This Instead
- Look at camera, explain in your own words
- Upload as "Unlisted" (visible to anyone with link)
- Keep concise, under 5 minutes
- Show face, especially when explaining
- Test audio quality before recording
- Tell your bug story (guide has 3 examples)
- Use computer screen recording software
- Upload as regular YouTube video (Unlisted)

---

## Folder Structure

```
Video_Assignments/
├── README.md (this file)
│
├── Week_3_Minecraft/
│   └── minecraft_crafting.py
│
├── Week_4_Chat_Parser/
│   ├── chat_command_parser_SOLUTION.py
│   ├── chat_command_vid chap 4.py
│   ├── ASSIGNMENT Instructions.md
│   └── ASSIGNMENT_REQUIREMENTS.md
│
└── Week_6_Broken_Links/           ← THIS WEEK
    ├── broken_link_checker.py          (your code to demonstrate)
    ├── ASSIGNMENT_REQUIREMENTS.md      (official assignment)
    └── ASSIGNMENT_GUIDE.md             (how to record video)
```

---

## Quick Links & Resources

### Textbook
- [Automate the Boring Stuff with Python (Free Online)](https://automatetheboringstuff.com/)
- [Chapter 12: Web Scraping](https://automatetheboringstuff.com/2e/chapter12/)

### Library Documentation
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)

### Video Help
- [How to Upload Unlisted Video to YouTube](https://support.google.com/youtube/answer/157177)
- [OBS Studio (Free Screen Recording)](https://obsproject.com/)

---

## Need Help?

1. **Code not working?**
   - Check that libraries are installed: `pip list | findstr requests`
   - Read error messages carefully
   - Check `ASSIGNMENT_GUIDE.md` for common issues

2. **Don't know what to say?**
   - Read `ASSIGNMENT_GUIDE.md` - has full script outline
   - Practice explaining to yourself out loud
   - Imagine teaching a friend who doesn't know Python

3. **Video technical issues?**
   - Test recording setup before the real thing
   - Check audio levels
   - Make sure screen is readable in recording

---

**Good luck with your Week 6 video! You've got this! 🎥🐍**

Remember: The goal is to show you understand the code, not to be perfect. Explain clearly, demonstrate confidently, and tell your bug story!
