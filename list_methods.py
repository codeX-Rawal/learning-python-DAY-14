# Day 14: List Methods in Python

numbers = [5, 2, 9, 1, 7]
print("Original list:", numbers)

# append()
numbers.append(10)
print("After append:", numbers)

# extend()
numbers.extend([3, 6])
print("After extend:", numbers)

# insert()
numbers.insert(2, 4)
print("After insert:", numbers)

# remove()
numbers.remove(9)
print("After remove:", numbers)

# pop()
last_item = numbers.pop()
print("Popped item:", last_item)
print("After pop:", numbers)

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# count()
print("Count of 2:", numbers.count(2))

# index()
print("Index of 7:", numbers.index(7))

# Copy list
new_list = numbers.copy()
print("Copied list:", new_list)

# Clear list
numbers.clear()
print("After clear:", numbers)

# Practice example
marks = []
n = int(input("How many marks? "))

for i in range(n):
    mark = int(input("Enter mark: "))
    marks.append(mark)

marks.sort()
print("Sorted marks:", marks)
