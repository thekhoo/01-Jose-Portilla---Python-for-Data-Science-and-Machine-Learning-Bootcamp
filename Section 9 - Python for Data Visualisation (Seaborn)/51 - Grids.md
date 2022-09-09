# 51 - Grids

```py
import seaborn as sns
iris = sns.load_dataset('iris')     # Measurement of different flowers/irises
iris.head()
```

## Pair Grid

Gives us an empty grid of plots (Empty `.pairplot()`). Gives more customisability over `.pairplot()`.

```py
g = sns.PairGrid(iris)

# Mapping plots to the PairGrid
g.map(plt.scatter)

# Mapping plots separately
g.map_diag(sns.distplot)    # Diagonal
g.map_upper(plt.scatter)    # Upper
g.map_lower(sns.kdeplot)    # Lower
```

## Facet Grid

* `data` DataFrame data passed in.
* `col` Name of the parameter within the DataFrame that you want to compare in the column of the subplot
* `row` Name of the parameter within the DataFrame that you want to compare in the row of the subplot

```py
tips = sns.load_dataset('tips')

g = sns.FacetGrid(data=tips,col=,row=)

# Dist Plot (1 Variable)
g.map(sns.distplot,'total_bill')

# Scatter Plot (2 Variables)
g.map(sns.scatter,'total_bill','tip')
```

