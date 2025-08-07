#%%
from collections import Counter

word_counts = Counter()

with open("gutenberg counts.txt") as f:
    for line in f:
        count,word = line.split()
        word = word.lower()
        if word.startswith("x"):
            word_counts[word] = int(count)

for word,count in word_counts.most_common():
    print(f"{word} {count}")

#%%
with open("x 50 enwiki-2023-04-13.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        if "included" in line or "Included" in line:
            print(line)

