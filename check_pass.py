import bcrypt
import sqlite3
from admin import admin_menu
from user import user_menu

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def login():
    username = input('/nPlease enter your username: ')
    password = input('\nPlease enter your password: ')

    result = cursor.execute('SELECT user_id, password FROM Users WHERE email = ? AND active = 1', (username,)).fetchone()
    if not result:
        print('Wrong username, please try again')
    hashed_pw = result.encode()
    encoded_pw = password.encode('utf-8')
    check_password = bcrypt.checkpw(encoded_pw, hashed_pw)
    if check_password:
        print('Check Password result ----', end = '')

def is_manager(username):
    user = cursor.execute('SELECT user_type FROM Users WHERE email = ?', (username,)).fetchone()
    print(user)
    print('Hello from is_manager()')
    if user[0].lower() == 'admin':
        admin_menu()
    if user[0].lower() == 'user':
        user_menu()