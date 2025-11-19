'''
I downloaded some public domain texts from
https://corpus.canterbury.ac.nz/descriptions/#cantrbry
The "Canterbury Corpus", and I take a look at the most common first letters.
Mostly, what I'm trying to do is find a "consensus" for most common and least common.
'''

#%%
from collections import Counter

def clean_corpus(corpus_file):
    with open(corpus_file, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.replace('-\n', '')  # Remove linebreaks after "-"
    text = text.replace('\n', ' ')  # Replace other line breaks with spaces 
    import re
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove all non-alphabetic characters except spaces
    text = text.lower()  # Convert to lowercase
    words = text.split()
    return words

def count_unique_first_letters(word_list):
    first_letters = Counter()
    unique_words = set(word_list)
    for word in unique_words:
        first_letters[word[0].lower()] += 1
    # now add a zero entry for any letter not present
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in first_letters:
            first_letters[letter] = 0
    return first_letters

def file_to_counts(corpus_file):
    words = clean_corpus(corpus_file)
    counts = count_unique_first_letters(words)
    return counts

def query_letter(corpus_file, letter):
    "Return Counter of words in corpus that start with letter"
    words = clean_corpus(corpus_file)
    filtered_words = [word for word in words if word.startswith(letter.lower())]
    return Counter(filtered_words).most_common()

#%%
# Load multiple corpus files and take the intersection of twelve most common first letters

canterbury_corpus_files = ['alice29.txt', 'plrabn12.txt', 'lcet10.txt', 'asyoulik.txt','pg100.txt']
canterbury_individual_counts = [file_to_counts(f) for f in canterbury_corpus_files]

alice = file_to_counts('alice29.txt')
milton = file_to_counts('plrabn12.txt')
tech = file_to_counts('lcet10.txt')
ayl = file_to_counts('asyoulik.txt')
billy = file_to_counts('pg100.txt')

# also create a corpus by adding the words from all four together
# clean the four word corpus files and add them together
canterbury_combined = []
for f in canterbury_corpus_files:
    canterbury_combined.extend(clean_corpus(f))
canterbury_combined_counts = count_unique_first_letters(canterbury_combined)



def top_n_intersection(count_dicts, n=12):
    top_n_sets = [set(dict(Counter(d).most_common(n)).keys()) for d in count_dicts]
    common_letters = set.intersection(*top_n_sets)
    return common_letters

# and least common
def bottom_n_intersection(count_dicts, n=12):
    bottom_n_sets = [set(dict(Counter(d).most_common()[:-n-1:-1]).keys()) for d in count_dicts]
    common_letters = set.intersection(*bottom_n_sets)
    return common_letters



SETS_TO_USE = canterbury_individual_counts
# SETS_TO_USE = [canterbury_combined_counts]
N = 12


common_top_letters = top_n_intersection(SETS_TO_USE, n=N)
print("Consensus most common first letters:", common_top_letters)

least_common_letters = bottom_n_intersection(SETS_TO_USE, n=N)
print("Consensus least common first letters:", least_common_letters)

# print the remaining letters
all_letters = set('abcdefghijklmnopqrstuvwxyz')
remaining_letters = all_letters - common_top_letters - least_common_letters
print("Remaining letters:", remaining_letters)


#%% sorted list of alice letters
sorted_alice = sorted(alice.items(), key=lambda x: x[1], reverse=True)
set(_[0] for _ in sorted_alice[:12]) - common_top_letters












#%% likewise for complete works of shakespeare
sorted_billy = sorted(billy.items(), key=lambda x: x[1], reverse=True)
# [('s', 3422),
#  ('c', 2681),
#  ('p', 2284),
#  ('b', 1882),
#  ('d', 1830),
#  ('t', 1689),
#  ('a', 1659),
#  ('f', 1511),
#  ('m', 1509),
#  ('r', 1387),
#  ('h', 1245),
#  ('w', 1185),
#  ('e', 1110),
#  ('l', 1104),
#  ('u', 963),
#  ('g', 946),
#  ('i', 945),
#  ('o', 815),
#  ('n', 585),
#  ('v', 512),
#  ('j', 260),
#  ('k', 207),
#  ('q', 162),
#  ('y', 137),
#  ('z', 16),
#  ('x', 12)]

set(_[0] for _ in sorted_billy[:12]) - common_top_letters #{'b', 'h', 'w'}


#%%

## function to choose a word starting with a letter
# pick the most common, excluding very short words and the letter itself
# (unless there are no other options)
def choose_example_word(corpus_file, letter):
    words_counter = query_letter(corpus_file, letter)
    for word, count in words_counter:
        if len(word) > 4:
            return word
    # if no longer word found, return the most common entry (which might be 'the', 'and', etc)
    return words_counter[0][0] if words_counter else ''

# function to print a markdown table from a corpus
# columns are letter, count, percentage, example word
def print_corpus_table(corpus_file):
    counts = file_to_counts(corpus_file)
    total_unique = sum(counts.values())
    print("| Letter | Count | Percentage | Example Word |")
    print("|--------|-------|------------|--------------|")
    # sort by letter count descending
    for letter, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_unique) * 100
        example_word = choose_example_word(corpus_file, letter)
        print(f"|   {letter}   |  {count}  |   {percentage:.2f}%   | {example_word} |")

print_corpus_table('alice29.txt')

print_corpus_table('pg100.txt')






# %% IMDB titles from tsv
# title.basics.tsv


# read first few lines to look at format
with open('title.basics.tsv', 'r', encoding='utf-8') as f:
    for _ in range(20):
        print(f.readline())

# note: third column is "primaryTitle", ie english title
imdb_titles = []
with open('title.basics.tsv', 'r', encoding='utf-8') as f:
    next(f)  # skip header
    for line in f:
        parts = line.split('\t')
        title = parts[2]
        imdb_titles.append(title)

#%%
# Now strip articles "The", "A", "An" from start of titles
# and cast to lowercase while we're at it
# also strip non
def clean_imdb_title(title):
    title = title.lower()
    for article in ['the ', 'a ', 'an ']:
        if title.startswith(article):
            title = title[len(article):]
            break
    return title
imdb_titles_cleaned = [clean_imdb_title(title) for title in imdb_titles]
imdb_counts = count_unique_first_letters(imdb_titles_cleaned)

# Counter({'s': 473482,
#          'm': 349873,
#          'c': 315081,
#          'd': 312523,
#          'b': 308012,
#          'l': 296990,
#          't': 293037,
#          'a': 287913,
#          'e': 260050,
#          'p': 248348,
#          'h': 210529,
#          'f': 200158,
#          'w': 195018,
#          'r': 189572,
#          'g': 175533,
#          'i': 166997,
#          'n': 155446,
#          'k': 138771,
#          'j': 124075,
#          'o': 118083,
#          'v': 86909,
#          'u': 79501,
#          '2': 58875,
#          '1': 58387,
#          'y': 43508,
#          'z': 28979,
#          'q': 19352,
#          '3': 14264,
#          '5': 9117,
#          '4': 8947,
#          '#': 8212,
#          '7': 6660,
#          'x': 6524,
#          "'": 6393,
#          '6': 5643,
#          '"': 5516,
#          '9': 5241,
#          'é': 5156,
#          '8': 5002,
#          '0': 4343,
#          '¡': 3493,
#          '¿': 3464,
#          '(': 2732,
#          '.': 1761,
#          'à': 1443,
#          'á': 1014,
#          'ö': 987,
#          'ü': 976,
#          '$': 973,
#          'ä': 757,
#          'ç': 739,
#          'å': 583,
#          'ô': 582,
#          'ú': 553,
#          '*': 325,
#          '«': 298,
#          '@': 231,
#          '[': 222,
#          'ó': 208,
#          'ø': 189,
#          '-': 167,
#          'è': 166,
#          'ê': 152,
#          'â': 151,
#          'í': 148,
#          'î': 140,
#          'æ': 115,
#          'þ': 97,
#          '+': 81,
#          '&': 62,
#          '£': 62,
#          '/': 60,
#          '_': 45,
#          'õ': 41,
#          '?': 37,
#          'ñ': 35,
#          'ò': 32,
#          ':': 30,
#          '~': 27,
#          'û': 25,
#          'ì': 19,
#          '»': 17,
#          '×': 16,
#          '!': 15,
#          '<': 14,
#          '>': 13,
#          ',': 8,
#          '`': 7,
#          '½': 7,
#          '%': 7,
#          '§': 7,
#          '=': 6,
#          '¥': 5,
#          'ã': 4,
#          '^': 4,
#          'ë': 4,
#          ';': 4,
#          '\\': 3,
#          '|': 3,
#          '鉄': 3,
#          '¨': 3,
#          'ï': 2,
#          'µ': 2,
#          'ż': 1,
#          'ù': 1,
#          ')': 1,
#          '姆': 1,
#          'а': 1,
#          '©': 1})


#%%
# what starts with © ???
def query_imdb_letter(letter):
    "Return Counter of words in imdb titles that start with letter"
    filtered_titles = [title for title in imdb_titles_cleaned if title.startswith(letter.lower())]
    return Counter(filtered_titles).most_common()

query_imdb_letter('2')

# lots of tv episodes with dates and other broken entries. 
# I might need to come back to the imdb stuff.


