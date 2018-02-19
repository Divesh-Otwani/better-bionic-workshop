# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


app = dash.Dash()



###########################################################
#                    Html Elements
###########################################################

breakTag = html.Br() # put this and it just adds space between things

title = html.H1("Examples of Other Input Elements")

dropdown = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL' # default value
    )

multiSelectDropDown = dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'], # default value
        multi=True # notice this is the only change from the last example
    )

radioSelect = dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    )


checkboxes = dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        values=['MTL', 'SF']
    )


slider = dcc.Slider(
         min=0,
         max=9,
         marks={i: 'Label {}'.format(i) for i in range(1, 6)},
         value=5,
         step=1,
    )


smoothe_slider = dcc.Slider(
         min=0,
         max=9,
         marks={},
         value=5,
         step=0.01,
    )



###########################################################
###########################################################


# Layout
allElems = [title, breakTag, dropdown,
            breakTag, breakTag, multiSelectDropDown,
            breakTag, breakTag, radioSelect,
            breakTag, breakTag, checkboxes,
            breakTag, breakTag, slider,
            breakTag, breakTag, smoothe_slider]
topHtmlElement = html.Div(allElems)
app.layout = topHtmlElement



###########################################################
#           Two Callbacks
###########################################################



"""
We have two callbacks.

1) A button to just print back out everything


2) A callback that demonstrates that
not just buttons can be input.
It changes anytime you change a slider.


"""



###########################################################
###########################################################


if __name__ == '__main__':
    app.run_server(debug=True)
