from typing import List


def puzzle_1(numbers: List[int]) -> int:
    increases = 0

    for idx, num in enumerate(numbers[1:]):
        prev = numbers[idx]
        if num > prev:
            increases += 1

    return increases


def puzzle_2(numbers: List[int]) -> int:
    increases = 0

    for idx, _ in enumerate(numbers[1:]):
        if (idx + 3) >= len(numbers):
            # We can't create anymore windows
            break

        prev_window = sum(numbers[idx : idx + 3])
        cur_window = sum(numbers[1:][idx : idx + 3])

        if cur_window > prev_window:
            increases += 1

    return increases


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    numbers = [int(x) for x in data.split("\n")]

    output_1 = puzzle_1(numbers)
    print(output_1)

    output_2 = puzzle_2(numbers)
    print(output_2)


if __name__ == "__main__":
    main()