# While-loop
# A while loop is similar to an if statement. It repeats some code while the given condition is true. It will continue to execute the code for as long as the condition is true

# syntax
# while __condition__:
#     code to repeat

num = 1

while num <= 10:
    print(num)
    num += 1;

# Exercise
# Print all squeres from 1 to 99. (1, 4, 9, ...)

num = 1
square = num * num
while square < 100:
    print(square)
    num += 1;
    square = num * num
