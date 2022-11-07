
"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q6-a
Description of Problem :lose 10 best positive returns of spy and lly 
method: we just remove the top 10 returns from the positive returns list
method:sort find top 10 and remove then calculate the rest 
"""
import os
ticker = 'SPY'
# ticker = 'LLY'

input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')
returns_new_positive=[]
bounus=1
try:
    with open(ticker_file) as f:
            # skip first line
            lines = f.read().splitlines()[1:]
    for row in lines:
        returns=float(row.split(',')[-3])
        if returns>0:
            returns_new_positive.append(returns)
        
    returns_new_positive.sort(reverse=True)
    # print(returns_new)            
    returns_new=returns_new_positive[10:]
    for i in returns_new:
        bounus=bounus+bounus*i
    final_amount=100*bounus
    # print('the final amount for SPY is: ',round(final_amount,5))
    print('the final amount for LLY/spy is: ',round(final_amount,5))
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)