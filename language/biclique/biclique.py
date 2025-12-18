#%%
'''
This file takes in a word list and searches for a large "biqlique"
which here means a set of word endings and beginnings such that any
pair of endings and beginnings can be combined to form a valid word.

The inspiration is a toy I say called
"Fisher-Price Preschool Learning Toy Spin ‘n Rhyme Fidget Spinner, Owl-Themed Early Reading Activity for Kids Ages 3+ Years"

The word set there is:
{p,b,m,h,r},{ad,at,ail,ay,ug}
Which gives the words:
p-ad, p-at, p-ail, p-ay, p-ug,
b-ad, b-at, b-ail, b-ay, b-ug,
m-ad, m-at, m-ail, m-ay, m-ug,
h-ad, h-at, h-ail, h-ay, h-ug,
r-ad, r-at, r-ail, r-ay, r-ug
'''

# # # 2of12 comes from http://wordlist.aspell.net/12dicts/ 
# with open("./2of12.txt", "r") as f: words = set(f.read().splitlines())
# ALIAS="12dicts"

# # filtered version of 12dicts from here: https://github.com/InnovativeInventor/dict4schools
# # safedict_simple.txt removes both innappriate and complex words,... supposedly
# # lots of abbreviations in there though -_-
# with open("./safedict_simple.txt", "r") as f: safedict_words = set(f.read().splitlines())
# words = words.intersection(safedict_words)
# ALIAS="12dicts_childfriendly"

# wikipedia wordlist from here: https://github.com/IlyaSemenov/wikipedia-word-frequency/tree/master
# FREQUENCY_THRESHOLD = 10 # only keep words with a frequency above this threshold
# with open("./enwiki-2023-04-13.txt", "r", encoding="utf8") as f: 
#     words = set()
#     for line in f.read().splitlines():
#         # each line is a word and a number, separated by a space
#         # I want to keep the word only if the number is greater than 50, alphabetical, and lowercase
#         word, count = line.split()
#         if int(count) < FREQUENCY_THRESHOLD: continue 
#         if not word.isalpha(): continue
#         words.add(word)
# ALIAS="wikipedia"

# words = {"ax","bx","cx","dx",}
# ALIAS="testlist"

# medical wordlist from here: https://github.com/glutanimate/wordlist-medicalterms-en/blob/master/wordlist.txt
# with open("./medical wordlist.txt", "r", encoding="utf8") as f:  words = set(f.read().splitlines())
# # words = {w for w in words if w.islower()}
# # words = {w for w in words if w.isalpha()}
# ALIAS="medical"

# scrabble dict from here: https://gist.github.com/deostroll/7693b6f3d48b44a89ee5f57bf750bd32
with open("./scrabble dictionary.txt", "r") as f: words = set(f.read().splitlines())
ALIAS="scrabble"


PF_REQUIRED = 5 # clique size
SF_REQUIRED = PF_REQUIRED # required suffixes for each prefix

MIN_NODE_LENGTH = 1 # minimum length of a prefix or suffix to consider
MAX_NODE_LENGTH = 3
MIN_WORD_LENGTH = 0
MAX_WORD_LENGTH = None 

PREVENT_OVERLAP_PF = True # if True, don't pair prefixes that are the start or end of the other
PREVENT_OVERLAP_SF = PREVENT_OVERLAP_PF # Likewise for suffixes, but my implementation of the overlap prevention is a bit lazy and might overzealously filter some suffixes. 
REMOVE_COMMON_SUFFIXES = True # remove common suffixes like "ing", "ed", "s", etc. from the word list before processing


# bit of hacky file naming to preserve backwards compatibility
# if MAX_NODE_LENGTH:
#     FLUFF = f"L,{MIN_NODE_LENGTH},{MAX_NODE_LENGTH},{MIN_WORD_LENGTH},{MAX_WORD_LENGTH}"
# else:
#     FLUFF = f"L,{MIN_NODE_LENGTH},{MIN_WORD_LENGTH},{MAX_WORD_LENGTH}"


FLUFF = f"L,{MIN_NODE_LENGTH},{MAX_NODE_LENGTH},{MIN_WORD_LENGTH},{MAX_WORD_LENGTH}"
FLUFF = FLUFF + f"_PO,{int(PREVENT_OVERLAP_PF)},{int(PREVENT_OVERLAP_SF)}"
if REMOVE_COMMON_SUFFIXES: FLUFF = FLUFF + "_RCS"
if ALIAS=="wikipedia": FLUFF = FLUFF + f"_freq{FREQUENCY_THRESHOLD}"
OUTPUT_FILE = f"bicliques_{PF_REQUIRED}_{SF_REQUIRED}_{'_'+FLUFF if FLUFF else ""}_{ALIAS}.txt"

PRINT_DFS_RESULTS = True # If I just want existence, instead of the whole set, this lets me see them.







# %% PRE-FILTERING / CLEANUP
def remove_suffixes(words, suffixes):
    """Remove words that end with any of the given suffixes IFF the word also exists without the suffix."""
    if not suffixes: return words
    words = {w for w in words if not any(w.endswith(s) and w[:-len(s)] in words for s in suffixes)}
    words = {w for w in words if not any(w.endswith(s) and w[:-len(s)]+"e" in words for s in suffixes)}
    return words

words = {w.replace("'","") for w in words} # remove apostrophes
words = {w.replace("-","") for w in words} # remove hyphens
words = {w.lower() for w in words} # lowercase (the words should already be lowercase)
words = list(set(words)) # remove duplicates
words = {w for w in words if len(w) >= 2}
if MAX_WORD_LENGTH: words = {w for w in words if len(w) <= MAX_WORD_LENGTH}
if MIN_WORD_LENGTH: words = {w for w in words if len(w) >= MIN_WORD_LENGTH}
if REMOVE_COMMON_SUFFIXES:
    words = remove_suffixes(words,
        ["ing","ed","es","s","er","est","ly","tion","ity","ness","ment","al","ing"])
print(len(words), "words after pre-filtering")





#%% BREAK WORDS INTO ALL POSSIBLE (PREFIX,SUFFIX) PAIRS
from collections import defaultdict
pairs = defaultdict(set)
for w in words:
    for i in range(1,len(w)):
        prefix = w[:i]+"-"
        suffix = "-"+w[i:]
        if MIN_NODE_LENGTH and (len(prefix)<MIN_NODE_LENGTH+1 or len(suffix)<MIN_NODE_LENGTH+1): continue
        if MAX_NODE_LENGTH and (len(prefix)>MAX_NODE_LENGTH+1 or len(suffix)>MAX_NODE_LENGTH+1): continue
        pairs[prefix].add(suffix)
        pairs[suffix].add(prefix)

suffixes = {k for k in pairs if k.startswith("-")}
prefixes = {k for k in pairs if k.endswith("-")}
print(len(prefixes),"prefixes ;", len(suffixes),"suffixes")




#%% (FILTER 1) Iteratively reduce elements to those with sufficient valid partners & define threshold functions
print(f"Reducing prefixes and suffixes to those with at least {SF_REQUIRED}/{PF_REQUIRED} valid partners")


def get_partner_threshold(x):
    """
    Args:
        x: String or set containing prefix/suffix elements
    Returns:
        SF_REQUIRED for prefixes (ending with '-')
        PF_REQUIRED for suffixes (starting with '-')
    """
    # Handle set input - examine first element
    if isinstance(x, set): x = next(iter(x))
    if isinstance(x, frozenset): x = next(iter(x))
    # Handle string input
    if isinstance(x, str):
        if x.startswith("-"): return PF_REQUIRED
        elif x.endswith("-"): return SF_REQUIRED
        else: raise ValueError(f"String '{x}' must start or end with '-'")

def get_own_threshold(x):
    """inverse of the above"""
    if isinstance(x, set): x = next(iter(x))
    if isinstance(x, frozenset): x = next(iter(x))
    if isinstance(x, str):
        if x.startswith("-"): return SF_REQUIRED
        elif x.endswith("-"): return PF_REQUIRED
        else: raise ValueError(f"String '{x}' must start or end with '-'")

def enough_partners(key, partners):
    """Check if key has enough partners based on prefix/suffix type."""
    return len(partners) >= get_partner_threshold(key)

def reduce_pairs(pairs):
    """Remove partners that don't meet threshold requirements."""
    changes = 0
    for key, partners in pairs.items():
        valid_partners = {p for p in partners if enough_partners(p, pairs[p])}
        if len(valid_partners) != len(partners):
            pairs[key] = valid_partners
            changes += 1
    return changes

# Iteratively reduce until convergence
for iteration in range(100):
    changes = reduce_pairs(pairs)
    print(f"Iteration {iteration}; changed values: {changes}")
    if changes == 0: break

# Final cleanup: remove elements that don't meet threshold
pairs = {k: v for k, v in pairs.items() if enough_partners(k, v)}
# (pairs SHOULD NEVER CHANGE AFTER THIS POINT)

# Count remaining elements
prefixes = {k for k in pairs if k.endswith("-")}
suffixes = {k for k in pairs if k.startswith("-")}
print(f"{len(prefixes)} prefixes; {len(suffixes)} suffixes remain")


def check_overlap(f1,f2):
    f1,f2 = f1.strip("-"), f2.strip("-")
    if f1.endswith(f2) or f1.startswith(f2) or f2.endswith(f1) or f2.startswith(f1):
        return True
    else:
        return False

def get_shared_partners(nodes, pairs=pairs):
    """Return partners shared by all given nodes."""
    return set.intersection(*[pairs[node] for node in nodes])

def count_shared_partners(nodes, pairs=pairs): return len(get_shared_partners(nodes, pairs))

def enough_shared_partners(nodes, pairs=pairs):
    """Check if nodes have enough shared partners based on prefix/suffix type."""
    if not nodes: return False
    threshold = get_partner_threshold(nodes)
    # Lazy overlap check: if there are *any* overlaps, increase the required threshold by 1.
    # This won't block *all* cases with overlaps, but it will block most.
    shared_partners = get_shared_partners(nodes, pairs)
    # k = next(iter(nodes))
    # if (PREVENT_OVERLAP_SF and k.endswith("-")) or (PREVENT_OVERLAP_PF and k.startswith("-")):
    #     if any(check_overlap(k, p) for p in shared_partners):
    #         threshold += 1
    return len(shared_partners) >= threshold

def big_enough_clique(nodes):
    "Check if a set of nodes is big enough. Doesn't check for validity."
    return len(nodes) >= get_own_threshold(nodes)





#%% FIND METAPARTNERS
# A metapartner is a partner that has at least THRESHOLD partners in common
# The metapartners object essentially defines a graph of prefixes / suffixes
# (FILTER 2) will be to remove nodes and edges without enough shared metapartners
#   A valid node must have N-1 metapartners, and share N-2 metapartners with each of its metapartners.



class Metapartners(defaultdict):
    def __init__(self): 
        super().__init__(set)
    
    def build_from_pairs(self, pairs,):
        """Build metapartners from pairs data"""
        for k, v in pairs.items():
            potential_metapartners = set().union(*[pairs[p] for p in v])
            self[k] = {p for p in potential_metapartners if p != k and enough_shared_partners({k,p})}
            if k.endswith("-") and PREVENT_OVERLAP_PF:
                self[k] = {p for p in self[k] if not check_overlap(k, p)}
            if k.startswith("-") and PREVENT_OVERLAP_SF:
                self[k] = {p for p in self[k] if not check_overlap(k, p)}
        return self
    
    def clean(self):
        """1. Remove metapartners that are not keys. 2. Remove keys with insufficient partners. 3. Repeat 1."""
        original_length = len(self)

        cleaned_dict = {k: v.intersection(self.keys()) for k, v in self.items()}
        filtered_dict = {k: v for k, v in cleaned_dict.items() if len(v) >= get_own_threshold(k)-1}
        cleaned_dict = {k: v.intersection(filtered_dict.keys()) for k, v in filtered_dict.items()}
        self.clear()
        self.update(cleaned_dict)
        return original_length - len(self)
    
    def clean_edges(self):
        """Remove edges where the nodes don't share at least N-2 partners."""
        original_length = len(self)
        for k, v in list(self.items()):
            for p in list(v):
                if len(self[k].intersection(self[p])) < get_own_threshold(k)-2:
                    self[k].discard(p)
                    self[p].discard(k)
        self.clean()
        return original_length - len(self)
    
    def remove_nodes(self, key_set_to_remove, verbose=False):
        """Remove all nodes in the metapartner graph that are not part of the clique defined by key_set."""
        if verbose:
            old_count = len(self)
            print(f"Before filtering, {len(self)} nodes in metapartner graph")
        
        # filter the metapartner keys to only those not in the removal set
        filtered = {k: v for k, v in self.items() if k not in key_set_to_remove}
        self.clear()
        self.update(filtered)
        self.clean()
        
        if verbose:
            new_count = len(self)
            print(f"Removed {old_count - new_count} nodes")
            print(f"After filtering, {new_count} nodes in metapartner graph")
        
        return self
    
    def remove_edges(self, edges_to_remove, verbose=False):
        """edge_set_to_remove: iterable of iterable pairs (tuples/frozensets/etc) representing edges to remove."""
        if verbose:
            old_count = len(self)
            print(f"Before filtering, {len(self)} nodes in metapartner graph")
        
        # edges_to_remove = {frozenset(edge) for edge in edges_to_remove}
        for node1,node2 in edges_to_remove:
            self[node1].discard(node2)
            self[node2].discard(node1)

        self.clean()
        if verbose:
            new_count = len(self)
            print(f"After filtering, {new_count} nodes in metapartner graph")
        return self

print("Building metapartner graph from pairs...")
metapartners = Metapartners()
metapartners.build_from_pairs(pairs)

print(len(metapartners), "nodes in metapartner graph before filtering")

for iteration in range(100):
    changes1 = metapartners.clean()
    changes2 = metapartners.clean_edges()
    print(f"Iteration {iteration}; changed values: {changes1,changes2}")
    if changes1+changes2 == 0: break
print(len(metapartners), "nodes in metapartner graph after filtering")







#%% DEPTH FIRST SEARCH FOR EXISTENCE OF A CLIQUE

dead_end_cliques = defaultdict(set)
validated_cliques = defaultdict(dict)

def dfs_clique_exists(current_clique,
                      valid_nodes=None, invalid_nodes=None,
                      clique_size_required=None,
                      metapartners=metapartners,):
    """Check if current_clique is a subset of a clique of sufficient size.
    The global dead_end_cliques is used to cache results of previous searches.

    Args:
        current_clique: Set of nodes (prefixes or suffixes) to start from.
        valid_nodes: whitelist for nodes - passing this blacklists all nodes not in this set.
        invalid_nodes: blacklist for nodes
        clique_size_required: minimum size for a valid clique to return a result and end the recursion
        metapartners: Metapartners graph to use for checking connections.
    RETURNS:
        False if no such clique exists,
        Or a superset of current_clique that is of the required size.
    """
    global dead_end_cliques
    # base case 0: If current clique is already know to be a dead end, return False
    # for cs in range(clique_size_required+1):
    if frozenset(current_clique) in dead_end_cliques[clique_size_required]: 
        return False
    if frozenset(current_clique) in validated_cliques[clique_size_required]: 
        return validated_cliques[clique_size_required][frozenset(current_clique)]
    # Base case 1: If current clique is invalid, return False
    if not enough_shared_partners(current_clique): 
        dead_end_cliques[clique_size_required].add(frozenset(current_clique))
        return False
    # Base case 2: If current clique is large enough (and valid), return a clique
    if clique_size_required is None: clique_size_required = get_own_threshold(current_clique)
    if len(current_clique) >= clique_size_required:
        assert enough_shared_partners(current_clique) # should be redundant, but will only get called once
        validated_cliques[clique_size_required][frozenset(current_clique)] = frozenset(current_clique)
        return current_clique
    # Otherwise, we have a valid but not large enough clique.
    neighbor_sets = [metapartners[node] for node in current_clique]
    common_neighbors = set.intersection(*neighbor_sets) - set(current_clique) # (last bit redundant)
    for neighbor in common_neighbors:
        if valid_nodes is not None and neighbor not in valid_nodes: continue
        if invalid_nodes is not None and neighbor in invalid_nodes: continue
        new_clique = current_clique | {neighbor}
        result = dfs_clique_exists(new_clique, valid_nodes,invalid_nodes,clique_size_required,metapartners)
        if result:
            validated_cliques[clique_size_required][frozenset(current_clique)] = frozenset(result)
            return result
    # If we reach here, we didn't find a valid superset clique
    if len(current_clique) == 2:
        # If the current clique is of size 2, we can remove the edge between the two nodes
        # This has very marginal effect.
        node,partner = tuple(current_clique)
        metapartners[node].discard(partner)
        metapartners[partner].discard(node)
    dead_end_cliques[clique_size_required].add(frozenset(current_clique))
    return False




## %% (FILTER 3 & 4) Find the nodes that are part of a large enough metapartner clique
# Then Further restrict metapartner graph to only have edges if the neighbors are part of a clique together
# Restrict the metapartners to just those nodes that are part of such a clique.
def filter_metapartners_nodes(clique_size, metapartners=metapartners):
    """Filter metapartners to only those that are part of a clique of size >= clique_size."""
    
    validated_nodes = set()
    invalidated_nodes = set()

    for node in list(metapartners.keys()):
        if node in validated_nodes or node in invalidated_nodes: continue
        dfs_result = dfs_clique_exists({node},
                                       clique_size_required=min(clique_size, get_own_threshold(node)),
                                       metapartners=metapartners,
                                       invalid_nodes=invalidated_nodes,)
        if dfs_result:
            if PRINT_DFS_RESULTS and clique_size>=min(PF_REQUIRED,SF_REQUIRED): 
                print(dfs_result,get_shared_partners(dfs_result))
            validated_nodes = validated_nodes.union(dfs_result)
            validated_nodes.add(node)
        else:
            invalidated_nodes.add(node)

    metapartners.remove_nodes(invalidated_nodes)
    print(f"Size {clique_size}: Removed {len(invalidated_nodes)} nodes from metapartners graph. Remaining nodes:", 
          len(metapartners))
    assert validated_nodes.isdisjoint(invalidated_nodes)
    return metapartners

def filter_metapartners_edges(clique_size, metapartners=metapartners):
    """Filter metapartners to only those that are part of a clique of size >= clique_size."""
    
    validated_edges = set()
    invalidated_edges = set()

    for node in list(metapartners.keys()):
        for partner in list(metapartners[node]):
            edge = frozenset((node, partner))
            if edge in validated_edges or edge in invalidated_edges: continue
            dfs_result = dfs_clique_exists({node, partner},
                                           clique_size_required=min(clique_size, get_own_threshold(node)),
                                           metapartners=metapartners,)
            if dfs_result:
                # if PRINT_DFS_RESULTS and clique_size>=min(PF_REQUIRED,SF_REQUIRED): 
                #     print(dfs_result,get_shared_partners(dfs_result))
                validated_edges.add(edge)
                validated_edges.update(frozenset((n1, n2)) for n1 in dfs_result for n2 in dfs_result if n1 != n2)
            else:
                invalidated_edges.add(edge)
                # remove the edge from the metapartners graph
                metapartners[node].discard(partner)
                metapartners[partner].discard(node)
                metapartners.clean()

    print(f"Size {clique_size}: Removed {len(invalidated_edges)} edges from metapartners graph. Remaining edges:", 
          sum([len(v) for v in metapartners.values()]) // 2)
    assert validated_edges.isdisjoint(invalidated_edges)
    return metapartners


# for clique_size in range(1, max(PF_REQUIRED,SF_REQUIRED)+1):
# for clique_size in range(min(PF_REQUIRED,SF_REQUIRED), max(PF_REQUIRED,SF_REQUIRED)+1):
for clique_size in range(1, max(PF_REQUIRED,SF_REQUIRED)+1):
    metapartners = filter_metapartners_nodes(clique_size)
for clique_size in range(1, max(PF_REQUIRED,SF_REQUIRED)+1):
    metapartners = filter_metapartners_edges(clique_size)





#%%



#%% USE PREFIXES WITH CLIQUES TO FIND ALL SUCH CLIQUES
##%% Do a breadth first search for all maximal cliques
maximal_cliques_bfs = list() # each cell in the list is a set of maximal sets - cell 0 is size 1, cell 1 is size 2, etc
# prefixes_to_search = metapartners.keys() & prefixes
maximal_cliques_bfs.append({frozenset([p]) for p in metapartners.keys() }) # start with all singletons

for size in range(2, max(PF_REQUIRED,SF_REQUIRED)+10):
    print("BFS search for metapartner cliques of size", size, end=' ... ')
    new_cliques = set()
    for clique in maximal_cliques_bfs[size-2]: # size-2 because size starts at 2
        neighbor_sets = [metapartners[node] for node in clique]
        common_neighbors = set.intersection(*neighbor_sets) - set(clique) # (last bit redundant)
        for neighbor in common_neighbors:
            new_clique = clique | {neighbor}
            if enough_shared_partners(new_clique):
                new_cliques.add(frozenset(new_clique))
    maximal_cliques_bfs.append(new_cliques)
    print("Found", len(new_cliques), "cliques of size", size)
    if len(new_cliques) == 0: break


# flatten the results and "complete" the cliques back and forth
# (but only include the completions for the cliques that are big enough on their own merits)
# (the completion may introduce overlaps)
discovered_cliques = {frozenset(get_shared_partners(get_shared_partners(clique)))
                   for clique in set.union(*maximal_cliques_bfs)
                   if len(clique) >= get_own_threshold(clique)}
print(len(discovered_cliques), "discovered distinct and sufficient cliques after BFS search")


#%% If the prevent_overlap flag is set, 
#   we also want to check that the partners are actually a long enough clique.
#   This can be done by check whether partners are a superset of a valid clique of size N
def partners_are_long_enough(clique):
    """Check if the partners of a clique are long enough."""
    shared_partners = get_shared_partners(clique)
    comparison_sets = maximal_cliques_bfs[get_partner_threshold(clique)-1]
    for cs in comparison_sets:
        if shared_partners.issuperset(cs):
            return True
    return False

discovered_cliques = {clique for clique in discovered_cliques if partners_are_long_enough(clique)}
print(len(discovered_cliques), "discovered distinct and sufficient cliques after BFS search")


# %% Now filter the maximal cliques as follows:
# Iterate through the cliques in reverse order of size.
# Don't keep cliques which are :
#   subsets of cliques we've already decided to keep. 
#   and have partners that are the subset of a clique we've already decided to keep.
# TODO: check whether the ordering can still give us a double subset pair...

long_cliques = set()

for clique in sorted(discovered_cliques, key=lambda x: -len(x)):
    # print(clique)
    clique_supersets = {c for c in long_cliques if clique.issubset(c)}
    clique_partners = get_shared_partners(clique)
    if any (clique_partners.issubset(get_shared_partners(c)) for c in clique_supersets):
        continue
    else:
        long_cliques.add(clique)

print(len(long_cliques), "long cliques found with size >= threshold size", PF_REQUIRED,SF_REQUIRED)

# Now pair the prefixes and suffixes in the long cliques
long_clique_pairs = set()
for clique in long_cliques:
    shared_partners = get_shared_partners(clique)
    # ensure prefixes and suffixes are in the right order
    if next(iter(clique)).endswith("-"):
        biclique_prefixes, biclique_suffixes = frozenset(clique),frozenset(shared_partners)
    else:
        biclique_prefixes, biclique_suffixes = frozenset(shared_partners), frozenset(clique)
    long_clique_pairs.add((biclique_prefixes, biclique_suffixes))
print(len(long_clique_pairs), "bicliques found with size >= threshold size", PF_REQUIRED,SF_REQUIRED)


# ##%% SORT AND SAVE THE RESULTS

def clique_sort_function(clique_pair):
    """sort by prefix length, then suffix length, then alphabetically"""
    return (-len(clique_pair[0]), -len(clique_pair[1]), clique_pair[0],clique_pair[1],clique_pair)

long_clique_lists = [(sorted(p), sorted(s)) for p,s in long_clique_pairs]
long_clique_lists = sorted(long_clique_lists, key=clique_sort_function)

with open(OUTPUT_FILE, "w") as f:
    for p,s in long_clique_lists:
        f.write(f"{len(p)},{len(s)},{p},{s}\n")

for p,s in long_clique_lists:
    assert get_shared_partners(get_shared_partners(p)) >= set(p)
    assert get_shared_partners(get_shared_partners(s)) >= set(s)
























#%%
maximal_cliques = [p for p,s in long_clique_lists]

# %% FIND SUPERSETS OF THE ORIGINAL TOY
# original_prefixes = {'p-','b-','m-','h-','r-'}
# original_suffixes = {'-ad','-at','-ail','-ay','-ug'}

# print("Shared partners of original prefixes and suffixes:")
# print(get_shared_partners(original_prefixes))
# print(get_shared_partners(original_suffixes))
# #{'-ound', '-ill', '-uff', '-ail', '-ay', '-ush', '-ad', '-od', '-ug', '-are', '-ole', '-ate', '-atter', '-ock', '-at'}
# #{'b-', 'r-', 'h-', 'm-', 'p-'}



#%% FIND THE 5-cliques WITH LONGEST MINIMUM PREFIX/SUFFIX LENGTH
CSFTT =  CLIQUE_SIZE_FOR_TERRIBLE_TOY = 5

# Originally defaulted to zero, now set to the best known results
biggest_min_length_so_far = 5
biggest_min_word_so_far = 10
biggest_average_length_so_far = 6.3

for clique in maximal_cliques:
    if len(clique) >= CSFTT:
        shared_partners = get_shared_partners(clique)
        # filter to longest N prefixes and suffixes
        filtered_shared_partners = sorted(shared_partners, key=lambda x: -len(x))[:CSFTT]
        filtered_clique = sorted(clique, key=lambda x: -len(x))[:CSFTT]
        
        min_prefix_length = min(len(p)-1 for p in filtered_clique)
        min_suffix_length = min(len(s)-1 for s in filtered_shared_partners)
        min_chunk_length = min(min_prefix_length, min_suffix_length)
        min_word_length = min_prefix_length + min_suffix_length
        
        mean_prefix_length = sum(len(p)-1 for p in filtered_clique) / len(filtered_clique)
        mean_suffix_length = sum(len(s)-1 for s in filtered_shared_partners) / len(filtered_shared_partners)
        average_length = (mean_prefix_length + mean_suffix_length) / 2

        if min_chunk_length > biggest_min_length_so_far:
            biggest_min_length_so_far = min_chunk_length
            print("New biggest minimum chunk length:", biggest_min_length_so_far)
            print(filtered_clique, filtered_shared_partners, min_prefix_length, min_suffix_length)
        if min_word_length > biggest_min_word_so_far:
            biggest_min_word_so_far = min_word_length
            print("New biggest minimum word length:", biggest_min_word_so_far)
            print(filtered_clique, filtered_shared_partners, min_prefix_length, min_suffix_length)
        if average_length > biggest_average_length_so_far:
            biggest_average_length_so_far = average_length
            print("New biggest average length:", biggest_average_length_so_far)
            print(filtered_clique, filtered_shared_partners, min_prefix_length, min_suffix_length)
            
        # if min_chunk_length == biggest_min_length_so_far:
        #     biggest_min_length_so_far = min_chunk_length
        #     print("Tied results for min chunk length:", biggest_min_length_so_far)
        #     print(filtered_clique, filtered_shared_partners, min_prefix_length, min_suffix_length)

# Results for 6:
# ['sentiment-', 'individu-', 'ration-', 'nation-', 'neutr-', 'form-'] ['-alization', '-alism', '-ality', '-alist', '-alize', '-ally'] 4 4
# for 7:
# ['sentimental-', 'individual-', 'rational-', 'national-', 'neutral-', 'modern-', 'formal-'] ['-ization', '-ity', '-ize', '-ism', '-ist', '-ly'] 6 2
# For 5 (but I searched with a suffix threshold of 6, so some better (worse) results might exist):
# ['sentiment-', 'individu-', 'ration-', 'nation-', 'neutr-'] ['-alization', '-alism', '-ality', '-alist', '-alize'] 5 5

# This one might be the funniest for making a shitpost toy:
# ['sentimental-', 'national-', 'rational-', 'modern-', 'human-'] ['-ization', '-ity', '-ize', '-ism', '-ist'] 5 3

# with the 7 search and no overlap prevention:
# New biggest minimum chunk length: 1
# ['br-', 'sh-', 'h-', 'r-', 't-'] ['-ake', '-ush', '-ook', '-ow', '-ad'] 1 2
# New biggest minimum chunk length: 3
# ['individua-', 'nationa-', 'neutra-', 'forma-', 'rea-'] ['-lization', '-lity', '-lize', '-list', '-lism'] 3 4
# New biggest minimum chunk length: 4
# ['individu-', 'materi-', 'nation-', 'capit-', 'soci-'] ['-alization', '-alistic', '-alize', '-alism', '-alist'] 4 5
# New biggest minimum chunk length: 5
# ['individu-', 'materi-', 'nation-', 'ration-', 'natur-'] ['-alization', '-alistic', '-alize', '-alism', '-alist'] 5 5


# New biggest average length: 6.5
# ['comprehensi-', 'destructi-', 'responsi-', 'impressi-', 'suggesti-'] ['-veness', '-bility', '-vely', '-ble', '-ve'] 8 2
# New biggest average length: 6.6
# ['internationa-', 'sensationa-', 'sentimenta-', 'individua-', 'industria-'] ['-list', '-lize', '-lism', '-lly', '-l'] 9 1

# on the wp corpus:
# New biggest minimum chunk length: 6
# ['institution-', 'internation-', 'profession-', 'commerci-', 'conceptu-'] ['-alisation', '-alization', '-alizing', '-alised', '-alized'] 8 6
# New biggest minimum word length: 14
# ['institution-', 'internation-', 'profession-', 'commerci-', 'conceptu-'] ['-alisation', '-alization', '-alizing', '-alised', '-alized'] 8 6
# New biggest average length: 8.5
# ['institution-', 'internation-', 'profession-', 'commerci-', 'conceptu-'] ['-alisation', '-alization', '-alizing', '-alised', '-alized'] 8 6
#
# a smattering of at least min chunk 7:
# {'languag-', 'structur-', 'architectur-', 'hardwar-', 'temperatur-'} {'-especific', '-edependent', '-eindependent', '-edriven', '-erelated'}
# {'temperature-', 'pressure-', 'insulin-', 'protein-', 'estrogen-'} {'-regulated', '-related', '-dependent', '-independent', '-induced'}
# {'histori-', 'crystall-', 'phytoge-', 'chromat-', 'cinemat-'} {'-ographic', '-ographically', '-ographer', '-ography', '-ographers'}
# 'parasit-', 'microbi-', 'anthrop-', 'endocrin-', 'pharmac-'} {'-ologist', '-ological', '-ologically', '-ologica', '-ologists'}
# New biggest minimum chunk length: 7
# ['constitutio-', 'institutio-', 'internatio-', 'conventio-', 'professio-'] ['-nalisation', '-nalization', '-nalizing', '-nalised', '-nalized'] 9 7
# New biggest minimum word length: 16
# ['constitutio-', 'institutio-', 'internatio-', 'conventio-', 'professio-'] ['-nalisation', '-nalization', '-nalizing', '-nalised', '-nalized'] 9 7
# New biggest average length: 9.100000000000001
# ['constitutio-', 'institutio-', 'internatio-', 'conventio-', 'professio-'] ['-nalisation', '-nalization', '-nalizing', '-nalised', '-nalized'] 9 7
# New biggest average length: 9.5
# ['deinstituti-', 'constituti-', 'nondimensi-', 'instituti-', 'internati-'] ['-onalization', '-onalisation', '-onalizing', '-onalized', '-onalize'] 9 7
# New biggest minimum chunk length: 8
# ['constituti-', 'instituti-', 'internati-', 'conventi-', 'professi-'] ['-onalization', '-onalisation', '-onalizing', '-onalised', '-onalized'] 8 8
#
# New biggest minimum word length: 17
# ['constitutional-', 'anthropomorph-', 'compartmental-', 'institutional-', 'international-'] ['-isation', '-ization', '-ising', '-izing', '-ized'] 13 4
# New biggest average length: 9.399999999999999
# ['constitutional-', 'anthropomorph-', 'compartmental-', 'institutional-', 'international-'] ['-isation', '-ization', '-ising', '-izing', '-ized'] 13 4
# New biggest average length: 9.4
# ['anthropomorph-', 'institutional-', 'mischaracter-', 'reconceptual-', 'recontextual-'] ['-izations', '-isation', '-ization', '-ising', '-izing'] 12 5


# New biggest minimum word length: 17
# ['constitutional-', 'anthropomorph-', 'compartmental-', 'institutional-', 'international-'] ['-isation', '-ization', '-izing', '-ized', '-ised'] 13 4
# New biggest average length: 9.3
# ['constitutional-', 'anthropomorph-', 'compartmental-', 'institutional-', 'international-'] ['-isation', '-ization', '-izing', '-ized', '-ised'] 13 4
# New biggest average length: 9.399999999999999
# ['constitutional-', 'anthropomorph-', 'compartmental-', 'institutional-', 'international-'] ['-isation', '-ization', '-ising', '-izing', '-ized'] 13 4
# New biggest minimum chunk length: 6
# ['constitution-', 'compartment-', 'institution-', 'internation-', 'convention-'] ['-alisation', '-alization', '-alizing', '-alised', '-alized'] 10 6
# New biggest average length: 9.5
# ['deinstitutional-', 'constitutional-', 'nondimensional-', 'anthropomorph-', 'compartmental-'] ['-isation', '-ization', '-izing', '-ized', '-ize'] 13 3
# *** New biggest average length: 9.6
# ['otorhinolaryng-', 'psychopharmac-', 'electrophysi-', 'paleoanthrop-', 'dendrochron-'] ['-ological', '-ologists', '-ologist', '-ologic', '-ology'] 11 5
# New biggest minimum chunk length: 7
# ['constitut-', 'institut-', 'internat-', 'convent-', 'profess-'] ['-ionalization', '-ionalisation', '-ionalizing', '-ionalists', '-ionalised'] 7 9
# New biggest minimum chunk length: 8
# ['constituti-', 'instituti-', 'internati-', 'conventi-', 'professi-'] ['-onalization', '-onalisation', '-onalizing', '-onalised', '-onalists'] 8 8



#%% SAME BUT FOR SHORTEST MAXIMUM LENGTH
CSFRT =  CLIQUE_SIZE_FOR_REASONABLE_TOY = 7

# smallest_max_length_so_far = 99999
# smallest_max_word_so_far = 99999
smallest_max_length_so_far = 2
smallest_max_word_so_far = 4

for clique in maximal_cliques:
    if len(clique) >= CSFRT:
        shared_partners = get_shared_partners(clique)
        # filter to shortest N prefixes and suffixes
        filtered_shared_partners = sorted(shared_partners, key=lambda x: len(x))[:CSFRT]
        filtered_clique = sorted(clique, key=lambda x: len(x))[:CSFRT]
        max_prefix_length = max(len(p)-1 for p in filtered_clique)
        max_suffix_length = max(len(s)-1 for s in filtered_shared_partners)
        max_chunk_length = max(max_prefix_length, max_suffix_length)
        max_word_length = max_prefix_length + max_suffix_length
        if max_chunk_length < smallest_max_length_so_far:
            smallest_max_length_so_far = max_chunk_length
            print("New smallest maximum chunk length:", smallest_max_length_so_far)
            print(filtered_clique, filtered_shared_partners, max_prefix_length, max_suffix_length)
        if max_word_length < smallest_max_word_so_far:
            smallest_max_word_so_far = max_word_length
            print("New smallest maximum word length:", smallest_max_word_so_far)
            print(filtered_clique, filtered_shared_partners, max_prefix_length, max_suffix_length)


# meh. For this, I feel like some lexicographic sorting would be better.
# ['ra-', 'sa-', 'pa-', 'mo-', 'la-', 'co-', 'ha-'] ['-d', '-w', '-p', '-ck', '-te', '-ve'] 2 2

# with 7,7 thresholds and no overlap prevention:
# New smallest maximum chunk length: 3
# ['l-', 'r-', 's-', 'w-', 'st-', 'sl-', 'br-'] ['-ow', '-ag', '-ay', '-ick', '-ake', '-ash', '-ave'] 2 3
# New smallest maximum chunk length: 2
# ['mo-', 'co-', 'sa-', 'ra-', 'ha-', 'pa-', 'ro-'] ['-t', '-d', '-w', '-te', '-ve', '-ck', '-il'] 2 2


# Here are some results with only 3 letter words:
# ['c-', 'h-', 'l-', 'm-', 'r-', 's-'],['-ad', '-ap', '-aw', '-ay', '-ob', '-ot', '-ow']






# I reran with only long words. Didn't improve the best, but here are some new terrible word sets
# New biggest minimum chunk length: 2
# ['administra-', 'interroga-', 'demonstra-', 'manipula-', 'apprecia-'] ['-tively', '-tive', '-tion', '-tor', '-te'] 8 2
# New biggest minimum word length: 10
# ['administra-', 'interroga-', 'demonstra-', 'manipula-', 'apprecia-'] ['-tively', '-tive', '-tion', '-tor', '-te'] 8 2
# New biggest minimum chunk length: 3
# ['individual-', 'rational-', 'material-', 'militar-', 'natural-'] ['-ization', '-istic', '-ize', '-ist', '-ism'] 7 3
# New biggest minimum chunk length: 4
# ['individua-', 'nationa-', 'rationa-', 'materia-', 'natura-'] ['-lization', '-listic', '-list', '-lize', '-lism'] 6 4
# New biggest minimum chunk length: 5
# ['individu-', 'ration-', 'materi-', 'nation-', 'natur-'] ['-alization', '-alistic', '-alism', '-alist', '-alize'] 5 5
# New smallest maximum chunk length: 11
# ['permissi-', 'impressi-', 'percepti-', 'suggesti-', 'exhausti-', 'destructi-', 'comprehensi-'] ['-ve', '-on', '-ble', '-vely', '-veness'] 11 6
# New smallest maximum word length: 17
# ['permissi-', 'impressi-', 'percepti-', 'suggesti-', 'exhausti-', 'destructi-', 'comprehensi-'] ['-ve', '-on', '-ble', '-vely', '-veness'] 11 6
# New smallest maximum chunk length: 9
# ['permissi-', 'impressi-', 'expressi-', 'suggesti-', 'exhausti-', 'percepti-', 'destructi-'] ['-ve', '-on', '-ble', '-vely', '-veness'] 9 6
# New smallest maximum word length: 15
# ['permissi-', 'impressi-', 'expressi-', 'suggesti-', 'exhausti-', 'percepti-', 'destructi-'] ['-ve', '-on', '-ble', '-vely', '-veness'] 9 6
# New smallest maximum chunk length: 8
# ['impress-', 'permiss-', 'express-', 'percept-', 'suggest-', 'exhaust-', 'destruct-'] ['-ion', '-ive', '-ible', '-ively', '-iveness'] 8 7



# %%
