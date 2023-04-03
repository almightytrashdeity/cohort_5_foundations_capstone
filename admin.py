import sqlite3
import bcrypt
from my_class import *
from view import *
from user_update import *
from export import export_single_user, export_competencies

menu_prompt = '''***** User Competency Tool *****
Please choose an option from below:
        1) View all Competencies
        2) View all Assessment Resutls
        3) Update user information
        4) Exit
Your selection: 
'''

def admin_menu():
    while(user_input := input(menu_prompt)) != "q":
        if user_input == "1":
            prompt_view_comp()
        elif user_input == "2":
            pass
        elif user_input == "3":
            prompt_update_user()    
        elif user_input == "q":
            exit()
        else:
            print("Invalid entry, please try again!")

def prompt_view_comp():
    user_id = input('Please enter User ID: ')
    export_single_user(user_id)

def prompt_update_user():
    first_name = input("Please type in a User's name: ")
    view_user(first_name)
    user_id = int(input("Please select ID to update: "))
    to_update = ('first_name','last_name','phone','email','password',)
    print("What would you like to update?: ")
    for option, i in enumerate(to_update):
        print(f'{option}: {i}')

    user_choice = input('\n')
    new_value = input('Please enter the updated information: ')
    update_user((new_value, user_id), to_update[int(user_choice)])
    print('Your update was successfull!!!!')
    view_user(first_name)
    input('Press enter to continue. ')

admin_menu()