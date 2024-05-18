#!/usr/bin/env python3

'''
print(10 + 5)    # addition
print(10 - 5)    # subtraction
print(10 * 5)    # multiplication
print(10 / 5)    # division
print(10 ** 5)   # exponents

print(10 + 5 * 2)       # multiplication happens before addition
print((10 + 5) * 2)         # parentheses happen before multiplication
print(10 + 5 * 2 - 10 ** 2) # first exponents, then multiplication, then addition and subtraction from left-to-right
print(15 / 3 * 4)       # division and multiplication happen from left-to-right
print(100 / ((5 + 5) * 2))  # the inner most parentheses are first performing addition, then parentheses again with multiplication, finally the division 
'''
# declaring variables
x = 10
y = 2
z = 5

print(str(x) + '+' + str(y) + '*' + str(z) + '=' + str(x+y*z))
# so im converting all the variables into strings following the lab instructions
# however the dificult part was more of converting everything into the proper string for the print
