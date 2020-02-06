# Binary Search
# - "sorted" list of data
# - Keep comparing the item in the middle of the list to the target value
#   while removing the half of the list from the search range.
#
# - Time Complexity: O(log n)
#   (In the worst case, it will take log n steps if you have n elements)


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


countries = ["Australia", "Brazil", "Canada", "Denmark", "Ecuador",
             "France", "Germany", "Hungary", "Italy", "Japan",
             "Korea", "Latvia", "Malaysia", "New Zealand", "Oman",
             "Poland", "Qatar", "Russia", "Slovakia", "Turkey",
             "Uruguay", "Vietnam", "Wales", "Yemen", "Zambia"]


print(binary_search(countries, "Slovakia"))

