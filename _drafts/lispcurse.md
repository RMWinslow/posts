---
layout: post
title: The Lisp Curse and AI Tooling
subtitle: When building is cheaper than adopting, ecosystems fragment.
parent: Robots
date: 2026-04-06
toc: true
---

<!--
AI NOTES

## Primary Sources

### The Lisp Curse — Rudolf Winestock (2011)
http://www.winestockwebdesign.com/Essays/Lisp_Curse.html

Central claim: "Lisp is so powerful that problems which are technical issues in
other programming languages are social issues in Lisp."

The thought experiment: adding OO to Scheme is a sophomore homework assignment;
adding OO to C requires Bjarne Stroustrup. Because Scheme makes it easy, many
individual hackers did it, producing a warehouse inventory of incompatible OO
packages. Because C makes it hard, only two serious attempts (C++ and Objective-C)
gained traction — which meant the question was already answered for any given
platform, so documentation, IDE support, and library compatibility followed.

Quotes Mark Tarver (The Bipolar Lisp Programmer): "Lisp allows you to just chuck
things off so easily... each person had implemented his own solution and it worked
for him so that was fine." Lone-wolf projects solve 80% of the problem — a
different 80% in each case. Poorly documented, not portable, abandoned when the
maintainer's real life intrudes.

Tarver also built Qi, a Lisp dialect implementing most of Haskell's and OCaml's
features in under 10,000 lines of macros. One man did what took teams of academics
for Haskell. Winestock's "exercise for the reader": if Lisp and Haskell rivalry
develops, every second Lisp hacker rolls their own lazy evaluation / type
inference / pattern matching. Endgame: "A random old-time Lisp hacker's collection
of macros will add up to an undocumented, unportable, bug-ridden implementation
of 80% of Haskell because Lisp is more powerful than Haskell."

Key structural point: "secondary and tertiary effects matter." Technology affects
social behavior, which loops back to affect technology. Lisp's power encourages
independence to the point of bloody-mindedness. This independence produced the
Lisp Machines but now prevents any "Lisp OS" project from reaching critical mass.

Also: the free Lisp dev environment problem. Building a Smalltalk-quality IDE
would require large-scale cooperation among "the kind of people who become Lisp
hackers." Every project has friction; the countervailing force ("we must all hang
together") is weakened because one can always start one's own project. Individual
hackers "hack Emacs to get something that's good enough." The Lisp Curse is the
ally of Worse Is Better.

Final line: "The expressive power of Lisp has drawbacks. There is no such thing
as a free lunch."

Winestock himself links to the c2 AI Winter page in the opening paragraph.

### Beating the Averages — Paul Graham (2001/2003)
http://www.paulgraham.com/avg.html

Graham's argument is about Lisp as competitive advantage, not about fragmentation.
At Viaweb (1995), they chose Lisp for server-side software because rapid
development mattered and server-based apps meant you could use any language.
Result: they could duplicate a competitor's newly announced feature within a day
or two. "It must have seemed to our competitors that we had some kind of secret
weapon."

The Blub Paradox: a programmer using a mid-power language looks down and sees
languages obviously less powerful (missing features they use), but looks up and
sees only "weird languages" — can't recognize what they're missing. "By induction,
the only programmers in a position to see all the differences in power between the
various languages are those who understand the most powerful one."

Graham kept Lisp secret as a competitive advantage: "In business, there is nothing
more valuable than a technical advantage your competitors don't understand."

Relevance to the post: Graham describes the individual benefit of high
expressiveness (speed, competitive edge). Winestock describes the collective cost
(fragmentation, no ecosystem). Same coin, two sides. Graham even notes that Lisp's
obscurity is an advantage — which is exactly the dynamic that prevents
standardization.

### AI Winter — c2 wiki (Ward Cunningham's wiki)
https://wiki.c2.com/?AiWinter

Term coined by Richard Gabriel for the crash (~1990-94) of the 1980s AI/Lisp
enthusiasm boom. Described as a specific case of "HypeWinter — what happens to a
good idea when it's hyped beyond all recognition, after the hype."

Key quote from Duane Rettig (comp.lang.lisp): Lisp companies rode the AI wave in
the early 80s when corporations poured billions into AI hype promising thinking
machines in 10 years. When promises proved harder than thought, AI crashed and
Lisp crashed with it due to association. "Some high-level managers who were burned
by the AI hype actually kill any project with either the name AI or Lisp in it."
Successful AI branches (speech recognition, expert systems) distanced themselves
from the name. Some came back to Lisp quietly — both because the "L word" was a
marketing negative, and because it became a competitive advantage not to mention
how their time-to-market was so quick.

Also described as "an example of TightlyCoupledReputation."

## Secondary Sources

### Hacker News discussion of The Lisp Curse
https://news.ycombinator.com/item?id=14480157

### "Perl can escape the Lisp Curse" — Mark Gardner (2021)
https://phoenixtrap.com/2021/06/22/perl-lisp-curse/

### The Bipolar Lisp Programmer — Mark Tarver
http://www.lambdassociates.org/blog/bipolar.htm
(Quoted extensively in Winestock's essay. The "it works for me" attitude.)

## Current Hook

### Andrej Karpathy tweet / AI knowledge management hype (2026)
Karpathy tweeted about building a custom Obsidian-integrated wiki with AI and
hoping someone would productize it. This prompted an explosion of AI knowledge
management systems — many people independently building bespoke solutions.
TODO: find and link the specific tweet.

## Possible Angles

### Coase / theory of the firm
When transaction costs of building drop below transaction costs of adopting,
markets fragment instead of consolidating. The Coasean boundary of the firm
shifts: it becomes cheaper to "make" than to "buy" (or adapt), so no one buys.

### AI as the new Lisp (in terms of expressiveness)
AI coding tools give every developer Lisp-level (or higher) expressiveness
regardless of their language. The 80%-different-80% problem now applies to entire
applications, not just libraries. The Karpathy tweet is the "warehouse inventory
list of object-oriented packages for Scheme" but for knowledge management tools.

### The window for network effects
When building cost drops to near-zero, the window for capturing network effects
shrinks to near-zero. By the time you could ship a polished product, the market
is already a thousand bespoke solutions.
-->
