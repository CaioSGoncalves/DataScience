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
                sigmoid_output = self.sigmoid(sum(self.W * entries[i]))
                Error = self.cost(sigmoid_output, label[i])
                ErrorTotal += Error
                Gradient += (sigmoid_output - label[i]) * entries[i]
            self.W = self.W - (self.alpha * Gradient) / len(entries)
            ErrorTotal = ErrorTotal
            self.ErrorPlot.append(ErrorTotal)
            if self.stopConditions(ErrorTotal): 
                break

    def sigmoid(self, sum):
        return 1/(1 + np.exp(-sum))

    def decision_boundary(self, prob):
        if prob >= 0.5:
            return 1
        else:
            return 0  

    def cost(self, hypothesis, label):
       return -label * np.log(hypothesis) - (1-label) * np.log(1-hypothesis)    

    def stopConditions(self, error):
        self.iterations += 1
        return self.iterations >= self.maxIterations or np.abs(error) <= self.precision

    def predict(self,entry):
        sigmoid_output = self.sigmoid(sum(self.W * entry))
        return self.decision_boundary(sigmoid_output)

