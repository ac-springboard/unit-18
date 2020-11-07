def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    l1 = list(str(num1))
    l2 = list(str(num2))
    l1.sort()
    l2.sort()
    return l1 == l2
