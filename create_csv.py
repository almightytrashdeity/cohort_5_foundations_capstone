import csv
import sqlite3

def create_csv():
    connection = sqlite3.connect('courtneys_capstone.db')
    cursor = connection.cursor()
    rows = cursor.execute('SELECT user_id, assessment_id, score, assessment_date FROM AssessmentResults').fetchall()

    header = [row[0] for row in cursor.description]
    for row in rows:
        row = ','.join([str(i) for i in row])
        with open('competency.csv', 'a') as my_csv:
            my_csv.write(row + '\n')

    print(str(len(rows)) + ' rows written seccessfully to ')
    