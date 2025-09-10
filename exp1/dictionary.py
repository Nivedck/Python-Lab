# Creating a dictionary
student = {
    "name": "Nived",
    "age": 20,
    "branch": "IT"
}

# Accessing values
print("Name:", student["name"])

# Adding a new key-value pair
student["roll"] = 101

# Updating a value
student["age"] = 21

# Removing a key
del student["branch"]

# Iterating through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
