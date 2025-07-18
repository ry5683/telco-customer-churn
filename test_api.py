import requests

url = 'http://127.0.0.1:5000/predict'

# Sample data with feature names that now match the model's expectations
sample_data = {
    'tenure': 2,
    'MonthlyCharges': 70.70,
    'TotalCharges': 151.65,
    'InternetService_Fiber optic': 1,
    'PaymentMethod_Electronic check': 1
}

response = requests.post(url, json=sample_data)

print("API Response:")
print(response.json())