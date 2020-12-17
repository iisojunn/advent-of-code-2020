"""Day 16 Advent of code"""


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


def is_valid(field, field_ranges):
    for ranges in field_ranges.values():
        if any([is_in_range(field, range_) for range_ in ranges]):
            return True
    return False


def scan_tickets(field_ranges, tickets):
    error_rate = 0
    for ticket in tickets:
        for field in ticket:
            if not is_valid(field, field_ranges):
                error_rate += field
    return error_rate


if __name__ == '__main__':
    DATA = read_input()
    FIELD_RANGES, MY_TICKET, TICKETS = parse_input(DATA)
    ERROR_RATE = scan_tickets(FIELD_RANGES, TICKETS)
    print(f"Ticket scanning error rate is {ERROR_RATE}")
