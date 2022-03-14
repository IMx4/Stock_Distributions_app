import dash_bootstrap_components as dbc
from dash import html

"""
composes the header row
"""
header = dbc.Row(
    dbc.Col(
        html.H1("Distribution Dashboard", id="header",
                className='text-center text-primary mb-4 m-4'),
        width={"size": 10, "offset": 1}
    )
)
