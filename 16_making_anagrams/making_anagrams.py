from collections import Counter

# a = 'fcrxzwscanmligyxyvym'
# b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'


def solution(a, b):
    counter = 0
    scanned_chars = []
    for char in a:
        if char not in b:
            counter += 1
        else:
            if char not in scanned_chars:
                if a.count(char) > b.count(char):
                    counter += a.count(char) - b.count(char)
        scanned_chars.append(char)

    scanned_chars = []
    for char in b:
        if char not in a:
            counter += 1
        else:
            if char not in scanned_chars:
                if b.count(char) > a.count(char):
                    counter += b.count(char) - a.count(char)
        scanned_chars.append(char)
    return counter


def solution_2(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())


