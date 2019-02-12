import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

app = dash.Dash()

df = pd.read_csv('data/wheels.csv')

def encodeImage(img):
    encode = base64.b64encode(open(img, 'rb').read())
    return 'data:image/png;base64,{}'.format(encode.decode())

app.layout = html.Div([
            html.Div(dcc.Graph(id='wheels',
                                figure={'data':[go.Scatter(
                                                        x=df['color'],
                                                        y=df['wheels'],
                                                        dy=1,
                                                        mode='markers',
                                                        marker={'size':15}
                                )],
                                'layout':go.Layout(title='Foo', hovermode='closest')}
                                ), style={'width':'30%', 'float':'left'}),
            html.Div([html.Img(id='hover-data', src='children', height=300)],
                        style={'paddingTop':35}),

])

# @app.callback(Output('hover-data', 'children'),
#                 [Input('wheels', 'hoverData')])  #hoverData is predefined into the library
# def callback(hoverData):
#     return json.dumps(hoverData, indent=2)

@app.callback(Output('hover-data', 'src'),
                [Input('wheels', 'hoverData')])
def callback(hoverData):
    wheel = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = 'data/images/'
    return encodeImage(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()
