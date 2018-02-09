# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

"""

https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_td_bgcolor


"""

app = dash.Dash()

titleStyle = {'margin-bottom':'0.5in',
              'font-size':'300%'}
title = html.H1(children="Making Bionic Better", style = titleStyle)


#################################################################################
#################################################################################
# Interaction
#################################################################################
#################################################################################

nameOfClass = html.Div([
    dcc.Input(id='my-id', value='', type='text'),
    html.Div(id='my-div')
])

weekdropDown = dcc.Dropdown\
    (\
    options=[
            {'label': 'Monday', 'value': 'Mo'},
            {'label': 'Tuesday', 'value': 'Tu'},
            {'label': 'Wednesday', 'value': 'We'},
            {'label': 'Thursday', 'value': 'Th'},
            {'label': 'Friday', 'value': 'Fr'}
        ],
    value=[],
     multi=True,
     id='dropdown'
    )


weekMeetLabelStyle = {'text-align':'justify', 'margin-top':'0.5in'}
weekMeetLabel = html.Label('Days of the week the class meets', style=weekMeetLabelStyle)
weekMeetDays = html.Div([
    weekMeetLabel,
    weekdropDown
    ])



# Time:



buttonStyle = {'margin-bottom': '0.6in'}
submitButton = html.Button('Update Class', id='button', style=buttonStyle)

interactStyle = {}
interaction = html.Div([ nameOfClass, weekMeetDays, submitButton], style = interactStyle)

#################################################################################
#################################################################################
# End Interaction
#################################################################################
#################################################################################

responseStyle ={
                 }
interactResponse = html.Div(id='interact-response', style=responseStyle)


hruleStyle = {'margin-bottom':'0.5in'}
hrule = html.Hr(style=hruleStyle)

page = html.Div(children=[
    title,
    hrule,
    interaction,
    hrule,
    interactResponse
    ])


centerstyle = {'text-align':'center'}

myOverallStyle = {'columnCount':1,
           'text-align':'center',
           'margin':'auto',
           'width':'50%',
           'top':'0px',
#           'left':'0',
           'position':'relative',
           'padding':'auto',
           'font-family':'Times New Roman'
           }

app.layout = html.Div([page], style=myOverallStyle, className='body')

####################################################################################
####################################################################################
####################################################################################
#          Callbacks
####################################################################################
####################################################################################
####################################################################################


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


@app.callback(
    Output(component_id='interact-response', component_property='children'),
    [Input('button', 'n_clicks')],
    [State('my-id', 'value'), State('dropdown', 'value')])
def buttonresponse(numclicks, textInput, dropdown):
    titleColStyle = {
        'text-align':'center',
        'border-bottom':'2px solid #ddd',
        'margin':'auto',
        'position':'relative',
        'padding':'auto',
        }
    titlecol = html.Tr([html.Td('Name'), html.Td('Class')],style = titleColStyle)
    row1 = html.Tr([html.Td('Divesh'), html.Td('Algebra')])
    numclicks = 0 if numclicks==None else numclicks
    row2 = html.Tr([html.Td('Matt'), html.Td('CS30' + str(numclicks))])
    row3 = html.Tr([html.Td('Textfield'), html.Td(textInput)])
    row4 = html.Tr([html.Td('DropDown'), html.Td(dropdown)])
    tableStyle = {'border' : '3px solid black'}
    simpleTable = html.Table([titlecol, row1, row2, row3, row4], style=tableStyle)
    return simpleTable



if __name__ == '__main__':
    app.run_server(debug=True)
