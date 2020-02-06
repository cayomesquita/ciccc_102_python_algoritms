# Linear Search
# - "unsorted" list of data
# - search for the target in a linear manner (one by one)
# - Time Complexity: O(n)
#   (In the worst case, it will take n steps if you have n elements)


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


items = [5, 3, 2, 4, 1, 7, 11, 32, 12, 9, 8, 0]
print(linear_search(items, 10))


