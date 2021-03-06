"""Day 9 Advent of code"""
from itertools import islice


def read_input():
    with open("input", "r") as input_file:
        return [int(num) for num in input_file.read().splitlines()]


def sums_of_two(nums):
    for i, num1 in enumerate(nums):
        for num2 in islice(nums, i + 1):
            yield num1 + num2


def find_invalid_number(numbers):
    for i, number in enumerate(numbers[25:], start=25):
        if number not in sums_of_two(numbers[i-25:i]):
            return number


def calculate_weakness(numbers, start, end):
    contiguous_set = numbers[start:end]
    return min(contiguous_set) + max(contiguous_set)


def find_weakness(numbers, target):
    for i, num in enumerate(numbers):
        current = num
        for k in range(i + 1, len(numbers)):
            current += numbers[k]
            if current == target:
                return calculate_weakness(numbers, i, k)
            if current > target:
                break


if __name__ == '__main__':
    NUMBERS = read_input()
    invalid = find_invalid_number(NUMBERS)
    print(f"First number without valid property {invalid}")
    weakness = find_weakness(NUMBERS, invalid)
    print(f"The encryption weakness is {weakness}")
