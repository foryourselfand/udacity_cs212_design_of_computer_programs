import re
from pprint import pprint
from typing import Dict, Set, Tuple


def get_types() -> Dict[str, str]:
    types: Dict[str, str] = dict()
    
    with open('cycling.txt', 'r') as file_cycling:
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
    
    with open('checking.txt', 'r') as file_checking:
        for line in file_checking.read().splitlines():
            pattern_equals = re.compile('if (.*) is not (.*): continue')
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
            pair = (element_first, element_second)
            
            pairs.add(pair)
    return pairs


def main():
    types: Dict[str, str] = get_types()
    pprint(types)
    
    pairs: Set[Tuple[str, str]] = get_pairs()
    pprint(pairs)


if __name__ == '__main__':
    main()
