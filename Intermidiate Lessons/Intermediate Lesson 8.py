"""
2023 1/4 ~ 2023 1/5
1444  جُمَادَىٰ ٱلثَّانِي 11 ~ 1444  جُمَادَىٰ ٱلثَّانِي 12

Database Programming
"""
# Database Programming
# one of the most important and popular way to store data in computer science

import sqlite3  # SQL = Structured Query Language -- sq-lite3 sql for python

# create database
connection = sqlite3.connect('mydata.db')  # connecting to existing or creating new file/database

# cursor
# to execute sql database query, we need cursor - its like an interface of database
cursor = connection.cursor()

# creating database(in this case table) in pure sql
cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""") # this creates new empty table with three columns

# insert data
cursor.execute("""
INSERT INTO persons VALUES
    (1,'Moy', 'Man', 18),
    (2,'Sashko', 'Man', 18),
    (3,'Sasuke', 'Uchina', 18)
""")  # don't forget to add , after ()

cursor.execute("""
SELECT * FROM persons
WHERE last_name = 'Man' 
""")  # specific which specific data we want to pull out

rows = cursor.fetchall()  # putting data into variable
print(rows)

# everything we wrote will not apply until we commit

connection.commit()

connection.close()

# we will get error twice we run the code because we already made the table once - encountered by IF NOT EXIST

"""
This Lesson continues to file Intermediate Lesson 8-2.py
"""

