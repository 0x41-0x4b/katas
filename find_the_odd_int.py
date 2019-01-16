"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears and odd number of times.
"""
def find_int(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
