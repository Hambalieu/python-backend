menu = ["espresso", "mocha", "latte", "cappucino", "cortado", "american"]


#using map to find all the items in the menu list that starts with letter c:
def find_coffee(coffee):
  if coffee[0] == "c":
    return coffee
map_coffee = map(find_coffee, menu)
for item in map_coffee:
  print(item)


# Using filter to find all the items in the menu list that starts with letter c:
def find_coffee(coffee):
  if coffee[0] == "c":
    return coffee
filter_coffee = filter(find_coffee, menu)    
for x in filter_coffee:
  print(x)
