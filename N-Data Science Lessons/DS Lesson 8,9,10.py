"""
2023 2/24
1444 شَعْبَان 4

Data visualization (Types of chart pt.2)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # belongs to matplotlib, == allows 3d visualization

"""
use this,
if want to see interactive figure instead of png

import matplotlib
matplotlib.use('TkAgg')
"""

# histogram -- LESSON 8
# will visualize height of the students

mu, sigma = 172, 8  # average, standard deviation
x = mu + sigma * np.random.randn(10000)  # avg + (SD *, randn == random normal distribution

plt.hist(x, 100, facecolor="blue", density=True)  # (target, amount, extra...), density = percentage

plt.title("Height of Students")

plt.xlabel("Heights")
plt.ylabel("Percentage of students")

plt.text(145, 0.04, "μ = 172, Σ = 8", fontsize='12')  # text(x axis, y axis, "text")
plt.grid(True)

plt.show()

# scatter plots -- LESSON 9

x = np.random.randn(50)
y = np.random.randn(50)

plt.scatter(x, y, c='red', marker='x', s=50)
plt.show()

# 3D plotting -- LESSON 10

# line
ax = plt.axes(projection="3d")  # specifying axes/dimension

z = np.linspace(0, 30, 100)
x = np.sin(z)
y = np.cos(z)

ax.plot3D(x, y, z)  # plotting 3d

plt.show()

# surface
ax2 = plt.axes(projection="3d")


def z_function(x, y):  # just another way to get value
    return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)  # converting vectors into matrices
Z = z_function(X, Y)

ax2.plot_surface(X, Y, Z)

plt.show()


"""
Quick 日記
From these lesson not only
it teach me how to graph in python.
But it gave me good understanding of how different
graphs work mathematically behind
XD that was fun
"""
