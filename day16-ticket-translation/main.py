"""Day 16 Advent of code"""
import math


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().split("\n\n")


def parse_field(spec):
    key, ranges_str = spec.split(": ")
    ranges = [[int(limit) for limit in range_.split("-")] for range_ in
              ranges_str.split(" or ")]
    return key, ranges


def parse_input(data):
    fields = dict([parse_field(field) for field in data[0].split("\n")])
    my_ticket = [int(field) for field in data[1].split("\n")[1].split(",")]
    tickets = [[int(field) for field in ticket.split(",")] for ticket in
               data[2].split("\n")[1:] if ticket]
    return fields, my_ticket, tickets


def is_in_range(field, range_):
    return range_[0] <= field <= range_[1]


def is_in_any_range(field, ranges):
    return any(is_in_range(field, range_) for range_ in ranges)


def is_valid(field, field_ranges):
    return any(is_in_any_range(field, ranges) for ranges in field_ranges.values())


def scan_tickets(field_ranges, tickets):
    error_rate = 0
    for ticket in tickets:
        for field in ticket:
            if not is_valid(field, field_ranges):
                error_rate += field
    return error_rate


def is_all_in_range(ranges, field_values):
    return all(is_in_any_range(field, ranges) for field in field_values)


def resolve_possible_field_orders(valid_tickets, field_ranges):
    possible_field_indices = {key: [] for key in field_ranges.keys()}
    for index, values in enumerate(transpose(valid_tickets)):
        for field_name, ranges in field_ranges.items():
            if is_all_in_range(ranges, values):
                possible_field_indices[field_name].append(index)
    return possible_field_indices


def transpose(valid_tickets):
    return list(map(list, zip(*valid_tickets)))


def only_option(possible_field_order):
    for name, possible_indices in possible_field_order.items():
        if len(possible_indices) == 1:
            return name, possible_indices[0]


def resolve_field_order(valid_tickets, field_ranges):
    field_order = {}
    possible = resolve_possible_field_orders(valid_tickets, field_ranges)
    while len(possible) != len(field_order):
        field_name, index = only_option(possible)
        field_order[field_name] = index
        consume_index(index, possible)
    return field_order


def consume_index(index, possible):
    for indices in possible.values():
        if index in indices:
            indices.pop(indices.index(index))


def multiply_departure_fields(my_ticket, field_order):
    return math.prod([my_ticket[index] for field, index in field_order.items()
                      if field.startswith("departure")])


if __name__ == '__main__':
    DATA = read_input()
    FIELD_RANGES, MY_TICKET, TICKETS = parse_input(DATA)
    ERROR_RATE = scan_tickets(FIELD_RANGES, TICKETS)
    print(f"Ticket scanning error rate is {ERROR_RATE}")

    VALID_TICKETS = [
        ticket
        for ticket in TICKETS
        if all(is_valid(field, FIELD_RANGES) for field in ticket)
    ]

    FIELD_ORDER = resolve_field_order(VALID_TICKETS, FIELD_RANGES)
    result = multiply_departure_fields(MY_TICKET, FIELD_ORDER)
    print(f"My ticket six departure values multiplied is {result}")
