import numpy as np

class GradientDescent(object):

    def __init__(self, alpha=0.1, maxIterations=1000):
        self.alpha = alpha
        self.maxIterations = maxIterations
        self.precision = 0.0000001

    def fit(self, entries, label):
        self.iterations = 0       
        # insert the constant column 1 in entries
        entries = np.insert(entries, 0, 1, axis=1)
        self.W = np.random.rand(len(entries[0]))
        Gradient = 0
        ErrorTotal = 0
        self.ErrorPlot = []
        while True:
            Gradient = 0
            ErrorTotal = 0
            for i in range(len(entries)):
                Hypothesis = sum(self.W * entries[i])
                Error = (Hypothesis - label[i])
                ErrorTotal += Error
                Gradient += Error * entries[i]
            self.W = self.W - (self.alpha * Gradient) / len(entries)
            self.ErrorPlot.append(ErrorTotal)
            if self.stopConditions(ErrorTotal): 
                break
        print(Gradient)

    def stopConditions(self, error):
        self.iterations += 1
        return self.iterations >= self.maxIterations or np.abs(error) <= self.precision

    def predict(self,entry):
        return sum(self.W * entry)

