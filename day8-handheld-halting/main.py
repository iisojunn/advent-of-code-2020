"""Day 8 Advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def parse_value(argument):
    value = int(argument[1:])
    if argument.startswith("+"):
        return value
    return -value


def execute_instruction(instruction):
    global accumulator, instruction_index
    operation, argument = instruction.split(" ")
    if operation == "jmp":
        instruction_index += parse_value(argument)
    elif operation == "acc":
        accumulator += parse_value(argument)
        instruction_index += 1
    elif operation == "nop":
        instruction_index += 1


if __name__ == '__main__':
    code = read_input()
    accumulator = 0
    instruction_index = 0
    visited = []
    while instruction_index not in visited:
        visited.append(instruction_index)
        execute_instruction(code[instruction_index])

    print(f"Accumulator value before second visit is {accumulator}")
