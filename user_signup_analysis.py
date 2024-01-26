# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:17:37 2024

@author: abudh
"""

# Purpose: Analyzing user sign-ups for SaaS platforms from a CSV file and generating plots.

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
file_path = 'users.csv'  # Replace with the actual file path
df = pd.read_csv(file_path)

# Plot 1: Number of users for each country
users_per_country = df['Country'].value_counts()
users_per_country.plot(kind='bar', title='Number of Users per Country')
plt.xlabel('Country')
plt.ylabel('Number of Users')
plt.show()

# Plot 2: Total revenue per country
df['Subscription_Price'] = df['Subscription_Price'].str.replace('$', '').astype(float)
total_revenue_per_country = df.groupby('Country')['Subscription_Price'].sum()
total_revenue_per_country.plot(kind='bar', title='Total Revenue per Country ($)')
plt.xlabel('Country')
plt.ylabel('Total Revenue ($)')
plt.show()

# Plot 3: Subscription type for each country
subscription_type_per_country = df.groupby(['Country', 'Subscription_Price']).size().unstack().plot(kind='bar', stacked=True, title='Subscription Type per Country')
plt.xlabel('Country')
plt.ylabel('Number of Users')
plt.legend(title='Subscription Price')
plt.show()
