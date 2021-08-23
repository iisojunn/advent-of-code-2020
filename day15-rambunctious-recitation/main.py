"""Day 15 Advent of code"""


def play_round(numbers, indices):
    last = numbers[-1]
    last_indices = indices.get(last)
    if last_indices and len(last_indices) > 1:
        return last_indices[-1] - last_indices[-2]
    return 0


def play_until(limit, numbers):
    indices = {}
    for i, num in enumerate(numbers):
        add_new_index(indices, i, num)

    while len(numbers) < limit:
        new_value = play_round(numbers, indices)
        add_new_index(indices, len(numbers), new_value)
        numbers.append(new_value)

    return numbers


def add_new_index(indices, new_index, new_value):
    if indices.get(new_value):
        indices[new_value].append(new_index)
    else:
        indices[new_value] = [new_index]


if __name__ == '__main__':
    initial_numbers = [int(x) for x in "8,11,0,19,1,2".split(",")]
    NUMBERS = play_until(2020, initial_numbers)
    print(f"Number 2020th is {NUMBERS[-1]}")

    NUMBERS = play_until(30000000, initial_numbers)
    print(f"Number 30000000th is {NUMBERS[-1]}")
