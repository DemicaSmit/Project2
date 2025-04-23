import dash
from dash import html, dcc, dash_table
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np

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
                {"name": "Accuracy", "id": "Accuracy"},
                {"name": "Precision", "id": "Precision"},
                {"name": "Recall", "id": "Recall"},
                {"name": "F1 Score", "id": "F1 Score"},
            ],
            data=[
                {"Model": "Logistic Regression", "Accuracy": 0.89, "Precision": 0.87, "Recall": 0.88, "F1 Score": 0.875},
                {"Model": "Random Forest", "Accuracy": 0.93, "Precision": 0.94, "Recall": 0.92, "F1 Score": 0.93},
                {"Model": "SVM", "Accuracy": 0.91, "Precision": 0.90, "Recall": 0.91, "F1 Score": 0.905},
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

    # Bar Chart Comparison
    html.Div([
        html.H3("📈 Visual Comparison (Accuracy & F1 Score)", style={"color": "#ecf0f1", "marginBottom": "20px"}),

        dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Bar(
                        name="Accuracy",
                        x=["LogReg", "Random Forest", "SVM"],
                        y=[0.89, 0.93, 0.91],
                        marker_color="#2980b9"
                    ),
                    go.Bar(
                        name="F1 Score",
                        x=["LogReg", "Random Forest", "SVM"],
                        y=[0.875, 0.93, 0.905],
                        marker_color="#27ae60"
                    )
                ],
                layout=go.Layout(
                    barmode="group",
                    title="Model Performance Comparison",
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
        html.H3("🧠 Confusion Matrix (Random Forest)", style={"color": "#ecf0f1", "marginBottom": "20px"}),

        dcc.Graph(
            figure=ff.create_annotated_heatmap(
                z=np.array([[90, 10], [5, 95]]),
                x=["Predicted Negative", "Predicted Positive"],
                y=["Actual Negative", "Actual Positive"],
                colorscale="Blues",
                showscale=True
            )
        )
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
