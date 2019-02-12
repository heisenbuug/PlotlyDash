import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv('data/OldFaithful.csv')

#Launching the application
app = dash.Dash()

# Create a dash Layout that contains a Graph Component
app.layout = html.Div([dcc.Graph(id = 'Figure',
                                    figure = {'data': [go.Scatter(x = df['X'],
                                                                    y = df['Y'],
                                                                        mode = 'markers')],
                                         'layout': go.Layout(title = 'Options',
                                                                xaxis = {'title': 'Duration'},
                                                                yaxis = {'title': 'Interval'})})])

if __name__ == '__main__':
    app.run_server()
