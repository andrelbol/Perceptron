from Perceptron import Perceptron

perceptron = Perceptron('data.csv', 10000, 0.01)
weigth, bias, error, all_errors = perceptron.train()
# print(error)
# print("weigth: " + str(weigth))
accurracy = perceptron.test(weigth, bias)
print(accurracy)
