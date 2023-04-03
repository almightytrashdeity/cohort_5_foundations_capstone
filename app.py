import sqlite3
import csv
from my_class import *
from check_pass import login
from create_user import *


connection = sqlite3.connect('courtneys_capstone.db')
c = connection.cursor()

menu_prompt = """********Competency Tool**********
Please choose one of these options:
        1) Login with Username(email)
        2) Create a User
        3) Exit
Your Selection: 
"""
def menu():
    while(user_input := input(menu_prompt)) != "3":
        if user_input == "1":
            login()
        elif user_input == "2":
            prompt_create_user()
        elif user_input == "3":
            exit()
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