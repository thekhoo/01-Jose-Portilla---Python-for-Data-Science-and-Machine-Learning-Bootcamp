"""
18 - Numpy Arrays
"""

import numpy as np

# NumPy Arrays
my_list = [1,2,3]
arr = np.array(my_list)
print('Numpy Array')
print(arr)

# Matrices
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)
print('\nNumpy Matrix')
print(mat)

# Starting Integer, End Integer, Step Size
np_range = np.arange(0,10,1)
print('\nNumpy Number Range')
print(np_range)

# Ones and Zeros
ones_list = np.ones(4)
ones_mat = np.ones((3,4))
zeros_list = np.zeros(5)

print('\nNumpy Ones and Zeros Matrices')
print(ones_list)
print(ones_mat)
print(zeros_list)

# Identity Matrix
iden_mat = np.eye(4)
print('\nNumpy Identity Matrix')
print(iden_mat)

# Linear Space
# Staring Integer, Ending Integer, Number of Evenly Spaced Points
linear_space = np.linspace(0,5,10)
print('\nNumpy Linear Space')
print(linear_space)

# Random Matrix (0 to 1)
random_arr = np.random.rand(5)
random_mat = np.random.rand(3,4)
print('\nNumpy Random Matrix')
print(random_arr)
print(random_mat)

# Random Normal Distribution
# Creates a random set of numbers from a normal distribution (Around 0)
normal_random_arr = np.random.randn(4)
normal_random_mat = np.random.randn(4,3)
print('\nNumpy Random Matrix (Normal Distribution)')
print(normal_random_arr)
print(normal_random_mat)

# Random Number Generation Matrix
# Starting Integer, Ending Integer, Number of Integers
random_int_arr = np.random.randint(0,100,10)
print('\nNumpy Random Integer Arrays')
print(random_int_arr)

# Reshaping Arrays
init_arr = np.arange(25)
print('\nReshaping Arrays')
print('-- Before --')
print(init_arr)

mod_arr = init_arr.reshape(5,5)
print('-- After --')
print(mod_arr)

# Max and Min Values with locations
init_arr_max = init_arr.max()
init_arr_min = init_arr.min()
max_loc = init_arr.argmax()
min_loc = init_arr.argmin()

print('\nNumpy Maximum and Minimum Values')
print(f'Maximum Value: {init_arr_max} at index {max_loc}')
print(f"Minimum Value: {init_arr_min} at index {min_loc}")

# Shape and DType (Data Type inside the Array)
arr_shape = mod_arr.shape
arr_dtype = mod_arr.dtype

print('\nShape and Data Type')
print(f'Shape: {arr_shape}')
print(f'Data Type: {arr_dtype}')