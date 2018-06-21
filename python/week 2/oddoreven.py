'''
Mario Martinez
6/17/2018

This program takes in a number and determines if it's even or odd

Time spent: 1.5 hours

Honor Code: I pledge that this program represents my own
program code. I received help from no one in designing and debugging my program.
'''
import math

# propmt user to enter a number
number = int(input('Please enter a number to see if it is even or odd: '))

if number % 2 == 0:  # calculate number and if there's no remainder it's even
    print('Number is even!')
else:  # if there's a remainer it's odd
    print('Number is odd!')
