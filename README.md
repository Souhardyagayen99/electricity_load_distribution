# ⚡ Electricity Load Distribution & Prediction System

A comprehensive machine learning-based web application for predicting electricity usage and load forecasting for both individual users and electricity providers.

## 🚀 Features

### 👤 Individual User Predictions
- **Real-time Predictions**: Predict electricity usage for any user and month
- **Historical Data Analysis**: Uses actual user consumption patterns from CSV data
- **Machine Learning Model**: Powered by trained linear regression model
- **User-friendly Interface**: Dropdown selection for 99 users (M101-M199)

### 🏢 Provider Dashboard
- **Load Forecasting**: Predict total electricity expenses for all users
- **Cost Analysis**: Detailed breakdown of kWh consumption and costs
- **Peak Usage Identification**: Identify high and low consumption users
- **Revenue Forecasting**: Financial planning and resource allocation
- **Professional Analytics**: Comprehensive insights for electricity providers

## 📊 Key Capabilities

- **Real Data Integration**: Uses actual electricity usage data from CSV files
- **Machine Learning Predictions**: Linear regression model for accurate forecasting
- **Cost Calculation**: Automatic conversion from watts to kWh with pricing
- **Responsive Design**: Modern, professional UI that works on all devices
- **Error Handling**: Robust error management and user feedback

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Linear Regression)
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Model Persistence**: Joblib for model serialization

## 📁 Project Structure

```
electricity_load_distribution/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── linear_regression_model.pkl     # Trained ML model
├── scaler.pkl                      # Data scaler for preprocessing
├── Electricity_Usage_by_Month.csv  # Real user data (99 users)
├── Electricity_Usage_by_Month.xlsx # Excel version of data
├── model_train.ipynb              # Model training notebook
├── model_train_xlsx.ipynb         # Alternative training notebook
├── templates/
│   ├── index.html                 # Individual user prediction page
│   └── provider.html              # Provider dashboard page
└── README.md                      # This file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Souhardyagayen99/electricity_load_distribution.git
cd electricity_load_distribution
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
- **Individual Predictions**: http://127.0.0.1:5000/
- **Provider Dashboard**: http://127.0.0.1:5000/provider

## 📖 Usage Guide

### For Individual Users
1. Navigate to the main page
2. Select a user ID from the dropdown (M101-M199)
3. Choose a month for prediction
4. Click "Predict Usage" to see results
5. View current usage, predicted usage, and annual forecast

### For Electricity Providers
1. Navigate to the Provider Dashboard
2. Select a month for load forecasting
3. Click "Predict Total Expenses"
4. Review comprehensive analytics including:
   - Total predicted expenses
   - User count and average usage
   - Peak usage identification
   - Detailed cost breakdown
   - Key insights and recommendations

## 🔧 Model Details

### Training Data
- **Dataset**: 99 users with monthly electricity usage (12 months)
- **Features**: Monthly consumption patterns (Jan-Dec)
- **Target**: Total annual electricity usage
- **Model**: Linear Regression with StandardScaler preprocessing

### Model Performance
- **Train R² Score**: 1.0000
- **Test R² Score**: 1.0000
- **Accuracy**: High accuracy for electricity usage prediction

## 💡 Business Applications

### For Individual Users
- **Bill Estimation**: Predict monthly electricity costs
- **Usage Optimization**: Understand consumption patterns
- **Budget Planning**: Plan for electricity expenses

### For Electricity Providers
- **Load Forecasting**: Plan electricity generation and distribution
- **Financial Planning**: Estimate revenue and operational costs
- **Resource Allocation**: Optimize infrastructure investments
- **Peak Demand Management**: Identify high-usage periods
- **Customer Insights**: Understand usage patterns and trends

## 📈 Key Metrics

- **Total Users**: 99 active electricity consumers
- **Data Coverage**: 12 months of historical usage
- **Prediction Accuracy**: High accuracy with R² = 1.0000
- **Cost Calculation**: $0.12 per kWh rate
- **Real-time Processing**: Instant predictions and analytics

## 🔮 Future Enhancements

- [ ] Real-time data integration
- [ ] Advanced ML models (Random Forest, Neural Networks)
- [ ] Seasonal trend analysis
- [ ] Anomaly detection
- [ ] API endpoints for external integrations
- [ ] Mobile application
- [ ] Advanced visualization (charts, graphs)
- [ ] Multi-provider support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Souhardya Gayen**
- GitHub: [@Souhardyagayen99](https://github.com/Souhardyagayen99)

## 🙏 Acknowledgments

- Scikit-learn for machine learning capabilities
- Flask for web framework
- Pandas for data processing
- Real electricity usage data for training

---

⭐ **Star this repository if you find it helpful!** 