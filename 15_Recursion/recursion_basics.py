def print_stars(n):
    for _ in range(n):
        print("*", end="")


def print_stars_recur(n):
    if n > 0:
        print_stars(n - 1)
        print("*", end="")


def factorial(n):
    sum = 1
    for num in range(2, n + 1):
        sum *= num
    return sum


def factorial_recur(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recur(n - 1)


def fibonacci(n):
    """
    Returns fibonacci of n (iteratively)
    1, 1, 2, 3, 5, 8, 13, 21, ..., nth
    :param n:
    :return:
    """
    a = 1
    b = 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fibonacci_recur(n):
    """
    Returns fibonacci of n (recursively)
    1, 1, 2, 3, 5, 8, 13, 21, ..., nth
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def power(base, n):
    """
    Returns base to the power of n (iteratively)
    :param n:
    :return:
    """
    result = 1
    for _ in range(n):
        result *= base
    return result


def power_recur(base, n):
    """
    Returns base to the power of n (recusrsively)
    :param n:
    :return:
    """
    return 1 if n == 0 else base * power_recur(base, n - 1)

