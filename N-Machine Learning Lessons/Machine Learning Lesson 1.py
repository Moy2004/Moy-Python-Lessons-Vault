"""
2023 3/29
1444 رَمَضَان 7

Linear Regression
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Linear Regression (Supervised Learning)
"""
The purpose of linear regression is to take a bunch of data points and to 
draw a straight line right through them. This line should then be as near as possible to all the points. When we 
have found this line, we can use it to make predictions for future values. 
"""

time_studied = np.array([20, 3, 8, 22, 45, 10, 1, 15, 2, 15, 25, 13, 10, 10, 17, 7]).reshape(-1, 1)
scores = np.array([90, 65, 75, 92, 100, 80, 40, 95, 60, 85, 94, 83, 82, 87, 85, 78]).reshape(-1, 1)
# currently we have array in horizontal format, for sklearn we need vertical and reshape does that.

model = LinearRegression()  # training the model
model.fit(time_studied, scores)  # finding that line

plt.scatter(time_studied, scores)

# predicting the score based on hour studied
print(model.predict(np.array([30]).reshape(-1, 1)))

# plotting prediction line
plt.plot(np.linspace(0, 70, 100).reshape(-1, 1), model.predict(np.linspace(0, 70, 100).reshape(-1, 1)), 'r')

plt.ylim(0, 100)
plt.show()

# Testing
# here we will find how accurate and properly the model is trained
time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.3)
# taking 0.2 = 20% of the data for testing the model
model_2 = LinearRegression()
model_2.fit(time_train, score_train)

print(model_2.score(time_test, score_test))  # show the score in decimal
