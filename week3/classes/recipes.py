class Recipes():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish  
        self.items = items 
        self.time = time
    def content(self):
        print("The " + self.dish + " has "  + str(self.items) + \
          " and takes " + str(self.time)  + " min to prepare")    

pizza = Recipes("Pizza",["tomato","bread", "cheese"], 45)  
pasta = Recipes("Pasta", ["chicken", "spagetti", " marinera sauce"], 50)        


print(pizza.items)

print(pasta.items)
