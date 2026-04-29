
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
REMOVE_LOOPS = False



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
with open("atlas_subgraph_hashes.json", "r") as f:
    ATLAS_SUBGRAPH_HASHES = {k: set(v) for k,v in json.load(f).items()}


#%% Precompute the words corresponding to each graph in the wordset
HASH_TO_WORDS = defaultdict(list)
for word in words:
    graph = word_graph(word)
    graph_hash = hash_graph(graph)
    HASH_TO_WORDS[graph_hash].append(word)







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
    
    if seed_hash in ATLAS_SUBGRAPH_HASHES:
        # if it's in the atlas,
        # we can start by getting the subset of words which are ismorphically subgraphs
        # by taking the union of words for each subgraph hash
        words_isomorphic_to_subgraphs = set()
        for subgraph_hash in ATLAS_SUBGRAPH_HASHES[seed_hash]:
            words_isomorphic_to_subgraphs = set(HASH_TO_WORDS[subgraph_hash]) | words_isomorphic_to_subgraphs

    def word_is_subgraph(word):

        # check if it's even isomorphic to a subgraph
        if seed_hash in ATLAS_SUBGRAPH_HASHES:
            if word not in words_isomorphic_to_subgraphs:
                return False

        # check that the letters match up
        if not set(word) <= set(seed_word):
            return False
        
        # check that the edges match up as well
        if not edge_set(word_graph(word)) <= edge_set(seed_graph):
            return False 

        return True
    
    subgraph_words = [word for word in words if word_is_subgraph(word)]
    return subgraph_words


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
