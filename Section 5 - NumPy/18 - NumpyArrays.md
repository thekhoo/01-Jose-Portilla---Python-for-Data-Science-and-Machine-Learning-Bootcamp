# 18 - Numpy Arrays
## Numpy Arrays and Matrices
Standard lists can be turned into NumPy arrays as shown below

`my_list = [1,2,3]`

`arr = np.array(my_list)`


`my_mat = [[1,2,3],[4,5,6],[7,8,9]]`

`mat = np.array(my_mat)`


NumPy also has a built in Range Function:

`np.arange(start_int,end_int,step_size)`

`np_range = np.arange(0,10,1)`


NumPy is also capable of building arrays of ones and zeros in 1D and 2D matrices

`ones_list = np.ones(4)`

`ones_mat = np.ones((3,4))`

`zeros_list = np.zeros(3)`


Identity Matrices can also be created

`identity_mat = np.eye(4)`


Arrays with equally split distances in between can also be created

`np.linspace(start_int,end_int,number_of_spaced_points)`

`linear_space = np.linspace(0,5,10)`



