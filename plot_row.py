
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from data_api import Data_Api
from plots import Plots

"""
composes a row containing plots
"""
api = Data_Api()

plot_row = dbc.Row([
    dbc.Col([
        html.H3("Time Series",
                className='text-center text-primary mb-4'),
        dcc.Dropdown(id='file_dropdwn', multi=False, value=api.csv_list()[0]['value'],
                     options=api.csv_list(),  clearable=False,
                     ),

        dcc.Graph(id='series_fig', figure={})
    ], xs=12, sm=12, md=12, lg=5, xl=5
    ),
    dbc.Col([
        html.H3("Distribution",
                className='text-center text-primary mb-4'),
        dcc.Dropdown(id='distribution', multi=False, value=Plots.get_plot_list()[0],
                     options=[{'label': x, 'value': x}
                              for x in Plots.get_plot_list()], clearable=False,
                     ),
        dcc.Graph(id='dist_fig', figure={})
    ], xs=12, sm=12, md=12, lg=5, xl=5
    ),
], justify='center')
