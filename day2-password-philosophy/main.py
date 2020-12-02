"""Day 2 solution for advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        input_data = input_file.read().splitlines()
        print(f"Input read from file {input_data}")
        return input_data


def is_valid_with_old_policy(entry):
    limit, character, password = entry.replace(":", "").split(" ")
    lower_limit, upper_limit = limit.split("-")
    return int(lower_limit) <= password.count(character) <= int(upper_limit)


def check_valid_passwords(validation_method):
    valid_passwords = 0
    for entry_line in read_input():
        if validation_method(entry_line):
            valid_passwords += 1
    print(f"Valid passwords {valid_passwords}")


def solve_part_1():
    check_valid_passwords(is_valid_with_old_policy)


def is_valid_with_new_policy(entry):
    positions, character, password = entry.replace(":", "").split(" ")
    pos_a, pos_b = positions.split("-")
    pos_a_contains_char = password[int(pos_a) - 1] == character
    pos_b_contains_char = password[int(pos_b) - 1] == character
    return bool(pos_a_contains_char) != bool(pos_b_contains_char)


def solve_part_2():
    check_valid_passwords(is_valid_with_new_policy)


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()
