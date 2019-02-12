import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
X = np.random.randint(1, 101, 100)
Y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id = 'scatterPlot2',
                                    figure = {'data' : [
                                        go.Scatter(
                                            x = X,
                                            y = Y,
                                            mode = 'markers'
                                        )],
                                    'layout' : go.Layout(title = 'Scatter PLot First')}
                                ),

                                dcc.Graph(id = 'scatterPlot',
                                            figure = {'data' : [
                                                go.Scatter(
                                                    x = X,
                                                    y = Y,
                                                    mode = 'markers'
                                        )],
                                    'layout' : go.Layout(title = 'Scatter PLot Second')}
                        )])

if __name__ == '__main__':
    app.run_server()
