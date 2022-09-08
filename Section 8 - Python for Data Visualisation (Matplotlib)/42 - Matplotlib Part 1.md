# 42 - Matplotlib Part 1

Matplotlib is the "grandfather" library of data visualization with Python. It was created by John Hunter. He created it to try to replicate MatLab's (another programming language) plotting capabilities in Python. So if you happen to be familiar with matlab, matplotlib will feel natural to you.

It is an excellent 2D and 3D graphics library for generating scientific figures. 

Some of the major Pros of Matplotlib are:

* Generally easy to get started for simple plots
* Support for custom labels and texts
* Great control of every element in a figure
* High-quality output in many formats
* Very customizable in general

Matplotlib allows you to create reproducible figures programmatically. Let's learn how to use it! Before continuing this lecture, I encourage you just to explore the official Matplotlib web page: http://matplotlib.org/

## Installation 

You'll need to install matplotlib first with either:

    conda install matplotlib
or
    pip install matplotlib

```py
import matplotlib.pyplot as plt
import numpy as np
```

## Plotting

There's two ways of plotting:
* Functional Method
* Object-Oriented Method (Better)

**Functional Method**
```py
x = np.linspace(0,5,11)
y = x ** 2

# Functional Method
plt.plot(x,y)   # Linestyles and colours can be added similar to how it's done in MATLAB
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()

# Functional Method - Multiplots on the same canvas
num_rows = 1    # Number of Rows in the subplot
num_cols = 2    # Number of Columns in the subplot
plot_num = 1    # Number for the current plot

plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')
```

**Object-Oriented Method**
Creating figure objects and calling methods off of it.
```py
# Object Oriented Method
fig = plt.figure()  # Creates a figure object (Blank canvas)
axes = fig.add_axes([left,bottom,width,height]) # Adds axes to the plot
axes.plot(x,y) # Plot the data
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Title')

# Object Oriented Method - Multi Axis
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) # left, bottom, width, height
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # numbers must be between 0 and 1

axes1.plot(x,y)
axes1.set_title('Larger Plot')

axes2.plot(y,x)
axes2.set_title('Smaller Plot')
```

