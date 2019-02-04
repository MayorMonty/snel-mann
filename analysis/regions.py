# Finds suspcious regions in a file by comparing the Chi Squares of halfs

import distribution

""" Recursively searches through text and finds regions with strange Chi Sqaure Distributions """
def unusal(string, chi_threshold = None):
    first, second = string[:len(string)//2], string[len(string)//2:]

    index, chi = distribution.compare(first, second)

    if chi_threshold is None:
        chi_threshold = distribution.chi_square((18 * 1000) / 127, distribution.frequency(string))


    if chi > chi_threshold / 4:
        return unusal([first, second][index], chi_threshold * 2)
    else:
        return [first, second][index]



