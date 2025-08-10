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




#%% step 2 in reduction: find metapartners

# To be valid, I need not only N partners, 
# but there must also be N-1 other fragments that share at least N partners with me.
metapartners = defaultdict(set)

for k,v in pairs.items():
    potential_metapartners = set().union(*[pairs[p] for p in v])
    # print(k,len(potential_metapartners))
    metapartners[k] = {p for p in potential_metapartners if p != k and len(pairs[p].intersection(v)) >= THRESHOLD}
    # print(k,len(metapartners[k]))


print(sum([len(v) for v in metapartners.values()]), "metapartners found")



print(sum([len(v) for v in metapartners.values()]), "metapartners found")


# Furthermore, to be a valid metapartner, we must also share at least N-2 metapartners with each other
# (not including the two of us)
# for k,v in metapartners.items():
#     valid_metapartners = {p for p in v if len(metapartners[p].intersection(v)) >= THRESHOLD-2}
#     metapartners[k] = valid_metapartners

# print(sum([len(v) for v in metapartners.values()]), "metapartners found")

# Furthermore, the N-2 shared metapartners must also have N shared partners with each of us.

def reduce_to_valid_triads(metapartners=metapartners, pairs=pairs, threshold=THRESHOLD):
    # Iterate through and remove any metapartners that don't meet the criteria
    changed_value_count = 0
    for k, v in metapartners.items():
        current_metapartners = set(v) # make a copy to iterate over
        for mp in current_metapartners:
            shared_mp = metapartners[mp] & current_metapartners
            valid_shared_metapartners = {mmp for mmp in shared_mp if len(pairs[k] & pairs[mp] & pairs[mmp]) >= threshold}
            if len(valid_shared_metapartners) < threshold-2:
                metapartners[k].remove(mp)
                changed_value_count += 1
    return changed_value_count

for i in range(100):
    changed_value_count = reduce_to_valid_triads()
    print("iteration",i, "; changed values:", changed_value_count)
    if changed_value_count==0: break


print(sum([len(v) for v in metapartners.values()]), "metapartners found")
