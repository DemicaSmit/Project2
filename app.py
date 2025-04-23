# app.py
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.CYBORG])
server = app.server

sidebar = dbc.Nav(
    [
        dbc.NavLink("Overview", href="/", active="exact"),
        dbc.NavLink("Predict", href="/predict", active="exact"),
        dbc.NavLink("Dataset", href="/dataset", active="exact"),
        dbc.NavLink("Analysis", href="/analysis", active="exact"),
    ],
    vertical=True,
    pills=True,
    
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(sidebar, width=2, className="sidebar-col"),
        dbc.Col(dash.page_container, width=10)
    ])
], fluid=True, className="g-0")


if __name__ == "__main__":
    app.run(debug=True)
