
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


""" 
composes a modal for downloading stock csv files
"""
download_modal = html.Div([

    dbc.Modal([

        dbc.ModalHeader(
            "Select term and enter ticker symbol to download data."),
        dbc.ModalBody([

            dbc.RadioItems(
                id="radios",
                class_name="btn-group d-flex flex-row justify-content-center ml-3 ",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary",
                labelCheckedClassName="active",
                options=[
                    {"label": "6mo", "value": "6mo"},
                    {"label": "1y", "value": "1y"},
                    {"label": "2y", "value": "2y"},
                    {"label": "5y", "value": "5y"},
                    {"label": "10y", "value": "10y"},
                ],
                value="1yr",
            ),

            dbc.Form([
                dbc.Label("Symbol", style={"content-align": "center"}),
                dbc.Input(type="text", id="ticker_id",
                          placeholder="example: GOOGL", style={"margin": "20px"}),
                dbc.Button(id="ticker_submit", children="Submit",
                           color="primary", style={"margin": "20px"}),
            ], class_name="d-flex flex-row ml-3 p-3", style={"padding": "1em"}),

            dcc.Loading(id="spinner",
                        children=[html.Div([html.Div(id="spinner_out")])],
                        type="circle",),

        ]),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="close_modal",
                className="ms-auto",
                n_clicks=0,
            )
        )
    ], id="data_api_modal",
        is_open=False,
        className="modal-lg",
        backdrop='static',
        keyboard=False,
        fade=True),
])


confirmation = html.H4('', id="success_ouput", className='bg-success text-white',
                       style={"text-align": "center", "vertical-align": "text-top", "padding": "10px"})

failed = html.H4('', id="success_ouput", className='bg-danger text-white',
                 style={"text-align": "center", "vertical-align": "text-top", "padding": "10px"})
