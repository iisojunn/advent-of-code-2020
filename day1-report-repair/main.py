"""Advent of code, first day, task 1"""


def read_input():
    with open("input", "r") as input_file:
        input_list = [int(line) for line in input_file.read().splitlines()]
        print(f"Read input list {input_list}")
        return input_list


def find_two_addends(numbers, target):
    for i in numbers:
        for j in numbers:
            if i != j:
                if i + j == target:
                    return i, j


def solve_part_1():
    a, b = find_two_addends(read_input(), 2020)
    print(f"Found addends {a} and {b} that add up to 2020")
    print(f"Result of multiplication is {a * b}")


if __name__ == '__main__':
    solve_part_1()
