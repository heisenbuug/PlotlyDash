import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/gapminderDataFiveYear.csv')

app = dash.Dash()

yearOptions = []
for year in df['year'].unique():
    yearOptions.append({'label':str(year), 'value':year})

app.layout = html.Div([
            dcc.Graph(id='graph'),
            dcc.Dropdown(id='yearPicker', options=yearOptions,
                            value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
                [Input('yearPicker', 'value')])

def updateFigure(sYear):

    nDf = df[df['year']==sYear]

    traces=[]
    for item in nDf['continent'].unique():
        print(item)
        contDf = nDf[nDf['continent']==item]
        traces.append(go.Scatter(
            x=contDf['gdpPercap'],
            y=contDf['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size':15},
            name=item
        ))
        print(contDf['lifeExp'])
    return {'data':traces, 'layout':go.Layout(title='Country Plots',
                                                xaxis={'title': 'GDP/Capita',
                                                        'type':'log'},
                                                yaxis={'title':'Life Expectancy'})}

if __name__ == '__main__':
    app.run_server()
