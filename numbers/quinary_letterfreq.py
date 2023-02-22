
#%%
import nltk
nltk.download('brown')
nltk.download('gutenberg')
nltk.download('reuters')
nltk.download('nps_chat')
from nltk.corpus import brown, gutenberg, reuters, nps_chat
word_count = nltk.FreqDist(nps_chat.words())

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

# %%
