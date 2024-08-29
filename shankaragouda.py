# -*- coding: utf-8 -*-
"""Shankaragouda.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y9ukqCEehjpSkLniioXzLPemgT3lbSun
"""

import numpy as np
import sklearn
from sklearn import linear_model
height=[[4.0],[5.0],[6.0],[7.0],[8.0],[9.0],[10.0]]
weight=[  8, 10 , 12, 14, 16, 18, 20]
reg=linear_model.LinearRegression()
reg.fit(height,weight)
X_height=[[12.0]]
print("prediction: " , reg.predict(X_height))

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Step 1: Define the data
x = [[4.0], [5.0], [6.0], [7.0], [8.0], [9.0], [10.0]]
y = [16, 25, 36, 49, 64, 81, 100]

# Step 2: Fitting Linear Regression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# Step 3: Linear Regression prediction
print("Linear Regression Prediction for x=11:", lin_reg.predict([[11]]))

# Step 4: Fitting Polynomial Regression
polynomial_regression = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression(),
)
polynomial_regression.fit(x, y)

# Step 5: Polynomial Regression prediction
X_height = [[20.0]]
target_predicted = polynomial_regression.predict(X_height)
print("Polynomial Regression Prediction for x=20:", target_predicted)