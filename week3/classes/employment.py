# Using inheritance class

# parent class
class Employees:
  def __init__(self, firstname, lastname) -> None:
    self.firstname = firstname 
    self.lastname = lastname

# child class 
class Supervisors(Employees):
    def __init__(self, firstname, lastname, password) -> None:
       super().__init__(firstname, lastname)  
       self.password = password

# child class
class Chefs(Employees):
    def leave_request(self, days):
      return "May I take a leave for " + str(days) + " days"

# instance of the child class supervisors
adrian = Supervisors("Adrian", "A", "googoo")


# instance of the child class chefs
emily = Chefs("Emily", "E")
john = Chefs("John", "J")

print(emily.leave_request(5))

print(adrian.password)

print(john.lastname)
