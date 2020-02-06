# Tuples are almost identical to lists. The only big difference between lists and tuples is that tuples can't

vowels = ("a", "e", "i", "o", "u")
vowels2 = "a", "e", "i", "o", "u"

print(vowels[0])
print("k" in vowels)
# vowels[0] = "A" # Error

# Methods
vowels.index("e")
vowels.count("i")


# Use cases
# 1. return multiple values from a function
def a():
    return 1, "Mars"


# 2. check if an item is in a tuple

# 3. multiple assignments
year, country = 2020, "Canada"
_, _, province = 2020, "Canada", "BC"

# swap
x = 10
y = 20
x, y = y, x
