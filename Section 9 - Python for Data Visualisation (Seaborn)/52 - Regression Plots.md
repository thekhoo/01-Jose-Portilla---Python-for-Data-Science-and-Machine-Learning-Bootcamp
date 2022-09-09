# 52 - Regression Plots

 ```py
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
```

# Linear Model (LM) Plot

Creates a scatter plot with a linear plot on top of it.

* `x` Name of the column whos data is to be plotted with respect to the x axis
* `y` Name of the column whos data is to be plotted with respect to the y axis
* `data` The DataFrame where the data comes from
* `hue` Name of the column to form an additional category split
    * `col` can be called to separate by columns instead of by colour
    * `row` can be called to separate by rows instead of by colour
* `markers` Markers to be used for each category in `hue`
* `scatter_kws` Dictionary with matplotlib arguments to adjust the scatter plot
* `aspect` Aspect ratio between height and width of the separate grids
* `size` Size of the figure

```py
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={},aspect=0.6,size=8)
```

