
#%%
from collections import Counter, defaultdict
from os import path as ospath

import networkx as nx


WORDLIST = "../biclique/scrabble dictionary.txt"
# WORDLIST = "./dolph/enable1.txt"
# WORDLIST = "./dolph/popular.txt"
# WORDLIST = "./dolph/ospd.txt"
# WORDLIST = "./samplewords.txt"
# WORDLIST = "../biclique/2of12.txt"
# WORDLIST = "../biclique/medical wordlist.txt"
# WORDLIST = "../biclique/enwiki-2023-04-13.txt"

MAX_NODES = 4
REMOVE_LOOPS = True



def load_words(filepath):
    script_dir = ospath.dirname(__file__)
    with open(ospath.join(script_dir, filepath), "r", encoding="utf-8") as file:
        return file.read().split()
words = load_words(WORDLIST)

words = [word for word in words if len(set(word)) <= MAX_NODES]



def word_graph(word):
    graph = nx.Graph()
    for letter in word:
        graph.add_node(letter)
    for a, b in zip(word, word[1:]):
        if a == b and REMOVE_LOOPS: continue
        graph.add_edge(a, b)
    return graph




#%% precompute word metadata

WORD_DATA = {}

def lettermask(word):
    mask = 0
    for letter in set(word.lower()):
        mask |= 1 << (ord(letter) - ord('a'))
    return mask

for word in words:
    graph = word_graph(word)
    graph_hash = nx.weisfeiler_lehman_graph_hash(graph)
    letters_key = "".join(sorted(graph.nodes()))
    WORD_DATA[word] = {
        "letters": "".join(sorted(set(word))),
        "mask": lettermask(word),
        "graph": graph,
        "edges": set(tuple(sorted(edge)) for edge in graph.edges()),
        "hash": nx.weisfeiler_lehman_graph_hash(graph),
        "n": len(set(word)),
        "n_edges": len(graph.edges()),
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

HASH_TO_WORDS = defaultdict(set)
for word in WORD_DATA:
    hash = WORD_DATA[word]["hash"]
    HASH_TO_WORDS[hash].add(word)

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






#%% precompute the set of subgraph relationships for the networkx atlas of small graphs
# there are efficiency improvements to be made here, 
# but I'm going to save this to file.

# def hash_graph(graph):
#     return nx.weisfeiler_lehman_graph_hash(graph)

# ATLAS = nx.graph_atlas_g()

# # Seed with the trivial reflexive subgraph
# ATLAS_SUBGRAPH_HASHES = {hash_graph(graph): {hash_graph(graph)} for graph in ATLAS}

# for i,graph in enumerate(ATLAS):
#     print(i)
#     for possible_subgraph in ATLAS:
#         if graph == possible_subgraph:
#             continue
#         if len(possible_subgraph.nodes()) > len(graph.nodes()):
#             continue
#         if len(possible_subgraph.edges()) > len(graph.edges()):
#             continue
#         if nx.algorithms.isomorphism.GraphMatcher(graph, possible_subgraph).subgraph_is_isomorphic():
#             ATLAS_SUBGRAPH_HASHES[hash_graph(graph)].add(hash_graph(possible_subgraph))

# # save the relations to json
# import json
# with open("atlas_subgraph_hashes.json", "w") as f:
#     json.dump({k: list(v) for k,v in ATLAS_SUBGRAPH_HASHES.items()}, f)

#%% load the relations from json
import json
with open("atlas_subgraph_hashes.json", "r") as f:
    ATLAS_SUBGRAPH_HASHES = {k: set(v) for k,v in json.load(f).items()}








#%%

def find_subgraph_words(seed_word):
    # Unlike most operations, this cares about the particular letter positions.
    # EG cat is a subgraph of cats but not act, nor bow.
    # Otherwise, it would be silly to check individually.

    # If we wanted the letter-invariant form, 
    # we would start by constructing the network of subgraph relationships 
    # for all unique small graphs

    seed_graph = WORD_DATA[seed_word]["graph"]
    seed_hash = WORD_DATA[seed_word]["hash"]
    
    # Prune candidate words using pre-computed sets
    # First by number of nodes
    candidate_words = set(MAX_NODE_COUNT_TO_WORDS[len(seed_graph)])
    # Then by isomorphism to subgraphs, if available in the atlas
    if seed_hash in ATLAS_SUBGRAPH_HASHES:
        words_isomorphic_to_subgraphs = set()
        for subgraph_hash in ATLAS_SUBGRAPH_HASHES[seed_hash]:
            words_isomorphic_to_subgraphs = set(HASH_TO_WORDS[subgraph_hash]) | words_isomorphic_to_subgraphs
        candidate_words = candidate_words & words_isomorphic_to_subgraphs
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

for word in sorted(words, key=len, reverse=True):
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

# Finally, print all words_just_as_good
print(f"Best word: {best_word} with {best_count} subgraph words")
if words_just_as_good:
    print(f"Other words just as good: {', '.join(words_just_as_good)}")


# %%
