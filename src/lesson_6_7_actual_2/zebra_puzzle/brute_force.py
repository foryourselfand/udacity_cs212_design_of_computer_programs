import itertools


def immediately_right(house_first, house_second):
    """House first is immediately right of second if first - second == 1."""
    return house_first - house_second == 1


def next_to(house_first, house_second):
    """Two houses are next to each other if they differ by 1."""
    return abs(house_first - house_second) == 1


def zebra_puzzle_my_cycling():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]  # 1
    orderings = list(itertools.permutations(houses))
    
    for (Kools, OldGold, Chesterfields, LuckyStrike, Parliaments) in orderings:  # SMOKE
        for (dog, snails, fox, horse, ZEBRA) in orderings:  # ANIMAL
            
            if OldGold != snails: continue  # smoke animal
            if not next_to(Chesterfields, fox): continue  # smoke animal
            if not next_to(Kools, horse): continue  # smoke animal
            
            for (Norwegian, Englishman, Spaniard, Ukranian, Japanese) in orderings:  # NATION
                if Norwegian != first: continue  # nation nation
                if Spaniard != dog: continue  # nation animal
                if Japanese != Parliaments: continue  # nation smoke
                
                for (green, red, ivory, yellow, blue) in orderings:  # COLOR
                    if not immediately_right(green, ivory): continue  # color color
                    
                    if Englishman != red: continue  # nation color
                    if not next_to(Norwegian, blue): continue  # nation color
                    if Kools != yellow: continue  # smoke color
                    
                    for (milk, coffee, tea, orange_juice, WATER) in orderings:  # DRINK
                        if milk != middle: continue  # drink drink
                        
                        if coffee != green: continue  # drink color
                        if Ukranian != tea: continue  # nation drink
                        if LuckyStrike != orange_juice: continue  # smoke drink
                        
                        return WATER, ZEBRA


def zebra_puzzle_my_generator():
    """Return a tuple (WATER, ZEBRA) indicating """
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (Kools, OldGold, Chesterfields, LuckyStrike, Parliaments) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
    
                if OldGold is snails
                if next_to(Chesterfields, fox)
                if next_to(Kools, horse)
    
                for (Norwegian, Englishman, Spaniard, Ukranian, Japanese) in orderings
    
                if Norwegian is first
                if Spaniard is dog
                if Japanese is Parliaments
    
                for (green, red, ivory, yellow, blue) in orderings
    
                if immediately_right(green, ivory)
                if Englishman is red
                if next_to(Norwegian, blue)
                if Kools is yellow
    
                for (milk, coffee, tea, orange_juice, WATER) in orderings
    
                if milk is middle
                if coffee is green
                if Ukranian is tea
                if LuckyStrike is orange_juice
                )


def zebra_puzzle_their():
    """Return a tuple (WATER, ZEBRA) indicating """
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
    
                if immediately_right(green, ivory)  # 6
    
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
    
                if Englishman is red  # 2
                if Norwegian is first  # 10
                if next_to(Norwegian, blue)  # 15
    
                for (coffee, tea, milk, orange_juice, WATER) in orderings
    
                if coffee is green  # 4
                if Ukranian is tea  # 5
                if milk is middle  # 9
    
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
    
                if Kools is yellow  # 8
                if LuckyStrike is orange_juice  # 13
                if Japanese is Parliaments  # 14
    
                for (dog, snails, fox, horse, ZEBRA) in orderings
    
                if Spaniard is dog  # 3
                if OldGold is snails  # 7
                if next_to(Chesterfields, fox)  # 11
                if next_to(Kools, horse)  # 12
                )


def main():
    water, zebra = zebra_puzzle_my_cycling()
    # water, zebra = zebra_puzzle_my_generator()
    # water, zebra = zebra_puzzle_their()
    print(f'{water=}')
    print(f'{zebra=}')


if __name__ == '__main__':
    main()
