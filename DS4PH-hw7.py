import os
from datetime import date
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Choose value of Beta 1"),
    dcc.Slider(min = -10, max = 10, step = 0.5, value = 10, id='beta1'),
    html.H1("Choose value of Beta 0"),
    dcc.Slider(min = -10, max = 10, step = 0.5, value = 10, id='beta0'),
    dcc.Graph(id='final_graph')
])

@app.callback(Output('final_graph', 'figure'),
              Input(component_id  = 'beta1', component_property = 'value'),
              Input(component_id  = 'beta0', component_property = 'value'))

def update_output_div(beta1,beta0):
    x=np.linspace(-5, 5, 1000)
    eta=beta0 + beta1 *x
    p = 1 / (1 + np.exp(-eta))
    h=px.line(x=x,y=p)
    #h.show()
    return(h)
              

if __name__ == '__main__':
    app.run_server(host='jupyter.biostat.jhsph.edu', port = os.getuid() + 38)