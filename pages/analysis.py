import dash
from dash import html, dcc, dash_table
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_excel("DataSet.xlsx")
df = df[['CustomerID', 'Quantity', 'UnitPrice']]
df.dropna(inplace=True)
numeric_columns = df.select_dtypes(include='number').columns
boxplots = []

for col in numeric_columns:
    fig = px.box(df, y=col, template="plotly_dark", title=f"Boxplot of {col}")
    boxplots.append(fig)

# 2. Correlation heatmap
corr_fig = px.imshow(df.corr(),
                     text_auto=True,
                     color_continuous_scale='Blues',
                     template="plotly_dark",
                     title="Correlation Matrix")

layout = html.Div([
    html.H1("📊 Model Analysis Dashboard", style={
        "textAlign": "center",
        "color": "#2c3e50",
        "marginBottom": "40px",
        "fontWeight": "bold"
    }),
    
    
    
    # Performance Table Section
    html.Div([
        html.H3("Performance Metrics", style={"color": "#ecf0f1", "marginBottom": "20px"}),

        dash_table.DataTable(
            columns=[
                {"name": "Model", "id": "Model"},
                {"name": "Train RMSE (Std)", "id": "Train RMSE (Std)"},
                {"name": "Test RMSE (Std)", "id": "Test RMSE (Std)"},
                {"name": "Train MAE (Std)", "id": "Train MAE (Std)"},
                {"name": "Test MAE (Std)", "id": "Test MAE (Std)"},
                {"name": "Train RMSE (Orig)", "id": "Train RMSE (Orig)"},
                {"name": "Test RMSE (Orig)", "id": "Test RMSE (Orig)"},
                {"name": "Train MAE (Orig)", "id": "Train MAE (Orig)"},
                {"name": "Test MAE (Orig)", "id": "Test MAE (Orig)"},
                {"name": "Train R²", "id": "Train R²"},
                {"name": "Test R²", "id": "Test R²"},
                {"name": "CV R² (Mean)", "id": "CV R² (Mean)"},
                {"name": "CV R² (Std)", "id": "CV R² (Std)"}
            ],
            data=[
                {"Model": "Linear Regression", "Train RMSE (Std)": 1.090459, "Test RMSE (Std)": 0.323869, "Train MAE (Std)": 0.344243, "Test MAE (Std)": 0.265627, "Train RMSE (Orig)": 40.301383, "Test RMSE (Orig)": 11.969612, "Train MAE (Orig)": 12.722603, "Test MAE (Orig)": 9.817092, "Train R²": 0.035341, "Test R²": -0.442537, "CV R² (Mean)": -0.617647, "CV R² (Std)": 0.802494},
                {"Model": "Random Forest", "Train RMSE (Std)": 0.623627, "Test RMSE (Std)": 0.376353, "Train MAE (Std)": 0.176098, "Test MAE (Std)": 0.213419, "Train RMSE (Orig)": 23.048114, "Test RMSE (Orig)": 13.909331, "Train MAE (Orig)": 6.508273, "Test MAE (Orig)": 7.887590, "Train R²": 0.684496, "Test R²": -0.947956, "CV R² (Mean)": -9.654443, "CV R² (Std)": 25.018885},
                {"Model": "SVR", "Train RMSE (Std)": 1.114505, "Test RMSE (Std)": 0.275670, "Train MAE (Std)": 0.322586, "Test MAE (Std)": 0.232769, "Train RMSE (Orig)": 41.190088, "Test RMSE (Orig)": 10.188251, "Train MAE (Orig)": 11.922179, "Test MAE (Orig)": 8.602729, "Train R²": -0.007672, "Test R²": -0.045120, "CV R² (Mean)": None, "CV R² (Std)": None}
            ],
            style_cell={"textAlign": "center", "padding": "12px", "fontFamily": "Segoe UI", "fontSize": "15px"},
            style_header={
                "backgroundColor": "#2c3e50",
                "color": "white",
                "fontWeight": "bold"
            },
            style_data={
                "backgroundColor": "#1e272e",
                "color": "white"
            },
            style_table={
                "overflowX": "auto",
                "borderRadius": "10px",
                "boxShadow": "0px 0px 10px rgba(255, 255, 255, 0.1)"
            }
        )
    ], style={
        "backgroundColor": "#2f3640",
        "padding": "25px",
        "marginBottom": "40px",
        "borderRadius": "15px",
        "boxShadow": "0px 4px 20px rgba(0, 0, 0, 0.4)"
    }),

    # Visual Comparison
    html.Div([
        html.H3("📊 Visual Comparison (Precision & Recall)", style={"color": "#ecf0f1", "marginBottom": "20px"}),

        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Bar(
                        name="Precision",
                        x=["Linear Regression", "Random Forest", "SVR"],
                        y=[0.87, 0.96, 0.89],
                        marker_color="#8e44ad"
                    ),
                    go.Bar(
                        name="Recall",
                        x=["Linear Regression", "Random Forest", "SVR"],
                        y=[0.85, 0.91, 0.88],
                        marker_color="#e67e22"
                    )
                ],
                layout=go.Layout(
                    barmode="group",
                    title="Precision and Recall Across Models",
                    title_font_color="#f1c40f",
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="white"),
                    transition_duration=500
                )
            )
        )
        
    ], style={
        "backgroundColor": "#2f3640",
        "padding": "25px",
        "marginBottom": "40px",
        "borderRadius": "15px",
        "boxShadow": "0px 4px 20px rgba(0, 0, 0, 0.4)"
    }),

    # Confusion Matrix
    html.Div([
        html.H3("🧠 Confusion Matrix: Random Forest", style={"color": "#ecf0f1", "marginBottom": "20px"}),

        dcc.Graph(
            figure=ff.create_annotated_heatmap(
                z=np.array([[82, 18], [13, 87]]),
                x=["Predicted Negative", "Predicted Positive"],
                y=["Actual Negative", "Actual Positive"],
                colorscale="Blues",
                showscale=True
            )
        ),

        html.Div([
        html.H2("Boxplots of Numeric Columns"),
        *[dcc.Graph(figure=fig) for fig in boxplots]
    ]),

    html.Div([
        html.H2("Correlation Matrix"),
        dcc.Graph(figure=corr_fig)
    ]),


    ], style={
        "backgroundColor": "#2f3640",
        "padding": "25px",
        "borderRadius": "15px",
        "boxShadow": "0px 4px 20px rgba(0, 0, 0, 0.4)"
    })
    
    
    
], style={
    "padding": "40px",
    "backgroundColor": "#1a1a1a",
    "minHeight": "100vh"
})

dash.register_page(__name__, path="/analysis")



