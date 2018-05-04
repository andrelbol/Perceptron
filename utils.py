import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def convert_array_to_multi_array(array):
    new_array = []
    for number in array:
        new_array.append(convert_number_to_array(number))
    return np.array(new_array)


def normalize_matrix(np_matrix):
    return (np_matrix-np_matrix.mean())/np_matrix.std()

def apply_step(array):
    for index in range(0, len(array)):
        array[index] = 1 if (array[index] > 0) else 0
    return array

def get_values_from_csv(csv_file):
    data_frame = pd.read_csv(csv_file)
    data_frame = shuffle(data_frame)
    input_data = normalize_matrix(data_frame.iloc[:, 1:].values)
    desired_response = convert_array_to_multi_array(data_frame.iloc[:, 0].values)
    input_train, input_test, desired_response_train, desired_response_test = train_test_split(input_data, desired_response, test_size=0.33)
    return input_train, input_test, desired_response_train, desired_response_test

def convert_number_to_array(number):
    return {
        '1': [1, 0, 0],
        '2': [0, 1, 0],
        '3': [0, 0, 1]
    }.get(str(number))

def matrix_equals(matrix_1, matrix_2):
    for index in range(0, matrix_1.shape[0]):
        if(matrix_1[index] != matrix_2[index]):
            return False
    return True
