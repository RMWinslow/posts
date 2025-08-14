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

# # 2of12 comes from http://wordlist.aspell.net/12dicts/ 
with open("./2of12.txt", "r") as f: words = set(f.read().splitlines())
ALIAS="12dicts"

# # filtered version of 12dicts from here: https://github.com/InnovativeInventor/dict4schools
# # safedict_simple.txt removes both innappriate and complex words,... supposedly
# # lots of abbreviations in there though -_-
# with open("./safedict_simple.txt", "r") as f: safedict_words = set(f.read().splitlines())
# words = words.intersection(safedict_words)
# ALIAS="12dicts_childfriendly"

# wikipedia wordlist from here: https://github.com/IlyaSemenov/wikipedia-word-frequency/tree/master
# with open("./enwiki-2023-04-13.txt", "r", encoding="utf8") as f: 
#     words = set()
#     for line in f.read().splitlines():
#         # each line is a word and a number, separated by a space
#         # I want to keep the word only if the number is greater than 50, alphabetical, and lowercase
#         word, count = line.split()
#         if int(count) < 1000: continue 
#         # if len(word) < 5: continue # This will hopefully remove most abbreviations
#         if word.isalpha() and word.islower():
#             words.add(word)
# ALIAS="wikipedia"

# words = {"ax","bx","cx","dx",}
# ALIAS="testlist"

# medical wordlist from here: https://github.com/glutanimate/wordlist-medicalterms-en/blob/master/wordlist.txt
# with open("./medical wordlist.txt", "r", encoding="utf8") as f:  words = set(f.read().splitlines())
# words = {w for w in words if not w[0].isupper()} # ignore capitalized words
# ALIAS="medical"


THRESHOLD_PREFIX = 7 # clique size
THRESHOLD_SUFFIX = 7 # required suffixes for each prefix

MAX_WORD_LENGTH = None # maximum length of a word to consider
PREVENT_OVERLAP = False # if True, don't pair prefixes that are the start or end of the other

max_word_length_str = f"_maxl{MAX_WORD_LENGTH}" if MAX_WORD_LENGTH else ""
OUTPUT_FILE = f"bicliques_{THRESHOLD_PREFIX}_{THRESHOLD_SUFFIX}_pvovl{int(PREVENT_OVERLAP)}{max_word_length_str}_{ALIAS}.txt"







# %% PRE-FILTERING / CLEANUP
words = {w.replace("'","") for w in words} # remove apostrophes
words = {w.replace("-","") for w in words} # remove hyphens
words = {w.lower() for w in words} # lowercase (the words should already be lowercase)
words = list(set(words)) # remove duplicates
words = {w for w in words if len(w) >= 2}
if MAX_WORD_LENGTH: words = {w for w in words if len(w) <= MAX_WORD_LENGTH}
print(len(words), "words after pre-filtering")



#%% BREAK WORDS INTO ALL POSSIBLE (PREFIX,SUFFIX) PAIRS
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




#%% ITERATIVELY REDUCE THE ELEMENTS UNDER CONSIDERATION

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


# PAIRS WILL NO LONGER CHANGE AFTER THIS POINT
# Anyways, here's a little helper function
def get_shared_partners(nodes, pairs=pairs):
    return set.intersection(*[pairs[node] for node in nodes])









#%% FIND METAPARTNERS
# A metapartner is a partner that has at least THRESHOLD partners in common

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




# filter the metapartners to only those with at least N-1 metapartners
metapartners = {k: v for k, v in metapartners.items() if len(v) >= min(THRESHOLD_SUFFIX,THRESHOLD_PREFIX)-1}
#remove any metapartners that are not valid, as defined by previous line
metapartners = {k: v.intersection(metapartners.keys()) for k, v in metapartners.items()}

print(len(metapartners), "nodes in metapartner graph after filtering")














#%% DEPTH FIRST SEARCH FOR EXISTENCE OF A CLIQUE
# The metapartners are now like nodes in a graph.
# and a necessary condition for an N- biclique is an N-clique of metapartners.


# Now do a depth-first search to find cliques of size N
# I might regret doing it this way, but I'll do an initial iteration
# where I just check whether an N-clique exists for a particular node, 
# without finding all possible N-cliques.

def dfs_clique_exists(current_clique,prefix_clique_size=THRESHOLD_PREFIX,suffixes_required=THRESHOLD_SUFFIX,valid_nodes=None, invalid_nodes=None):
    shared_partners = get_shared_partners(current_clique)
    # Base case 1: If current clique is invalid, return False
    if len(shared_partners) < suffixes_required:
        return False
    # Base case 2: If current clique is large enough (and valid), return a clique
    if len(current_clique) >= prefix_clique_size:
        assert len(shared_partners) >= suffixes_required # should be redundant, but will only get called once
        print(current_clique,shared_partners)
        return current_clique
    # Otherwise, we have a valid but not large enough clique.
    neighbor_sets = [metapartners[node] for node in current_clique]
    common_neighbors = set.intersection(*neighbor_sets) - set(current_clique) # (last bit redundant)
    for neighbor in common_neighbors:
        if valid_nodes is not None and neighbor not in valid_nodes: continue
        if invalid_nodes is not None and neighbor in invalid_nodes: continue
        new_clique = current_clique | {neighbor}
        result = dfs_clique_exists(new_clique, prefix_clique_size,suffixes_required)
        if result:
            return result
    return False

# iterate through prefixes to find every one with valid cliques
# prefixes_with_cliques = prefixes.copy() # these are implicitly prefixes with 1-cliques
prefixes_with_cliques = prefixes & metapartners.keys() # These must have at least some metapartners

# for clique_size in range(3, THRESHOLD_PREFIX+1):
# for clique_size in [5,THRESHOLD_PREFIX]:
for clique_size in [THRESHOLD_PREFIX]:
    invalid_nodes = set()
    print("checking for prefix cliques of size", clique_size)
    prefixes_with_bigger_cliques = set()
    for prefix in prefixes_with_cliques:
        if prefix in prefixes_with_bigger_cliques: continue
        dfs_result = dfs_clique_exists({prefix}, prefix_clique_size=clique_size, valid_nodes=prefixes_with_cliques, invalid_nodes=invalid_nodes)
        if dfs_result:
            prefixes_with_bigger_cliques = prefixes_with_bigger_cliques.union(dfs_result)
        else:
            invalid_nodes.add(prefix)
            # print("invalid node:", prefix)
    print(len(prefixes_with_bigger_cliques), "prefixes with cliques found of length", clique_size)
    prefixes_with_cliques = prefixes_with_bigger_cliques

    if not prefixes_with_cliques:
        print("No prefix cliques of size", clique_size)
        break

# note: I thought the iterative approach would speed things up,
# but it seems slower than just checking for maximum depth from the start.








#%% USE PREFIXES WITH CLIQUES TO FIND ALL SUCH CLIQUES
metapartners_with_cliques = {k: v.intersection(prefixes_with_cliques) for k, v in metapartners.items() if k in prefixes_with_cliques}

def check_valid_clique(clique, suffixes_required=THRESHOLD_SUFFIX):
    # Check that the clique has enough partners in common
    shared_partners = get_shared_partners(clique)
    if PREVENT_OVERLAP: shared_partners = lazy_overlap_filter(shared_partners)
    if len(shared_partners) < suffixes_required: return False
    return True

def lazy_overlap_filter(suffixes):
    # Used for the PREVENT_OVERLAP option.
    # it's plausible this will overzealously filter
    # eg with {-abc, -ab, -bc}, we'd like to keep {-ab,-bc}...
    # and with {-c,-cad, -cab}, we'd like to keep {-cad,-cab}...
    # that makes things more difficult, but I think I'll err on the side of removing the shorter option.
    filtered_suffixes = set()
    for suffix1 in sorted(suffixes, key=lambda x: -len(x)):
        if not any(check_overlap(suffix1, suffix2) for suffix2 in filtered_suffixes):
            filtered_suffixes.add(suffix1)
    return filtered_suffixes

# check whether there is *potentially* another element to add to the clique
# this is a necessary but NOT sufficient condition for a bigger clique to exist.
# I am using this as prefiltering.
# There must be an additional prefix which N-n shared metapartners with the clique,
# AND the clique with that prefix added must have enough suffixes in common.
def potential_bigger_clique(clique, mpcs=metapartners_with_cliques, clique_size=THRESHOLD_PREFIX, suffixes_required=THRESHOLD_SUFFIX):
    shared_metapartners = set.intersection(*[mpcs[node] for node in clique])
    for sm in shared_metapartners-set(clique):
        if len(mpcs[sm] & shared_metapartners) >= clique_size-len(clique)-1:
            if check_valid_clique(clique | {sm}, suffixes_required=suffixes_required):
                return True
    return False

# Validate that with the mps they have, there are potential pairs, triads, etc.
def trim_mpcs(mpcs=metapartners_with_cliques, clique_size=THRESHOLD_PREFIX, suffixes_required=THRESHOLD_SUFFIX):
    # We can skip the check for clique_size=1, since all prefixes in mpcs are part of *some* clique
    values_have_changed = 0
    # validate the pairs.
    for k,v in mpcs.items():
        for p in v.copy():
            if not potential_bigger_clique({k,p}, mpcs,clique_size,suffixes_required):
                v.remove(p)
                values_have_changed += 1
    # validate triads
    for k,v in mpcs.items():
        for p1 in v.copy():
            if not any(potential_bigger_clique({k,p1,p2}, mpcs,clique_size,suffixes_required) for p2 in v if p2 != p1):
                v.remove(p1)
                values_have_changed += 1

    # and then remove any metapartners without enough remaining partners
    # and remove them as metapartners from other prefixes
    nodes_to_remove = {k for k,v in metapartners_with_cliques.items() if len(v) < clique_size-1}
    for k,v in metapartners_with_cliques.items():
        metapartners_with_cliques[k] = v - nodes_to_remove
    for node in nodes_to_remove:
        if node in metapartners_with_cliques:
            del metapartners_with_cliques[node]
    return values_have_changed

for i in range(100):
    changed_value_count = trim_mpcs()
    print("iteration",i, "; changed values:", changed_value_count)
    if changed_value_count==0: break

print(len(metapartners_with_cliques), "metapartners with cliques after trimming")
print(min(len(v) for v in metapartners_with_cliques.values()), "minimum number of partners in common")
print(sum(len(v) for v in metapartners_with_cliques.values()), "total partners in common")


#%%
maximal_cliques = set()

# assumption: after searching for superset cliques of a particular clique,
# we don't ever need to check that clique or its supersets again.
valid_checked_cliques = set()
invalid_checked_cliques = set() 

total_loop_count = 0

def dfs_clique_fullsearch(current_clique, suffixes_required=THRESHOLD_SUFFIX):

    # print(current_clique)
    # global total_loop_count
    # total_loop_count += 1
    # if total_loop_count%1000000==0: print(total_loop_count, len(maximal_cliques), current_clique)

    # Base case 0: skip if this clique has already been checked
    if current_clique in valid_checked_cliques:
        # print("skipping checked clique:", current_clique)
        return True
    if current_clique in invalid_checked_cliques:
        # print("skipping invalid clique:", current_clique)
        return False

    # Base case 1: If current clique is invalid, return False and store it as invalid
    if check_valid_clique(current_clique, suffixes_required) is False:
        invalid_checked_cliques.add(frozenset(current_clique))
        return False # returning False here means this clique is not valid

    # Otherwise, we have a valid clique.
    neighbor_sets = [metapartners_with_cliques[node] for node in current_clique]
    common_neighbors = set.intersection(*neighbor_sets) - set(current_clique) # (last bit redundant)
    
    bigger_clique_exists = False
    for neighbor in common_neighbors:
        new_clique = current_clique | {neighbor}
        if dfs_clique_fullsearch(new_clique):
            bigger_clique_exists = True

    if not bigger_clique_exists:
        maximal_cliques.add(frozenset(current_clique)) # add the bigger clique found
        # print("found maximal clique:", current_clique, "with shared partners:", shared_partners)
    
    valid_checked_cliques.add(frozenset(current_clique)) # By assumption, we never need to search for supersets of this clique again
    # print("exhausting clique:", current_clique)

    return True # If we return True, it simply means this particular clique is "valid" (but not necessarily maximal)


#iterate through enumerated prefixes with cliques
for i,prefix in enumerate(prefixes_with_cliques):
    print("full search for maximal cliques including prefix", i+1, "of", len(prefixes_with_cliques), ":", prefix)
    dfs_clique_fullsearch({prefix})
    # if i==6: break # TEMPORARY LIMIT FOR TESTING


print('---')
print(len(maximal_cliques))
print(max([len(mc) for mc in maximal_cliques]))
# for mc in maximal_cliques: print(','.join(sorted(mc)))




##%%
# FILTER MAXIMAL_CLIQUES
long_cliques = {c for c in maximal_cliques if len(c) >= THRESHOLD_PREFIX}
for lc in long_cliques: print(lc)
print(len(long_cliques), "long cliques found with size >= threshold prefix size", THRESHOLD_PREFIX)


##%% SORT AND SAVE THE RESULTS

long_clique_lists = [sorted(c) for c in long_cliques]
clique_sort = lambda x: (-len(x), -len(get_shared_partners(x)), x) # sort by pf length, then sf length, then alphabetically
long_clique_lists = sorted(long_clique_lists, key=clique_sort)


with open(OUTPUT_FILE, "w") as f:
    for clique in long_clique_lists:
        clique_suffixes = sorted(get_shared_partners(clique))
        f.write(f"{len(clique)},{len(clique_suffixes)},{clique},{clique_suffixes}\n")








































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

biggest_min_length_so_far = 0
biggest_min_word_so_far = 0
biggest_average_length_so_far = 0

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




#%% SAME BUT FOR SHORTEST MAXIMUM LENGTH
CSFRT =  CLIQUE_SIZE_FOR_REASONABLE_TOY = 7

smallest_max_length_so_far = 99999
smallest_max_word_so_far = 99999

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
