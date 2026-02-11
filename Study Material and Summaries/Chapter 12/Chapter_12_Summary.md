===============================================================================
IS 305 - CHAPTER 12: DESIGNING AND DEPLOYING COMMAND LINE PROGRAMS
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: February 9, 2026

===============================================================================
CHAPTER OVERVIEW
===============================================================================

WHAT THIS CHAPTER COVERS:
This chapter teaches you how to run Python programs from the command line terminal
instead of from a code editor like Mu. You'll learn how to make your programs 
accessible and convenient to use through terminal commands, virtual environments,
and various deployment strategies.

WHY THIS MATTERS:
- Running programs from terminals is faster than opening an editor every time
- Command line programs can be run by others who don't have Python installed
- Understanding deployment makes your programs usable in real-world scenarios
- Terminal skills are essential for professional software development
- Makes automation truly convenient and practical

KEY CONCEPTS YOU'LL LEARN:
1. Using the terminal to navigate and run programs
2. Understanding and modifying the PATH environment variable
3. Creating and using virtual environments
4. Installing third-party packages with pip
5. Making Python programs "self-aware" with system variables
6. Designing text-based user interfaces
7. Deploying programs for quick access on Windows, macOS, and Linux

DEPLOYMENT: The process of making software usable outside code editors.

===============================================================================
PROGRAMMING TERMINOLOGY
===============================================================================

Understanding different types of programs:

PROGRAM
A complete piece of software, large or small, with instructions that a computer
carries out. This is the most general term.

SCRIPT
A program that an interpreter runs from its source-code form rather than from 
a compiled, machine-code form. Python programs are often called scripts even 
though Python code can be compiled.

COMMAND
A program that is often run from a text-based terminal and doesn't have a 
graphical user interface (GUI). All configuration is done up front by specifying 
command line arguments before running the command. Examples: dir, ls, cd

SHELL SCRIPT / BATCH FILE
A single text file that conveniently runs several bundled terminal commands in 
one batch. This way, a user can run one shell script instead of manually entering 
several commands individually.
- macOS/Linux: .sh file extension (or no extension)
- Windows: .bat file extension (called batch files)

APPLICATION
A program that has a GUI and contains multiple related features. Examples: Excel,
Firefox. Applications usually have several files that an installer program sets 
up on your computer.

APP
A common name for mobile phone and tablet applications, but the term can be used 
for desktop applications as well.

WEB APP
A program that runs on a web server, and which users interact with over the 
internet through a web browser.

===============================================================================
USING THE TERMINAL
===============================================================================

WHAT IS A TERMINAL?
A command line interface (CLI) where you type text commands to interact with 
your computer. Also called: command prompt, terminal, shell, or console.

WHY USE THE TERMINAL?
- Fast program execution without opening code editors
- Essential for professional software development
- Powerful for automation and batch operations
- Required for server management and deployment

OPENING A TERMINAL:

Windows:
  - Click Start button (or press Windows key)
  - Enter "Command Prompt" or "PowerShell" or "Terminal"

macOS:
  - Click Spotlight icon (or press ⌘-spacebar)
  - Enter "Terminal"

Ubuntu Linux:
  - Press Windows key to bring up Dash
  - Enter "Terminal"
  - Or use keyboard shortcut: CTRL-ALT-T

TERMINAL PROMPTS:

Windows:
  C:\Users\al>your commands go here
  (Shows full path to current folder, followed by >)

macOS:
  al@Als-MacBook-Pro ~ % your commands go here
  (Shows username, computer name, current directory, followed by %)

Ubuntu Linux:
  al@al-VirtualBox:~$ your commands go here
  (Shows username@computername:directory$)

NOTE: The ~ symbol represents your home folder on macOS and Linux.

===============================================================================
RUNNING PYTHON FROM THE TERMINAL
===============================================================================

STARTING THE PYTHON INTERACTIVE SHELL:

Windows:
  C:\Users\al>python
  >>> (Python interactive shell prompt appears)

macOS/Linux:
  al@Als-MacBook-Pro ~ % python3
  >>> (Python interactive shell prompt appears)

RUNNING A PYTHON SCRIPT FILE:

Absolute Path (works from any directory):
  Windows:   python C:\Users\al\Scripts\yourScript.py
  macOS:     python3 /Users/al/Scripts/yourScript.py
  Linux:     python3 /home/al/Scripts/yourScript.py

Relative Path (when in the same directory as the script):
  Windows:   python yourScript.py
  macOS/Linux: python3 yourScript.py

IMPORTANT: You do NOT need to open Mu to run Python scripts. The terminal can
run them directly.

===============================================================================
NAVIGATING THE FILE SYSTEM IN THE TERMINAL
===============================================================================

CURRENT WORKING DIRECTORY (CWD)
Just like running Python programs have a current working directory to which 
relative filepaths are attached, the terminal also has a CWD.

THE pwd COMMAND (macOS/Linux)
Print Working Directory - shows the current directory you're in.

  al@Als-MacBook-Pro ~ % pwd
  /Users/al

THE cd COMMAND (Windows/macOS/Linux)
Change Directory - moves you to a different folder.

On Windows (without arguments, shows CWD):
  C:\Users\al>cd
  C:\Users\al

Changing directories:
  C:\Users\al>cd Desktop
  C:\Users\al\Desktop>cd ..
  C:\Users\al>cd C:\Windows\System32
  C:\Windows\System32>

SPECIAL DIRECTORY NAMES:
  .     Current directory
  ..    Parent directory (one level up)
  ~     Home directory (macOS/Linux only)

SWITCHING DRIVES ON WINDOWS:
You cannot change drives with cd. Enter the drive letter followed by a colon:

  C:\Windows\System32>D:
  D:\>cd backup
  D:\backup>

THE dir COMMAND (Windows)
Lists the file and subfolder contents of the current working directory.

  C:\Users\al>dir
  08/26/2036  06:42 PM           171,304 _recursive-centaur.png
  08/18/2035  11:25 AM             1,278 _viminfo
  08/13/2035  12:58 AM    <DIR>          __pycache__
              77 File(s)     83,805,114 bytes
             108 Dir(s)  149,225,267,200 bytes free

THE ls COMMAND (macOS/Linux)
Lists the file and subfolder contents of the current working directory.

  al@Als-MacBook-Pro ~ % ls
  Desktop    Documents    Downloads    Pictures

WORKFLOW TIP:
You'll often bounce between:
- cd to change directories
- dir/ls to see the contents of the directory

LISTING EXECUTABLE FILES:
  Windows:        dir *.exe
  macOS/Linux:    file * | grep executable

RUNNING PROGRAMS FROM THE TERMINAL:

Windows (with or without .exe extension):
  C:\>example.exe
  C:\>example

macOS/Linux (./ followed by program name):
  $ ./example

Absolute path (any OS):
  Windows:        C:\full\path\to\example.exe
  macOS/Linux:    /full/path/to/example

OPENING FILES WITH ASSOCIATED APPLICATIONS:

Windows:
  C:\>example.txt
  (Opens example.txt in default text editor)

macOS/Linux:
  $ open example.txt
  (Opens example.txt in default application)

===============================================================================
THE PATH ENVIRONMENT VARIABLE
===============================================================================

WHAT IS PATH?
PATH is an environment variable that contains a list of folders the terminal 
checks when you enter the name of a program. This allows you to run programs 
without typing their full path every time.

HOW PATH WORKS:

When you type a command like "python", the terminal:
1. Checks folders listed in PATH (in order)
2. Runs the first matching program it finds

IMPORTANT PLATFORM DIFFERENCES:

Windows:
  - First checks the current working directory (CWD)
  - Then checks folders in PATH
  
macOS/Linux:
  - Only checks folders in PATH
  - Does NOT check the CWD
  - To run a program in CWD, use: ./example

VIEWING THE PATH VARIABLE:

Windows:
  C:\Users\al>echo %PATH%
  C:\Windows\system32;C:\Windows;C:\Users\al\Scripts
  (Folders separated by semicolons)

macOS/Linux:
  $ echo $PATH
  /home/al/.local/bin:/home/al/bin:/usr/local/bin:/usr/bin:/bin
  (Folders separated by colons)

EXAMPLE PATH ON UBUNTU LINUX:
  al@al-virtual-machine:~$ echo $PATH
  /home/al/.local/bin:/home/al/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/
  usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

If you type "python3", Linux would check:
1. /home/al/.local/bin folder first
2. Then /home/al/bin folder
3. Then /usr/local/sbin folder
4. And so on...
5. Eventually finds python3 in /usr/bin and runs it

IMPORTANT: The terminal does NOT search subfolders under a PATH folder.
If C:\Users\al\Scripts is in PATH:
  - spam.exe in C:\Users\al\Scripts will be found
  - spam.exe in C:\Users\al\Scripts\eggs will NOT be found

===============================================================================
PATH EDITING - ADDING YOUR SCRIPTS FOLDER
===============================================================================

RECOMMENDED SCRIPTS FOLDER LOCATION:

Windows:    C:\Users\al\Scripts
macOS:      /Users/al/Scripts
Linux:      /home/al/Scripts

(Replace 'al' with your actual username)

WHY ADD A SCRIPTS FOLDER TO PATH?
Once a folder is in PATH, you can run any program in that folder from anywhere
by just typing its name. No need to cd to the folder every time.

EDITING PATH ON WINDOWS:

1. Click Start menu
2. Enter "Edit environment variables for your account"
3. This opens the Environment Variables window
4. Select "Path" from the User variables list (top section)
   (NOT from System variables at the bottom)
5. Click "Edit"
6. Add the new folder: C:\Users\al\Scripts
7. Separate with semicolon if needed
8. Click OK

IMPORTANT: Edit USER variables, not SYSTEM variables.

EDITING PATH ON macOS:

1. Open .zshrc file in your home folder
2. Add this line to the bottom:
   export PATH=/Users/al/Scripts:$PATH
3. Save the file
4. Changes apply to future terminal windows (not current ones)

EDITING PATH ON LINUX:

1. Open .bashrc file in your home folder
2. Add this line to the bottom:
   export PATH=/home/al/Scripts:$PATH
3. Save the file
4. Changes apply to future terminal windows (not current ones)

NOTE: The modification only affects future terminal windows you open. Currently
open terminal windows won't have the updated PATH.

===============================================================================
THE which AND where COMMANDS
===============================================================================

PURPOSE:
Find out which folder in the PATH environment variable a program is located in.

THE which COMMAND (macOS/Linux):

  al@Als-MacBook-Pro ~ % which python3
  /Library/Frameworks/Python.framework/Versions/3.13/bin/python3

This shows the exact location of the python3 program that runs when you type
"python3" in the terminal.

THE where COMMAND (Windows):

  C:\Users\al>where python
  C:\Users\al\AppData\Local\Programs\Python\Python313\python.exe
  C:\Users\al\AppData\Local\Programs\Python\Python312\python.exe

Windows shows EVERY folder in PATH that contains a program named "python".
The topmost one is the version that runs when you enter "python".

WHY THIS IS USEFUL:
- Verify which version of Python is being used
- Troubleshoot PATH configuration issues
- Find the location of installed programs
- Check if multiple versions of a program exist

===============================================================================
VIRTUAL ENVIRONMENTS
===============================================================================

THE PROBLEM VIRTUAL ENVIRONMENTS SOLVE:

Imagine you have:
- Program A that uses package version 1.0
- Program B that uses package version 2.0

Python can't have two versions of the same package installed at the same time.
If version 2.0 is not backward compatible with version 1.0, you'd be constantly
uninstalling one version and reinstalling the other each time you wanted to 
switch programs.

THE SOLUTION: VIRTUAL ENVIRONMENTS

Virtual environments are separate installations of Python that each have their
own set of installed third-party packages.

BEST PRACTICE:
In general, each Python application you create needs its own virtual environment.
However, you can use one virtual environment for all your small learning scripts.

CREATING A VIRTUAL ENVIRONMENT:

1. cd to your Scripts folder:
   Windows:   cd C:\Users\al\Scripts
   macOS/Linux: cd ~/Scripts

2. Run the venv module:
   Windows:   python -m venv .venv
   macOS/Linux: python3 -m venv .venv

This creates the virtual environment's files in a new folder named .venv

FOLDER NAME CONVENTIONS:
- .venv is the conventional name
- Files/folders starting with a period are hidden by default
- You can choose any folder name you want

ACTIVATING A VIRTUAL ENVIRONMENT:

Windows:
  C:\Users\al\Scripts>cd .venv\Scripts
  C:\Users\al\Scripts\.venv\Scripts>activate.bat
  (.venv) C:\Users\al\Scripts\.venv\Scripts>

macOS/Linux:
  $ cd .venv/bin
  $ source activate
  (.venv) $ 

WHAT HAPPENS WHEN YOU ACTIVATE:
1. The PATH environment variable changes to run the Python interpreter inside
   .venv instead of the original system Python
2. Terminal prompt changes to include (.venv) so you know it's active
3. Changes apply ONLY to the current terminal window
4. Other terminal windows are not affected

VERIFYING ACTIVATION:

Windows:
  (.venv) C:\Users\al\Scripts\.venv\Scripts>where python.exe
  C:\Users\Al\Scripts\.venv\Scripts\python.exe
  C:\Users\Al\AppData\Local\Programs\Python\Python313\python.exe

The .venv version is listed first, so it will be used.

macOS/Linux:
  (.venv) $ which python3
  /home/al/Scripts/.venv/bin/python3

FRESH PYTHON INSTALLATION:
A newly created virtual environment has only the default packages:

  (.venv) C:\Users\al\Scripts\.venv\Scripts>python -m pip list
  Package    Version
  ---------- -------
  pip        23.0
  setuptools 65.5.0

None of the packages from your original Python installation are included.

VIRTUAL ENVIRONMENT BEST PRACTICES:

Standard Practice:
- Create one virtual environment per Python project
- Each project can have unique package dependencies
- Prevents conflicts between projects

Relaxed Practice (for learning):
- On Windows: One virtual environment for all small scripts in Scripts folder
- On macOS/Linux: Virtual environment protects system Python (see below)

SYSTEM PYTHON (macOS/Linux):
- The original Python installation that comes with the operating system
- macOS and Linux have programs that rely on this installation
- Installing/updating packages to system Python has slight risk of breaking
  OS programs
- Creating a virtual environment is a good precaution against this risk
- Running scripts with system Python is fine
- Installing packages to system Python is slightly risky

MU EDITOR AND VIRTUAL ENVIRONMENTS:
- Mu has its own virtual environment
- Packages installed to Scripts\.venv won't be available in Mu
- When you press F5 in Mu, it uses Mu's virtual environment
- For advanced work: Edit code in Mu, run it in terminal with your venv active
- Swap between windows with ALT-TAB (Windows/Linux) or ⌘-TAB (macOS)

DEACTIVATING A VIRTUAL ENVIRONMENT:

Windows:
  (.venv) C:\>deactivate.bat

macOS/Linux:
  (.venv) $ deactivate

Or simply close the terminal window and open a new one.

DELETING A VIRTUAL ENVIRONMENT:
Just delete the .venv folder and its contents. That's it!

===============================================================================
INSTALLING PYTHON PACKAGES WITH pip
===============================================================================

WHAT IS pip?
pip is a command line package manager program that comes with Python.
Recursive acronym: "pip installs package"

WHAT IS PyPI?
PyPI (pronounced "pie-pee-eye") is the Python Package Index at https://pypi.org
It contains hundreds of thousands of third-party packages you can install.

PACKAGE vs MODULE:
- Package: A collection of Python code available on PyPI that you install
- Module: An individual .py file containing Python code that you import

You install PACKAGES from PyPI that contain MODULES, and you IMPORT modules
with an import statement.

RUNNING pip:

RECOMMENDED METHOD (always use this):
  Windows:     python -m pip install package_name
  macOS/Linux: python3 -m pip install package_name

ALTERNATIVE (not recommended):
  Windows:     pip install package_name
  macOS/Linux: pip3 install package_name

WHY USE python -m pip?
Running pip through the Python interpreter (python -m pip) prevents errors in
rare cases where you have multiple Python installations and your PATH is 
misconfigured. This ensures pip installs to the same Python interpreter that
runs when you enter python/python3.

IMPORTANT: DO NOT USE PIP WITH ANACONDA
If you've installed the Anaconda distribution of Python, use the conda package
manager through the conda command instead of pip.

INSTALLING A PACKAGE:

  C:\Users\al>python -m pip install package_name

Remember to use python3 on macOS/Linux.
Run this from terminal, NOT from Python interactive shell.

LISTING INSTALLED PACKAGES:

  C:\Users\al>python -m pip list
  Package                   Version
  ------------------------- -----------
  altgraph                  0.17.3
  argon2-cffi               21.3.0
  async-generator           1.10
  wsproto                   1.2.0

UPGRADING A PACKAGE TO LATEST VERSION:

  C:\Users\al>python -m pip install -U package_name

INSTALLING A SPECIFIC VERSION:

  C:\Users\al>python -m pip install package_name==1.17.4

UNINSTALLING A PACKAGE:

  C:\Users\al>python -m pip uninstall package_name

GETTING HELP WITH pip:

  C:\Users\al>python -m pip --help

INSTALLING BOOK PACKAGES:
To ensure compatibility with this book, install the automateboringstuff3 package:

  Windows:     python -m pip install automateboringstuff3
  macOS/Linux: python3 -m pip install automateboringstuff3

This package contains all the correct versions of packages featured in the book.

===============================================================================
SELF-AWARE PYTHON PROGRAMS
===============================================================================

Python's standard library doesn't come with modules that give your programs
sentience, but several built-in variables can give your Python program useful
information about itself, the operating system it's on, and the Python 
interpreter running it.

THE __file__ VARIABLE:

WHAT IT CONTAINS:
The path to the current .py file as a string.

EXAMPLE:
If you run yourScript.py in your home folder:
  __file__ evaluates to: 'C:\Users\al\yourScript.py'

USING WITH pathlib:
  from pathlib import Path
  Path(__file__)  # Returns a Path object of this file

WHY THIS IS USEFUL:
Locate files that exist in the Python program's folder.

IMPORTANT: __file__ doesn't exist in the Python interactive shell.

THE sys.executable VARIABLE:

WHAT IT CONTAINS:
The full path and file of the Python interpreter program itself.

EXAMPLE:
  import sys
  print(sys.executable)
  # Output: C:\Users\al\AppData\Local\Programs\Python\Python313\python.exe

THE sys.version VARIABLE:

WHAT IT CONTAINS:
The string that appears at the top of the interactive shell with version
information about the Python interpreter.

EXAMPLE:
  import sys
  print(sys.version)
  # Output: 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:34) [MSC v.1929 64 bit (AMD64)]

THE sys.version_info.major AND sys.version_info.minor VARIABLES:

WHAT THEY CONTAIN:
Integers of the major and minor version numbers of the Python interpreter.

EXAMPLE:
  import sys
  print(sys.version_info.major)  # 3
  print(sys.version_info.minor)  # 13

DETAILED VERSION INFO:
  list(sys.version_info)  # Returns [3, 13, 1, 'final', 0]

WHY THIS IS USEFUL:
Having version information as integers is much easier to work with than trying
to pull it out of the sys.version string.

THE os.name VARIABLE:

WHAT IT CONTAINS:
  'nt' if running on Windows
  'posix' if running on macOS or Linux

WHY THIS IS USEFUL:
Your Python script can run different code depending on what operating system
it's running on.

EXAMPLE:
  import os
  if os.name == 'nt':
      print("Running on Windows")
  else:
      print("Running on macOS or Linux")

THE sys.platform VARIABLE:

WHAT IT CONTAINS:
More specific operating system identification:
  'win32' on Windows
  'darwin' on macOS
  'linux' on Linux

EXAMPLE:
  import sys
  if sys.platform == 'win32':
      print("Windows detected")
  elif sys.platform == 'darwin':
      print("macOS detected")
  elif sys.platform == 'linux':
      print("Linux detected")

THE platform MODULE:

For highly specific information about OS version and CPU type, use the built-in
platform module.

Documentation: https://docs.python.org/3/library/platform.html

CHECKING IF A MODULE IS INSTALLED:

Use a try block with ModuleNotFoundError:

  try:
      import nonexistentModule
  except ModuleNotFoundError:
      print('This code runs if nonexistentModule was not found.')

WHY THIS IS USEFUL:
If a module is necessary for your program to function, you can put a descriptive
error message here and call sys.exit() to terminate the program. This is more
helpful to users than a generic error message and traceback.

EXAMPLE WITH ERROR HANDLING:
  import sys
  try:
      import pyperclip
  except ModuleNotFoundError:
      print('ERROR: pyperclip module is required.')
      print('Install it with: python -m pip install pyperclip')
      sys.exit()

===============================================================================
TEXT-BASED PROGRAM DESIGN
===============================================================================

BACKGROUND:
Before GUI-supporting operating systems were common, all programs used text to
communicate with users. This book focuses on creating small, useful programs
rather than professional software applications, so programs use print() and
input() through a command line interface rather than windows, buttons, and
graphics.

TUI (TEXT-BASED USER INTERFACE):
Even when limited to text, applications can still provide a user interface
similar to modern GUIs. Applications like Norton Commander used text-based
columns, menus, and navigation.

ADVANTAGES OF TEXT-BASED USER INTERFACES:
- Simplicity: Much easier to create than GUIs
- Fast to develop: No need to learn complex GUI frameworks
- Suitable for automation: Command-line programs are ideal for scripts
- Professional use: Developers frequently use CLI tools

===============================================================================
SHORT COMMAND NAMES
===============================================================================

THE DEBATE: copy vs cp

When learning Linux, many are surprised to find:
- Windows command: copy
- Linux command: cp

Is saving two characters really worth a cryptic name?

THE ANSWER: YES

WHY SHORT NAMES MATTER:
- We READ source code more often than we WRITE it (use verbose names there)
- We TYPE commands more often than we READ them (use short names here)
- You might type a command a dozen times a day
- Short names reduce wrist strain
- Short names make command line easier to use

NAMING BEST PRACTICES:
1. Check if the name already exists:
   - Windows: where command_name
   - macOS/Linux: which command_name
2. Do an internet search for the name
3. Choose something short but memorable
4. Short names go a long way toward ease of use

EXAMPLE: ccwd (copy current working directory)
- Short enough to type quickly
- Descriptive enough to remember
- Unique (not used by other programs)

===============================================================================
COMMAND LINE ARGUMENTS
===============================================================================

WHAT ARE COMMAND LINE ARGUMENTS?
Text supplied after a command that configures how the command behaves.
Similar to arguments passed to a function call.

BASIC EXAMPLE:
  ls                    # Lists files in current directory
  ls exampleFolder      # Lists files in exampleFolder

The "exampleFolder" is a command line argument that configures the ls command
to list a different folder.

RUNNING PYTHON SCRIPTS WITH ARGUMENTS:

If you enter:
  python3 yourScript.py hello world

The python3 program receives the command line arguments and forwards them to
your Python script.

THE sys.argv LIST:

Python scripts access command line arguments through sys.argv.

EXAMPLE:
Command:  python3 yourScript.py hello world
sys.argv: ['yourScript.py', 'hello', 'world']

IMPORTANT DETAILS:
- The first item (sys.argv[0]) is always the script filename
- Remaining items are the arguments split by spaces
- Use double quotes to include spaces in an argument:
  
  Command:  python3 yourScript.py "hello world"
  sys.argv: ['yourScript.py', 'hello world']

WHY COMMAND LINE ARGUMENTS ARE USEFUL:
- Specify configurations before the program starts
- No need for configuration menus or multistep processes
- Very quick to run programs with different settings

DRAWBACK:
Can become incredibly complicated and unreadable as you add more options.

SIMPLE COMMAND LINE ARGUMENT HANDLING:

For simple argument sets, read sys.argv directly:

  import sys
  if len(sys.argv) > 1:
      print(f'You provided: {sys.argv[1]}')
  else:
      print('No arguments provided')

COMPLEX COMMAND LINE ARGUMENT HANDLING:

Questions to consider:
- Should "python yourScript.py spam eggs" do the same as "python yourScript.py eggs spam"?
- If user can have either cheese OR bacon argument, what if they provide both?
- How do you handle all the edge cases?

For complex argument handling, use Python's built-in argparse module.
Documentation: https://docs.python.org/3/library/argparse.html

===============================================================================
CLIPBOARD I/O
===============================================================================

CONCEPT:
Instead of relying only on input() for text input, you can use the clipboard
for your Python program's text input and output.

THE pyperclip MODULE:
A cross-platform third-party package for clipboard operations.

INSTALLATION:
  Windows:     python -m pip install pyperclip
  macOS:       python3 -m pip install pyperclip
  Linux:       python3 -m pip install pyperclip
               sudo apt install xclip

(See Appendix A for full installation instructions)

pyperclip FUNCTIONS:

pyperclip.copy(text)
  Places text on the clipboard.

pyperclip.paste()
  Returns the clipboard's text as a string.

BASIC CLIPBOARD I/O PROGRAM DESIGN:

All clipboard I/O programs follow this pattern:

  1. Import the pyperclip module
  2. Call pyperclip.paste() to obtain input text from clipboard
  3. Perform some work on the text
  4. Copy results to clipboard by passing them to pyperclip.copy()

EXAMPLE PROGRAM:
  import pyperclip
  
  # Get text from clipboard
  text = pyperclip.paste()
  
  # Process the text
  result = text.upper()
  
  # Put result back on clipboard
  pyperclip.copy(result)

WHY THIS IS USEFUL:
Once deployed, clipboard I/O programs are very convenient:
1. Highlight input text
2. Press CTRL-C to copy
3. Run the program
4. Results are on clipboard, ready to paste

EXAMPLE USE CASE:
The "Add Bullets to Wiki Markup" project from Chapter 8 uses this design.

===============================================================================
COLORFUL TEXT WITH Bext
===============================================================================

THE Bext PACKAGE:
A third-party package built on Jonathan Hartley's Colorama package that allows
you to print colorful text in terminal windows.

INSTALLATION:
Follow instructions in Appendix A.

IMPORTANT LIMITATION:
Bext only works in programs run from a terminal window, NOT from Mu or most
other code editors.

CHANGING TEXT COLOR - fg() FUNCTION:

SYNTAX: bext.fg(color)

Available colors:
'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'purple', 'cyan', 'white'

Special value: 'reset' - changes color back to terminal's default

EXAMPLE:
  >>> import bext
  >>> bext.fg('red')
  >>> print('This text is red.')
  This text is red.

CHANGING BACKGROUND COLOR - bg() FUNCTION:

SYNTAX: bext.bg(color)

Same colors available as fg().

EXAMPLE:
  >>> bext.bg('blue')
  >>> print('Red text on blue background is an ugly color scheme.')
  Red text on blue background is an ugly color scheme.
  >>> bext.fg('reset')
  >>> bext.bg('reset')
  >>> print('The text is normal again. Ah, much better.')
  The text is normal again. Ah, much better.

COLOR USAGE CONSIDERATIONS:

1. UNKNOWN TERMINAL MODE:
   User may have terminal in light mode OR dark mode
   No way to know if default is black-on-white or white-on-black

2. USE COLOR SPARINGLY:
   Too much color makes programs look tacky or unreadable
   Use for emphasis, not decoration

Bext TUI-LIKE FEATURES:

bext.clear()
  Clears the screen.

bext.width() and bext.height()
  Returns the current width (in columns) and height (in rows) of the terminal
  window, respectively.

bext.hide() and bext.show()
  Hides and shows the cursor, respectively.

bext.title(text)
  Changes the title bar of the terminal window to the text string.

bext.goto(x, y)
  Moves the cursor to column x and row y in the terminal, where 0, 0 is the
  top-left position.

bext.get_key()
  Waits for the user to press any key and then returns a string describing
  the key. Like a single-key version of input().

RETURN VALUES OF bext.get_key():
- Regular keys: 'a', 'z', '5'
- Special keys: 'left', 'f1', 'esc'
- TAB key: '\t'
- ENTER key: '\n'

TEST EXAMPLE:
Call bext.get_key() in interactive shell to test various keys and see their
return values.

DEMONSTRATION PROGRAM:
ASCII Art Fish Tank program shows what Bext can do:
https://inventwithpython.com/projects/fishtank.py

How it works:
1. Uses bext.clear() to clear terminal window
2. Calls bext.goto() to position cursor
3. Calls bext.fg() to change text color
4. Prints fish using text characters like ><)))*>
5. Featured in "The Big Book of Small Python Projects" (No Starch Press, 2021)

===============================================================================
TERMINAL CLEARING
===============================================================================

THE bext.clear() FUNCTION:
Useful for removing text left over from before your program ran.
Can also be used for flipbook-style animation.

ANIMATION TECHNIQUE:
1. Call clear() to clear the terminal
2. Use print() calls to fill it with text
3. Pause for a moment with time.sleep()
4. Repeat

PYTHON ONE-LINER TO CLEAR SCREEN:

  import os
  def clear():
      os.system('cls' if os.name == 'nt' else 'clear')

WHY THIS WORKS:
- os.system() runs the cls program (on Windows) or clear program (on macOS/Linux)
- Uses conditional expression (ternary operator)
- Syntax: value1 if condition else value2
- Evaluates to value1 if condition is True, value2 if False

CONDITIONAL EXPRESSIONS:
Also called ternary operators in other languages.

General syntax:
  value1 if condition else value2

In our example:
  'cls' if os.name == 'nt' else 'clear'
  
  If os.name == 'nt' is True: evaluates to 'cls'
  If os.name == 'nt' is False: evaluates to 'clear'

NOTE: Conditional expressions often produce unreadable code and are usually
best avoided, but this is a simple enough case.

LIMITATIONS:
- Only works in Python scripts run from terminal
- Does NOT work from Mu or other code editors
- Lets your program clear screen without requiring Bext package

===============================================================================
SOUND AND TEXT NOTIFICATION
===============================================================================

SOUNDS IN COMMAND LINE PROGRAMS:

Historical Context:
Terminal programs existed before rich audio capabilities. Today, there's no
reason text-based programs must be silent.

GOOD REASONS TO USE SOUNDS:
- Notification that a task is complete
- Alert that a problem has occurred
- Can notify user while they're looking at other windows

GOOD REASONS TO LIMIT SOUNDS:
- Easy to overuse to the point of annoyance
- User may be doing a task involving audio already
- User may be in an online meeting
- User's computer might be muted

THE playsound3 PACKAGE:

A third-party package for simple audio file playback.

INSTALLATION:
Install with pip (details in appendix)

PLAYING AN AUDIO FILE:
  import playsound3
  playsound3.playsound('hello.mp3')

SUPPORTED FORMATS:
- MP3 files
- WAV files

Download test file: https://autbor.com/hello.mp3

IMPORTANT BEHAVIOR:
The playsound() function BLOCKS until the audio file finishes playing.
This will halt your program if you give it a long audio file.

TROUBLESHOOTING:
If playsound() raises exceptions (happens with odd characters like = in filename),
try passing a Path object instead of a string:
  from pathlib import Path
  playsound3.playsound(Path('hello.mp3'))

TEXT OUTPUT CONSIDERATIONS:

THE UNIX PHILOSOPHY:
Piping text output of one command to another is easier if the command outputs
only relevant information. Extraneous text would have to be filtered.

DESIGN APPROACHES:

Minimal Output by Default:
- Many commands keep text output to a minimum or have none at all
- Communicate success/error with exit code (covered in Chapter 19)
- Offer -v or --verbose argument to enable verbose mode for human users

Maximum Output by Default:
- Some commands flood output with information
- Offer -q or --quiet argument for quiet mode (no text output)
- Can also mute sound notifications

SIMPLE PROGRAMS:
If your program doesn't require this level of sophistication, you can ignore
these considerations. However, offering these options makes programs more
user-friendly when shared with others.

===============================================================================
POP-UP MESSAGE BOXES WITH PyMsgBox
===============================================================================

GUI vs TUI:
Designing a full GUI requires learning entire code libraries like Tkinter,
wxPython, or PyQt. However, you can add small GUI message boxes to your program
with the PyMsgBox package.

THE PyMsgBox PACKAGE:

A third-party package that creates dialogs using Tkinter.

INSTALLATION:
  Windows/macOS: pip install pymsgbox (Tkinter comes with Python)
  Ubuntu Linux: Must first install Tkinter
                sudo apt install python3-tk
                Then: pip install pymsgbox

See Appendix A for full instructions.

PyMsgBox FUNCTIONS:

These function names mirror JavaScript's message box functions.

pymsgbox.alert(text)
  Displays a text message until the user clicks OK.
  Returns: The string 'OK'

pymsgbox.confirm(text)
  Displays a text message until the user clicks OK or Cancel.
  Returns: 'OK' or 'Cancel'

pymsgbox.prompt(text)
  Displays a text message along with a text field.
  Returns: The text the user entered as a string, or None if they clicked Cancel

pymsgbox.password(text)
  Same as pymsgbox.prompt(), but the text the user enters is masked by asterisks.
  Returns: The password text or None if they clicked Cancel

BLOCKING BEHAVIOR:
These functions won't return until the user clicks OK, Cancel, or X (close).

USE CASE:
If your program requires only occasional notification or user input, using
PyMsgBox's dialogs could be a suitable replacement for print() and input().

EXAMPLES:

Alert:
  import pymsgbox
  pymsgbox.alert('The process is complete!')
  # Shows dialog, waits for user to click OK, returns 'OK'

Confirm:
  import pymsgbox
  response = pymsgbox.confirm('Do you want to continue?')
  if response == 'OK':
      print('User chose to continue')
  else:
      print('User cancelled')

Prompt:
  import pymsgbox
  name = pymsgbox.prompt('What is your name?')
  if name is not None:
      print(f'Hello, {name}!')

Password:
  import pymsgbox
  password = pymsgbox.password('Enter your password:')
  if password is not None:
      print('Password received')  # Don't actually print passwords!

===============================================================================
DEPLOYING PYTHON PROGRAMS
===============================================================================

THE GOAL:
Make your Python programs easy to run without opening Mu, loading the .py file,
and clicking the Run button each time.

PREREQUISITES:
1. Add a Scripts folder to your PATH environment variable (see earlier section)
   Windows:  C:\Users\al\Scripts
   macOS:    /Users/al/Scripts
   Linux:    /home/al/Scripts

2. Set up a virtual environment for your Python scripts (see earlier section)

DEPLOYMENT ON WINDOWS:

Step 1: Place yourScript.py in Scripts folder
  C:\Users\al\Scripts\yourScript.py

Step 2: Create a yourScript.bat batch file in Scripts folder

Batch files contain terminal commands that run together when you run the batch
file. They have a .bat extension and are Windows's version of shell scripts.

BATCH FILE CONTENT:
Create yourScript.bat with this content:

  @call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat
  @python %HOMEDRIVE%%HOMEPATH%\Scripts\yourScript.py %*
  @pause
  @deactivate

EXPLANATION OF EACH LINE:

Line 1: Activate virtual environment
  @call %HOMEDRIVE%%HOMEPATH%\Scripts\.venv\Scripts\activate.bat
  
  - @ symbol makes command itself not appear in terminal
  - %HOMEDRIVE% is 'C:'
  - %HOMEPATH% is '\Users\al'
  - call is necessary; without it, rest of batch file won't run
  
Line 2: Run Python script
  @python %HOMEDRIVE%%HOMEPATH%\Scripts\yourScript.py %*
  
  - Runs python.exe which then runs yourScript.py
  - %* forwards any command line arguments to Python program
  - Always include %* in case you later add command line arguments

Line 3: Pause before closing
  @pause
  
  - Displays "Press any key to continue"
  - Waits for user to press a key
  - Prevents terminal from immediately closing
  - Lets you see any remaining printed output
  - Omit if program has no printed output

Line 4: Deactivate virtual environment
  @deactivate
  
  - Deactivates virtual environment
  - Only matters if batch file was run from terminal
  - Terminal window remains open after program finishes

RUNNING THE BATCH FILE:

Method 1: Run dialog
  1. Press Windows key + R
  2. Enter: yourScript
  3. Press Enter

Method 2: Terminal
  From any folder, just enter: yourScript
  (No need to include .bat extension)

REUSING THE BATCH FILE:
For other Python scripts:
1. Copy yourScript.bat to newScript.bat
2. Change yourScript.py to newScript.py
3. Everything else stays the same

DEPLOYMENT ON macOS:

Step 1: Place yourScript.py in Scripts folder
  /Users/al/Scripts/yourScript.py

Step 2: Create a yourScript.command file

.command files are macOS's way of creating executable scripts for Spotlight.

COMMAND FILE CONTENT:
Create yourScript.command with this content:

  source ~/Scripts/.venv/bin/activate
  python3 ~/Scripts/yourScript.py
  deactivate

EXPLANATION:
- ~ represents home folder (/Users/al)
- Line 1 activates virtual environment
- Line 2 runs Python script using virtual environment's Python
- Line 3 deactivates virtual environment

Step 3: Add execute permissions
  $ cd ~/Scripts
  $ chmod u+x yourScript.command

This makes the file executable by you (the user).

RUNNING THE COMMAND FILE:

Method 1: Spotlight
  1. Press ⌘-spacebar
  2. Enter: yourScript.command
  3. Spotlight autocompletes after first few characters

Method 2: Terminal
  $ yourScript.command

WHY .command FILE IS NEEDED:
If you try to run yourScript.py from Spotlight, it sees the .py extension and
assumes you want to OPEN the file in an editor rather than RUN it.

TEXTEDIT GOTCHA:
If using TextEdit to create the .command file:
1. Make it plaintext: Press SHIFT-⌘-T or click Format → Make Plain Text
2. Watch for auto-capitalization: TextEdit may change python3 to Python3
   (which causes an error)

LIMITATION:
Spotlight has no way to pass command line arguments. Any arguments must be
written directly in the .command file.

DEPLOYMENT ON UBUNTU LINUX:

Step 1: Place yourScript.py in Scripts folder
  /home/al/Scripts/yourScript.py

Step 2: Create a shell script named yourScript

SHELL SCRIPT CONTENT:
Create yourScript (no file extension) with this content:

  #!/usr/bin/env bash
  source ~/Scripts/.venv/bin/activate
  python3 ~/Scripts/yourScript.py
  read -p "Press any key to continue..." -n1 -s
  deactivate

EXPLANATION:
- Line 1: Identifies file as bash shell script
- Line 2: Activates virtual environment
- Line 3: Runs Python script
- Line 4: Waits for keypress (prevents window from closing)
- Line 5: Deactivates virtual environment

Omit Line 4 (read -p...) if program has no printed output.

Step 3: Add execute permissions
  $ cd ~/Scripts
  $ chmod u+x yourScript

This makes the file executable.

At this point, you can run from terminal:
  $ yourScript

Step 4: Create a yourScript.desktop file for Dash

To run from Dash (Ubuntu's program launcher), create a .desktop file.

DESKTOP FILE CONTENT:
Create /home/al/.local/share/applications/yourScript.desktop with:

  [Desktop Entry]
  Name=yourScript
  Exec=gnome-terminal -- /home/al/Scripts/yourScript
  Type=Application

IMPORTANT DETAILS:
- Save to: /home/al/.local/share/applications/
- Exec field requires full path (/home/al); cannot use ~
- If .local folder is hidden, press CTRL-H in Save dialog to show hidden files
- Name field text appears in Dash and can be anything
- Convenient to use same name as yourScript.py

RUNNING THE PROGRAM:

Method 1: Dash
  1. Press Windows key
  2. Enter: yourScript
  3. Dash autocompletes the name

Method 2: Terminal
  $ yourScript

===============================================================================
COMPILING PYTHON PROGRAMS WITH PyInstaller
===============================================================================

WHAT IS COMPILING?
Python is often called an "interpreted language," but it's possible to create
executable programs from Python code with PyInstaller.

HOW PyInstaller WORKS:
PyInstaller doesn't compile Python to machine code. Instead, it creates an
executable program that CONTAINS:
- A copy of the Python interpreter
- Your script

CHARACTERISTICS:
- Executable programs tend to be fairly large
- A simple "Hello, world" program can be close to 8MB
- Literally a thousand times larger than assembly language version

BENEFIT:
You can share your program with others who don't have Python installed.
Just send them one executable file.

INSTALLATION:
  python -m pip install pyinstaller

PLATFORM LIMITATION:
You must run PyInstaller on the operating system where you want the executable
to run. Running PyInstaller on Windows creates a Windows .exe file, but not
a macOS or Linux program, and vice versa.

COMPILING A PYTHON SCRIPT:

Basic command:
  Windows:     python -m PyInstaller --onefile yourScript.py
  macOS/Linux: python3 -m PyInstaller --onefile yourScript.py

SAMPLE OUTPUT:
  C:\Users\al>python -m PyInstaller --onefile yourScript.py
  378 INFO: PyInstaller: X.X.X
  378 INFO: Python: 3.XX.XX
  392 INFO: Platform: Windows-XX-XX.X.XXXX
  393 INFO: wrote C:\Users\al\Desktop\hello-test\hello.spec
  399 INFO: UPX is not available.
  --snip--
  11940 INFO: Appending PKG archive to EXE
  11950 INFO: Fixing EXE headers
  13622 INFO: Building EXE from EXE-00.toc completed successfully.

IMPORTANT NOTES:
- Must use capital P and capital I: PyInstaller
- Lowercase "pyinstaller" gives "No module named pyinstaller" error
- The --onefile argument has TWO dashes

RESULTS:
After running PyInstaller:
- build folder (can be deleted)
- dist folder (contains the executable program)

THE EXECUTABLE:
- Located in the dist folder
- No need to create a virtual environment for it
- Can copy to other computers
- Can send as email attachment (though many providers block executables)

ADDITIONAL RESOURCES:
For basic programs, these instructions work. For more complex cases, see:
https://pyinstaller.org

===============================================================================
PRACTICE QUESTIONS FROM TEXTBOOK
===============================================================================

1. What command lists folder contents on Windows? What about on macOS and Linux?

   ANSWER:
   Windows: dir
   macOS/Linux: ls

2. What does the PATH environment variable contain?

   ANSWER:
   PATH contains a list of folders that the terminal checks when you enter
   the name of a program. This allows you to run programs without typing their
   full path every time. Folders are separated by semicolons on Windows and
   colons on macOS/Linux.

3. What does the __file__ variable contain?

   ANSWER:
   The __file__ variable contains the .py file's path as a string. For example,
   if you run yourScript.py in your home folder, it evaluates to something like
   'C:\Users\al\yourScript.py'. This is useful if you need to locate files that
   exist in the Python program's folder. Note: __file__ doesn't exist when you
   run the Python interactive shell.

4. What command erases the text from the terminal window on Windows? What about
   on macOS and Linux?

   ANSWER:
   Windows: cls
   macOS/Linux: clear

5. How do you create a new virtual environment?

   ANSWER:
   1. cd to your Scripts folder (or desired location)
   2. Run the venv module:
      Windows:     python -m venv .venv
      macOS/Linux: python3 -m venv .venv
   
   This creates a new virtual environment in a folder named .venv (or whatever
   name you specify).

6. What command line argument should you pass to PyInstaller when compiling
   programs?

   ANSWER:
   --onefile
   
   Full command:
   Windows:     python -m PyInstaller --onefile yourScript.py
   macOS/Linux: python3 -m PyInstaller --onefile yourScript.py
   
   Note: The argument has TWO dashes and must use capital P and capital I in
   PyInstaller.

===============================================================================
END OF CHAPTER 12 SUMMARY
===============================================================================
