class Payslips:
  def __init__(self, name , payment, amount) -> None:
    self.name = name 
    self.payment = payment 
    self.amount = amount 

  def pay(self):
    self.payment = "yes"

  def status(self):
    if self.payment == "yes":
      return self.name + " is paid " + str(self.amount)
    else:
      return self.name + " is not paid yet"

boye = Payslips("Boye", "no", 1000)  
ala = Payslips("Ala", "no", 3000) 


print(boye.status())
print(ala.status())

print("After payment:")
ala.pay()
print(ala.payment)
print(ala.status())
