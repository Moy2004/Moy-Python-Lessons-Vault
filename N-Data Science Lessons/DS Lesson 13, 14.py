"""
2023 2/26
1444 شَعْبَان 6

Pandas Statistics, Sorting and Functions
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Pandas Data -- Lesson 13
data = {
    'number': [31, 1, 16, 14],
    'name': ['moy', 'hong', 'sashko', 'bobo'],
    'age': [18, 18, 18, 19],
    'height': [185, 200, 182, 165],
    'gender': ['m', 'm', 'm', 'f']
}

Data_Frame = pd.DataFrame(data)
Data_Frame.set_index('number', inplace=True)

print(Data_Frame.count())  # counting amount of element in each column. Can get specific using []
print(Data_Frame.sum())  # can do various calculation, have to choose which one

print(Data_Frame['height'].mean())  # getting mean value of height, can also do median
print(Data_Frame['height'].describe())  # get all other things in one attribute
"""
other we can use 

.mode, it finds the value that is used most often
.std, Standard deviation
.min and .max
"""

# Sorting and Functions -- Lesson 14
Data_Frame['height'].apply(np.sin)  # doing calculation directly
Data_Frame['height'].apply(lambda x: x * 100)  # Doing specific calculation

for row in Data_Frame.iterrows():  # iterating the values, individual
    print(row)

Data_Frame.sort_index(inplace=True)  # sorting by index
print(data)

Data_Frame.sort_values(by=['name', 'age'], inplace=True)  # sorting values
print(data)

"""
Quick 日記
XD, I wonder if there is a 
excel or spreadsheet mode in
pycharm, like you can see plotted graph
I want to see table on spreadsheet.
"""
