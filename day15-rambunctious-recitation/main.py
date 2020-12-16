"""Day 15 Advent of code"""


def play_round(numbers):
    last = numbers[-1]
    reverse = list(reversed(numbers))
    try:
        index = reverse[1:].index(last)
    except ValueError:
        return 0
    return index + 1


def play_until(limit, numbers):
    while len(numbers) < limit:
        new_value = play_round(numbers)
        numbers.append(new_value)
    return numbers


if __name__ == '__main__':
    initial_numbers = [int(x) for x in "8,11,0,19,1,2".split(",")]
    NUMBERS = play_until(2020, initial_numbers)
    print(f"Number 2020th is {NUMBERS[-1]}")
