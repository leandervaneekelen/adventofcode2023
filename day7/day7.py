"""
Puzzle #1: For n poker hands, determine the rank of each hand (a higher rank being better, i.e. the nth ranking
poker hand is the best). Each hand has a bid; calculate the product sum of the poker hands rank and their bid.
The rank is based on poker hands (five of a kind, four of a kind, etc). Ties are broken on based on 
the value of the first card (highest wins), or the second card in case that ties, or the third card, etc...

Puzzle #2: the `J` cards now count as jokers and can pretend to be whatever card is best for the purpose of 
determining hand type. E.g. `QJJQ2` is now a four of a kind. This effectively means we add the joker count
to the most occuring card other than the joker itself.

"""

from collections import Counter
from functools import cmp_to_key
import numpy as np

# Poker hand types
FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

# Relative card strengths
CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
RELATIVE_CARD_STRENGHTS = dict(zip(CARDS, reversed(range(len(CARDS)))))
CARDS_WITH_JOKERS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
RELATIVE_CARD_STRENGHTS_WITH_JOKERS = dict(
    zip(CARDS_WITH_JOKERS, reversed(range(len(CARDS_WITH_JOKERS))))
)


def hand_type(hand, joker=False):
    counts = count_with_joker(hand) if joker else Counter(hand)
    occurences = [i[-1] for i in counts.most_common()]
    if occurences == [5]:
        return FIVE_OF_A_KIND
    elif occurences == [3, 2]:
        return FULL_HOUSE
    elif occurences == [4, 1]:
        return FOUR_OF_A_KIND
    elif occurences == [3, 1, 1]:
        return THREE_OF_A_KIND
    elif occurences == [2, 2, 1]:
        return TWO_PAIR
    elif occurences == [2, 1, 1, 1]:
        return ONE_PAIR
    else:
        return HIGH_CARD


def count_with_joker(hand):
    counts_without_jokers = Counter(hand.replace("J", ""))
    counts_with_jokers = Counter(hand)
    if counts_with_jokers["J"] == 5:
        return (
            counts_with_jokers  # Edge case where we have all jokers (five of a kind!)
        )
    most_occuring_card, _ = counts_without_jokers.most_common()[0]
    joker_count = counts_with_jokers["J"]
    counts_without_jokers[most_occuring_card] += joker_count
    return counts_without_jokers


def compare_hands(hand1, hand2, joker=False):
    type1 = hand_type(hand1, joker)
    type2 = hand_type(hand2, joker)
    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1
    else:  # In case of ties, first strongest card wins
        relative_strength = (
            RELATIVE_CARD_STRENGHTS_WITH_JOKERS if joker else RELATIVE_CARD_STRENGHTS
        )
        for i, j in zip(hand1, hand2):
            strength_i = relative_strength[i]
            strength_j = relative_strength[j]
            if strength_i > strength_j:
                return 1
            elif strength_i < strength_j:
                return -1
        return 0  # Equal hands


if __name__ == "__main__":
    # Read puzzle input
    with open("./input.txt", "r") as file:
        hands_and_bids = [line.strip().split() for line in file.readlines()]

    sort_func = lambda x: cmp_to_key(compare_hands)(x[0])
    hands_and_bids = sorted(hands_and_bids, key=sort_func)
    sorted_bids = np.array([bid for _, bid in hands_and_bids]).astype(int)
    total_winnings = np.dot(sorted_bids, np.arange(1, len(sorted_bids) + 1))
    print(f"The solution for puzzle #1 is {total_winnings}")

    sort_func = lambda x: cmp_to_key(lambda a, b: compare_hands(a, b, joker=True))(x[0])
    hands_and_bids = sorted(hands_and_bids, key=sort_func)
    sorted_bids = np.array([bid for _, bid in hands_and_bids]).astype(int)
    total_winnings = np.dot(sorted_bids, np.arange(1, len(sorted_bids) + 1))
    print(f"The solution for puzzle #1 is {total_winnings}")
