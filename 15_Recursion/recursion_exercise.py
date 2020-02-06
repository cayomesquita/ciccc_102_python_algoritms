""" Recursion in-class Exercise (7 Problems) """


def bunny_ears(n):
    """
    We have a number of bunnies and each bunny has two big floppy ears.
    We want to compute the total number of ears across all the bunnies recursively
    (without loops or multiplication).

    bunny_ears(0) -> 0
    bunny_ears(1) -> 2
    bunny_ears(2) -> 4
    bunny_ears(3) -> 6
    bunny_ears(50) -> 100
    """
    return 2 + bunny_ears(n - 1) if n > 0 else 0


def count_x(string: str):
    """
    Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

    count_x("xxhixx") -> 4
    count_x("xhixhix") -> 3
    count_x("hi") -> 0
    count_x("x") -> 1
    count_x("") -> 0
    count_x("hihi") -> 0
    """
    if len(string) == 0:
        return 0
    if len(string) == 1:
        return 1 if string == "x" else 0
    half = len(string) // 2
    return count_x(string[:half]) + count_x(string[half:])


def no_x(string: str):
    """
    Given a string, compute recursively a new string where all the 'x' chars have been removed.

    no_x("xaxb") -> "ab"
    no_x("abc") -> "abc"
    no_x("xx") -> ""
    no_x("axxbxx") -> "ab"
    no_x("Hellox") -> "Hello"
    """
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return "" if string == "x" else string

    half = len(string) // 2
    return no_x(string[:half]) + no_x(string[half:])


def array_6(nums, index):
    """
    Given an array of ints, compute recursively if the array contains a 6.
    We'll use the convention of considering only the part of the array that begins at the given index.
    In this way, a recursive call can pass index+1 to move down the array.
    The initial call will pass in index as 0.

    array_6([1, 6, 4], 0) -> True
    array_6([1, 4], 0) -> False
    array_6([6], 0) -> True
    array_6([], 0) -> True
    array_6([1, 9, 4, 6, 6], 0) -> True
    """
    return False if index >= len(nums) else True if nums[index] == 6 else array_6(nums, index + 1)


def all_star(string):
    """
    Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

    all_star("hello") -> "h*e*l*l*o"
    all_star("abc") -> "a*b*c"
    all_star("ab") -> "a*b"
    all_star("3.14") -> "3*.*1*4"
    all_star("a") -> "a"
    all_star("") -> ""
    """
    if len(string) <= 1:
        return string
    half = len(string) // 2
    part_1 = string[:half]
    part_2 = string[half:]
    if part_1[-1] == "*" or part_2[0] == "*":
        return all_star(part_1) + all_star(part_2)
    else:
        return all_star(part_1) + "*" + all_star(part_2)

    # return string[0] + "*" + all_star(string[1:]) if len(string) > 1 else string


def parenthesis_bit(string):
    """
    Given a string that contains a single pair of parenthesis,
    compute recursively a new string made of only of the parenthesis and their contents,
    so "xyz(abc)123" yields "(abc)".

    parenthesis_bit("xyz(abc)123") -> "(abc)"
    parenthesis_bit("x(hello)") -> "(hello)"
    parenthesis_bit("(xy)1") -> "(xy)"
    parenthesis_bit("()") -> "()"
    parenthesis_bit("(x)") -> "(x)"
    parenthesis_bit("res (ipsa) loquitor") -> "(ipsa)"
    parenthesis_bit("hello(not really)there") -> "(not really)"
    """
    if string[0] == "(" and string[-1] == ")":
        return string
    start = 1 if string[0] != "(" else 0
    end = -1 if string[-1] != ")" else len(string)
    return parenthesis_bit(string[start:end])


def str_count(string, sub):
    """
    Given a string and a non-empty substring sub, compute recursively the number of times that
    sub appears in the string, without the sub strings overlapping.

    str_count("catcowcat", "cat") -> 2
    str_count("catcowcat", "cow") -> 1
    str_count("catcowcat", "dog") -> 0
    str_count("xyx", "x") -> 2
    str_count("iiiijj", "i") -> 4
    str_count("iiiijj", "ii") -> 2
    str_count("iiiijj", "jj") -> 1
    str_count("aaabababab", "ab") -> 4
    """
    if len(string) < len(sub):
        return 0
    elif string[:len(sub)] == sub:
        return 1 + str_count(string[len(sub):], sub)
    else:
        return str_count(string[1:], sub)
