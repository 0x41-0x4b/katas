"""
Write a function that takes a string input, and returns the first character that is not repeated anywhere in the string.
"""
def first_non_repeating_letter(string):
    if string == '' or string is None:
        return ''
    else:
        result = False
        for letter in string:
            if string.lower().count(letter.lower()) == 1:
                return letter
        if not result:
            return ''
