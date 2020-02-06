# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]
print(squares)

# 2. list operations
squares += [64, 81]  # add two elements at the end of the list
print(squares)

# 3. list methods
animals = ["Eagle", "Beaver", "Kangaroo", "Rooster", "Jaguar", "Monkey", "Panda", "Condo"]
animals.append("Dog")
animals.insert(1, "Cat")
animals.remove("Rooster")
print(animals.pop(0))  # pop(remove) the element at index 0
print(animals.count("Beaver"))
print(animals.index("Panda"))
