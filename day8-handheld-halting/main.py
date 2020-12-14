"""Day 8 Advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def parse_value(argument):
    value = int(argument[1:])
    if argument.startswith("+"):
        return value
    return -value


def execute(instruction, acc, code_index):
    operation, argument = instruction.split(" ")
    if operation == "jmp":
        code_index += parse_value(argument)
    elif operation == "acc":
        acc += parse_value(argument)
        code_index += 1
    elif operation == "nop":
        code_index += 1
    return acc, code_index


def execute_until_second_loop_starts(code):
    acc = 0
    code_index = 0
    visited = []
    while code_index not in visited:
        visited.append(code_index)
        acc, code_index = execute(code[code_index], acc, code_index)
    return acc


if __name__ == '__main__':
    CODE = read_input()
    accumulator = execute_until_second_loop_starts(CODE)
    print(f"Accumulator value before second visit is {accumulator}")
