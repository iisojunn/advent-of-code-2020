"""Day 19 Advent of code 2020"""


def read_input(input_):
    with open(input_, "r") as input_file:
        rules, messages = input_file.read().split("\n\n")
        return parse_rules(rules), messages.splitlines()


def parse_rules(rules):
    rules_ = {}
    for rule in rules.splitlines():
        name, sub_rule = rule.split(": ")
        rules_[int(name)] = parse_sub_rule(sub_rule)
    return rules_


def parse_sub_rule(sub_rule):
    if '"' in sub_rule:
        return {tuple(sub_rule.replace('"', ""))}
    return {parse_part(part) for part in sub_rule.split(" | ")}


def parse_part(part):
    return tuple(int(r) for r in part.split(" "))


def valid_with_requirements(msg, reqs, rules):
    if not reqs:
        yield msg
    else:
        req = reqs[0]
        if type(req) == str:
            if msg.startswith(req):
                yield from valid_with_requirements(msg[1:], reqs[1:], rules)
        else:
            for message in valid_with_sub_rule(msg, rules[req], rules):
                yield from valid_with_requirements(message, reqs[1:], rules)


def valid_with_sub_rule(message, sub_rule, rules):
    for option in sub_rule:
        yield from valid_with_requirements(message, option, rules)


def is_valid(message, rules):
    sub_rule_to_check = rules[0]
    return not all(valid_with_sub_rule(message, sub_rule_to_check, rules))


if __name__ == '__main__':
    RULES, MESSAGES = read_input("input")
    VALID_MSG = [is_valid(MSG, RULES) for MSG in MESSAGES].count(True)
    print(f"There are {VALID_MSG} valid messages")
    assert VALID_MSG == 162

    RULES[8] = {(42,), (42, 8)}
    RULES[11] = {(42, 31), (42, 11, 31)}
    VALID_MSG = [is_valid(MSG, RULES) for MSG in MESSAGES].count(True)
    print(f"There are {VALID_MSG} valid messages with rule changes")
    assert VALID_MSG == 267
