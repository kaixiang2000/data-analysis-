
"""
kaixiangli
Class: CS 677
Date:11/06/2022
Homework Problem #Q1
Description of Problem :create 5 tables 
for R R- R+ 3 sets
method: we create function to calculate stander div
we create function to calculate R
"""
import os

ticker = 'LLY'
input_dir = r'C:\Users\yanqi\OneDrive\Desktop'
ticker_file = os.path.join(input_dir, ticker + '.csv')

# initial list
weekdaylist = []
yearlist = []

# define function for standard div
def stddiv(mylist):
    sumstddivlist = []
    for item in mylist:
        item = float(item)
        sumstddivlist.append(item * item)
    squrenumstddiv = (sum(sumstddivlist) / len(sumstddivlist)) - ((sum(mylist) / len(mylist)) * (sum(mylist) / len(mylist)))
    numstddiv = squrenumstddiv ** 0.5
    #numstddiv = round(numstddiv, 7)
    print("Standard Div is " + str(round(numstddiv,5)))

# define functio9n to calculate r r- and r+
def calculation(pickuponeweekday, pickuponeyear):
    returns_lly_list = []
    returns_lly_positve_list = []
    returns_lly_negative_list = []

    for row in lines:
        # define weekdays
        weekdays = row.split(",")[4]
        year = row.split(",")[1]
        # print(weekdays)

        if year == pickuponeyear:
            if weekdays == pickuponeweekday:
                # print(row.split(","))
                dailyreturn = float(row.split(",")[13]) #collect all returns
                returns_lly_list.append(dailyreturn)
                # seperate to r+ and r-
                if dailyreturn > 0:
                    returns_lly_positve_list.append(dailyreturn)
                elif dailyreturn < 0:
                    returns_lly_negative_list.append(dailyreturn)

    # Average for R set
    raverage = sum(returns_lly_list) / len(returns_lly_list)
    #raverage = round(raverage, 7)
    print("Mean for R set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(round(raverage,5)))
    print("Today number for R set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(len(returns_lly_list)))
    stddiv(returns_lly_list)

    # Average for R+ set
    posraverage = sum(returns_lly_positve_list) / len(returns_lly_positve_list)
    #posraverage = round(posraverage, 7)
    print("Mean for R+ set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(round(posraverage,5)))
    print("Today number for R+ set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(len(returns_lly_positve_list)))
    stddiv(returns_lly_positve_list)

    # Average for R- set
    negraverage = sum(returns_lly_negative_list) / len(returns_lly_negative_list)
    #negraverage = round(negraverage, 7)
    print("Mean for R- set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(round(negraverage,5)))
    print("Today number for R- set on " + pickuponeyear + " and " + pickuponeweekday + " is " + str(len(returns_lly_negative_list)))
    stddiv(returns_lly_negative_list)

try:

    with open(ticker_file) as f:
        # skip first line
        lines = f.read().splitlines()[1:]

    # Question 1
    for row in lines: #loop weekend
        day = row.split(",")[4]
        if day not in weekdaylist:
            weekdaylist.append(day)

    for row in lines: #loop year
        year = row.split(",")[1]
        if year not in yearlist:
            yearlist.append(year)

    for r in yearlist:
        for i in weekdaylist:
            calculation(i, r)

except Exception as e:
    print(e)
    print('failed to read stock data for ticker: ', ticker)
