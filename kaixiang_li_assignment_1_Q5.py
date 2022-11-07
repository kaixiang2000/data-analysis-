
"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q5
Description of Problem :all returns calculate spy and lly buy and hold 
method: buy the first day and sell on the last day 
method: create list of returns to collect returns 
then set bonus =1 dollar calculate bonus+=bonus*returns 
final mutiply 100
"""

import os
# ticker = 'SPY'
ticker = 'LLY'
returns_lly=[]
input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')
bonus=1
try:

    with open(ticker_file) as f:
        lines = f.read().splitlines()[1:]
        # skip first line
        for row in lines:
            returns=float(row.split(',')[-3])
            returns_lly.append(returns)
        for i in returns_lly:
            bonus=bonus+bonus*i
        money_all=100*bonus

        print("The final return for SPY/LLY :",round(money_all,5))
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)