"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased.
The indexind just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.
"""
def to_weird_case(string):
    return ''.join([letter.upper() if index % 2 == 0 else letter for index, letter in enumerate(string)])
