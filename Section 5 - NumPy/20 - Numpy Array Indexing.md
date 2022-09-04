# 20 - Numpy Array Indexing

## Indexing from an Array (1D)

Works similar to a normal python array. Using square brackets `my_list[idx]` the item at the index specified will be returned.

```py
arr = np.arange(0,11,1)

arr[8]      # Grab at Index 8
arr[2:5]    # Grab from Index 2 to 4
arr[1:]     # Grab everything after Index 1 (Starts at Index 2)
arr[:6]     # Grab everything up to Index 5
```

Values can also be broadcasted into an array.

```py
arr[0:5] = 100  # Everything from Index 0 to Index 4 will be replaced with 100
```

## Slicing an Array (1D)

In NumPy, to avoid memory issues with large arrays, a slice is a different view of the array but *is not* copied into the new variable. Any changes made to a slice will be made on the array that it was sliced from.

```py
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99    # This will affect the original array 'arr'
```

## Copying an Array (1D)

This specifically indicates that a copy of the array is to be made. Changes made to this will not be done to the array from which it is copied from.

```py
arr_copy = arr.copy()   # This copies the array into a new variable
```

## Indexing from an Array (2D)

There are two formats to grab data from a 2D Array. Double bracket format and single bracket format.

#### Double Bracket Format

This uses two sets of square brackets, the first one indicating the row and the second indicating the column.

```py
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

# Grabbing the item 40
item = arr_2d[2][1]
```

#### Single Bracket Format

**RECOMMENDED METHOD**

Similar to the Double Bracket Method, instead of having two square brackets, commas can be used to separate rows and columns.

```py
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

# Grabbing the item 40
item = arr_2d[2,1]
```

## Slicing an Array (2D)

Similar to how a 1D Array is sliced. 

*The following example grabs the first and second rows (Index 0 and 1)*

```py
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

sliced_arr = arr_2d[:2]
```

*The following example grabs the first and second rows (Index 0 and 1), and in both these rows, columns 1 to end*

```py
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])

sliced_arr = arr_2d[:2,1:]
```

## Comparing Arrays

Different arrays can be compared to get boolean arrays.

*The following example returns a boolean array where elements less than or equal to 5 will be False while the rest will be True*

```py
 arr = np.arange(1,11)

 # Boolean Comparison
 bool_arr = arr > 5
```

## Conditional Selection

The boolean array can be passed into square brackets to get results where the boolean array is True.
```py
 arr = np.arange(1,11)

 # Boolean Comparison
 bool_arr = arr > 5

 # Conditional Selection
 result_arr = arr[bool_arr]
```



