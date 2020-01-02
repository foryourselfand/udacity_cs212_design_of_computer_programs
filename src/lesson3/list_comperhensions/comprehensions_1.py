def foo(iterable):  # BAD UGLY SLOW
    uppercase_tas = []
    for index in range(len(iterable)):
        uppercase_tas.append(iterable[index].upper())
    return uppercase_tas


def bar(iterable):
    return [name.upper() for name in iterable]


def main():
    udacity_tas = ['Peter', 'Andy', 'Sarah', 'Gundega', 'Job', 'Sean']
    
    print(*foo(udacity_tas), sep = '\n', end = '\n\n')
    print(*bar(udacity_tas), sep = '\n', end = '\n\n')
