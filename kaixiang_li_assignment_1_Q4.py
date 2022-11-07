"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q4
Description of Problem :oracle calculate spy and lly 
method: we set bonus =1 to calculate all  positive returns then multiply 100
"""
import os
bonus=1#(for 1 dollar)
ticker = 'SPY'
# ticker = 'LLY'
input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')
try:

    with open(ticker_file) as f:
        # skip first line
        lines = f.read().splitlines()[1:]
    for row in lines:
        returns=float(row.split(',')[-3])
        if returns>0:
            bonus=bonus+bonus*returns
    money_all=100*bonus
    print("For SPY/LLY we final get: ",round(money_all,5))
except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)    