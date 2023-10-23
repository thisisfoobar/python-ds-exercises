def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    vowels_in_phrase = {}
    for letter in phrase:
        lower_letter = letter.lower()
        if lower_letter in vowels:
            if lower_letter in vowels_in_phrase.keys():
                vowels_in_phrase[lower_letter] += 1
            else:
                vowels_in_phrase[lower_letter] = 1
    return vowels_in_phrase