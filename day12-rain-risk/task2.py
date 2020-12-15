"""Day 12 Advent of code task 2"""


def read_input():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def forward(amount, north_, east_, waypoint):
    north_ += amount * waypoint[0]
    east_ += amount * waypoint[1]
    return north_, east_, waypoint


def left(amount, north_, east_, waypoint):
    for _rotation in range(int(amount / 90)):
        waypoint = (waypoint[1], -waypoint[0])
    return north_, east_, waypoint


def right(amount, north_, east_, waypoint):
    for _rotation in range(int(amount / 90)):
        waypoint = (-waypoint[1], waypoint[0])
    return north_, east_, waypoint


def north(amount, north_, east_, waypoint):
    waypoint = (waypoint[0] + amount, waypoint[1])
    return north_, east_, waypoint


def east(amount, north_, east_, waypoint):
    waypoint = (waypoint[0], waypoint[1] + amount)
    return north_, east_, waypoint


def south(amount, north_, east_, waypoint):
    waypoint = (waypoint[0] - amount, waypoint[1])
    return north_, east_, waypoint


def west(amount, north_, east_, waypoint):
    waypoint = (waypoint[0], waypoint[1] - amount)
    return north_, east_, waypoint


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
    north_, east_ = 0, 0
    waypoint = (1, 10)
    for cmd, amount in [(instr[0], int(instr[1:])) for instr in instructions]:
        north_, east_, waypoint = \
            COMMANDS[cmd](amount, north_, east_, waypoint)
    return north_, east_


if __name__ == '__main__':
    INSTRUCTIONS = read_input()
    print(INSTRUCTIONS)
    NORTH, EAST = follow_instructions(INSTRUCTIONS)
    print(f"Manhattan distance is {abs(NORTH) + abs(EAST)}")
