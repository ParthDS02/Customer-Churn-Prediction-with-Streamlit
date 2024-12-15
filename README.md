# Customer Churn Prediction with Streamlit

## Overview
Customer churn prediction is a vital tool for businesses to identify customers likely to leave their service. In this project, I build a machine learning pipeline to predict customer churn, integrating data analysis, feature engineering, modeling, and Demonstrate as a Streamlit web application.

### Project Highlights:
- **Dataset Exploration**: Analyzed key patterns and trends in customer behavior.
- **Data Cleaning and Feature Engineering**: Prepared the data for accurate model training.
- **Model Training and Evaluation**: Tested five models, achieving up to **91.5% accuracy**.
- **Interactive Web Application**: Created a user-friendly app with Streamlit for real-time churn predictions.

## Tools and Technologies
- **Language**: Python (v3.11.5)
- **IDE**: Visual Studio Code
- **Libraries**:
  - **Data Manipulation**: Pandas, NumPy
  - **Visualization**: Matplotlib
  - **Machine Learning**: Scikit-learn
  - **App Development**: Streamlit
  - **Model Persistence**: Joblib

## Project Workflow
### 1. Dataset Exploration
- Loaded and analyzed the dataset, focusing on the target variable (**churn**).

### 2. Data Cleaning
- Handled missing values and duplicates to ensure data integrity.

### 3. Data Visualization
- Created visualizations like pie charts and histograms to understand key trends.

### 4. Feature Engineering
- Encoded categorical variables for machine learning models.

### 5. Model Training and Evaluation
| Model                    | Accuracy (%) |
|--------------------------|--------------|
| Logistic Regression      | **91.50**    |
| K-Nearest Neighbors      | 91.00        |
| Support Vector Classifier| 91.00        |
| Decision Tree            | 85.00        |
| Random Forest Classifier | 89.00        |

### 6. Streamlit App Creation
- Built an interactive app for churn predictions.

### 7. Demostration
- Demostration the app locally.

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/churn-prediction.git
   cd churn-prediction
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser to input customer data and receive predictions.

## Directory Structure
```
churn-prediction/
|-- data/                # Contains the dataset
|-- notebooks/           # Jupyter Notebooks for EDA and model training
|-- app.py               # Streamlit application
|-- models/              # Saved ML models and scaler using Joblib
|-- README.md            # Project documentation (this file)
```

## Screenshots
Include screenshots of:
- Data visualizations (pie chart, Bar chart, histogram)
- Streamlit app interface (input form, prediction result)
  
### Data Visualization Example
![Pie Chart](https://github.com/user-attachments/assets/3783d1d0-bf8a-4e8f-b0ce-86304fbeaa01)
![Bar Chart](https://github.com/user-attachments/assets/6bd0c243-1d3e-4d58-9692-fae05c86796f)
![Histogram 1](https://github.com/user-attachments/assets/9ecd46ce-ebcd-4603-8f99-06f08fce3751)
![Histogram 2](https://github.com/user-attachments/assets/bfda5628-ba8d-4c29-a5fb-795e57484221)

### App Interface
![Streamlit App](https://github.com/user-attachments/assets/316459d6-f250-4144-af3f-f8c0c9497baa)

## Key Takeaways
- Logistic Regression performed the best with **91.5% accuracy**.
- The Streamlit app offers an intuitive way to leverage machine learning for business insights.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Feel free to fork the repository and submit a pull request to suggest improvements.

## Future Enhancements
- Deploy the app on a cloud platform like AWS or Azure.
- Incorporate additional features to improve model accuracy.
