# coding: utf-8


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

az = pd.read_csv('data/AMZN.csv',index_col=0)

#Create a new column PriceDiff in the DataFrame az
az['PriceDiff'] = az['Close'].shift(-1) - az['Close']

#Run this code to display the price difference of Amazon on 14th July 2020
print(f"The price difference on the 14th July is: {az['PriceDiff'].loc['2020-07-14']}")


# ** Expected Output: ** -75.12988

# Create a new column in the DataFrame - Daily return
# Daily Return is calcuated as PriceDiff/Close
#Create a new column Return in the DataFrame az

az['Return'] = az['PriceDiff'] /az['Close']

#Run this code to print the return on 14th July 2020
print(f"The return on the 14th July is: {az['Return'].loc['2020-07-14']}")

# ** Expected Output: ** -0.02436

#Create a new column Direction using list comprehension. 
#The List Comprehension means : if the price difference is larger than 0, denote as 1, otherwise, denote as 0,
#for every record in the DataFrame - fb

az['Direction'] = [1 if az['PriceDiff'].loc[ei] > 0 else 0 for ei in az.index ]

# Show the price difference 14th July 2020
print('Price difference on {} is {}. direction is {}'.format('2020-07-14', az['PriceDiff'].loc['2020-07-14'], az['Direction'].loc['2020-07-14']))


# DataFrame can be used to calculate the rolling average 

az['ma50'] = az['Close'].rolling(50).mean()

#plot the moving average of 2019
plt.figure(figsize=(10, 8))
az['ma50'].loc['2019-01-01':'2019-12-31'].plot(label='MA50')
az['Close'].loc['2019-01-01':'2019-12-31'].plot(label='Close')
plt.legend()
plt.show()
