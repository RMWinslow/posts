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
        self.original_titles = dict()
        titles = []
        with open(self.source, 'r', encoding='utf-8') as f:
            next(f)  # skip header
            for line in f:
                parts = line.split('\t')
                titleType = parts[1]
                if titleType not in ['movie', 'tvMovie']:
                    continue
                original_title = title = parts[2]  # primaryTitle
                title = title.lower()
                for article in ['the ', 'a ', 'an ']:
                    if title.startswith(article):
                        title = title[len(article):]
                        break
                titles.append(title)
                self.original_titles[title] = original_title
        return titles
    

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



#%%


imdb = IMDBTitleCorpus('title.basics.tsv')
imdb.print_table()

# | Letter | Count | Percentage | Example Word |
# |--------|-------|------------|--------------|
# |   s   |  69269  |   9.31%   | stranger |
# |   m   |  52237  |   7.02%   | macbeth |
# |   l   |  50305  |   6.76%   | legacy |
# |   d   |  48646  |   6.54%   | don giovanni |
# |   b   |  44129  |   5.93%   | broken |
# |   a   |  41672  |   5.60%   | alone |
# |   c   |  40390  |   5.43%   | carmen |
# |   t   |  37973  |   5.10%   | trapped |
# |   p   |  35318  |   4.75%   | promise |
# |   h   |  30872  |   4.15%   | hamlet |
# |   r   |  27224  |   3.66%   | reunion |
# |   f   |  26784  |   3.60%   | family |
# |   g   |  25062  |   3.37%   | guardian |
# |   e   |  24950  |   3.35%   | escape |
# |   k   |  24895  |   3.35%   | karma |
# |   i   |  24653  |   3.31%   | inheritance |
# |   w   |  24470  |   3.29%   | weekend |
# |   n   |  22289  |   3.00%   | nightmare |
# |   o   |  19375  |   2.60%   | other side |
# |   u   |  15492  |   2.08%   | untitled |
# |   j   |  14550  |   1.96%   | journey |
# |   v   |  13678  |   1.84%   | vengeance |
# |   y   |  7267  |   0.98%   | youth |
# |   z   |  5499  |   0.74%   | zero hour |
# |   q   |  2936  |   0.39%   | quest |
# |   1   |  2884  |   0.39%   | 11:11 |
# |   2   |  1700  |   0.23%   | 24 hours |
# |   3   |  1164  |   0.16%   | 30 days |
# |   x   |  1083  |   0.15%   | xenophobia |
# |   5   |  743  |   0.10%   | 50/50 |
# |   4   |  721  |   0.10%   | 49 days |
# |   7   |  600  |   0.08%   | 72 hours |
# |   9   |  474  |   0.06%   | 90 minutes |
# |   6   |  380  |   0.05%   | 6 days |
# |   8   |  379  |   0.05%   | 8th day |
# |   '   |  372  |   0.05%   | 'til death do us part |
# |   #   |  345  |   0.05%   | #vanlife |
# |   à   |  297  |   0.04%   | à fleur de peau |
# |   é   |  285  |   0.04%   | électre |
# |   .   |  280  |   0.04%   | ...y mañana serán hombres |
# |   ö   |  273  |   0.04%   | ök tudják, mi a szerelem |
# |   ç   |  245  |   0.03%   | çilginlar |
# |   ô   |  222  |   0.03%   | ôkubo hikozaemon |
# |   ¡   |  219  |   0.03%   | ¡viva méxico! |
# |   ¿   |  175  |   0.02%   | ¿adónde van nuestros hijos? |
# |   ü   |  161  |   0.02%   | überfahrt |
# |   á   |  155  |   0.02%   | ánima |
# |   (   |  121  |   0.02%   | (s)he |
# |   0   |  112  |   0.02%   | 0-18 or a message from the sky |
# |   ä   |  90  |   0.01%   | änkeman jarl |
# |   â   |  80  |   0.01%   | ângelo de sousa - tudo o que sou capaz |
# |   ú   |  80  |   0.01%   | útvesztö |
# |   å   |  66  |   0.01%   | ådalens poesi |
# |   î   |  59  |   0.01%   | împuscaturi pe portativ |
# |   $   |  52  |   0.01%   | $elfie shootout |
# |   è   |  32  |   0.00%   | è sbarcato un marinaio |
# |   ó   |  31  |   0.00%   | óbidos |
# |   [   |  28  |   0.00%   | [focus] |
# |   í   |  27  |   0.00%   | ídolos |
# |   ê   |  25  |   0.00%   | être ou ne pas être |
# |   û   |  21  |   0.00%   | ûmi no kyodai |
# |   ø   |  21  |   0.00%   | østersen og perlen |
# |   @   |  19  |   0.00%   | @festivbercine.ron |
# |   æ   |  18  |   0.00%   | æon flux |
# |   -   |  13  |   0.00%   | -but the flesh is weak |
# |   *   |  13  |   0.00%   | *batteries not included |
# |   »   |  8  |   0.00%   | »fata morgana« med nina og frederik |
# |   «   |  7  |   0.00%   | «erra» |
# |   +   |  7  |   0.00%   | + (amas) |
# |   õ   |  6  |   0.00%   | õnnelind flamingo |
# |   §   |  5  |   0.00%   | § 51 stgb |
# |   ñ   |  5  |   0.00%   | ñam ñam |
# |   ?   |  5  |   0.00%   | ???? movie |
# |   :   |  5  |   0.00%   | :03 from gold |
# |   &   |  5  |   0.00%   | & - là il cielo e la terra si univano, là le stagioni si ricongiungevano, là il vento e la pioggia si univano |
# |   "   |  4  |   0.00%   | "giliap" |
# |   ì   |  4  |   0.00%   | ìjé love |
# |   _   |  4  |   0.00%   | _titans |
# |   /   |  3  |   0.00%   | /afk: away from keyboard |
# |   ò   |  2  |   0.00%   | òrain: das geheimnis um beethovens schottische lieder |
# |   <   |  2  |   0.00%   | <3 me (heart me) |
# |   >   |  2  |   0.00%   | >g< wie gelsenkirchen - eine stadt sprengt ihre vergangenheit |
# |   ¥   |  2  |   0.00%   | ¥$ vultures rave miami wynwood marketplace 12 12 12 |
# |   £   |  2  |   0.00%   | £1,000 reward |
# |   ;   |  2  |   0.00%   | ;igy6 tributes and memorials |
# |   ë   |  1  |   0.00%   | ëndra e skercos |
# |   =   |  1  |   0.00%   | =love today is your trigger the movie |
# |   ½   |  1  |   0.00%   | ½ revolution |
# |   姆   |  1  |   0.00%   | 姆兰河那边 |
# |   þ   |  1  |   0.00%   | þegiðu og syntu |
# |   а   |  1  |   0.00%   | а winter's night dream |
# |   )   |  1  |   0.00%   | ) ( |
# |   ż   |  1  |   0.00%   | żwirko and wigura. 15 days of glory |
# |   |   |  1  |   0.00%   | || the ballsvile booklet 2022 || ballsvile productions || |
# |   !   |  1  |   0.00%   | !women art revolution |

