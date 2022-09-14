#Calculating the largest number in a List
numbers = [3, 6, 20, 68, 4, 10]
max = numbers[0]
for nums in numbers:
  if  nums > max:
    max = nums
print(max)


# ## 2D List
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
# # getting an item in a matrix
print(matrix[0][1])

# # iterating throw a matrix in python
for row in matrix:
  for item in row:
    print(item)

# Remove the duplicates in a list
my_list = [3, 2, 6, 20, 2,  68, 4, 3, 10]
uniq_nums = []
for numbers in my_list:
  if numbers not in uniq_nums:
    uniq_nums.append(numbers)
print(uniq_nums)
