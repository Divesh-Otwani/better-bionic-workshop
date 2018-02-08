# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

"""

TODO:

take input and display a schedule
via a colored table with each slot representing
a time

https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_td_bgcolor


"""

app = dash.Dash()


title = html.H1(children="Making Bionic Better")

weekMeetDays = dcc.Dropdown\
    (\
    options=[
            {'label': 'Monday', 'value': 'Mo'},
            {'label': 'Tuesday', 'value': 'Tu'},
            {'label': 'Wednesday', 'value': 'We'},
            {'label': 'Thursday', 'value': 'Th'},
            {'label': 'Friday', 'value': 'Fr'}
        ],
    value=['Mo', 'We', 'Fr'],
    multi=True
    )

submitButton = html.Button('Update Age', id='button')

buttonStuff = html.Div([submitButton, html.Div(id='button-response')],
                       style={'columnCount':2})

centerstyle = {'text-align':'center', 'margin-left':'auto', 'margin-right':'auto'}


graphEx = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )




page = html.Div(children=[
    title,
    html.Label('Days of the week you meet'),
    weekMeetDays,
    html.Label('Input Test: '),
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div', style=centerstyle),
    html.Hr(),
    buttonStuff
    ])


myStyle = {'columnCount':1,
           'text-align':'center',
#           'left-margin':'30%',
#           'right-margin':'30%',
           'margin':'auto',
           'width':'50%',
           'top':'0px',
#           'left':'0',
           'position':'relative',
           'padding':'auto'
           }

app.layout = html.Div([page], style=myStyle)


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output(component_id='button-response', component_property='children'),
    [Input('button', 'n_clicks')])
def buttonresponse(numclicks):

    titlecol = html.Tr([html.Td('Name'), html.Td('Age')])
    row1 = html.Tr([html.Td('Divesh'), html.Td('Five')])
    row2 = html.Tr([html.Td('Matt'), html.Td(str(numclicks))])
    simpleTable = html.Table([titlecol, row1, row2], style=centerstyle)
    ret = html.Div([simpleTable], style = centerstyle)
    return ret


# fixing the css
#app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
