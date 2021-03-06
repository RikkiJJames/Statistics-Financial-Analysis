#import the package "Pandas" and "MatPlotLib" into Jupyter Notebook
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#importing data
az = pd.read_csv('data/AMZN.csv',index_col=0)

# run this cell to ensure Amazon stock data was imported
print(az.iloc[0, 0])

print(az.head())

print(az.columns)

# Number of rows (observations) and columns (variables)
print(az.shape)

#Show last five rows
print(az.tail())

#Show last seven rows
print(az.tail(7))

# print summary statistics of Amazon
print(az.describe())

# Select all data so far in 2020
az_2020 = az.loc['2020-01-06':'2020-12-14']

# Print price of Amazon on the 14th July
print(az.loc['2020-07-14'])

# print the opening price of the first row
print(az.iloc[0, 0])

# print the opening price of the ms last row
print(az.iloc[-1, 0])

# plot the Close price of 2020 of Amazon
plt.figure(figsize=(10, 8))
az_2020['Close'].plot()



