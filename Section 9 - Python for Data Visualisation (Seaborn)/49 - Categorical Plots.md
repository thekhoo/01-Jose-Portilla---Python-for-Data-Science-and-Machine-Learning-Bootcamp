# 49 - Categorical Plots

```py
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')
tips.head()
```

## Bar Plot

Aggregates categorical data by a function *(Normally mean)*. Shows the average per categorical column value by default.

Estimator objects: Statistical function that estimate within each categorical bin. Custom functions can be placed into the `estimator` perimeter.

* `x` is categorical
* `y` is numerical


```py
# Average Values
sns.barplot(x='sex',y='total_bill',data=tips)

# Standard Deviation
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
```

## Count Plot

Same as the bar plot but the estimator is counting the number of occurances. **Only set the x value - categorical*

```py
sns.countplot(x='sex',data=tips)
```

## Box Plot

Used to show distribution of categorical data. This showns the distribution of quantitative data in a way that facilitates comparisons between the variables.

* `x` is categorical
* `y` is numerical

```py
sns.boxplot(x='day',y='total_bill',data=tips)

# Split by hue - Used to compare additional parameter of data
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
```

Results in four quartiles.
* 0% - 25% line
* 25% - 50% first box
* 50% - 75% second box
* 75% - 100% line
* other points (Outliers)

## Violin Plot

Similar to a box plot. Allows to plot all the components that correspond to actual data points (Does not have outliers). Slightly harder to read than a box plot.

* `x` is categorical
* `y` is numerical

```py
sns.violinplot(x='day',y='total_bill',data=tips)

# Split by hue - Side by side
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
```

## Strip Plot

Draws a scatter plot when one variable is categorical. `jitter` set to `True` allows some width to the plot so dense datapoints can be seen easier.

```py
sns.splitplot(x='day',y='total_bill',data=tips,jitter=True)
```

## Swarm Plot

Combination of strip plot and violin plot combined. Points are adjusted so they don't overlap. A drawback of swarm plot is that they don't scale well to large numbers and should be avoided for large datasets.

```py
sns.swarmplot(x='day',y='total_bill',data=tips)

# Combining with a violin plot (Very crowded, not really for presentation but more for analysis)
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='black')
```

## Factor Plot

Most general form of all the plots. The `kind` specified to form any of the graphs shown previously.

```py
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')
```
