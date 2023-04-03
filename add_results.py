import sqlite3

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def create_results(user_id, assessment_id, score, assessment_date, admin_id):
       

    insert_sql ='''INSERT INTO AssessmentResults(user_id, assessment_id, score, assessment_date, admin_id)
    values(?,?,?,?,?);'''
    values = (user_id, assessment_id, score, assessment_date, admin_id,)
    cursor.execute(insert_sql,values)
    connection.commit()
    print(f'Success: Results was Successfully added!!!!')

def add():
    user_id = input('Please enter user ID: ')
    assessment_id = input('Please enter assessment number: ')
    score = input('Please enter score recived 0-4: ')
    assessment_date = input('Please enter the date of the assessment taken yyyy-mm-dd: ')
    admin_id = input('Please enter Admin ID:')

    create_results(user_id, assessment_id, score, assessment_date, admin_id)

add()