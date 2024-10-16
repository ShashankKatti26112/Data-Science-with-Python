import pandas as pd  
import numpy as np   
import matplotlib.pyplot as plt 
import seaborn as sns  
from sklearn.tree import DecisionTreeClassifier  
from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score, classification_report  

# Load the dataset into a DataFrame
df = pd.read_csv("C:/Users/hp/Downloads/heart_v2.csv")

# Display the first few rows to understand the data structure
print("First 5 rows of the dataset:")
print(df.head())

# Get information about the dataset (columns, data types, non-null values)
print("\nDataset Info:")
df.info()

# Check for missing values in the dataset
print("\nMissing values per column:")
print(df.isnull().sum())

# Generate descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# Visualize the distribution of the target column (if present)
if 'target' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='target', palette='viridis')
    plt.title('Distribution of Target Variable')
    plt.show()
else:
    print("\nNo 'target' column found in the dataset.")

# Check for correlations between numerical columns
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Example: Group by and summarize data (replace 'age' and 'target' with relevant columns)
if 'age' in df.columns and 'target' in df.columns:
    print("\nAverage age by target:")
    print(df.groupby('target')['age'].mean())

# Building and evaluating a Decision Tree model
if 'target' in df.columns:
    # Splitting the data into features (X) and target (y)
    X = df.drop('target', axis=1)  # All columns except 'target'
    y = df['target']  # The target column

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initializing and training the Decision Tree model
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    # Making predictions on the test set
    y_pred = clf.predict(X_test)

    # Evaluating the model
    print("\nDecision Tree Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
else:
    print("\nThe dataset does not contain a 'target' column, so the model could not be built.")
