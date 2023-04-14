import sqlite3

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def create_comp(competency_id, competency_name, creation_date):
    insert_sql = '''INSERT INTO Competencies (competency_id, competency_name, creation_date)
    values( ?,?,?,?,?);'''
    values = (creation_date,competency_id,competency_name,)
    cursor.execute(insert_sql, values)
    connection.commit()
    print(f'Success: Competency was Successfully added!!!!')

def add_comp():
    competency_name = input('Please enter competency name: ')
    creation_date = input('Please enter creation date yyyy-mm-dd: ')
    competency_id = input('competency_id: ')

    create_comp(competency_name, creation_date,competency_id)