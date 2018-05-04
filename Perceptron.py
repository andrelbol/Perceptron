import numpy as np

import utils

class Perceptron:

    def __init__(self, csv_file, max_iterations, alpha):
        self.input_train, \
            self.input_test, \
            self.desired_response_train, \
            self.desired_response_test = utils.get_values_from_csv(csv_file)
        self.max_iterations = 4
        self.alpha = 0.1


    def train():
        input_column_quantity = self.input_train.shape[1]
        response_column_quantity = self.desired_response_train.shape[1]
        weight_matrix = np.random.rand(response_column_quantity, input_column_quantity)
        bias = np.random.rand(response_column_quantity)
        for index in range(0, self.max_iterations-1):
            step_input = np.matmul(weight_matrix, self.input_train[index].T)
            response_array = apply_step(step_input)
            error_array = desired_response[index] - response_array

    def __str__(self):
        return 'Perceptron: Max Iterations: ' + str(self.max_iterations) + ', Alpha: ' + str(self.alpha)
