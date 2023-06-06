---
title: Patterns in Consonants
description: A subset of consonant sounds which adheres to an interesting pattern.
parent: Language
layout: post
date: 2022-04-07
last_modified_date: 2023-06-05
---

This is a simplification of [some stuff](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet_chart) I've been reading about linguistics.

Vowels are noises you make by letting air freely exit your vocal tract without restriction or turbulence.
Consonants are noises you make by interfering with the air flow in some way.

Some consonants are hard to wrap your head around. [^noteaboutR]
But there are some other consonants that fit into a nice little pattern.

[^noteaboutR]: What's going on with the sound that "R" makes? All the consonant charts I've seen have it on there *somewhere*. But different charts seem to put R in different places. Is it like some sort of incomprehensible eldritch mystery sound?

<!--https://improveyouraccent.co.uk/consonant-chart/*/-->

|  | Lips | Teeth | Ridge | Velar |
|--:|:-:|:-:|:-:|:-:|
| Strong Stop | P | T | Ch* | K |
| Weak Stop | B | D | J* | G |
| Strong Fricative | F | Th or S | Sh | * |
| Weak Fricative | V | Th or Z | Zh |  |
| Nasal | M | N |  | Ng |

Columns indicate where the sound is made. 
Velar consonants are made with the back of your tongue on your soft palate.
Ridge consonants are actually called 'post-alveolar', which means you put your tongue on that ridge behind your upper teeth.
If you say "no, toe, doe", your tongue does pretty much the same thing for each word.

Rows indicate how the sound is made.
Stop consonants, also called plosives, temporally halt airflow. 
Nasal consonants redirect air through your nose.
Fricative consonants create friction in the airflow without halting it entirely.

A few notes/caveats:
* English also can have a fricative in the back of the mouth, but that's only really used in words like lo*ch* or Ba*ch*.
* The *Ch* and *J* sounds are labelled in most consonant charts as 'affricate', which is like halfway between a stop and a fricative. The airflow stops, but then the tongue lingers to cause some frication. For me *J* feels like a plain stop in many words. This might be an accent thing.
* Both the hard and soft *Th* sounds are rare outside of English. [They are very similar to S and Z](https://www.youtube.com/watch?v=0MUsVcYhERY).
* In [Dog of Wisdom](https://www.youtube.com/watch?v=D-UmfqFjpl0), the airplane dog talks almost entirely using weak stops. "Babadegada", indeed.


<!--The letter *h*, among it's many uses, can be a glottal fricative, meaning a noise you make with friction in your throat.-->

## This pattern in constructed scripts


### Korean Hangul

Korea's writing system was deliberately designed so that there is a connection between the shapes of the letters and the sounds that they make.
Much has been written about how this writing system, called Hangul, [is the most brilliant thing ever](https://en.wikipedia.org/wiki/Hangul_supremacy).

Here are some of the consonants in Hangul that fit the above pattern.

|  | Lips | Teeth  | Velar |
|--:|:-:|:-:|:-:|
| Strong Stop | ㅍ | ㅌ | ㅋ |
| Weak Stop | ㅂ | ㄷ | ㄱ |
| Nasal | ㅁ | ㄴ | ㅇ |

Note that these sounds aren't the same as English consonants. The ㄱ sound for example, is somewhere between English's *K* and *G*.


### Tolkien's Tengwar

It's sometimes joked that Tolkien invented the world of Middle Earth as an excuse to have people look at his invented languages.

Tengwar is the alphabet used by Tolkien's elves. The sounds that each character makes is dependent on the language that you are writing, but for English, the letters are usually mapped like so:[^tengwarfont]

[^tengwarfont]: The embedded Tengwar font, called "Tengwar Formal CSUR", comes from the [Free Tengwar Font Project](http://freetengwar.sourceforge.net/).

<style>
    @font-face {
        font-family: 'tengwar';
        src: url("{{site.webfontdirectory}}/tengwar/TengwarFormalCSUR.ttf");
    }
    .tengwartd {
        text-align: center;
        font-family: 'tengwar';
        font-size: large;
    }
</style>
<table>
  <thead>
    <tr>
      <th style="text-align: right"> </th>
      <th style="text-align: center">Lips</th>
      <th style="text-align: center">Teeth</th>
      <th style="text-align: center">Ridge</th>
      <th style="text-align: center">Velar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: right">Strong Stop</td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
    </tr>
    <tr>
      <td style="text-align: right">Weak Stop</td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
    </tr>
    <tr>
      <td style="text-align: right">Strong Fricative</td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
    </tr>
    <tr>
      <td style="text-align: right">Weak  Fricative</td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"> </td>
    </tr>
    <tr>
      <td style="text-align: right">Nasal</td>
      <td class="tengwartd"></td>
      <td class="tengwartd"></td>
      <td class="tengwartd"> </td>
      <td class="tengwartd"></td>
    </tr>
  </tbody>
</table>

This is only part of the [Tengwar alphabet](https://www.tecendil.com/tengwar-handbook/). 
The Dental Fricatives here are the *Th* sounds. *S* and *Z* are mapped to <span class="tengwartd"></span> and <span class="tengwartd"></span>.


In Tengwar, the vertical stem tells you how the sound is made.
The shape of the loops (direction, whether there is a bar) tells you where in the mouth the sound is made.
The loops are doubled to indicate the weak version of the sound.


### Shorthand 

In Pitman's shorthand, some consonants are distinguished by having a thicker stroke.

|  | Lips | Teeth | Ridge | Velar |
|--:|:-:|:-:|:-:|:-:|
| Strong Stop | \ | \| | / | - |
| Weak Stop | **\\** | **\|** | **/** | **-** |
| Strong Fricative | ╰ | ( or ) | ╯ |  |
| Weak Fricative | **╰** | **(** or **)** | **╯** |  |
| Nasal | ⌢ | ⌣ |  | **⌣** |

Unicode doesn't have dedicated characters for Pitman's shorthand,
(at least not yet),
so I've repurposed similar-looking characters for the table above.

<!--⏜⏝⌢⌣-->


