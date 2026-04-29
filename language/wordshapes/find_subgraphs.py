
#%%
from collections import Counter, defaultdict
from os import path as ospath

# import networkx as nx


WORDLIST = "../biclique/scrabble dictionary.txt"
# WORDLIST = "./dolph/enable1.txt"
# WORDLIST = "./dolph/popular.txt"
# WORDLIST = "./dolph/ospd.txt"
# WORDLIST = "./samplewords.txt"
# WORDLIST = "../biclique/2of12.txt"
# WORDLIST = "../biclique/medical wordlist.txt"
# WORDLIST = "../biclique/enwiki-2023-04-13.txt"

MAX_NODES = 3
REMOVE_LOOPS = 1
UNDIRECTED = 1  

# TODO: Report number of non-looping words which are subsets of the word
# TODO: A strictly directed version?


def load_words(filepath):
    script_dir = ospath.dirname(__file__)
    with open(ospath.join(script_dir, filepath), "r", encoding="utf-8") as file:
        return file.read().split()
words = load_words(WORDLIST)

words = [word for word in words if len(set(word)) <= MAX_NODES]


def word_edges(word, remove_loops=REMOVE_LOOPS, undirected=UNDIRECTED):
    # compute word edges without invoking networkx
    edges = set()
    for a, b in zip(word, word[1:]):
        if a == b and remove_loops: continue
        edges.add((a, b))
    if undirected:
        edges = set(tuple(sorted(edge)) for edge in edges)
    return edges




#%% precompute word metadata

WORD_DATA = {}

def lettermask(word):
    mask = 0
    for letter in set(word.lower()):
        mask |= 1 << (ord(letter) - ord('a'))
    return mask

for word in words:
    WORD_DATA[word] = {
        "letters": "".join(sorted(set(word))),
        "mask": lettermask(word),
        "edges": word_edges(word),
        "n": len(set(word)),
        "n_edges": len(word_edges(word)),
    }
# TODO: I might be able to do something by comparing the simple subset.
# If h <= g, then removing self-edges from each preserves the subset relationship.



#%% Precompute some inverse mappings

MAX_NODE_COUNT_TO_WORDS = defaultdict(set)
for n in range(1, MAX_NODES + 1):
    for word in words:
        if len(set(word)) <= n:
            MAX_NODE_COUNT_TO_WORDS[n].add(word)
            #TODO: this needs refactoring

LETTERMASK_TO_WORDS = defaultdict(set)
for word in words:
    mask = WORD_DATA[word]["mask"]
    LETTERMASK_TO_WORDS[mask].add(word)

def get_letter_subset_words(seed_word):
    seed_mask = lettermask(seed_word)
    subset_words = set()
    subset_masks = [mask for mask in LETTERMASK_TO_WORDS if mask & seed_mask == mask]
    for mask in subset_masks:
        subset_words |= LETTERMASK_TO_WORDS[mask]
    return subset_words













#%%

def find_subgraph_words(seed_word):
    # Unlike most operations, this cares about the particular letter positions.
    # EG cat is a subgraph of cats but not act, nor bow.
    # Otherwise, it would be silly to check individually.

    # Prune candidate words using pre-computed sets
    # First by number of nodes
    candidate_words = set(MAX_NODE_COUNT_TO_WORDS[WORD_DATA[seed_word]["n"]])
    # Then by letter subset, which is necessary but not sufficient.
    letter_subset_words = get_letter_subset_words(seed_word)
    candidate_words = candidate_words & letter_subset_words

    def word_is_subgraph(word):        
        return WORD_DATA[word]["edges"] <= WORD_DATA[seed_word]["edges"]
    
    return [word for word in candidate_words if word_is_subgraph(word)]


best_count = 0
best_word = None
best_set = None
words_just_as_good = set()  # in case of ties, keep track of them

# Keep track of words already found to be subgraphs.
# Trivially, they can't be better than a seed_word we've already checked.
visited_words = set()

for word in sorted(words, key=lambda w: WORD_DATA[w]["n_edges"], reverse=True):
    if word in visited_words:
        continue

    subgraph_words = find_subgraph_words(word)
    count = len(subgraph_words)

    if count > best_count:
        best_count = count
        best_word = word
        best_set = subgraph_words
        words_just_as_good = set()  # in case of ties, keep track of them
        print(f"New best word: {best_word} with {best_count} subgraph words")
    elif count == best_count:
        words_just_as_good.add(word)
        print(f"Tie for best word: {word} with {count} subgraph words")

    visited_words |= set(subgraph_words)

# check whether any of the subset words are just as good as the best word, in which case we should report them too.
for word in best_set:
    if word in words_just_as_good:
        continue
    subgraph_words = find_subgraph_words(word)
    count = len(subgraph_words)
    if count == best_count:
        words_just_as_good.add(word)
        print(f"Word just as good as best word: {word} with {count} subgraph words")


# Append some info on the best word to a log file. (find_subgraph_log.txt)
# two newlines
# then global params from the top (max nodes, remove loops, undirected)
# then the best word and count
# then the list of subgraph words, ten per line
#   with padding based on the longest word, so they line up nicely
# then any words just as good, but without the subgraph words, and with a header "Words just as good:"
# then two more newlines
with open("find_subgraph_log.txt", "a", encoding="utf-8") as log_file:
    log_file.write("\n\n")
    log_file.write(f"## MAX_NODES: {MAX_NODES}, REMOVE_LOOPS: {REMOVE_LOOPS}, UNDIRECTED: {UNDIRECTED}\n")
    log_file.write(f"Best word: {best_word} with {best_count} subgraph words\n")
    log_file.write("Subgraph words:\n")
    longest_word_length = max(len(word) for word in best_set)
    for i, word in enumerate(sorted(best_set)):
        log_file.write(word.ljust(longest_word_length + 2))
        if (i + 1) % 10 == 0:
            log_file.write("\n")
    if words_just_as_good:
        log_file.write("\nWords just as good:\n", )
        log_file.write(", ".join(sorted(words_just_as_good)))
    log_file.write("\n\n")

# %%
