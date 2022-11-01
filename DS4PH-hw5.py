import requests as rq
import bs4
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import os
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
import plotly.express as px

url='https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
page=rq.get(url)
bs4page=bs4.BeautifulSoup(page.text,'html.parser')
t=bs4page.find('table',{'class':'wikitable'})

df=pd.read_html(str(t))[0]


df=df.iloc[:,[0,2,4,6]]
df=df.rename(columns={'IMF[1]':'IMF','United Nations[12]':'United Nations','World Bank[13][14]':'World Bank'})
flag={'Country/Territory':[],'Organization':[],'GDP':[]}
new_df=pd.DataFrame(flag)

for i in range(1,4):
    org=df.columns[i][0]
    for j in range(df.shape[0]):
        nr={'Country/Territory':df.iloc[j][0],'Organization':org,'GDP':df.iloc[j][i]}
        new_df=new_df.append(nr,ignore_index=True)  
        
app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(options = [
            {'label' : 'IMF', 'value' : 'IMF'},
            {'label' : 'United Nations', 'value' : 'United Nations'},
            {'label' : 'World Bank', 'value' : 'World Bank'}
        ],
        value = 1, id = 'input-level'
                ),
    dcc.Graph(id = 'output-graph')
])


@app.callback(
    Output('output-graph', 'figure'),
    Input('input-level', 'value'))
def update_figure(selected_org):
    subdat = new_df.loc[new_df['Organization'] == selected_org].sort_values(by = ['GDP'])
    fig = px.bar(subdat, x='Country/Territory', y='GDP')
    return fig

if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run_server(host='jupyter.biostat.jhsph.edu', port = os.getuid() + 37)