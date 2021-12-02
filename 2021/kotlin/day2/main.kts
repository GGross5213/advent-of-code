import java.io.File

enum class Command {
    forward, down, up
}

class Instruction(val command: Command, val value: Int)

fun puzzle1(instructions: List<Instruction>): Int {
    var horizontal: Int = 0
    var depth: Int = 0

    for (instruction in instructions) {
        when (instruction.command) {
            Command.forward -> horizontal += instruction.value
            Command.down -> depth += instruction.value
            Command.up -> depth -= instruction.value
        }
    }

    return horizontal * depth
}

fun puzzle2(instructions: List<Instruction>): Int {
    var horizontal: Int = 0
    var depth: Int = 0
    var aim: Int = 0

    for (instruction in instructions) {
        when (instruction.command) {
            Command.forward -> {
                horizontal += instruction.value
                depth += instruction.value * aim
            }
            Command.up -> aim -= instruction.value
            Command.down -> aim += instruction.value
        }
    }
    return horizontal * depth
}

fun main() {
    val lines: List<String> = File("input.txt").readLines()

    val instructions: List<Instruction> = lines.map { 
        Instruction(Command.valueOf(it.split(" ").elementAt(0)), it.split(" ").elementAt(1).toInt())
    }

    val output1: Int = puzzle1(instructions)
    println(output1)

    val output2: Int = puzzle2(instructions)
    println(output2)
}

main()