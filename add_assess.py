import sqlite3

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def create_assessment(assessment_type,assessment_description,due_date,creation_date,competency_id):
    insert_sql = '''INSERT INTO Assessments (assessment_type,assessment_description,due_date,creation_date,competency_id)
    values( ?,?,?,?,?);'''
    values = (assessment_type,assessment_description,due_date,creation_date,competency_id,)
    cursor.execute(insert_sql, values)
    connection.commit()
    print(f'Success: assessment was Successfully added!!!!')

def add_assess():
    assessment_type = input('Please enter assessment type: ')
    assessment_description = input('Please enter assessment description: ')
    creation_date = input('Please enter creation date yyyy-mm-dd: ')
    due_date = input("Please enter due date yyyy-mm-dd: ")
    competency_id = input('competency_id: ')

    create_assessment(assessment_type,assessment_description,due_date,creation_date,competency_id)

#add()