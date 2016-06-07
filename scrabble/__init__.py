import gzip
import os
from bisect import bisect_left
from itertools import combinations

_scores = { "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10 }


class Letter(object):
    def __init__(self, letter):
        self.letter = letter

    @property
    def score(self):
        return _scores[self]




class Word(object):
    def __init__(self, word):
        assert isinstance(word, str)
        self.word = word

    @property
    def letters(self):
        return list(self.word)

    @property
    def set(self):
        return list(self.word)


def loadwords():
    with gzip.open(os.path.join(os.path.dirname(__file__), '..',
                                'static', 'zingarelli2005.txt.gz'), 'rt') as fp:
        words = fp.read().split('\n')
    return words



def score_word(word):
    return sum([scores[c] for c in word])


def findwords(rack, words):
    rack = ''.join(sorted(rack))
    foundwords = []
    for i in range(2, len(rack) + 1):
        for comb in combinations(rack, i):
            1/0
            ana = ''.join(comb)
            j = bisect_left(words, ana)
            if j == len(words):
                continue
            words = words[j].split()
            if words[0] == ana:
                foundwords.extend(words[1:])
    return foundwords

#
#
# if __name__ == "__main__":
#     import sys
#
#     if len(sys.argv) == 2:
#         rack = sys.argv[1].strip()
#     else:
