
## Robert Winslow's Not-quite-a-blog


Welcome!

These blogposts are informal, non-rigorous, and often incomplete.

With that warning out of the way, 
Here are a few posts I'm fond of:
- [Astro Symbols: Symbols for astronomical objects, both ancient and modern.](./nature/astrosymbols)
- [Isomorphic Keyboards: Musical note layouts where relative physical position matches relative pitch.](./art/isomorphic)
- [Doctors and Lords: A Bugfix for the English Language](./language/lord)


---

<ul>
{%- assign posts = site.pages   |   where:"layout", "post"   |   sort:"title" -%}
{% for post in posts %}
{%- if post.nav_exclude != true -%}
<li>
    <b><a href="{{ game_page.url | absolute_url }}">{{ post.title }}</a></b>
    {% if post.subtitle %}{{ post.subtitle }}{% endif %}
</li>
{% endif %}
{% endfor %}
</ul>

---

<ul>
{%- assign posts = site.pages   |   where:"layout", "post"   |   sort:"date" -%}
{% for post in posts %}
{%- if post.nav_exclude != true -%}
<li>
    <b><a href="{{ game_page.url | absolute_url }}">{{ post.title }}</a></b>
    {% if post.subtitle %}{{ post.subtitle }}{% endif %}
</li>
{% endif %}
{% endfor %}
</ul>

---

<ul>
{%- assign posts = site.pages   |   where:"layout", "post"   |   sort:"last_modified_date" -%}
{% for post in posts %}
{%- if post.nav_exclude != true -%}
<li>
    <b><a href="{{ game_page.url | absolute_url }}">{{ post.title }}</a></b>
    {% if post.subtitle %}{{ post.subtitle }}{% endif %}
</li>
{% endif %}
{% endfor %}
</ul>




<!--
---



I'm not sure whether this counts as a blog, 
since the posts are non-chronological and organized into groups,


[Click here to return to my main website.]

I may want to migrate the posts to a more bloggish template at some point, but this will do for now.
-->

