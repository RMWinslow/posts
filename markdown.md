---
title: Markdown Kitchen Sink
nav_exclude: true
search_exclude: true
---


# Markdown Kitchen Sink

## Header 2

### Header 3

#### Header 4

##### Header 5

###### Header 6

This is a paragraph. 
This is a paragraph. 
This is a paragraph. 
This is a paragraph. 
This is a paragraph. 
This is a paragraph. 
This is a paragraph. 
This is a paragraph. ~~The world is flat.~~ We now know that the world is on the curved back of a turtle.

<aside markdown="block">
This is an aside element made using html tags, **with markdown="block"**
</aside>

[See here for list of syntax](https://www.markdownguide.org/extended-syntax/#footnotes)



----------------
----------------

----------------

## Tables

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

### Alignment

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |


### Big table:

| Syntax      | Description | Syntax      | Description | Syntax      | Description | Syntax      | Description | Syntax      | Description | Syntax      | Description | Syntax      | Description |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |:-----------:| ----------- | ----------- |:----------- | ----------- | -----------:| ----------- |
| Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       |
| Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        |
| Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       | Header      | Title       |
| Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        | Paragraph   | Text        |


<aside>
This is an aside element made using html tags, **without markdown="block"**
</aside>


### Code blocks

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```


```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

<pre>
This
    is a pre
        block
u
s    h
i     t
n      m
g       l 
</pre>


<code>
This
    is a pre
        block
u
s    h
i     t
n      m
g       l 
</code>

Here is some `inline code`



## Footnotes

Here's a simple footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.

    `{ my code }`

    Add as many paragraphs as you like.


## Lists

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

- [x] Write the press release
- [ ] Update the website
    - [ ] bah bah bah
- [ ] Contact the media

Nested lists:

- list 
- list 
- list
  - list
    - [x] post dog
  - list
    - list
      - list
          - list
      - list
    - list
    - list
        1. list
        2. list
        3. list
    1. list
    2. list
       1. list
    3. list

1. list
2. list
    - list
3. list
4. list
5. list
6. list








## Links

http://www.example.com

`http://www.example.com`

[link with text](http://www.example.com)













## Uncommon Features

I need to highlight these ==very important words==.

I need to highlight these <mark>very important words</mark>.

H~2~O

H<sub>2</sub>O

X^2^

X<sup>2</sup>




### Mermaid Diagrams

The following code is displayed as a diagram only when a `mermaid` key supplied in `_config.yml`.

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


### Latex

I use [KaTeX](https://katex.org/docs/supported.html)

Here is some inline math $\beta^2+\sum_i n_i + \frac{a}{b}$
Wow! So neat!

Here is a display equation

$$\beta^2+\sum_i n_i + \frac{a}{b}$$

Two more, back to back

$$\beta^2+\sum_i n_i + \frac{a}{b}$$

$$\beta^2+\sum_i n_i + \frac{a}{b}$$

One equation with a linebreak using `\\`

$$\beta^2+\sum_i n_i + \frac{a}{b}\\
\beta^2+\sum_i n_i + \frac{a}{b}$$


Some aligned environments

$$
\begin{align}
   a&=b+c \\
   d+e&=f
\end{align}
$$

$$
\begin{align*}
   a&=b+c \\
   d+e&=f
\end{align*}
$$

$$
\begin{CD}
   A @>a>> B \\
@VbVV @AAcA \\
   C @= D
\end{CD}
$$








