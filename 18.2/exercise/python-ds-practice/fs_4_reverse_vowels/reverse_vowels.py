def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    phrase = list(s)
    positions_map = [i for i, c in enumerate(phrase, 0) if c.casefold() in 'aeiou'.casefold()]
    positions_inv = positions_map[::-1]
    for i, n in enumerate(positions_map, 0):
        inv_position = positions_inv[i]
        phrase[n] = s[inv_position:inv_position + 1]
    return ''.join(phrase)
