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



# %% PRE-FILTERING / cleanup

words = {w.replace("'","") for w in words} # remove apostrophes
words = {w.replace("-","") for w in words} # remove hyphens
words = {w.lower() for w in words} # lowercase (the words should already be lowercase)

words = {w for w in words if (len(w) >= 2 and len(w) <= 6)}

words = list(set(words)) # remove duplicates

print(len(words))



#%% Break words into all possible (prefix,suffix) pairs
from collections import defaultdict
pairs = defaultdict(set)
for w in words:
    for i in range(1,len(w)):
        prefix = w[:i]+"-"
        suffix = "-"+w[i:]
        pairs[prefix].add(suffix)
        pairs[suffix].add(prefix)

len(pairs)




#%% iteratively reduce the elements under consideration

THRESHOLD = 5 # minimum number of associated suffixes for a prefix to be considered or vice versa
# partner_count = {k: len(v) for k, v in pairs.items()}

def reduce_pairs(pairs=pairs, threshold=THRESHOLD):
    # Iterate through and recount "valid partners" for each element.
    # A valid partner is one that has at least THRESHOLD associated valid partners.
    # This should converge quickly unless I make a bug.
    changed_value_count = 0
    for k, v in pairs.items():
        current_partner_count = len(v)
        valid_partners = {p for p in v if len(pairs[p]) >= threshold}
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
pairs = {k: v for k, v in pairs.items() if len(v) >= THRESHOLD}
suffixes = {k for k in pairs if k.startswith("-")}
prefixes = {k for k in pairs if k.endswith("-")}
print(len(prefixes),"prefixes ;", len(suffixes),"suffixes remain")






# %%
