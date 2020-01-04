import math


def main():
    print(1 is 1)
    print(1 is 1 ** 1)
    print(1 is int(math.pow(1, 1)))
    print()
    
    print(100000 is 100000)
    print(100000 is 100000 ** 1)
    print(100000 is int(math.pow(100000, 1)))
    print()


if __name__ == '__main__':
    main()

'''
Integer first = new Integer(1);
Integer second = new Integer(1);

first == second True


//---//

Integer first = new Integer(1000);
Integer second = new Integer(1000);

first == second False
'''
