import random

deck_default = [rank + suit for rank in '23456789TJQKA' for suit in 'SHDC']


def deal(hands_number, cards_number = 5, deck = None):
    """Shuffle the deck and deal out numhands n-card hands."""
    if deck is None:
        deck = deck_default
    
    random.shuffle(deck)
    
    return [deck[cards_number * index: cards_number * (index + 1)]
            for index in range(hands_number)]


def main():
    print(deal(2, 7))


if __name__ == '__main__':
    main()
