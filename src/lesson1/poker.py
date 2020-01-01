def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key = hand_rank)


def allmax(iterable, key = None):
    """Return a list of all items equal to the max of the iterable."""
    # result = []
    #
    # max_element = max(iterable, key = key)
    # max_value = key(max_element)
    # for element in iterable:
    #     max_temp = key(element)
    #     if max_value == max_temp:
    #         result.append(element)
    #
    # return result
    
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    """Return a value indicating the ranking hand."""
    # ranks = card_ranks(hand)
    # if straight(ranks) and flush(hand):  # straight flush
    #     return 8, max(ranks)
    # elif kind(4, ranks):  # 4 of a kind
    #     return 7, kind(4, ranks), kind(1, ranks)
    # elif kind(3, ranks) and kind(2, ranks):  # full house
    #     return 6, kind(3, ranks), kind(2, ranks)
    # elif flush(hand):  # flush
    #     return 5, ranks
    # elif straight(ranks):  # straight
    #     return 4, max(hand)
    # elif kind(3, ranks):  # 3 of a kind
    #     return 3, kind(3, ranks), ranks
    # elif two_pair(ranks):  # 2 pair
    #     return 2, two_pair(ranks), ranks
    # elif kind(2, ranks):  # kind
    #     return 1, kind(2, ranks), ranks
    # else:  # high card
    #     return 0, ranks
    
    # counts is the count of each rank; ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    
    groups = group(['--23456789TJQKA'.index(rank) for rank, suit in hand])
    counts, ranks = unzip(groups)
    
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([suit for rank, suit in hand])) == 1
    
    return max(count_rankings[counts], 4 * straight + 5 * flush), ranks


count_rankings = {(5,):            10,
                  (4, 1):          7,
                  (3, 2):          6,
                  (3, 1, 1):       3,
                  (2, 2, 1):       2,
                  (2, 1, 1, 1):    1,
                  (1, 1, 1, 1, 1): 0}


def group(items):
    """Return a list of [(count, x)...], highest count first, then highest x first"""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)


def unzip(pairs):
    return zip(*pairs)


# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function
#                  returns their corresponding ranks as a
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks
#                  in a hand (where the order goes from
#                  highest to lowest rank).


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    # ranks_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    # ranks_input = [rank for rank, suit in cards]
    #
    # ranks_result = []
    # for rank_input in ranks_input:
    #     rank_result: int = 0
    #
    #     if rank_input in ranks_dict.keys():
    #         rank_result = ranks_dict[rank_input]
    #     else:
    #         rank_result = int(rank_input)
    #
    #     ranks_result.append(rank_result)
    #
    # ranks_result.sort(reverse = True)
    # return ranks_result
    
    ranks = ['--23456789TJQKA'.index(rank) for rank, suit in hand]
    ranks.sort(reverse = True)
    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    return ranks


def straight(ranks):
    """Return True if the ordered ranks from a 5-card straight."""
    # for rank_previous, rank_current in zip(ranks, ranks[1:]):
    #     if rank_previous - rank_current != 1:
    #         return False
    # return True
    return max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5


def flush(hand):
    """Return True if all the cards have the same suit."""
    # suits = [suit for rank, suit in hand]
    # suit_first = suits[0]
    # for suit_current in suits[1:]:
    #     if suit_current != suit_first:
    #         return False
    # return True
    suits = [suit for rank, suit in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if the is no n-of-a-kind in the hand"""
    # result = dict()
    #
    # for rank in ranks:
    #     if rank not in result.keys():
    #         result[rank] = 0
    #     result[rank] += 1
    #
    # for rank, number in result.items():
    #     if number == n:
    #         return rank
    # return None
    
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # pair_first = kind(2, ranks)
    # if not pair_first:
    #     return None
    #
    # ranks_without_first_pair = [rank for rank in ranks if rank != pair_first]
    # pair_second = kind(2, ranks_without_first_pair)
    # if not pair_second:
    #     return None
    #
    # return max(pair_first, pair_second), min(pair_first, pair_second)
    
    pair_high = kind(2, ranks)
    pair_low = kind(2, list(reversed(ranks)))
    if pair_high and pair_high != pair_low:
        return pair_high, pair_low
    return None


def test():
    """Test cases for the functions in poker program."""
    sf = '6C 7C 8C 9C TC'.split()  # Straight Flush
    fk = '9D 9H 9S 9C 7D'.split()  # Four of a Kind
    fh = 'TD TC TH 7C 7D'.split()  # Full House
    tp = '5C 5D 9H 9C 6S'.split()  # Two Pair
    s1 = 'AS 2S 3S 4S 5C'.split()  # A-5 straight
    s2 = '2C 3C 4C 5S 6S'.split()  # 2-6 straight
    ah = 'AS 2S 3S 4S 6C'.split()  # A high
    sh = '2S 4S 4S 6C 7D'.split()  # 7 high
    
    # print(poker([s1, s2, ah, sh]))
    # assert poker([s1, s2, ah, sh]) == s2
    
    fk_ranks = card_ranks(fk)
    tp_ranks = card_ranks(tp)
    
    assert kind(4, fk_ranks) == 9
    assert kind(3, fk_ranks) is None
    assert kind(2, fk_ranks) is None
    assert kind(1, fk_ranks) == 7
    
    assert two_pair(fk_ranks) is None
    assert two_pair(tp_ranks) == (9, 5)
    
    assert straight([9, 8, 7, 6, 5]) is True
    assert straight([9, 8, 8, 6, 5]) is False
    
    assert flush(sf) is True
    assert flush(fk) is False
    
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    # assert poker([sf for _ in range(100)]) == sf
    assert poker([sf] + 99 * [fh]) == sf
    
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    
    return 'tests pass'


def main():
    print(test())
    # print(max([3, 4, 5, 0]), max([3, 4, -5, 0], key = abs))
    # print(card_ranks(['AC', '3D', '4S', 'KH']))
    
    # print(poker([['6C', '7C', '8C', '9C', 'TC'], ['6D', '7D', '8D', '9D', 'TD'], ['9D', '9H', '9S', '9C', '7D'],
    #              ['TD', 'TC', 'TH', '7C', '7D']]))
    # print(*deal(10, 10), sep = '\n')


if __name__ == '__main__':
    main()
