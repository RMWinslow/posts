

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

MAX_NODES = 5
REMOVE_LOOPS = False



def load_words(filepath):
    script_dir = ospath.dirname(__file__)
    with open(ospath.join(script_dir, filepath), "r", encoding="utf-8") as file:
        return file.read().split()


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
    # Unlike other operations, this cares about the particular letter positions.
    # EG cat is a subgraph of cats but not act, nor bow.
    seed_graph = word_graph(seed_word)
    def word_is_subgraph(word):
        if not set(word) <= set(seed_word):
            return False
        graph = word_graph(word)
        return nx.algorithms.isomorphism.GraphMatcher(seed_graph, graph).subgraph_is_isomorphic()
    subgraph_words = [word for word in words if word_is_subgraph(word)]
    return subgraph_words
