"""
Puzzle 1: extract the first and the last occurence of an integer from a list of strings.
In the case of only one integer, the first and last occurence are the same.

Puzzle 2: the integers can now also be spelled as words. The options are
"one, two, three, four, five, six, seven, eight, and nine"
"""

from copy import deepcopy
import re

if __name__ == "__main__":
    # Read puzzle input
    input_file = "./input.txt"
    with open(input_file, "r") as f:
        input_list = f.readlines()
        input_list = [l.strip() for l in input_list]

    ## Puzzle 1

    # Get first and last occurence of ints in string
    ints = []
    for input in input_list:
        if matches := re.findall("\d", input):
            first, last = matches[0], matches[-1]
            number = int(f"{first}{last}")
            ints.append(number)

    # # Add all ints
    calibration_value = sum(ints)
    print(f"The calibration result is {calibration_value}.")

    ## Puzzle 2

    # Make lookup table for words 2 ints
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    lookup = {}
    word_int_lookup = dict(zip(words, range(1, 10)))
    int_int_lookup = dict(
        zip((str(i) for i in range(1, 10)), range(1, 10))
    )  # Lookup table has to map both 1 -> 1 and 'one' -> 1
    lookup.update(word_int_lookup)
    lookup.update(int_int_lookup)

    # Get first and last occurence of ints in string
    ints = []
    all_options = deepcopy(words)
    all_options.append(r"\d")
    filter = "|".join(all_options)
    filter = rf"(?=({filter}))"  # Positive look ahead assertion that deals with overlapping words such as 'sevenine' -> (7, 9)
    for input in input_list:
        if matches := re.findall(filter, input):
            first, last = lookup[matches[0]], lookup[matches[-1]]
            number = int(f"{first}{last}")
            ints.append(number)

    # Add all ints
    calibration_value = sum(ints)
    print(f"The calibration result is {calibration_value}.")
