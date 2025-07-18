# End-to-End Customer Churn Prediction Project

This project is a complete machine learning workflow to predict customer churn for a telecommunications company. The process includes data cleaning, exploratory data analysis (EDA), model training, and deployment of the best-performing model as a web API using Flask.

## Project Goal
The goal of this project was to analyze a dataset of telecommunications customers and build a machine learning model capable of predicting which customers are most likely to churn (cancel their service). This provides a valuable tool for the business to proactively target at-risk customers with retention offers.

## Workflow
1.  **Exploratory Data Analysis (EDA):** Investigated the dataset to understand feature distributions and relationships with the target variable ('Churn').
2.  **Data Preprocessing:** Cleaned the data, handled missing values, and converted categorical features into a numerical format using one-hot encoding.
3.  **Model Training & Comparison:** Trained and evaluated five different classification models to find the best performer based on the F1-Score for the 'Churn' class.
4.  **Deployment:** The best-performing model (Logistic Regression) was saved and deployed as a REST API using Flask.

## Models Compared
The following models were trained and evaluated:

| Model                       | F1-Score (Churn = Yes) |
| --------------------------- | ---------------------- |
| **Logistic Regression** | **0.56** |
| Decision Tree               | 0.50                   |
| Random Forest               | 0.53                   |
| XGBoost                     | 0.54                   |
| Neural Network (TensorFlow) | 0.56                   |


## How to Run This Project
1.  **Set up the environment:**
    ```bash
    # Create and activate the conda environment
    conda create -n ml-env python=3.11
    conda activate ml-env
    # Install required packages
    pip install pandas scikit-learn matplotlib xgboost tensorflow flask requests
    ```
2.  **Run the Flask API:**
    ```bash
    # Navigate to the project directory
    cd telco-customer-churn
    # Run the server
    python app.py
    ```
3.  **Test the API:**
    In a new terminal window, run the test script:
    ```bash
    python test_api.py
    ```

## API Endpoint
The API has a single endpoint for making predictions.

* **URL:** `/predict`
* **Method:** `POST`
* **Data Payload (JSON):** A JSON object containing customer features. Only non-zero features need to be provided.
    ```json
    {
        "tenure": 2,
        "MonthlyCharges": 70.70,
        "TotalCharges": 151.65,
        "InternetService_Fiber optic": 1,
        "PaymentMethod_Electronic check": 1
    }
    ```
* **Success Response:**
    * **Code:** 200
    * **Content:** `{"prediction": 1}` (1 for Churn, 0 for No Churn)