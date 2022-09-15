# queue uses FIFO - first in first out

# In python we can use list but also we can use collections.deque

#Implementing queue using list:
# amz_stock_price_queue = []
# amz_stock_price_queue.insert(0, 125)
# amz_stock_price_queue.insert(0, 124)
# amz_stock_price_queue.insert(0, 123)
# amz_stock_price_queue.insert(0, 122)

# print(amz_stock_price_queue)

# #Pop method will pop out the first element inserted
# print(amz_stock_price_queue.pop())


# #Using collections deque to implement queue
from collections import deque
# q = deque()
# q.appendleft(5)
# q.appendleft(7)
# q.appendleft(2)
# q.appendleft(4)
# q.appendleft(3)

# print(q)

# # pop removes the element that was inserted first
# q.pop()
# print(q)


#Implementing a queue class
class Queue:
  def __init__(self):
    self.buffer = deque()
#Add element to queue
  def enqueue(self, val):
    self.buffer.appendleft(val)
#Remove element from queue
  def dequeue(self):
    return self.buffer.pop()
#Check if queue is empty
  def is_empty(self):
    return len(self.buffer)==0
#Check for the size of the queue
  def size(self):
    return len(self.buffer)


pq = Queue()

# Adding elements using the queue class we just created
pq.enqueue({
  'company':'Wal Mart',
  'timestamp': '15th Sep, 2:25pm',
  'price': 131.01
})
pq.enqueue({
  'company':'Wal Mart',
  'timestamp': '15th Sep, 2:26pm',
  'price': 132
})
pq.enqueue({
  'company':'Wal Mart',
  'timestamp': '15th Sep, 2:27pm',
  'price': 134
})

print(pq.buffer)

#Removing first element using the deque method
pq.dequeue()
print(pq.buffer)

#checking the size of the queue
print(pq.size())

# Checking if the queue is empty
# It will return False since i still have elements inside my queue
print(pq.is_empty())
