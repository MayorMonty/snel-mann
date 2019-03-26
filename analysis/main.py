# Glue file for data analysis
# Will first scan data/ and find Chi-squared values of the distribution

import os
import numpy as np

import sys

import logging

import statistic
import distribution
import regions

import time


logging.basicConfig(filename='output.log',level=logging.DEBUG)

# ls files
files = os.listdir("text_files")

# Expected value for Chi Square
EXPECTED = (18 * 1000) / 127

# Stores Chi Square values for each file and file contents
dataset = [0] * len(files)
contents = [""] * len(files)

print("Searching through files...")

# Iterate through each file in the directory
for index, filename in enumerate(files):
    print(" Scanning {}...".format(filename))
    data = open("text_files/" + filename, "r").read()

    # Save file contents for later
    contents[index] = data

    # Get character distribution & calculate Chi Square
    freq = distribution.frequency(data)
    dataset[index] = distribution.chi_square(EXPECTED, freq)

print("Done\n\n")

# Calculate the five number summary using numpy
quarts = np.percentile(dataset, [25, 50, 75])

print("Chi Square Distribution of Characters -- Five Number Summary")
print(" MIN = {} ({})".format(min(dataset), files[dataset.index(min(dataset))]))
print(" Q1 = {}".format(quarts[0]))
print(" Q2 = {}".format(quarts[1]))
print(" Q3 = {}".format(quarts[2]))
print(" MAX = {} ({})".format(max(dataset), files[dataset.index(max(dataset))]))

print("\n")


# Find outliers
print("Outliers")
outliers = statistic.outliers(dataset, 10, 90)

if len(outliers[0]) < 1:
    print(" NONE")

    print("\nNo usual files found.")
    sys.exit(0)

for i in outliers[0]:
    print(" {} (χ² = {})".format(files[i], dataset[i]))


print("\nFinding usual regions of outlier files...")

for i in outliers[0]:
    strange = regions.unusal(contents[i])

    print("\n")

    print("{}".format(files[i]))
    print("{}".format(strange))

    logging.debug("{}, {}, {}".format(files[i], dataset[i], strange)) 
