import matplotlib.pyplot as plt
from numpy.random import random

import plotly.graph_objects as go
from plotly import offline

monthsAgo = [6,3,1]
asphalt = [20.2,34,22.4]
plastic = [6.5,2.1,1.1]
softLumber = [30.3,38,7.9]
hardLumber = [16.2,8.4,2.5]
plywood = [11.3,8.1,7.2]
insulation = [6.3,4.2,2.2]


fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=asphalt, 
    name='Asphalt',
    line=dict(color='red', width=4)
))
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=plastic, 
    name='Plastic',
    line=dict(color='blue', width=4)
))
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=softLumber, 
    name='Soft lumber',
    line=dict(color='purple', width=4)
))
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=hardLumber, 
    name='Hard lumber',
    line=dict(color='yellow', width=4)
))
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=plywood, 
    name='Plywood',
    line=dict(color='green', width=4)
))
fig.add_trace(go.Scatter(
    x=monthsAgo, 
    y=insulation, 
    name='insulation',
    line=dict(color='orange', width=4)
))
# Edit the layout
fig.update_layout(
    title='Precent of change in price 6,3,1 months',
    xaxis_title='Over the months',
    yaxis_title='Supplies'
)
fig.show()