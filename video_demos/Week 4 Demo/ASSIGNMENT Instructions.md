# Week 4 Video Demo Assignment - Chat Command Parser

## Scenario
You are writing a chat command parser for a multiplayer game server. Players type commands into chat, but the players are often messy, so commands may have:
- Extra spaces
- Mixed capitalization
- Optional arguments
- Minor formatting errors

Your job is to recognize valid commands, extract their parameters, and reject invalid ones gracefully.

## Supported Commands

### 1. /whisper <player> <message>
- Player name: alphabetic only
- Message: any text after the player name

### 2. /tp <x> <y> <z>
- Exactly 3 integers (can be negative)

### 3. /emote <action>
- Action is a single lowercase word

### 4. /roll <number>
- Number must be a positive integer

## Program Requirements

Write a program that accomplishes the following:

1. **Normalizes input**
   a. Strip leading/trailing whitespace
   b. Treat commands as case-insensitive
   c. Reduce multiple spaces between tokens to a single space

2. **Recognizes commands using Regex**
   a. Detect which command (if any) the line represents
   b. Extract all required arguments
   c. For each line of input, print exactly one of the following:
      - If valid:
        ```
        VALID COMMAND
        Type: whisper
        Target: Alex
        Message: Hello there!
        ```
      - If invalid:
        ```
        INVALID COMMAND
        ```

3. **A summary of the commands in the form:**
   ```
   SUMMARY:
   Valid commands: X
   Invalid commands: Y
   ```

## Provided Input (MUST USE EXACTLY THIS)

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
