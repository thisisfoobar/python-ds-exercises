def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check(["nah", [1], "nope"])
        False
    """
    val = True
    for item in lst:
        if not isinstance(item,list):
            val = False
    return val