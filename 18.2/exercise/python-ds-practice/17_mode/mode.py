def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    mde = float("-inf")
    # This is to avoid to count the same number several times
    nus = set(nums)
    for n in nus:
        mde = n if nums.count(n) > mde else mde
    return mde
