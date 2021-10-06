from collections import Counter


def solution(logo):
    """Example: 'google'
        we already ordered the list alphabetically,
        so if the occurrence count is the same,
        it will return in alphabetical order
    """
    chars = list(logo)
    chars.sort()
    chars_collection = Counter(chars)

    for letter, frequency in chars_collection.most_common(3):
        print(letter, frequency)