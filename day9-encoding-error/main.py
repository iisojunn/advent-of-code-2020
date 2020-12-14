"""Day 9 Advent of code"""


def read_input():
    with open("input", "r") as input_file:
        return [int(num) for num in input_file.read().splitlines()]


def sums_of_two(nums):
    for i, num in enumerate(nums):
        for k in range(i + 1, len(nums)):
            yield num + nums[k]


def find_invalid_number(numbers):
    for i, number in enumerate(numbers):
        if i < 25:
            continue
        if number not in sums_of_two(numbers[i-25:i]):
            return number


if __name__ == '__main__':
    print(read_input())
    invalid = find_invalid_number(read_input())
    print(f"First number without valid property {invalid}")
