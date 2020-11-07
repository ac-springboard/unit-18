def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # result = {}
    # for lettr in phrase:
    #     result[lettr] = phrase.count(lettr)
    # return result

    return {lettr: phrase.count(lettr) for lettr in phrase}


print(multiple_letter_count("YouTube or not YouTube. That's the question!"))
