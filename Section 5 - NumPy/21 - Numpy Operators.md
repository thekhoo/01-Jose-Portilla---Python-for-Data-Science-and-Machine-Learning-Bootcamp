# 21 - Numpy Operators

## Array with Array

Array and array operations can be done with simple arithmetic signs.

*Adding arrays together (Basic Arithmetic Operations)*

```py
arr_1 = np.arange(1,11)
arr_2 = np.arange(11,21)

arr_3 = arr_1 + arr_2
arr_4 = arr_1 - arr_2
```

## Array with Scalars

Simple arithmetic operations can also be undertaken with scalar values. The scalar value along with the arithmetic operator will be applied to each element in the array.

```py
arr = np.arange(1,11)

arr_2 = arr + 100   # All elements added by 100
arr_3 = arr - 50    # All elements subtracted by 100
arr_4 = arr ** 2    # All elements squared
```

## Universal Array Functions

Different functions that can be used on the array.

*Trigonometric functions*

```py
arr = np.arange(1,11)

sin_arr = np.sin(arr)   # Sine the entire array
exp_arr = np.exp(arr)   # Apply exponential to all elements in the array
```