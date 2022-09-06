# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1]
print(new_trial)




# string reversal using recursion

def string_reversal(str):
  if len(str) == 0:
    return str
  else:
    return string_reversal(str[1:]) + str[0]

str = "monday"
reverse = string_reversal(str)      
print(reverse)


