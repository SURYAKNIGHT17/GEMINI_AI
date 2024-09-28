
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV
df = pd.read_csv('SuperStoreOrders.csv')

# Diagnosis & Preprocessing

# 1. Data Types
print("Data Types:\n", df.dtypes)

# 2. Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# 3. Duplicates
print("\nDuplicates:\n", df.duplicated().sum())

# 4. Convert data types
df['Sales'] = df['Sales'].astype(float)
df['Quantity'] = df['Quantity'].astype(int)
df['Discount'] = df['Discount'].astype(float)
df['Profit'] = df['Profit'].astype(float)
df['Shipping Cost'] = df['Shipping Cost'].astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# 5. Handle Outliers (if any)
# You may need to investigate outliers using boxplots or other methods.

# 6. Feature Engineering
# Create new features like:
df['Shipping Time'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Unit Price'] = df['Sales'] / df['Quantity']
df['Profit Margin'] = df['Profit'] / df['Sales']

# Analysis

# 1. Sales Analysis
print("\nSales Analysis:")
print(df.groupby('Category')['Sales'].sum())
sns.barplot(x='Category', y='Sales', data=df)
plt.title('Sales by Category')
plt.show()

# 2. Profit Analysis
print("\nProfit Analysis:")
print(df.groupby('Category')['Profit'].sum())
sns.barplot(x='Category', y='Profit', data=df)
plt.title('Profit by Category')
plt.show()

# 3. Customer Segmentation
print("\nCustomer Segmentation:")
print(df.groupby('Segment')['Sales'].sum())
sns.barplot(x='Segment', y='Sales', data=df)
plt.title('Sales by Segment')
plt.show()

# 4. Shipping Time Analysis
print("\nShipping Time Analysis:")
print(df.groupby('Ship Mode')['Shipping Time'].mean())
sns.boxplot(x='Ship Mode', y='Shipping Time', data=df)
plt.title('Shipping Time by Mode')
plt.show()

# 5. Product Performance Analysis
print("\nProduct Performance Analysis:")
print(df.groupby('Product Name')['Sales'].sum())
sns.barplot(x='Product Name', y='Sales', data=df)
plt.title('Sales by Product')
plt.show()

# 6. Correlation Analysis
print("\nCorrelation Analysis:")
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()

# 7. Sales Trends Over Time
print("\nSales Trends Over Time:")
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.plot(monthly_sales.index, monthly_sales.values)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Monthly Sales Trends')
plt.show()

# 8. Top Performing Products
print("\nTop Performing Products:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)[:10]
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Best-Selling Products')
plt.show()

# 9. Top Customers
print("\nTop Customers:")
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False)[:10]
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title('Top 10 Customers by Sales')
plt.show()

# 10. Discount Impact
print("\nDiscount Impact:")
sns.scatterplot(x='Discount', y='Sales', data=df)
plt.title('Discount vs. Sales')
plt.show()

# 11. Profit Margin Analysis
print("\nProfit Margin Analysis:")
sns.histplot(df['Profit Margin'], kde=True)
plt.title('Distribution of Profit Margin')
plt.show()

# 12. Shipping Time vs. Customer Satisfaction
print("\nShipping Time vs. Customer Satisfaction (Assuming 'Customer Satisfaction' is available):")
# (You would need a "Customer Satisfaction" column in your data for this analysis.)
# Example:
# sns.scatterplot(x='Shipping Time', y='Customer Satisfaction', data=df)
# plt.title('Shipping Time vs. Customer Satisfaction')
# plt.show()

# 13. Regional Analysis
print("\nRegional Analysis:")
regional_sales = df.groupby('Region')['Sales'].sum()
plt.pie(regional_sales.values, labels=regional_sales.index, autopct='%1.1f%%')
plt.title('Sales by Region')
plt.show()

# 14. Market Analysis
print("\nMarket Analysis:")
market_sales = df.groupby('Market')['Sales'].sum()
plt.pie(market_sales.values, labels=market_sales.index, autopct='%1.1f%%')
plt.title('Sales by Market')
plt.show()

# 15. State Analysis
print("\nState Analysis:")
state_sales = df.groupby('State')['Sales'].sum()
sns.barplot(x=state_sales.index, y=state_sales.values)
plt.title('Sales by State')
plt.xticks(rotation=90)
plt.show()

# 16. Category-Wise Profit Margin
print("\nCategory-Wise Profit Margin:")
category_profit_margin = df.groupby('Category')['Profit Margin'].mean()
sns.barplot(x=category_profit_margin.index, y=category_profit_margin.values)
plt.title('Average Profit Margin by Category')
plt.show()

# 17. Ship Mode vs. Shipping Cost
print("\nShip Mode vs. Shipping Cost:")
sns.boxplot(x='Ship Mode', y='Shipping Cost', data=df)
plt.title('Shipping Cost by Ship Mode')
plt.show()

# 18. Customer Segmentation by Sales
print("\nCustomer Segmentation by Sales:")
sales_segments = pd.qcut(df['sales'], q=4, labels=['Low', 'Medium', 'High', 'Very High'])
sns.countplot(x=sales_segments)
plt.title('Customer Segmentation by Sales')
plt.show()

# ... Add more analyses and visualizations as needed based on your specific business questions.

