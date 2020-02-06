# Data types

# There are many different data types in Python

# int: Integer
# float: Floating point
# bool: boolean
# str: a sequence of characters in quotes

language = "en_us"

print(type(language))

users = 10

print(str(users) + language)

# Typer Conversion (type casting): "chaging type"
# There are several built-in functions that let you convert on data type to another.

# str(x): converts x into a string representation.
# int(x): converts x into an integer.
# float(x): converts x into a floating-point numbere.

# Exercise: what is the type of the following operations?

# 1. 10 / 2 -> 5.0 (float)  '/': float division
print(type(10 / 2))

# 2. 10 // 3 -> 3 (int)     '//': int division
print(type(10 // 3))

# 3. float(a.12) -> Error
#    float(5) -> 5.0 (float)
print(float("a.12"))
