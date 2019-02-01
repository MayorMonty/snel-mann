# Finds the character distribution of a file

"""Returns a list of the frequencies of each character by ASCII code"""
def frequency(string):
    dist = [0] * 127

    for char in string:
        dist[ord(char)] += 1
    
    return dist

def chi_square(expected, distribution):
    total = 0

    for number in distribution:
        total += ((number - expected) ** 2) / expected
    
    return total