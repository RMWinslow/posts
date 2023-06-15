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
    "font_size": 40,
    "node_size": 3000,
    "node_color": "tab:blue",
    "edgecolors": "black", # color of border of node shapes
    "edge_color": "darkgrey", # color of actual edges
    "font_color": "white",
    "font_weight": "bold",
    "linewidths": 5,
    "width": 5,
    "font_family": "monospace",
}

def drawGraph(word):
    G = nx.Graph()
    #word = word.upper()
    for a,b in zip(word,word[1:]):
        G.add_edge(a,b)
    
    pos = nx.spring_layout(G,0.1, seed=42)
    #pos = nx.planar_layout(G)

    fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(5, 5))
    nx.draw_networkx(G, pos, **DRAWING_OPTIONS)
    #ax = plt.gca()
    #ax.margins(0.10)
    ax.set_box_aspect(1) 
    plt.tight_layout()
    plt.axis("off")
    plt.savefig(f'../wordshapes/img/words/{word}.png', transparent=True)
    #plt.show()
    plt.close()

drawGraph('atomic')
drawGraph('_ilIL_li')

small_words =["i","to","air","absorb","elixir","propel","catch","alcohol","calculus","fire","tempest","torturous","aether","earth","instant","kabbalah","aqua","miasma","seascape","loyalty","anima","automata","attractant","gensengs","lanolin","exhume","intensities","nurturant","milliosmols"]

for word in small_words: drawGraph(word.upper())






#%%
import networkx as nx

atlas = nx.graph_atlas_g()[0:20]

for G in atlas:
    nx.draw(G)
    plt.show()
    plt.close()


#%%
