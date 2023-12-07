"""
Puzzle 1: You have n cards with two lists of integers per card. Identify how many integers appear simultaneously in both lists,
then take 1 * 2 ^ (n_matches - 1).

Puzzle 2: You have the same n cards as before. This time, you instead win copies of scratchcards 
below the winning card equal to the number of matches. Copies of scratch cards count towards the number
of scratch cards you have.
"""

from tqdm import tqdm


def parse_card(numbers):
    winning_numbers, play_numbers = numbers.split("|")
    winning_numbers = winning_numbers.strip().split()
    play_numbers = play_numbers.strip().split()
    overlap = set(winning_numbers).intersection(play_numbers)
    return overlap


if __name__ == "__main__":
    # Rad puzzle input
    with open("./input.txt", "r") as file:
        cards = [card.strip() for card in file.readlines()]

    # Puzzle 1
    points = 0
    for card in cards:
        card_id, numbers = card.split(":")
        winning_numbers, play_numbers = numbers.split("|")
        winning_numbers = winning_numbers.strip().split()
        play_numbers = play_numbers.strip().split()
        overlap = set(winning_numbers).intersection(play_numbers)
        points_i = 2 ** (len(overlap) - 1) if overlap else 0

        print(f"{card} --> {overlap} --> {points_i}")
        points += points_i

    print(f"The solution is: {points}")

    # Puzzle 2
    n_per_card = dict(
        zip(range(1, len(cards) + 1), [1 for _ in cards])
    )  # Number of copies per scratch card

    for card in tqdm(cards):
        card_id, numbers = card.split(":")
        card_id = int(card_id.split()[-1])
        n_copies = n_per_card[card_id]

        # We have n copies of the card
        # For every match in every copy, add 1 card to the `n_matches` subsequent card IDs
        for _ in range(n_copies):
            overlap = parse_card(numbers)
            n_matches = len(overlap)
            for id in range(card_id + 1, card_id + n_matches + 1):
                n_per_card[id] += 1

    # Total number of scratchcards is the solution
    n_cards = sum(n_per_card.values())
    print(f"The solution is: {n_cards}")
