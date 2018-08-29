#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:49:31 2018

@author: karan.ganesh.dumbre
"""
#### Install the library for microsoft sql server database

##### !conda install -c anaconda pymssql


import pymssql

cnx= {
      'host': 'mssqldb.c12wj3xlqsae.us-west-2.rds.amazonaws.com:1433',
      'username': 'test',
      'password': 'test123456',
      'db': 'tempDB'} 

conn = pymssql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])

# open connection
connection = pymssql.connect(cnx['host'], cnx['username'], cnx['password'], cnx['db'])
# open cursor
cursor = connection.cursor()
# query for creating table
create_table = """
                CREATE TABLE classroom ( 
                student_id INTEGER PRIMARY KEY, 
                name VARCHAR(20), 
                gender CHAR(1), 
                physics_marks INTEGER,
                chemistry_marks INTEGER,
                mathematics_marks INTEGER
              );"""
# execute query
cursor.execute(create_table)
# commit changes
connection.commit()

# sample data
classroom_data = [( 1, "Raj","M", 70, 84, 92),
                  ( 2, "Poonam","F", 87, 69, 93),
                  ( 3, "Nik","M", 65, 83, 90),
                  ( 4, "Rahul","F", 83, 76, 89)]

# open cursor
cursor = connection.cursor()
# insert each student record
for student in classroom_data:
    # formatted query string
    insert_statement = """INSERT INTO classroom 
                      (student_id, name, gender, physics_marks, chemistry_marks, mathematics_marks)
                      VALUES 
                      ({0}, '{1}', '{2}', {3}, {4}, {5});""".format(student[0], student[1], student[2], 
                                                              student[3],student[4], student[5])
    # execute insert query
    cursor.execute(insert_statement)

# commit the changes
connection.commit()

# open cursor
cursor = connection.cursor()
# query
query = "SELECT * FROM classroom"
# execute query
cursor.execute(query) 
# fetch results
result = cursor.fetchall() 
# print results
for row in result:
    print(row)
    
# close connection
connection.close()