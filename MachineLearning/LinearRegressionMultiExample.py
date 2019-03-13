import pandas as pd
import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

file_name = "DataSets/LinearRegression/ex1data2.txt"
data = pd.read_csv(file_name, names=['X1', 'X2', 'Y'])

#normalize Data
scalerX1 = StandardScaler().fit(data[['X1']])
data['X1'] = scalerX1.transform(data[['X1']])

scalerX2 = StandardScaler().fit(data[['X2']])
data['X2'] = scalerX2.transform(data[['X2']])

scalerY = StandardScaler().fit(data[['Y']])
data['Y'] = scalerY.transform(data[['Y']])

train, test = train_test_split(data, test_size=0.3)
X_train = train[['X1','X2']]
Y_train = train['Y']
X_test = test[['X1','X2']]
Y_test = test['Y']
model = LinearRegression.GradientDescent(maxIterations=10000,alpha=0.01)
model.fit(X_train.values,Y_train.values)


# Teste
# predictions = [model.predictions(x) for x in X_test.values]

# plt.plot(X_test,Y_test,'o',X_test,predictions)
# plt.title('Regressão Linear (Gradiente Descendente)')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()


plt.plot(model.ErrorPlot)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()