# Week 4 Video Demo Assignment - Chat Command Parser

**Due:** Wednesday, February 5, 2026  
**Video Length:** Less than 5 minutes  
**Chapters Covered:** Chapter 8 (Strings) & Chapter 9 (Regular Expressions)

---

## Assignment Overview

Record yourself demonstrating skills obtained in class. This is an **oral exam** style video - you must explain code naturally without reading from notes.

**Why video recordings?** In the age of AI, explaining code on camera demonstrates you truly understand it, even if AI helped generate it initially.

---

## SCENARIO: Chat Command Parser for Multiplayer Game Server

You are writing a chat command parser for a multiplayer game server. Players type commands into chat, but players are often messy, so commands may have:
- Extra spaces
- Mixed capitalization
- Optional arguments
- Minor formatting errors

Your job: Recognize valid commands, extract their parameters, and reject invalid ones gracefully.

---

## Supported Commands

### 1. `/whisper <player> <message>`
- **Player name:** alphabetic only
- **Message:** any text after the player name

### 2. `/tp <x> <y> <z>`
- Exactly 3 integers (can be negative)

### 3. `/emote <action>`
- Action is a single lowercase word

### 4. `/roll <number>`
- Number must be a positive integer

---

## Provided Input (MUST USE EXACTLY)

```python
chat_log = [
    # --- Valid baseline commands ---
    "/WHISPER   Alex   Hello there!",
    "/whisper Mia    Meet at spawn",
    "/TP  120   64   -30",
    "/EMOTE    dance",
    "/roll   20",

    # --- Valid: Case & spacing issues ---
    "   /whisper    Chris   Hi   ",
    "/Tp 10 20 30",
    "/tp    -5   70    42",

    # --- Invalid: Wrong argument counts ---
    "/tp 10 20",                  # missing z
    "/tp 10 20 30 40",             # extra argument
    "/roll",                       # missing number
    "/emote",                      # missing action
    "/whisper Alex",               # missing message

    # --- Invalid: type issues ---
    "/tp 12 sixty 9",               # non-numeric coordinate
    "/roll twenty",                 # non-numeric roll
    "/roll -5",                     # negative roll not allowed
    "/emote dance-now",             # invalid character in action
    "/whisper Al3x Hello",          # digit in player name

    # --- You choose Validity: Subtle formatting traps ---
    "/whisper  AlexHello",          # no space between name/message
    "/tp 10, 20, 30",               # commas instead of spaces
    "/tp (10) 20 30",               # parentheses
    "/roll  020",                   # leading zero
    "/emote DANCE",                 # uppercase action
    "/whisper \"Alex\" Hi",         # quoted name (unsupported)

    # --- You Choose Validity: Almost commands ---
    "/whisperAlex Hello",           # missing space after command
    "/tp10 20 30",                  # missing space
    "/roll20",                      # missing space
    "/emotes dance",                # unknown command
    "/tp x y z",                    # letters instead of numbers

    # --- Other Invalid ---
    "/",
    "/help",
    "tp 10 20 30",
    "just talking in chat",
    ""
]
```

---

## Program Requirements

### 1. Normalize Input
- Strip leading/trailing whitespace
- Treat commands as case-insensitive
- Reduce multiple spaces between tokens to a single space

### 2. Recognize Commands Using Regex
- Detect which command (if any) the line represents
- Extract all required arguments
- **Use only regex libraries from textbook**

### 3. Output Format

For each line of input, print exactly one of:

**If VALID:**
```
VALID COMMAND
Type: whisper
Target: Alex
Message: Hello there!
```

**If INVALID:**
```
INVALID COMMAND
```

### 4. Summary Output
```
SUMMARY:
Valid commands: X
Invalid commands: Y
```

---

## Video Recording Requirements

### BEFORE Recording:
- ✅ Write ALL code before recording
- ✅ Can use AI assistance, but MUST understand all code
- ✅ Test that code works completely

### DURING Recording:

**Must Show:**
1. ✅ Your face on camera (looking at camera, not reading notes)
2. ✅ Computer screen when demonstrating code
3. ✅ Clear and intelligible audio

**Must Do:**
1. ✅ Walk through your code
2. ✅ Demonstrate it working
3. ✅ Explain how it works
4. ✅ Describe the regex you used and how it works
5. ✅ Tell what decisions you made about validity/invalidity of edge cases
6. ✅ Describe at least 1 bug you encountered and how you fixed it

**Recording Style:**
- **Oral exam format** - like talking to professor who asked questions you know in advance
- Cannot read from script on camera (professor will know!)
- Information must be in your head
- Speak naturally, explain confidently

### Video Technical Requirements:
- Less than 5 minutes
- Upload to YouTube as "Unlisted" (not searchable but accessible via link)
- Test link in Incognito/Private browser before submitting
- NOT allowed: YouTube shorts or smartphone recordings

---

## What Gets Graded

If general requirements not met (face visible, audio clear, no reading notes), video will NOT be graded and must be resubmitted.

---

## Why Thorough Learning Matters for This Assignment

**From previous experience (Chapters 4-7):**
- Rushing = Getting lost when explaining → Frustration → Wanting to give up → Poor video quality

**This assignment requires:**
- Natural explanation (can't fake it on camera)
- Understanding regex patterns deeply
- Being able to debug and explain bugs
- Confidence to speak without notes

**Strategy:**
- Monday: Learn Chapter 8 thoroughly (string methods for normalization)
- Tuesday: Learn Chapter 9 thoroughly (regex patterns for command matching)
- Wednesday: Code with understanding, record with confidence

---

## Concepts Needed from Textbook

### From Chapter 8 (Strings):
- `.strip()` - remove leading/trailing whitespace
- `.lower()` - case normalization
- `.split()` - tokenizing input
- String manipulation methods

### From Chapter 9 (Regular Expressions):
- `re.compile()` - create regex patterns
- `.search()` - find pattern matches
- `.group()` - extract captured groups
- Grouping with parentheses `()`
- Character classes `[a-zA-Z]`, `\d`
- Quantifiers `+`, `*`, `{n}`
- Anchors `^`, `$`
- Word boundaries `\b`
- Case-insensitive flag `re.IGNORECASE`

---

## Submission

Submit YouTube link (unlisted, publicly accessible).
