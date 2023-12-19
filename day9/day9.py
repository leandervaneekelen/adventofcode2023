"""
Puzzle #1: given a list of integers, extrapolate the next integer value. The sum of all extrapolated integers
is the puzzle solution. Extrapolation happens by recursively calculating the difference between each position
until you reach zero, then back-inferring up to the to-be-extrapolated value.

Puzzle #2: do the same thing, but for the first value instead (i.e. calculate the left diagonal).
"""

import numpy as np

if __name__ == "__main__":
    # Read puzzle input
    with open("./input.txt", "r") as file:
        lines = [[int(n) for n in line.strip().split()] for line in file]

    extrapolated_values_forward = []
    extrapolated_values_backward = []
    for line in lines:
        # Calculate diffs
        line = np.array(line)
        diffs = []
        n = 0
        while (diff := np.diff(line, n=n)).any():
            n += 1
            diffs.append(diff)

        # Part ##1: forward diagonal

        # Backfill diagonal
        forward_diagonal = [diffs[-1][-1]]
        for n_ in reversed(range(n - 1)):
            diagonal_i = forward_diagonal[-1] + diffs[n_][-1]
            forward_diagonal.append(diagonal_i)

        extrapolated_value = forward_diagonal[-1]
        extrapolated_values_forward.append(extrapolated_value)

        ## Part 2: backward diagonal
        backwards_diagonal = [diffs[-1][0]]
        for n_ in reversed(range(n - 1)):
            diagonal_i = diffs[n_][0] - backwards_diagonal[-1]
            backwards_diagonal.append(diagonal_i)

        extrapolated_value = backwards_diagonal[-1]
        extrapolated_values_backward.append(extrapolated_value)

    print(f"The solution of puzzle #1 is: {sum(extrapolated_values_forward)}")
    print(f"The solution of puzzle #2 is: {sum(extrapolated_values_backward)}")
