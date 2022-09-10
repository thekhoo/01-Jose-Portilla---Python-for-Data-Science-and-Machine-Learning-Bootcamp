# 56 - Pandas Built-in Data Visualisation

```py
import pandas as pd
import numpy as np
import seaborn as sns   # Seaborn can be imported to make the graphs look nicer

df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')
df3 = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
```

## Histogram

The histogram is built on top of matplotlib/seaborn so matplotlib and seaborn parameters can be called within `hist()`.

```py
df1['A'].hist(bins=30)

# OR

df1['A'].plot(kind='hist',bins=30)

# OR

df1['A'].plot.hist()
```

## Different Plot Types

There are many plot types built into pandas:
* `df2.plot.area(alpha=0.4)` Area Plot. Line plot filled in with colour *(Alpha adjusts the transparency)*
* `df2.plot.bar(stacked=True)` Bar Plot. Index should be categorical for this. *(Stacked set to True or False to create a stacked column)*
* `df1['A'].plot.hist()` Histogram Plot. *(bins set to the number of bars in the histogram)*
* `df1.plot.line(x=df1.index.y='B',figsize=(12,3),lw=1)` Line Plot. *(Built on top of matplotlib - similar parameteres can be used)*
* `df1.plot.scatter(x='A',y='B',c='C')` Scatter Plot. *(Different colours can be added based on column categorical values by specifying the column name in the parameter `c`)*
* `df1.plot.scatter(x='A',y='B',s=df1['C'] * 100)` Scatter Plot. *(Varying size of markers based on column values. Insert column name in parameter `s`)*
* `df2.plot.box()` Box Plot.
* `df3.plot.hexbin(x='a',y='b',gridsize=25)` Hex Plot. Similar to the scatter plot.
* `df2['a'].plot.kde()` / `df2['a'].plot.density()` Kernal Density Estimation Plot. *(Can be done on the entire DataFrame too)*

