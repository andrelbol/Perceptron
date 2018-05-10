from Perceptron import Perceptron

# Primeiro teste
# perceptron = Perceptron('data.csv', 10000, 0.01)
# weigth, bias, error, all_errors = perceptron.train()
# accurracy = perceptron.test(weigth, bias)
# print(accurracy)

# Segundo teste
perceptron = Perceptron('breast-cancer-data.csv', 100, 0.1)
weigth, bias, error, all_errors = perceptron.train()
print(all_errors)
accurracy = perceptron.test(weigth, bias)
print(accurracy)
