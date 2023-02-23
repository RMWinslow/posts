
#%%
import nltk
nltk.download('brown')
nltk.download('gutenberg')
nltk.download('reuters')
nltk.download('nps_chat')
from nltk.corpus import brown, gutenberg, reuters, nps_chat
word_count = nltk.FreqDist(brown.words())

# %%
complete_word_list = set(word_count.keys())

allowable_letters = set("aeiouyzwthrf")
subset_word_list = [word for word in complete_word_list if set(word).issubset(allowable_letters)]
subset_word_count = {word:word_count[word] for word in subset_word_list}
print(sum(subset_word_count.values()))

def wordScore(letters):
    # calculates total count of words containing only letters in letters string or list
    allowable_letters = set(letters)
    subset_word_list = [word for word in complete_word_list if set(word.lower()).issubset(allowable_letters)]
    #subset_word_list = [word for word in complete_word_list if set(word).issubset(allowable_letters)]
    subset_word_count = {word:word_count[word] for word in subset_word_list}
    return sum(subset_word_count.values())





# %%
# which letters to check?
#abcdefghijklmnopqrstuvwxyz
#removing vowels and consonants in quinary:
# bcd fgh       pqrst vwx z
# 15 choose 6 is only 5005. So it's feasible to check every option.
from itertools import combinations
from collections import Counter
subset_counts = Counter()
for combo in combinations("bcdfghpqrstvwxz",6):
    letters = list('.:;-"aeiouy') + list(combo)
    subset_counts["".join(list(combo))] = wordScore(letters)


# %%
print(subset_counts.most_common()[:10])












# %%
letter_count = Counter()
for word, count in word_count.items():
    for c in word:
        letter_count[c] += count

print(letter_count.most_common())










# %% --------------------------------------------------------------------------------------------------
# further restrict analysis to alternating consonants and vowels
CORPUS = brown

consonants = set("bcdfghjklmnpqrstvwxz")
vowels = set("aeiouy")
def checkForAlternation(word):
    if len(word) == 0: return False # lots of number words we want to ignore
    #return True # uncomment to remove alternation restriction
    shouldBeVowels = word[::-1][::2] # first index reverse string, second index looks at every other char
    shouldBeConsonants = word[::-1][1::2]
    #if word[0] in consonants and word[-1] in consonants: return False # must begin or end with a vowel
    if set(shouldBeVowels).issubset(vowels) and set(shouldBeConsonants).issubset(consonants): return True
    if set(shouldBeVowels).issubset(consonants) and set(shouldBeConsonants).issubset(vowels): return True
    else: return False


uncleaned_word_count = nltk.FreqDist(CORPUS.words())
cleaned_word_count = Counter()
for word, count in uncleaned_word_count.items():
    newword = word.lower()
    newword = ''.join([c for c in word if c.isalpha()])
    if checkForAlternation(newword):
        cleaned_word_count[newword] += count

cleaned_word_list = set(cleaned_word_count.keys())
print(len(cleaned_word_list))
print(cleaned_word_count.most_common()[:10])

def cleaned_wordScore(letters):
    allowable_letters = set(letters)
    subset_word_list = [word for word in cleaned_word_list if set(word).issubset(allowable_letters)]
    subset_word_count = {word:word_count[word] for word in subset_word_list}
    return sum(subset_word_count.values())


#%%
cleaned_subset_counts = Counter()
for combo in combinations("bcdfghpqrstvwxz",6):
#for combo in combinations("bcdfghjklmnpqrstvwxz",6):
    letters = list('aeiouy') + list(combo)
    cleaned_subset_counts["".join(list(combo))] = cleaned_wordScore(letters)

print(cleaned_subset_counts.most_common()[:10])



# %%
'''
Results:

Alternation:
Brown: fhrstw/fnrstw
Gutenberg: fhrstw/fnrstw

Alteration which begins/ends with vowel:
Brown: bfhrst/bfnrst
Gutenberg: bfhrst/bfnrst

Alteration which ends with vowel:
Brown: bhrtvw/bhmnrt
Gutenberg: bhrtvw/bhmnrt

Is gutenberg just brown plus some stuff?

Using all the consonants:

'''