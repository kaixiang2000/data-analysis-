"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q3
Description of Problem :create 5 years tables spy and lly 
for R R- R+ 3 sets
method: we create function to calculate stander div
         we create function to calculate R  remove year condition
"""
import os

ticker = 'LLY'
# ticker = 'SPY'
input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')

# initial list for lly/SPY
weekdaylist = []
yearlist = []

# define function for standard div
def stddiv(mylist):
    sum_std = []# sum of stander diviation
    for item in mylist:
        item = float(item)
        sum_std.append(item * item)
    squrenumstddiv = (sum(sum_std) / len(sum_std)) - ((sum(mylist) / len(mylist)) * (sum(mylist) / len(mylist)))
    numstddiv = squrenumstddiv ** 0.5
    #numstddiv = round(numstddiv, 7)
    print("Standard Div is " + str(round(numstddiv,5)))

def calculation(pick_weekday):
    return_lly_r = []# for all returns
    return_lly_r_positive = []# for positive returns
    return_lly_r_negative = []# for negative returns
    for row in lines:
        # define weekdays
        weekdays = row.split(",")[4]
        # print(weekdays)

        
        if weekdays == pick_weekday:
            # print(row.split(","))
            returns = float(row.split(",")[-3])
            return_lly_r.append(returns)

            if returns > 0:
                return_lly_r_positive.append(returns)
            elif returns < 0:
                return_lly_r_negative.append(returns)

    # Average for R set
    raverage = sum(return_lly_r) / len(return_lly_r)
    #raverage = round(raverage, 7)
    print("Mean for R set on " + " and " + pick_weekday + " is " + str(round(raverage,5)))
    print("Today number for R set on "  + pick_weekday + " is " + str(len(return_lly_r)))
    stddiv(return_lly_r)

    # Average for R+ set
    posraverage = sum(return_lly_r_positive) / len(return_lly_r_positive)
    #posraverage = round(posraverage, 7)
    print("Mean for R+ set on "  + " and " + pick_weekday + " is " + str(round(posraverage,5)))
    print("Today number for R+ set on " + pick_weekday + " is " + str(len(return_lly_r_positive)))
    stddiv(return_lly_r_positive)

    # Average for R- set
    negraverage = sum(return_lly_r_negative) / len(return_lly_r_negative)
    #negraverage = round(negraverage, 7)
    print("Mean for R- set on " + " and " + pick_weekday + " is " + str(round(negraverage,5)))
    print("Today number for R- set on  " + pick_weekday + " is " + str(len(return_lly_r_negative)))
    stddiv(return_lly_r_negative)

try:

    with open(ticker_file) as f:
        # skip first line
        lines = f.read().splitlines()[1:]

    # Question 3
    for row in lines: #loop weekend
        day = row.split(",")[4]
        if day not in weekdaylist:
            weekdaylist.append(day)

    for j in weekdaylist:
            calculation(j)

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)