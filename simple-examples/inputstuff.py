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
    value='MTL', # default value
    id='dropdown1'
)

multiSelectDropDown = dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF'], # default value
    multi=True, # notice this is the only change from the last example
    id='dropdown2'
)

radioSelect = dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    id='radio'
)


checkboxes = dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF'],
    id='checkboxes'
)


slider = dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) for i in range(1, 6)},
    value=5,
    step=1,
    id='slider'
)


smoothe_slider = dcc.Slider(
    min=0,
    max=9,
    marks={},
    value=5,
    step=0.01,
    id='sslider',
    )

button = html.Button('Print Everything', id='the-button')
printEverything = html.P(children=[], id='print-everything-id')
sliderValue = html.P(children=[], id='slider-callback')

###########################################################
###########################################################


# Layout
allElems = [title, breakTag, dropdown,
            breakTag, breakTag, multiSelectDropDown,
            breakTag, breakTag, radioSelect,
            breakTag, breakTag, checkboxes,
            breakTag, breakTag, slider,
            breakTag, breakTag, smoothe_slider,
            breakTag, breakTag, button,
            breakTag, breakTag, printEverything,
            breakTag, breakTag, sliderValue,
            ]
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

@app.callback(
    Output(component_id='print-everything-id', component_property='children'),
    [Input(component_id='the-button', component_property='n_clicks')],
    [
        State('dropdown1', 'value'),
        State('dropdown2', 'value'),
        State('radio', 'value'),
        State('checkboxes', 'values'),
        State('slider', 'value'),
        State('sslider', 'value')
     ]
    )
def printEverything(numClicks, drop1, drop2, radio, checkbox, slider, sslider):
    drop1s = "Dropdown 1 is {}".format(drop1) + "  "
    drop2s = "Dropdown 2 is {}".format(drop2) + "  "
    radios = "Radio is {}".format(radio)  + "  "
    cbox = "Checkbox is {}".format(checkbox) + "  "
    slide = "Slider is {}".format(slider) + "   "
    sslide = "Slider is {}".format(sslider) + "  "
    everything = drop1s + drop2s + radios + cbox + slide + sslide
    return everything




@app.callback(
    Output(component_id='slider-callback', component_property='children'),
    [Input('sslider', 'value')],
    []
    )
def showSliderCallback(sliderVal):
    return "Slider Value is {}".format(sliderVal)


###########################################################
###########################################################


if __name__ == '__main__':
    app.run_server(debug=True)
