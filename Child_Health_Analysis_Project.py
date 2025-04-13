"""
Project Title: Analysis of Health Conditions Among Children Under Age 18 in the U.S. (Data From Data.Gov)

Project Objectives:
1. Data Cleaning and Preparation
2. Health Condition Trend Analysis
3. Demographic Breakdown
4. Distribution Analysis
5. Comparative Analysis
6. Data Visualization
7. Exporting Clean Data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Cleaning and Preparation
data = pd.read_csv("Health_conditions_among_children_under_age_18__by_selected_characteristics__United_States.csv")
data.replace(["*", "Not applicable", "Not available", "Suppressed", "..."], np.nan, inplace=True)
data.dropna(subset=['ESTIMATE'], inplace=True)
data['YEAR'] = data['YEAR'].astype(str)

print("Data Info:")
print(data.info())
print("\nMissing Values:")
print(data.isnull().sum())

#2. Health Condition Trend Analysis
plt.figure(figsize=(14, 7))
for condition in data['PANEL'].unique():
    temp = data[(data['PANEL'] == condition) & (data['STUB_NAME'] == 'Total')]
    plt.plot(temp['YEAR'], temp['ESTIMATE'], marker='o', label=condition)

plt.title("Trends of Health Conditions Among Children (Total)")
plt.xlabel("Year")
plt.ylabel("Estimate (%)")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Demographic Breakdown
plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='AGE', y='ESTIMATE', hue='PANEL')
plt.title("Distribution of Estimates by Age and Condition")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 4. Distribution Analysis
plt.figure(figsize=(10, 5))
sns.kdeplot(data['ESTIMATE'], fill=True, color='green')
plt.title("Density Plot of Estimate (%)")
plt.xlabel("Estimate")
plt.tight_layout()
plt.show()

# 5. Comparative Analysis
pivot = data.pivot_table(index='AGE', columns='PANEL', values='ESTIMATE', aggfunc='mean')
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("Average Health Estimates by Age and Condition")
plt.tight_layout()
plt.show()

# 6. Visualization

# Violin Plot for Yearly Distribution
plt.figure(figsize=(14, 6))
sns.violinplot(data=data, x='YEAR', y='ESTIMATE', inner='quartile', palette='Pastel1')
plt.title("Yearly Distribution of Health Estimates")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Plot: Average Estimate by Condition
condition_means = data.groupby("PANEL")["ESTIMATE"].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=condition_means.values, y=condition_means.index, palette='coolwarm')
plt.title("Average Estimate by Health Condition")
plt.xlabel("Average Estimate (%)")
plt.ylabel("Condition")
plt.tight_layout()
plt.show()

# Strip Plot: Estimates by Year & Condition
plt.figure(figsize=(14, 6))
sns.stripplot(data=data, x='YEAR', y='ESTIMATE', hue='PANEL', jitter=True, dodge=True)
plt.title("Health Estimates Spread by Year and Condition")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Swarm Plot: Estimates by Age Group & Condition
plt.figure(figsize=(14, 6))
sns.swarmplot(data=data, x='AGE', y='ESTIMATE', hue='PANEL')
plt.title("Estimates by Age Group and Condition")
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 7. Exporting Clean Data
data.to_csv("Cleaned_Child_Health_Data.csv", index=False)
print("Cleaned data saved as 'Cleaned_Child_Health_Data.csv'")
