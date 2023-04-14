import sqlite3
import bcrypt
from my_class import *
from view import *
from user_update import *
from export import *
from create_user import *
from edit import *
from add_assess import *
from add_results import *
from add_comp import *

menu_prompt = '''***** Manager Competency Tool *****
Please choose an option from below:
        1) View all Competencies
        2) View all Assessment Results
        3) Update user information
        4) View all Users
        5) Add a User
        6) Add a Competency
        7) Add an Assessment
        8) Add an Assessment Result
        9) Edit a User
        10) Edit a Competency
        11) Edit an Assessment
        12) Edit and Assessment Result
        13) Delete an Assessment Result
        14) Search for a User
        15) View a Users Assessments
        16) Exit
Your selection: 
'''

def admin_menu():
    while(user_input := input(menu_prompt)) != "4":
        if user_input == "1":
            prompt_view_comp()
        elif user_input == "2":
            pass
        elif user_input == "3":
            prompt_update_user() 
        elif user_input == "4":
            view_all()
        elif user_input == "5":
            add_user()
        elif user_input == "6":
            add_comp()
        elif user_input == "7":
            add_assess()
        elif user_input == "8":
            add_results()
        elif user_input == "9":
            update_user()
        elif user_input == "10":
            edit_comp()
        elif user_input == "11":
            edit_assess()
        elif user_input == "12":
            edit_results()
        elif user_input == "13":
            delete_results()
        elif user_input == "14":
            view_user()
        elif user_input == "15":
            view_assess()
        elif user_input == "16":
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

#admin_menu()