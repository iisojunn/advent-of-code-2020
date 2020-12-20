"""Day 19 Advent of code 2020"""


def read_input():
    with open("input", "r") as input_file:
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


def fulfils_option(message, option, rules):
    original_message = message
    for req in option:
        if type(req) == str:
            if not message:
                return False, original_message
            elif message.startswith(req):
                message = message[1:]
                continue
            return False, original_message
        fulfils, message = fulfils_sub_rule(message, rules[req], rules)
        if not fulfils:
            return False, original_message
    return True, message


def fulfils_sub_rule(message, sub_rule, rules):
    for option in sub_rule:
        fulfils, message = fulfils_option(message, option, rules)
        if fulfils:
            return True, message
    return False, message


def is_valid(message, rules):
    sub_rule_to_check = rules[0]
    fulfils, message = fulfils_sub_rule(message, sub_rule_to_check, rules)
    return fulfils and not message


if __name__ == '__main__':
    RULES, MESSAGES = read_input()
    VALID_MSG = [is_valid(MSG, RULES) for MSG in MESSAGES].count(True)
    print(f"There are {VALID_MSG} valid messages")
