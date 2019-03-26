# Finds the character distribution of a file

"""Returns a list of the frequencies of each character by ASCII code"""
def frequency(string):
    dist = [0] * 127

    for char in string:
        dist[ord(char)] += 1
    
    return dist

"""Find the Chi Square of a Distribution"""
def chi_square(expected, distribution):
    total = 0

    for number in distribution:
        total += ((number - expected) ** 2) / expected
    
    return total

"""Compares two strings of text and returns the one with the lower Chi Square. Returns a tuple and with the index the Chi Square"""
def compare(a, b, expected = (18 * 1000) / 127):
    a_chi = chi_square(expected, frequency(a))
    b_chi = chi_square(expected, frequency(b))

    return (0 if a_chi > b_chi else 1, max([a_chi, b_chi]))
