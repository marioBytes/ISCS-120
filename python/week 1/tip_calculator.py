import math
'''
Honor Code: I pledge that this program represents my own
program code. I received help from Judy Pino in designing and debugging my program.
Mario Martinez
version: 3.5.6
6/11/2018
I spent about 15 to 20 minutes working on this program.

This is a program that calculates a tip for a bill.
'''

#get subtotal and gratuity from user
subtotal = float(input('What is the subtotal? $'))
gratuity = float(input('What is the percentage of gratuity (without decimal)? '))

#calculate tip
tip = float((gratuity / 100) * subtotal)

print('The tip amount is: $', round(tip, 2),)
