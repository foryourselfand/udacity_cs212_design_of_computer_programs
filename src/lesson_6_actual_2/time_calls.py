import time

from brute_force import zebra_puzzle_my_cycling, zebra_puzzle_my_generator, zebra_puzzle_their


def timed_call(function, *args, **kwargs):
    """Call function with args; return the time in seconds and result."""
    time_start = time.time()
    result = function(*args, **kwargs)
    time_end = time.time()
    return time_end - time_start, result


def timed_calls(n, function, *args, **kwargs):
    """Call function n times with args; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timed_call(function, *args, **kwargs)[0] for _ in range(n)]
    else:
        times = []
        
        while sum(times) <= n:
            time_temp = timed_call(function, *args, **kwargs)[0]
            times.append(time_temp)
    
    return min(times), average(times), max(times)


def average(numbers):
    """Return the average (arithmetic mean) of a sequence of numbers."""
    return sum(numbers) / len(numbers)


# def c(sequence):
#     """Generate items in sequence; keeping counts as we go. c.starts is the
#     number of sequences started; c.items in number if items generated."""
#     c.start += 1
#     for item in sequence:
#         c.items += 1
#         yield item
#
#
# def instrument_function(function, *args, **kwargs):
#     c.start, c.items = 0, 0
#     result = function(*args, **kwargs)
#     print('%s got %s with %5d iterations over %7d items' % (function.__name__, result, c.start, c.items))


def main():
    n = 100
    
    print('%.5f %.5f %.5f' % timed_calls(n, zebra_puzzle_my_cycling))
    print('%.5f %.5f %.5f' % timed_calls(n, zebra_puzzle_my_generator))
    print('%.5f %.5f %.5f' % timed_calls(n, zebra_puzzle_their))


if __name__ == '__main__':
    main()
