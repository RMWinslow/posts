# This is inspired by the following YT video:
# https://www.youtube.com/watch?v=4uFahk0cuZU
# gh: https://github.com/jhntrnr/word-shapes
# I'm very confused by his 'graph' metric,
# and not even sure why he needs to load Scott.

# I'm not going to compute all the isomorphism hashes,
# but I can easily do a simple graph-based shape metric.
# Here's what I do:
#    Treat each word as a simple graph.
#    Each unique letter is a node, and the edges are between adjacent letters in the word.
#    Rather than comparing the entire graph structure, I just compare the Degree Sequence.

# The samplewords.txt input file is from jhntrnr's github repo.
# it's precleaned, so I don't have to check for capitals/punctuation, etc.
# (TODO: Might want to use a more expansive list. This one only has 11504 words.)

# other wordlists are from https://github.com/dolph/dictionary
# They may need to be cleaned

#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#word = word.lower()


#%% LOAD WORDS AND CREATE MAPPINGS
from collections import defaultdict, Counter
import networkx as nx
import matplotlib.pyplot as plt

#WORDLIST = 'samplewords.txt'
#WORDLIST = 'dolph/popular.txt'
WORDLIST = 'dolph/enable1.txt'

with open(WORDLIST,'r') as file: 
    words = file.read().split()

def validate(word):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if len(set(word) - alphabet) > 0: 
        print(word)
        return False
    return True
for word in words: assert validate(word)

def calc_degree_sequence(word):
    # https://mathworld.wolfram.com/DegreeSequence.html
    connections = defaultdict(set)
    for a,b in zip(word,word[1:]):
        if a!=b: #(exclude loops)
            connections[a].add(b)
            connections[b].add(a)
    degrees_list = [len(s) for s in connections.values()]
    return tuple(sorted(degrees_list, reverse=True)) #(tuple for hashability)

words_to_degree_sequences = dict()
#degree_sequences_to_words = defaultdict(set)
degree_sequences_to_words = defaultdict(list)
for word in words:
    degree_sequence = calc_degree_sequence(word)
    words_to_degree_sequences[word] = degree_sequence
    #degree_sequences_to_words[degree_sequence].add(word)
    degree_sequences_to_words[degree_sequence].append(word)
degree_sequence_counter = Counter(words_to_degree_sequences.values())

ds2w = degree_sequences_to_words
w2ds = words_to_degree_sequences
dsc = degree_sequence_counter

print(len(words), len(degree_sequences_to_words))



def calc_toads(word):
    connections = defaultdict(set)
    for a,b in zip(word,word[1:]):
        if a!=b: #(exclude loops)
            connections[a].add(b)
            connections[b].add(a)
    toads_list = [len(connections[c]) for c in word]
    return ''.join([str(d) for d in toads_list])













#%%
#Use the catalog to match words to graphs

# start by loading up the connected graphs and get their degree sequence.
Atlas = nx.graph_atlas_g()[:]  # graphs up to 7 nodes
connectedGraphs = [G for G in Atlas if nx.number_connected_components(G) == 1]

ds2ag = degree_sequence_to_atlas_graphs = defaultdict(list)
ag2ds = atlas_graphs_to_degree_sequence = dict()

for aG in connectedGraphs:
    degrees_list = [val for (node, val) in aG.degree()]
    degree_sequence = tuple(sorted(degrees_list, reverse=True))
    if degree_sequence==(0,): degree_sequence=tuple() # empty tuple for singleton graph
    ds2ag[degree_sequence].append(aG)
    ag2ds[aG] = degree_sequence



# Now compare graphs with the same degree 
# Iterate through the words at the top level because I don't want to recalculate the word graphs,
#   and I certainly can't hold them all in memory.
ag2w = atlas_to_words = defaultdict(list)
for word in words[:]:
    ds = w2ds[word]
    wG = nx.Graph()
    for a,b in zip(word,word[1:]):
        if a!=b:
            wG.add_edge(a,b)
    # If there is only one graph with this degree sequence, we don't have to actually check for isomorphism.
    # If there are multiple then we do.
    match_flag = False
    if len(ds2ag[ds]) == 1:
        aG = ds2ag[ds][0]
        ag2w[aG].append(word)
        match_flag = True
    else:
        for aG in ds2ag[ds]:
            if nx.is_isomorphic(wG,aG): 
                ag2w[aG].append(word)
                match_flag = True
                break
    if not match_flag and len(ds) <= 7: 
        print(word)

#ag2w

#%%
# Now check how many words are missing.
# and check that none were double matched
wordMatchCount = Counter()
for k,v in ag2w.items():
    for word in v:
        wordMatchCount[word] += 1

assert [word for word in words if wordMatchCount[word] > 1] == []

unmatchedWords = [word for word in words if wordMatchCount[word] == 0]
taco = list(set([w2ds[w] for w in unmatchedWords]))
burrito = [len(ds2w[ds]) for ds in taco]
max(burrito)
taco[404]

for ds in taco:
    if len(ds2w[ds]) > 100:
        print(ds)

#TODO: SOMEHOW COMPARE THESE BIGGER GRAPHS























#%% PLAY AROUND WITH THE RESULTS

# check for ds with multiple entries

i=0
for ds,wordlist in ds2w.items():
    if len(ds)==14 and len(wordlist) > 1:
        print(ds, wordlist)
        i+=1
print(i)


#%%
# Check for pentagram subgraph by repeatedly trimming all nodes that can't be part of the pentagram
alphabet = set('abcdefghijklmnopqrstuvwxyz')
def check_for_pentagram(word):
    for _ in range(3):
        connections = defaultdict(set)
        for a,b in zip(word,word[1:]):
            if a=='Ω' or b=='Ω': continue #'!' is placeholder for removed letters
            elif a!=b: #(exclude loops)
                connections[a].add(b)
                connections[b].add(a)
        for letter in connections:
            if len(connections[letter]) < 4:
                word = word.replace(letter,'Ω')
    degrees_list = [len(s) for s in connections.values()]
    return word,tuple(sorted(degrees_list, reverse=True))

for word in words:
    filtered_word, filtered_ds = check_for_pentagram(word)
    if len(filtered_ds) > 4:
        print(word,filtered_word, filtered_ds)

# No pentagrams, not even as subgraphs.


#%%
# check for peterson subgraph
# need at least 10 nodes with degree at least degree 3
def check_for_peterson(ds):
    if len(ds) < 10: return False
    if ds[8] < 3: return False
    return "maybe"

for ds in dsc:
    if check_for_peterson(ds):
        print(ds)

# No Peterson. The only words that even come close to being a possibility are 
#['microspectrophotometries'] (6, 6, 4, 4, 4, 4, 4, 3, 3, 2)
#['phosphatidylethanolamines'] (5, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2)





#%%
# Most common degree sequences

for ds, count in degree_sequence_counter.most_common():
    print(ds,count,list(degree_sequences_to_words[ds])[:3])

len([ds for ds in degree_sequence_counter if degree_sequence_counter[ds]==1])


#%%
taco = []
for ds in degree_sequence_counter:
    if degree_sequence_counter[ds]==1:
        taco.append(list(degree_sequences_to_words[ds])[0])

for word in sorted(taco,key=lambda word: len(word)):
    print(word,words_to_degree_sequences[word])

#%% check for complete graphs
def is_complete_graph(degree_sequence):
    # complete graphs will have all nodes with same degree
    # and that degree will be one less than the number of nodes
    if len(set(degree_sequence)) == 1:
        if degree_sequence[0] == len(degree_sequence) - 1:
            return True
    return False

for ds in degree_sequence_counter:
    if is_complete_graph(ds): print(degree_sequences_to_words[ds])




# %% biggest average degree for each word length
bestwords = defaultdict(list) 
bestscores = [0]*30 #only need 28 I think
for word in words:
    ds = words_to_degree_sequences[word]
    if len(ds)==0: continue
    avgdegree = sum(ds)/len(ds) # not technically the average degree but whatever
    if avgdegree > bestscores[len(word)]:
        bestscores[len(word)] = avgdegree
        bestwords[len(word)] = [word]
    elif avgdegree == bestscores[len(word)]:
        bestwords[len(word)].append(word)
bestwords
max(bestscores)
for i in range(30):
    if len(bestwords[i]) == 1: print(bestwords[i][0])
    else: print(bestwords[i])



#%%
def get_keys_with_highest_average(d):
    return [max(((key, value) for key, value in d.items() if len(key) == key_length), key=lambda x: x[1]) for key_length in set(map(len, d))]
get_keys_with_highest_average(w2ds)

# %%

























#%% 
# Plot graphs
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B')
G.add_edge('B', 'C')


options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "#268bd2",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()






#%%
DRAWING_OPTIONS = {
    "font_size": 50,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "lightgrey", # color of border of node shapes
    "edge_color": "darkgrey", # color of actual edges
    "font_color": "black",
    "font_weight": "bold",
    "linewidths": 5,
    "width": 5,
    "font_family": "monospace",
}

def drawGraph(word):
    #word = word.upper()
    wordToProcess = word #[::-1]

    G = nx.Graph()
    for a,b in zip(wordToProcess,wordToProcess[1:]):
        if a!=b: G.add_edge(a,b)
    
    pos = nx.spring_layout(G,0.1, seed=42)
    #pos = nx.planar_layout(G)
    #pos = nx.nx_agraph.graphviz_layout(G, prog="fdp")


    fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(8, 4))
    nx.draw_networkx(G, pos, **DRAWING_OPTIONS)
    #ax = plt.gca()
    ax.margins(0.20)
    #ax.set_box_aspect(1) 
    plt.tight_layout()
    plt.axis("off")
    plt.savefig(f'../wordshapes/img/flatwords/{word}.webp', transparent=True, dpi=100)
    #plt.show()
    plt.close()

drawGraph('atomic')
drawGraph('_ilIL_li')

small_words =["i","to","air","absorb","elixir","propel","catch","alcohol","calculus","fire","tempest","torturous","aether","earth","instant","kabbalah","aqua","miasma","seascape","loyalty","anima","automata","attractant","gensengs","lanolin","exhume","intensities","nurturant","milliosmols"]

for word in small_words: drawGraph(word)


#%% display as markdown table
for word in sorted(small_words, key=lambda x: len(set(x))):
    print(f"|  | {word} | ![word graph for {word}](wordshapes/img/flatwords/{word}.webp) |")








#%% Try to draw the word graphs all at once


DRAWING_OPTIONS = {
    "font_size": 10,
    "node_size": 100,
    "node_color": "white",
    "edgecolors": "#aaaa", # color of border of node shapes
    "edge_color": "#5555", # color of actual edges
    "font_color": "black",
    "font_weight": "bold",
    "linewidths": 2,
    "width": 2,
    "font_family": "monospace",
}

def exampleWords():
    U = nx.Graph()  # graph for union of all graphs
    for idx,word in enumerate(small_words):
        G = nx.Graph()
        for c in word: G.add_node(c)
        for a,b in zip(word,word[1:]):
            if a!=b: G.add_edge(a,b)
        for c in word: G.nodes[c]['label'] = c
        U = nx.disjoint_union(U, G)
    return U



U = exampleWords()
#fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(8, 4))
#pos = nx.spring_layout(U,0.2, seed=42)
pos = nx.nx_agraph.graphviz_layout(U, prog="neato",)
nx.draw(U,pos,**DRAWING_OPTIONS,with_labels=True, labels=nx.get_node_attributes(U, 'label'))













#%%
import networkx as nx

atlas = nx.graph_atlas_g()[0:20]

for G in atlas:
    nx.draw(G)
    plt.show()
    plt.close()


#%%
import random

import matplotlib.pyplot as plt
import networkx as nx


GraphMatcher = nx.isomorphism.vf2userfunc.GraphMatcher


def atlas6():
    """Return the atlas of all connected graphs with at most 6 nodes"""

    Atlas = nx.graph_atlas_g()[3:209]  # 0, 1, 2 => no edges. 208 is last 6 node graph
    U = nx.Graph()  # graph for union of all graphs in atlas
    for G in Atlas:
        # check if connected
        if nx.number_connected_components(G) == 1:
            # check if isomorphic to a previous graph
            if not GraphMatcher(U, G).subgraph_is_isomorphic():
                U = nx.disjoint_union(U, G)
    return U


G = atlas6()

print(G)
print(nx.number_connected_components(G), "connected components")

plt.figure(1, figsize=(8, 8))
# layout graphs with positions using graphviz neato
pos = nx.nx_agraph.graphviz_layout(G, prog="neato")
# color nodes the same in each connected subgraph
C = (G.subgraph(c) for c in nx.connected_components(G))
for g in C:
    c = [random.random()] * nx.number_of_nodes(g)  # random color...
    nx.draw(g, pos, node_size=40, node_color=c, vmin=0.0, vmax=1.0, with_labels=False)
plt.show()

# %%










#%% draw k5
G = nx.complete_graph(5)


pos = nx.circular_layout(G)
fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(5, 5))
nx.draw(G, pos, **DRAWING_OPTIONS)
#ax = plt.gca()
#ax.margins(0.10)
ax.set_box_aspect(1) 
plt.tight_layout()
plt.axis("off")
plt.savefig(f'../wordshapes/img/K5.webp', transparent=True, dpi=50)
#plt.show()
plt.close()











