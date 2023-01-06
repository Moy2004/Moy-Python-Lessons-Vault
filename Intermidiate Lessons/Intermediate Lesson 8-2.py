"""
2023 1/4 ~ 2023 1/5
1444  جُمَادَىٰ ٱلثَّانِي 11 ~ 1444  جُمَادَىٰ ٱلثَّانِي 12

Database-Programming with Object-Oriented Programming
"""
import sqlite3

# Load Data
# will load database entries into a script as an object (other way around as well)

class Person:

    def __init__(self, id_number=-1, first='', last='', age=-1):
        # if we don't initialize we have to manually input the data (ex. p1 = Person(data))
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age

        self.connection = sqlite3.connect('mydata.db')  # connecting to database made from previous script
        self.cursor = self.connection.cursor()

    # method that loads in the person from the table then converts into a python object
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM persons 
        WHERE id = {}
        """.format(id_number))  # finding a person using ID number

        results = self.cursor.fetchone() # fetch-one = only bring first one when there are several same data
                                         # but since everyone have diff ID it's going to bring correct one

        self.id_number = id_number
        self.first = results[1]  # 0 is id XD incase forgot
        self.last = results[2]
        self.age = results[3]

    # method that insert person data in to the table

    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO persons VALUES 
        ({}, '{}', '{}', {})
        """.format(self.id_number, self.first, self.last, self.age))

        self.connection.commit()

# printing and choosing person to load in from db
p1 = Person()
p1.load_person(1)  # ID 1 person
print(p1.id_number, p1.first, p1.last, p1.age)

# inserting and defining person to insert into db
p2 = Person(4, 'Desmond', 'Johnson', 28)
p2.insert_person()

connection = sqlite3.connect('mydata.db')  # have to make separate connection for inserting
cursor = connection.cursor()

cursor.execute("SELECT * FROM persons")  # we can do this way, used other way just so its readable XD

results = cursor.fetchall()
print(results)

connection.close()

"""
Quick 日記
今日はダイタシステムを作れる。
それ以外はAIをデータトレーニングできる。
だんだん見える、
世界がどうように作動するのか。
"""
