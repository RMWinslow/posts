---
layout: post
title: AI SEO
parent: Robots
date: 2026-04-03
---

I've actually gotten a few emails about obscure card games because I have the only AI-legible transcriptions of the rules for those games on the internet, and so the robot cites me as the authoritative source. Ideally I'd like to set up my personal website so that people encounter me through less trivial AI queries.

I can't speak to how all AI systems interface with the web, but I think I have a pretty good idea of how Claude Code does it.

Here's how I *think* Claude Code uses the web:

1. It uses the Websearch tool to get a list of pages.
    1. Claude sends a search query to Anthropic's servers.
    2. The server passes the request along to a standard search engine. I think they used to use Google, but now use Brave.
    3. The server gives Claude the list of titles, URLs, and page summary snippets. (Basically the exact same thing you get when you use Google)
2. The LLM chooses which pages to view based only on that info.
3. It then uses the Webfetch tool to get a **summary** of the page.
    1. Claude gives the tool a url and a question.
    2. The tool gets the html, and converts it to markdown (markdown is just text with very minimal formatting markers).
    3. The markdown text is given to a much simpler LLM, along with your question and instructions to return a short response without exact quotes.
    4. Claude then sees the short summary answer and pretends that it actually looked at the source page. It did not, and will admit this if pressed.


This is partially based on the strange problems I've encountered when trying to use it for research, partially based on the Anthropic Documentation (which is annoyingly riddled with incorrect statements), and partially based on some discussion surrounding a recent leak of some of the Claude Code source code.

This is the most important thing to understand: The Claude that talks to the user will never actually look at a webpage. They won't let it. If your page has fancy data structure hooks, it won't see them. If your page has too much content, so This has been incredibly annoying for my attempts to use AIs are research assistants, but these safeguards are in place for a reason. Microsoft's Bing chatbot was the first to be given internet access, and completely lost its marbles when given direct access to the web. I built my own scripting tool to access web content, hoping to improve Claude's citation practices, but when I forced Claude to use my tool, it immediately lost its marbles.

They don't let the robot actually look at the internet directly because to it, all text is gospel truth. When Microsoft first let the Bing AI directly view web results, it completely lost its marbles.

I haven't gotten around to trying to be serious about that task, however. That's not the kind of marketing I need to worry about in my line of work. All I've really done so far was ask a few AI agents to look at my website and give advice to make it more LLM-friendly. They told me a bunch of stuff I could do, but then I asked them to "Be honest. Would any of that have actually helped you interface with my website?" and the robot responded "No, not at all." The current

So if you really want your website to be cited by AI, my conjecture is this:

- **Step one is traditional SEO.** Your website has to actually show up in the search results because the robots are also using it.
- **Step two: Keep it simple.** Simple text served as part of the html. If you rely on javascript or database queries to render your text, the robot might have trouble reading it, and then it will give up and move on. If a single page has too much content, the AI won't read it - at best, it will get a summary from a much simpler AI. If you want an AI to read a page, the page should be programmed to be readable by a blind man using an internet browser from 1994 (because that's basically what the robots are doing).
