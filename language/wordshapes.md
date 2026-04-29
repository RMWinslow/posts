---
title: Word Shapes
subtitle: aka Letter-Adjacency Graphs.
layout: post
parent: Language
date: 2023-06-16
modified: 2026-04-28
toc: False
permalink: wordshapes
redirect_from: 
  - /language/wordshapes.html
  - /language/wordshapes
---

FIRE is a linear word. 
AQUA is a triangle.
<!-- It loops back around to `A`. -->
AUTOMATA is shaped like a house.

![FIRE](./wordshapes/img/words/FIRE.webp) ![AQUA](./wordshapes/img/words/AQUA.webp) ![AUTOMATA](./wordshapes/img/words/AUTOMATA.webp)

Define a word's "shape" as the graph[^graphtheory] where two letters are connected iff they're adjacent in the word.




## The Smallest Missing Shape

For five or fewer unique letters, 
there was only one graph where I couldn't find a word.
It's this one:


![SPOOKY PENTAGRAM](wordshapes/img/K5.webp)

The missing graph is K5, aka the *pentatope graph*, aka the *spooky pentagram*.[^subgraphk5]

[^subgraphk5]: I also checked the larger words and none of them seem to contain this shape as a subgraph. If we allow for abitrary two-word phrases, then we can find examples like "incant tactician" and "restart easters".


There is a caveat. 
The smaller K4 graph only has one associated word, and that's GENSENGS,
which is the plural of an alternate spelling of "ginseng".
That's... iffy, but [it *is* in the Scrabble dictionary](https://scrabble.merriam.com/finder/genseng). 


![GENSENGS](wordshapes/img/words/GENSENGS.webp)

For less tenuous K4 matches from other languages, 
Spanish has TINIENTE and Portuguese has LEALDADE.



Besides K4 and K5, I was able to find entirely sensible words 
for every one of the 30 possible[^simpleconnected] graphs of size 5 or smaller.

[^simpleconnected]: unique, simple, connected





## Table of Word Shapes

Here are my favorite words with each shape:

![Table of unique graphs with example words overlaid.](./wordshapes/img/wordgraphs.png)


And here's a tabular version of the same:

<style>
    main table img {
        max-width: 150px;
        max-height: 80px;
    }
    main table tr:nth-child(3){
        padding:0
    }
</style>

| Graph | Example Word | Visualization |
|:--|:--|:--|
| singleton graph | i | ![word graph for i](wordshapes/img/flatwords/i.webp) |
| 2-path | to | ![word graph for to](wordshapes/img/flatwords/to.webp) |
| 3-path | air | ![word graph for air](wordshapes/img/flatwords/air.webp) |
| K3 (triangle) | aqua | ![word graph for aqua](wordshapes/img/flatwords/aqua.webp) |
| paw graph | catch | ![word graph for catch](wordshapes/img/flatwords/catch.webp) |
| 4-path | fire | ![word graph for fire](wordshapes/img/flatwords/fire.webp) |
| diamond graph | miasma | ![word graph for miasma](wordshapes/img/flatwords/miasma.webp) |
| square graph | anima | ![word graph for anima](wordshapes/img/flatwords/anima.webp) |
| K4 (tetrahedron) | gensengs | ![word graph for gensengs](wordshapes/img/flatwords/gensengs.webp) |
| banner graph | absorb | ![word graph for absorb](wordshapes/img/flatwords/absorb.webp) |
| fork graph | elixir | ![word graph for elixir](wordshapes/img/flatwords/elixir.webp) |
| (3,2)-tadpole graph | propel | ![word graph for propel](wordshapes/img/flatwords/propel.webp) |
| bull graph | alcohol | ![word graph for alcohol](wordshapes/img/flatwords/alcohol.webp) |
| kite graph | calculus | ![word graph for calculus](wordshapes/img/flatwords/calculus.webp) |
| butterfly graph | tempest | ![word graph for tempest](wordshapes/img/flatwords/tempest.webp) |
| (4,1)-lollipop graph | torturous | ![word graph for torturous](wordshapes/img/flatwords/torturous.webp) |
| cricket graph | aether | ![word graph for aether](wordshapes/img/flatwords/aether.webp) |
| 5-path | earth | ![word graph for earth](wordshapes/img/flatwords/earth.webp) |
| dart graph | instant | ![word graph for instant](wordshapes/img/flatwords/instant.webp) |
| 5-star | kabbalah | ![word graph for kabbalah](wordshapes/img/flatwords/kabbalah.webp) |
| gem graph | seascape | ![word graph for seascape](wordshapes/img/flatwords/seascape.webp) |
| (2,3)-complete bipartite | loyalty | ![word graph for loyalty](wordshapes/img/flatwords/loyalty.webp) |
| house graph | automata | ![word graph for automata](wordshapes/img/flatwords/automata.webp) |
| (1,1,3)-complete tripartite | attractant | ![word graph for attractant](wordshapes/img/flatwords/attractant.webp) |
| house X graph | lanolin | ![word graph for lanolin](wordshapes/img/flatwords/lanolin.webp) |
| 5-cycle (pentagon) | exhume | ![word graph for exhume](wordshapes/img/flatwords/exhume.webp) |
| 3-dipyramidal | intensities | ![word graph for intensities](wordshapes/img/flatwords/intensities.webp) |
| 5-graph 31 | nurturant | ![word graph for nurturant](wordshapes/img/flatwords/nurturant.webp) |
| 5-wheel | milliosmols | ![word graph for milliosmols](wordshapes/img/flatwords/milliosmols.webp) |
| K5 (pentatope) | ??? | ![](wordshapes/img/K5.webp) |

Names are taken from this page on [Biconnected Graphs from Wolfram Mathworld](https://mathworld.wolfram.com/BiconnectedGraph.html).



### 6 Nodes

TODO

<!-- Also TODO: word pairs -->


## Prior Art


[This video by John Turner](https://www.youtube.com/watch?v=4uFahk0cuZU)
had a fun idea:
Looking at which words are 'shaped' the same. 
One of the ways he defines a word's shape is via its graph of letter adjacencies.
For example, "baboon" and "refers" have the same graph shape
because the network of connections between adjacent letters is similar.

[^graphtheory]: "Graph" as in "[graph theory](https://www.britannica.com/topic/graph-theory)", the study of networks and connections. To get a word's letter-adjacency graph: Each letter is a vertex. There is an edge connecting two letters if they show up next to each other in the word. The graphs are [simple graphs](https://mathworld.wolfram.com/SimpleGraph.html), meaning we don't connect a letter to itself (in words like "moon"), nor do we add extra edges when the same adjacency happens multiple times (in words like "donor").
<!--https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_and_Graph_Theory_(Guichard)/05%3A_Graph_Theory/5.01%3A_The_Basics_of_Graph_Theory-->



![Editted screenshot of John Turner's video, showing how 'baboon' and 'refers' have the same graph.](wordshapes/letterWheelExample.png)

Unfortunately, despite using a graphing library called [Scott](https://github.com/theplatypus/scott) to compute canonical representations of each word's graph, 
what Turner has calculated doesn't seem to *actually* be (just) about graph isomorphism.
It also takes into account the position of letters around the "letter wheel".
I found this unsatisfying.

Looking at just the networks of letter adjacency, "baboon" should be similar not just to words like 
"refers", 
but also to words like "cats" and "wooly".

<!-- 
This post *partially* answers that question
using the `enable1` dictionary of words from [this Github Repo](https://github.com/dolph/dictionary)
-->


