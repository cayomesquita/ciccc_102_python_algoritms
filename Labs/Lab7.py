""" Recursion """


# Palindrome is a word, phrase, or sequence that reads the same
# backward as forward.

# Examples)
# is_palindrome(madam) -> True
# is_palindrome(racecar) -> True
# is_palindrome(pizza) -> False


def is_palindrome(word):
    """
    Check if a given string input (word) is a palindrome.
    You must write your solution recursively. (no loops)
    :param word: string input
    :return: True if word is palindrome, otherwise False
    """
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    return False
