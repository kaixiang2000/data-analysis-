
"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q6-b
Description of Problem :relise 10 worst negative returns of spy and lly 
method: we just add the top 10  worst returns from the negative returns list
sort find top 10 worst and add them to positive returns then 
calculate all returns 
"""
import os
ticker = 'SPY'
# ticker = 'LLY'

input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')
returns_new_positive=[]
returns_new_negative=[]
bounus=1
try:
    with open(ticker_file) as f:
            # skip first line
        lines = f.read().splitlines()[1:]
    for row in lines:
        returns=float(row.split(',')[-3])
        if returns>0:
            returns_new_positive.append(returns)
        else:
            returns_new_negative.append(returns)
    
    # print(s_new)     
    returns_new_negative.sort()
    # print(returns_new_negative)       
    returns_new=returns_new_negative[:10]+returns_new_positive
    for i in returns_new:
        bounus=bounus+bounus*i
    final_amount=100*bounus
    # print('the final amount for SPY is: ',round(final_amount,5))
    print('the final amount for LLY/SPY is: ',round(final_amount,5))
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)