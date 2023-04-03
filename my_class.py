import sqlite3
import bcrypt

class User():

    def __init__(self, first_name, last_name, phone, email, password, active, date_created, hire_date, user_type):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.phone = phone
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt= bcrypt.gensalt())
        self.active = active
        self.date_created = date_created
        self.hire_date = hire_date
        self.user_type = user_type

    def change_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), salt= bcrypt.gensalt())

    def display_user(self):
        print(f'\n{self.first_name} {self.last_name}')
        print(f'{self.phone}\n {self.email}')
        print(f'\n{self.user_type}')

    def greet_user(self):
        print(f'\n Welcome to the Competency Tool, {self.first_name}!!!')