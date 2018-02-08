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

titleStyle = {'margin-bottom':'0.5in'}
title = html.H1(children="Making Bionic Better", style = titleStyle)


#################################################################################
#################################################################################
# Interaction
#################################################################################
#################################################################################

weekdropDown = dcc.Dropdown\
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

weekMeetDays = html.Div([
    html.Label('Days of the week you meet'),
    weekdropDown
    ])

buttonStyle = {'margin-bottom': '0.3in'}
submitButton = html.Button('Update Class', id='button', style=buttonStyle)

interactStyle = {'columnCount':1,
                 'width':'70%',
                 'position':'relative',
                 'text-align':'justify',
                 }
interaction = html.Div([submitButton, weekMeetDays], style = interactStyle)

#################################################################################
#################################################################################
# End Interaction
#################################################################################
#################################################################################

responseStyle = {'width':'100%',
                 'position':'relative',
                 'text-align':'justify'
                 }
interactResponse = html.Div(id='interact-response', style=responseStyle)

bodyStyle = {'columnCount':2}
body = html.Div([interaction, interactResponse], style=bodyStyle)


hruleStyle = {'margin-bottom':'0.5in'}
hrule = html.Hr(style=hruleStyle)

page = html.Div(children=[
    title,
    hrule,
    body
    ])


centerstyle = {'text-align':'center'}

myOverallStyle = {'columnCount':1,
           'text-align':'center',
#           'left-margin':'30%',
#           'right-margin':'30%',
           'margin':'auto',
           'width':'50%',
           'top':'0px',
#           'left':'0',
           'position':'relative',
           'padding':'auto',
           'font-family':'Times New Roman'
           }

app.layout = html.Div([page], style=myOverallStyle)


@app.callback(
    Output(component_id='interact-response', component_property='children'),
    [Input('button', 'n_clicks')])
def buttonresponse(numclicks):
    titleColStyle = {'bottom-border':'2pt solid black',
                     'background-color':'green'
                     }
    titlecol = html.Tr([html.Td('Name'), html.Td('Class')],style = titleColStyle)
    row1 = html.Tr([html.Td('Divesh'), html.Td('Algebra')])
    numclicks = 0 if numclicks==None else numclicks
    row2 = html.Tr([html.Td('Matt'), html.Td('CS30' + str(numclicks))])
    tableStyle = {'border' : '1px solid black',
                  'text-align':'center',
                  'padding':'0.5em',
                  'width':'100%'
                  }
    simpleTable = html.Table([titlecol, row1, row2], style=tableStyle)
    classNm = 'pure-table pure-table-horizontal'
    ret = html.Div([simpleTable], className=classNm)
    return ret


# fixing the css
#app.css.append_css({"external_url": "https://unpkg.com/purecss@1.0.0/build/pure-min.css"})

#app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
