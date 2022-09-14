from distutils.sysconfig import customize_compiler


customer = {
  "name":"Joe Ro",
  "email":"jro@gmail.com",
  "age":30,
  "is_verified": True
}
print(customer["name"])


## Write a program that transate digits to words:

phone = input("Phone: ")

my_dict = {"0":"Zero", "1": "One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}

output = ""
for ch in phone:
  output += my_dict.get(ch, "!") + " "
print(output)
