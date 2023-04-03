import sqlite3

def create_schema(cursor):
    with open('schema.sql', 'r') as infile:
        schema = infile.read()
        cursor.executescript(schema)
        connection.commit()
connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

create_schema(cursor)