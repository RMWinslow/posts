---
title: Home
nav_exclude: true
---

# Robert Winslow's Not-quite-a-blog

Welcome!

These blogposts are informal, non-rigorous, and often incomplete.

With that warning out of the way, 
Here are a few posts I'm fond of:
- [Astro Symbols: Symbols for astronomical objects, both ancient and modern.](./nature/astrosymbols)
- [Isomorphic Keyboards: Musical note layouts where relative physical position matches relative pitch.](./art/isomorphic)
- [Doctors and Lords: A Bugfix for the English Language](./language/lord)


The full list of posts can be found in the navigation bar, 
which is to the left on desktop
and under the hamburger menu on mobile.



<!--

The following site index works, but doesn't look great, and there are some posts I hid by changing parent to hidden instead of nav_excluding.
I mean, I guess the latter is something to fix in those individual pages, not something to account for here.
Also, not all posts have dates, so the date sorting is a bit buggy. Would also need to go through and add dates.


<ul>
{%- assign posts = site.pages   |   where:"layout", "post"   |   sort:"title" -%}
{% for post in posts %}
{%- if post.nav_exclude != true -%}
<li>
    <b><a href="{{ post_page.url | absolute_url }}">{{ post.title }}</a></b>
    {% if post.subtitle %}{{ post.subtitle }}{% endif %}
</li>
{% endif %}
{% endfor %}
</ul>


---



I'm not sure whether this counts as a blog, 
since the posts are non-chronological and organized into groups,


[Click here to return to my main website.]

I may want to migrate the posts to a more bloggish template at some point, but this will do for now.
-->




## All Posts, Chronologically:

<ul>
{%- assign post_pages = site.pages | where:"layout", "post" | sort:"date" | reverse -%}
{% for post_page in post_pages %}
{%- if post_page.nav_exclude != true and post_page.date -%}
<li>
    <b><a href="{{ post_page.url | absolute_url }}">{{ post_page.title }}</a></b>
    <small style="display: inline-block;"><i>{{ post_page.date | date: "%Y-%m-%d" }}</i></small>
    {% if post_page.subtitle %}{{ post_page.subtitle }}{% endif %}
</li>
{% endif %}
{% endfor %}
</ul>
