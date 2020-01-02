def foo(iterable):
    ta_facts = [f'{name} lives in {country} and is the TA for {course}'
                for name, country, course in iterable]
    return ta_facts


def bar(iterable):
    # ta_countries = [f'{name} lives in {country}' for name, country in iterable]
    ta_countries = [f'{name} lives in {country}' for name, country, course in iterable]
    # ta_countries = [f'{x} lives in {y}' for x, y, z in iterable]
    return ta_countries


def main():
    ta_data = [('Peter', 'USA', 'CS262'),
               ('Andy', 'USA', 'CS212'),
               ('Sarah', 'England', 'CS101'),
               ('Gundega', 'Latvia', 'CS373'),
               ('Job', 'USA', 'CS387'),
               ('Sean', 'USA', 'CS253')]
    
    print(*foo(ta_data), sep = '\n', end = '\n\n')
    print(*bar(ta_data), sep = '\n', end = '\n\n')


if __name__ == '__main__':
    main()
