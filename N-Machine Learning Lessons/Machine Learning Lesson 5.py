"""
2023 4/17
1444 رَمَضَان 26

K-Means Clustering
"""
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

# K-Means Clustering (Unsupervised Learning)
# In this learning method there is no classification, rather finding data set and creating a cluster to determine
# K = means how many cluster we want to make in the data set
# when each cluster is generated the centroid is randomly assigned in the data set, and data set form
# a cluster with the centroid that is nearest to them, and it is done few times till the accuracy increases

digit = load_digits()
data = scale(digit.data)

model = KMeans(n_clusters=10, init='random', n_init=10)  # (amount of cluster, initialize method, IM but diff points  )
model.fit(data)

model.predict([...])