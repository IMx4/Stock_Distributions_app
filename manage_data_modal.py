
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from data_api import Data_Api


"""
composes a modal for data managment
"""
api = Data_Api()
csv_files = api.csv_list()

manage_data_modal = html.Div([

    dbc.Modal([

        dbc.ModalHeader("Remove Stored Data"),
        dbc.ModalBody([

            dcc.Dropdown(id='manage_data_dropdwn', multi=False, value=csv_files[0]['value'],
                         options=csv_files,  clearable=False,
                         ),
            html.Div(id='delete-success-div', children=[]),

        ]),
        dbc.ModalFooter([
            dbc.Button(
                "Delete",
                id="delete_file",
                className="ms-auto",
                n_clicks=0,
            ),
            dbc.Button(
                "Close",
                id="close_modal2",
                className="ms-auto",
                n_clicks=0,
            )
        ])
    ], id="manage_data_modal",
        is_open=False,
        className="modal-lg",
        backdrop='static',
        keyboard=False,
        fade=True),
])

confirm_delete = html.H4("", id="delete_success_ouput", className="alert alert-success text-white",
                         style={"text-align": "center", "vertical-align": "text-top", "padding": "10px"})

delete_failed = html.H4("", id="delete_success_ouput", className="alert alert-danger text-white",
                        style={"text-align": "center", "vertical-align": "text-top", "padding": "10px"})
