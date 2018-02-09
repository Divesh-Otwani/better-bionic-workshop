# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State



app = dash.Dash()

title = html.H1(children="Making Bionic Better")


textinput = html.Div([
    dcc.Input(id='my-id', value='', type='text'),
    html.Div(id='my-div')
])



app.layout = html.Div([title, "Hello World", textinput])

@app.callback(Output('my-div', 'children'), [Input('my-id', 'value')], [])
def doSomethingWithTextInput(textInput):
    youEntered = "You entered {}".format(textInput)
    return youEntered




if __name__ == '__main__':
    app.run_server(debug=True)
