# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash()

"""
Here, we show you some basic stuff on styling.
We do this by making the palindrome.py website
look pretty.


# What is styling?

Styling is making your web page look nice:
controling, the font, colors, spacing,
text justified, centered, tables, table borders,
background, adding pictures and videos,
etc.

Styling is very organized.
We show you the rules by how it works and then
just like to a bunch of websites that mention how to
style extensively.
"""


titleStyle = {'margin-bottom':'0.5in',
              'font-size':'300%'}
title = html.H1(children=["A Simple Palindrome Example"], style=titleStyle)


"""
Here we see one example of styling.

I made a python dictionary and
assigned it to the variable titleStyle.
It maps strings to other strings.

How does it work?

Each html element can be styled a certain way according to the kind of
element it is. html.H1 elements are styled differently from html.Table
or html.Button elements.

The keys of what can be styled are called properties.
The values are called property values.
For example, we see the value of the font size property of
the html element assigned to the variable 'title' is '300%'.

The format we use is inline CSS.
See here: https://www.w3schools.com/html/html_css.asp

For example, this is a styled html element:

 <h1 style="color:blue;">This is a Blue Heading</h1> 


We would encode this as the following.

theStyle = {'color':'blue'}
heading = html.H1("This is a Blue Heading", style = theStyle)


# How did I learn about 'margin-bottom' and 'font-size'?

I googled around.
https://www.w3schools.com/cssref/pr_font_font-size.asp
Search to "how to do X with CSS"
and make guesses and try stuff.


"""




stringInputBox = dcc.Input(id='inputbox-id', value='racecar', type='text')
checkIfPalButton = html.Button(children='Check If Palindrome', id='button-id')
displayIfPalindrome = html.Div(children=[], id='response-id')
dividerLine = html.Hr() # This draws a horizontal line
lineBreak = html.Br() # This adds spacing

##########################################################################
##########################################################################


listOfHtmlElements = [
    title,
    dividerLine,
    lineBreak,
    stringInputBox,
    checkIfPalButton,
    lineBreak,
    lineBreak,
    lineBreak,
    displayIfPalindrome
    ]


pageStyle = {
    'columnCount':1,
    'text-align':'center',
    'margin':'auto',
    'width':'50%',
    'position':'relative',
    'font-family':'Times New Roman'
    }

wholePage = html.Div(children=listOfHtmlElements, style=pageStyle)

# The style above mainly just centeres the page.


topHtmlStyle = {
    'columnCount':1,
    'position':'absolute',
    'background-color':'lightblue',
    'top':0,
    'left':0,
    'right':0,
    'bottom':0,
    }
topHtmlElement = html.Div(children=[wholePage], style=topHtmlStyle)

# This topHtmlStyle just fills a light blue background.

app.layout = topHtmlElement





##########################################################################
##########################################################################



def isPal(s):
    if len(s) < 3:
        return True
    else:
        first = s[0]
        last = s[-1]
        return (first == last) and isPal(s[1:-1])


@app.callback(
    Output('response-id', 'children'),
    [Input('button-id', 'n_clicks')],
    [State('inputbox-id', 'value')]
    )
def doSomethingWithTextInput(numClicksOfButton, textInput):
    isPalMessage = "\"{}\" is in fact a palindome!".format(textInput)
    isNotPalMessage = "\"{}\" is NOT a palindome!".format(textInput)
    retMsg = isPalMessage if isPal(textInput) else isNotPalMessage


    oneelem = html.Td(retMsg)
    row = html.Tr([oneelem])
    tableStyle = {'border' : '5px solid black',
                  'margin':'auto',
                  'border-spacing':'30px',
                  'background-color':'lightgreen',
                  'font-size':'150%'
                  }
    table = html.Table([row], style = tableStyle)
    # we return a nicely formatted table with one cell.

    return table



"""
Most of this is guessing.

I don't know how CSS works and styles things.

I just search online for doing something in CSS
and play around with the key value pairs I can put
in these style dictionaries.




Hopefully the examples here are enough to get you
started on semi decent looking pages.

Please contact me if you want help.

"""



##########################################################################
##############################################################

if __name__ == '__main__':
    app.run_server(debug=True)







