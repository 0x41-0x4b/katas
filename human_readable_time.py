"""
Write a function, wich takes a non-negative integer (seconds) as input and returns the time in a human-readable format(HH:MM:SS)
Hours, padded to 2 digits, range: 00-99
Minutes, padded to 2 digitrs, range: 00-59
Seconds, padded to 2 digits, range: 00-59
The maximum time never exceeds 359999 (99:59:59)
"""
def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(seconds / 3600, seconds / 60 % 60, seconds % 60)
