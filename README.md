# House Price Prediction Using Machine Learning

## 1. Project Abstract

House Price Prediction Using Machine Learning is a machine learning project developed to predict the price of a house based on important features such as Area, Bedrooms, and Age of the house.

The project follows a complete machine learning pipeline starting from data collection and data cleaning to Exploratory Data Analysis (EDA), feature selection, train-test splitting, model training, evaluation, model comparison, and final house price prediction.

Three regression approaches are explored in this project:

1. Simple Linear Regression
2. Multiple Linear Regression
3. Polynomial Regression

The performance of the models is evaluated using important regression metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.

The project helps demonstrate how machine learning regression algorithms can be applied to real-world house price prediction problems.

## 2. Project Objective

The main objective of this project is to develop a machine learning model that can predict house prices using different house-related features.

The project also aims to:

- Understand and preprocess the house price dataset.
- Perform Exploratory Data Analysis (EDA).
- Analyze relationships between features using correlation.
- Select relevant features for prediction.
- Split the dataset into training and testing data.
- Train different regression models.
- Evaluate model performance using regression metrics.
- Compare different models.
- Predict the price of a new house.

## 3. Machine Learning Pipeline

House Price Dataset
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
EDA + Scatter Plots
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Linear Regression
        ↓
Multiple Linear Regression
        ↓
Polynomial Regression
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
House Price Prediction

## 4. Dataset

The dataset contains information about houses and their prices.

### Features

- Area — House area in square feet
- Bedrooms — Number of bedrooms
- Age — Age of the house in years

### Target

- Price — House price in ₹ Lakhs

## 5. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- VS Code

## 6. Project Structure

```text
House-Price-Prediction/
│
├── dataset/
│   └── house_prices.csv
│
├── notebooks/
│   └── house_price_analysis.ipynb
│
├── src/
│   └── train.py
│
├── models/
│
├── graphs/
│   ├── area_vs_price.png
│   ├── correlation_heatmap.png
│   └── model_comparison.png
│
└── README.md
## 7. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset and identify relationships between the input features and house price.

### 7.1 Dataset Shape

The dataset contains:

- Rows: 10
- Columns: 4

### 7.2 Missing Values

The dataset was checked for missing values.

Result:

- Area: No missing values
- Bedrooms: No missing values
- Age: No missing values
- Price: No missing values

### 7.3 Duplicate Values

The dataset was checked for duplicate rows.

Result:

- Duplicate rows: 0

### 7.4 Area vs House Price

A scatter plot was created between Area and Price.

The plot shows a strong positive relationship between house area and house price. In general, as the area of the house increases, the house price also increases.

Graph:

`graphs/area_vs_price.png`

### 7.5 Correlation Analysis

Correlation was used to understand the relationship between the numerical features.

Important correlations:

- Area and Price: 0.995892
- Bedrooms and Price: 0.965822
- Age and Price: -0.952346

Area and Price have a very strong positive correlation.

Bedrooms and Price also have a strong positive correlation.

Age and Price have a strong negative correlation, meaning that older houses tend to have lower prices in this dataset.

Graph:

`graphs/correlation_heatmap.png`
## 8. Model Training

Three regression models were considered for house price prediction.

### 8.1 Simple Linear Regression

Simple Linear Regression uses one independent feature to predict the target.

In this project:

- Input: Area
- Target: Price

### 8.2 Multiple Linear Regression

Multiple Linear Regression uses multiple independent features to predict the target.

Features used:

- Area
- Bedrooms
- Age

Target:

- Price

### 8.3 Polynomial Regression

Polynomial Regression was used to capture a non-linear relationship between Area and Price.

A polynomial degree of 2 was used.

## 9. Train-Test Split

The dataset was divided into training and testing sets.

- Training data: 80%
- Testing data: 20%
- Random state: 42

The training data is used to train the machine learning models, while the testing data is used to evaluate their performance.

## 10. Model Evaluation Metrics

The following regression metrics were used:

### MAE — Mean Absolute Error

MAE measures the average absolute difference between actual and predicted values.

Lower MAE indicates better model performance.

### MSE — Mean Squared Error

MSE calculates the average squared difference between actual and predicted values.

Lower MSE indicates better performance.

### RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

Lower RMSE indicates better performance.

### R² Score

R² Score measures how well the model explains the variation in the target variable.

A value closer to 1 indicates better performance.

## 11. Multiple Linear Regression Results

The Multiple Linear Regression model produced the following results:

- MAE: 2.2808
- MSE: 9.1494
- RMSE: 3.0248
- R² Score: 0.9949

## 12. Model Comparison

The R² scores obtained from the models are:

| Model | R² Score |
|---|---:|
| Simple Linear Regression | 0.9958 |
| Multiple Linear Regression | 0.9949 |
| Polynomial Regression | 0.9998 |

Based on this small dataset and this particular train-test split, Polynomial Regression achieved the highest R² score.

Graph:

`graphs/model_comparison.png`

> Note: The dataset contains only 10 records, so these results should not be treated as evidence of real-world performance. A larger dataset would be needed for reliable evaluation.
## 13. Final House Price Prediction

A new house was given to the trained Multiple Linear Regression model for prediction.

### Input House Details

- Area: 1800 sqft
- Bedrooms: 3
- Age: 5 years

### Predicted Price

**₹84.57 Lakhs**

## 14. Conclusion

The House Price Prediction project demonstrates how machine learning regression algorithms can be used to predict house prices.

The project covered the complete machine learning workflow:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Correlation Analysis
- Feature Selection
- Train-Test Split
- Model Training
- Model Evaluation
- Model Comparison
- House Price Prediction

Three regression approaches were explored: Simple Linear Regression, Multiple Linear Regression, and Polynomial Regression.

For the given dataset and test split, Polynomial Regression achieved the highest R² score of approximately 0.9998. Multiple Linear Regression was also able to provide accurate predictions using Area, Bedrooms, and Age.

The project provides a basic understanding of regression-based machine learning and can be improved further by using a larger real-world house price dataset.

## 15. Future Enhancements

The project can be improved in the future by:

- Using a larger real-world dataset.
- Adding more house features such as location, bathrooms, parking, and property type.
- Performing advanced feature engineering.
- Applying cross-validation.
- Testing additional regression algorithms.
- Performing hyperparameter tuning.
- Creating a web application for house price prediction.
- Deploying the trained model online.

## 16. Project Status

**Project: House Price Prediction Using Machine Learning**

Status: Completed

The complete pipeline from data analysis to model training, evaluation, comparison, and prediction has been implemented.