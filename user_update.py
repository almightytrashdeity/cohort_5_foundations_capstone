import sqlite3
from view import view_user

def update_user(values,to_update):
    connection = sqlite3.connect('courtneys_capstone.db')
    cursor =connection.cursor()

    if type(values[1]) == str:
        query = f""" 
        UPDATE Users SET {to_update} = ?
        WHERE first_name = ?;
        """
    
    if type(values[1])== int:
        query =f""" 
        UPDATE Users SET {to_update} = ?
        WHERE user_id = ?;
        """
    cursor.execute(query,values)
    connection.commit()
    #update_user(values, to_update)