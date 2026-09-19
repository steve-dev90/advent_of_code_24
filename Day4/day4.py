
import re

def solve_day4_part1(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    xmas_sum = 0

    #Find all occasions of XMAS and SAMX for each line
    for line in lines:
        xmas_sum += process_line(line)

    #Pivot rows and repeat above
    xmas_sum = convert_to_horizontal(lines, xmas_sum)

    #Add n spaces at the beginning of each line, where n is the line number
    lines_plus_one = []
    lines_minus_one = []

    for i in range(0, len(lines)):
        #Remove the newline character in line
        line_no_newline = lines[i].split('\n')[0]
        lines_plus_one.append(
            ''.join([' ' * i + line_no_newline + ' ' * (len(lines) - (i + 1))])
            )
        lines_minus_one.append(
            ''.join([' ' * (len(lines) - (i + 1)) + line_no_newline + ' ' * i])
            )

    xmas_sum = convert_to_horizontal(lines_plus_one, xmas_sum)
    xmas_sum = convert_to_horizontal(lines_minus_one, xmas_sum)

    return xmas_sum

def process_line(line):
    xmas = re.findall(r"XMAS", line)
    samx = re.findall(r"SAMX", line)
    return len(xmas) + len(samx)

def convert_to_horizontal(lines, xmas_sum):
    num_chars = len(lines[0].split('\n')[0])
    for i in range(0, num_chars):
        line = ''.join([line[i] for line in lines])
        xmas_sum += process_line(line)
    return xmas_sum

def solve_day4_part2(input_file):
    return False

if __name__ == "__main__":
    input_file = "input_day4.txt"  # Replace with the actual path to your input file
    # input_file = "sample_input.txt"
    part1 = solve_day4_part1(input_file)
    # part2 = solve_day4_part2(input_file)
    print(f"Day 4 Solution Part1: {part1}")
    # print(f"Day 4 Solution Part2: {part2}")
