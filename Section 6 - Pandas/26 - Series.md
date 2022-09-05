# 26 - Series

## Creating a Pandas Series

Pandas Series are built on top of NumPy arrays. Lists, arrays and dictionaries can be converted into series objects. Dictionaries will return a series with both data and indices.

The function `pd.Series()` takes multiple inputs but we'll focus on two:

* data - The data that will be entered into the series
* index - The data that will be the index for the series

```py
labels = [a,b,c]
my_data = [10,20,30]
arr = np.array(my_data)
d = {a: 10, b: 20, c: 30}

# Creating a Series
data_series = pd.Series(data=my_data)

# Creating a Series with Indeces
data_series_idx = pd.Series(data=my_data,index=labels)

# Creating a Series from NumPy Arrays
data_series_numpy = pd.Series(data=arr,index=labels)

# Creating a Series from a Dictionary
data_series_dict = pd.Series(d)
```

## How Pandas Series is Different from NumPy Arrays

Unlike NumPy Arrays, Pandas Series can store more than just numbers. Pandas Series can also be used to store strings and built-in functions.

```py
# Strings
labels = [a,b,c]
series = pd.Series(data=labels)

# Built in Functions
series = pd.Series(data=[sum,print,len])
```

## Getting Information from a Series

Here, two series are created with the countries as the index and integers as the data point. To select a data point, it works similar to a NumPy array where you pass in the index label `arr[idx]` and get the data. In this case, the index will be a string.

```py
ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
ser3 = pd.Series(data=labels)

# Getting value for index USA
usa = ser1['USA']

# Getting value using an integer index (Getting from Index 1)
result = ser3[1]    
```

## Adding Series

When doing addition or subtraction in NumPy or Pandas, the integers are automatically converted into floats. This is to avoid data loss from divisions etc.

Series can be added together directly. Pandas will match the index of the series being added together. For the indices where it cannot find a match between all the Series, it will return Not a Number (NaN)

```py
# Adding two series together
ser_result = ser1 + ser2
```