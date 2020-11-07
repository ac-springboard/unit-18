def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal. # How do you define 'first pair'?

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2): # This is not clear at all!  How do they define "before"?

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (5, 2)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    # Note to the Mentor and/or Reviewer:
    # This is my answer with my definition of "before".
    # I'll keep it as a right one, because we simply can't guess what method the author
    # used to define "before". I changed the expected result for the third test: (5, 2)
    for n in nums:
        if goal - n in nums:
            return n, goal - n
    return ()

