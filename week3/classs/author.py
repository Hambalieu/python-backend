# Define class MyFirstClass
class MyFirstClass():  
    # Define string variable called index
    print("Who wrote this?")
    index = "Author-Book"
    # Define function hand_list()
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        # variable + “ wrote the book: ” + variable
        print(philosopher + " wrote the book: " + book + " in the year " + str(year ))

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The art of War", 2005)

