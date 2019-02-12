import dash
import dash_html_components as html
import pandas as pd

app = dash.Dash()

app.layout = html.Div(['This is the outerMost Div',
                        html.Div(['This is an innerDiv'],
                        style = {'color': 'red', 'border': '3px black solid'}),
                        html.Div(['This is Second Inner Div'],
                        style = {'color': 'blue', 'border': '4px blue solid'})],
                    style = {'color': 'green', 'border': '2px green solid'})



if __name__ == '__main__':
    app.run_server()
