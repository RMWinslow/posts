#%%
from collections import defaultdict


WORDLIST = "./dolph/enable1.txt"
# WORDLIST = "./dolph/popular.txt"
# WORDLIST = "./dolph/ospd.txt"
# WORDLIST = "./samplewords.txt"
# WORDLIST = "../biclique/2of12.txt"
# WORDLIST = "../biclique/scrabble dictionary.txt"
# WORDLIST = "../biclique/medical wordlist.txt"
WORDLIST = "../biclique/enwiki-2023-04-13.txt"

CLIQUE_SIZE = 5




def load_words(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().split()


def is_clique_word(word, N=4):

    # First check that there are exactly N unique letters
    if not len(set(word)) == N:
        return False

    connections = defaultdict(set)
    for a, b in zip(word, word[1:]):
        if a == b:
            continue
        connections[a].add(b)
        connections[b].add(a)

    return all(len(connections[letter]) == N-1 for letter in set(word))




words = load_words(WORDLIST)

matches = []
for word in words:
    if is_clique_word(word,CLIQUE_SIZE):
        matches.append(word)

print(f"Wordlist: {WORDLIST}")
print(f"K{CLIQUE_SIZE} matches: {len(matches)}")
for word in matches:
    print(word)

