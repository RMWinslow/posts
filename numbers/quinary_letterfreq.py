
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

Using all the consonants in brown corpus:
[('dhnrst', 340606), ('dfhnst', 336843), ('fhnrst', 336489), ('dhnstw', 331623), ('dfhnrt', 327819), ('hnrstw', 323694), ('dhmnst', 323033), ('fhnstw', 320288), ('bdhnst', 318552), ('dhlnst', 316376), ('fhrstw', 315850), ('hmnrst', 312222), ('cdhnst', 310994), ('fhmnst', 309364), ('dghnst', 309281), ('fhmrst', 307999), ('fhnrtw', 307919), ('bfhnst', 306589), ('dhnrtw', 305849), ('dhnpst', 305461), ('fhlnst', 305328), ('bhnrst', 305142), ('dfhntw', 304615), ('hmnstw', 304599), ('chnrst', 303636), ('fhmnrt', 303524), ('dfhrst', 303498), ('hlnrst', 303139), ('bhnstw', 301920), ('bfhrst', 301510), ('hlnstw', 301362), ('ghnrst', 301153), ('dhnstv', 300998), ('fhlrst', 300847), ('bdfhnt', 300743), ('bfhnrt', 300031), ('cfhnst', 299622), ('hnprst', 298645), ('dfhmnt', 298145), ('dhmnrt', 297844), ('dhknst', 297761), ('fghnst', 297074), ('bdhnrt', 297000), ('dfhlnt', 295518), ('dhnstx', 295473), ('chnstw', 295444), ('dhnqst', 294957), ('dhjnst', 294895), ('fhlnrt', 294165), ('dhnstz', 294023), ('cfhrst', 294018), ('fhnpst', 293132), ('hnrstv', 292259), ('ghnstw', 292236), ('fghnrt', 292062), ('fhprst', 291922), ('bhmnst', 291329), ('dghnrt', 290854), ('cfhnrt', 290849), ('fhnstv', 290676), ('dhlnrt', 290478), ('fghrst', 289876), ('cdfhnt', 289324), ('dfghnt', 289243), ('hlmnst', 288802), ('cdhnrt', 288460), ('fhrstv', 288385), ('hnpstw', 288095), ('fhknst', 287096), ('fhnrtv', 286677), ('fhnprt', 286389), ('chmnst', 286107), ('dhrstw', 285693), ('fhnstx', 285518), ('hnstvw', 285499), ('bdhntw', 285327), ('dfhnpt', 285176), ('bhlnst', 285119), ('fhnqst', 285063), ('fhjnst', 285036), ('dfhntv', 284672), ('dhnprt', 284609), ('fhlstw', 284427), ('fhnstz', 284209), ('hmrstw', 284170), ('ghmnst', 283969), ('hknstw', 283795), ('hknrst', 283791), ('hlrstw', 283087), ('dhlntw', 282909), ('dhnrtv', 282880), ('dhmntw', 282532), ('hnrstx', 282045), ('hnqrst', 282042), ('hjnrst', 281673), ('fhkrst', 281624), ('bhrstw', 281612), ('bfhstw', 281458), ('dfhknt', 280896), ('hnrstz', 280741)]

[('cjkvwz', 29540), ('djkvxz', 29527), ('cdjqxz', 29516), ('djkqvz', 29510), ('cjkvwx', 29490), ('cgjkpx', 29482), ('cgkpqz', 29481), ('ckqvwx', 29478), ('cgkpqx', 29477), ('gjkpvx', 29460), ('gjkpqv', 29455), ('ckqvwz', 29448), ('djkqvx', 29439), ('cgkpxz', 29410), ('gkpvxz', 29406), ('gkpqvz', 29403), ('gkpqvx', 29397), ('ckvwxz', 29395), ('dkqvxz', 29384), ('djqvxz', 29342), ('djkqxz', 29266), ('jmqvxz', 29236), ('cjlqxz', 29220), ('gjpvxz', 29168), ('gjpqvz', 29162), ('jkvwxz', 29104), ('jkqvwz', 29083), ('gjpqvx', 29075), ('cjkqwz', 29073), ('gpqvxz', 29046), ('jkqvwx', 29029), ('cjvwxz', 29026), ('cjkqwx', 29020), ('cjkwxz', 29019), ('cgjpxz', 29016), ('cgjpqz', 29008), ('cjqvwz', 28999), ('kqvwxz', 28955), ('cjqvwx', 28948), ('ckqwxz', 28928), ('cgjpqx', 28922), ('cqvwxz', 28881), ('cgpqxz', 28878), ('jkqwxz', 28836), ('gjkpxz', 28816), ('gjkpqz', 28814), ('gjkpqx', 28725), ('gkpqxz', 28674), ('jqvwxz', 28634), ('cjkpvz', 28558), ('cjkpqv', 28556), ('ckpqvx', 28497), ('cjkpvx', 28488), ('ckpqvz', 28487), ('cjqwxz', 28485), ('gjpqxz', 28439), ('ckpvxz', 28417), ('cjkpqz', 28334), ('cjkpxz', 28263), ('cjkpqx', 28261), ('ckpqxz', 28193), ('cjpvxz', 28024), ('cjpqvz', 28015), ('cjpqvx', 27943), ('cpqvxz', 27900), ('cjpqxz', 27726), ('jkpvxz', 27562), ('jkpqvz', 27559), ('jkpqxz', 27538), ('cgjkvz', 27488), ('jkpqvx', 27484), ('cgjkqv', 27476), ('kpqvxz', 27434), ('cgjkvx', 27409), ('cgkqvx', 27398), ('cgkqvz', 27397), ('cgkvxz', 27328), ('cgjvxz', 27313), ('cgjqvz', 27302), ('cgjqvx', 27222), ('jpqvxz', 27180), ('cgqvxz', 27169), ('gjkvxz', 27056), ('gjkqvz', 27051), ('gjkqvx', 26968), ('gjqvxz', 26938), ('gkqvxz', 26908), ('cgjkqz', 26552), ('cgjkxz', 26482), ('cgjkqx', 26470), ('cgkqxz', 26392), ('gjkqxz', 26319), ('cgjqxz', 26303), ('cjkqvz', 25644), ('cjkqvx', 25576), ('cjkvxz', 25575), ('ckqvxz', 25499), ('cjqvxz', 25391), ('cjkqxz', 25347), ('jkqvxz', 25146)]
'''