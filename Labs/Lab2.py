"""
Basic python list problems -- no loops.
"""


def first_last6(nums):
    """
    Given a list of ints, return True if 6 appears as either the first or last element in the list.
    The list will be length 1 or more.
    """
    return nums[0] == 6 or 6 == nums[len(nums) - 1]


def same_first_last(nums):
    """
    Given a list of ints, return True if the list is length 1 or more, and the first element
    and the last element are equal.
    """
    length = len(nums)
    return length >= 1 and nums[0] == nums[length - 1]


def common_end(a, b):
    """
    Given 2 lists of ints, a and b, return True if they have the same first element or they have the same last element.
    Both lists will be length 1 or more.
    """
    return a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]


def sum3(nums):
    """
    Given a list of ints length 3, return the sum of all the elements.
    """
    sum = 0
    for num in nums:
        sum += num
    return sum


def rotate_left3(nums):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    """
    num_list = list(nums)
    num_list.append(num_list.pop(0))
    return num_list


def reverse3(nums):
    """
    Given a list of ints length 3, return a new list with the elements in reverse order,
    so {1, 2, 3} becomes {3, 2, 1}.
    """
    # new_list = []
    # for num in nums:
    #     new_list.insert(0, num)
    # return new_list
    return nums[::-1]


def max_ends3(nums):
    """
    Given a list of ints length 3, figure out which is larger, the first or last element in the list,
    and set all the other elements to be that value. Return the changed list.
    """
    # largest = nums[len(nums) - 1]
    # if nums[0] > largest:
    #     largest = nums[0]
    # i = 0
    # for _ in nums:
    #     nums[i] = largest
    #     i += 1
    # return nums
    return [nums[0]] * 3 if nums[0] > nums[1] else [nums[-1]] * 3


def make_ends(nums):
    """
    Given a list of ints, return a new list length 2 containing the first and last elements from the original list.
    The original list will be length 1 or more.
    """
    return [nums[0], nums[len(nums) - 1]]


def has23(nums):
    """
    Given an int list length 2, return True if it contains a 2 or a 3.
    """
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False
