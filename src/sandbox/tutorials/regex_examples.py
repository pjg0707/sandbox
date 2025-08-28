"""
Created on Sat Apr  4 12:49:26 2020

@author: Pablo
"""

import re

EXAMPLE_STRING = """
Pablo is 26 years old, Lissy is 25 years old, Dotty is 0 years old,
Cory is 0 years old and Independiente is 115 years old.
"""

# Looks for numbers between 1 and 3 digits
ages = re.findall(r"\d{1,3}", EXAMPLE_STRING)

# Looks for words where the first character is a CAPITAL LETTER.
names = re.findall(r"[A-Z][a-z]*", EXAMPLE_STRING)

print(names)
print(ages)

ageDict = {}  # Creates an empty dictionary
x = 0
for eachName in names:
    # Each name becomes the KEY of the dictionary and
    # the ages become the VALUES.
    ageDict[eachName] = ages[x]
    x += 1

print(ageDict)
