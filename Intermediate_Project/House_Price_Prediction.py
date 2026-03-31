import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def main():
    print("--- House Price Prediction Project ---")
    print("           Made by AB Corp            ")
    print("            Shresth Singh            ")
    print("-" * 38)
    
    # 1. Load the Dataset
    print("\n[1] Loading California Housing Dataset...")
    california = fetch_california_housing()
    df = pd.DataFrame(california.data, columns=california.feature_names)
    df['Price'] = california.target # Target variable (Median house value in 100k's)
    
    # 2. Exploratory Data Analysis (EDA)
    print("\n[2] Exploratory Data Analysis:")
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
    print("\nChecking for missing values:")
    print(df.isnull().sum()) # No missing values in this dataset
    
    # 3. Visualization
    print("\n[3] Generating Visualizations...")
    
    # Plot 1: Correlation Heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    print(">> Close the heatmap window to continue...")
    plt.show()
    
    # 4. Data Preprocessing
    print("\n[4] Preparing Data for Modeling...")
    X = df.drop('Price', axis=1) # Features
    y = df['Price']              # Target
    
    # Train/Test Split (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training data size: {X_train.shape}")
    print(f"Testing data size: {X_test.shape}")
    
    # 5. Model Building & Training
    print("\n[5] Training Linear Regression Model...")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 6. Evaluation & Results
    print("\n[6] Evaluating Model...")
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("-" * 30)
    print("MODEL METRICS:")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"Mean Squared Error (MSE):  {mse:.4f}")
    print(f"Root Mean Sq Error (RMSE): {rmse:.4f}")
    print(f"R-squared (R2 Score):      {r2:.4f}")
    print("-" * 30)
    
    # Plot 2: Actual vs Predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Actual vs Predicted House Prices")
    plt.tight_layout()
    print(">> Close the scatter plot window to finish the script...")
    plt.show()
    
    print("\nProject execution complete.")

if __name__ == "__main__":
    main()