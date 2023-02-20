""""
2023 2/20
1444 رَجَب 29

Numpy Arrays
"""
import numpy as np  # instead of writing numpy.something now we can just say np

# NumpyBasic - level library that handles list and arrays, handles using mathematics


# making a list
list_1 = np.array([1, 2, 3, 4])  # four direction vector
list_2 = np.array([5, 6, 7, 8])

print(list_1.shape)  # command such as shape in this case are called attributes
print(list_1 + list_2)  # it will add as vector value unlike python array

list_3 = np.array([  # 3 by 3 matrix
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(list_3.shape)
print(list_3)

# shortcut to make initialized array that has complex dimension
list_complex = np.zeros((5, 5, 5))  # np.value((X,Y,Amount))
list_complex_2 = np.full((3, 3, 3), 4)  # np.full((Dimension), Value)

print(list_complex)
print(list_complex_2)

"""
Extra others

Variable = np.empty((Dimension)) == will make the matrix table that has values that are not initialized
Variable = np.random.random((Dimension)) == Input random values
"""

# Making an array with given range that is increasing in arithmetic sequence
x = np.arange(0, 1000, 5)  # (start, end, term) ** doesn't include 1000 it self

print(x)
print(x.size)  # to know the amount of values in the array

y = np.linspace(0, 100, 5)  # (start, end, amount) will print evenly distributed number of range in given amount

print(y)
"""
z = np.sin(x)
print(z)

this way it will print all the sin value of the arithmetic sequence with term of 5
"""

"""
Quick 日記
Back to lessons XD,
I will do data science first then do two projects.
One thing that might pull me back is that I don't have
enough mathematical knowledge for data science since I didnt
learned the math to do data science.
still I can do basic level such as vectors and algebra
so goodae
"""
