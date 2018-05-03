import pandas
import numpy as np

def convert_to_array(number):
    return {
        '1': [1, 0, 0],
        '2': [0, 1, 0],
        '3': [0, 0, 1]
    }.get(str(number))

def get_values_from_csv():
    data_frame = pandas.read_csv('data.csv')
    return data_frame.iloc[:, 0].values, data_frame.iloc[:, 1:].values

def perceptron(max_iterations, alpha, X, D):
    t = 1
    E = 1
    N = X.shape[1]
    W = np.random.rand(N)
    b = np.random.rand(N)
    y = np.zeros(N)
    e = np.zeros(N)
    print(N)
    while(t < max_iterations and E > 0):
        E = 0
        for i in range(0, N-1):
            y[i] = W*X[i]+b[i]
            e[i] = D[i] - y[i]
            W = W+alpha*e[i]*x[i].T
            b = b + alpha*e[i]
            E = E + np.sum(e)
        t += 1
    return W



D, X = get_values_from_csv()
max_iterations = 100
alpha = 0.5
result = perceptron(max_iterations, alpha, X, D)
print(result)
