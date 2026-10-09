import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load Dataset
df = pd.read_csv("dataset/house_prices.csv")

# Features and Target
X = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]


# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Multiple Linear Regression
multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)

multiple_pred = multiple_model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, multiple_pred)
mse = mean_squared_error(y_test, multiple_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, multiple_pred)

print("Multiple Linear Regression")
print("--------------------------")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)


# Polynomial Regression
X_poly = df[["Area"]]
y_poly = df["Price"]

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(
    X_poly, y_poly, test_size=0.2, random_state=42
)

poly_model = make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

poly_model.fit(X_train_p, y_train_p)

poly_pred = poly_model.predict(X_test_p)

poly_r2 = r2_score(y_test_p, poly_pred)

print("\nPolynomial Regression")
print("--------------------")
print("R² Score:", poly_r2)


# Final House Price Prediction
new_house = pd.DataFrame({
    "Area": [1800],
    "Bedrooms": [3],
    "Age": [5]
})

predicted_price = multiple_model.predict(new_house)

print("\nFinal House Price Prediction")
print("----------------------------")
print("Area: 1800 sqft")
print("Bedrooms: 3")
print("Age: 5 years")
print("Predicted Price: ₹", round(predicted_price[0], 2), "Lakhs")