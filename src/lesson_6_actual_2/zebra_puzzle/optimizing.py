import re
from collections import Counter, defaultdict
from pprint import pprint
from typing import Dict, Set, Tuple


def get_types() -> Dict[str, str]:
    types: Dict[str, str] = dict()
    
    with open('lesson_6_actual_2/zebra_puzzle/cycling.txt', 'r') as file_cycling:
        for line_raw in file_cycling.read().splitlines():
            line = line_raw.strip()
            
            pattern = re.compile(r'for (.*) in orderings: {2}# (.*)')
            matched = pattern.search(line)
            
            elements_raw = matched.group(1)
            types_raw = matched.group(2)
            
            elements_prepared = elements_raw[1:-1]
            elements_split = elements_prepared.split(', ')
            for element_actual in elements_split:
                types[element_actual] = types_raw
    return types


def get_pairs() -> Set[Tuple[str, str]]:
    pairs: Set[Tuple[str, str]] = set()
    
    with open('lesson_6_actual_2/zebra_puzzle/checking.txt', 'r') as file_checking:
        for line in file_checking.read().splitlines():
            pattern_equals = re.compile('if (.*) != (.*): continue')
            pattern_immediately_right = re.compile('if not immediately_right\((.*), (.*)\): continue')
            pattern_next_to = re.compile('if not next_to\((.*), (.*)\): continue')
            
            match_equals = pattern_equals.search(line)
            match_immediately_right = pattern_immediately_right.search(line)
            match_next_to = pattern_next_to.search(line)
            
            matches = {True if match_temp else False: match_temp for match_temp in (match_equals,
                                                                                    match_immediately_right,
                                                                                    match_next_to)}
            match = matches[True]
            element_first = match.group(1)
            element_second = match.group(2)
            element_second = element_second if element_second not in ['first', 'middle'] else element_first
            
            pair = (element_first, element_second)
            
            pairs.add(pair)
    return pairs


def main():
    types: Dict[str, str] = get_types()
    
    pairs: Set[Tuple[str, str]] = get_pairs()
    
    most_type: Counter[str, int] = Counter()
    most_type_pairs: Counter[str, int] = Counter()
    most_elements: Dict[str, Counter[str, int]] = defaultdict(Counter)
    
    for pair in pairs:
        element_first, element_second = pair
        type_first, type_second = types[element_first], types[element_second]
        most_type[type_first] += 1
        most_type[type_second] += 1
        
        type_pair = f'{type_first} {type_second}'
        most_type_pairs[type_pair] += 1
        
        most_elements[type_first][element_first] += 1
        most_elements[type_second][element_second] += 1

    pprint(most_type, width = 1)
    print()
    
    pprint(most_type_pairs, width = 1)
    print()
    
    pprint(dict(most_elements), width = 1)
    print()
    
if __name__ == '__main__':
    main()

# 19
