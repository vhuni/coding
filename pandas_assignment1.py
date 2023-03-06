'''
1. Import pandas and any other necessary libraries
2. Read 'BigMartSalesData.csv' as a dataframe called sales
3. Check the head of the dataframe
4. Check the tail of dataframe
5. Check the info of the data
6. Check if there null values in the data
7. Convert the CustomerID to a string and print the type
8. Convert the InvoiceDate to datatime type and print the type
9. Convert the month column to the name of the month and print the months
10. What is the average unit price?
11. What is the highest amount ever paid for an order?
12. Find the top 5 customers who have spent the most amount.
13. Find the bottom 5 customer who have spent the most amount.
14. How many orders were made in 2010 and 2011 respectively.
15. How many customers ordered just once?
'''

# 1.
import pandas as pd
import calendar

# 2.
data = pd.read_csv('BigMartSalesData.csv')
# 3.
print(data.head())
# 4.
print(data.tail())
# 5.
print(data.info())
# 6.
print(data.isnull().sum())
# 7.
data['CustomerID'] = (data['CustomerID'].astype('string'))
print('CustomerID datatype: ',data['CustomerID'].dtypes)
# 8.
data['InvoiceDate'] = (data['InvoiceDate'].astype('datetime64'))
print('InvoiceDate datatype: ',data['InvoiceDate'].dtypes)
# 9.
data['Month'] = data['Month'].apply(lambda x: calendar.month_abbr[x])
print(data['Month'].head())
# 10.
print(data['UnitPrice'].mean())
# 11. 
print(data['Amount'].max())
# 12.
print(data.groupby('CustomerID')['Amount'].sum().sort_values(ascending=False).head())
# 13.
print(data.groupby('CustomerID')['Amount'].sum().sort_values(ascending=True).head())
# 14.
print(data.groupby('Year')['InvoiceNo'].count())
# 15. How many customers ordered just once?
print('Customers with just 1 order: ',data['CustomerID'].nunique())
