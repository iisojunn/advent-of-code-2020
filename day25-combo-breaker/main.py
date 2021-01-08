"""Day 25 Advent of code 2020"""

DIVISOR = 20201227
CARD_PUBLIC = 3248366
DOOR_PUBLIC = 4738476


def resolve_card_loops(card_public):
    value = 1
    loops = 0
    while value != card_public:
        value = (value * 7) % DIVISOR
        loops += 1
    return loops


def resolve_encryption_key(card_loops, door_public):
    value = 1
    for _ in range(0, card_loops):
        value = (value * door_public) % DIVISOR
    return value


if __name__ == '__main__':
    CARD_LOOPS = resolve_card_loops(CARD_PUBLIC)
    ENCRYPTION_KEY = resolve_encryption_key(CARD_LOOPS, DOOR_PUBLIC)
    print(f"Encryption key is {ENCRYPTION_KEY}")
