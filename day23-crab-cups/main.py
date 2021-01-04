"""Day 23 Advent of Code"""

INPUT = "158937462"


def cup_labels(cups):
    index_1 = cups.index(1)
    return "".join(str(cup) for cup in cups[index_1 + 1:] + cups[:index_1])


def do_move(cups):
    current = cups[0]
    new_cups = [cups.pop(1) for _ in range(3)]
    destination = get_destination_index(cups, current)
    return cups[1:destination] + new_cups + cups[destination:] + [current]


def get_destination_index(cups, current):
    if current > min(cups):
        label = max([cup for cup in cups if cup < current])
        return cups.index(label) + 1
    return cups.index(max(cups)) + 1


if __name__ == '__main__':
    CUPS = [int(cup) for cup in INPUT]
    for _ in range(100):
        CUPS = do_move(CUPS)
    print(f"Labels on the cup after 1 is {cup_labels(CUPS)}")
