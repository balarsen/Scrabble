import gzip
import os
from bisect import bisect_left
from itertools import combinations
from operator import itemgetter, attrgetter


import numpy as np

_scores = { "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
            "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
            "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
            "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
            "x": 8, "z": 10 }

for k in _scores.keys():
    _scores[k.capitalize()] = _scores[k]


def getwords(rack, anadict):
    rack = ''.join(sorted(rack))
    foundwords = []
    for i in range(2, len(rack) + 1):
        for comb in combinations(rack, i):
            ana = ''.join(comb)
            1 / 0


def findwords(rack, anadict, wordsdict):
    rack = ''.join(sorted(rack))
    foundwords = []
    for i in range(2, len(rack) + 1):
        for comb in combinations(rack, i):
            ana = ''.join(comb)
            j = bisect_left(anadict, ana)
            if j == len(anadict):
                # 1/0
                continue
            words = anadict[j].split()
            # 1/0
            if words[0] == ana:
                foundwords.append((wordsdict[j], score_a_word(wordsdict[j])))
    return foundwords

def get_max_word(rack, words, swords):
    fwords = findwords(rack, swords, words)
    # pqdata = map(itemgetter(1), fwords)
    return max(fwords, key=lambda x: x[1])



def score_a_word(word):
    """
    given a word get its score
    """
    return sum([_scores[c] for c in word])


def sort_lists(words, swords):
    ind = np.argsort(swords)
    words = [words[i] for i in ind]
    swords = [swords[i] for i in ind]
    return words, swords


def loadwords():
    with gzip.open(os.path.join(os.path.dirname(__file__), '..',
                                'static', 'zingarelli2005.txt.gz'), 'rt') as fp:
        words = fp.read().split('\n')
    words = sorted([v.strip() for v in words if len(v) <= 7])
    return words


def loadwords_sorted():
    with gzip.open(os.path.join(os.path.dirname(__file__), '..',
                                'static', 'zingarelli2005_sorted.txt.gz'), 'rt') as fp:
        words = fp.read().split('\n')
    words = sorted([v.strip() for v in words])
    return words


def make_sorted_words(words):
    words = loadwords()
    # sort all the words
    swords = [''.join(sorted(v)) for v in words]
    return swords


def make_sorted_file(words):
    words = loadwords()
    # sort all the words
    swords = [''.join(sorted(v)) for v in words]

    with gzip.open(os.path.join(os.path.dirname(__file__), '..',
                                'static', 'zingarelli2005_sorted.txt.gz'), 'wt') as f:
        for v in swords:
            f.write(v + '\n')
