import time #time module provides time-related functions
from time import gmtime, strftime #Function strptime() can parse year with century as a decimal number when given %Y format code
print('Hello, what is your name ?')
myName = str(input())
print('Nice to meet you '+ myName)
print('Hello, what is your age ?')
age = int(input())
print('You look amazing for a '+ str(age)+' year old')
time.sleep(2)
currentYear = int(strftime("%Y", gmtime()))
birthYear = currentYear - age
print('You were born in the year '+ str(birthYear))
