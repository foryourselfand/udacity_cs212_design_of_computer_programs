def sq(x): print('sq_called', x); return x * x


def main():
    q = (sq(x) for x in range(10) if x % 2 == 0)
    
    print(q)
    
    print(next(q), end = '\n\n')
    print(next(q), end = '\n\n')
    print(next(q), end = '\n\n')
    print(next(q), end = '\n\n')
    print(next(q), end = '\n\n')
    # print(next(q), end = '\n\n')  # StopIteration
    
    for _ in (sq(x) for x in range(10) if x % 2 == 0):
        pass
    print()

    print(list((sq(x) for x in range(10) if x % 2 == 0)))
    print()


if __name__ == '__main__':
    main()
