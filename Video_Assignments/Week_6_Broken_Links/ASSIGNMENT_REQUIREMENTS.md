# IS305 Week 6 Video Assignment - Web Scraping for Broken Links

**Due:** Wednesday  
**Duration:** Less than 5 minutes  
**Topic:** Finding 404 Broken Links on Web Pages (Chapters 12-13)

---

## Assignment Overview

Throughout the quarter (for weeks we're not meeting), you will do video recordings of yourself demonstrating skills you're obtaining in this class.

**Why record yourself?** We live in the age of AI, and it's very difficult to know for certain whether or not a student has completed written assignments themselves. It's so easy to get AI to write for you! By explaining the code you're writing, you demonstrate that you understand the code, even if AI originally helped you generate the code.

---

## Requirements for This Week's Assignment

### Before Your Recording:

You're going to write all your code **before** you start recording this week! Feel free to use the support of AI, as necessary, but make sure you understand all the code, because you're going to have to explain it in your video recording!

**Program Requirements:**
- Using the Python libraries from our textbook, write a program that, given the URL of a web page, will find every `<a>` link on the page
- Test whether the linked URL results in a "404 Not Found" status code
- The program should print out any broken links
- **Note:** This is an exercise directly from our textbook!

### For Your Video Recording:

1. **Walk me through your code!** Demonstrate it working, and explain briefly how it works.
2. **Tell me about at least 1 bug** you encountered during the code writing process and what strategies you used to overcome it.

---

## General Video Requirements

Remember, the purpose of these recordings is to demonstrate your knowledge and skills. That means, you can't just read through a script on camera. Although a good way to prepare for this recording is to write and internalize a script, make sure the information is in your head before you start talking to the camera. Imagine this is an "oral exam" with the professor, where you know in advance what the questions are, you come prepared to deliver answers orally, and you're not allowed to bring a cheat sheet with you.

### All video recordings must:

- ✅ Show your face looking and talking to the camera (I'll be able to tell if you're reading notes off screen!)
- ✅ Show your computer screen when you're demonstrating something on the computer
- ✅ Have clear and intelligible audio (I can't grade this unless I can hear your voice)

### This video recording:

- ✅ Should be less than 5 minutes

If any of these general requirements are not met, your video will not be graded, and you'll be asked to resubmit. Also, you are **NOT** allowed to upload your video as a Youtube short or to use a smartphone to record your video!

---

## Submission Instructions

Upload your recording to Youtube (or your favorite similar video service) and submit the link to your video below. This is over Chapters 12 and 13 which you should have.

### Before you submit:

1. ✅ Verify that the Youtube link is publicly accessible by testing the URL in an Incognito or Private browser window
   - **Hint:** use the "Unlisted" visibility setting on Youtube so that your video isn't searchable on Youtube, but is visible to folks with the link
2. ✅ Review the Rubric below to make sure your video meets all the requirements
   - I'll be using this Rubric to assign points to your submission

---

## Files Included

- `broken_link_checker.py` - Working solution demonstrating the assignment
- `ASSIGNMENT_GUIDE.md` - Step-by-step guide for recording your video
- `ASSIGNMENT_REQUIREMENTS.md` - This file (official assignment from professor)

---

## Libraries to Use

From Chapters 12-13:

- **requests**: Download web pages, check HTTP status codes
- **beautifulsoup4 (bs4)**: Parse HTML and find links

Install commands:
```bash
python -m pip install requests
python -m pip install beautifulsoup4
```
