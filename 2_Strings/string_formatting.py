# Escape characters (\)
# - newline: "\n"
# - tab: "\t"
# - quotes: \"
city = "va\nc\"ou\tver"
print(city)

dont_worry = "Don't worry, about \"the weather!\""
print(dont_worry)

# Slovak
message = "Ahoj, \nako sa mas?\nJa som OK"
print(message)

multiline_message = """
Ahoj,
Ako a mas?
Ja som OK!
"""

print(multiline_message)

# * formatting string
# %s: string
# %d: digits
# %f: float

name = "Derrick"
city = "Vancouver"
temp = 8

message1 = "Hello, %s! My name is %s. The temp is %d today" % (city, name, temp)
print(message1)

country = "Canada"

message2 = f"{country} is big!"
print(message2)

average_poit = 80.532154
# 80.5
print(f"the average point is {average_poit:.2f}")

print("the average point is %.2f" % average_poit)

x = 10
y = 17

print(f"{x} * {y} = {x * y}")
