def naive_selection_sort(items):
    steps = 0
    for pivot in range(len(items)):
        index_minimum = pivot
        for index in range(pivot, len(items)):
            steps += 1
            if items[index] < items[index_minimum]:
                index_minimum = index
        items[pivot], items[index_minimum] = items[index_minimum], items[pivot]
    print(steps)
    return items

def selection_sort(items):
    steps = 0
    for pivot in range(len(items) - 1):
        index_minimum = pivot
        for index in range(pivot + 1, len(items)):
            steps += 1
            if items[index] < items[index_minimum]:
                index_minimum = index
        if index_minimum != pivot:
            items[pivot], items[index_minimum] = items[index_minimum], items[pivot]
    print(steps)
    return items

items = [5, 2, 1, 4, 3]

print(naive_selection_sort(items))
print(selection_sort(items))
