import pandas
import numpy

def convertToArray(number):
    return {
        '1': [1, 0, 0],
        '2': [0, 1, 0],
        '3': [0, 0, 1]
    }.get(str(number))

def getValues():
    data_frame = pandas.read_csv('data.csv')
    return data_frame.iloc[:, 1:], data_frame.iloc[:, 0]

def calculateOutput():


def perceptron():
    t = 1
    E = 1
    N = w.shape[1]
    print(N)
    while(t<max_iterations and E > 0):
        E = 0
        for i in range(1, N):

X, d = getValues()
perceptron(X, d)
