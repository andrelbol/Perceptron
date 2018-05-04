import numpy as np

import utils

class Perceptron:

    def __init__(self, csv_file, max_iterations, alpha):
        self.input_train, \
            self.input_test, \
            self.desired_response_train, \
            self.desired_response_test = utils.get_values_from_csv(csv_file)
        self.max_iterations = max_iterations
        self.alpha = alpha


    def train(self):
        t = 1
        all_errors = []
        max_error = 1
        input_row_quantity = self.input_train.shape[0]
        input_column_quantity = self.input_train.shape[1]
        response_column_quantity = self.desired_response_train.shape[1]
        weight_matrix = np.random.rand(response_column_quantity, input_column_quantity)
        bias = np.random.rand(response_column_quantity)
        while( t < self.max_iterations and max_error > 0):
            max_error = 0
            for index in range(0, input_row_quantity):
                step_input = np.matmul(weight_matrix, self.input_train[index].transpose()) + bias
                response_array = utils.apply_step(step_input)
                error_array = self.desired_response_train[index] - response_array
                weight_matrix += self.alpha*np.matmul(error_array.transpose().reshape(3, 1), self.input_train[index].reshape(1, 13))
                bias += self.alpha*error_array
                max_error += np.sum([value*value for value in error_array])

            all_errors.append(max_error)
            t += 1
        return weight_matrix, bias, max_error, all_errors

    def test(self, weight, bias):
        input_row_quantity = self.input_test.shape[0]
        right_answers = 0
        for index in range(0, input_row_quantity):
            predicted_response = utils.apply_step(np.matmul(weight, self.input_test[index].reshape(13, 1).flatten()) + bias)
            predicted_response = predicted_response.flatten()
            if(utils.matrix_equals(predicted_response, self.desired_response_train[index])):
                print("YES")
                right_answers += 1
        return right_answers/input_row_quantity

    def __str__(self):
        return 'Perceptron: Max Iterations: ' + str(self.max_iterations) + ', Alpha: ' + str(self.alpha)
