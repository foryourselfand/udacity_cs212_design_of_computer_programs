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


def get_solution_faster(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None"""
    f, letters = compile_formula(formula, False)
    for digits in itertools.permutations((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                yield formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose = False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as params of function. For example, 'YOU == ME**2' returns
    (lambda Y, M, E, U, O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'
    So if YOU is a word in the formula, and the function is called with Y
    equals to 0, it should return False.
    For example, 'YOU == ME**2' =>
    lambda E, M, O, U, Y: M!=0 and Y!=0 and ((U*1+O*10+Y*100) == (E*1+M*10)**2)"""
    letters = ''.join(set(re.findall(r'[A-Z]', formula)))
    letters_first = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if letters_first:
        tests = ' and '.join(letter + '!=0' for letter in letters_first)
        body = '%s and (%s)' % (tests, body)
    
    f = 'lambda %s: %s' % (params, body)
    if verbose:
        print(f)
    return eval(f), letters


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


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') -> '+'"""
    if word.isupper():
        terms = []
        for index, character in enumerate(word[::-1]):
            terms.append(f'{character}*{10 ** index}')
        return f'({"+".join(terms)})'
    else:
        return word


def main():
    formula = 'YOU == ME**2'
    print(f'{formula=}')
    solution_first = next(get_solution_faster(formula))
    print(f'{solution_first=}')
    
    # for solution in get_solution(formula):
    #     print(f'{solution=}')
    
    # test()
    # lambdas()
    # cProfile.run('test()')


if __name__ == '__main__':
    main()
