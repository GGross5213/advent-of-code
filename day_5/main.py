from typing import Tuple


def str_binary_to_num(binary_str: str, ONE: str) -> int:
    return sum(
        [
            ((2 ** ((len(binary_str) - 1) - index)) * int(char == ONE))
            for index, char in enumerate(binary_str)
        ]
    )


def calculate_seat_id(row: int, col: int) -> int:
    return (row * 8) + col


def get_row_col(boarding_pass: str) -> Tuple[int, int]:
    return (
        str_binary_to_num(boarding_pass[:7], "B"),
        str_binary_to_num(boarding_pass[6:], "R"),
    )


def part_1(data: str) -> None:
    boarding_passes = data.split("\n")

    highest_seat_id = max(
        [calculate_seat_id(*get_row_col(bp)) for bp in boarding_passes]
    )
    print(f"Part 1: {highest_seat_id}")


def part_2(data: str) -> None:
    boarding_passes = data.split("\n")

    seat_ids_sorted = sorted(
        [calculate_seat_id(*get_row_col(bp)) for bp in boarding_passes]
    )

    my_seat = 0
    for seat_1, seat_2 in zip(seat_ids_sorted, seat_ids_sorted[1:]):
        if seat_2 - seat_1 == 2:
            my_seat = seat_1 + 1
            break

    print(f"Part 2: {my_seat}")


def main() -> None:
    with open("input.txt", "r") as file:
        data = file.read()

    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()