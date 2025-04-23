import dash
from dash import html, dcc, Input, Output, State, callback
import joblib
import numpy as np

# Load models and scaler
models = {
    "SVM": joblib.load("artifacts/SVR.pkl"),
    "Random Forest": joblib.load("artifacts/Random_Forest.pkl"),
    "Logistic Regression": joblib.load("artifacts/Linear_Regression.pkl"),
}
scaler = joblib.load("artifacts/scaler.pkl")  # expects 2 features: UnitPrice, Quantity

# Styles
container_style = {
    'maxWidth': '500px',
    'margin': '0 auto',
    'padding': '40px',
    'boxShadow': '0px 4px 20px rgba(0,0,0,0.5)',
    'borderRadius': '10px',
    'backgroundColor': '#2f3640'
}
input_style = {
    'marginBottom': '10px',
    'padding': '10px',
    'width': '100%',
    'borderRadius': '5px',
    'border': '1px solid #555',
    'backgroundColor': '#1a1a1a',
    'color': 'white'
}
predict_button_style = {
    'backgroundColor': '#3498db',
    'color': 'white',
    'border': 'none',
    'padding': '10px 20px',
    'borderRadius': '5px',
    'cursor': 'pointer',
    'fontWeight': 'bold'
}

# Layout
layout = html.Div([    
    html.H1("🔍 Make a Prediction", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '30px',
        'fontWeight': 'bold'
    }),

    html.Div([
        html.Label("Choose a Model", style={
            'fontWeight': 'bold',
            'color': '#ecf0f1',
            'marginBottom': '10px',
            'display': 'block'
        }),
        dcc.Dropdown(
            id='model_choice',
            options=[{'label': k, 'value': k} for k in models.keys()],
            placeholder="Select a Machine Learning Model",
            className='dark-dropdown',
            style={'marginBottom': '20px'}
        ),

        html.Div(id='input_fields', style={'marginBottom': '20px'}),

        html.Button("Predict", id="predict_btn", n_clicks=0,
                    style={**predict_button_style, 'opacity': 0.5, 'cursor': 'not-allowed'},
                    disabled=True),

        html.Div(id='prediction_result', style={
            'marginTop': '30px',
            'fontSize': '20px',
            'fontWeight': 'bold',
            'color': '#2ecc71',
            'textAlign': 'center'
        }),
    ], style=container_style)
], style={
    'backgroundColor': '#1a1a1a',
    'minHeight': '100vh',
    'padding': '40px'
})

# Update inputs based on model choice
@callback(
    Output('input_fields', 'children'),
    Input('model_choice', 'value')
)
def update_inputs(model_name):
    if not model_name:
        return ""
    
    # Adjusted input fields based on new inputs
    fields = ['ProductCode', 'UnitPrice', 'Hour', 'DayOfWeek', 'CountryCode']
    return [
        dcc.Input(
            id=f'input_{i}',
            type='number',
            placeholder=f'{field}',
            style=input_style
        ) for i, field in enumerate(fields)
    ]

# Enable/Disable Predict button
@callback(
    Output('predict_btn', 'disabled'),
    Output('predict_btn', 'style'),
    Input('model_choice', 'value')
)
def toggle_predict_button(model_name):
    if model_name:
        return False, {**predict_button_style, 'opacity': 1, 'cursor': 'pointer'}
    else:
        return True, {**predict_button_style, 'opacity': 0.5, 'cursor': 'not-allowed'}

# Make prediction
@callback(
    Output('prediction_result', 'children'),
    Input('predict_btn', 'n_clicks'),
    State('model_choice', 'value'),
    State('input_0', 'value'),  # ProductCode
    State('input_1', 'value'),  # UnitPrice
    State('input_2', 'value'),  # Hour
    State('input_3', 'value'),  # DayOfWeek
    State('input_4', 'value'),  # CountryCode
    prevent_initial_call=True
)
def make_prediction(n_clicks, model_name, f0, f1, f2, f3, f4):
    if None in [f0, f1, f2, f3, f4]:
        return "⚠️ Please fill in all fields."

    try:
        # Features to be passed to the model
        features = np.array([[f0, f1, f2, f3, f4]])

        # Scale UnitPrice (index 1) and CountryCode (index 4)
        # Ensure that you pass both features to the scaler as expected
        scaled_vals = scaler.transform([[f1, f4]])[0]  # Transform UnitPrice and CountryCode
        features[0][1] = scaled_vals[0]  # scaled UnitPrice
        features[0][4] = scaled_vals[1]  # scaled CountryCode

        # Make prediction
        model = models[model_name]
        prediction = model.predict(features)

        # Multiply prediction by 3 and ensure it's positive
        predicted_quantity = prediction[0] * 10
        if predicted_quantity < 0:
            predicted_quantity = abs(predicted_quantity)

        # Return the result as "Quantity Needed"
        return f"✅ Quantity Needed: {predicted_quantity:.2f} units."

    except Exception as e:
        return f"❌ Error: {str(e)}"



# Register page
dash.register_page(__name__, path="/predict")
