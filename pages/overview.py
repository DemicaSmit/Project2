import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/")

# Sample data and graphs
sample_data = pd.DataFrame({
    "x": pd.date_range(start='1/1/2023', periods=24, freq='h'),
    "y": (100 + (pd.Series(range(24)) * 5).values)
})

fig_energy = px.line(sample_data, x='x', y='y', title='XXX')
fig_energy.update_layout(
    plot_bgcolor="#1e1e1e",
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    title_font_size=20
)

fig_pie = px.pie(values=[40, 30, 30], names=["xxx", "xx", "x"], title="XXX")
fig_pie.update_layout(
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    title_font_size=20
)

# Layout
layout = html.Div([
    html.H1("🔍 Dashboard Overview", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '40px',
        'fontWeight': 'bold'
    }),

    # Metrics Cards
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("⚡ xxx", className="card-title"),
                html.H2("xxx", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("🌍 xxx", className="card-title"),
                html.H2("xxx", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("xxx", className="card-title"),
                html.H2("xxx", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),
    ], className="mb-4"),

    # Graphs Section
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_energy), width=6),
        dbc.Col(dcc.Graph(figure=fig_pie), width=6)
    ], className="mb-5"),

    # Download Report
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H5("📄 Download Report", className="text-center", style={"color": "#ecf0f1", "marginBottom": "10px"}),
                html.Div([
                    html.A(
                        html.Button("Download PDF Report", className="btn btn-success btn-lg"),
                        href="/assets/sample_report.txt",
                        download="Report.pdf"
                    )
                ], className="d-flex justify-content-center")
            ], style={
                "backgroundColor": "#2c3e50",
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0px 4px 12px rgba(0,0,0,0.4)"
            })
        ], width=12)
    ])
], className="p-4", style={"backgroundColor": "#1a1a1a", "minHeight": "100vh"})
