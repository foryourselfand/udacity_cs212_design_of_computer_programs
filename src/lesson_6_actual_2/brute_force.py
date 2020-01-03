import itertools
from datetime import datetime


def immediately_right(house_first, house_second):
    """House first is immediately right of second if first - second == 1."""
    return house_first - house_second == 1


def next_to(house_first, house_second):
    """Two houses are next to each other if they differ by 1."""
    return abs(house_first - house_second) == 1


def zebra_puzzle():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # 1
    orderings = list(itertools.permutations(houses))
    
    for (red, green, ivory, yellow, blue) in orderings:  # color
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:  # nation
            for (dog, snails, fox, horse, ZEBRA) in orderings:  # animal
                for (coffee, tea, milk, oj, WATER) in orderings:  # drink
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:  # smoke
                        
                        if Englishman is not red: continue
                        if Spaniard is not dog: continue
                        if coffee is not green: continue
                        if Ukranian is not tea: continue
                        if not immediately_right(green, ivory): continue
                        if OldGold is not snails: continue
                        if Kools is not yellow: continue
                        if milk is not middle: continue
                        if Norwegian is not first: continue
                        if not next_to(Chesterfields, fox): continue
                        if not next_to(Kools, horse): continue
                        if LuckyStrike is not oj: continue
                        if Japanese is not Parliaments: continue
                        if not next_to(Norwegian, blue): continue


def main():
    time_start = datetime.now()
    
    zebra_puzzle()
    
    time_end = datetime.now()
    time_all = (time_end - time_start).total_seconds()
    print('time_all:', time_all)
    
    # 628.371489 with pass


if __name__ == '__main__':
    main()
