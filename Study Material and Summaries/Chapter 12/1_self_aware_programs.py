# CHAPTER 12 - SECTION 1: SELF-AWARE PYTHON PROGRAMS - Reference

# This file contains complete working examples for Section 1

import sys
import os

print("=== COMMAND LINE ARGUMENTS ===")
print(f"sys.argv contains: {sys.argv}")
print(f"Script name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"You provided {len(sys.argv) - 1} argument(s)")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Argument {i}: {arg}")
else:
    print("No command line arguments provided")
    print("Try running: python section1_self_aware_programs.py arg1 arg2")

print("\n=== PYTHON INTERPRETER INFO ===")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Major version: {sys.version_info.major}")
print(f"Minor version: {sys.version_info.minor}")
print(f"Full version info: {list(sys.version_info)}")

print("\n=== OPERATING SYSTEM INFO ===")
print(f"os.name: {os.name}")
if os.name == 'nt':
    print("  → Running on Windows")
elif os.name == 'posix':
    print("  → Running on macOS or Linux")

print(f"sys.platform: {sys.platform}")
if sys.platform == 'win32':
    print("  → Windows platform")
elif sys.platform == 'darwin':
    print("  → macOS platform")
elif sys.platform == 'linux':
    print("  → Linux platform")

print("\n=== CHECKING IF MODULE EXISTS ===")
try:
    import nonexistentmodule
except ModuleNotFoundError:
    print("The module 'nonexistentmodule' was not found (as expected)")

try:
    import os  # This exists
    print("The module 'os' was successfully imported")
except ModuleNotFoundError:
    print("This won't print because 'os' exists")

print("\n=== FILE PATH INFO ===")
try:
    # Note: __file__ doesn't exist in interactive shell
    print(f"Current script file: {__file__}")
    from pathlib import Path
    print(f"As Path object: {Path(__file__)}")
    print(f"Absolute path: {Path(__file__).absolute()}")
except NameError:
    print("__file__ is not available (running in interactive shell?)")
