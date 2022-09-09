# 53 - Style and Colour

 ```py
import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
```

## Setting Styles

Styles can be customised by using the method `sns.set_style()`. Options are:

* `white` plain white background
* `ticks` ticks at the edge of the box
* `darkgrid` dark grid background
* `whitegrid` white grid background

```py
sns.set_style()
sns.countplot(x='sex',data=tips)
```

The graph spines can also be removed by calling the method `sns.despine()`. There are four parameters - top, right, bottom, left. By default, top and right are `True` while left and bottom are `False`.

```py
sns.despine()
```

## Size and Aspect

Matplotlib's `plt.figure.figsize()` can be used to change the size of seaborn plots since it's built on top of matplotlib.

```py
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)
```

## Scale and Context

Seaborn comes with `.set_context()` which allows the changing of default parameters and font scales. These default options are available:

* paper
* notebook
* talk
* poster

The font scale can still be adjusted after setting the default option if it's still too big/too small.

```py
sns.set_context('poster')
sns.countplot(x='sex',data=tips)
```

## Changing Colours

Changing the colourmap can be done by changing the `palette` parameter in the plot. This can be done by going to the colourmap documentation on matplotlib's website.

https://matplotlib.org/stable/tutorials/colors/colormaps.html
