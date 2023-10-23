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

    vowels = set('aeiou')
    lst = list(s)

    i = 0
    j = len(lst) - 1

    while i < j:
        if lst[i].lower() not in vowels:
            i += 1
        elif lst[j].lower() not in vowels:
            j -= 1
        else:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    
    return "".join(lst)