import itertools
from datetime import datetime


def immediately_right(house_first, house_second):
    """House first is immediately right of second if first - second == 1."""
    return house_first - house_second == 1


def next_to(house_first, house_second):
    """Two houses are next to each other if they differ by 1."""
    return abs(house_first - house_second) == 1


def main():
    time_start = datetime.now()
    
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # 1
    orderings = list(itertools.permutations(houses))
    
    for (red, green, ivory, yellow, blue) in orderings:  # color
        for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings:  # nation
            for (dog, snails, fox, horse, ZEBRA) in orderings:  # animal
                for (coffee, tea, milk, oj, WATER) in orderings:  # drink
                    for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings:  # smoke
                        # pass
                        
                        if Englishman is not red: continue  # nation color
                        if Spaniard is not dog: continue  # nation animal
                        if coffee is not green: continue  # drink color
                        if Ukranian is not tea: continue  # nation drink
                        if not immediately_right(green, ivory): continue  # color color
                        if OldGold is not snails: continue  # smoke animal
                        if Kools is not yellow: continue  # smoke color
                        if milk is not middle: continue  # drink drink
                        if Norwegian is not first: continue  # nation nation
                        if not next_to(Chesterfields, fox): continue  # smoke animal
                        if not next_to(Kools, horse): continue  # smoke animal
                        if LuckyStrike is not oj: continue  # smoke drink
                        if Japanese is not Parliaments: continue  # nation smoke
                        if not next_to(Norwegian, blue): continue  # nation color
    
    time_end = datetime.now()
    time_all = (time_end - time_start).total_seconds()
    print('time_all:', time_all)
    # 628.371489 with pass


if __name__ == '__main__':
    main()
