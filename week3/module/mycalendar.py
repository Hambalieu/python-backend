import  sys, calendar

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


