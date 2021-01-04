"""Day 23 Advent of Code"""

INPUT = "158937462"
# INPUT = "389125467"


class Cup:

    def __init__(self, label):
        self.label = label
        self.next = None

    def __str__(self):
        return str(self.label)

    def __repr__(self):
        return f"{self.label} -> {str(self.next)}"


class CupCircle:

    def __init__(self, cup_data):
        self.first = None
        self.size = len(cup_data)
        self.cups = {}
        self.populate(cup_data)

    def all_cups(self, start_label):
        if start_label is None:
            start_cup = self.first
        else:
            start_cup = self.cups[start_label]
        cup = start_cup
        for _ in range(self.size):
            yield cup
            cup = cup.next

    def populate(self, cup_data):
        self.first = self.create_cup(int(cup_data[0]))
        previous = self.first
        for cup in cup_data[1:]:
            new = self.create_cup(int(cup))
            previous.next = new
            previous = new
        previous.next = self.first

    def create_cup(self, label):
        cup = Cup(label)
        self.cups[label] = cup
        return cup


def do_move(current, cup_circle):
    a = current.next
    b = a.next
    c = b.next
    picked = [a, b, c]
    # print("pick up:", picked)
    destination_label = get_destination_label(current.label, picked,
                                              cup_circle.size)
    # print("destination:", destination_label)
    destination = cup_circle.cups[destination_label]

    current.next = c.next
    c.next = destination.next
    destination.next = a
    return current.next


def get_destination_label(current_label, picked_cups, total):
    destination = current_label - 1
    picked_labels = [cup.label for cup in picked_cups]
    while destination in picked_labels or destination < 1:
        if destination in picked_labels:
            destination -= 1
        if destination < 1:
            destination = total
    return destination


def cup_labels(cup_circle, start=None):
    return "".join(str(cup.label) for cup in cup_circle.all_cups(start))


if __name__ == '__main__':
    CUP_CIRCLE = CupCircle(INPUT)
    CURRENT = CUP_CIRCLE.first
    for move in range(1, 101):
        # print(f"Before move {move}:", cup_labels(CUP_CIRCLE))
        CURRENT = do_move(CURRENT, CUP_CIRCLE)
        # print()
    CUP_LABELS = cup_labels(CUP_CIRCLE, start=1)[1:]
    print(f"Labels on the cups after 1 is {CUP_LABELS}")
    assert ("69473825" == CUP_LABELS)

    INPUT = [int(cup) for cup in INPUT] + [i for i in range(10, 1000000 + 1)]
    CUP_CIRCLE = CupCircle(INPUT)
    CURRENT = CUP_CIRCLE.first
    for move in range(1, 10000001):
        CURRENT = do_move(CURRENT, CUP_CIRCLE)
    CUP1 = CUP_CIRCLE.cups[1]
    RESULT = CUP1.next.label * CUP1.next.next.label
    print(f"Result of multiplication is {RESULT}")
    assert (96604396189 == RESULT)
