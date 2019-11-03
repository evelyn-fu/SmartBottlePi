import numpy as np

# X = np.array([[1], [2], [3], [4], [5]])
# ones = np.ones([X.shape[0], 1])
# X = np.concatenate([ones, X], 1)
# y = np.array([[2], [4], [6], [8], [10]])

# Initialize hyper parameters alpha, number of iterations, and theta
# y = theta[0][0] + theta[0][1]x

class LinearRegression:

    def __init__(self):
        self.theta = [1.0, 1.0, 1.0]
        self.alpha = 0.0001
        self.iters = 1000

    # Cost function is 1/2M([h(theta)(x1)-y1]^2) where M is length of dataset --> formula from Andrew Ng's class
    def computeCost(self, X, y, theta):
        return np.sum(np.power(((X @ self.theta.T) - y), 2) / (2 * len(X)))

    # Requires X and y, as well as all hyperparameters
    # Gradient descent function is theta - a(1/M)([h(theta)(x1)-y)*x1])
    def fit(self, X, y, epoch=1):
        for _ in range(epoch):
            for i in range(self.iters):
                self.theta = self.theta - (self.alpha/len(X)) * np.sum((X @ self.theta.T - y) * X, axis=0)
                cost = self.computeCost(X, y, self.theta)

    def predict(self, X):
        return X @ self.theta.T

# theta, cost = gradientDescent(X, y, theta, alpha, iterations)