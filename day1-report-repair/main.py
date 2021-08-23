"""Advent of code, first day, task 1"""


def read_input():
    with open("input", "r") as input_file:
        input_list = [int(line) for line in input_file.read().splitlines()]
        print(f"Read input list {input_list}")
        return input_list


def find_two_addends(numbers, target):
    for x in numbers:
        for y in numbers:
            if x != y and x + y == target:
                return x, y


def solve_part_1():
    a, b = find_two_addends(read_input(), 2020)
    print(f"Found addends {a} and {b} that add up to 2020")
    print(f"Result of multiplication is {a * b}")


def find_three_addends(numbers, target):
    for z in numbers:
        sub_target = target - z
        result = find_two_addends(numbers, sub_target)
        if result is not None:
            return result[0], result[1], z


def solve_part_2():
    a, b, c = find_three_addends(read_input(), 2020)
    print(f"Found three addends {a}, {b}, {c} that add up to 2020")
    print(f"Result of multiplication is {a * b * c}")


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()
