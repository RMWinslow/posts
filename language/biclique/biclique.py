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

# 2of12 comes from http://wordlist.aspell.net/12dicts/ 
with open("./2of12.txt", "r") as f: words = set(f.read().splitlines())
# words


THRESHOLD_PREFIX = 7 # minimum number of associated suffixes for a prefix to be considered or 
THRESHOLD_SUFFIX = 7 # vice versa

MAX_WORD_LENGTH = None # maximum length of a word to consider
PREVENT_OVERLAP = True # if True, don't pair prefixes that are the start or end of the other






# %% PRE-FILTERING / cleanup
words = {w.replace("'","") for w in words} # remove apostrophes
words = {w.replace("-","") for w in words} # remove hyphens
words = {w.lower() for w in words} # lowercase (the words should already be lowercase)
words = list(set(words)) # remove duplicates
words = {w for w in words if len(w) >= 2}
if MAX_WORD_LENGTH: words = {w for w in words if len(w) <= MAX_WORD_LENGTH}
print(len(words), "words after pre-filtering")



#%% Break words into all possible (prefix,suffix) pairs
from collections import defaultdict
pairs = defaultdict(set)
for w in words:
    for i in range(1,len(w)):
        prefix = w[:i]+"-"
        suffix = "-"+w[i:]
        pairs[prefix].add(suffix)
        pairs[suffix].add(prefix)

suffixes = {k for k in pairs if k.startswith("-")}
prefixes = {k for k in pairs if k.endswith("-")}
print(len(prefixes),"prefixes ;", len(suffixes),"suffixes")




#%% iteratively reduce the elements under consideration

print("reducing prefixes and suffixes to those with at least", THRESHOLD_PREFIX,'/',THRESHOLD_SUFFIX, "valid partners")

def threshold_check(key,partners, threshold_p=THRESHOLD_PREFIX, threshold_s=THRESHOLD_SUFFIX):
    if key.startswith("-"):
        return len(partners) >= threshold_s
    elif key.endswith("-"):
        return len(partners) >= threshold_p
    else:
        raise ValueError("Key must start or end with '-'")

def reduce_pairs(pairs=pairs):
    # Iterate through and recount "valid partners" for each element.
    # A valid partner is one that has at least THRESHOLD associated valid partners.
    # This should converge quickly unless I make a bug.
    changed_value_count = 0
    for k, v in pairs.items():
        current_partner_count = len(v)
        valid_partners = {p for p in v if threshold_check(p,pairs[p])}
        new_partner_count = len(valid_partners)
        pairs[k] = valid_partners
        if new_partner_count != current_partner_count:
            changed_value_count += 1
    return changed_value_count

for i in range(100):
    changed_value_count = reduce_pairs()
    print("iteration",i, "; changed values:", changed_value_count)
    if changed_value_count==0: break

# Final pass to remove any elements that don't meet the threshold
pairs = {k: v for k, v in pairs.items() if threshold_check(k, v)}
suffixes = {k for k in pairs if k.startswith("-")}
prefixes = {k for k in pairs if k.endswith("-")}
print(len(prefixes),"prefixes ;", len(suffixes),"suffixes remain")




#%% Find Metapartners
# A metapartner is a partner that has at least THRESHOLD partners in common
# To be valid, I need not only N partners, 
# but there must also be N-1 other fragments that share at least N partners with me.

metapartners = defaultdict(set)

def check_overlap(f1,f2):
    f1 = f1.strip("-")
    f2 = f2.strip("-")
    if f1.endswith(f2) or f1.startswith(f2) or f2.endswith(f1) or f2.startswith(f1):
        return True
    else:
        return False

for k,v in pairs.items():
    potential_metapartners = set().union(*[pairs[p] for p in v])
    # print(k,len(potential_metapartners))
    metapartners[k] = {p for p in potential_metapartners if p != k and threshold_check(k,pairs[p].intersection(v))}
    if PREVENT_OVERLAP: 
        metapartners[k] = {p for p in metapartners[k] if not check_overlap(k,p)}
    # print(k,len(metapartners[k]))




#%% DEPTH FIRST SEARCH for existence of a clique
# The metapartners are now like nodes in a graph.
# and a necessary condition for an N- biclique is an N-clique of metapartners.


# Now do a depth-first search to find cliques of size N
# I might regret doing it this way, but I'll do an initial iteration
# where I just check whether an N-clique exists for a particular node, 
# without finding all possible N-cliques.

def dfs_clique_exists(current_clique,prefix_clique_size=THRESHOLD_PREFIX,suffixes_required=THRESHOLD_SUFFIX,valid_nodes=None):
    shared_partners = set.intersection(*[pairs[node] for node in current_clique])
    # Base case 1: If current clique is invalid, return False
    if len(shared_partners) < suffixes_required:
        return False
    # Base case 2: If current clique is large enough (and valid), return ~~True~~ a clique
    if len(current_clique) >= prefix_clique_size:
        assert len(shared_partners) >= suffixes_required # should be redundant, but will only get called once
        print(current_clique,shared_partners)
        return current_clique
    # Otherwise, we have a valid but not large enough clique.
    neighbor_sets = [metapartners[node] for node in current_clique]
    common_neighbors = set.intersection(*neighbor_sets) - set(current_clique) # (last bit redundant)
    for neighbor in common_neighbors:
        if valid_nodes is not None and neighbor not in valid_nodes:
            continue
        new_clique = current_clique | {neighbor}
        result = dfs_clique_exists(new_clique, prefix_clique_size,suffixes_required)
        if result:
            return result
    return False

# dfs_clique_exists({"-at","b-","p-","m-","h-"})
# dfs_clique_exists({"b-"})

# iterate through prefixes to find every one with valid cliques
prefixes_with_cliques = prefixes.copy() # these are implicitly prefixes with 1-cliques

for clique_size in range(3, THRESHOLD_PREFIX+1):
# for clique_size in range(THRESHOLD, THRESHOLD+1):
    print("checking for prefix cliques of size", clique_size)
    prefixes_with_bigger_cliques = set()
    for prefix in prefixes_with_cliques:
        if prefix in prefixes_with_bigger_cliques: continue
        dfs_result = dfs_clique_exists({prefix}, prefix_clique_size=clique_size, valid_nodes=prefixes_with_cliques)
        if dfs_result:
            prefixes_with_bigger_cliques = prefixes_with_bigger_cliques.union(dfs_result)
    print(len(prefixes_with_bigger_cliques), "prefixes with cliques found of length", clique_size)
    prefixes_with_cliques = prefixes_with_bigger_cliques

    if not prefixes_with_cliques:
        print("No more prefixes with cliques found of length", clique_size)
        break




#%% Use prefixes with cliques to find ALL such cliques
# I won't use "overlap" filtering on the suffixes, but I can do that as a second pass.

maximal_cliques = set()

def dfs_clique_fullsearch(current_clique, suffixes_required=THRESHOLD_SUFFIX):

    shared_partners = set.intersection(*[pairs[node] for node in current_clique])

    if PREVENT_OVERLAP:
        # it's plausible this will overzealously filter
        # eg with {-abc, -ab, -bc}, we'd like to keep {-ab,-bc}...
        # and with {-c,-cad, -cab}, we'd like to keep {-cad,-cab}...
        # that makes things more difficult, but I think I'll err on the side of removing the shorter option.
        filtered_shared_partners = set()
        for partner1 in sorted(shared_partners, key=lambda x: -len(x)):
            if not any(check_overlap(partner1, partner2) for partner2 in filtered_shared_partners):
                filtered_shared_partners.add(partner1)
        shared_partners = filtered_shared_partners


    # Base case 1: If current clique is invalid, return False
    if len(shared_partners) < suffixes_required:
        return False # returning False here means this clique is not valid

    # Otherwise, we have a valid clique.
    neighbor_sets = [metapartners[node] for node in current_clique]
    common_neighbors = set.intersection(*neighbor_sets) - set(current_clique) # (last bit redundant)
    
    bigger_clique_exists = False
    for neighbor in common_neighbors:
        new_clique = current_clique | {neighbor}
        if dfs_clique_fullsearch(new_clique):
            bigger_clique_exists = True

    if not bigger_clique_exists:
        maximal_cliques.add(frozenset(current_clique)) # add the bigger clique found
    
    return True # If we return True, it simply means this particular clique is "valid" (but not necessarily maximal)


for prefix in prefixes_with_cliques:
    dfs_clique_fullsearch({prefix})

print(len(maximal_cliques))


#%%
# filter maximal_cliques
long_cliques = {c for c in maximal_cliques if len(c) >= THRESHOLD_PREFIX}
for lc in long_cliques: print(lc)


# %%
