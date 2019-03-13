import pandas as pd
from KMeans import KMeans
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

mat = loadmat('DataSets/KMeans_PCA/ex7data2.mat')
data = mat['X']

model = KMeans()
model.fit(data)

colors = ["r", "g", "c"]

for classification in model.classes:
	color = colors[classification]
	for sample in model.classes[classification]:
		plt.scatter(sample[0], sample[1], color = color,s = 30)

for centroid in model.centroids:
	plt.scatter(centroid[0], centroid[1], s = 130, marker = "x", color='black')
plt.show()

