import random

mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n = 5, deck = None):
    if deck is None:
        deck = mydeck
    # result = []
    # for i in numhands:
    #     temp = [random.choice(deck) for _ in range(n)]
    #     result.append(" ".join(temp))
    # return result
    random.shuffle(deck)
    return [deck[n * i: n * (i + 1)] for i in range(numhands)]
