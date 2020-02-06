""" Sorting Practice Problems """


# Write a program that sorts the first half of a list in ascending order
# and the second half in descending order.

# e.g. alist = [8, 1, 7, 5, 2, 4, 2, 9, 3, 6] the alist should be
# changed to [1, 2, 5, 7, 8, 9, 6, 4, 3, 2]. This should work for other lists of course.


def sort_half(alist):
    if len(alist) < 2:
        return alist

    half = len(alist) // 2

    a = list(alist)[:half]
    b = list(alist)[half:]

    a.sort(reverse=False)
    b.sort(reverse=True)
    return a + b


# Suppose two lists A and B have already been sorted.
# Elements of A have been sorted into ascending order and
# B has also been sorted in ascending order. Write a Python
# program to merge the elements of A and B into a list.
# At the end of the program the result list will contain
# all the elements of A and B in ascending order.


def merge_two(A, B):
    l = []
    index_a = 0
    index_b = 0

    while index_a < len(A) and index_b < len(B):
        if A[index_a] < B[index_b]:
            l.append(A[index_a])
            index_a += 1
        else:
            l.append(B[index_b])
            index_b += 1
    l += A[index_a:]
    l += B[index_b:]
    return l


# Write a program to replace all negative values in a list
# called mylist with zeros. So, if mylist = [2, 5, -1, 3, 7, -2, 8],
# then mylist should be changed to [2, 5, 0, 3, 7, 0, 8]. This
# should of course work for other lists.


def replace_negative(mylist):
    for index in range(len(mylist)):
        if mylist[index] < 0:
            mylist[index] = 0
    return mylist
