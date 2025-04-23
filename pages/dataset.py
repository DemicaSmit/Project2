import dash
from dash import html, dcc, dash_table
import pandas as pd

# Try reading the Excel file
try:
    df = pd.read_excel("DataSet.xlsx")
except Exception as e:
    print(f"Error reading the Excel file: {e}")
    df = pd.DataFrame()  # Return an empty DataFrame if there's an error

# Now check if DataFrame is empty
if df.empty:
    print("Dataset is empty or failed to load. Please check the Excel file.")
else:
    layout = html.Div([
        html.H1("📊 Dataset Viewer", style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'marginBottom': '30px',
            'fontWeight': 'bold'
        }),

        html.Div([
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in df.columns],
                page_size=15,
                style_table={
                    'height': '500px',
                    'overflowY': 'auto',
                    'width': '100%',
                    'border': '1px solid #444',
                    'borderRadius': '10px',
                    'boxShadow': '0 4px 15px rgba(0, 0, 0, 0.3)',
                    'backgroundColor': '#1a1a1a',
                    'marginBottom': '20px'
                },
                style_cell={
                    'textAlign': 'center',
                    'padding': '10px',
                    'border': '1px solid #333',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '14px',
                    'backgroundColor': '#1a1a1a',
                    'color': '#ecf0f1'
                },
                style_header={
                    'backgroundColor': 'white',
                    'color': 'black',
                    'fontWeight': 'bold',
                    'textAlign': 'center',
                    'padding': '10px',
                    'border': 'none'
                },
                style_data_conditional=[
                    {
                        'if': {'state': 'active'},
                        'backgroundColor': '#2f3640',
                        'color': '#f1c40f'
                    },
                    {
                        'if': {'state': 'selected'},
                        'backgroundColor': '#2980b9',
                        'color': 'white'
                    }
                ],
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Feature1'},
                        'textAlign': 'left'
                    },
                    {
                        'if': {'column_id': 'Feature2'},
                        'textAlign': 'left'
                    },
                    {
                        'if': {'column_id': 'Feature3'},
                        'textAlign': 'left'
                    },
                    {
                        'if': {'column_id': 'Label'},
                        'textAlign': 'center'
                    }
                ]
            ),
        ], style={
            'maxWidth': '90%',
            'margin': '0 auto',
            'padding': '20px',
            'boxShadow': '0px 4px 15px rgba(0, 0, 0, 0.3)',
            'borderRadius': '10px',
            'backgroundColor': '#2f3640',
            'textAlign': 'center'
        })
    ], style={
        'backgroundColor': '#1a1a1a',
        'minHeight': '100vh',
        'padding': '40px'
    })

dash.register_page(__name__, path="/dataset")
