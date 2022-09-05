# 28 - DataFrames Part 2

## Conditional Selection for DataFrames

Works similar to NumPy. A boolean DataFrame can be generated.

```py
import numpy as np
import pandas as pd

from numpy.random import randn

# Setting a Fixed Seed
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

# Returns a DataFrame of booleans with True for data more than 0 and False for data less than 0.
bool_df = df > 0

# Returns values within the original DataFrame that are True and NaN for values that are false.
result_df = df[bool_df]

# Normally done as follows
result_df = df[df > 0]
```

The following can be done for individual columns within the DataFrame which is returned as a series.

```py
# Filtering a column's value
bool_col = df['W'] > 0

# Returns all the rows that are true based on the previous condition
result_df = df[bool_col]

# Return the series for a column of the resulting DataFrame
result_series = result_df['X']
```

The important thing to note is that the boolean opeartor - `df[df[bool_col]]` is still a DataFrame and thus, DataFrame functions can be used on it. The previous process can also be simplified into a one-liner.

```py
# df[df['W'] > 0] is getting the boolean DataFrame where Column 'W' is more than 0
# ['Y', 'X'] is the selection of columns 'Y' and 'X' from the resulting DataFrame
result_df = df[df['W'] > 0]['Y','X']
```

## Multiple Conditions

What if we wanna implement multiple conditions?

* W > 0 and,
* Y > 1

**NOTE:** Python's normal `and` operator cannot be used here like the following case `df[(df['W']) and (df['Y'] > 1))]`. The right way is to use an ampersand `&`.

```py
# The correct way to write it using an ampersand (&) is:
result_df = df[(df['W'] > 0) & (df['Y'] > 1)]

# To implement an "OR" condition, use a pipe (|)
result_df = df[(df['W'] > 0) | (df['Y'] > 1)]
```

## Resetting index back to default

Call the method `.reset_index()` this will create a new column called 'index' and the current index will become an integer index starting from 0. Similar to `.drop()`, the setting `inplace` has to be set to `True`.

```py
# Using inplace
df.reset_index(inplace=True)

# Not using inplace
df = df.reset_index()
```

## Changing the Index

This can be done by inserting a new column into the DataFrame and using the method `.set_index()`. Similarly, `inplace` needs to be set to `True`.

**NOTE:** This will overwrite the existing index without creating a new column. If the previous index should be a column, call the method `.reset_index()` first.

```py
new_idx = 'CA NY WY OR CO'.split()  # This creates a list really quickly as .split() will split by empty space

# Set the index
df.set_index(new_idx,inplace=True)
```