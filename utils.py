import pandas as pd
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

def convert_array_to_multi_array(array):
    new_array = []
    for number in array:
        new_array.append(convert_number_to_array(number))
    return np.array(new_array)

def normalize_dataframe(dataframe):
    return (dataframe-dataframe.min())/(dataframe.max() - dataframe.min())

def apply_step(array):
    for index in range(0, len(array)):
        array[index] = 1 if (array[index] > 0) else 0
    return array

def get_values_from_csv(csv_file):
    # Read from file
    data_frame = pd.read_csv(csv_file)
    data_frame = shuffle(data_frame)

    # Separate data
    desired_response = data_frame.iloc[:, 10]
    input_data = data_frame.iloc[:, :9]

    # Normalizing input
    input_data = normalize_dataframe(input_data)

    # Sampling for train/test
    input_train, input_test, desired_response_train, desired_response_test = train_test_split(input_data, desired_response, test_size=0.33)
    input_train = np.array(input_train)
    input_test = np.array(input_test)

    desired_response_train = np.array([convert_two_and_four_to_zero_and_one(value) for value in desired_response_train])
    desired_response_test = np.array([convert_two_and_four_to_zero_and_one(value) for value in desired_response_test])
    return input_train, input_test, desired_response_train, desired_response_test

def convert_number_to_array(number):
    return {
        '1': [1, 0, 0],
        '2': [0, 1, 0],
        '3': [0, 0, 1]
    }.get(str(number))

def convert_two_and_four_to_zero_and_one(number):
    return {
        '2': 0,
        '4': 1
    }.get(str(number))



def matrix_equals(matrix_1, matrix_2):
    for index in range(0, matrix_1.shape[0]):
        if(matrix_1[index] != matrix_2[index]):
            return False
    return True