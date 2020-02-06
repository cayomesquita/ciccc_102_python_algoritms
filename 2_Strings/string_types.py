# Methods -> Functions that belong to String type
# str.method() (dot operator to call methods)
# method() -> '()' call, execute, run

city = "vancouver"

# 1. Capitalize
print(city.capitalize())  # Vancouver

# 2. Uppercase(A), Lowercase(a)
print(city.lower())

print(city.upper())

# 3. index: returns the index of substring (no match cause Error)
#     find: returns the index of substring (no match returns -1)
print(city.index("o"))  # 4
print(city.index("cou"))  # 3
# print(city.index("x"))  # Error
print(city.find("ver"))  # 6
print(city.find("x"))  # -1

# 4. count: returns the occurrences of substring in string
# * case-sensitive (0) vs case-insensitive
food = "poutine donut tacos big-mac pizza"
print(food.count(" "))  # space is a character (ASCII 32)

# 5. 'in': to check wether some string is in another string
gretting = "hello world"
message = "hello"
print(message in gretting)  # True

# 6. String validation
# isalnum(): checks if string has alphanumeric chars (alphabets + numbers)
# isalpha(): checks if string has alphabets chars (only alphabets)
# isdigit(): checks if string has digits chars (only numbers)
# isupper()
# islower()
# isspace(): checks if string has whitespace chars
# - space(""), tab("ºt"), newline("ºn")

unit_num = "123"
street_name = "Robson"

print(unit_num.isdigit())  # True
print(street_name.isalpha())  # True
print(street_name.isalpha())  # True
