"""Day 12 Advent of code"""

FACING_MAP = {
    0:  (1, 0),
    90: (0, 1),
    180: (-1, 0),
    270: (0, -1),
    (1, 0): 0,
    (0, 1): 90,
    (-1, 0): 180,
    (0, -1): 270
}


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def forward(amount, north_, east_, facing):
    north_ += facing[0] * amount
    east_ += facing[1] * amount
    return north_, east_, facing


def left(amount, north_, east_, facing):
    new_degrees = (FACING_MAP[facing] - amount) % 360
    return north_, east_, FACING_MAP[new_degrees]


def right(amount, north_, east_, facing):
    new_degrees = (FACING_MAP[facing] + amount) % 360
    return north_, east_, FACING_MAP[new_degrees]


def north(amount, north_, east_, facing):
    north_ += amount
    return north_, east_, facing


def east(amount, north_, east_, facing):
    east_ += amount
    return north_, east_, facing


def south(amount, north_, east_, facing):
    north_ -= amount
    return north_, east_, facing


def west(amount, north_, east_, facing):
    east_ -= amount
    return north_, east_, facing


COMMANDS = {
    "F": forward,
    "L": left,
    "R": right,
    "N": north,
    "E": east,
    "S": south,
    "W": west,
}


def follow_instructions(instructions):
    north_, east_, = 0, 0
    facing = (0, 1)
    for cmd, amount in [(instr[0], int(instr[1:])) for instr in instructions]:
        north_, east_, facing = COMMANDS[cmd](amount, north_, east_, facing)
    return north_, east_


if __name__ == '__main__':
    INSTRUCTIONS = read_input()
    NORTH, EAST = follow_instructions(INSTRUCTIONS)
    print(f"Manhattan distance is {abs(NORTH) + abs(EAST)}")
