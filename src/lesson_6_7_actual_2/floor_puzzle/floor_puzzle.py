import itertools


def is_adjacent(floor_first, floor_second):
    return abs(floor_first - floor_second) == 1


def floor_puzzle_my():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = itertools.permutations(floors)
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if Hopper == top: continue
        if Kay == bottom: continue
        if Liskov == top or Liskov == bottom: continue
        if Perlis <= Kay: continue
        if is_adjacent(Ritchie, Liskov): continue
        if is_adjacent(Liskov, Kay): continue
        return [Hopper, Kay, Liskov, Perlis, Ritchie]


def floor_puzzle_their():
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings:
        if (Hopper is not top
                and Kay is not bottom
                and Liskov is not top
                and Liskov is not bottom
                and Perlis > Kay
                and abs(Ritchie - Liskov) > 1
                and abs(Liskov - Kay) > 1):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]


def main():
    solution_my = floor_puzzle_my()
    solution_their = floor_puzzle_their()
    
    print(f'{solution_my=}')
    print(f'{solution_their=}')


if __name__ == '__main__':
    main()
