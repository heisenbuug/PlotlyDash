import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
            dcc.Input(id = 'myId', value = 'Initial Text', type='text'),
            html.Div(id='myDiv')
])

@app.callback(Output(component_id='myDiv', component_property='children'),
[Input(component_id='myId', component_property='value')])
def update_op_div(input_val):
    return "You entered " + input_val

if __name__ == '__main__':
    app.run_server()
