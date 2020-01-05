import cProfile

from time_calls import timed_calls


def longest_subpalindrome_slice_my(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    text = text.lower()
    
    if len(text) == 0:
        return 0, 0
    elif len(text) == 1:
        return 0, 1
    
    max_len = 1
    max_i, max_j = 0, 1
    start_i, start_j = 0, 1
    text_len = len(text)
    
    while True:
        current_i, current_j = start_i, start_j
        
        while True:
            is_palindrom_found = text[current_i] == text[current_j]
            if is_palindrom_found:
                current_len = current_j - current_i
                if current_len >= max_len:
                    max_len = current_len
                    max_i, max_j = current_i, current_j + 1
                
                current_i -= 1
                current_j += 1
            if not is_palindrom_found or current_i < 0 or current_j > text_len - 1:
                break
        
        start_mod = (start_i + start_j) % 2
        if start_mod % 2 == 0:
            start_i += 1
        elif start_mod % 2 == 1:
            start_j += 1
        
        if start_i > text_len - 2 or start_j > text_len - 1:
            break
    
    return max_i, max_j


def longest_subpalindrome_slice_their(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    if text == '': return 0, 0
    
    def length(slicing): a, b = slicing; return b - a
    
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start + 1)]
    return max(candidates, key = length)


def grow(text, start, end):
    """Start with a 0- or 1- length palindrome; try to grow a bigger one."""
    while start > 0 and end < len(text) and text[start - 1].upper() == text[end].upper():
        start -= 1
        end += 1
    return start, end


def test(longest_subpalindrome_slice):
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('Race carr') == (7, 9)
    return 'tests pass'


def main():
    # print(test())
    # print(longest_subpalindrome_slice_my('Race carr'))
    # cProfile.run("test()")
    n = 10000
    print('%.5f %.5f %.5f' % timed_calls(n, test, longest_subpalindrome_slice_my))
    print('%.5f %.5f %.5f' % timed_calls(n, test, longest_subpalindrome_slice_their))


if __name__ == '__main__':
    main()
