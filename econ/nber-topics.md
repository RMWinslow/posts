---
title: Economist Research Topic Transitions
parent: Econ
layout: post
date: 2026-09-17
modified: 2026-09-22
---


The following is a messy visualization of researcher movement between topics.


<!--
<div class="full-width">
<iframe src="./nber-topics/nber_topic_transitions.html" title="NBER research topic transitions" width="100%" height="750" scrolling="no" style="border: 0;"></iframe>
</div>
-->

<div class="full-width">
<iframe src="./nber-topics/nber_topic_excess_transitions.html" title="NBER research topic excess transitions" width="100%" height="750" scrolling="no" style="border: 0;"></iframe>
</div>




I took the [database of NBER working papers](https://www.nber.org/research/data/nber-working-papers-and-chapters-metadata) from the start of 2000 to April 3, 2025 (which is when I downloaded the files to make this visualization). These files have titles, authors, abstracts, and JEL topic codes for each paper.

For each author I took the set of JEL topic codes for all the papers they authored in the dataset, and I found the first appearance date for each code for that author.
if the first appearance for one code (eg. G12) strictly precedes the first appearance of another (eg. G23) then I count that as a "transition" between the codes (eg. G12->G23) for that author. 


<!-- TODO: Rework the post to include BOTH graphs...
The graph above then displays the likelihood of a "transition" from one topic to another,
measured as 
the number of transitions
divided by the number of authors with a paper in the upstream topic.
For an edge to be shown in the graph, the upstream topic must have at least 10 authors,
and at least 25% of those authors must have a "transition" to the downstream topic. 
-->
<!-- [^originalversion]: [The prototype](./nber-topics/nber_topic_transitions.html) just divided the number of transitions by the number of authors with a paper in the upstream topic. But using *that* metric for the threshold biases the upstream topics to only have a few authors. -->
<!--Q58 is an apparent exception.-->

The graph above then displays topic pairs where there's an unexpectedly high number of these "transitions".
The "expected" number of transitions between A and B is 
the number of transitions *from A* times
the number of transitions *to B*,
divided by the total number of edges in the graph.
For an edge to be shown in the graph, the number of actual transitions must be at least 25 more than the "expected" number of transitions for that pair of topics.


The original research question I wanted to explore was whether economists tend to specialize in more niche topics over the course of their career or if they tend to generalize instead.
There are some obvious shortcomings for this particular data source - 
using only NBER working papers with an arbitrary date cutoff means I'm not actually observing a the full history for each researcher - which could be fixed by scraping a larger database of papers. 
But I put this idea into the freezer because I'm doubtful, when interpreted across various publication sources, that the specificity of JEL codes reflect the specificity of the research rather than the preferences of journal editors for granular categorization.
I'd need some sort of heirarchical categorization based on the content of the papers themselves.



<!-- 
TODO: Some sort of little note about Aghion and Harris' work, and why this is a blog post instead of a paper.
About a year later, 
I pulled this idea off the shelf to see if I  -->

Ah well. It's still a fun visualization to play around with. 

