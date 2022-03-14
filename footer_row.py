from dash import html
import dash_bootstrap_components as dbc


"""
creates the footer row
- includes link to external reference
"""
footer_row = dbc.Row(
    dbc.Col(
        html.A(children="Learn more about the distribution of stock market returns.",
               href="https://klementoninvesting.substack.com/p/the-distribution-of-stock-market",
               target="_blank"),
        id="footer", width={"size": 9}),
    justify='center')
