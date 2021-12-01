from typing import List, Set, Tuple


def read_instruction(instruction: str) -> Tuple[str, int]:
    inst, num = instruction.split(" ")

    return inst, int(num)


def part_1(instructions: List[str]):
    def follow_instructions(
        current_index: int, accumulator: int, instructions_seen: Set[int]
    ) -> int:
        if current_index in instructions_seen:
            return accumulator

        instructions_seen.add(current_index)

        inst, num = read_instruction(instructions[current_index])

        next_index = current_index + 1

        if inst == "acc":
            accumulator += num

        if inst == "jmp":
            next_index = current_index + num

        return follow_instructions(next_index, accumulator, instructions_seen)

    acc = follow_instructions(0, 0, set())

    print("Part 1: ", acc)


def part_2(instructions: List[str]):
    def follow_instructions(
        current_index: int,
        accumulator: int,
        instructions_seen: Set[int],
        instructions,
    ) -> Tuple[int, bool]:
        if current_index in instructions_seen or current_index == len(instructions):
            return accumulator, current_index == len(instructions)

        instructions_seen.add(current_index)

        inst, num = read_instruction(instructions[current_index])

        next_index = current_index + 1

        if inst == "acc":
            accumulator += num

        if inst == "jmp":
            next_index = current_index + num

        return follow_instructions(
            next_index, accumulator, instructions_seen, instructions
        )

    acc = 0

    for index, line in enumerate(instructions):
        inst, _ = read_instruction(line)

        if inst == "nop":
            new_inst = instructions.copy()
            new_inst[index] = line.replace("nop", "jmp")
            accum, finished = follow_instructions(0, 0, set(), new_inst)
            if finished:
                print("Part 2", accum)
                break

        if inst == "jmp":
            new_inst = instructions.copy()
            new_inst[index] = line.replace("jmp", "nop")
            accum, finished = follow_instructions(0, 0, set(), new_inst)
            if finished:
                print("Part 2", accum)
                break


def main():
    with open("input.txt", "r") as file:
        data = file.read()

    instructions = data.split("\n")

    part_1(instructions)
    part_2(instructions)


if __name__ == "__main__":
    main()