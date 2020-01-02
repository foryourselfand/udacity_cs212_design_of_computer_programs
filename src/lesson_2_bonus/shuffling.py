import random
from collections import defaultdict
from math import factorial


def shuffle_bad1(deck):
    """My teacher's algorithm."""
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle_bad2(deck):
    """A modification of my teacher's algorithm."""
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        swap(deck, i, j)


def shuffle_bad3(deck):
    """An easier modification of my teacjer's algorith."""
    N = len(deck)
    for i in range(N):
        swap(deck, i, random.randrange(N))


def shuffle_good(deck):
    """Knuth's Algorithm P."""
    N = len(deck)
    for i in range(N - 1):
        swap(deck, i, random.randrange(i, N))


def swap(deck, i, j):
    """Swap elements i and j of a collection"""
    # print(f'swap {i} {j}')
    deck[i], deck[j] = deck[j], deck[i]


def test_shuffler(shuffler, deck = 'abcd', n = 10000):
    counts = defaultdict(int)
    for _ in range(n):
        input_list = list(deck)
        shuffler(input_list)
        counts[''.join(input_list)] += 1
    e = n * 1. / factorial(len(deck))  # expected count
    ok = all((0.9 <= counts[item] / e <= 1.1) for item in counts)
    name = shuffler.__name__
    print('%s(%s) %s' % (name, deck, 'ok' if ok else '*** BAD ***'))
    for item, count in sorted(counts.items()):
        print('%s:%4.1f' % (item, count * 100 / n), end = '\t')
    print()


def test_shufflers(shufflers = None, decks = None):
    if shufflers is None:
        shufflers = [shuffle_good, shuffle_bad1, shuffle_bad2, shuffle_bad3]
    if decks is None:
        decks = ['abc', 'ab']
    for deck in decks:
        for shuffler in shufflers:
            test_shuffler(shuffler, deck)
            print()
        print()


def main():
    # deck = list(range(1, 11))
    # shuffle_good(deck)
    # pprint(deck)
    
    test_shufflers()


if __name__ == '__main__':
    main()
