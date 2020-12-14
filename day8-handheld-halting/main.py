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


class LastCommandNotReached(Exception):
    pass


def execute_until_last_command(code):
    acc = 0
    code_index = 0
    last_index = len(code)
    visited = []
    while code_index not in visited:
        visited.append(code_index)
        acc, code_index = execute(code[code_index], acc, code_index)
        if code_index == last_index:
            return acc
    raise LastCommandNotReached


def create_candidate(code, index, operation, new_operation):
    candidate = code.copy()
    candidate[index] = code[index].replace(operation, new_operation)
    return candidate


def code_candidates(code):
    for i, instruction in enumerate(code):
        if "jmp" in instruction:
            yield create_candidate(code, i, "jmp", "nop")
        elif "nop" in instruction:
            yield create_candidate(code, i, "nop", "jmp")


def fix_loop_and_execute(code):
    for code_candidate in code_candidates(code):
        try:
            acc = execute_until_last_command(code_candidate)
            return acc
        except LastCommandNotReached:
            continue


if __name__ == '__main__':
    CODE = read_input()
    accumulator = execute_until_second_loop_starts(CODE)
    print(f"Accumulator value before second visit is {accumulator}")
    accumulator = fix_loop_and_execute(CODE)
    print(f"Accumulator value with fixed loop is {accumulator}")
