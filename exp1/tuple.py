# Creating a tuple
colors = ('red', 'green', 'blue', 'green')

# Accessing elements
print("First color:", colors[0])

# Counting elements
print("Count of 'green':", colors.count('green'))

# Finding index
print("Index of 'blue':", colors.index('blue'))

# Tuple unpacking
r, g, b, g2 = colors
print("Unpacked:", r, g, b, g2)
