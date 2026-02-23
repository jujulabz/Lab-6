"""

User Login System,
Melissa Palmer,
The program t simulates a user login
system using a dictionary to store usernames
and passwords.,
I used the textbook chapter 5 for the if staetments as well as Chapter 6 from our textbook for libaires
and i used https://www.geeksforgeeks.org/python/nested-if-statement-in-python/ for the if statement as well.

2/22/26

"""
#dictonary of users and passwords
user = {'guest': 'guest',
            'Green0':'Red0',
            'Chesse': 'Burger2',
            'mpalmer33': 'login65'
            }

username = input(f'Enter Username: ') #user input im asking for the users username

if username not in user:
    print('User not found') #if the user doesnt match anything inside my dictonary then the program tells users that the user can not be found
else:
    password = input(f'Enter Password: ') # now we go to the second condition if username is user then users get prompted to enter a password
    
    if password != user[username]: # if the password does not match the associated password with the username then access is denied
        print('\nAccess Denied.')
    
    else:
        if username == "guest": #here the program check if the user is the guest account 
            print(f"\nWelcome, {username}. You have Guest access.") # if true then prints out this welcome message this works for all other users in my dictonary
        else:
            print(f"\nWelcome, {username}. You have Security Level 1.") # prints out security level if all bools reult in true 
       