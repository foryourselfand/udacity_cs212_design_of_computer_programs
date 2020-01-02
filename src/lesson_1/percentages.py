from dealing import deal
from poker import hand_rank


def percentages(n = 700 * 1000):
    """Sample n random hands and print a table of percentages for each type of hand"""
    counts = [0] * 10
    for i in range(n // 10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(10)):
        print("%d: %6.3f" % (i, 100. * counts[i] / n))


def main():
    percentages()


if __name__ == '__main__':
    main()
