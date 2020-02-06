"""
 String, List - Level 2.0
"""


def count_hi(string):
    """
    Return the number of times that the string "hi" appears anywhere in the given string.
    """
    return str(string).count("hi") if len(string) > 0 else 0


def cat_dog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat_counter = 0
    dog_counter = 0
    if len(string) >= 3:
        aux = str(string)
        cat_counter = aux.count("cat")
        dog_counter = aux.count("dog")
    return cat_counter == dog_counter


def count_code(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except it'll accept any letter for the 'd', so 'cope' and 'cooe' count.
    """
    aux = str(string)
    sum = 0
    index = 0
    try:
        while index + 3 < len(aux):
            index = aux.index("co", index)
            if aux[index + 2].isalpha() and aux[index + 3] == "e":
                sum += 1
            index += 2
    finally:
        return sum


def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string,
    ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.
    """
    a = str.lower(a)
    b = str.lower(b)
    try:
        if len(a) > len(b):
            if a.rindex(b) + len(b) == len(a):
                return True
        else:
            if b.rindex(a) + len(a) == len(b):
                return True
    except ValueError as e:
        return False
    return False


def count_evens(nums):
    """
    Return the number of even ints in the given list.
    Note: the % 'mod' operator computes the remainder, e.g. 5 % 2 is 1.
    """
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += 1
    return sum


def big_diff(nums):
    """
    Given a list length 1 or more of ints, return the difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
    """
    minimum = nums[0]
    maximum = nums[0]
    for index in range(1, len(nums)):
        minimum = min(nums[index], minimum)
        maximum = max(nums[index], maximum)
    return maximum - minimum


def sum13(nums):
    """
    Return the sum of the numbers in the list, returning 0 for an empty array.
    Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
    """
    sum = 0
    index = 0
    while index < len(nums):
        if nums[index] == 13:
            index += 2
            continue
        sum += nums[index]
        index += 1
    return sum


def sum67(nums):
    """
    Return the sum of the numbers in the list, except ignore sections of numbers starting with a 6
    and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
    """
    sum = 0
    count_flag = True
    for num in nums:
        if (count_flag and num == 6) or (not count_flag and num == 7):
            count_flag = not count_flag
            continue
        if count_flag:
            sum += num
    return sum


def has22(nums):
    """
    Given a list of ints, return True if the array contains a 2 next to a 2 somewhere.
    """
    two_flag = False
    for num in nums:
        if num == 2 and two_flag:
            return True
        two_flag = num == 2
    return False
