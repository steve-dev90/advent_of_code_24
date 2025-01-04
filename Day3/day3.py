
import re

def solve_day3(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    muls = []
    for line in lines:
        muls  += re.findall("mul\(\d{1,3},\d{1,3}\)", line)

    return process_muls(muls)

def solve_day3_part2(input_file):
    with open(input_file, 'r') as f:
        input = f.read()

    do_nots = re.split("don\'t\(\)", input)

    muls = []
    muls += re.findall("mul\(\d{1,3},\d{1,3}\)", do_nots[0])
    for do_not in do_nots[1:]:
        do_cmds = re.split("do\(\)", do_not)
        #Ignore first as associated with don't()
        combine_do_cmds = ''.join(do_cmds[1:])
        muls += re.findall("mul\(\d{1,3},\d{1,3}\)", combine_do_cmds)

    return process_muls(muls)

def process_muls(muls):
    sum = 0
    for mul in muls:
        numbers = re.findall("\d{1,3}", mul)
        sum += int(numbers[0]) * int(numbers[1])

    return sum

if __name__ == "__main__":
    input_file = "input_day3.txt"  # Replace with the actual path to your input file
    # input_file = "sample_input.txt"
    part1 = solve_day3(input_file)
    part2 = solve_day3_part2(input_file)
    print(f"Day 3 Solution Part1: {part1}")
    print(f"Day 3 Solution Part2: {part2}")
