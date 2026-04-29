#%%
from collections import defaultdict
from itertools import combinations, combinations_with_replacement
from os import path as ospath


WORDLIST = "./dolph/enable1.txt"
# WORDLIST = "./dolph/popular.txt"
# WORDLIST = "./dolph/ospd.txt"
# WORDLIST = "./samplewords.txt"
# WORDLIST = "../biclique/2of12.txt"
# WORDLIST = "../biclique/scrabble dictionary.txt"
# WORDLIST = "../biclique/medical wordlist.txt"
# WORDLIST = "../biclique/enwiki-2023-04-13.txt"

CLIQUE_SIZE = 5
MAX_RESULTS = 100


def load_words(filepath):
    script_dir = ospath.dirname(__file__)
    with open(ospath.join(script_dir, filepath), "r", encoding="utf-8") as file:
        return file.read().split()


def edge_pairs(word):
    edges = set()
    for a, b in zip(word, word[1:]):
        if a == b:
            continue
        edges.add(tuple(sorted((a, b))))
    return frozenset(edges)


def valid_letters(word):
    return all("a" <= c <= "z" for c in set(word))


words = load_words(WORDLIST)

# Bucket by unique-letter set, then by internal edge set.
# For word pairs, we only union the adjacencies from each word separately:
# no edge is added across the space between the two words.
buckets = defaultdict(lambda: defaultdict(list))
for word in words:
    letters = frozenset(word)
    if len(letters) < 2 or len(letters) > CLIQUE_SIZE:
        continue
    if not valid_letters(word):
        continue
    buckets[letters][edge_pairs(word)].append(word)


matches = []
lettersets = list(buckets)
for letters_1, letters_2 in combinations_with_replacement(lettersets, 2):
    union_letters = letters_1 | letters_2
    if len(union_letters) != CLIQUE_SIZE:
        continue

    needed_edges = frozenset(tuple(sorted(pair)) for pair in combinations(sorted(union_letters), 2))
    edge_buckets_1 = buckets[letters_1]
    edge_buckets_2 = buckets[letters_2]

    for edges_1, words_1 in edge_buckets_1.items():
        missing_edges = needed_edges - edges_1
        for edges_2, words_2 in edge_buckets_2.items():
            if not missing_edges.issubset(edges_2):
                continue

            for word_1 in words_1:
                for word_2 in words_2:
                    matches.append((word_1, word_2))
                    if len(matches) >= MAX_RESULTS:
                        break
                if len(matches) >= MAX_RESULTS:
                    break
            if len(matches) >= MAX_RESULTS:
                break
        if len(matches) >= MAX_RESULTS:
            break
    if len(matches) >= MAX_RESULTS:
        break


print(f"Wordlist: {WORDLIST}")
print(f"K{CLIQUE_SIZE} pair matches found: {len(matches)}")
for word_1, word_2 in matches:
    print(f"{word_1} | {word_2}")
