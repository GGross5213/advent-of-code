from typing import List, Dict, Tuple
from copy import deepcopy


def list_to_string(lst: List[List[str]]) -> str:
    return "\n".join(["".join(row) for row in lst])


def count_adjacent_empty_seats(index_x, index_y, floor_plan) -> int:
    start_x = index_x - 1 if index_x - 1 >= 0 else 0
    start_y = index_y - 1 if index_y - 1 >= 0 else 0

    end_x = index_x + 1 if index_x + 1 > len(floor_plan) else len(floor_plan) - 1
    end_y = index_y + 1 if index_y + 1 > len(floor_plan[0]) else len(floor_plan[0]) - 1

    filled_seats = 0

    for ix, row in enumerate(floor_plan[start_x : end_x + 1]):
        for iy, space in enumerate(row[start_y : end_y + 1]):
            if ix == index_x and iy == index_y:
                continue

            if space == "#":
                filled_seats += 1

    return filled_seats


def stablize_floor_plan(floor_plan: List[List[str]]) -> List[List[str]]:
    is_stabilized = False
    count = 1
    _floor_plan = deepcopy(floor_plan)
    while not is_stabilized:
        new_floor = deepcopy(_floor_plan)
        has_changed = False
        for index, row in enumerate(_floor_plan):
            for index1, space in enumerate(row):
                if space == ".":
                    continue
                filled_adjacent_seats = count_adjacent_empty_seats(
                    index, index1, _floor_plan
                )

                if space == "#" and filled_adjacent_seats >= 4:
                    new_floor[index][index1] = "L"
                    has_changed = True

                if space == "L" and filled_adjacent_seats == 0:
                    new_floor[index][index1] = "#"
                    has_changed = True

        is_stabilized = not has_changed
        _floor_plan = deepcopy(new_floor)

        count += 1

    return _floor_plan


def part_1(floor_plan: List[List[str]]):
    stablized_plan = stablize_floor_plan(floor_plan)
    print("Stabilzed Plan: ")
    print(list_to_string(stablized_plan))

    filled_seats = sum([row.count("#") for row in stablized_plan])

    print("Part 1: ", filled_seats)


def part_2(data: str):
    pass


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    floor_plan = [list(d.strip()) for d in data.split("\n")]
    part_1(floor_plan)
    part_2(floor_plan)


if __name__ == "__main__":
    main()