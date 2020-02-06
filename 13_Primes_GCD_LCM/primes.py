import math


def naive_is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Exercise
# Gerenate a list of primes ( from 2 to 100,000)
def generate_prime_list(n):
    """ Generate a list of primes from 2 to n"""
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# print(generate_prime_list(20))
print(generate_prime_list(100000))