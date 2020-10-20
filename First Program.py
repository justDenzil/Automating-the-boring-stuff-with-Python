import time
from time import gmtime, strftime
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
