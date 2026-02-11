# Week 4 Video Demo - Chat Command Parser SOLUTION
# This is approximately 80-100 lines of actual code (not counting comments/blank lines)
# Time estimate: 1-2 hours to write and test (after learning Ch 8 & 9)
# Difficulty: Medium - but totally doable after understanding regex from Ch 9

import re

# ============================================================================
# STEP 1: Define regex patterns for each command
# ============================================================================
# These use concepts from Chapter 9 (Regular Expressions)

# /whisper <player> <message>
# - Player name must be alphabetic only: [a-zA-Z]+
# - Message is everything after the player name: .+
whisper_pattern = re.compile(r'^/whisper\s+([a-zA-Z]+)\s+(.+)$', re.IGNORECASE)

# /tp <x> <y> <z>
# - Exactly 3 integers (can be negative): -?\d+
# - \s+ means one or more spaces between them
tp_pattern = re.compile(r'^/tp\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)$', re.IGNORECASE)

# /emote <action>
# - Single lowercase word: [a-z]+
# - Must be lowercase, so we check after normalization
emote_pattern = re.compile(r'^/emote\s+([a-z]+)$', re.IGNORECASE)

# /roll <number>
# - Positive integer only: \d+
# - We'll validate it's positive (not zero or negative) separately
roll_pattern = re.compile(r'^/roll\s+(\d+)$', re.IGNORECASE)


# ============================================================================
# STEP 2: Function to normalize input
# ============================================================================
# Uses concepts from Chapter 8 (String methods)

def normalize_input(text):
    """
    Normalize input by:
    1. Stripping leading/trailing whitespace
    2. Reducing multiple spaces to single space
    """
    text = text.strip()  # Remove leading/trailing whitespace
    text = ' '.join(text.split())  # Split and rejoin to collapse multiple spaces
    return text


# ============================================================================
# STEP 3: Function to process each command
# ============================================================================

def process_command(line):
    """
    Process a single line of chat input.
    Returns: (is_valid, command_type, details_dict)
    """
    # Normalize the input
    normalized = normalize_input(line)
    
    # If empty after normalization, it's invalid
    if not normalized:
        return (False, None, None)
    
    # Try to match /whisper command
    match = whisper_pattern.match(normalized)
    if match:
        player = match.group(1)
        message = match.group(2)
        return (True, 'whisper', {'Target': player, 'Message': message})
    
    # Try to match /tp command
    match = tp_pattern.match(normalized)
    if match:
        x = match.group(1)
        y = match.group(2)
        z = match.group(3)
        return (True, 'tp', {'X': x, 'Y': y, 'Z': z})
    
    # Try to match /emote command
    # Special check: action must be lowercase after normalization
    match = emote_pattern.match(normalized)
    if match:
        action = match.group(1)
        # Check if original action was lowercase (not DANCE or Dance)
        # We need to check the normalized version before case conversion
        original_action_start = normalized.lower().find(action)
        if original_action_start != -1:
            # Extract the actual action from normalized (before IGNORECASE)
            actual_action = normalized.split()[-1]  # Get last word
            if actual_action.islower() and actual_action.isalpha():
                return (True, 'emote', {'Action': action})
    
    # Try to match /roll command
    match = roll_pattern.match(normalized)
    if match:
        number = match.group(1)
        # Validate it's a positive integer (not zero, no leading zeros except "0")
        if int(number) > 0 and (number == "0" or not number.startswith("0")):
            return (True, 'roll', {'Number': number})
    
    # No valid command matched
    return (False, None, None)


# ============================================================================
# STEP 4: Main program
# ============================================================================

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
    "/whisper  AlexHello",          # no space between name/message - INVALID (no space)
    "/tp 10, 20, 30",               # commas instead of spaces - INVALID
    "/tp (10) 20 30",               # parentheses - INVALID
    "/roll  020",                   # leading zero - INVALID
    "/emote DANCE",                 # uppercase action - INVALID (must be lowercase)
    "/whisper \"Alex\" Hi",         # quoted name - INVALID (quotes not supported)

    # --- You Choose Validity: Almost commands ---
    "/whisperAlex Hello",           # missing space after command - INVALID
    "/tp10 20 30",                  # missing space - INVALID
    "/roll20",                      # missing space - INVALID
    "/emotes dance",                # unknown command - INVALID
    "/tp x y z",                    # letters instead of numbers - INVALID

    # --- Other Invalid ---
    "/",
    "/help",
    "tp 10 20 30",
    "just talking in chat",
    ""
]

# Process each line and track statistics
valid_count = 0
invalid_count = 0

for line in chat_log:
    is_valid, cmd_type, details = process_command(line)
    
    if is_valid:
        valid_count += 1
        print("VALID COMMAND")
        print(f"Type: {cmd_type}")
        for key, value in details.items():
            print(f"{key}: {value}")
        print()  # Blank line
    else:
        invalid_count += 1
        print("INVALID COMMAND")
        print()  # Blank line

# Print summary
print("SUMMARY:")
print(f"Valid commands: {valid_count}")
print(f"Invalid commands: {invalid_count}")
