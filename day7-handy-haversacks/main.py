"""Day 7 Advent of code 2020"""
import re

BAG_REGEX = r"(?P<bag_name>[a-z\s]*) bags contain (?P<contents>.*)\."
CONTENTS_REGEX = r"[\s]*(?P<bag_amount>[1-9]) (?P<bag_name>[a-z\s]*) bag[s]*"


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def parse_content(content):
    match = re.match(CONTENTS_REGEX, content)
    return match.group("bag_name"), match.group("bag_amount")


def parse_contents(contents):
    if contents == "no other bags":
        return {}
    return dict([parse_content(content) for content in contents.split(",")])


def parse_bag_rule(row):
    match = re.match(BAG_REGEX, row)
    return match.group("bag_name"), match.group("contents")


def parse_bag_to_listing(listing, row):
    bag_name, contents = parse_bag_rule(row)
    listing[bag_name] = parse_contents(contents)


def parse_bags(bag_listing):
    listing = {}
    for row in bag_listing:
        parse_bag_to_listing(listing, row)
    return listing


def bags_containing(bags, name):
    contained_in = []
    for bag_name, contents in bags.items():
        for content_name, amount in contents.items():
            if content_name == name:
                contained_in.append(bag_name)
    return contained_in


def bags_that_can_contain(bag_name):
    found = set()
    to_check = [bag_name]
    while to_check:
        containers = bags_containing(BAGS, to_check.pop())
        to_check += containers
        found = found.union(set(containers))
    return found


if __name__ == '__main__':
    BAGS = parse_bags(read_input())
    total = len(bags_that_can_contain('shiny gold'))
    print(f"Shiny gold bag can be in {total} bags.")
