import numpy as np

# Parameters
N = 10
M = 100

success_rate = 0.95

# this will create an array with N length containing the value [0..1]
def generate_single_data(_n):
    temp_list = []
    if (_n < 1):
        raise TypeError("Array can not be created with length less than 1")
    for counter in range (0, _n + 1):
        print(counter)

generate_single_data(2)