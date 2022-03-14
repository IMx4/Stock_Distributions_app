
import dash
from dash import html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
from data_api import Data_Api
from plots import Plots
from download_modal import download_modal, confirmation, failed
from manage_data_modal import manage_data_modal, confirm_delete, delete_failed
from header import header
from plot_row import plot_row
from button_row import button_row
from footer_row import footer_row


# data api to retreive stock data
api = Data_Api()

# get list of available csv files in current dir
csv_files = api.csv_list()

# add theming and scaling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

""" 
app layout
- contains all hmtml elements that are rendered to page
---------------------------------------------------------------------------------------------
"""
app.layout = dbc.Container([

    header,
    plot_row,
    button_row,
    footer_row,
    download_modal,
    manage_data_modal

], fluid=True)


"""
callbacks
- Callback and functions to control page state
-------------------------------------------------------------------------------------------
"""

############# time series plot ################


@app.callback(
    Output('series_fig', 'figure'),
    [Input('file_dropdwn', 'value'),
     Input('stock-radios', 'value')]
)
def update_graph(symbol, column):
    if len(symbol) > 0 and symbol != 'Download Data':
        df = api.load_csv(symbol)
        figln = px.line(df, x='Date', y=column)

        return figln
    return {}

############# distribution plot ###############


@app.callback(
    [Output("dist_fig", "figure"),
     Output("parameters1", "children"),
     Output("parameters2", "children"),
     Output("parameters3", "children"),
     Output("parameters4", "children")],
    Input("distribution", "value"),
    Input("file_dropdwn", "value")
)
def update_graph2(distribution, symbol):

    if len(symbol) > 0 and symbol != 'Download Data':
        df = api.load_csv(symbol)
        plot = Plots(distribution, df)
        return plot.fig, f'{plot.mu:.4f}', f'{plot.beta:.4f}', f'{plot.bic:.4f}', f'{plot.aic:.4f}'

    return {}, dash.no_update, dash.no_update, dash.no_update, dash.no_update

############# download modal ##################


@app.callback(
    Output("data_api_modal", "is_open"),
    [Input("download_data", "n_clicks"),
     Input("close_modal", "n_clicks")],
    [State("data_api_modal", "is_open")],
)
def toggle_data_api_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

########## download data submit button #############


@app.callback(
    [Output("file_dropdwn", "options"),
     Output("ticker_id", "value"),
     Output("spinner_out", "children")],
    [Input("ticker_submit", "n_clicks"),
     Input("close_modal", "n_clicks"),
     Input("ticker_id", "value")],
    State("radios", "value"),
    prevent_initial_call=True
)
def download_data(submit_clicks, close_clicks, ticker, date_range):

    ctx = dash.callback_context
    callback_id = ctx.triggered[0]['prop_id'].split('.')[0]
    global csv_files
    csv_files = api.csv_list()

    # if modal close button is pressed
    if callback_id == 'close':
        return dash.no_update, dash.no_update, dash.no_update

    # if modal submit button is pressed
    if callback_id == 'ticker_submit':
        data, symbol = api.pull_ticker_data(ticker, date_range)
        success = api.write_csv(data, symbol)
        if success:
            c = confirmation
            c.children = f'{ticker} Saved...'
            return(csv_files, '', c)
        else:
            f = failed
            f.children = f'{ticker} not found ...'
            return (csv_files, '', f)

    if callback_id == 'ticker_id':
        if ticker == '':
            return (csv_files, ticker, '')

    return (csv_files, ticker, '')

############# manage data modal ##################


@app.callback(
    Output('manage_data_modal', 'is_open'),
    [Input('manage_data', 'n_clicks'),
     Input('close_modal2', 'n_clicks')],
    [State('manage_data_modal', 'is_open')],
)
def toggle_data_api_modal(n1, n2, is_open):

    if n1 or n2:
        return not is_open
    return is_open

############## manage data delete button ###########


@app.callback(
    [Output('delete-success-div', 'children'),
     Output('delete_file', 'n_clicks'),
     Output('manage_data_dropdwn', 'options'),
     Output('manage_data_dropdwn', 'value')],
    [Input('delete_file', 'n_clicks'),
     Input('manage_data_modal', 'is_open'),
     Input('manage_data_dropdwn', 'value')],
    prevent_initial_call=True
)
def delete_success(clicks, is_open, file_name):
    if is_open:
        if clicks > 0 and (file_name != 'Download Data' or file_name != ''):
            success = api.remove_csv(file_name)
            if success:
                s = confirm_delete
                s.children = f'Removed - {file_name}'
                return (s, 0, api.csv_list(), '')
            else:
                f = delete_failed
                f.children = f'{file_name} not found'
                return (f, 0, dash.no_update, '')

    return ('', clicks, api.csv_list(), file_name)


############# top 3 BIC list ###############
@app.callback(
    [Output("top_3_bic", "children"),
     Output("top_3_aic", "children")],
    Input("file_dropdwn", "value")
)
def top3(symbol):

    if len(symbol) > 0 and symbol != 'Download Data':

        df = api.load_csv(symbol)
        bic_top_3, aic_top_3 = Plots.top_3_fits(df)
        bic_data = [html.Li(f'{key}: {fit:.4f}') for key, fit in bic_top_3]
        aic_data = [html.Li(f'{key}: {fit:.4f}') for key, fit in aic_top_3]

        return bic_data, aic_data

    return ''


if __name__ == '__main__':
    app.run_server(debug=False)
