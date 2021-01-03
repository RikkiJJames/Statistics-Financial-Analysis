# coding: utf-8

# ## Build a simple trading strategy 

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# ### 1. Munging the stock data and add two columns - MA10 and MA50


#import az's stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
az = pd.read_csv('data/AMZN.csv',index_col=0)
az['MA10'] = az['Close'].rolling(10).mean()
az['MA50'] = az['Close'].rolling(50).mean()
az = az.dropna()
az.head()


# ### 2. Add "Shares" column to make decisions base on the strategy 

#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)

az['Shares'] = [1 if az.loc[ei, 'MA10']>az.loc[ei, 'MA50'] else 0 for ei in az.index]

#Add a new column "Profit" using List Comprehension, for any rows in az, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

#Plot a graph to show the Profit/Loss

az['Close1'] = az['Close'].shift(-1)
az['Profit'] = [az.loc[ei, 'Close1'] - az.loc[ei, 'Close'] if az.loc[ei, 'Shares']==1 else 0 for ei in az.index]
az['Profit'].plot()
plt.axhline(y=0, color='red')

# ### 3. Use .cumsum() to display our model's performance if we follow the strategy 

#Use .cumsum() to calculate the accumulated wealth over the period

az['wealth'] = az['Profit'].cumsum()
az.tail()

#plot the wealth to show the growth of profit over the period

az['wealth'].plot()
plt.title('Total money you win is {}'.format(az.loc[az.index[-2], 'wealth']))

# Expected result : 1696.32
