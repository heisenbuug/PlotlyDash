import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

data = pd.read_excel('data.xlsx')

x_data = data['X']
y_data = data['Y']

trace0 = go.Scatter(x = x_data, y = y_data + 500,
                    mode = 'markers', name = 'Markers')

trace1 = go.Scatter(x = x_data, y = y_data,
                    mode = 'lines', name = 'Lines')

trace2 = go.Scatter(x = x_data, y = y_data - 500,
                    mode = 'lines+markers', name = 'Lines & Markers')
data = [trace0, trace1, trace2]

layout = go.Layout(title = 'Line Charts')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig, filename = 'lineCharts.html')
