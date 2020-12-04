import math


def part1():
    slope_grid = []

    with open("input.txt") as file:
        for line in file.readlines():
            slope_grid.append(list(line.strip()))

    num_of_rows = len(slope_grid)
    num_of_cols = len(slope_grid[0])

    def find_trees_in_path_recur(cur_row: int, cur_col: int) -> int:
        cur_pos = slope_grid[cur_row][cur_col % num_of_cols]

        if cur_row == num_of_rows - 1:  # you are in the last row
            return int(cur_pos == "#")

        return int(cur_pos == "#") + find_trees_in_path_recur(cur_row + 1, cur_col + 3)

    total_trees = find_trees_in_path_recur(0, 0)

    print(f"Total Trees: {total_trees}")


def part2():
    slope_grid = []

    with open("input.txt") as file:
        for line in file.readlines():
            slope_grid.append(list(line.strip()))

    num_of_rows = len(slope_grid)
    num_of_cols = len(slope_grid[0])

    def find_trees_in_path_recur(
        right: int, down: int, cur_row: int, cur_col: int
    ) -> int:
        cur_pos = slope_grid[cur_row][cur_col % num_of_cols]

        if cur_row == num_of_rows - 1:  # you are in the last row
            return int(cur_pos == "#")

        return int(cur_pos == "#") + find_trees_in_path_recur(
            right, down, cur_row + down, cur_col + right
        )

    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    product_of_trees = math.prod(
        [find_trees_in_path_recur(right, down, 0, 0) for right, down in paths]
    )

    print(f"Product of Trees: {product_of_trees}")


if __name__ == "__main__":
    part1()
    part2()