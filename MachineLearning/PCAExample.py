import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from scipy.io import loadmat

mat = loadmat('DataSets/KMeans_PCA/ex7data1.mat')
data = mat['X']
scalerX = StandardScaler().fit(data)
data = scalerX.transform(data)
print('Dimensao Antes do PCA: ', data.shape[1])

pca = decomposition.PCA(n_components=1)
pca.fit(data)
result = pca.transform(data)
print('Dimensao Apos PCA: ', result.shape[1])

rebuild = pca.inverse_transform(result)
print('Dimensao Apos Reconstrucao: ', rebuild.shape[1])

data = scalerX.inverse_transform(data)
plt.plot(data[0],data[1], color='b', label='Antes PCA')

rebuild = scalerX.inverse_transform(rebuild)
plt.plot(rebuild[0],rebuild[1], color='r', label='Reconstruido')

plt.title('Diferenca Antes PCA Depois PCA (Reconstruido)')
plt.legend()
plt.show()
