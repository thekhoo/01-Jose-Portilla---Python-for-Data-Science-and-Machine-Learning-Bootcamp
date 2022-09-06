# 33 - Operations

```py
import pandas as pd

df = pd.DataFrame({
    'col1':[1,2,3,4],
    'col2':[444,555,666,444],
    'col3':['abc','def','ghi','xyz']
    })
```

## Unique Values

3 main methods to find unique values in a DataFrame.

* `.unique()` for array
* `.nunique()` for number of unique values
* `.value_counts()` how many times each unique value occurs in a column

## Apply Method

This is a powerful method that allows custom functions to be applied on columns within the DataFrame.

Imaging having a function `times2(x)`that returns a number multiplied by 2.

```py
def times2(x):
    return x*2

df = df['col1'].apply(times2)

# A similar thing can be done using lambda
df = df['col1'].apply(lambda x: x*2)
```

## Removing Columns

Columns can be dropped using the method `.drop()`. The axis must be specified whereby:

* (axis=0) Horizontal
* (axis=1) Vertical

**NOTE:** The `inplace` method must be set to True if not assigned to a variable.

```py
# inplace True
df.drop('col1',axis=1,inplace=True)

# inplace False
df = df.drop('col1',axis=1)
```

## Getting Column and Index Names of a DataFrame

These are attributes of the DataFrame and can be called using `df.index` or `df.columns` to get information regarding the index and columns respectively.

## Sorting and Ordering a DataFrame

The function `.sort_values()` can be used to sort a DataFrame. The parameter `by` is used to specify which column to sort on. The `axis` parameter can be used to specify to sort by row or column.

```py
df.sort_values(by='col2',axis=0)
```

## Checking for Null Values

The method `.isnull()` can be used to return a boolean DataFrame with `True` for null values and `False` for non-null values.

## Pivot Tables

Similar to pivot tables in Excel. The function takes in 3 parameters.

* `values` for the values that are to be displayed within the pivot table.
* `index` for the column(s) that will be used as the index.
* `columns` for the actual columns that will be displayed.

```py
data = {
    'A':['foo','foo','foo','bar','bar','bar'],
    'B':['one','one','two','two','one','one'],
    'C':['x','y','x','y','x','y'],
    'D':[1,3,2,5,4,1] 
    }

df = pd.DataFrame(data)

# Values form the D Column
# Multi-Level Index equal to the A and B Column (Passed as a list)
# Actual columns defined by the C Column
pivot_tbl = df.pivot_table(values='D',index=['A','B'],columns='C')
```

