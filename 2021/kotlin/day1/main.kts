import java.io.File

fun puzzle1(numbers: List<Int>): Int {
    var increases: Int = 0

    for (idx in numbers.indices) {
        if ((idx + 1) >= numbers.size) {
            break
        }
        val cur: Int = numbers.elementAt(idx)
        val next: Int = numbers.elementAt(idx + 1) 

        if (next > cur) {
            increases += 1
        }
    }

    return increases
}

fun puzzle2(numbers: List<Int>): Int {
    var increases: Int = 0

    val windows: List<List<Int>> = numbers.windowed(3)
    for (idx in windows.indices) {
        // Could maybe use defaults to avoid this? 
        if ((idx + 1) >= windows.size) {
            break
        }
        val cur: Int = windows.elementAt(idx).sum()
        val next: Int = windows.elementAt(idx + 1).sum()
        
        if (next > cur) {
            increases += 1
        }
    }

    return increases
}

fun main() {
    val lines: List<String> = File("input.txt").readLines()

    val numbers: List<Int> = lines.map { it.toInt() }

    val output1: Int = puzzle1(numbers)
    println(output1)

    val output2: Int = puzzle2(numbers)
    println(output2)
}

main()