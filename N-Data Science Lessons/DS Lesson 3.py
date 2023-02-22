"""
2023 2/22
1444 شَعْبَان 2

Plotting Functions with Matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt

# matplotlib - plots the function to the graph

x = np.linspace(-100, 100, 201)
y = 0.5 * x ** 2 + 2 * x  # y = 0.5x^2 + 2x
y1 = np.sin(x) * 2000

plt.plot(x, y)
plt.plot(x, y1, 'r--')  # adding color and type of line r-- == red dotted line

plt.show()

"""
Quick 日記
This is getting fun,
graphing and data visualization
"""