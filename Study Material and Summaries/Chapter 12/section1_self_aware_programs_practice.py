# CHAPTER 12 - SECTION 1: SELF-AWARE PYTHON PROGRAMS - Practice

# Q1: Import sys module, print value of sys.argv to see what starship mission parameters were passed
# WHAT IT DOES: Lets your program accept inputs when run from command line. Example: 'python enterprise.py engage' - you can grab 'engage' from sys.argv
# Example: import os
# Example: print(os.name)
import sys
print(sys.argv)

# Q2: Check if the captain gave any orders to the Enterprise. If len(sys.argv) > 1, print "Orders received", else print "Awaiting commands"
# WHAT IT DOES: Checks if user gave your program any inputs. sys.argv[0] is always the script name, so >1 means they passed actual arguments
# Example: if len(sys.argv) > 2:
# Example:     print("Multiple missions")
if len(sys.argv) > 1:
    print('Arguments provided')
else:
    print('No arguments')


# Q3: Print where Python is installed on your Windows system using sys.executable
# WHAT IT DOES: Shows where Python is installed - like finding the Windows 95 installation folder on your retro PC collection
# Example: import sys
# Example: print(sys.executable)
import sys
print(sys.executable)

# Q4: Print the Python version to check if it can run Path of Exile build calculator scripts using sys.version
# WHAT IT DOES: Lets you check what Python version is running - like checking if your system meets game requirements
# Example: import sys
# Example: print(sys.version)
import sys
print(sys.version)


# Q5: Check if your Python version is new enough for the Starfleet database (needs 3.10+) using sys.version_info.major and sys.version_info.minor
# WHAT IT DOES: Lets you check specific version parts - like NFL stats tracker requiring Python 3.10+ for advanced analytics. Major=3, Minor=14 means Python 3.14
# Example: print(sys.version_info.major)
# Example: print(sys.version_info.minor)
print (sys.version_info.major)
print (sys.version_info.minor)


# Q6: Import os module, detect if you're running on Windows (your favorite OS!) using os.name. If os.name == 'nt', print "Running on Windows!", else print "macOS or Linux detected"
# WHAT IT DOES: Detects what OS is running - useful for playing the Windows XP startup sound only on Windows systems
# Example: import os
# Example: if os.name == 'posix':
# Example:     print("Unix-like system")
import os
print(os.name)
if os.name == 'nt' :
    print("Windows")
else:
    print("macOS or Linux")


# Q7: Print the specific platform to determine which NFL game highlights folder to use (Windows vs Mac) using sys.platform
# WHAT IT DOES: More specific OS detection - 'win32' for Windows, 'darwin' for Mac, 'linux' for Linux - for loading platform-specific game files
# Example: import sys
# Example: print(sys.platform)
import sys
print(sys.platform)



# Q8: Try to import a Star Trek database module called 'borg_collective_data'. Use try/except to catch ModuleNotFoundError and print "Borg database not found - Install required modules!"
# WHAT IT DOES: Checks if a module is installed before using it - like checking if Path of Exile build calculator is installed before running loot analysis
# Example: try:
# Example:     import metalband_discography
# Example: except ModuleNotFoundError:
# Example:     print("Metal database missing")
try:
    import fakemodulethatdoesnotexist

except ModuleNotFoundError:
    print("I'ts not fucking there!!!!")