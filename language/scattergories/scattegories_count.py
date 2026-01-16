'''
I downloaded some public domain texts from
https://corpus.canterbury.ac.nz/descriptions/#cantrbry
The "Canterbury Corpus", and I take a look at the most common first letters.
Mostly, what I'm trying to do is find a "consensus" for most common and least common.
'''
#%%
from collections import Counter

from typing import List, Set, Dict, Tuple
import re
from functools import cached_property



class Corpus:
    def __init__(self, source: str):
        self.source = source
    
    # WORD LIST (REQUIRES SUBCLASS TO IMPLEMENT _load_and_clean)
    @cached_property
    def words(self) -> List[str]:
        return self._load_and_clean()
    
    def _load_and_clean(self) -> List[str]:
        """Load and clean the corpus. Must be implemented by subclasses."""
        raise NotImplementedError
    
    # FIRST LETTER COUNTS
    @cached_property
    def first_letter_counts(self) -> Counter:
        return self._count_unique_first_letters()
    
    def _count_unique_first_letters(self) -> Counter:
        """Count unique words starting with each letter. 
        Then add zero entries for missing letters."""
        first_letters = Counter()
        unique_words = set(self.words)
        
        for word in unique_words:
            if word: first_letters[word[0].lower()] += 1
        
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter not in first_letters:
                first_letters[letter] = 0
        
        return first_letters
    
    # QUERYING AND ANALYSIS FUNCTIONS
    def query_letter(self, letter: str) -> List[Tuple[str, int]]:
        """Return most common words starting with the given letter."""
        filtered_words = [word for word in self.words if word.startswith(letter.lower())]
        return Counter(filtered_words).most_common()
    
    def choose_example_word(self, letter: str, min_length: int = 4) -> str:
        """Choose a representative word starting with the given letter.
        Avoid short words if possible.
        If not, avoid common words like 'a', 'an', 'the'.
        If no other options, return the most common word."""
        words_counter = self.query_letter(letter)

        # Prefer longer words
        for word, count in words_counter:
            if len(word) > min_length:
                return word

        # Among short words, avoid very common ones
        common_exclusions = {'a', 'an', 'the', 'and', 'of', 'in', 'to', 'is', 'it', 'that'}
        for word, count in words_counter:
            if word not in common_exclusions:
                return word

        # Fall back to most common word
        return words_counter[0][0] if words_counter else ''
    
    def get_sorted_counts(self, reverse: bool = True) -> List[Tuple[str, int]]:
        """Return letter counts sorted by frequency."""
        return sorted(self.first_letter_counts.items(), key=lambda x: x[1], reverse=reverse)
    
    def print_table(self):
        """Print a formatted markdown table of letter frequencies."""
        counts = self.first_letter_counts
        total_unique = sum(counts.values())
        
        print(f"\n### {self.source}")
        print("| Letter | Count | Percentage | Example Word |")
        print("|--------|-------|------------|--------------|")
        
        for letter, count in self.get_sorted_counts():
            percentage = (count / total_unique) * 100 if total_unique > 0 else 0
            example_word = self.choose_example_word(letter)
            print(f"|   {letter}   |  {count}  |   {percentage:.2f}%   | {example_word} |")


class TextFileCorpus(Corpus):
    def __init__(self, source: str, exclude_numbers: bool = True):
        super().__init__(source)
        self.exclude_numbers = exclude_numbers
    
    def _load_and_clean(self) -> List[str]:
        with open(self.source, 'r', encoding='utf-8') as f:
            text = f.read().lower()
        text = text.replace('-\n', '')  # Remove linebreaks after "-"
        text = text.replace('\n', ' ')  # Replace other line breaks with spaces 
        
        # remove all non-alphanumeric characters except spaces (and possibly numbers)
        if self.exclude_numbers:
            text = re.sub(r'[^a-z\s]', '', text)
        else:
            text = re.sub(r'[^a-z0-9\s]', '', text)

        words = text.split()
        return words

class IMDBTitleCorpus(Corpus):
    def _load_and_clean(self) -> List[str]:
        titles = []
        with open(self.source, 'r', encoding='utf-8') as f:
            next(f)  # skip header
            for line in f:
                parts = line.split('\t')
                title = parts[2]  # primaryTitle
                title = title.lower()
                for article in ['the ', 'a ', 'an ']:
                    if title.startswith(article):
                        title = title[len(article):]
                        break
                titles.append(title)
        return titles
    def query_letter(self, letter):
        return super().query_letter(letter)
    
imdb = IMDBTitleCorpus('title.basics.tsv')
imdb.print_table()



#%% SHAKESPEARE EXAMPLE
billy = TextFileCorpus('pg100.txt') # Complete Works of Shakespeare
billy.print_table()

# | Letter | Count | Percentage | Example Word |
# |--------|-------|------------|--------------|
# |   s   |  3422  |   11.38%   | shall |
# |   c   |  2681  |   8.92%   | cannot |
# |   p   |  2284  |   7.60%   | prince |
# |   b   |  1882  |   6.26%   | before |
# |   d   |  1830  |   6.09%   | death |
# |   t   |  1689  |   5.62%   | their |
# |   a   |  1659  |   5.52%   | again |
# |   f   |  1511  |   5.03%   | first |
# |   m   |  1509  |   5.02%   | master |
# |   r   |  1387  |   4.61%   | richard |
# |   h   |  1245  |   4.14%   | heart |
# |   w   |  1185  |   3.94%   | which |
# |   e   |  1110  |   3.69%   | enter |
# |   l   |  1104  |   3.67%   | leave |
# |   u   |  963  |   3.20%   | under |
# |   g   |  946  |   3.15%   | great |
# |   i   |  945  |   3.14%   | indeed |
# |   o   |  815  |   2.71%   | other |
# |   n   |  585  |   1.95%   | never |
# |   v   |  512  |   1.70%   | villain |
# |   j   |  260  |   0.86%   | justice |
# |   k   |  207  |   0.69%   | kings |
# |   q   |  162  |   0.54%   | queen |
# |   y   |  137  |   0.46%   | young |
# |   z   |  16  |   0.05%   | zounds |
# |   x   |  12  |   0.04%   | xanthippe |


#%% ALICE EXAMPLE
alice = TextFileCorpus('alice29.txt')
alice.print_table()

# | Letter | Count | Percentage | Example Word |
# |--------|-------|------------|--------------|
# |   s   |  339  |   12.30%   | seemed |
# |   c   |  222  |   8.06%   | could |
# |   t   |  204  |   7.40%   | there |
# |   p   |  182  |   6.61%   | please |
# |   f   |  168  |   6.10%   | first |
# |   a   |  149  |   5.41%   | alice |
# |   b   |  148  |   5.37%   | began |
# |   w   |  141  |   5.12%   | would |
# |   d   |  139  |   5.05%   | dormouse |
# |   m   |  131  |   4.75%   | mouse |
# |   l   |  126  |   4.57%   | little |
# |   r   |  124  |   4.50%   | rabbit |
# |   h   |  122  |   4.43%   | herself |
# |   e   |  102  |   3.70%   | enough |
# |   g   |  81  |   2.94%   | gryphon |
# |   i   |  75  |   2.72%   | indeed |
# |   o   |  60  |   2.18%   | other |
# |   n   |  58  |   2.11%   | never |
# |   u   |  49  |   1.78%   | under |
# |   k   |  35  |   1.27%   | knave |
# |   v   |  28  |   1.02%   | voice |
# |   y   |  26  |   0.94%   | youre |
# |   j   |  21  |   0.76%   | jumped |
# |   q   |  20  |   0.73%   | queen |
# |   x   |  3  |   0.11%   | x |
# |   z   |  2  |   0.07%   | zealand |

#%% Paradise Lost example
milton = TextFileCorpus('plrabn12.txt')
milton.print_table()

# | Letter | Count | Percentage | Example Word |
# |--------|-------|------------|--------------|
# |   s   |  1108  |   11.78%   | shall |
# |   c   |  702  |   7.46%   | could |
# |   a   |  664  |   7.06%   | against |
# |   d   |  663  |   7.05%   | death |
# |   p   |  627  |   6.67%   | place |
# |   r   |  532  |   5.66%   | round |
# |   t   |  480  |   5.10%   | their |
# |   f   |  464  |   4.93%   | first |
# |   e   |  460  |   4.89%   | earth |
# |   b   |  457  |   4.86%   | before |
# |   i   |  450  |   4.78%   | image |
# |   m   |  416  |   4.42%   | might |
# |   u   |  359  |   3.82%   | under |
# |   h   |  346  |   3.68%   | heaven |
# |   w   |  333  |   3.54%   | which |
# |   l   |  303  |   3.22%   | light |
# |   g   |  276  |   2.93%   | great |
# |   o   |  265  |   2.82%   | other |
# |   v   |  164  |   1.74%   | voice |
# |   n   |  146  |   1.55%   | night |
# |   j   |  67  |   0.71%   | judge |
# |   k   |  51  |   0.54%   | knowledge |
# |   q   |  33  |   0.35%   | quite |
# |   y   |  28  |   0.30%   | yield |
# |   z   |  9  |   0.10%   | zephon |
# |   x   |  4  |   0.04%   | xerxes |



















# lots of tv episodes with dates and other broken entries. 
# I might need to come back to the imdb stuff.


