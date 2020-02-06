# Loop - to repeat code

# for loops are used to iterate over a given sequence.
# On each iteration, the loop variable defined in the for loop will be assigned to the next value(sequence).

# Syntax
# for __ in collection:
#     what to repeate

# Numbers (simple loop with a list)
for i in [1, 2, 3, 4, 5]:
    print(i)
print("=======================")
# range(start, end, steps): returns a range numbers
for i in range(10):  # 0 <= < end, 1 step
    print(i)
print("=======================")
for i in range(1, 11):  # start <= < end, 1 step
    print(i)
print("=======================")
for i in range(1, 11, 2):  # start <= < end, 1 step
    print(i)
print("=======================")
for i in range(10, 5, -1):  # start <= < end, 1 step
    print(i)
print("=======================")

# Exercise
# 1. Write a loop to print all even numbrs from 0 to 100 (inclusive)

for i in range(0, 101, 2):
    print(i)
print("=======================")

# 1. Write a loop to print all odd numbrs from 0 to 100 (inclusive)

for i in range(1, 101, 2):
    print(i)
print("=======================")

# Strings: a sequence of characters
for ch in "Hello":
    print(ch)

# list: a sequence of items
for item in ["Hello", "Hola", "ahoj"]:
    print(item)

# (optional) list coprehension
a = [i for i in range(10) if i % 2 == 0]
print(type(a))
print(a)

print("======================")

# Exercise
# print the names that have less than 5 characters fro given list

names = ["Derrick", "Leo", "Sen", "Richard", "Douglas"]
print([name for name in names if len(name) < 5])

# How to write a for-loop to calculate the following 2⁰ + 2¹ + 2² + ... + 2^30
sum = 0

for power in range(31):
    sum += 2 ** power

print(sum)
