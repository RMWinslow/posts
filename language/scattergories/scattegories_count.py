'''
I downloaded some public domain texts from
https://corpus.canterbury.ac.nz/descriptions/#cantrbry
The "Canterbury Corpus", and I take a look at the most common first letters.
Mostly, what I'm trying to do is find a "consensus" for most common and least common.
'''

#%%
from collections import Counter




CORPUS_FILE = 'alice29.txt'
# CORPUS_FILE = 'lcet10.txt'
CORPUS_FILE = 'plrabn12.txt'

# open the corpus and:
#    remove linebreaks after "-"
#    replace other line breaks with spaces
#    remove all non-alphabetic characters except spaces
with open(CORPUS_FILE, 'r') as file:
    text = file.read()
text = text.replace('-\n', '')  # Remove linebreaks after "-"
text = text.replace('\n', ' ')  # Replace other line breaks with spaces 
import re
text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove all non-alphabetic characters except spaces
# Split the cleaned text into words
words = text.split()
# Initialize a Counter to count word beginnings
first_letters = Counter()
word_counts = Counter()
# Iterate through each word and count the first letter
for word in words:
    first_letters[word[0].lower()] += 1
    word_counts[word.lower()] += 1


first_letters.most_common()
# word_counts.most_common(10)

# # %% Now examine only unique words
unique_words = set(words)
first_letters_unique = Counter()
for word in unique_words:
    first_letters_unique[word[0].lower()] += 1
first_letters_unique.most_common()


