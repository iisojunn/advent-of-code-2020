"""Day 18 Advent of code"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().replace(" ", "").splitlines()


def resolve_value(string):
    values = []
    operators = []
    math_string = iter(enumerate(string))
    for i, element in math_string:
        if element == "(":
            match = matching_parenthesis(string[i:])
            element = resolve_value(string[i + 1:i + match])
            for skip in range(match):
                next(math_string)
        if str(element) in '*+':
            operators.append(element)
        else:
            values.append(int(element))
    return calculate_value(values, operators)


def matching_parenthesis(string):
    count = 0
    for i, char in enumerate(string):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count == 0:
                return i


def calculate_value(values, operators):
    value = values[0]
    for i, operator in enumerate(operators, start=1):
        if operator == '*':
            value *= values[i]
        elif operator == '+':
            value += values[i]
    return value


if __name__ == '__main__':
    VALUE = 0
    for line in read_input():
        VALUE += resolve_value(line)
    print(f"Total sum for math problems with same precedence is {VALUE}")
