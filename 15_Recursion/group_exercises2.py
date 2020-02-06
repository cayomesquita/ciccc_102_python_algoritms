""" group exercises 2 """

# Write a recursive function printBinary that accepts integer and
# prints that number's representation in binary (base 2)
#
# Examples:
# print_binary(2)    prints 10
# print_binary(7)    prints 111
# print_binary(12)   prints 1100    return str(print_binary(num // 2)) + str(num % 2)
# print_binary(42)   prints 101010
# print_binary(-500) prints -111110100
import operator


def print_binary(num) -> str:
    if num < 0:
        return "-" + str(print_binary(-num))
    if num == 0:
        return 0;
    if num == 1:
        return 1
    return print_binary(num // 2) + str(num % 2)


# Write a recursive function evaluate that accepts a string
# representing a math expression and computes its value.
# - The expression will be "fully parenthesized" and will
#   consist of + and * on single-digit integers only.
# - You can use a helper function. (Do not change the original function header)
# - Recursion
#
# evaluate("7")                 -> 7
# evaluate("(2+2)"              -> 4
# evaluate("(1+(2*4))"          -> 9
# evaluate("((1+3)+((1+2)*5))") -> 19
def operator_at(expr) -> int:
    """
    return the index of the operator according with the exemple term_operator_term. if it can not find, it returns expr length
    :param expr:
    :return:
    """
    if expr[0] != "(":
        return 1
    if expr[-1] != ")":
        return -2
    index = 0
    stack = [expr[index]]
    index += 1
    while len(stack) > 0:
        if expr[index] == "(":
            stack.append("(")
        if expr[index] == ")":
            stack.pop()
        index += 1
    return index


def evaluate(expr):
    if len(expr) == 1:  # term
        return expr
    else:  # (expr) or term_OPERATOR_term
        index_operator = operator_at(expr)
        if index_operator == len(expr):  # (expr) case
            return evaluate(expr[1:-1])
        # term_OPERATOR_term case
        term_1 = int(evaluate(expr[:index_operator]))
        term_operator = operator.add if expr[index_operator] == "+" else operator.mul
        term_2 = int(evaluate(expr[index_operator + 1:]))
        return term_operator(term_1, term_2)


# Write a recursive function that accepts an integer number of digits
# and prints all base-10 numbers that have exactly that many digits, in
# ascending order, one per line.
#
# print_decimal(1)  prints from 0 to 9  (single digit)
# print_decimal(2)  prints from 10 to 99 (two digits)
# print_decimal(3)  prints from 100 to 999 (three digits)
def print_decimal_recur(length, num):
    if len(str(num)) == length:
        print(num)
        print_decimal_recur(length, num + 1)


def print_decimal_recur2(num):
    print(num)
    next_num = num + 1
    if len(str(next_num)) == len(str(num)):
        print_decimal_recur2(next_num)


def print_decimal_recur3(digits, string):

    pass


def print_decimal(digits):
    print_decimal_recur(digits, 10 ** (digits - 1))
    # print_decimal_recur2(10 ** (digits - 1))
    print_decimal_recur3(digits,"")
    pass
