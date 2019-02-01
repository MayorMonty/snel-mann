# Glue file for data analysis
# Will first scan data/ and find Chi-squared values of the distribution

import os
import distribution

from numpy import percentile

files = os.listdir("data")

# Expected value for Chi Square
EXPECTED = (18 * 1000) / 127

# Stores Chi Square values for each file
dataset = [0] * len(files)

print("Searching through files...")

# Iterate through each file in the directory
for index, filename in enumerate(files):
    print(" Scanning {}...".format(filename))
    data = open("data/" + filename, "r").read()

    # Get character distribution & calculate Chi Square
    freq = distribution.frequency(data)
    dataset[index] = distribution.chi_square(EXPECTED, freq)

print("Done\n\n")

# Calculate the five number summary using numpy
quarts = percentile(dataset, [25, 50, 75])

print("Chi Square Distribution of Characters -- Five Number Summary")
print("MIN = {} ({})".format(min(dataset), files[dataset.index(min(dataset))]))
print("Q1 = {}".format(quarts[0]))
print("Q2 = {}".format(quarts[1]))
print("Q3 = {}".format(quarts[2]))
print("MAX = {} ({})".format(max(dataset), files[dataset.index(max(dataset))]))

print("\n")

# Find outliers
print("Outliers")