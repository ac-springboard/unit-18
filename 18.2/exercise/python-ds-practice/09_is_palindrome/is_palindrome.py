def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    original = list(phrase.lower().replace(' ', ''))
    oricopy = original.copy()
    oricopy.reverse()

    # print('1', phrase)
    # print('2', original)
    # print('3', oricopy)

    return original == oricopy


# print(is_palindrome('tenet'))
# print(is_palindrome('minoa'))
# print(is_palindrome('ralar'))
