def mrange(start, end=10, steps=1):
    """

    :param start:
    :param end:
    :param steps:
    :return:
    """
    num = start
    list = []
    while num < end:
        list += [num]
        num += steps;
    return list


print(mrange(1, 10))
print(mrange(1, 10, 2))


# n: args
def xrange(*args):
    if len(args) == 1:
        return mrange(0, args[0])
    if len(args) <= 3:
        return mrange(*args)
    else:
        raise TypeError("Invalid Number of arguments!")


print(xrange(1, 5, 2))
print(xrange(1, 8))
print(xrange(15))


def nooone(i=1):
    if i > 10:
        return i


print(nooone())
print(type(nooone()))
