# 18 - Numpy Arrays
## Numpy Arrays and Matrices
Standard lists can be turned into NumPy arrays as shown below

```py
my_list = [1,2,3]
arr = np.array(my_list)


my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)
```

NumPy also has a built in Range Function:

```py
np.arange(start_int,end_int,step_size)
np_range = np.arange(0,10,1)
```

NumPy is also capable of building arrays of ones and zeros in 1D and 2D matrices

```py
ones_list = np.ones(4)
ones_mat = np.ones((3,4))
zeros_list = np.zeros(3)
```

Identity Matrices can also be created

```py
identity_mat = np.eye(4)
```

Arrays with equally split distances in between can also be created

```py
np.linspace(start_int,end_int,number_of_spaced_points)
linear_space = np.linspace(0,5,10)
```

## Random Arrays and Matrices

Random arrays can be generated from 0 to 1, around a Normal Distribution (With 0 as the centre) and between a range of integers.

*NOTE:* Unlike the previous section, no tuples are required to create a 2D matrix using these methods. All end integers are exclusive

Random between 0 and 1

```py
random_arr = np.random.rand(4)
random_mat = np.random.rand(4,5)
```

Random around Normal Distribution (0 as Center)

```py
random_arr_norm = np.random.randn(4)
random_mat_norm = np.random.randn(4,5)
```

Random between set integers

```py
np.random.randint(start_int,end_int,array_size)
random_arr_int = np.random.randint(0,100,10)
```

## Reshaping Arrays

1D Arrays can be reshaped into 2D Arrays provided there are enough indices to fill the matrix
(i.e. a 4x1 matrix can be reshaped into a 2x2 matrix)

```py
init_arr = np.arange(25)
mod_arr = init_arr.reshape(5,5)
```

## Minimum and Maximum Values and Positions

The minimum and maximum values in an array can be determined as well as their respective locations.

```py
arr = np.random.randint(0,100,10)

max_int = arr.max()
min_int = arr.min()

max_int_loc = arr.argmax()
min_int_loc = arr.argmin()
```

## Shape and DType

Shape: The shape of the matrix/array (1x4, 2x2, 3x5)
DType: Short for Data Type, it returns the data type of the elements inside the array

*NOTE:* These are properties and do not need a set of parenthesis at the back

```py
arr_shape = arr.shape
arr_dtype = arr.dtype
```


