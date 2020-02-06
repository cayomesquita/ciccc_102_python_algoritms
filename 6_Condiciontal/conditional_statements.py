# Conditional statement
# (if-else statements)

# Getting user input
# input(prompt) - takes user input and returns as string
age = int(input("Enter your age: "))

if age >= 21:
    print("You can start drinking!!")
elif 13 < age < 21:
    print("Study hard to SAT!")
else:
    print("Pay video games!")