# In this lab, you will be using two searching algorithms we covered in class to
# search for a word in dictionary. Compare the performance for each algorithm.
# You will have to output the number of steps for both algorithms when used for searching
# for the same word. (case-insensitive)
# Your output should look like this. Try to search for 5 different words of your choice.
#
# ex)
# Searching for "orange"...
# Linear Search: {} steps
# Binary Search: {} steps
#
# Searching for "orangeeeeee"...
# Linear Search: no matching word found
# Binary Search: no matching word found


def binary_search(items, target):
    lower = 0
    upper = len(items) - 1
    steps = 0
    while lower <= upper:
        mid = (lower + upper) // 2
        steps += 1
        if items[mid] == target:
            return mid, steps
        elif items[mid] > target:
            upper = mid - 1
        elif items[mid] < target:
            lower = mid + 1

    return -1, steps


def linear_search(items, target):
    """
    Return the index of the target in the items.
    Return -1 if the target not found.
    :param items: a list of items
    :param target: the item we're searching for
    :return the index of the item in the items list.
    """
    steps = 0
    for i in range(len(items)):
        steps += 1
        if items[i] == target:
            return i, steps

    return -1, steps


# Open the dictionary file and read all lines as a list of words.
with open('words') as f:
    lines = f.readlines()

# Strip off the newline character for each word.
lines = [line.strip() for line in lines]

target = input("Search Word: ")
li = linear_search(lines, target)
bi = binary_search(lines, target)

print(f"Searching for \"{target}\"")
print(f"Linear Search: {li[1]} steps")
print(f"Binary Search: {bi[1]} steps")
