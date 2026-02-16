# Week 4 Video Demo - Chat Command Parser
# Student: April Sykes
# Due: February 5, 2026

import re

# Provided chat log - MUST USE EXACTLY THIS
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


# TODO: Step 1 - Create regex patterns for each command
# /whisper <player> <message> - player is alphabetic, message is any text
whisper_pattern = re.compile(r'/whisper\s+([a-zA-Z]+)\s+(.+)', re.IGNORECASE)
# /tp <x> <y> <z> - three integers (can be negative)
tp_pattern = re.compile(r'/tp\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)$', re.IGNORECASE)
# /emote <action> - single lowercase word
emote_pattern = re.compile(r'/emote\s+([a-z]+)$', re.IGNORECASE)
# /roll <number> - positive integer only
roll_pattern = re.compile(r'/roll\s+([1-9]\d*)$', re.IGNORECASE)


# TODO: Step 2 - Initialize counters
valid_count = 0
invalid_count = 0


# TODO: Step 3 - Loop through chat_log
for line in chat_log:
    # Normalize the line (strip, reduce spaces)
    normalized = line.strip()
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Try to match each pattern using .search()
    whisper_match = whisper_pattern.search(normalized)
    tp_match = tp_pattern.search(normalized)
    emote_match = emote_pattern.search(normalized)
    roll_match = roll_pattern.search(normalized)
    
    # Print results in correct format
    if whisper_match:
        print("VALID COMMAND")
        print(f"Type: whisper")
        print(f"Target: {whisper_match.group(1)}")
        print(f"Message: {whisper_match.group(2)}")
        valid_count += 1
    
    elif tp_match:
        print("VALID COMMAND")
        print(f"Type: tp")
        print(f"X: {tp_match.group(1)}")
        print(f"Y: {tp_match.group(2)}")
        print(f"Z: {tp_match.group(3)}")
        valid_count += 1
    
    elif emote_match:
        print("VALID COMMAND")
        print(f"Type: emote")
        print(f"Action: {emote_match.group(1)}")
        valid_count += 1
    
    elif roll_match:
        print("VALID COMMAND")
        print(f"Type: roll")
        print(f"Number: {roll_match.group(1)}")
        valid_count += 1
    
    else:
        print("INVALID COMMAND")
        invalid_count += 1


# TODO: Step 4 - Print summary
print("\nSUMMARY:")
print(f"Valid commands: {valid_count}")
print(f"Invalid commands: {invalid_count}")
