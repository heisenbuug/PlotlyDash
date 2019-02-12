import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

app = dash.Dash()

feature = df.columns
app.layout = html.Div([
            html.Div([
                dcc.Dropdown(id='x', options=[{'label':i,'value':i}for i in feature],
                                value='displacement')
            ], style={'width': '48%', 'display':'inline-block'}),
            html.Div([
                dcc.Dropdown(id='y',
                            options=[{'label':i, 'value':i} for i in feature],
                            value='weight')
            ], style={'width': '48%', 'display':'inline-block'}),
            dcc.Graph(id='graph')
], style={'padding':10})

@app.callback(Output('graph', 'figure'),
                [Input('x', 'value'),
                    Input('y', 'value')])
def update(xName, yName):
    return{'data':[go.Scatter(x=df[xName],
                            y=df[yName],
                            text=df['name'],
                            mode='markers',
                            marker={'size':15,
                                    'opacity':0.5,
                                    'line':{'width':0.5, 'color':'black'}})
                            ]
            ,'layout':go.Layout(title='Automobile',
                                xaxis={'title':xName},
                                yaxis={'title':yName},
                                hovermode='closest'
                                )}

if __name__ == '__main__':
    app.run_server()
