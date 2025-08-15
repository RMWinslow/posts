---
title: Prefix-suffix Bicliques
subtitle: How many word fragments can we find that all fit together?
layout: post
parent: Language
date: 2025-08-12
---

<!-- See word shapes folder for related files-->

I saw this toy at the store:

![spinning spelling toy](https://m.media-amazon.com/images/I/71l-ccB7zyL._AC_SL1500_.jpg)

It has five prefixes and five suffixes such that each pair forms a valid word.

| prefix | suffix |
|:-:|:-:|
| p- | -ad |
| b- | -at |
| m- | -ail |
| h- | -ay |
| r- | -ug |

Can we do better than 5 of each? I ran a quick search on a [dictionary-consensus wordlist](http://wordlist.aspell.net/12dicts/), and the best[^wordcombos] I could find was a 7x7:

[^wordcombos]: By "best", I mean largest NxN set. If we just wanted to know the largest NxM set period, then we would look at every word that ends in "s". 

| Prefix | Suffix |
|:------:|:------:|
| b-     | -ad    |
| d-     | -ang   |
| f-     | -ate   |
| g-     | -ay    |
| p-     | -ear   |
| r-     | -ill   |
| s-     | -un    |

I actually found a few dozen 7x7 sets. The one above seems well-suited to an actual toy, but the first one I found was the following, which would make for a beautifully stupid children's toy:

| Prefix         | Suffix     |
|:--------------:|:----------:|
| materia-       | -l         |
| rea-           | -listic    |
| rationa-       | -lize      |
| natura-        | -list      |
| socia-         | -lization  |
| nationa-       | -lly       |
| individua-     | -lism      |

<!-- | Prefix         | Suffix     |
|:--------------:|:----------:|
| forma-         | -l         |
| individua-     | -lism      |
| nationa-       | -list      |
| neutra-        | -lity      |
| rationa-       | -lization  |
| rea-           | -lize      |
| sentimenta-    | -lly       | -->

There's also a 7x8 set, but it has a few questionable word-pairs:

| Prefix | Suffix |
|:------:|:------:|
| b-     | -ad    |
| c-     | -ake   |
| h-     | -ash   |
| l-     | -ay    |
| m-     | -ob    |
| r-     | -ock   |
| s-     | -oot   |
|        | -ow    |

<!-- 
| Prefix | Suffix |
|:------:|:------:|
| b-     | -ake   |
| c-     | -are   |
| fl-    | -ash   |
| h-     | -at    |
| m-     | -ay    |
| r-     | -ock   |
| st-    | -ow    |
|        | -uff   | -->


And if we're willing to use medical terminology, then here's a 10x10:

| Prefix      | Suffix    |
|:-----------:|:---------:|
| aden-       | -algia    |
| chondr-     | -itis     |
| desm-       | -odynia   |
| encephal-   | -ography  |
| hepat-      | -oid      |
| my-         | -ology    |
| neur-       | -oma      |
| odont-      | -opathy   |
| oste-       | -osis     |
| splen-      | -otomy    |


## Other Musings


### Can We expand on the original toy's wordlist?

Yes and no.
There are no prefixes we could add that work with all five of the original suffixes 
`-ad,-at,-ail,-ay,-ug`.

However, there *are* another 10 additional suffixes that work with `p-, b-, m-, h-, r-`:  

<!-- `-ad, -ail, -are, -at, -ate, -atter, -ay, -ill, -ock, -od, -ole, -ound, -uff, -ug, -ush` -->
`-are, -ate, -atter, -ill, -ock, -od, -ole, -ound, -uff, -ush`

<!-- , in the sense that there's no 6x6 word set which contains the original 5x5. -->



### Can we make a toy with only 3-letter words?

The original toy has one two-letter suffix, `-ail`, which means some of the resulting words are four letters long.
that's a bit unsatisfying.
If they replaced `-ail` with `-od`, then the toy would be more symmetric.
Though "bod" and "mod" are admittedly questionable as words go...



<!-- 6,7,['b-', 'c-', 'h-', 'm-', 'r-', 's-'],['-ad', '-at', '-ay', '-ob', '-od', '-ow', '-um'] -->
<!-- ['b-', 'c-', 'h-', 'm-', 's-'],['-ad', '-at', '-ay', '-ob', '-ow',] -->
<!--rob is a bit questionable...-->

Here's an alternate set, which doesn't have that problem, but does have a couple of its own odd or archaic words:

| Prefix | Suffix |
|:------:|:------:|
| d-     | -ad    |
| h-     | -ay    |
| l-     | -id    |
| m-     | -ot    |
| r-     | -ug    |


Here's one with a couple "kid-friendly" naughty words - "pee" and "wee" 
which would paradoxically make for an *excellent* toy but also one that a toy company would be averse to selling.

| Prefix | Suffix |
|:------:|:------:|
| b-     | -ad    |
| l-     | -ay    |
| p-     | -ee    |
| s-     | -et    |
| w-     | -it    |



<!--"mid" is a bit mid-->


<!-- | Prefix | Suffix |
|:------:|:------:|
| b-     | -ad    |
| c-     | -at    |
| h-     | -ay    |
| m-     | -ob    |
| s-     | -ow    | -->

<!-- 
| Prefix | Suffix |
|:------:|:------:|
| c-     | -ad    |
| h-     | -ap    |
| m-     | -at    |
| p-     | -aw    |
| r-     | -ay    |
| s-     | -ot    |

... "mot", "hap"... 
yeah, I understand why they added the extra letter.[^otheroption]

[^otheroption]: I'm completely ignoring the sets with both `c-` and `-um`. Those are right out.


['ca-', 'co-', 'ma-', 'pa-', 'ra-', 'so-'],['-d', '-n', '-p', '-t', '-w', '-y']
*("pap" is admittedly a bit questionable)*

And here's a  -->

And here's an alternative with 2-letter prefixes and 1-letter suffixes:

| Prefix | Suffix |
|:------:|:------:|
| ca-    | -d     |
| co-    | -n     |
| ma-    | -p     |
| ra-    | -w     |
| so-    | -y     |
<!-- | pa-    | -t     | -->


Still not perfect. I understand what the toy designers resorted to `-ail`.








### Can we make a toy with only 2-letter words?

No.

You can get a 3x4 set with two letter words if you're willing to accept exclamations:
`ah, am, an, ax, eh, em, en, ex, oh, om, on, ox`

But there's no 5x5 set.





### Stop trying to make a better toy. Let's make a worse one.

That result up above with words like "materia-listic" was pretty silly.
I wonder how big I could force the words to be in a toy like this...

Turning to the wikipedia corpus (all words used on wikipedia), 
I found a 5x5 set where the minimum word length is 17 and the average is 18.8.
But this cheats by using both British and American spellings.

| Prefix           | Suffix       |
|-----------------:|:-------------|
| anthropomorph-   | -izations    |
| institutional-   | -isation     |
| mischaracter-    | -ization     |
| reconceptual-    | -ising       |
| recontextual-    | -izing       |

Here's one that doesn't rely on variant spellings.
The minimum word length is only 16, but the average is 19.2.
And wow! What a terrible list of words!

| Prefix           | Suffix       |
|-----------------:|:-------------|
| otorhinolaryng-  | -ological    |
| psychopharmac-   | -ologists    |
| electrophysi-    | -ologist     |
| paleoanthrop-    | -ologic      |
| dendrochron-     | -ology       |



<!-- 
New biggest minimum word length: 12
['collabora-', 'communica-', 'demonstra-', 'investiga-', 'distribu-'] ['-tions', '-ting', '-tive', '-tors', '-tion'] 8 4
New biggest average length: 6.5
['collabora-', 'communica-', 'demonstra-', 'investiga-', 'distribu-'] ['-tions', '-ting', '-tive', '-tors', '-tion'] 8 4 -->


