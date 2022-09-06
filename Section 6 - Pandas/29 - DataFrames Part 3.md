# 29 - DataFrames Part 3

## Multi-Level Index

This section showcases the ability to create multi-level indexes or index hierachy. Similar to the "Rows" feature in Excel Pivot Tables, this allows data to be broken down into different levels of indexes.

```py
# Code given in Jupyter Notebook
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside)) # Makes this into a tuple pair
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Multi-Index Level DataFrame
df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
```

Subsets can easily be retrieved by calling outside indexes as such.

```py
# Getting index G1
g1_df = df.loc['G1']

# Return row with index 1 within the G1 Subset
g1_df_sub = df.loc['G1'].iloc[1]

# Returning specific data within the subset and row (Col B)
g1_df_b = df.loc['G1'].iloc[1]['B']
```

## Renaming the Index

The index can be renamed using `df.index.names`.

```py
# Outer Index - Groups
# Inner Index - Num
df.index.names = ['Groups','Num']
```

## DataFrame Cross Section

Can be used to slice a DataFrame to get data for one outer index or one row from each index depending on the data entered.

```py
# Grabbing all rows with index value G1 in the "Groups" column (Outer Index)
g1_df = df.xs('G1')

# Grabbing all rows with index value of 1 in the 'Num' column (Inner Index)
one_df = df.xs(1,level='Num')
```
