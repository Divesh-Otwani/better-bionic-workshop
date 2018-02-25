# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash()

title = html.H1(children=["Making A Table"])
htmlBr = html.Br()

###### Table Def

titlecell1 = html.Td('Name')
titlecell2 = html.Td('Class')
titlerow = html.Tr([titlecell1, titlecell2])

row1cell1 = html.Td('Divesh')
row1cell2 = html.Td('Algebra')
row1 = html.Tr([row1cell1, row1cell2])

row2cell1 = html.Td('Matt')
row2cell2 = html.Td('Analysis')
row2 = html.Tr([row2cell1, row2cell2])

table = html.Table([titlerow, row1, row2])

###### End of Table Def


listOfHtmlElements = [title, htmlBr, table]

topHtmlElement = html.Div(children=listOfHtmlElements)
app.layout = topHtmlElement


"""

Obviously you can produce html tables
with callbacks.
So, you can make a button that makes a table when you
click it.

Next, in style.py, we show you
that you can style the page and each element
(and each element's style overrides the style from the
element in which it's contained).

Long story short, you can do things like color the cells in a table,
make a table with any kind of border you want, control spacing,
make things centered with nice backgrounds and so on.

And, you can do all of these in response to clicking a button, 
selecting from a drop down, moving a slider.

"""


if __name__ == '__main__':
    app.run_server(debug=True)




