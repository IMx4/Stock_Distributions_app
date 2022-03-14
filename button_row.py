from dash import html
import dash_bootstrap_components as dbc

"""
composes a row with two cols
col 1 - buttons for time series data, download, and manage
col 2 - top 3 data
"""
button_row = dbc.Row([
    dbc.Col([
        html.Div([
            html.Div([
                dbc.RadioItems(
                    id="stock-radios",
                    class_name="btn-group d-flex flex-row justify-content-around",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Open", "value": "Open"},
                        {"label": "High", "value": "High"},
                        {"label": "Low", "value": "Low"},
                        {"label": "Close", "value": "Close"},
                        {"label": "Volume", "value": "Volume"},
                    ],
                    value="Close",
                ),
            ], id="stock-col-div"),
            html.Div([
                dbc.Button("Download Data", id="download_data",
                           color="primary", className="me-1 m-3"),
                dbc.Button("Manage Data", id="manage_data",
                           color="primary", className="me-1 m-3"),
            ], id="modal-button-div")
        ], id="button-div")
    ], xs=12, sm=12, md=12, lg=5, xl=5),

    dbc.Col([
        html.Div([
            html.Div([
                html.Div([html.H6("LOC :", className="label", id="loc"), html.H6(
                    "", id="parameters1", className="param-val")]),
                html.Div([html.H6("SCALE :", className="label", id="scale"), html.H6(
                    "", id="parameters2", className="param-val")]),
                html.Div([html.H6("BIC :", className="label", id="bic"), html.H6(
                    "", id="parameters3", className="param-val")]),
                html.Div([html.H6("AIC :", className="label", id="aic"), html.H6(
                    "", id="parameters4", className="param-val")]),
            ], id="params1"),

            html.Div([
                html.Div([
                    html.H5("Top 3 BIC Scores", style={
                            "padding-left": "1rem"}),
                    html.Ol(id="top_3_bic", children=''),
                ], id="bic-div", style={"float": "left"}),
                html.Div([
                    html.H5("Top 3 AIC Scores", style={
                            "padding-left": "1rem"}),
                    html.Ol(id="top_3_aic", children=''),
                ], id="aic-div", style={"float": "right"}),
            ], id="params2")
        ], id="parameter-div")
    ], xs=12, sm=12, md=12, lg=5, xl=5),

    ################# Popovers for data abbreviations ###################
    dbc.Popover(
        [
            dbc.PopoverHeader("Location"),
            dbc.PopoverBody(
                "Measure of central tendency (measure varies by distribution)"),
        ],
        target="loc",
        trigger="hover",
        hide_arrow=True,
    ),
    dbc.Popover(
        [
            dbc.PopoverHeader("Scale"),
            dbc.PopoverBody(
                "Measure of dispersion (measures varies by distribution)"),
        ],
        target="scale",
        trigger="hover",
        hide_arrow=True,
    ),
    dbc.Popover(
        [
            dbc.PopoverHeader("Bayesian Information Criterion"),
            dbc.PopoverBody(
                "Measures the goodness of fit of empirical and theoretical distribution while punishing model complexity."),
        ],
        target="bic",
        trigger="hover",
        hide_arrow=True,
    ),
    dbc.Popover(
        [
            dbc.PopoverHeader("Akaike Information Criterion"),
            dbc.PopoverBody(
                "Measures the goodness of fit of empirical and theoretical distribution while punishing model complexity."),
        ],
        target="aic",
        trigger="hover",
        hide_arrow=True,
    ),

], justify='center')
