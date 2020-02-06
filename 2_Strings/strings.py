# + Concatenation: combinating two strings
print("hello" + " world")

# * multiplication: repeat strings
print("hello" * 5)

# Strings indexing (index = position)
singer = "Lady Gaga"
# index   012345678
# index "always" starts from "0"

print(singer[0])  # "L"
print(singer[7])  # "g"
print(singer[-1])  # "a" last char
# print(singer[0])    # Error (index out of bounds)

# String Slicing (Substring)
# start_index <=   < end_index
actor = "Will Smith"
# index  0123456789
print(actor[0:4])  #
print(actor[4:6])  #
print(actor[-3:-1])  #

# shortcuts
# starting at 0
print(actor[:4])

# from index 5 go to the end
print(actor[5:])

# from 0 to the end (copy)
print(actor[:])

# How to get the number of characters?
# len(str): returns the number of chars
print(len(actor))
print(actor[len(actor) - 1])
print(actor[-1])

# Strings are IMMUTABLE
# I can't change the internals (characters)
ball_player = "Lebron James"
