"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q6-c
Description of Problem :best 5 and worst 5 returns misguide by oracle for spy and lly 
method: we use top 5 worst returns from negative returns and add them to positive returns list
and remove the top 5 best returns from positive returns then 
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
            elif returns<0:
                returns_new_negative.append(returns)
        returns_new_positive.sort(reverse=True)
        returns_new_negative.sort()
        returns_new_positive=returns_new_positive[5:]
        returns_new=returns_new_positive+returns_new_negative[:5]
        for i in returns_new:
            bounus=bounus+bounus*i
        final_amount=100*bounus
        print('The final amount for LLY/SPY is:',round(final_amount,5))

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
