"""
Puzzle 1: determine the product of the number of ways you can win each race.
Each way represents a number of seconds you can hold the button of your boat to let it speed up.

# Puzzle 2: just kidding, there's only one race. Concatenate all of the separate integers into one
big number and see how many winning combinations there are now.
"""

import numpy as np


def solve_race(available_time, distance_to_beat):
    speeds = np.arange(available_time + 1)
    time_left = available_time - speeds
    distances = np.multiply(speeds, time_left)
    winning_times = speeds[distances > distance_to_beat]
    n_winning_combinations = len(winning_times)
    return n_winning_combinations


if __name__ == "__main__":
    # Read puzzle input
    with open("./input.txt", "r") as file:
        sheet = file.readlines()
    times, distances = sheet
    times = [int(time) for time in times.split()[1:]]
    distances = [int(distance) for distance in distances.split()[1:]]

    # Calculate for every race what duration of holding the button would result
    # in winning the race
    n_winning_combinations = []
    for time, distance in zip(times, distances):
        n_winning_combinations_i = solve_race(time, distance)
        n_winning_combinations.append(n_winning_combinations_i)
    print(f"The solution of part 1 is: {np.product(n_winning_combinations)}")

    # Part 2 - one big number
    available_time = int("".join(str(n) for n in times))
    distance_to_beat = int("".join(str(n) for n in distances))
    n_winning_combinations = solve_race(available_time, distance_to_beat)
    print(f"The solution of part 2 is: {n_winning_combinations}")
