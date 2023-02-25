"""
2023 2/25
1444 شَعْبَان 5

Pandas Series
"""
import matplotlib.pyplot as plt
import pandas as pd

# pandas: efficiently manipulate and structure the data

# series
# two column table, ([values], [indexes])

series = pd.Series([10, 20, 30, 40], ('A', 'B', 'C', 'D'))

series.name = 'Pandas Series'  # name for series

print(series)

print(series['C'])  # get value of specific index
print(series.iloc[2])  # finding the index that have a value of integer 2

print(dict(series))  # converting series into dictionary

"""
Series are superior to Dictionary 
because dictionary are limited of what they can do,
unlike that series can do calculation and many other manipulation

Thing we can do with series ==
"""

s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([7, 5, 2, 1], ['c', 'b', 'a', 'd'])

print(s1 + s2)  # position are not very important when adding, it depends majorly on index

print(s1.head(1))  # getting first one row
print(s2.head(2))  # getting last two row


def mysquare(x):  # x^2 function
    return x ** 2


print(s1.apply(mysquare))  # applying function into series for calculation
print(s2.sort_index())

s2.sort_values(inplace=True)  # permanently sorting the series
print(s2)

# visualizing grpah with panda
Graph = pd.Series([31, 4, 13, 10], ['A', 'B', 'C', 'D'])

Graph.plot()
plt.show()

Graph.plot.pie()  # can draw many other type of graph direct like this
plt.show()

# exporting
# like below there are many types of to convert or export
Graph.to_string() # convert as a string
Graph.to_sql()  # export as sql

"""
Quick 日記
There wasn't much here
But one thing I did learned for sure
is that pandas is very flexible or
accessible way to
handle series or collection of data
"""
