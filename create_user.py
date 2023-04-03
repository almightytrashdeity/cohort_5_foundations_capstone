import sqlite3
import bcrypt
from my_class import *

def add_user(values):
    connection = sqlite3.connect('courtneys_capstone.db')
    db_cursor = connection.cursor()

    class_user = User(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
    
    users ="""INSERT INTO Users (first_name,last_name,phone,email,password,date_created,hire_date,
        user_type) values(?,?,?,?,?,?,?,?);"""
    first_name = values[0]
    first_name = class_user.first_name
    last_name = class_user.last_name
    phone = class_user.phone
    email = class_user.email
    password = (class_user.password).decode()
    date_created = class_user.date_created
    hire_date = class_user.hire_date
    user_type = class_user.user_type

    db_cursor.execute(users,(values.first_name, values.last_name, values.phone, values.email,(values.password).decode(),values.date_created,values.hire_date,values.user_type))
    connection.commit()
    print(f'Success: user "{values.first_name}')