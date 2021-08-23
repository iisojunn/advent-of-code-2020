"""Day 9 Advent of code 2020"""
import math

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


def lengths_of_one_rows(step_list):
    rows_of_ones = []
    found_ones = 0
    for step in step_list:
        if step == 1:
            found_ones += 1
        elif found_ones > 0:
            rows_of_ones.append(found_ones)
            found_ones = 0
    return rows_of_ones


def calculate_permutations(one_rows):
    possible_permutations = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    factors = [possible_permutations[x] for x in one_rows]
    return math.prod(factors)


if __name__ == '__main__':
    print(adapter_list())
    STEPS = steps(adapter_list())
    ones = count_steps(STEPS, step_size=1)
    threes = count_steps(STEPS, step_size=3)
    print(f"The result of one steps and three steps multiplication is "
          f"{ones * threes}")
    ONE_ROWS = lengths_of_one_rows(STEPS)
    permutations = calculate_permutations(ONE_ROWS)
    print(f"Total number of adapter connection permutations {permutations}")
