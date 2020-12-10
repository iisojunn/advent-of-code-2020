"""Day 6 advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def group_answers(input_list):
    answers = set()
    for row in input_list:
        if row:
            answers = answers.union(set(row))
        else:
            yield answers
            answers = set()
    if answers:
        yield answers


if __name__ == '__main__':
    any_yes = sum([len(answers) for answers in group_answers(read_input())])
    print(f"Sum of any yes answers by groups is {any_yes}")
