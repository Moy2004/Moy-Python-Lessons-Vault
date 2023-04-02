"""
2023 4/2
1444 رَمَضَان 11

Support Vector Machines
"""
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np

# Support Vector Machines
# classifying data using ting call support vector

data = load_breast_cancer()

X = data.data
Y = data.target

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# training data set are always random so accuracy change if we want to keep same data set
# use random_state= #

# Kernel Function = Some graphs are hard to separate with line in 2D so by using Kernel it turns into 3D
# Soft Margin = How many error you want to allow, == C

clf = SVC(kernel='linear', C=3)  # there are many function we can use we are using linear separation (is fast)
clf.fit(x_train, y_train)

clf2 = KNeighborsClassifier(n_neighbors=3)  # using this to compare the accuracy
clf2.fit(x_train, y_train)

print(f'SVC: {clf.score(x_test, y_test)}')
print(f'KNN: {clf2.score(x_test, y_test)}')

"""
Quick 日記
These lessons are just giving me basic idea of 
how machine learning works, 
I should definitely study these more 
theoretically later 
"""
