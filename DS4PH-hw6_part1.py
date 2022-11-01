from dash import Dash, dcc, html, Input, Output
import os

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Enter your data to see the results"),
    html.Div([
        html.H2('Enter your weight'),
        dcc.Input(id = 'weight', value = 95, type = 'number'),
        html.H2('Is this weight in Kilograms(kgs) or Pounds(lbs)'),
        dcc.RadioItems(options = [{'label': 'Kilogram', 'value': 'kg'},{'label': 'Pound', 'value': 'lb'}],
                       value = 'kg',
                       id = 'weight_unit'),
        html.H2('Enter your height'),
        dcc.Input(id = 'height', value = 2, type = 'number'),
        html.H2('Is this height in Meters(m) or Feet(ft)'),
        dcc.RadioItems(options = [{'label': 'Meters', 'value': 'm'},{'label': 'Feet', 'value': 'ft'}],
                       value = 'm',
                       id = 'height_unit')

    ]),
    html.Br(),
    html.H1("Your body mass index is: "),
    html.H1(id = 'bmi')

])


@app.callback(
    Output(component_id = 'bmi'   , component_property = 'children'),
    Input(component_id  = 'weight', component_property = 'value'),
    Input(component_id  = 'weight_unit', component_property = 'value'),
    Input(component_id  = 'height'   , component_property = 'value'),
    Input(component_id  = 'height_unit'   , component_property = 'value')
)
def update_output_div(weight, weight_unit,height,height_unit):
    if weight_unit == 'lb':
        weight=weight*0.453
    if height_unit == 'ft':
        height=height/3.2808
    rval=weight/(height*height)
    return rval

if __name__ == '__main__':
    app.run_server(host='jupyter.biostat.jhsph.edu', port = os.getuid() + 37)