#%%
'''
This file takes in a word list and searches for a large "biqlique"
which here means a set of word endings and beginnings such that any
pair of endings and beginnings can be combined to form a valid word.

Here, I want to use BFS

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

# # 2of12 comes from http://wordlist.aspell.net/12dicts/ 
with open("./2of12.txt", "r") as f: words = set(f.read().splitlines())
ALIAS="12dicts"


MIN_PREFIX_CLIQUE = 5
MIN_SUFFIX_CLIQUE = 5

MAX_WORD_LENGTH = None # maximum length of a word to consider
MIN_WORD_LENGTH = None # maximum length of a word to consider
MIN_NODE_LENGTH = 2 # minimum length of a prefix or suffix to consider


OUTPUT_FILE = f"bicliques_dfs_{ALIAS}.txt"



# %% PRE-FILTERING / CLEANUP
words = {w.replace("'","") for w in words} # remove apostrophes
words = {w.replace("-","") for w in words} # remove hyphens
words = {w.lower() for w in words} # lowercase (the words should already be lowercase)
words = list(set(words)) # remove duplicates
words = {w for w in words if len(w) >= 2}
if MAX_WORD_LENGTH: words = {w for w in words if len(w) <= MAX_WORD_LENGTH}
if MIN_WORD_LENGTH: words = {w for w in words if len(w) >= MIN_WORD_LENGTH}
print(len(words), "words after pre-filtering")


#%% BREAK WORDS INTO ALL POSSIBLE (PREFIX,SUFFIX) PAIRS
from collections import defaultdict
pairs = defaultdict(set)
for w in words:
    for i in range(1,len(w)):
        prefix = w[:i]+"-"
        suffix = "-"+w[i:]
        if MIN_NODE_LENGTH and (len(prefix)<MIN_NODE_LENGTH+1 or len(suffix)<MIN_NODE_LENGTH+1): continue
        pairs[prefix].add(suffix)
        pairs[suffix].add(prefix)

suffixes = {k for k in pairs if k.startswith("-")}
prefixes = {k for k in pairs if k.endswith("-")}
print(len(prefixes),"prefixes ;", len(suffixes),"suffixes")

# %%
def count_shared_partners(clique):
    shared_partners = set.intersection(*(pairs[node] for node in clique))
    return len(shared_partners)

metapartners = defaultdict(set)











# start by getting the pairs of prefixes that share at least one suffix
metapartners = defaultdict(set)
for p1 in prefixes:
    partners = pairs[p1]  # get the set of suffixes for this prefix
    for p2 in set.union(*[pairs[s] for s in partners]):
        if p2 in prefixes:  # only consider suffixes that are also prefixes
            metapartners[p1].add(p2)
            pairs[p2].add(p1)

len(metapartners)