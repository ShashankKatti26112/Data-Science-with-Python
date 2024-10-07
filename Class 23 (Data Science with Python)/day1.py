import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read the CSV file
data = pd.read_csv("C:/Users/hp/Desktop/Data Science with Python/Class 23 (Data Science with Python)/day.csv")

# Display the first few rows of the DataFrame
print("First few rows of the dataset:")
print(data.head())

# Display summary statistics for numeric columns
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Convert 'dteday' to datetime if it exists in the dataset
if 'dteday' in data.columns:
    # Specify the format as day-first (dd-mm-yyyy)
    data['dteday'] = pd.to_datetime(data['dteday'], format='%d-%m-%Y')

# Visualize the distribution of total rentals ('cnt')
plt.figure(figsize=(10, 6))
sns.histplot(data['cnt'], bins=30, kde=True)
plt.title('Distribution of Total Bike Rentals')
plt.xlabel('Total Rentals')
plt.ylabel('Frequency')
plt.show()

# Plot total rentals over time
if 'dteday' in data.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(data['dteday'], data['cnt'])
    plt.title('Total Bike Rentals Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Rentals')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Calculate correlation matrix and visualize it using a heatmap
plt.figure(figsize=(10, 8))
corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Calculate average rentals based on weather situation ('weathersit') if present
if 'weathersit' in data.columns:
    avg_rentals_by_weather = data.groupby('weathersit')['cnt'].mean()
    print("\nAverage bike rentals by weather situation:")
    print(avg_rentals_by_weather)

    # Plot average rentals by weather situation
    plt.figure(figsize=(8, 5))
    avg_rentals_by_weather.plot(kind='bar', color='skyblue')
    plt.title('Average Bike Rentals by Weather Situation')
    plt.xlabel('Weather Situation')
    plt.ylabel('Average Rentals')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Find and print the day with the highest number of rentals
if 'dteday' in data.columns:
    max_rentals_day = data.loc[data['cnt'].idxmax()]
    print(f"\nDay with the highest rentals: {max_rentals_day['dteday']}, Total rentals: {max_rentals_day['cnt']}")

# Visualize total rentals by month (assuming 'dteday' exists)
if 'dteday' in data.columns:
    data['month'] = data['dteday'].dt.month
    monthly_rentals = data.groupby('month')['cnt'].mean()

    plt.figure(figsize=(10, 6))
    monthly_rentals.plot(kind='bar', color='lightcoral')
    plt.title('Average Monthly Bike Rentals')
    plt.xlabel('Month')
    plt.ylabel('Average Rentals')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# Check correlation between 'cnt' (total rentals) and 'temp' (temperature)
if 'temp' in data.columns:
    temp_corr = data['cnt'].corr(data['temp'])
    print(f"\nCorrelation between temperature and total rentals: {temp_corr:.2f}")

# Machine Learning: Linear Regression
# Feature selection
features = ['temp', 'humidity', 'windspeed', 'weathersit']  # Add other relevant features if needed
data = pd.get_dummies(data, columns=['weathersit'], drop_first=True)  # Convert categorical variable into dummy/indicator variables

# Check if selected features exist in the dataset
for feature in features:
    if feature not in data.columns:
        print(f"Feature '{feature}' is not in the dataset.")
        break
else:
    X = data[features]
    y = data['cnt']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\nMean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # Print the coefficients of the model
    print("\nCoefficients:")
    for i, col in enumerate(X.columns):
        print(f"{col}: {model.coef_[i]:.4f}")
