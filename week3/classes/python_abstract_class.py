from abc import ABC, abstractmethod

class Employee(ABC):

  @abstractmethod
  def donate(self):
    pass

class Donation(Employee):
  def donate(self):
    a = input("How much would you like to donate: ")
    return a

amounts = []

jenny = Donation()
j = jenny.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)
