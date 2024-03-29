# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:04:26 2024

@author: 2017109600
"""

import pandas as pd

# Using double backslashes
file_path = 'C:\\Users\\2017109600\\css2024day4\\movie_dataset.csv'

# OR

# Using a raw string
file_path = r'C:\Users\2017109600\css2024day4\movie_dataset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

df.info()
#df.columns = df.columns.str.strip()


df['Revenue (Millions)'] = pd.to_numeric(df['Revenue (Millions)'], errors='coerce')
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)

highest_rated_movie = df[df['Rating'] == df[ 'Rating'] .max()]['Title'].values[0] 
average_revenue = df[ 'Revenue (Millions)'].mean()
average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue (Millions)'] .mean()
movies_2016 = df[df['Year'] == 2016] .shape[0]  
movies_nolan = df[df['Director'] == 'Christopher Nolan'] .shape[0]
high_rated_movies = df[df['Rating'] >= 8.0].shape [0]
median_rating_nolan = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
year_highest_avg_rating = df.groupby('Year')['Rating']. mean(). idxmax()
movies_2006 = df[df['Year'] == 2006] .shape[0]
movies_2016 = df[df['Year'] == 2016] .shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
most_common_actor = df['Actors'].str.split(', ').explode().mode()[0]
unique_genres_count = df['Genre'].str.split(', ').explode().nunique()

import seaborn as sns
import matplotlib.pyplot as plt
## Select only numerical columns for correlation analysis

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
numerical_features_df = df[numerical_columns]

# Calculate the correlation matrix
correlation_matrix = numerical_features_df.corr() 

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Print insights based on correlation values
print("\nInsights:")
print (correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(6))

#Create a heatmap using Seaborn
plt.figure (figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap = 'coolwarm', linewidths=.5) 
plt.title('Correlation Matrix of Numerical Features')
plt.show()
