import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import base64

df = pd.read_csv('data/wheels.csv')

app = dash.Dash()

def encodeImage(img):
    encode = base64.b64encode(open(img, 'rb').read())
    return 'data:image/png;base64,{}'.format(encode.decode())

app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                            options=[{'label':i,'value':i}for i in df['wheels'].unique()],
                            value=1
                            ),
            html.Div(id='wOutput'),
            html.Hr(),
            dcc.RadioItems(id='color',
                            options=[{'label':i,'value':i}for i in df['color'].unique()],
                            value='blue'),
            html.Div(id='cOutput'),
            html.Img(id='image', src='children', height=300)
                    ],
                    style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(Output('wOutput', 'children'),
            [Input('wheels', 'value')])
def callbacka(wValue):
    return "You choose {}".format(wValue)

@app.callback(Output('cOutput', 'children'),
            [Input('color', 'value')])
def callbackb(cValue):
    return "You choose " + cValue

@app.callback(Output('image', 'src'),
                [Input('wheels', 'value'),
                Input('color', 'value')])
def callImage(wheel, color):
    path = 'data/images/'
    return encodeImage(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])

if __name__ == '__main__':
    app.run_server()
