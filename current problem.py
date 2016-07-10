def word_lengths(words):
    """Return the length of words in the input list.

    For example::

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """

    wrd_lngths = []

    for item in words:
        item_length = len(item)
        wrd_lngths.append(item_length)

    print wrd_lngths
    return wrd_lngths

word_lengths(["hello", "hey", "hello", "spam"])