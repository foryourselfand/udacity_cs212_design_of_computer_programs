import collections
from pprint import pprint


def main():
    result_single = collections.Counter()
    result_pair = collections.Counter()
    
    with open('pairs.txt', 'r') as file:
        for line in file.read().splitlines():
            line_split = line.split(' ')
            
            result_pair[line] += 1
            result_single[line_split[0]] += 1
            result_single[line_split[1]] += 1
    
    pprint(result_single, width = 1)
    pprint(result_pair, width = 1)


if __name__ == '__main__':
    main()
