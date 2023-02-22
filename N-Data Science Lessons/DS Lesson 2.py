"""
2023 2/22
1444 شَعْبَان 2

Numpy Functions
"""
import numpy as np

# mathematical functions
List_1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(np.cos(List_1))  # simple conversion

print(np.sum(List_1))  # aggregate function
"""
Like above there are alot we can input

- simple conversion
cos, sin, tan
exp(e) ,sqrt, log

- aggregate function
sum, subtract, max, min
mean, median, std(standard deviation)

"""

# shape manipulation function
List_2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
])

List_2_change = List_2.reshape((2, 6))  # putting values in 2 row with 6 each
"""
Like above there are alot we can input

.flatten()  == change it to one dimensional list
.transpose()  == making dimension inverse

"""

# joining and separating array
List_3 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
])

List_4 = np.array([
    [11, 22, 33, 44],
    [55, 66, 77, 88],
    [99, 10, 11, 22]
])

join = np.concatenate((List_3, List_4))
print(join)

"""
Like above there are alot we can input

.concatenate(())  == joining the function directly (dimension changes)
.stack(())  == joining under one array but shapes stay the same (two shapes)
.hstack == joining the function onto other horizontally (line 1 of each are now 1 row)
.vstack == same as concatenate
"""

split = np.split(List_3, 3)  # splitting each row of array to individual array
print(join)

# adding value
List_5 = np.array([
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 0, 1],
    [2, 3, 4, 5]
])

new = [6, 7, 8, 9]
List_5 = np.append(List_5, [new], axis=0)

print(List_5)

"""
- append
we have to put [], 
because if we dont then it will flatten the array because the dimension the "new" is different from "List_5"

- insert
List_5 = np.insert(main, row, target, axis=column)
we can enter any row if we are planning to add as a column 
This will change the dimensions 
"""

"""
Quick 日記
There is scientific mode in pycharm
where I can directly draw graph and 
work with spreadsheet XD, I try 
that for upcoming project.
"""
