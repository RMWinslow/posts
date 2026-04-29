
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




def word_graph(word):
    graph = nx.Graph()
    for letter in word:
        graph.add_node(letter)
    for a, b in zip(word, word[1:]):
        if a == b and REMOVE_LOOPS: continue
        graph.add_edge(a, b)
    return graph

def get_isomorphic_words(seed_word):
    seed_graph = word_graph(seed_word)
    seed_key = nx.weisfeiler_lehman_graph_hash(seed_graph)
    seed_n_nodes = len(set(seed_word))
    def word_matches_seed(word):
        if len(set(word)) != seed_n_nodes:
            return False
        graph = word_graph(word)
        key = nx.weisfeiler_lehman_graph_hash(graph)
        return key == seed_key
    isomorphic_words = [word for word in words if word_matches_seed(word)]
    return isomorphic_words





#%% precompute the set of subgraph relationships for the networkx atlas of small graphs
# there are efficiency improvements to be made here, 
# but I'm going to save this to file.

def hash_graph(graph):
    return nx.weisfeiler_lehman_graph_hash(graph)

ATLAS = nx.graph_atlas_g()

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


#%% Precompute the words corresponding to each graph in the wordset
HASH_TO_WORDS = defaultdict(list)
for word in words:
    graph = word_graph(word)
    graph_hash = hash_graph(graph)
    HASH_TO_WORDS[graph_hash].append(word)


#%% Precompute the words corresponding to each letter set.
# ~~then precompute the subset relationships between letter sets~~
## create a function to quickly grab potential subset words
def letter_set_key(word):
    return "".join(sorted(set(word)))

def lettermask(word):
    mask = 0
    for letter in set(word.lower()):
        mask |= 1 << (ord(letter) - ord('a'))
    return mask

LETTERSET_TO_WORDS = defaultdict(set)
for word in words:
    key = letter_set_key(word)
    LETTERSET_TO_WORDS[key].add(word)

LETTERMASK_TO_WORDS = defaultdict(set)
for word in words:
    mask = lettermask(word)
    LETTERMASK_TO_WORDS[mask].add(word)

print(f"Unique letter sets: {len(LETTERSET_TO_WORDS)}")
print(f"Unique letter masks: {len(LETTERMASK_TO_WORDS)}")

def get_letter_subset_words(seed_word):
    seed_mask = lettermask(seed_word)
    subset_words = set()
    subset_masks = [mask for mask in LETTERMASK_TO_WORDS if mask & seed_mask == mask]
    for mask in subset_masks:
        subset_words |= LETTERMASK_TO_WORDS[mask]
    return subset_words


#%% Precompute word sets for each number of nodes
MAX_NODE_COUNT_TO_WORDS = defaultdict(set)
for n in range(1, MAX_NODES + 1):
    for word in words:
        if len(set(word)) <= n:
            MAX_NODE_COUNT_TO_WORDS[n].add(word)




#%%

def find_subgraph_words(seed_word):
    # Unlike most operations, this cares about the particular letter positions.
    # EG cat is a subgraph of cats but not act, nor bow.
    # Otherwise, it would be silly to check individually.

    # If we wanted the letter-invariant form, 
    # we would start by constructing the network of subgraph relationships 
    # for all unique small graphs

    seed_graph = word_graph(seed_word)
    seed_hash = hash_graph(seed_graph)
    
    def edge_set(graph):
        return {tuple(sorted(edge)) for edge in graph.edges()}
    
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
        return edge_set(word_graph(word)) <= edge_set(seed_graph)
    
    return [word for word in candidate_words if word_is_subgraph(word)]


best_count = 0
best_word = None
best_set = None

for word in words:
    if len(set(word)) > MAX_NODES:
        continue
    subgraph_words = find_subgraph_words(word)
    count = len(subgraph_words)
    if count > best_count:
        best_count = count
        best_word = word
        best_set = subgraph_words
        print(f"New best word: {best_word} with {best_count} subgraph words")

# %%
