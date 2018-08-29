#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 12:20:53 2018

@author: karan.ganesh.dumbre
"""

import sqlite3

connection = sqlite3.connect('classroomDB.db')
connection.close()

connection = sqlite3.connect('classroomDB.db')
cursor = connection.cursor()

create_table = '''
                CREATE TABLE classroom (
                student_id INTEGER PRIMARY KEY,
                name VARCHAR(20),
                gender CHAR,
                physics_marks INTEGER,
                chemistry_marks INTEGER,
                mathematics_marks INTEGER
                );'''
                        
### Excecute Query
cursor.execute(create_table)


####connection commit
connection.commit()

###3 Connection Close
connection.close()


#### Insert Data

classroom_data = [(1,'RAJ','M',70,84,92),
                  (2,'POONAM','F',87,61,93),
                  (3,"NIK",'M',65,83,90),
                  (4,"RAHUL",'M',83,76,89)]

connection = sqlite3.connect('classroomDB.db')

cursor = connection.cursor()

for student in classroom_data:
    insert_statement = """ insert into classroom
                        (student_id,name,gender,physics_marks,chemistry_marks,mathematics_marks)
                        VALUES
                        ({0},'{1}','{2}',{3},{4},{5});""".format(student[0],student[1],student[2],student[3],student[4],student[5]);
                        
    cursor.execute(insert_statement);

####connection commit
connection.commit()

###3 Connection Close
connection.close()


#### Extract Data

connection = sqlite3.connect('classroomDB.db')
cursor = connection.cursor()

query = 'SELECT * FROM classroom'

cursor.execute(query)

result = cursor.fetchall()

for row in result:
    print(row)
    
connection.close()


