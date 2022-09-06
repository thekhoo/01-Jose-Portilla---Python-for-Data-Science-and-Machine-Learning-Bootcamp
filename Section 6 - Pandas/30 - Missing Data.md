# 30 - Missing Data

Methods to deal with missing data in Pandas. Missing points are normally automatically filled with NULL or NaN values by Pandas.

## Creating DataFrame from a Dictionary

Similar to how series can be created from dictionaries, DataFrames can also be created from dictionaries.

```py
import numpy as np
import pandas as pd

# Columns are A, B and C
d = {
    'A': [1, 2, np.nan],
    'B': [5, np.nan, np.nan],
    'C': [1,2,3]
}

df = pd.DataFrame(d)
```

## DropNA Method

The `.dropna()` method will drop all rows that have one or more null/missing values. This can also be done along rows or columns.

* (Rows) axis=0
* (Columns) axis=1

A threshold value can also be set to determine the minimum number of null values for the row to be dropped.
*(i.e. If `thresh=2`, a minimum of 2 values must be null before the row is dropped)

```py
df = df.dropna()

# Drop null columns
df = df.dropna(axis=1)

# Drop null rows with a threshold of 2
df = df.dropna(axis=0, thresh=2)
```

# FillNA Method

Works to fill in missing values using `.fillna()`. It takes in one parameter `value` which is the value that will replace the null values.

```py
# Filling all missing values with "FILL VALUE"
df = df.fillna(value='FILL VALUE')
```

Common practice is to fill missing values with mean values as such.

```py
df = df['A'].fillna(value=df['A'].mean())
```