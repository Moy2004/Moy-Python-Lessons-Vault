"""
2023 4/1
1444 رَمَضَان 10

K-Nearest Neighbors Classification
"""
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# K-Nearest Neighbors Classification (Supervised Learning)
# Allows us to classify unknown data by looking at data that already exist
# finding the nearest values(neighbors) of the number and assign the same category as its neighbors

data = load_breast_cancer()
print(data.feature_names)  # value data
print(data.target_names)  # classification

x_train, x_test, y_train, y_test = train_test_split(np.array(data.data), np.array(data.target), test_size=0.2)
# take value and classification data as numpy array, then split 20% into test and other to training

clf = KNeighborsClassifier(n_neighbors=3)  # how many neighbouring data we want to look at.
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))  # testing how well it is trained - accuracy

"""
to predict we put write this, 
clf.predict([]) 

and then input the data below and we will get if cancer exist or not

['mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension']
"""

"""
Quick 日記
Im scared of hospital things (not scared of dentist or vaccines)
but like these kind so my heart was beating entire time I was
doing this XDDDDDDDD
"""

