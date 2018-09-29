import pandas as pd
import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
from ArrayUtil import one_dim_array_reshape

file_name = "DataSets/LinearRegression/ex1data1.txt"
data = pd.read_csv(file_name, names=['X', 'Y'])

#normalize Data
scalerX = StandardScaler().fit(data[['X']])
data['X'] = scalerX.transform(data[['X']])

scalerY = StandardScaler().fit(data[['Y']])
data['Y'] = scalerY.transform(data[['Y']])

train, test = train_test_split(data, test_size=0.3)
X_train = train['X']
Y_train = train['Y']
X_test = test['X']
Y_test = test['Y']
model = LinearRegression.GradientDescent(maxIterations=10000,alpha=0.1)
model.fit(one_dim_array_reshape(X_train.values),one_dim_array_reshape(Y_train.values))

# Plot regressão linear
predictions = [model.predict(x) for x in np.insert(one_dim_array_reshape(X_test.values), 0, 1, axis=1)]
X_test = scalerX.inverse_transform(X_test)
Y_test = scalerY.inverse_transform(Y_test)
predictions = scalerY.inverse_transform(predictions)
plt.plot(X_test,Y_test,'o',X_test,predictions)
plt.title('Regressão Linear (Gradiente Descendente)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Plot Erro
plt.plot(model.ErrorPlot)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()