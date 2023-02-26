"""
2023 2/26
1444 شَعْبَان 6

Pandas Data Frames

Pandas DataFrames are a two-dimensional labeled data structure used for analyzing and manipulating data in Python.
They allow for easy selection and filtering of rows and columns, grouping data, merging multiple DataFrames, and more.
- CHATGPT
"""
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'number': [31, 1, 16, 14],
    'name': ['moy', 'hong', 'sashko', 'bobo'],
    'age': [18, 18, 18, 19],
    'height': [185, 200, 182, 165],
    'gender': ['m', 'm', 'm', 'f']
}

Data_Frame = pd.DataFrame(data)  # converting to data frame
Data_Frame.set_index('number', inplace=True)  # this way we can assign specific name or number to column

print(Data_Frame)
print(Data_Frame.T)  # swapping row and columns

print(Data_Frame['name'].iloc[0])  # getting specific value
"""
can use attributes learn from previous lessons

print(Data_Frame.head(2))  # print first two 
print(Data_Frame.ndim)  # dimension
print(Data_Frame.shape)  # shape
print(Data_Frame.dtypes)  # give data type
"""

Data_Frame.hist() # plotting all the useful values automatically
plt.show()

"""
Quick 日記
This will be very useful
when dealing with large data
such as machine learning or stock data
XDDDDDDD
ez graphing
"""