import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output


external_stylesheets=[dbc.themes.CYBORG]   # dark theme 😎

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = pd.read_csv("IndividualDetails.csv")
active = df[df['current_status'] == 'Hospitalized'].shape[0]
total = df.shape[0]
death = df[df['current_status'] == 'Deceased'].shape[0]
recover = df[df['current_status'] == 'Recovered'].shape[0]

options = [
    {'label': 'All', 'value': 'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}
]

app.layout=html.Div([
    html.H1("Corona Virus Pandemic",style={"textAlign":"center"}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total cases'),
                    html.H4(total)
                ],className='card-body')
            ],className='card bg-danger')
        ],className="col-md-3"),
        html.Div([html.Div([
                html.Div([
                    html.H3('Active cases'),
                    html.H4(active)
                ],className='card-body')
            ],className='card bg-info')], className="col-md-3"),
        html.Div([html.Div([
                html.Div([
                    html.H3('Recovered'),
                    html.H4(recover)
                ],className='card-body')
            ],className='card bg-warning')], className="col-md-3"),
        html.Div([html.Div([
                html.Div([
                    html.H3('Deaths'),
                    html.H4(death)
                ],className='card-body')
            ],className='card bg-success')], className="col-md-3")
    ], className="row"),
    html.Div([], className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker', options=options, value='All'),
                    dcc.Graph(id='bar')
                ], className='card-body')
            ], className="card"),
        ], className='col-md-12')
    ], className="row")
], className = "container")


@app.callback(Output('bar', 'figure'),[Input('picker', 'value')])
def update_graph(type):

    if type == 'All':
         df_bar = df['detected_state'].value_counts().reset_index()
         return {'data':[go.Bar(x=df_bar['detected_state'],y=df_bar['count'])],
                'layout':go.Layout(title="State Total count")}
    else:
        df_hs = df[df['current_status'] == type]
        df_br = df_hs['detected_state'].value_counts().reset_index()
        return {'data': [go.Bar(x=df_br['detected_state'], y=df_br['count'])],
                'layout': go.Layout(title="State Total count")}

if __name__ == "__main__":
    app.run(debug=True)