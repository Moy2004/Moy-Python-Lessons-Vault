"""
2023 2/24
1444 شَعْبَان 4

Data visualization (Types of chart pt.1)
"""
import matplotlib.pyplot as plt
import numpy as np

# Barchart  -- LESSON 6
# demonstrating skill of 4 people of 4 different type of programming language

# y values
python = (85, 67, 23, 98)  # regular pyhon tuple
java = (50, 67, 89, 14)  # in order skill of (person1, 2, 3, 4)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

# x values
people = ['Bob', 'Hannah', 'Ava', 'OEUO']
# ** Ovuvuevuevue Enyetuenwuevue Ugbemugbem Osas = OEUO

index = np.arange(4)  # creating four x value

# plotting bar, these four plot are one set under arrange so its 4x4
plt.bar(index, python, width=0.2, label='python')
plt.bar(index + 0.2, java, width=0.2, label='java')  # added 0.2, so it doesn't overlap for person
plt.bar(index + 0.4, networking, width=0.2, label='networking')
plt.bar(index + 0.6, machine_learning, width=0.2, label='machine_learning')

plt.title("IT Skill Level")

plt.xlabel("Person")
plt.ylabel("Skill Level")

plt.xticks(index + 0.2, people)  # putting individual name under bar. (Where, What)

plt.legend(loc='upper left')
plt.ylim(0, 140)  # Limit of y value

plt.show()

# Pie chart  -- LESSON 7
# will track Region of origin of student

region = ["East Asian", "South East Asian", "South Asian", "West Asian", "Western"]
student = (60, 20, 40, 20, 30)

# to organize the chart in either descending or ascending order
pairs = zip(student, region)  # way to organize the information as dictionary -> prints [(60, 'East Asia)...]
pairs = sorted((list(pairs)))  # soring list of (pair) in small -> big
student, region = zip(*pairs)  # after sorting the list, unzipping so we can access

explode = [0, 0, 0.1, 0, 0]  # how much distance you want to make from the center of the circle
# gave distance to West cause it is not in Asia, == easy to read
# ** HAVE TO PUT AFTER ZIPPING because the order is changed and undesired target might change it distance

plt.pie(student, labels=region, autopct="%.2f%%", explode=explode, startangle=90)
# auto-pct = percentage, %.2f%% = percent round up to two digit

plt.title("Student Region of Origin")

plt.show()

"""
Quick 日記
It's been so long that I only been 
using standard XY graph XD.
"""

