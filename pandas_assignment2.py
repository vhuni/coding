'''
1. import pandas as pd and any other necessary libraries
2. Read the csv file into a dataframe
3. Obtain an overview of the count and data type
4. Get the descriptive statistics of the data
5. Check to see if there are any null values in the dataframe
6. Replace the missing ages with the average age and print the number of missing values
7. Drop the 'SibSp' column
8. Print the number of male and female passengers
9. Rename 'Id' to 'PassengerId'
10. Extract the title of the passengers
'''
# 1.
import pandas as pd
# 2.
data = pd.read_csv('ship.csv')
# 3. 
print(data.info())
# 4.
print(data.describe())
# 5.
print(data.isnull().sum())
# 6.
ave_age = data['Age'].mean()
# print(ave_age)
data['Age'] = data['Age'].fillna(ave_age)
# 7.
data.drop(['SibSp'],axis=1)
# 8.
print(data.groupby('Gender').count())
# 9.
data.rename(columns={'PassengerId':'PassengerID'},inplace=True)
# 10.
data['Title'] = data['Name'].str.extract(r', (\w+\.)')
print(data.head())