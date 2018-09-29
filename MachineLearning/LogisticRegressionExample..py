import pandas as pd
import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
from ArrayUtil import one_dim_array_reshape

file_name = "DataSets/LogisticRegression/ex2data1.txt"
data = pd.read_csv(file_name, names=['X1', 'X2', 'Y'])

#normalize Data

features = data[['X1','X2']]
scalerX = StandardScaler().fit(features)
data[['X1','X2']] = scalerX.transform(features)



train, test = train_test_split(data, test_size=0.3)
X_train = train[['X1','X2']]
Y_train = train['Y']
X_test = test[['X1','X2']]
Y_test = test['Y']
model = LogisticRegression.GradientDescent(maxIterations=10000,alpha=0.01)
model.fit(X_train.values,Y_train.values)

# Plot regressão logistica
predictions = [model.predict(x) for x in np.insert(X_test.values, 0, 1, axis=1)]

# X_test[['X1','X2']] = scalerX.inverse_transform(X_test)
reta = -(model.W[0] + model.W[1] * X_test['X1']) / model.W[2]

plt.scatter(X_test['X1'], X_test['X2'], c=Y_test)
plt.plot(X_test['X1'], reta)
plt.title('Regressão Logistica (Gradiente Descendente)')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()

# Plot Erro
plt.plot(model.ErrorPlot)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()