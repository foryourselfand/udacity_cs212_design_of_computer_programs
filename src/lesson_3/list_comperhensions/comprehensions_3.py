def foo(iterable):
    ta_facts_remote = [f'{name} lives in {country} and is the TA for {course}'
                       for name, country, course in iterable
                       if country != 'USA']
    return ta_facts_remote


def main():
    ta_data = [['Peter', 'USA', 'CS262'],
               ['Andy', 'USA', 'CS212'],
               ['Sarah', 'England', 'CS101'],
               ['Gundega', 'Latvia', 'CS373'],
               ['Job', 'USA', 'CS387'],
               ['Sean', 'USA', 'CS253']]
    
    print(*foo(ta_data), sep = '\n', end = '\n\n')


if __name__ == '__main__':
    main()
