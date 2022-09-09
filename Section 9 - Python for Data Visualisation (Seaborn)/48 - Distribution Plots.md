# 48 - Distribution Plots

Importing `seaborn` within python.

```py
import seaborn as sns

# Generate a DataFrame as an example
tips = sns.load_dataset('tips')
tips.head()
```

## Dist Plot

Shows the distribution of a univariate distribution. Passes in a single column of a DataFrame. Gives a Histogram and a Kernal Density Estimation (KDE).

* `kde` - True or False (Whether KDE is shown on the graph)
* `bins` - Number of bins on the graph (Bars for the histogram)

```py
sns.distplot(tips['total_bill'],kde=False,bins=30)
```

## Joint Plot

Match up two dist plots for bivariate data. Bivariate - 2 variables.

* `x` One column name of data that is to be compared from the DataFrame passed in
* `y` Second column name of data that is to be compared from the DataFrame passed in
* `data` DataFrame where the data is to be analysed
* `kind` How the distribution is shown
    * `scatter` (default)
    * `hex` (hexagonal distribution)
    * `regression` (regression line)
    * `kde` (2D kde - Density of points)

```py
sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')
```

## Pair Plot

Does a joint plot for every single combination of columns in the DataFrame. Works as a quick way to visualise all the data.

Different color hues can be applied to the pair plot. This can be done by passing in the `hue` parameter.

`palette` can be used to choose groups of colours for the graphs. *From matplotlib*

```py
# Different colors based on sex
sns.pairplot(tips,hue='sex',palette='coolwarm')
```

## Rug Plot

Just like dist plot, a single column of data is taken. A dash is placed at each data point to see the density spread of the data. The KDE is basically a sum of all the normal distributions.

```py
sns.rugplot(tips['total_bill'])
```

# KDE Dist Plot

Dist plot but only with the KDE plot and no histograms.

```py
sns.kdeplot(tips['total_bill'])
```
