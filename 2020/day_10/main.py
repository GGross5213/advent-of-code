from typing import List, Dict, Tuple


def part_1(adapters: List[int]):
    diff_1 = 0
    diff_3 = 0
    jolt = 0

    for adapter in sorted(adapters):
        diff = adapter - jolt
        if diff == 1:
            diff_1 += 1

        if diff == 3:
            diff_3 += 1

        jolt = adapter

    # One for your device since its 3 higher than highest adapter
    diff_3 += 1

    print("Part 1: ", diff_3 * diff_1)


# Assumes adapters is sorted.
def count_paths(
    adapters: List[int], memoized: Dict[List[int], int]
) -> Tuple[int, Dict[List[int], int]]:
    str_adapters = ",".join([str(a) for a in adapters])
    if str_adapters in memoized:
        return memoized[str_adapters], memoized

    # We have at least one path if we include all following adapters
    path_count = 1
    for index, adapter in enumerate(adapters):
        two = adapters[(index + 2) % len(adapters)]
        skip_two_paths = 0

        if two - adapter in (2, 3) and two > adapter:
            skip_two_paths, memoized = count_paths(
                adapters[(index + 2) % len(adapters) :], memoized
            )

        path_count += skip_two_paths

        three = adapters[(index + 3) % len(adapters)]
        skip_three_paths = 0
        if three - adapter == 3 and three > adapter:
            skip_three_paths, memoized = count_paths(adapters[index + 3 :], memoized)

        path_count += skip_three_paths

    memoized[str_adapters] = path_count

    return path_count, memoized


def part_2(adapters: List[int]):
    adapters.append(0)
    sorted_adapters = sorted(adapters)

    all_permutations, _ = count_paths(sorted_adapters, dict())

    print("Print 2: ", all_permutations)


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    adapters = [int(d) for d in data.split("\n")]

    part_1(adapters)
    part_2(adapters)


if __name__ == "__main__":
    main()