'''
Mario Martinez
6/17/2018

This program calcualtes the amount of taxes a user will pay according to their marital status and income.

Time spent: 3 hours

Honor Code: I pledge that this program represents my own
program code. I received help from the math video on Canvas in designing and debugging my program.
'''

import math

single = 1
married = 2

# prompt and get user marital status
maritalStatus = int(
    input('Enter 1 if you\'re single or enter 2 if you\'re married: '))

if maritalStatus == 1:  # single code
    # prompt and get user for income if single
    income = float(input('Enter your income $'))

    # First income tax bracket calculations
    if income >= 0 and income <= 9325:
        taxesOwed = float(income * .10)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

    # Second income tax bracket calculations
    elif income >= 9326 and income <= 37950:
        taxesOwed = float(((income - 9325) * .15) +
                          932.50)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

    # Third income tax bracket calculations
    elif income >= 37951 and income <= 91900:
        taxesOwed = float(((income - 37950) * .25) +
                          5226.25)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

    # Fourth income tax bracket calculations
    elif income >= 91901 and income <= 191650:
        taxesOwed = float(((income - 91900) * .28) +
                          18713.75)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

    # Fifth income tax bracket calculations
    elif income >= 191651 and income <= 416700:
        taxesOwed = float(((income - 191650) * .33) +
                          46643.75)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

    # Sixth income tax bracket calculations
    elif income >= 416701 and income <= 418400:
        taxesOwed = float(((income - 416700) * .35) +
                          120910.25)  # calculate taxes owed
        print('Taxes owed $', '%.2f' % taxesOwed)

    # Last income tax bracket calculations
    elif income >= 418401:
        taxesOwed = float(((income - 418400) * .396) +
                          121505.25)  # calculate taxes owed
        print('Taxes owed $', "%.2f" % taxesOwed)

elif maritalStatus == 2:  # married code
    print('This portion of the app is under construction')
