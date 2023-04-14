import sqlite3
import bcrypt
from my_class import *

def add_user(values):
    connection = sqlite3.connect('courtneys_capstone.db')
    db_cursor = connection.cursor()

    #class_user = User(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
    
    users ="""INSERT INTO Users (first_name,last_name,phone,email,password,date_created,hire_date,
        user_type) values(?,?,?,?,?,?,?,?);"""

    values = []
    first = input('Please add a first name: ')
    last = input('Please add a last name: ')
    phone = input('Please add a phone number: ')
    email = input('Please add an email: ')
    password = input('Please add a password: ')
    date_created = input('Please add the date the user was created: ')
    date_hired = input('Please add the date the user was hired: ')
    user_type =input('Please add the user type: ')

    first.append(values)
    last.append(values)
    phone.append(values)
    email.append(values)
    password.append(values)
    date_created.append(values)
    date_hired.append(values)
    user_type.append(values)

    db_cursor.execute(users,(values.first, values.last, values.phone, values.email,(values.password).decode(),values.date_created,values.hire_date,values.user_type))
    connection.commit()
    print(f'Success: user "{values.first}')
#add_user()