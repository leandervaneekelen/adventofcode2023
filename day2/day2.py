"""
Puzzle 1: there is a bag containing 12 red cubes, 13 green cubes, and 14 blue cubes. Each game 
consists of a list of multiple independent random samples from that bag. Some games
contain samples that are impossible (e.g. 15 blue cubes sampled). Which games are possible
and what is the sum of the IDs of those games? 

Puzzle 2: what is the maximum number of cubes observed for each color in each game?
(e.g. 12 red, 3 blue, 1 green; 11 green, 2 red, 4 blue -> [12, 11, 4])
The 'power' of a game is the product of this [r,g,b] tuple.
What is the sum of all powers?
"""

from typing import List, Dict
import re
import numpy as np

COLORS = ["red", "green", "blue"]


def parse_sample(sample: str) -> List[int]:
    """
    Return a list of n occurences of red, green and blue cubes from a sample.
    For multiple observations of the same cube colors within one sample (e.g. 5 blue, 10 blue),
    take the observation with the highest count (10 blue).
    """

    occurences = [0, 0, 0]
    observations = sample.split(",")
    for obs in observations:
        obs = obs.strip()
        for i, color in enumerate(COLORS):
            if match := re.match(rf"(\d{{1,2}})\s{color}", obs):
                n = int(match.group(1))
                occurences[i] = max(occurences[i], n)
                break
    return occurences


def possible_sample(sack_content: List[int], sample: List[int]) -> bool:
    """
    Check if any of the color occurences in the sample exceeds the sack content.
    Returns False if the sample has more cubes than the sack's content
    (e.g. 10 blue observed in a sack with 5 blue cubes -> False).
    """

    for content, observation in zip(sack_content, sample):
        if observation > content:
            return False
    return True


if __name__ == "__main__":
    # Read puzzle input
    with open("./input.txt", "r") as f:
        games = [l.strip() for l in f.readlines()]

    # Puzzle 1

    SACK_CONTENT = [12, 13, 14]  # rgb

    # Find games where all samples are possible
    possible_games = []
    for game in games:
        id, samples = game.split(":")
        id = int(id.split(" ")[-1])  # 'Game 1' -> 1
        samples = samples.split(";")
        samples = [parse_sample(sample) for sample in samples]
        if all(possible_sample(SACK_CONTENT, sample) for sample in samples):
            possible_games.append(id)

    # Sum ID of possible games
    sum_of_ids = sum(possible_games)
    print(f"The sum of the IDs is {sum_of_ids}!")

    # Puzzle 2
    powers = []
    for game in games:
        id, samples = game.split(":")
        samples = samples.split(";")
        samples = [parse_sample(sample) for sample in samples]
        max_occurences = np.stack(samples, axis=0).max(axis=0)
        power = np.product(max_occurences)
        powers.append(power)
    sum_of_powers = sum(powers)
    print(f"The sum of the powers of all games is {sum_of_powers}")
