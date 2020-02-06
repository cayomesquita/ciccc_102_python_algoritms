# Bubble Sort
# - Time Complexity: O(n²)
#
# For each scan,
#     For each comparison (two adjacent items),
#         if left item > right tiem:
#                 "swap" two items

def bubble_sort_while(items):
    limit = len(items) - 1
    step = 0
    while limit > 0:
        swap = False
        for index in range(limit):
            next_index = index + 1
            if items[index] > items[next_index]:
                items[index], items[next_index] = items[next_index], items[index]
                swap = True
            step += 1
        if not swap:
            break
        limit -= 1
    print(step)
    return items


def naive_bubble_sort(items):
    step = 0
    for scan in range(len(items)):
        swap = False
        for index in range(len(items) - 1):
            next_index = index + 1
            if items[index] > items[next_index]:
                items[index], items[next_index] = items[next_index], items[index]
                swap = True
            step += 1
        if not swap:
            break
    print(step)
    return items

def bubble_sort(items):
    step = 0
    for scan in range(len(items)):
        swap = False
        for index in range(len(items) - 1 - scan):
            next_index = index + 1
            if items[index] > items[next_index]:
                items[index], items[next_index] = items[next_index], items[index]
                swap = True
            step += 1
        if not swap:
            break
    print(step)
    return items

items = [5, 2, 1, 4, 3]

print(bubble_sort_while(items))
