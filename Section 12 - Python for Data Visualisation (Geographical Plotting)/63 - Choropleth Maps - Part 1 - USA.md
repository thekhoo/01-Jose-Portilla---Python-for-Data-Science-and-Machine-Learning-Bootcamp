# 63 - Choropleth Maps - Part 1 - USA

The course focuses on using `plotly` for plotting due to its interactive capabilities. `matplotlib` also has a function for static plots using the `basemap` extension.

**Choropleth Cheat Sheet** https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf

**Importing packages**
```py
import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
```

Now we need to begin to build our data dictionary. Easiest way to do this is to use the **dict()** function of the general form:

* type = 'choropleth',
* locations = list of states
* locationmode = 'USA-states'
* colorscale= 

Either a predefined string:

    'pairs' | 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' | 'Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'

or create a [custom colorscale](https://plot.ly/python/heatmap-and-contour-colorscales/)

* text= list or array of text to display per point
* z= array of values on z axis (color of state)
* colorbar = {'title':'Colorbar Title'})

Here is a simple example:

```py
data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],            # Text same index sequence as the locations
            z=[1.0,2.0,3.0],                            # Values to be shown on the colourbar (Follows index sequence too)
            colorbar = {'title':'Colorbar Title'})
```

Then, a layout object is created.

```py
layout = dict(geo={'scope':'usa'})
```

Then, plot using `.iplot()`. If `.plot()` is used instead, this will open a new HTML window and the image can be saved as an image.

```py
choromap = go.Figure(data=[data],
                     layout=layout)

iplot(choromap)
```

## Example with Real Data from a DataFrame

```py
# Reading Data from a DataFrame
import pandas as pd

df = pd.read_csv('data/2011_US_AGRI_Exports')
data = dict(
    type            = 'choropleth',
    colorscale      = 'ylorbr',
    locations       = df['code'],
    locationmode    = 'USA-states',
    z               = df['total exports'],
    text            = df['text'],
    colorbar        = {'title': 'Millions USD'},
    marker          = dict(
                        line = dict(
                            color = 'rgb(12,12,12)',
                            width=1
                        ))
)

layout = dict(
    title   = '2011 US Agriculture Exports by State',
    geo     = dict(
                scope='usa',
                showlakes=True,
                lakecolor='rgb(85,173,240)'
            )
)

# Saving the map and plotting it with iplot()
choromap2 = go.Figure(data=[data],layout=layout)
iplot(choromap2)
```

