"""Day 9 Advent of code 2020"""
from more_itertools import quantify


def read_input():
    with open("input", "r") as input_file:
        return [int(num) for num in input_file.read().splitlines()]


def adapter_list():
    input_data = sorted(read_input())
    device_adapter = input_data[-1] + 3
    return [0, *input_data, device_adapter]


def steps(adapters):
    return [later - first for first, later in zip(adapters, adapters[1:])]


def count_steps(step_list, step_size):
    return quantify(step_list, lambda step: step == step_size)


if __name__ == '__main__':
    STEPS = steps(adapter_list())
    ones = count_steps(STEPS, step_size=1)
    threes = count_steps(STEPS, step_size=3)
    print(f"The result of one steps and three steps multiplication is "
          f"{ones * threes}")
