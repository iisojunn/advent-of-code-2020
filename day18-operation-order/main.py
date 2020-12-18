"""Day 18 Advent of code"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().replace(" ", "").splitlines()


def resolve_value(string, additions_before=False):
    values = []
    operators = []
    math_string = iter(enumerate(string))
    for i, element in math_string:
        if element == "(":
            match = matching_parenthesis(string[i:])
            element = resolve_value(string[i + 1:i + match], additions_before)
            for skip in range(match):
                next(math_string)
        if str(element) in '*+':
            operators.append(element)
        else:
            values.append(int(element))
    return calculate_value(values, operators, additions_before)


def matching_parenthesis(string):
    count = 0
    for i, char in enumerate(string):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count == 0:
                return i


def calculate_value(values, operators, additions_before):
    if additions_before:
        values, operators = calculate_additions_before(values, operators)
    return calculate_with_same_precedence(values, operators)


def calculate_additions_before(values, operators):
    while '+' in operators:
        index = operators.index('+')
        operators.pop(index)
        values[index] = values[index] + values.pop(index + 1)
    return values, operators


def calculate_with_same_precedence(values, operators):
    value = values[0]
    for i, operator in enumerate(operators, start=1):
        if operator == '*':
            value *= values[i]
        elif operator == '+':
            value += values[i]
    return value


if __name__ == '__main__':
    math_problems = read_input()
    VALUE = sum([resolve_value(line) for line in math_problems])
    print(f"Total sum for math problems with same precedence is {VALUE}")
    VALUE2 = sum(
        [resolve_value(line, additions_before=True) for line in math_problems])
    print(f"Total sum for math problems with addition precedence is {VALUE2}")
