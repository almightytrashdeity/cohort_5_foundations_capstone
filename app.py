import sqlite3
import csv
from my_class import *
from check_pass import login
from create_user import *
from user import user_menu
from admin import admin_menu


connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

menu_prompt = """********Competency Tool**********
Please choose one of these options:
        1) Login with Username(email)
        2) Create a User
        3) Exit
Your Selection: 
"""

def menu(user_type):
    while True:
        prompt_input = input(menu_prompt)
        while prompt_input != "3":
            if prompt_input == "1":
                email = input("Enter your email: ")
                password = input("Enter your password: ")
                password_check = cursor.execute("SELECT password FROM Users WHERE email = ?", (email,)).fetchone()
                if password_check == None:
                    print("wrong email")
                    continue
                elif password_check == password:
                    if user_type == "user":
                        user_menu()
                    elif user_type == "manager":
                        admin_menu()
                else:
                    print("Invalid password, try again")
                    continue
            elif prompt_input == "2":
                prompt_create_user()
            else:
                print("Invalid entry, please try again!")


def prompt_create_user():
    first_name = input('Enter First Name:  ')
    last_name = input('Enter Last Name: ')
    phone = input('Enter Phone number (digits only please): ')
    email = input('Enter Email: ')

    password = input('Enter Password: ')
    date_created = input('Enter Today\'s date YYYY-MM-DD: ')
    hire_date = input('Enter hire date:')
    user_type = input('Enter your user infomation:')
    if not user_type:
        user_type = 'user'
    active = 1
    values = User(first_name, last_name, phone, email, password,active,date_created, hire_date, user_type)

    add_user(values)

    input("Press Enter to continue") 


menu()