def search(pattern, text):
    """Return True if pattern appears anywhere in text."""
    if pattern.startswith('^'):
        return match(pattern[1:], text)
    else:
        return match('.*' + pattern, text)


def match(pattern, text):
    """Return True if pattern appears at the start of text."""
    if pattern == '':
        return True
    elif pattern == '$':
        return text == ''
    elif len(pattern) > 1 and pattern[1] in '*?':
        p, op, pat = pattern[0], pattern[1], pattern[2:]
        if op == '*':
            return match_star(p, pat, text)
        elif op == '?':
            if match1(p, text) and match(pat, text[1:]):
                return True
            else:
                return match(pat, text)
    else:
        return match1(pattern[0], text) and match(pattern[1:], text[1:])


def match1(pattern, text):
    """Return True if first character of text matched pattern character p."""
    if not text: return False
    return pattern == '.' or pattern == text[0]


def match_star(p, pattern, text):
    """Return True if any number of char p
    followed by pattern, matches text."""
    return match(pattern, text) or (match1(p, text) and match_star(p, pattern, text[1:]))


def test():
    assert search('baa*!', 'Sheep said baaaa!')
    assert search('baa*!', 'Sheep said baaaa humbug') == False
    assert match('baa*!', 'Sheep said baaaa!') == False
    assert match('baa*!', 'baaaa! said the sheep')
    assert search('def', 'abcdefg')
    assert search('def$', 'abcdef')
    assert search('def$', 'abcdefg') == False
    assert search('^start', 'not the start') == False
    assert match('a*b*c*', 'just anything')
    assert match('x?', 'text')
    assert match('text?', 'text')
    assert match('text?', 'tex')
    
    def words(text): return text.split()
    
    assert all(match('aa*bb*cc*$', s) for s in words('abc aaabbccc aaaabcccc'))
    assert not any(match('aa*bb*cc*$', s) for s in words('ac aaabbcccd aaaa-b-cccc'))
    assert all(search('^ab.*aca.*a$', s) for s in words('abracadabra abacaa about-acacia-fa'))
    assert not any(search('t.p', s) for s in words('TYPE teepee tp'))
    
    return 'test passes'


def main():
    print(test())


if __name__ == '__main__':
    main()
