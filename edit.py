import sqlite3
from view import *

connection = sqlite3.connect('courtneys_capstone.db')
cursor = connection.cursor()

def edit_assess(values, to_update):
    if type(values[1]) == str:
        query = f""" 
        UPDATE Assessments SET {to_update} = ?
        WHERE assessment_id = ?;
        """
    
    if type(values[1])== int:
        query =f""" 
        UPDATE Assessments SET {to_update} = ?
        WHERE assessment_id = ?;
        """
    cursor.execute(query,values)
    connection.commit()

def edit_results(values, to_update):
    if  type(values[1]) == str:
        query = f"""
        UPDATE AssessmentResults SET {to_update} = ?
        WHERE assessment_id = ?"""

    if type(values[1]) == int:
        query = f"""
        UPDATE AssessmentResults SET {to_update} = ?
        WHERE assessment_id = ?"""
    cursor.execute(query, values)
    connection.commit()

def edit_comp(values, to_update):
    if type(values[1]) == str:
        query = f""" 
        UPDATE Competencies SET {to_update} = ?
        WHERE competency_id = ?;
        """
    
    if type(values[1])== int:
        query =f""" 
        UPDATE Competencies SET {to_update} = ?
        WHERE competency_id = ?;
        """
    cursor.execute(query,values)
    connection.commit()

def delete_results():
    query = f"""
    SELECT * FROM AssessmentResults 
    WHERE assessment_id = ?"""
    delete = input("Are you sure you want to delete these results?")
    if delete.lower() == "yes":
        q = f"""
        DELETE * FROM AssessmentResults
        WHERE assessment_id = ?"""
        cursor.execute(q)
        connection.commit()
    if delete.lower() == "no":
        pass

    cursor.execute(query)
    connection.commit()