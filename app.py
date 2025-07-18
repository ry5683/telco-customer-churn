from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model, scaler, and column list
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Create DataFrame from input and reindex to match the training columns
    data_df = pd.DataFrame([data]).reindex(columns=model_columns, fill_value=0)
    
    data_scaled = scaler.transform(data_df)
    
    prediction = model.predict(data_scaled)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)