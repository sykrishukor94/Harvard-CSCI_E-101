# Week 6 Material
# pivot tables
# import pandas and numpy
import pandas as pd
import numpy as np

df = pd.read_csv('cookiesdirtydata.csv')
df.head(5)
# drop rows if all elements are blank
df.dropna(how="all", inplace = True)

df.head(5)

# remove leading/trailing spaces
df["Salesman"] = df["Salesman"].str.strip()

df

# replaces invalid valuzes with NaN for one column
df['Price'] = df['Price'].replace('[^A-Za-z0-9]',np.NaN,regex=True)

# replaces invalid values with NaN for multiple columns
df[['Tweets','Sales']] = df[['Tweets','Sales']].replace('[^0-9]',np.NaN,regex=True)

df

# drop rows if one or more elements are blank
df = df.dropna()

df

# convert Date string to datetime object
df['Date'] = pd.to_datetime(df['Date'], format = '%m/%d/%Y')

df.head()

# save date frame to CSV file
df.to_csv("cookies_clean1.csv", index= False)

# pivot index (row) and column
df.pivot(index="Date", columns ="Salesman")

# pivot index (row) and column with specified values
df.pivot(index="Date", columns ="Salesman", values = "Sales")

# pivot index (row) and column with specified values
df.pivot(index="Salesman", columns ="Date", values = "Sales")

# read new data file
df = pd.read_csv('BankTest.csv')

df.tail(20)

# Using pivot_table method to group and summarize data
df.pivot_table(index="y", columns ="marital")

# Using pivot_table method to group and summarize data with specified values
df.pivot_table(index="y", columns ="education", values = "age" )
df.pivot_table(index="marital", columns ="y", values = "balance")
# Using pivot_table method to group and summarize data using aggfunc parameter to get sum, min, max, etc.
df.pivot_table(index="marital", columns ="y", values = "age", aggfunc="max")