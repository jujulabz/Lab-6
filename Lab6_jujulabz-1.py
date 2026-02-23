"""

User Login System,
Melissa Palmer,
The program t simulates a user login
system using a dictionary to store usernames
and passwords.,
Any info about starter code (If used, where it came from, link, etc.), and the
Date.

"""

user = {'guest': 'guest',
            'Green0':'Red0',
            'Chesse': 'Burger2',
            'mpalmer33': 'login65'
            }

username = input(f'Enter Username: ')

if username not in user:
    print('User not found')
else:
    password = input(f'Enter Password: ')
    
    if password != user[username]:
        print('\nAccess Denied.')
    
    else:
        if username == "guest":
            print(f"\nWelcome, {username}. You have Guest access.")
        else:
            print(f"\nWelcome, {username}. You have Security Level 1.")
       