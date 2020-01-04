import cProfile
import itertools
import re
import time

from time_calls import timed_call


def get_formula_translated(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    # formula_characters = set(re.findall('[A-Z]', formula))
    formula_characters = set(character for character in formula if character.isalpha() and character.isupper())
    translate_from = ''.join(formula_characters)
    
    number_permutations = itertools.permutations('0123456789', len(translate_from))
    for number_permutation in number_permutations:
        translate_to = ''.join(number_permutation)
        translate_table = str.maketrans(translate_from, translate_to)
        formula_translated = formula.translate(translate_table)
        yield formula_translated


def get_solution(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to get_solution it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for formula_translated in get_formula_translated(formula):
        if is_valid(formula_translated):
            yield formula_translated
            



def is_valid(formula_translated):
    """Formula f is is_valid iff it has no numbers with leading zero and eval is true."""
    try:
        return not re.search(r'\b0[0-9]', formula_translated) and eval(formula_translated) is True
        
        # formula_replaced = formula_translated.replace(' + ', ' ').replace(' == ', ' ')
        # formula_splitted = formula_replaced.split(' ')
        
        # for number in formula_splitted:
        #     if len(number) > 1 and number[0] == '0':
        #         return False
        #
        # formula_evaluated = eval(formula_translated)
        # return formula_evaluated
    except ArithmeticError:
        pass
    return False


def test():
    examples = """TWO + TWO == FOUR
    A**2 + B**2 == C**2
    X / X == X
    A**N + B**N == C**N and N > 1
    ATOM**0.5 == A + TO + M
    GLITTERS != GOLD
    ONE < TWO and FOUR < FIVE
    ONE < TWO < THREE
    RAMN == R**3 + RM**3 == N**3 + RX**3
    sum(range(AA)) == BB
    sum(range(POP)) == BOBO
    ODD + ODD == EVEN
    PLUTO not in set([PLANETS])""".splitlines()
    
    time_start = time.time()
    for example in examples:
        solution = timed_call(get_solution, example)
        
        print(example)
        solution_time = solution[0]
        solution_results = solution[1]
        
        solution_first = next(solution_results)
        
        print(solution_first)
        print('%.6f' % solution_time)
        print()
    time_end = time.time()
    time_total = time_end - time_start
    print('%6.4f tot.' % time_total)


def lambdas():
    f = lambda Y, M, E, U, O: (1 * U + 10 * O + 100 * Y) == (1 * E + 10 * M) ** 2
    print(f(1, 2, 3, 4, 5))
    print(f(2, 1, 7, 9, 8))
    print(289 == 17 ** 2)


def main():
    # formula = 'ONE < TWO and FOUR < FIVE'
    # print(f'{formula=}')
    # solution_first = next(get_solution(formula))
    # print(f'{solution_first=}')
    
    # for solution in get_solution(formula):
    #     print(f'{solution=}')
    
    # test()
    cProfile.run('test()')
    # lambdas()


if __name__ == '__main__':
    main()
