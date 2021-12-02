from collections import namedtuple
from typing import List

FORWARD = "forward"
DOWN = "down"
UP = "up"
COMMANDS = [FORWARD, DOWN, UP]

Instruction = namedtuple("Instruction", ["command", "value"])


def puzzle_1(commands: List[Instruction]) -> int:
    horizontal = 0
    depth = 0

    for command in commands:
        if command.command == FORWARD:
            horizontal += command.value
        if command.command == DOWN:
            depth += command.value
        if command.command == UP:
            depth -= command.value

    return horizontal * depth


def puzzle_2(commands: List[Instruction]) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        if command.command == FORWARD:
            horizontal += command.value
            depth += command.value * aim
        if command.command == UP:
            aim -= command.value
        if command.command == DOWN:
            aim += command.value

    return horizontal * depth


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    # Create list of tuples
    commands = [
        Instruction(x.split(" ")[0], int(x.split(" ")[1])) for x in data.split("\n")
    ]

    output_1 = puzzle_1(commands)
    print(output_1)

    output_2 = puzzle_2(commands)
    print(output_2)


if __name__ == "__main__":
    main()