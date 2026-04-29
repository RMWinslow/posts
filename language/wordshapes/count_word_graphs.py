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

MAX_NODES = 7




def load_words(filepath):
    script_dir = ospath.dirname(__file__)
    with open(ospath.join(script_dir, filepath), "r", encoding="utf-8") as file:
        return file.read().split()


def word_graph(word):
    graph = nx.Graph()
    for letter in word:
        graph.add_node(letter)
    for a, b in zip(word, word[1:]):
        if a == b:
            continue
        graph.add_edge(a, b)
    return graph


def graph_key_and_letters(word):
    graph = word_graph(word)
    # Same abstract graph shape => same WL hash.
    graph_key = nx.weisfeiler_lehman_graph_hash(graph)
    # Same graph instantiation => same graph shape and same set of letters.
    # TODO: make this actually care about the letter position in the word
    # What I actually care about, I guess, is which word has the most other words as subgraphs.
    letters_key = "".join(sorted(graph.nodes()))
    return graph_key, letters_key

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




words = load_words(WORDLIST)

graph_counter = Counter()
instantiation_counter = Counter()
graph_examples = defaultdict(list)
instantiation_examples = defaultdict(list)

for word in words:
    if len(set(word)) > MAX_NODES: continue

    key, letters_key = graph_key_and_letters(word)
    inst_key = (key, letters_key)

    graph_counter[key] += 1
    instantiation_counter[inst_key] += 1

    if len(graph_examples[key]) < 5:
        graph_examples[key].append(word)
    if len(instantiation_examples[inst_key]) < 5:
        instantiation_examples[inst_key].append(word)


print(f"Wordlist: {WORDLIST}")
print(f"Words: {len(words)}")
print(f"Distinct graph shapes: {len(graph_counter)}")
# print(f"Distinct graph instantiations: {len(instantiation_counter)}")

print("\nWords per graph shape")
for key, count in graph_counter.most_common():
    print(count, key, graph_examples[key])

# print("\nWords per graph instantiation")
# for key, count in instantiation_counter.most_common():
#     print(count, key, instantiation_examples[key])
