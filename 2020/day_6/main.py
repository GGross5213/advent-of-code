from typing import Set
from functools import reduce


def part_1(data: str):
    # Basically turn each group into a set of characters
    # Sets can't have any duplicates so you get all unique answers
    # Then take the length of the set
    unique_answer_cnt_per_group = [
        len({c for p in group.split("\n") for c in p}) for group in data.split("\n\n")
    ]

    sum_of_counts = sum(unique_answer_cnt_per_group)

    print("Part 1: ", sum_of_counts)


def part_2(data: str):
    def set_intersection(x: Set[str], y: Set[str]) -> Set[str]:
        return x & y

    # Basically turn each set of answers for each person into a group into a Set.
    # Then reduce all answers for a group into a single set by finding the intersection of them all
    # So now we are left with a set that has all common answers. Take the length.
    # Now we have a list of the lenght of each set of common answers for every group
    # We can just take the sum of the list
    total = sum(
        [
            len(reduce(set_intersection, [{c for c in p} for p in group.split("\n")]))
            for group in data.split("\n\n")
        ]
    )
    print("Part 2: ", total)


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()