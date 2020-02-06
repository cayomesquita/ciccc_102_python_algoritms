""" Group Lab 2 (in-class) """
import random


def permutation(word: str):
    """
    Write a recursive function permutation that accepts a string as a parameter
    and outputs all possible rearrangements of the letters in the string.
    The arrangements may be output in any order.
    example)
    permutation("park")
    output: park, pakr, pkar, prak, arpk, aprk, akrp, ...
    :param word: word to permute
    :return: display permutations of a given word
    """
    if len(word) == 2:
        x = [word, (word[1] + word[0])]
        return x
    else:
        list_words = []
        for i in range(0, len(word)):
            y = permutation(word[0:i] + word[i + 1: len(word)])
            for j in y:
                list_words.append(word[i] + j)
        return list_words


def sum_of_dice_recur(dices, desired_sum, combination, solution: set):
    if (dices * 6) < desired_sum or desired_sum < dices:
        return
    if dices == 1:
        new_combination = combination + (desired_sum,)
        solution.add(new_combination)
        return
    for _ in range(dices):
        for num in range(1, 7):
            rest = desired_sum - num
            new_combination = combination + (num,)
            sum_of_dice_recur(dices - 1, rest, new_combination, solution)


def sum_of_dice(dice: int, desired_sum: int):
    """
    Prints all possible outcomes of rolling the given number of six-sided dice
    that add up to the given desired sum, in {#, #, #} format.

    :param dice: the number of dice
    :param desired_sum: desired sum
    :return: display all possible ways
    example)
    sum_of_dice(2, 7)
    output: {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1}
    """
    solution = set([])
    sum_of_dice_recur(dice, desired_sum, (), solution)
    print(solution)
