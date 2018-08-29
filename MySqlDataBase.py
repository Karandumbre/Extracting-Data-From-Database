#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:26:24 2018

@author: karan.ganesh.dumbre
"""
### Execute the below statement for MYSQL Database
#### !conda install -c anaconda pymysql

import pymysql

### To create a connection to mysql database, we need first the database. 
###So create database using mysql workbench

# Connection details
# Connect to the database
connection = pymysql.connect(host='localhost',  
                       port=3306,  
                       user='root',  
                       passwd='<your_password>',  
                       db='classroom',  
                       charset='utf8')  


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
                      ({0}, "{1}", "{2}", {3}, {4}, {5});""".format(student[0], student[1], student[2], 
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



