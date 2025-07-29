from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# Load model and scaler
model = joblib.load("linear_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

# Load real user data from CSV
df = pd.read_csv("Electricity_Usage_by_Month.csv")
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June',
          'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a dictionary of user data from the CSV
user_data = {}
for _, row in df.iterrows():
    user_id = row['UserID']
    user_data[user_id] = [row[month] for month in months]

# List of months for the dropdown (with full names)
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    total_prediction = None
    user_usage = None
    available_users = list(user_data.keys())

    if request.method == "POST":
        user_id = request.form["user_id"]
        month = request.form["month"]

        try:
            if user_id not in user_data:
                raise ValueError(f"User ID not found. Available users: {', '.join(available_users[:10])}...")

            month_index = month_names.index(month)  # 0-based index
            user_usage_data = user_data[user_id]

            # Show current month's usage
            user_usage = user_usage_data[month_index]

            # Build input vector for the model (12 months)
            input_vector = user_usage_data.copy()
            scaled_input = scaler.transform([input_vector])
            predicted_total = model.predict(scaled_input)[0]

            # Calculate prediction for the specific month (proportional to current usage)
            current_month_usage = user_usage_data[month_index]
            total_current_usage = sum(user_usage_data)
            prediction = (current_month_usage / total_current_usage) * predicted_total if total_current_usage > 0 else 0
            total_prediction = predicted_total

        except Exception as e:
            return render_template("index.html", 
                                   months=month_names, 
                                   available_users=available_users,
                                   error=str(e))

    return render_template("index.html", 
                           months=month_names,
                           available_users=available_users,
                           prediction=prediction,
                           total_prediction=total_prediction,
                           user_usage=user_usage)

@app.route("/provider", methods=["GET", "POST"])
def provider_dashboard():
    total_expenses = None
    user_count = None
    avg_usage = None
    peak_usage = None
    low_usage = None
    month_prediction = None
    cost_breakdown = None
    
    if request.method == "POST":
        try:
            # Get the month for prediction
            month = request.form.get("month", "January")
            month_index = month_names.index(month)
            
            # Calculate predictions for all users
            total_predicted_usage = 0
            user_predictions = []
            
            for user_id, user_usage_data in user_data.items():
                # Predict total annual usage for this user
                input_vector = user_usage_data.copy()
                scaled_input = scaler.transform([input_vector])
                predicted_total = model.predict(scaled_input)[0]
                
                # Calculate prediction for the specific month
                current_month_usage = user_usage_data[month_index]
                total_current_usage = sum(user_usage_data)
                month_prediction_user = (current_month_usage / total_current_usage) * predicted_total if total_current_usage > 0 else 0
                
                total_predicted_usage += month_prediction_user
                user_predictions.append({
                    'user_id': user_id,
                    'predicted_usage': month_prediction_user,
                    'current_usage': current_month_usage
                })
            
            # Calculate statistics
            user_count = len(user_data)
            avg_usage = total_predicted_usage / user_count if user_count > 0 else 0
            
            # Find peak and low usage users
            user_predictions.sort(key=lambda x: x['predicted_usage'], reverse=True)
            peak_usage = user_predictions[0] if user_predictions else None
            low_usage = user_predictions[-1] if user_predictions else None
            
            # Calculate total expenses (assuming $0.12 per kWh = $0.00012 per watt)
            # Convert watts to kWh (assuming 24 hours per day, 30 days per month)
            watts_to_kwh = total_predicted_usage * 24 * 30 / 1000  # Convert to kWh
            total_expenses = watts_to_kwh * 0.12  # $0.12 per kWh
            
            # Cost breakdown
            cost_breakdown = {
                'total_kwh': watts_to_kwh,
                'rate_per_kwh': 0.12,
                'total_cost': total_expenses,
                'avg_cost_per_user': total_expenses / user_count if user_count > 0 else 0
            }
            
            month_prediction = month
            
        except Exception as e:
            return render_template("provider.html", 
                                   months=month_names,
                                   error=str(e))
    
    return render_template("provider.html", 
                           months=month_names,
                           total_expenses=total_expenses,
                           user_count=user_count,
                           avg_usage=avg_usage,
                           peak_usage=peak_usage,
                           low_usage=low_usage,
                           month_prediction=month_prediction,
                           cost_breakdown=cost_breakdown)

if __name__ == "__main__":
    app.run(debug=True)
