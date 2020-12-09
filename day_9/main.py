from typing import List


def part_1(numbers: List[int]):
    preamble = numbers[:25]

    for index, num in enumerate(numbers[25:]):
        is_valid = any([(num - p) in preamble for p in preamble])
        if not is_valid:
            print("Part 1: ", num)
            print(preamble)
            print(index)
            break

        preamble.pop(0)
        preamble.append(num)


def part_2(numbers: List[int]):
    preamble = numbers[:25]
    wrong_num = 0
    for index, num in enumerate(numbers[25:]):
        is_valid = any([(num - p) in preamble for p in preamble])
        if not is_valid:
            print("Part 1: ", num)
            wrong_num = num
            break

        preamble.pop(0)
        preamble.append(num)

    def find_set(base_index):
        for x in range(base_index + 1, len(numbers)):
            total = sum(numbers[base_index : x + 1])
            if total == wrong_num:
                return numbers[base_index : x + 1]

            if total > wrong_num:
                return None
        return None

    cont_set = []
    for index, _ in enumerate(numbers):
        tmp_set = find_set(index)

        if tmp_set:
            cont_set = tmp_set
            break

    sorted_set = sorted(tmp_set)

    total = sorted_set[0] + sorted_set[-1]

    print("Part 2", total)


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    numbers = [int(n) for n in data.split("\n")]
    part_1(numbers)
    part_2(numbers)


if __name__ == "__main__":
    main()