# 61 - Plotly and Cufflinks

**NOTE:** As of the time of writing, `plotly` and `cufflinks` can only be used with Jupyter Notebook.

**Installing Plotly and Cufflinks using pip**
```
pip install plotly
pip install cufflinks
pip install chart-studio
```

**Imports and Setup**
```py
import pandas as pd
import numpy as np
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

%matplotlib inline

# Checking plotly version (> 1,9)
print(__version__)

init_notebook_mode(connected=True)
cf.go_offline()
```

## Plotting

Creating the data:

```py
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
```

Plotting:

```py
df.plot()   # Default plot using matplotlib

df.iplot()  # Interactive plot using plotly and cufflinks
```

With the interactive plot, you can click on data categories to turn them on and off.

## Using `.iplot()`

The type of plot can be changed by specifying `kind` inside `df.iplot(kind=)`. Options are:

* `df.iplot(kind='scatter',x=categorical_col ,y=value_column ,mode='markers')` - Scatter Plot
* `df2.iplot(kind='bar', x=categorical_col, y=value_column)` - Bar Plot
    * `df.sum().iplot(kind='bar')` Bar plot called together with an aggregate function in front. *(`.groupby()`,`.sum()`)*
* `df.iplot(kind='box)` - Box Plot
* `df3.iplot(kind='surface',colorscale='rdylbu')` - Surface Plot
* `df.iplot(kind='hist',bins=50)` - Histogram Plot *(Can be used for one column or whole DataFrame)*
* `df[['A','B']].iplot(kind='spread')` - Spread Plot
* `df.iplot(kind='bubble',x='A',y='B',size='C')` - Bubble Plot
* `df.scatter_matrix()` - Scatter Matrix Plot *(Similar to Seaborn's Pair Plot)*