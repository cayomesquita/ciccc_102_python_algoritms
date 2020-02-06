""" Primes, GCD, LCM """
import math


def is_prime(n):
    """ Check if n is prime """
    if n > 1:
        for num in range(2, int(math.sqrt(n)) + 1):
            if n % num == 0:
                return False
    if n == 1:
        return False
    return True


def gcd(a, b):
    """ GCD of a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def lcm(a, b):
    """ LCM of a and b """
    return (a * b) / gcd(a, b)


def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes
