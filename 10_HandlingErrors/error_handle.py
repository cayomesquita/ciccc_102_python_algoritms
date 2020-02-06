# Errors

# 1. Syntax Error (Compile-time Error)
# - When python program can not interpret your code, since you can not follow the correct sintax for python
# - This errors you are likely ti ge when you make a typo (indentantion)
# - Python will show red inderline


# 2. Exceptions (Run-time Error) - crash
# When unexpected things happen during the execution of a program (run-time), even if your code is syntactically correct
# - There are differents types of exceptions in python, and you can see which exception is 'thrown' in the error message.
# -> PLEASE READ THE ERROR MESSAGE
while True:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))

        print(a / b)

        break
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please enter a number!")
    except ZeroDivisionError as e:
        print("Can not divide by zero!")
        print("Please enter a non-zero number!")
