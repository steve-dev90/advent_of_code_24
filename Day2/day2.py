
from functools import reduce

def solve_day2(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    part1 =  reduce(check_line_part1, lines, 0)
    part2 =  reduce(check_line_part2, lines, 0)

    return part1, part2

def check_line_part1(safe_num, line):
    numbers = [int(i) for i in line.strip().split()]

    if check_numbers(numbers):
        return safe_num + 1

    return safe_num

def check_line_part2(safe_num, line):
    numbers = [int(i) for i in line.strip().split()]

    if check_numbers(numbers):
        return safe_num + 1

    for index in range(0, len(numbers)):
        numbers_less_one = numbers[0:index] + numbers[index + 1:]
        if check_numbers(numbers_less_one):
            return safe_num + 1

    return safe_num

def check_numbers(numbers):
    diff = [numbers[i] - numbers[i+1] for i in range(0,len(numbers)-1)]

    greater_than_three = reduce(lambda count, num: count + (abs(num) > 3), diff, 0)
    if greater_than_three > 0:
        return False

    negatives = reduce(lambda count, num: count + (num < 0), diff, 0)
    positives = reduce(lambda count, num: count + (num > 0), diff, 0)
    if (negatives == len(diff)) | (positives == len(diff)):
        return True

    return False

if __name__ == "__main__":
    # input_file = "sample_input.txt"  # Replace with the actual path to your input file
    input_file = "input_day2.txt"
    part1, part2 = solve_day2(input_file)
    print(f"Day 2 Solution Part1: {part1}")
    print(f"Day 2 Solution Part2: {part2}")