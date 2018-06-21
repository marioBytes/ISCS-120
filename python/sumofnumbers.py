import math


numbers = 1  # prompt user for first number

total = 0

# as long as number is greater than 0 loop
while numbers >= 0:
    # prompt user to enter another number unitl it equals a negative number
    total = int(input('Enter another positive number: '))
    new_total = total + numbers


print(total)
