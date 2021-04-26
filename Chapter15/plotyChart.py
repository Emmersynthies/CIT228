import matplotlib.pyplot as plt
from numpy.random import random

import plotly.graph_objects as go
from plotly import offline

days = [25,26,27,28,29,30]
highTemps = [35,51,57,56,48,44]
lowTemps = [32,45,48,50,43,40]


fig = go.Figure()
# Create and style traces
fig.add_trace(go.Scatter(
    x=days, 
    y=highTemps, 
    name='highTemps',
    line=dict(color='red', width=4)
))
fig.add_trace(go.Scatter(
    x=days, 
    y=lowTemps, 
    name='lowTemps',
    line=dict(color='blue', width=4)
))
# Edit the layout
fig.update_layout(
    title='Tempatures in Frankfort, MI',
    xaxis_title='Days',
    yaxis_title='Temperature (degrees F)'
)
fig.show()