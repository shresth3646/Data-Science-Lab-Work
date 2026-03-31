**Project Title**
Regression: House Price Prediction

**Description**
The objective of this project is to build a machine learning regression model capable of predicting house prices based on various housing features such as median income, house age, average rooms, and geographical location.

**Dataset**
Source: Scikit-learn datasets (fetch_california_housing) / StatLib repository.
Description of data: The dataset contains 20,640 instances with 8 numeric, predictive attributes and the target variable (median house value in units of $100,000 for California districts).

**Steps Performed**
1. Data Cleaning: Checked for missing values and confirmed the dataset was clean. Handled feature extraction into Pandas DataFrame.
2. Exploratory Data Analysis: Analyzed summary statistics, feature types, and dataset shape.
3. Visualization: Plotted a Correlation Heatmap to understand the relationships between features (e.g., Median Income vs Price) and created an Actual vs. Predicted scatter plot to visualize model performance.
4. Model Building (if applicable): Split the data into 80% training and 20% testing sets. Trained a Multiple Linear Regression model using the training data.
5. Run this exat command in the terminal
 `python -m pip install pandas numpy matplotlib seaborn scikit-learn`

**Results**
Key findings: Median Income (MedInc) is the strongest positive predictor of house prices.
Metrics (if applicable):
Mean Absolute Error (MAE): ~0.533
Mean Squared Error (MSE): ~0.555
Root Mean Squared Error (RMSE): ~0.745
R-squared (R2): ~0.595

**Tools Used**
Python
NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

**Conclusion**
The Linear Regression model established a solid baseline for predicting house prices, explaining nearly 60% of the variance in the target variable. Future improvements could include standardizing features using StandardScaler or experimenting with more complex algorithms like Random Forest Regressor to capture non-linear relationships.

**Author**
Shresth Singh