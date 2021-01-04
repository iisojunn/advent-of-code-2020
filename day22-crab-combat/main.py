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


def play_combat(deck1, deck2):
    while not game_over(deck1, deck2):
        play_round(deck1, deck2)
    return get_win_deck(deck1, deck2)


def game_over(deck1, deck2):
    return deck1.empty() or deck2.empty()


def play_round(deck1, deck2):
    card1 = deck1.get()
    card2 = deck2.get()
    player1_won_round = card1 > card2
    place_cards_after_round(card1, card2, deck1, deck2, player1_won_round)


def place_cards_after_round(card1, card2, deck1, deck2, player1_won_round):
    if player1_won_round:
        deck1.put(card1)
        deck1.put(card2)
    else:
        deck2.put(card2)
        deck2.put(card1)


def get_win_deck(deck1, deck2):
    if player1_winner(deck1):
        return deck1
    return deck2


def player1_winner(deck1):
    return not deck1.empty()


def calculate_score(win_deck):
    score = 0
    while not win_deck.empty():
        multiplier = win_deck.qsize()
        score += multiplier * win_deck.get()
    return score


def play_recursive_combat(deck1, deck2):
    play_recursive_game(deck1, deck2)
    return get_win_deck(deck1, deck2)


def play_recursive_game(deck1, deck2):
    played_rounds = {"1": [], "2": []}
    while not game_over(deck1, deck2):
        if is_instant_win_for_player_1(deck1, deck2, played_rounds):
            return True
        play_recursive_round(deck1, deck2)
    return player1_winner(deck1)


def is_instant_win_for_player_1(deck1, deck2, played_rounds):
    order1 = card_order(deck1)
    order2 = card_order(deck2)
    game_over_ = order1 in played_rounds["1"] or order2 in played_rounds["2"]
    played_rounds["1"].append(order1)
    played_rounds["2"].append(order2)
    return game_over_


def card_order(deck):
    size = deck.qsize()
    cards = []
    for _ in range(size):
        card = deck.get()
        cards.append(card)
        deck.put(card)
    return tuple(cards)


def play_recursive_round(deck1, deck2):
    card1 = deck1.get()
    card2 = deck2.get()
    if sub_game_needed(card1, card2, deck1, deck2):
        player1_won_round = play_recursive_game(copy_deck(deck1, card1),
                                                copy_deck(deck2, card2))
    else:
        player1_won_round = card1 > card2
    place_cards_after_round(card1, card2, deck1, deck2, player1_won_round)


def sub_game_needed(card1, card2, deck1, deck2):
    return deck1.qsize() >= card1 and deck2.qsize() >= card2


def copy_deck(deck, card_amount):
    new_deck = queue.Queue()
    cards = deck.qsize()
    for _ in range(cards):
        card = deck.get()
        deck.put(card)
        if new_deck.qsize() < card_amount:
            new_deck.put(card)
    return new_deck


if __name__ == '__main__':
    DECK1, DECK2 = read_input()
    WIN_DECK = play_combat(DECK1, DECK2)
    SCORE = calculate_score(WIN_DECK)
    print(f"Winning player score is {SCORE}")

    DECK1, DECK2 = read_input()
    WIN_DECK = play_recursive_combat(DECK1, DECK2)
    SCORE = calculate_score(WIN_DECK)
    print(f"Winning player score in recursive combat is {SCORE}")
