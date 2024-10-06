import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/hp/Desktop/Data Science with Python/Data Science Assignments/Movies.csv")

# Inspect the dataset
print(df.head())

# Drop unnecessary columns
movies_cleaned = df.drop(['director_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes', 'movie_facebook_likes'], axis=1)
print(movies_cleaned.head())

# Fill NaN values in the 'language' column with the mode
movies_cleaned['language'].fillna(movies_cleaned['language'].mode()[0], inplace=True)

# Convert gross and budget from float to integer (if necessary) for easier calculation
movies_cleaned['gross'] = movies_cleaned['gross'].fillna(0).astype(int)
movies_cleaned['budget'] = movies_cleaned['budget'].fillna(0).astype(int)

# Create a profit column (gross - budget)
movies_cleaned['profit'] = movies_cleaned['gross'] - movies_cleaned['budget']

# Sort the dataframe based on profit
movies_sorted = movies_cleaned.sort_values(by='profit', ascending=False)

# Extract the top 10 profiting movies
top10 = movies_sorted.head(10)
print(top10)

# Extract the top 250 movies as per the IMDb score
IMDb_Top_250 = movies_cleaned.sort_values(by='imdb_score', ascending=False).head(250)

# Create dataframes for Meryl Streep, Leonardo DiCaprio, and Brad Pitt movies
# Ensure the correct column 'actor_1_name' is used to identify the actors, not 'actor_1_facebook_likes'
Meryl_Streep = movies_cleaned[movies_cleaned['actor_1_name'] == 'Meryl Streep']
Leo_Caprio = movies_cleaned[movies_cleaned['actor_1_name'] == 'Leonardo DiCaprio']
Brad_Pitt = movies_cleaned[movies_cleaned['actor_1_name'] == 'Brad Pitt']

# Combine the three dataframes
Combined = pd.concat([Meryl_Streep, Leo_Caprio, Brad_Pitt])

# Group the combined dataframe by director and calculate the mean IMDb score
# Only include numeric columns for mean calculation
grouped = Combined.groupby('director_name').mean(numeric_only=True)

# Calculate the mean of critic reviews and audience reviews
mean_critic_reviews = movies_cleaned['num_critic_for_reviews'].mean()
mean_user_reviews = movies_cleaned['num_user_for_reviews'].mean()

print("Mean critic reviews:", mean_critic_reviews)
print("Mean user reviews:", mean_user_reviews)
