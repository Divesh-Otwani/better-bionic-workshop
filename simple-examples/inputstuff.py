# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

"""
Just import the stuff above.
"""

app = dash.Dash()

"""
dash.Dash() is your actual web server as an object.
It's an instance of the class Dash().

All you do is

1) Build html elements and nest all of them in some large html element.
2) Assign the large html element to app.layout
3) Write a bunch of callback functions

and it has to be done in that exact order.

Of course, there's a bunch of questions here:

0) What is a webserver? What am I making anyway?
1) What is html? What are html elements and how do I make one in python?
2) How do I nest html elements inside each other?
3) What are callback functions? How do I write them?
What do they have to do with what I'm making?

TODO: I'll finish the documenation tomorrow.
Add a button and call back then ... finish the code.

"""

title = html.H1(children=["A Simple Palindrome Example"])

textInputBox = dcc.Input(id='inputbox', value='', type='text')
textResponse = html.Div(id='response')

topHtmlElement = html.Div([title, textInputBox, textResponse])
app.layout = topHtmlElement

@app.callback(Output('response', 'children'), [Input('inputbox', 'value')], [])
def doSomethingWithTextInput(textInput):
    youEntered = "You entered {}".format(textInput)
    return youEntered


if __name__ == '__main__':
    app.run_server(debug=True)
