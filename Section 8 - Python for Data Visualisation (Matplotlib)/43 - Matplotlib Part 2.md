# 43 - Matplotlib Part 2

## Subplots with Object-Oriented Method

```py
import matplotlib.pyplot as plt
import numpy as np

# Tuple unpacking
fig,axes = plt.subplots(nrows=1,ncols=2)    # Calls fig.add_axes automatically 
axes.plot(x,y)
```

`plt.subplot()` is just an axis manager on top of `plt.figure()`. Tuple unpacking is done to get `fig` and `axes` because axes is just an array of `matplotlib.axes`. Thus, it **can be iterated**.

To deal with overlapping plots in the figure, use the method `plt.tight_layout()` to fix the overlaps.

```py
# Just to show that it's a list of axes
for current_ax in axes:
    current_ax.plot(x,y)
```

## Figure Size, Aspect Ratio and DPI

Matplotlib allows for control over these 3 parameters individually - Figure Size, Aspect Ratio and DPI. They can be specified when calling the figure object.

### Figsize

* `width` - Width of the figure in inches.
* `height` - Height of the figure in inches.

```py
width = 3   # In inches
height = 2  # In inches

fig = plt.figure(figsize=(width,height))
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
```

This works for subplots too.

```py
width = 8   # In inches
height = 2  # In inches

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(width,height))

axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()
```

## Saving Figures

Figures can be saved using the `.savefig()` method.

```py
# dpi can be specified here or in the earlier section.
fig.savefig('my_picture.png',dpi=200)
```

## Legends

Legends can be added to a graph to specify what plot is what. Two steps have to be taken:

1. `ax.legend()` is added at the end of the code for the figure.
2. `label=label_name` has to be specified as a parameter for each different plot

```py
fig = plt.figure()

ax = fig.add_axes()

# Two plots on the same figure
ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.set_title('Title')
ax.set_ylabel('Y')
ax.set_xlabel('X')

# Adding a Legend
ax.legend()
```
A set of parameters to specify the location of the legend using the parameter `loc=` in the parenthesis of `ax.legend()`. This is found in the list below for location code and location string.

1. 0 - `best`
2. 1 - `upper right`
3. 2 - `upper left`
4. 3 - `lower left`
5. 4 - `lower right`
6. 5 - `right`
7. 6 - `center left`
8. 7 - `center right`
9. 8 - `lower center`
10. 9 - `upper center`
11. 10 - `center`

By entering a tuple with two parameters, an bottom and left method can also be used.

```py
ax.legend(loc=(0.1,0.1))
```


