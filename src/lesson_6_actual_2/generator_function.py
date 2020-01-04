def ints(start, end = None):
    i = start
    while end is None or i <= end:
        yield i
        i += 1


def all_ints():
    """Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."""
    # number_last = 0
    # while True:
    #     if number_last == 0:
    #         yield 0
    #         number_last += 1
    #     elif number_last >= 1:
    #         number_last *= -1
    #     elif number_last <= -1:
    #         number_last *= -1
    #         number_last += 1
    #     yield number_last
    
    # yield 0
    # i = 1
    # while True:
    #     yield +i
    #     yield -i
    #     i += 1
    
    yield 0
    for i in ints(1):
        yield +i
        yield -i


def main():
    # temp = ints(0, 10)
    # for elem in temp:
    #     print(elem)
    
    generator = all_ints()
    for _ in range(10):
        print(next(generator))


if __name__ == '__main__':
    main()
