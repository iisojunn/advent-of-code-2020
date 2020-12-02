"""Advent of code, first day, task 1"""


def read_input():
    with open("input", "r") as input_file:
        return [int(line) for line in input_file.read().splitlines()]


def find_addends(numbers, target):
    for i in numbers:
        for j in numbers:
            if i != j:
                if i + j == target:
                    return i, j


if __name__ == '__main__':
    input_list = read_input()
    print(f"Read input list {input_list}")
    a, b = find_addends(input_list, 2020)
    print(f"Found addends {a} and {b} that add up to 2020")
    print(f"Result of multiplication is {a*b}")
