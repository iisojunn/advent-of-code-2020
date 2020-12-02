"""Day 2 solution for advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        input_data = input_file.read().splitlines()
        print(f"Input read from file {input_data}")
        return input_data


def is_valid(entry):
    limit, character, password = entry.replace(":", "").split(" ")
    lower_limit, upper_limit = limit.split("-")
    return int(lower_limit) <= password.count(character) <= int(upper_limit)


def solve_part_1():
    valid_passwords = 0
    for entry_line in read_input():
        if is_valid(entry_line):
            valid_passwords += 1
    print(f"Valid passwords {valid_passwords}")


if __name__ == '__main__':
    solve_part_1()
