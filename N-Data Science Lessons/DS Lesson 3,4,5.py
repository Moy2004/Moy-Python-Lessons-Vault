"""
2023 2/22 ~ 2023 2/23
1444 شَعْبَان 2 ~ 1444 شَعْبَان 3

Data visualization (Basic Graphing)

note: this was several lessons but since they were too short of a code,
I combined them under one file.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

# matplotlib - plots the function to the graph


# Plotting Functions with Matplotlib  -- Lesson 3
x = np.linspace(-100, 100, 201)
y = 0.5 * x ** 2 + 2 * x  # y = 0.5x^2 + 2x
y2 = np.sin(x) * 2000

plt.plot(x, y)
plt.plot(x, y2, 'r--')  # adding color and type of line r-- == red dotted line

plt.show()

# Subplots and Multiple Windows  -- Lesson 4
# Subplots == having multiple graphs in one window

x = np.arange(0, 100, 1)

y = 0.5 * x ** 2 + 2 * x  # y = 0.5x^2 + 2x
y2 = np.sin(x) * 2000

y3 = np.arctan(x)
y4 = np.cos(x)

plt.figure(1)  # window 1
axis_1 = plt.subplot(211)  # 211 == three digit integer == (row+column+index)
axis_2 = plt.subplot(212)  # row and column are placement of graph (where you want graph to be placed)

axis_1.plot(x, y)
axis_2.plot(x, y2)

plt.figure(2)  # window 2
axis_3 = plt.subplot(121)
axis_4 = plt.subplot(122)

axis_3.plot(x, y3)
axis_4.plot(x, y4)

plt.tight_layout()  # Help organize graph, so it doesn't overlap on each other + perfect margin

plt.show()

# Matplotlib Styling  -- Lesson 5
style.use('bmh')  # theme of the graph https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

x = np.arange(0, 20, 0.2)
y = np.sin(x)

plt.title('Main Title')
plt.suptitle("Above Title")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.plot(x, y, label='Line 1')  # lable is the name for function
plt.legend(loc='upper left')  # put the legend/name of the function

plt.show()
