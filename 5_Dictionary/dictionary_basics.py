# Lists, strings tuples are index-based (0, 1, 2, 3, 4)

# Dictionary: A collection of key-value paris
# (Some other languages they call it Map)
# * You access its values by looking up a "key" instead of an index
# * Keys MUST be UNIQUE. (A key can be ny string or number)

contacts = {
    "Cayo": "778-123-1234",
    "Martin": "778-321-4312",
    "Derrick": "778-392-4838"
}
print(contacts)

# Access dictionary by key to get value
print(contacts["Cayo"])

# Add a new entry (key-value pair)
contacts["Leo"] = "604-234-1234"
print(contacts)

# Update a value for an existing key
contacts["Leo"] = "No Phone Number"
print(contacts)

# Delete an entry from a dictionary
del contacts["Martin"]
print(contacts)

# Get a list of keys
print(list(contacts.keys()))

# Get a list of values
print(list(contacts.values()))

# "in" keyword: is used to check if a list of dictionary contains a specific key
print("Cayo" in contacts)
print("Leo" in contacts)