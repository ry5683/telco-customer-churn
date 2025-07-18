# 📦 Telco Customer Churn Prediction – ML to API Pipeline

## 🔍 Overview
This end-to-end project predicts customer churn for a telecom provider using a real-world dataset. The pipeline spans data cleaning, feature engineering, model comparison, and deployment via a Flask API. It demonstrates practical ML implementation with business impact and production-readiness in mind.

---

## 🎯 Objective
Predict which customers are at risk of cancelling service. This allows the business to proactively retain users through strategic outreach and incentives.

---

## 🧰 Tech Stack
- **Languages:** Python
- **ML Libraries:** scikit-learn, XGBoost, TensorFlow
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Flask
- **Testing:** requests
- **Environment:** Conda

---

## 📊 Dataset
- **Source:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Size:** 7,043 rows × 21 columns
- **Target:** `Churn` (binary classification)

---

## 🧪 Workflow Summary

1. **EDA**
   - Identified churn drivers: `tenure`, `MonthlyCharges`, `InternetService`, `TechSupport`.
   - Observed class imbalance: ~27% of customers churned.

2. **Preprocessing**
   - Cleaned missing data (`TotalCharges`)
   - One-hot encoded categorical features
   - Feature scaling via `StandardScaler`

3. **Modeling**
   - Compared 5 models:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - XGBoost
     - Neural Network (TensorFlow)
   - **Metric Used:** F1-Score for class `Churn = Yes`

4. **Deployment**
   - Best model serialized with `joblib`
   - Exposed via REST API using Flask
   - Includes `test_api.py` for endpoint verification

---

## 🧠 Results

| Model                        | F1-Score (Churn = Yes) |
|-----------------------------|------------------------|
| **Logistic Regression**     | **0.56**               |
| Decision Tree               | 0.50                   |
| Random Forest               | 0.53                   |
| XGBoost                     | 0.54                   |
| Neural Net (TensorFlow)     | 0.56                   |

---

## 💡 Business Insights
- Customers with **fiber optic internet** and **no tech support** churn more often.
- Short tenure and high monthly charges are strong churn predictors.
- The model helps identify at-risk segments for targeted retention offers.

---

## 🚀 How to Run the Project

### 1. Setup Environment
```bash
conda create -n ml-env python=3.11
conda activate ml-env
pip install pandas scikit-learn matplotlib xgboost tensorflow flask requests
```

### 2. Run Flask API
```bash
# From project root
python app.py
```

### 3. Test API Endpoint
```bash
# In a second terminal
python test_api.py
```

---

## 🔌 API Usage

**Endpoint:** `POST /predict`  
**Payload Format:**
```json
{
  "tenure": 2,
  "MonthlyCharges": 70.70,
  "TotalCharges": 151.65,
  "InternetService_Fiber optic": 1,
  "PaymentMethod_Electronic check": 1
}
```

**Response:**
```json
{"prediction": 1}
```
(1 = Churn, 0 = No Churn)

---

## 🧠 What I Learned
- Building and comparing multiple ML models on a real business problem
- Managing class imbalance and scaling
- Creating and deploying a Flask-based API for live predictions
- Turning a data science model into a production-ready microservice

---

## 🛠️ Future Improvements
- Add FastAPI version with input validation
- Include unit tests and CI/CD pipeline via GitHub Actions
- Deploy live on Render or EC2 and attach demo link
