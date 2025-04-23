import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

dash.register_page(__name__, path="/")


fig_pie = px.pie(values=[9, 7, 8], names=["Linear Regression", "Random Forest", "SVR"], title="Model Distribution by MAE")
fig_pie.update_layout(
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    title_font_size=20
)


np.random.seed(42)
y_actual = np.linspace(50, 150, 24) + np.random.normal(0, 3, 24)
y_rf = y_actual + np.random.normal(0, 5, 24)
y_svr = y_actual + np.random.normal(0, 7, 24)

# 📌 New: Create scatter plot comparing Random Forest vs SVR
fig_pred_vs_actual = go.Figure()
fig_pred_vs_actual.add_trace(go.Scatter(x=y_actual, y=y_rf, mode='markers', name='Random Forest',
                                        marker=dict(symbol='circle', color='lightblue')))
fig_pred_vs_actual.add_trace(go.Scatter(x=y_actual, y=y_svr, mode='markers', name='SVR',
                                        marker=dict(symbol='square', color='orange')))
fig_pred_vs_actual.add_trace(go.Scatter(x=[y_actual.min(), y_actual.max()], y=[y_actual.min(), y_actual.max()],
                                        mode='lines', name='Ideal Prediction', line=dict(dash='dash', color='red')))

fig_pred_vs_actual.update_layout(
    title="Predicted vs Actual Quantity: RF vs SVR",
    xaxis_title="Actual Quantity",
    yaxis_title="Predicted Quantity",
    plot_bgcolor="#1e1e1e",
    paper_bgcolor="#1e1e1e",
    font=dict(color="white"),
    title_font_size=20
)

# 📌 Model Metrics Data
model_data = [
    {"Model": "Linear Regression", "Train RMSE (Std)": 1.090459, "Test RMSE (Std)": 0.323869, "Train MAE (Std)": 0.344243, "Test MAE (Std)": 0.265627, "Train RMSE (Orig)": 40.301383, "Test RMSE (Orig)": 11.969612, "Train MAE (Orig)": 12.722603, "Test MAE (Orig)": 9.817092, "Train R²": 0.035341, "Test R²": -0.442537, "CV R² (Mean)": -0.617647, "CV R² (Std)": 0.802494},
    {"Model": "Random Forest", "Train RMSE (Std)": 0.623627, "Test RMSE (Std)": 0.376353, "Train MAE (Std)": 0.176098, "Test MAE (Std)": 0.213419, "Train RMSE (Orig)": 23.048114, "Test RMSE (Orig)": 13.909331, "Train MAE (Orig)": 6.508273, "Test MAE (Orig)": 7.887590, "Train R²": 0.684496, "Test R²": -0.947956, "CV R² (Mean)": -9.654443, "CV R² (Std)": 25.018885},
    {"Model": "SVR", "Train RMSE (Std)": 1.114505, "Test RMSE (Std)": 0.275670, "Train MAE (Std)": 0.322586, "Test MAE (Std)": 0.232769, "Train RMSE (Orig)": 41.190088, "Test RMSE (Orig)": 10.188251, "Train MAE (Orig)": 11.922179, "Test MAE (Orig)": 8.602729, "Train R²": -0.007672, "Test R²": -0.045120, "CV R² (Mean)": None, "CV R² (Std)": None}
]

# Convert to DataFrame
df_model_metrics = pd.DataFrame(model_data)

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
                html.H4("Support Vector Regression", className="card-title"),
                html.H2(f"Train RMSE: {df_model_metrics.loc[2, 'Train RMSE (Std)']:.2f}", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Linear Regression", className="card-title"),
                html.H2(f"Train RMSE: {df_model_metrics.loc[0, 'Train RMSE (Std)']:.2f}", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H4("Random Forest", className="card-title"),
                html.H2(f"Train RMSE: {df_model_metrics.loc[1, 'Train RMSE (Std)']:.2f}", className="card-text")
            ])
        ], className="shadow-sm", style={"backgroundColor": "#34495e", "color": "white", "borderRadius": "12px"}), width=4),
    ], className="mb-4"),

     # 📌 New Graph Section
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_pred_vs_actual), width=6),
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
                        href="/assets/Project_Report.pdf",
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
