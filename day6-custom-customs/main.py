"""Day 6 advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def group_answers():
    group = []
    for row in read_input():
        if row:
            group.append(set(row))
        else:
            yield group
            group = []
    if group:
        yield group


def any_yes_answers():
    return [answers[0].union(*answers) for answers in group_answers()]


def all_yes_answers():
    return [answers[0].intersection(*answers) for answers in group_answers()]


if __name__ == '__main__':
    any_yes = sum(len(answers) for answers in any_yes_answers())
    print(f"Sum of any yes answers by groups is {any_yes}")
    all_yes = sum(len(answers) for answers in all_yes_answers())
    print(f"Sum of all yes answers by groups is {all_yes}")
