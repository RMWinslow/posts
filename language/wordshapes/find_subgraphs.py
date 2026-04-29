
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

def find_subgraph_words(seed_word):
    # Unlike most operations, this cares about the particular letter positions.
    # EG cat is a subgraph of cats but not act, nor bow.
    # Otherwise, it would be silly to check individually.

    # If we wanted the letter-invariant form, 
    # we would start by constructing the network of subgraph relationships 
    # for all unique small graphs

    seed_graph = word_graph(seed_word)
    
    def edge_set(graph):
        return {tuple(sorted(edge)) for edge in graph.edges()}
    
    def word_is_subgraph(word):
        if not set(word) <= set(seed_word):
            return False
        
        if not edge_set(word_graph(word)) <= edge_set(seed_graph):
            return False 

        return True
    
    subgraph_words = [word for word in words if word_is_subgraph(word)]
    return subgraph_words


best_count = 0
best_word = None

for word in words:
    if len(set(word)) > MAX_NODES:
        continue
    subgraph_words = find_subgraph_words(word)
    count = len(subgraph_words)
    if count > best_count:
        best_count = count
        best_word = word
        print(f"New best word: {best_word} with {best_count} subgraph words")

# %%
