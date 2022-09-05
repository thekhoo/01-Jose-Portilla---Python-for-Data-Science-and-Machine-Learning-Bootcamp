# 27 - DataFrames Part 1

## Creating a DataFrame

The code below creates a table with random numbers that follow a normal distribution in a **5x4 matrix** in a table with **Rows: A, B, C, D, E** and **Columns: W, X, Y, Z**

```py
import numpy as np
import pandas as pd

from numpy.random import randn

# Setting a Fixed Seed
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
```

## Returning Column(s) from a DataFrame

The recommended way to grab a column from a DataFrame is using the square bracket notation and pass in the column name like `df['W']`. 

The SQL method can also be used - `df.W`, but this is not recommended. May get confusing with the other methods available with DataFrames and Pandas.

Multiple columns can be grabbed by using the following method.

```py
# Use a List to get mulitple columns
new_df = df[['W','Z']]
```

## Creating New Columns through Arithmetic

New columns due to the addition of different columns can be created as such.

```py
df['new'] = df['X'] + df['Y']
```

## Removing Rows and Columns - df.drop()

Rows and columns can be removed (dropped) by specifying the axis along which the data is dropped.

* axis=0    Horizontal (x)
* axis=1    Vertical (y)

0 is row and 1 is column because when `df.shape` is called, it returns a tuple `(rows x columns)` thus row being 0 and column being 1.

Dropping the new column created in the previous section can be done as such.

```py
# Using inplace. This does not require you to reassign the DataFrame
df.drop('new',axis=1,inplace=True)

# Not using inplace. This requires you to reassign the DataFrame
new_df = df.drop('new',axis=1)
```

## Returning Rows and Columns (Subsets) from a DataFrame

There are two ways to select rows from a DataFrame. This will return a Series with the index being the column names and the respective data.

* .loc[]    (Labelled based index locatiom) Pass in the row you want in brackets.
* .iloc[]   (Integer based index location) Index based location. Uses a numerical index to return rows.

*Row comma Column notation for .loc[]*
```py
value_of_B = df.loc['B','Y']    # Gets the data point in Row B, Column Y
```

*Getting rows and columns*

```py
subset = df.loc[['A','B'],['X','Y']] # Gets the data points in Rows A and B and Columns X and Y
```


