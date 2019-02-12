import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
                    html.Label('This is my first Dropdown'),
                    dcc.Dropdown(options = [
                                            {'label': 'Ahmedabad',
                                                'value': 'GUJ'},
                                            {'label': 'Mumbai',
                                                'value': 'MH'}],
                                value = 'IN'),
                    html.Label('Slider'),
                    dcc.Slider(min = -10, max = 10, step = 0.5, value = 69,
                                marks = {i: i for i in range(-10, 10)}),

                    html.P(html.Label('We are radio items')),
                    dcc.RadioItems(options = [{'label': 'Apple',
                                                'value': 'AP'},
                                                {'label': 'Strawberry',
                                                    'value': 'Berry'}],
                                    value = 'Select')

])

if __name__ == '__main__':
    app.run_server()
