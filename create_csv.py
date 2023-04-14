import csv
import sqlite3

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def create_csv():
    rows = cursor.execute('SELECT Users.first_name, Users.last_name, AssessmentResults.assessment_id, AssessmentResults.score, AssessmentResults.assessment_date FROM AssessmentResults JOIN Users ON AssessmentResults.user_id = Users.user_id').fetchall()

    header = [row[0] for row in cursor.description]
    with open('competency.csv', 'w') as my_csv:
        for row in rows:
            row = ','.join([str(i) for i in row])
            my_csv.write(row + '\n')

    print(str(len(rows)) + ' rows written seccessfully to ')

def single_csv():
    name = input('Please enter a  users ID: ')
    query = 'SELECT Users.first_name, Users.last_name, AssessmentResults.assessment_id, AssessmentResults.score, AssessmentResults.assessment_date FROM AssessmentResults JOIN Users ON AssessmentResults.user_id = Users.user_id WHERE AssessmentResults.user_id = ?'
    rows = cursor.execute(query, name).fetchall()

    header = [row[0] for row in cursor.description]
    with open('competency.csv', 'w') as my_csv:
        for row in rows:
            row = ','.join([str(i) for i in row])
            my_csv.write(row + '\n')

    print(str(len(rows)) + ' rows written seccessfully to ')
    
    
#create_csv()
single_csv()