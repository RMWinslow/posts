'''
I downloaded some public domain texts from
https://corpus.canterbury.ac.nz/descriptions/#cantrbry
The "Canterbury Corpus", and I take a look at the most common first letters.
Mostly, what I'm trying to do is find a "consensus" for most common and least common.
'''

#%%
from collections import Counter

def clean_corpus(corpus_file):
    with open(corpus_file, 'r') as file:
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

alice = file_to_counts('alice29.txt')
milton = file_to_counts('plrabn12.txt')
tech = file_to_counts('lcet10.txt')
billy = file_to_counts('asyoulik.txt')


def top_n_intersection(count_dicts, n=12):
    top_n_sets = [set(dict(Counter(d).most_common(n)).keys()) for d in count_dicts]
    common_letters = set.intersection(*top_n_sets)
    return common_letters

# and least common
def bottom_n_intersection(count_dicts, n=12):
    bottom_n_sets = [set(dict(Counter(d).most_common()[:-n-1:-1]).keys()) for d in count_dicts]
    common_letters = set.intersection(*bottom_n_sets)
    return common_letters


common_top_letters = top_n_intersection([alice, milton, tech, billy], n=12)
print("Consensus most common first letters:", common_top_letters)

least_common_letters = bottom_n_intersection([alice, milton, tech, billy], n=12)
print("Consensus least common first letters:", least_common_letters)

# print the remaining letters
all_letters = set('abcdefghijklmnopqrstuvwxyz')
remaining_letters = all_letters - common_top_letters - least_common_letters
print("Remaining letters:", remaining_letters)


#%% count the 


