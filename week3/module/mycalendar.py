import  sys, calendar
from math import *



#check the path on your system
location = sys.path
# print(location)
for i in location:
  print(i)

#check how leap days are in between two years
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

#check is a year is leap
isleap = calendar.isleap(2030)
print(isleap)

#using the math module 
root = sqrt(9)
x = log10(50)
factorial_y = factorial(4)

print(x)
print(root)
print(factorial_y)
