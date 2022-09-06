# 32 - Merging, Joining and Concatenating

## Concatenation

```py
import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
```

Basically glues DataFrames together. Dimensions of the DataFrames being joined should match along the axis of concatenation. `pd.concat` can be used to concatenate DataFrames together.

```py
# Concat along rows (Default axis=0 if not specified)
df = pd.concat([df1,df2,df3])

# Concat along columns
df_col = pd.concat([df1,df2,df3],axis=1)
```

Nulls will be shown when axis don't match or when information doesn't line up correctly when concatenating. In the case of concatenating across columns for the previous example, this will result in NaN values throughout the concatenated DataFrame.

## Merging

Pandas is capable of merging DataFrames similar to merging SQL tables. Merging is done on a `key` column which is the column that will be used to identify how the data should be merged.

```py
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

df = pd.merge(left,right,how='inner',on='key')    
```

In the case of different column names but the same values that will be merged upon, a list can be used in the `on` parameter to specify the columns to merge.

**NOTE:** By default, pandas will do an inner join. Other options include *(outer,right)*

```py
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

df = pd.merge(left,right,on=['key1','key2'])
```

## SQL Joins (Inner, Left, Right, Outer, Cross)

### Inner Join 

An inner join **returns records that have matching values in both DataFrames**.

```py
df = pd.merge(left,right,how='inner',on=['key1','key2'])
```

### Left Outer Join

A left outer join **returns all the records on the left DataFrame and the matching records on the right DataFrame**.

```py
df = pd.merge(left,right,how='left',on=['key1','key2'])
```

### Right Outer Join

A right outer join **returns all the records on the right DataFrame and the matching records on the left DataFrame**.

```py
df = pd.merge(left,right,how='right',on=['key1','key2'])
```

### Full Outer Join

A full outer join **returns all the records where there is a match on either the left or right DataFrames**. Basically unions both DataFrames.

```py
df = pd.merge(left,right,how='outer',on=['key1','key2'])
```

### Right Outer Join

A right outer join **returns all the records on the right DataFrame and the matching records on the left DataFrame**.

```py
df = pd.merge(left,right,how='right',on=['key1','key2'])
```

### Cross Join

A cross join **creates the cartesian product from both frames, preserves the order of the left keys**.

```py
df = pd.merge(left,right,how='cross',on=['key1','key2'])
```

## Joining

Similar to merging, except **keys to join on are in the index and not a column**.

```py
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

df = left.join(right)   # Default to inner

# Joining can be specified
df = left.join(right,how='outer')
```
