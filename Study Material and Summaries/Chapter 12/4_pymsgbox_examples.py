# CHAPTER 12 - SECTION 4: POP-UP MESSAGE BOXES - Reference

# This file contains complete working examples for GUI message boxes

# IMPORTANT: Install pymsgbox first: python -m pip install pymsgbox
# On Ubuntu Linux: sudo apt install python3-tk

import pymsgbox

print("=== PyMsgBox DEMONSTRATION ===")
print("This will display several GUI message boxes.\n")

# ALERT - Just shows a message
print("1. pymsgbox.alert() - Simple alert message")
print("   An alert box will appear...")
result = pymsgbox.alert('This is an alert message!')
print(f"   User clicked: {result}")  # Always returns 'OK'
print()

# CONFIRM - OK or Cancel
print("2. pymsgbox.confirm() - Confirmation dialog")
print("   A confirm box will appear...")
result = pymsgbox.confirm('Do you want to continue?')
print(f"   User clicked: {result}")  # Returns 'OK' or 'Cancel'

if result == 'OK':
    print("   → User chose to continue")
else:
    print("   → User cancelled")
print()

# PROMPT - Text input
print("3. pymsgbox.prompt() - Text input dialog")
print("   A prompt box will appear...")
name = pymsgbox.prompt('What is your name?')

if name is not None:
    print(f"   User entered: '{name}'")
    print(f"   → Hello, {name}!")
else:
    print("   User cancelled (result is None)")
print()

# PASSWORD - Masked text input
print("4. pymsgbox.password() - Password input dialog")
print("   A password box will appear (text will be masked)...")
password = pymsgbox.password('Enter a password:')

if password is not None:
    print(f"   Password received (length: {len(password)} characters)")
    print("   → Password accepted!")
    # NEVER print actual passwords!
else:
    print("   User cancelled (result is None)")
print()

# PRACTICAL EXAMPLES
print("\n=== PRACTICAL EXAMPLES ===\n")

# Example 1: Confirm before deletion
print("Example 1: Confirmation before dangerous operation")
result = pymsgbox.confirm('Are you sure you want to delete all files?')
if result == 'OK':
    print("   → Would delete files (not really!)")
else:
    print("   → Operation cancelled, files safe")
print()

# Example 2: Collect user information
print("Example 2: Collecting user information")
email = pymsgbox.prompt('Enter your email address:')
if email is not None and '@' in email:
    print(f"   → Email saved: {email}")
elif email is not None:
    print("   → Invalid email format")
else:
    print("   → User cancelled")
print()

# Example 3: Simple login
print("Example 3: Simple password check")
pwd = pymsgbox.password('Enter password to continue:')
if pwd == 'secret':  # Don't do this in real code!
    pymsgbox.alert('Access granted!')
    print("   → User authenticated")
elif pwd is not None:
    pymsgbox.alert('Incorrect password!')
    print("   → Authentication failed")
else:
    print("   → Login cancelled")
print()

# Example 4: Multiple confirms
print("Example 4: Multi-step confirmation")
step1 = pymsgbox.confirm('Start the process?')
if step1 == 'OK':
    pymsgbox.alert('Processing step 1...')
    step2 = pymsgbox.confirm('Continue to step 2?')
    if step2 == 'OK':
        pymsgbox.alert('Process complete!')
        print("   → Both steps completed")
    else:
        print("   → Stopped at step 2")
else:
    print("   → Process not started")
print()

print("=== FUNCTION SUMMARY ===")
print("\npymsgbox.alert(text)")
print("  • Shows message with OK button")
print("  • Returns: 'OK' (string)")
print("  • Use for: Notifications, information, completion messages")
print()

print("pymsgbox.confirm(text)")
print("  • Shows message with OK and Cancel buttons")
print("  • Returns: 'OK' or 'Cancel' (string)")
print("  • Use for: Yes/no questions, confirmations before actions")
print()

print("pymsgbox.prompt(text)")
print("  • Shows message with text input field")
print("  • Returns: User's text input (string) or None if cancelled")
print("  • Use for: Collecting names, emails, short text input")
print()

print("pymsgbox.password(text)")
print("  • Shows message with masked text input field")
print("  • Returns: User's password (string) or None if cancelled")
print("  • Use for: Password entry, sensitive information")
print()

print("=== IMPORTANT NOTES ===")
print("• These functions BLOCK until user responds")
print("• Returns are strings, not booleans")
print("• Check for None when user might cancel")
print("• Good for simple programs that need occasional GUI input")
print("• Not a replacement for full GUI frameworks")
print("• Suitable alternative to print() and input() for some use cases")
