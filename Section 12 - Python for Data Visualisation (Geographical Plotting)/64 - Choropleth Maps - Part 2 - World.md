# 64 - Choropleth Maps - Part 2 - World

This section will focus on an **international level** for maps.

```py
import chart_studio.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
df = pd.read_csv('data/2014_World_GDP')

data = dict(
    type            = 'choropleth',
    locations       = df['CODE'],
    z               = df['GDP (BILLIONS)'],
    text            = df['COUNTRY'],
    colorbar        = {'title': 'GDP IN BILLIONS USD'},
)

layout = dict(
    title   = '2014 Global GDP',
    geo     = dict(
                showframe=False,
                projection={'type':'mercator'}
            )
)

choromap = go.Figure(data=[data],layout=layout)
iplot(choromap)
```