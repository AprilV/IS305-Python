# CHAPTER 12 - SECTION 4: POP-UP MESSAGE BOXES - Practice

# IMPORTANT: This section requires the pymsgbox module
# RUN THIS COMMAND IN YOUR TERMINAL FIRST (not in Python):
# python -m pip install pymsgbox
# On Ubuntu Linux: sudo apt install python3-tk (then install pymsgbox)
# NOTE: These create GUI pop-up windows, not terminal output


# Q1: Import pymsgbox module
# WHAT IT DOES: Loads the pymsgbox module so you can create GUI pop-up dialogs
# Example: import sys
import pymsgbox



# Q2: Display an alert message 'Legendary item dropped in Path of Exile!' using pymsgbox.alert(), store return value in 'loot_response', print loot_response
# WHAT IT DOES: Shows a pop-up window to notify user - like when Brady throws a touchdown or your favorite metal band releases a new album
# Example: nfl_alert = pymsgbox.alert('Chiefs win the Super Bowl!')
# Example: print(nfl_alert)
response = pymsgbox.alert('Task is complete and dies in your belly')
print(response)


# Q3: Display a confirm dialog 'Engage warp drive to next sector?' using pymsgbox.confirm(), store return value in 'kirk_decision', print kirk_decision
# WHAT IT DOES: Asks user to make a choice with OK/Cancel buttons - like confirming fourth quarter decisions or deleting old Windows XP files
# Example: playoff_choice = pymsgbox.confirm('Go for 2-point conversion?')
# Example: print(playoff_choice)
choice = pymsgbox.confirm('So you want to DIE!!!!')
print(choice)



# Q4: Display a confirm dialog 'Activate red alert status?' using pymsgbox.confirm(), store result in 'starfleet_command'. If starfleet_command == 'OK', print 'Red alert activated!', else print 'Remaining at yellow alert'
# WHAT IT DOES: Uses the user's choice to control what happens next - like running different plays based on coach's decision or installing Windows update
# Example: game_decision = pymsgbox.confirm('Challenge the ref call?')
# Example: if game_decision == 'OK':
# Example:     print('Challenge flag thrown')
# Example: else:
# Example:     print('Accepting the call')
user_choice = pymsgbox.confirm('Sean is a retarded fuck autistic piece of shit!')
if user_choice == 'OK':
    print('He should be removed')
else:
    print("He's already dead")





# Q5: Display a prompt dialog 'Enter your favorite Star Trek captain:' using pymsgbox.prompt(), store result in 'captain_name'. If captain_name is not None, print f'Live long and prosper, Captain {captain_name}!', else print 'No captain selected'
# WHAT IT DOES: Gets text input from user via pop-up box - easier than terminal input for getting Path of Exile character names or NFL team picks
# Example: qb_name = pymsgbox.prompt('Enter best quarterback:')
# Example: if qb_name is not None:
# Example:     print(f'{qb_name} leads the league')
# Example: else:
# Example:     print('No QB entered')
user_death = pymsgbox.prompt("How would you like to DIE!!!!!!!")
if user_death is not None:
    print(f'user_death: {user_death}')
else:
    print("You're already a fucking corpse")



# Q6: Display a password dialog 'Enter Starfleet security code:' using pymsgbox.password(), store result in 'security_code'. If security_code is not None, print 'Access granted to bridge' (don't print actual password!), else print 'Access denied - no code entered'
# WHAT IT DOES: Like prompt() but hides what they type with dots/asterisks - for getting passwords or Windows product keys securely
# Example: game_pin = pymsgbox.password('Enter fantasy football PIN:')
# Example: if game_pin is not None:
# Example:     print('League access granted')
# Example: else:
# Example:     print('No PIN provided')
pwd = pymsgbox.password('Enter your password:')
if pwd is not None:
    print('Password received')
else:
    print('No way buddy!')