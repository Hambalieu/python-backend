# Stack uses LIFO- Last in first out

# In python we can use list to implement stacks or use the collection.stack

# Pushing and pop in a stack is an order of 1 that is BIG O -O(1)

# Where as if you want to search for an element in a stack is an order of n that is Big O of n -O(n)

#Using list to impelement stack in python not recommended
stack_list = []

stack_list.append('https://www.espn.com/')
stack_list.append('https://www.espn.com/nfl/')
stack_list.append('https://www.espn.com/nfl/scoreboard')
stack_list.append('https://www.espn.com/nfl/schedule')
stack_list.append('https://www.espn.com/nfl/standings')

# print(stack_list)

#Pop will give me the last link that i have visited but it removes the element from the list
stack_list.pop()
# print(stack_list)

#If you just want to get the element you last added to the list withwout removing it use the below method
# print('')
# print(stack_list[-1])

# print(stack_list)


# Recommended approach is using collections.deque

from collections import deque
from inspect import stack


# stack_imp = deque()

# stack_imp.append('https://www.espn.com/')
# stack_imp.append('https://www.espn.com/nfl/')
# stack_imp.append('https://www.espn.com/nfl/scoreboard')
# stack_imp.append('https://www.espn.com/nfl/schedule')
# stack_imp.append('https://www.espn.com/nfl/standings')

# print(stack_imp)

# print('')

#Remove the last element added from the stack
# stack_imp.pop()

#Implement a Stack class
class Stack:
  def __init__(self):
    self.container = deque()
  def push(self, val):
    self.container.append(val)
  def pop(self):
    return self.container.pop()
  def peek(self):
    return self.container[-1]
  def is_empty(self):
    return len(self.container) == 0
  def size(self):
    return len(self.container)

# Now can use the stack class i created to implement all the functions in a stack
s = Stack()
#Add element to stack using the push method we created
s.push('https://www.espn.com/')
s.push('https://www.espn.com/nfl/')
s.push('https://www.espn.com/nfl/standing')
# print(s.container)

#Remove elelment from statck using pop method
#Note the pop method removes the last element that was added and also change the number of elements in the stack
s.pop()
# print(s.container)

# print('')
#We use the peek method to check the last element that was added to the stack without removing it from the stack
# print(s.peek())
# print('')
# print(s.container)


#Check if the stack is empty using the is_empty method we created
#Note this returns a boolean value i.e either True or False
# print(s.is_empty())

#Check the size of the stack gives us the number of elements in our stack
# print(s.size())


#Write a function in python that can reverse a string using stack data structure
def reverse_string(s):
  stack = Stack()
  for ch in s:
    stack.push(ch)

  revstr = ''
  while stack.size() != 0:
    revstr += stack.pop()
  return revstr

print(reverse_string('hello wolrd'))


#Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()"
def matched(ch1, ch2):
  is_match_dict = {
    ')':'(',
    ']':'[',
    '}':'{'
  }
  return is_match_dict[ch1] == ch2

def is_balanced(s):
  stack = Stack()
  for ch in s:
    if ch == '(' or ch == '{' or ch == '[':
      stack.push(ch)
    if ch == ')' or ch == '}' or ch == ']':
      if stack.size() == 0:
        return False
      if not matched(ch, stack.pop()):
        return False
  return stack.size() == 0

print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
