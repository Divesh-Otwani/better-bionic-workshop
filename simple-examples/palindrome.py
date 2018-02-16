# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

"""
Just import the stuff above.
You will need all of it, usually in each file.
"""

app = dash.Dash()

"""
dash.Dash() is your actual web server as an object.
It's an instance of the class dash.Dash().

Hopefully you are familiar enough with imports to understand
how you can refer to things you define in imported files;
I can get dcc.someFunction for example.

------------------------------------------------------
Building a web server.

------------------------------------------------------
Right now, we are building a web server
that displays one page, and on that page there is box to type
a string and a button that says "check if palindrome"
and once we click the button, some text is printed
telling us if we have a palindrome.



For making a single web page, do you this:

1) Build html elements and nest all of them in some large html element.
2) Assign the large html element to app.layout
3) Write a bunch of callback functions

and it has to be done in that exact order.

The background from the README.md file that is in the same folder
as this file covered most of what you need to know.

All you need now, is to know
 1) How do I make html elements in here?
 2) What are callback functions?

We answer these below.

"""



##############################################################
#                Making HTML Elements
##############################################################

title = html.H1(children=["A Simple Palindrome Example"])

# From reading the links in the readme, you should know about
# the html H1 to H6 tags: https://www.w3schools.com/tags/tag_hn.asp
# This represents that tag
# The first argument is named "children" for html.Anything
# (See here http://www.diveintopython.net/power_of_introspection/optional_arguments.html)
# The children is a list of other html elements
# You can use strings for html elements when it's simple enough

stringInputBox = dcc.Input(id='inputbox-id', value='', type='text')

# Input boxes are bit more complicated,
# You make an object that is an instance of the class dcc.Input
# Then, you specify a string for an unique id,
# An initial value to display
# and that the type of input is text like shown

checkIfPalButton = html.Button(children='Check If Palindrome', id='button-id')
# Buttons are similar

displayIfPalindrome = html.Div(children=[], id='response-id')
# This is div html tag (look it up on w3school.org)
# It has no children. I could have written
# html.Div(id='response-id') and that would be the same
# The default value of children is []
# We will insert html elements into the list children when
# the button is clicked.

listOfHtmlElements = [title, stringInputBox,checkIfPalButton,displayIfPalindrome]

topHtmlElement = html.Div(children=listOfHtmlElements)

##############################################################
##############################################################


# Now, you say that the web page you want to display
# just shows this one html element.
app.layout = topHtmlElement








##############################################################
#             Making Callback Functions
##############################################################

# You know this function:
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
    return retMsg

"""
# Alright, how do callbacks work?

at the top you write
@app.callback(Output(...), listOfInput, listOfState)

The first arguement is an instance of Output.
Your provide two arguments to make an Output,
the first is the id of the html element inside of
which you will put the html element that this function creates.
The second is the argument of this that
you are going to change.

The second argument is a list of instances of Input.
  How do you make input?
  The first arguement is the id.
  The second is the thing you are taking as input.
  These are special strings for different inputs.
  For buttons, the string is 'n_clicks'.
  For text fields, drop downs and other input forms,
  the string is usually 'value'.

The third is the listOfState.
  This is exactly like Input.


# What does it all mean?

Whenever the value inside the input changes,
the function is called with the arguments being
the list of input, then the output in that order.
Here, the first argument to the function
doSomethingWithTextInput is the number of button clicks.
The second is the textInput.

The function returns an html element.
That is inserted into the argument of the Output
we talked about earlier.
Here, the html element the function returns,
(which is just a string)
in inserted into the children list
of the html Div tag with the unique id  'response-id'.


Please contact me if something isn't clear.

"""



##############################################################
##############################################################



"""
Always have these few lines at the bottom of your code.
It just runs your web server
when you do
 $ python palindrome.py
on the command line
"""
if __name__ == '__main__':
    app.run_server(debug=True)
