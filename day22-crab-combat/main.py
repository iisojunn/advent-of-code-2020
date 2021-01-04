"""Day 22 Advent of Code"""
import queue


def read_input():
    with open("input", "r") as input_file:
        return parse_decks(input_file.read())


def parse_decks(data):
    return tuple(create_deck(deck_data) for deck_data in data.split("\n\n"))


def create_deck(deck_data):
    deck = queue.Queue()
    for card in deck_data.splitlines():
        if card.isdigit():
            deck.put(int(card))
    return deck


def play(deck1, deck2):
    while not game_over(deck1, deck2):
        play_round(deck1, deck2)


def game_over(deck1, deck2):
    return deck1.empty() or deck2.empty()


def play_round(deck1, deck2):
    card1 = deck1.get()
    card2 = deck2.get()
    if card1 > card2:
        deck1.put(card1)
        deck1.put(card2)
    else:
        deck2.put(card2)
        deck2.put(card1)


def get_winner(deck1, deck2):
    if not deck1.empty():
        return deck1
    return deck2


def calculate_score(deck1, deck2):
    win_deck = get_winner(deck1, deck2)
    score = 0
    while not win_deck.empty():
        multiplier = win_deck.qsize()
        score += multiplier * win_deck.get()
    return score


if __name__ == '__main__':
    DECK1, DECK2 = read_input()
    play(DECK1, DECK2)
    SCORE = calculate_score(DECK1, DECK2)
    print(f"Winning player score is {SCORE}")
