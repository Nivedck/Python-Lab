# Creating a list
fruits = ['apple', 'banana', 'cherry', 'date']

# Accessing elements
print("First fruit:", fruits[0])

# Modifying elements
fruits[1] = 'blueberry'
print("Modified list:", fruits)

# Adding elements
fruits.append('elderberry')
print("After append:", fruits)

# Inserting elements
fruits.insert(2, 'fig')
print("After insert at index 2:", fruits)

# Removing elements
fruits.remove('apple')
print("After removing 'apple':", fruits)

# Popping elements
last = fruits.pop()
print("Popped element:", last)

# Sorting the list
fruits.sort()
print("Sorted list:", fruits)

# Reversing the list
fruits.reverse()
print("Reversed list:", fruits)
