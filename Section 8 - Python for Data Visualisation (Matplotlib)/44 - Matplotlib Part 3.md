# 44 - Matplotlib Part 3

## Plot Appearance

### Color

The color parameter, `color=`, can take in multiple arguments like common color strings - `green`, `blue`, `red`. RGB Hex Codes can also be used.

```py
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='#FF8C00')

# OR

ax.plot(x,y,color='purple')
```

### Line Width

The line width can also be passed in as an argument through `linewidth=` OR `lw=`. Positive numbers can be used to control the thickness of the line

```py
ax.plot(x,y,color='purple',lw=3)     # Thicker
# OR
ax.plot(x,y,color='purple',linewidth=0.5)   # Thinner
```
### Transparency

The transparency can be adjusted by inserting a value under the alpha parameter, `alpha=`.

```py
ax.plot(x,y,color='purple',linewidth=0.5,alpha=0.5)   # Half transparent
```

### Line Style

Linesyles can be passed in as a string under the `linestyle=` or `ls=` parameter. Options include:

* '--' Dashed line
* '-' Solid Line
* '-.' Dash and Dot Line
* 'steps' to give a Stepped Graph.

### Markers

Markers are, normally, only used when there are a few data points. Done by adding `marker=` in the parenthesis. Default is normally `marker=o`.

```py
ax.plot(x,y,color='purple',ls=0.5,marker='o')
```

Marker size can also be specified
```py
ax.plot(x,y,color='purple',ls=0.5,marker='o',markersize = 20.)

markerfacecolour = 'yellow' # Colour of image/ace
marketedgewithtism
markerdeDGECOVER = 'green' 
```

## Minimum and Maximum Values (Y-limit and X-limit)

Showing the plot between 0 and 1.

```py
ax.set_xlim([0.1])
ax.set_ylin([0,2])
```
## Plots

Scatter plots, histograms and box plots can still be done using matplotlib (even though Seaborn does it better)

**Massive presence online for matplotlib graph design but Seaborn still better (As Seaborn is built for this)**
