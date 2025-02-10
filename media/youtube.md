---
title: YouTube Channels
description: "Experimental Little In-browser Feed."
parent: Media Recommendations
grand_parent: Art and Culture
layout: post
toc: true
date: 2021-06-24
last_modified_date: 2025-01-07
permalink: /youtube
redirect_from:
  - /media/youtube
nav_exclude: true
search_exclude: true
---

This is a little javascript feed that grabs the latest video from some of my favorite YouTube channels.
In a way, this also doubles as some channel recommendations.

## Why?

Some channels upload every day. Some upload once a year.
In Youtube's standard subcription feed, the videos from the former completely drown out the videos from the latter.
This is especially problematic because those rare uploads are often the ones I want to watch the most.

A better model for a subscription feed is to display the *latest* upload from each channel.
The [FreeTube](https://freetubeapp.io/) on desktop does something like this,
but I wanted a version that I could easily pull up on my phone.

I've set the feed to update once a week via github actions.
An added "benefit" of this setup is that there's no skinner-box incentive to refresh the page for updates.




## Videos



<!--

Alas, this is currently non-functional due to a lack of working CORS proxy. 

If I want to access the RSS feed for a youtube channel, then I need a server to do it. 
I was previously able to simply send the request through a proxy, but none I know of are currently useable.


https://news.ycombinator.com/item?id=41325889

barely related: https://news.ycombinator.com/item?id=38622404

----------------




Youtube's recommendation algorithm is a mess, and an unsorted list of every subscription isn't great for finding stuff I want to watch, so I made a categorized list of youtube channels that I like to check occasionally.

I also find that the YouTube experience is improved by a third-party client.
I use [FreeTube](https://freetubeapp.io/) on desktop,
and [NewPipe](https://newpipe.net/) on Android.

It takes a bit to load because I have to go through a CORS proxy to grab the youtube RSS feeds using only javascript.
-->

<!--
This page has some useful info about YT thumbnail URLs:
https://internetzkidz.de/en/2021/03/youtube-thumbnail-urls-sizes-paths/

-->


<style>
  .videoBlock {
    border: 1px solid var(--bordercolor);
    min-height: 65px;
    background-color: var(--boxcolor);
    display: flex;
  }
  .videoBlock:hover {
    background-color: var(--feedbackcolor);
  }
  .videoBlock a {
    text-decoration: none !important;
    flex: 1;
  }
  .videoBlock a:visited {
    color: var(--textcolor);
  }
  .videoBlock .mainlink {
    margin-bottom: 0rem;
    margin-top: 0.5rem;
    font-size: 110%;
    font-weight: bold;
    line-height: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .videoBlock img {
    float: left;
    margin-right: 1rem;
    height: 65px;
  }
  .videoBlock .metadata {
    color: var(--textcolor);
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
</style>


<div id="youtube_feeds"></div>


<script>
const channel_groups = new Map();

fetch('https://rmwinslow.github.io/ytrss/latest_videos.json')
  .then(response => response.json())
  .then(data => {process_channels(data)
  });

function process_channels(channels) {
  // Group the channels by category.
  channels.forEach(channel => {
    if (channel_groups.has(channel.category)) {
      channel_groups.get(channel.category).push(channel);
    } else {
      channel_groups.set(channel.category, [channel]);
    }
});

// Create a header and feed for each category.
feed_div = document.getElementById('youtube_feeds');
channel_groups.forEach((category_channels, category) => { // When using forEach on a Map, parameters are value,key,map.
  // Header
  category_header = document.createElement('h2');
  category_header.textContent = category;
  feed_div.appendChild(category_header);
  // Feed
  category_feed = document.createElement('div');
  category_channels.forEach(channel => {
    category_feed.appendChild(create_video_block(channel));
  });
  feed_div.appendChild(category_feed);
});
}

function create_video_block(channel) {
video_block = document.createElement('div');
video_block.className = 'videoBlock';
video_block.innerHTML = `
<a href="https://www.youtube.com/embed/${channel.video_id}">
    <img src="https://i3.ytimg.com/vi/${channel.video_id}/mqdefault.jpg" alt="Thumbnail">
    <div class="mainlink">${channel.title}</div>
    <div class="metadata">${channel.author} - ${channel.date.slice(0, 10)}</div>
</a>
`;
return video_block;
}

</script>
  


<!--

### A Man Walks About Describing Things

(aka the Tom Scott genre)

<div id="feed_walkingMen" class="youtubeFeed"></div>

### Math

<div id="feed_math" class="youtubeFeed"></div>

### Food and Cookery

<div id="feed_food" class="youtubeFeed"></div>

### Media Commentary

<div id="feed_media" class="youtubeFeed"></div>

### Commentary on Objects

<div id="feed_tat" class="youtubeFeed"></div>

### Fans of Fans

<div id="feed_fans" class="youtubeFeed"></div>


<details>
<summary>All channels. Click to expand.</summary>
<div id="feed_combined" class="youtubeFeed"></div>
</details>







<script>
//Constants go here. If things are broken, it's likely a cors proxy issue.
//https://gist.github.com/jimmywarting/ac1be6ea0297c16c477e17f8fbe51347
//const proxyserver = 'https://corsproxy.io/?'
//const proxyserver = 'https://corsproxy.org/?' //dead?
//http://www.whateverorigin.org/ // works but just barely and not the right format.
const proxyserver = 'https://api.allorigins.win/raw?url='
// const proxyserver = 'https://everyorigin.jwvbremen.nl/get?url='
const delay_ms = 1100

const channel_groups = {
    "feed_walkingMen" : [
        'UCUMQFUkgaEE68_ujIdW2wAw', // Dime Store Adventures: Investigating local history and folklore!
        'UCBa659QWEk1AI4Tg--mrJ2A', // Tom Scott: Amazing Places
        'UCbCq5Y0WPGimG2jNXhoQxGw', // Atomic Frontier: Tom Scott's Doppelganger
        'UCbbQalJ4OaC0oQ0AqRaOJ9g', // Jay Foreman: Map Men and Unfinished London
        'UC2LVhJH_9cT2XKp0VAfsKOQ', // Tim Traveler: Uninteresting Places
        'UC4a9LfdavRlVMaSSWFdIciA', // Rob Words
        ],
    "feed_math" : [
        'UCYO_jab_esuFRV4b17AJtAw', // 3blue1brown: Beautiful theorems
        'UCoxcjq-8xIDTYp3uz647V5A', // Numberphile: Videos about numbers
        'UCSju5G2aFaWMqn-_0YBtq5A', // Stand Up Maths: More videos about numbers. Took me a while to realize it's not the same channel as Numberphile.
        'UCK8XIGR5kRidIw2fWqwyHRA', // Reducible
        'UC4zzTEL5tuIgGMvzjk1Ozbg', // Henry Segerman
        'UCSIvk78tK2TiviLQn4fSHaw', // Up and Atom
        ],
    "feed_media" : [
        'UCrTNhL_yO3tPTdQ5XgmmWjA', // red letter media: Wisconsin's finest cultural output
        'UCEOXxzW2vU0P-0THehuIIeg', // Captain D: Like a 90s childrens science show, but about digital effects
        'UC7-E5xhZBZdW-8d7V80mzfg', // Jenny Nicholson: Why does she have so many porgs?
        'UCZXAVdAplsu1tFZ9OqQhJFg', // Virtual Frog *
        'UCH_7doiCkWeq0v3ycWE5lDw', // Any Austin
        'UCRrvZqCL1YsqRA8IpXrhYQQ', // Jill Bearup
        'UC9pgQfOXRsp4UKrI8q0zjXQ', // Lindsay Beige
        ],
    "feed_food" : [
        'UC9_p50tH3WmMslWRWKnM7dQ', // Adam Ragusea
        'UCsaGKqPZnGp_7N80hcHySGQ', // Tasting history: Historically accurate recipes, along with discussion of adjacent history.
        'UCJHA_jMfCvEnv-3kRjTCQXw', // Babish: Mostly makes meme food
        'UCRIZtPl9nb9RiXc9btSTQNw', // Food Wishes: Straightforward recipe videos
        'UCJLKwTg0IaSMoq6hLHT3CAA', // Ordinary Sausage
        'UCxr2d4As312LulcajAkKJYw', // Townsends
        ],
    "feed_fans" : [
        'UC3_AWXcf2K3l9ILVuQe-XwQ', // Matthias random stuff
        'UCUXW4gT27TOaDzKFyN-1tXQ', // Major Hardware
        'UC4AkVj-qnJxNtKuz3rkq16A', // Robert Murray-Smith
        'UC1E8OmOG17VckoPviOPmkMw', // TNT Omnibus (RMS' second channel)
        'UCtM5z2gkrGRuWd0JQMx76qA', // bigclivedotcom
        'UCg45A-ph7Eu8jQgfrwDkHLg', // Plasma channel (weird dangerous thrusters)
        ],
    "feed_tat" : [
        'UCtwKon9qMt5YLVgQt1tvJKg', // Objectivity: old artifacts
        'UCxt9Pvye-9x_AIcb1UtmF1Q', // Ashens: reviews of dollar store crud
        'UCnmgSO_4g6QcRzy0yFeglyA', // Grand Illusion: Tim's Toy Collection
        'UCyhOl6uRlxryALlT5yifldw', // JJ McCullough
        'UCmEmX_jw_pRp5UbAdzkZq-g', // Posy
        'UCfZwJg0C0P-xX7BicmwVKqw', // Lazy Posy
        'UCeEf90AEmmxaQs5BUkHqR3Q', // mitxela
        'UC7hlBf8aKs1OFNWEdWsveFA', // object history
        'UC7Jwj9fkrf1adN4fMmTkpug', // Dankpods
        'UCx6cailiCkg_mlMM7JX5yfA', // James Channel
        'UC5I2hjZYiW9gZPVkvzM8_Cw', // Techmoan
        ],
}



// The following is an older, larger, version of the list I wanted to preserve in the source.
// I trimmed it down for the sake of purity and performance.
// Among other issues, with over 100 channels, I was running into rate limits on the CORS proxy.
const more_channel_groups = { 
    "feed_walkingMen" : [
        'UCUMQFUkgaEE68_ujIdW2wAw', // Dime Store Adventures: Investigating local history and folklore!
        'UCBa659QWEk1AI4Tg--mrJ2A', // Tom Scott: Amazing Places
        'UCbCq5Y0WPGimG2jNXhoQxGw', // Atomic Frontier: Tom Scott's Doppelganger
        'UCbbQalJ4OaC0oQ0AqRaOJ9g', // Jay Foreman: Map Men and Unfinished London
        'UC2LVhJH_9cT2XKp0VAfsKOQ', // Tim Traveler: Uninteresting Places
        'UC4a9LfdavRlVMaSSWFdIciA', // Rob Words
        ],
    "feed_math" : [
        'UCYO_jab_esuFRV4b17AJtAw', // 3blue1brown: Beautiful theorems
        'UCoxcjq-8xIDTYp3uz647V5A', // Numberphile: Videos about numbers
        'UCSju5G2aFaWMqn-_0YBtq5A', // Stand Up Maths: More videos about numbers. Took me a while to realize it's not the same channel as Numberphile.
        'UCK8XIGR5kRidIw2fWqwyHRA', // Reducible
        'UC4zzTEL5tuIgGMvzjk1Ozbg', // Henry Segerman
        'UCSIvk78tK2TiviLQn4fSHaw', // Up and Atom
        ],
    "feed_engineering" : [
        'UCHnyfMqiRRG1u-2MsSQLbXA', // veritasium: Assorted videos about science and education.
        'UCMOqf8ab-42UUQIdVoKwjlQ', // Practical Engineering: Small-scale demonstrations of civil engineering challenges
        'UC6107grRI4m0o2-emgoDnAA', // Smarter Every Day: Dude makin' videos on all sorts of stuff that interests him.
        'UCEIwxahdLz7bap-VDs9h35A', // Steve Mould: Various Physics Visualizations
        'UC2bkHVIDjXS7sgrgjFtzOXQ', // Engineer Guy: Elegant videos about everyday engineering marvels
        'UC1yNl2E66ZzKApQdRuTQ4tw', // Sabine Hossenfelder
        'UCUHW94eEFW7hkUMVaZz4eDg', // Minute Physics
        'UCy0tKL1T7wFoYcxCe0xjN6Q', // Technology Connections
        'UCeXksuVW8H1x9v4gh7DWoyQ', // Physics for the birds
        'UCtESv1e7ntJaLJYKIO1FoYw', // Periodic Videos: Videos about all the elements
        'UC3j3w-oUtIAm_KI857ydvUA', // ThoiSoi2
        'UCKH_iLhhkTyt8Dk4dmeCQ9w', // Illinois EnergyProf: Clear lectures from Professor David Ruzic
        ],
    "feed_biology" : [
        'UCDSzwZqgtJEnUzacq3ddoOQ', // Ben G Thomas: Dino news
        'UCOuWeOkMrq84u5LY6apWQ8Q', // Trey the explainer: Paleontology speculation
        'UCzR-rom72PHN9Zg7RML9EbA', // PBS Eons: Old timey animals 
        'UCHsRtomD4twRf5WVHHk-cMw', // Tier Zoo: Talking about animals as if they were characters in a fighting game
        'UC9AUeAvdEVJfyS9rd9pvp8g', // Shed Science
        'UCVpankR4HtoAVtYnFDUieYA', // Ze Frank : True facts about animals 
        'UC-3SbfTPJsL8fJAPKiVqBLg', // Deep Look: Footage of small things
        'UC1KOOWHthbQVXH2kZue3_xA', // EV Nautilus: Deep Sea Livestreams
        'UC9Lp_AA5M2cMGrlvnnIns-g', // Bizarre Beasts
        'UCMy7mRjghOxB8h3nv60SU4w', // cm koseman
        'UC_aOteuWIY8ITg7DQQspG1g', // History of the Earth
        'UCH18915fTE6yZzKrqdea8RQ', // Clint's reptiles
        //'UCAJfDidJyukTekgSRZrjadw', // AronRa. Sadly, can't just subscribe to the taxonomy content
        'UCBbnbBWJtwsf0jLGUwX5Q3g', // journey to the microcosmos
        'UCO-8Osf4S3N0m7u1NivTfeg', // Phrenotopia
        ],
    "feed_space" : [
        'UCDW13ycIiHcl4QVN-YwVy0w', // Astro Pro 
        'UC7_gcs09iThXybpVgjHZ_7g', // PBS Space time
        'UC-9b7aDP6ZN0coj9-xFnrtw', // Astrum: Videos about the sensational weirdness of space. The titles are clickbaity, but the content is very good. For example, the author takes care to clearly indicate which footage is cgi, photoenhanced, etc. 
        'UCciQ8wFcVoIIMi-lfu8-cjQ', // Anton Petrov: Science discovery explainers, most space-related.
        'UCw95T_TgbGHhTml4xZ9yIqg', // The Vintage Space 
        //'', // 
        ],
    "feed_miscedu" : [
        //'', // 
        'UC2C_jShtL725hvbm1arSV9w', // CGP Grey: Mostly about flags and borders, but also about all sorts of stuff
        //'UCvG04Y09q0HExnIjdgaqcDQ', // Because Science (Doesn't really belong in this category)
        'UCFbtcTaMFnOAP0pFO1L8hVw', // Kyle Hill (Doesn't really belong in this category)
        'UC1VLQPn9cYSqx8plbk9RxxQ', // Action Lab: The titles are always clickbait, but the videos are still interesting.
        'UCKwQjav6uPCFPIDL6SXjNqQ', // Doctors Bjorkmann
        'UCV7OupzIpYe9oIn_QSlyfJw', // econimate
        'UCWul-fy84WOBE_YMcw7uJ9w', // Kieran Borovac
        //'UCeiYXex_fwgYDonaTcSIk6w', // Minute Earth - very mixed quality
        'UCtscFf8VayggrDYjOwDke_Q', // acollierastro
        'UCshObcm-nLhbu8MY50EZ5Ng', // Benn Jordan
        'UCCWeRTgd79JL0ilH0ZywSJA', // Alpha Phoenix
        'UCNq1BjOvgnPx596ddBE3wZQ', // sirrandalot
        'UCCKpicnIwBP3VPxBAZWDeNA', // Money & Macro
        'UC0p5jTq6Xx_DosDFxVXnWaQ', // The Economist
        'UCHa0gEhM-eCT6a0B1w_ZVrw', // Physics4Life
        'UCGaVdbSav8xWuFWTadK6loA', // Vlog Brothers
        'UCjD_dIlYBil51LU42cl3EkA', // Greg McCahon, the long distance motorbike guy
        'UCJVnko6tQ56PYB5BNNChPGg', // ibx2cat (2nd channel for a minecraft youtube is about... maps?)
        ],
    "feed_animals" : [
        'UCNo_xQ7NvTr31naPAcjQWjg', // OctoLab: Chill vids of little octodudes
        'UCDYyCQAk60CqabvkL5gU3Mw', // Kotumet: Otters Pets
        'UCrJH2Wy7PmCiitXKJ21yh4w', // Ninja Frog
        'UCWIxPuO_0emPbma8UlOc3JQ', // Cruiser (lots of bear videos)
        'UCpjhDz9Sqn-6h1ZwtvUiA2g', // Cheryl B (ditto)
        'UCWUH_hdDfzi98i3clGbh_Ww', // Mr Frog
        'UCKwcMBhbzQXgSM1T3TvHmiA', // Homura Ham
        'UCv3mh2P-q3UCtR9-2q8B-ZA', // Urban Rescue Ranch *
        'UCz6yuUg6N0iRiFhCLmXrNJQ', // LOUTRE (otter giving birth)
        'UCj2Eeg01Mn5WmcXxt695fUg', // Brady Brandwood (Leon the Lobster)
        ],
    "feed_birds" : [
        'UCsFgbVuhRrPV5FqyN7kOD8g', // Bald Eagle Cam
        'UCPPjuJTt9jiOZNHScvEmvRg', // Seducktive
        'UCnUdaxbBMPQ9o9KVz7Oa6eQ', // Apollo the Parrot
        'UC6q7I1DD2Jv5Ur9UEIavIrA', // David M Bird
        'UCDjdXwT-KrFPsqOSg4KL8Nw', // Leslie Bird Nerd
        'UCcNyzOCKvyMBaA4iQVgO9EQ', // MyBackyardBirding
        ],
    "feed_food" : [
        'UC9_p50tH3WmMslWRWKnM7dQ', // Adam Ragusea
        'UCsaGKqPZnGp_7N80hcHySGQ', // Tasting history: Historically accurate recipes, along with discussion of adjacent history.
        'UCJHA_jMfCvEnv-3kRjTCQXw', // Babish: Mostly makes meme food
        'UCRIZtPl9nb9RiXc9btSTQNw', // Food Wishes: Straightforward recipe videos
        'UCJLKwTg0IaSMoq6hLHT3CAA', // Ordinary Sausage
        'UCxr2d4As312LulcajAkKJYw', // Townsends
        ],
    "feed_film" : [
        'UCrTNhL_yO3tPTdQ5XgmmWjA', // red letter media: Wisconsin's finest cultural output
        'UCEOXxzW2vU0P-0THehuIIeg', // Captain D: Like a 90s childrens science show, but about digital effects
        'UCSc16oMxxlcJSb9SXkjwMjA', // YMS : His "Top Ten Films of 2015" list has 39 entries and was published in 2018.
        'UC7-E5xhZBZdW-8d7V80mzfg', // Jenny Nicholson: Why does she have so many porgs?
        'UCSUf5_EPEfl4zlBKZHkZdmw', // Danny Gonzales * 
        'UCTSRIY3GLFYIpkR2QwyeklA', // Drew Gooden *
        'UCZXAVdAplsu1tFZ9OqQhJFg', // Virtual Frog *
        'UCGeIjGngCkErevSNHdZYD5Q', // Expleen
        'UCE1jXbVAGJQEORz9nZqb5bQ', // Ahoy
        'UCNMyoMaXJZITZaRKCz7G23Q', // Peter Knetter
        'UCweDKPSF65wRw5VHFUJYiow', // Curious Archive
        'UCH_7doiCkWeq0v3ycWE5lDw', // Any Austin
        ],
    "feed_fights" : [
        'UCRrvZqCL1YsqRA8IpXrhYQQ', // Jill Bearup
        'UC9pgQfOXRsp4UKrI8q0zjXQ', // Lindsay Beige
        'UCkmMACUKpQeIxN9D9ARli1Q', // Shadiversity
        
        ],
    "feed_sketch" : [
        'UC_mneEC0wc29EGGmIsN_xLA', // Aunty Donna: Austrailian Sketch Comedy
        'UC9gFih9rw0zNCK3ZtoKQQyA', // Jenna Marbles: I love her horrible dogs.
        'UC3izYCSBcfi2LfdIr-qg0gQ', // Dragon's Tomb: Completely accurate board game tutorials.
        'UCWk68Uw6V990fjnTbcOHeoA', // Alex Ernst: Something something apple cider vinegar
        'UCto7D1L-MiRoOziCXK9uT5Q', // Game it Out: "As always, we're going to try to play this game as wrong as possible."
        'UCcMXHcc7fikiJ-PhrGUeQoQ', // Gatis Kandis
        'UClyGlKOhDUooPJFy4v_mqPg', // DougDoug
        'UCG_vclOrIHcW1dWF_h4WsLA', // Taskmaster Minnesota
        ],
    "feed_music" : [
        'UCq6aw03lNILzV96UvEAASfQ', // Bill Wurtz: Music? 
        'UC6yeqgmyqhDyMPzE4wwxQig', // Ryan's Shorts (Bass Pro Shop)
        'UCakAg8hC_RFJm4RI3DlD7SA', // BDG Brian David Gilbert
        'UCSE6yilNScIz1SLTNQvrXMw', // Vinheteiro
        'UCEgm-3RvRn4nCR-fGGVsfdQ', // Mattias Krantz
        'UCoNRSwYHJdy-yV1b82ZdHfQ', // Seth Everman
        ],
    "feed_tat" : [
        'UCtwKon9qMt5YLVgQt1tvJKg', // Objectivity: old artifacts
        'UCxt9Pvye-9x_AIcb1UtmF1Q', // Ashens: reviews of dollar store crud
        'UCnmgSO_4g6QcRzy0yFeglyA', // Grand Illusion: Tim's Toy Collection
        'UCyhOl6uRlxryALlT5yifldw', // JJ McCullough
        'UCmEmX_jw_pRp5UbAdzkZq-g', // Posy
        'UCfZwJg0C0P-xX7BicmwVKqw', // Lazy Posy
        'UCeEf90AEmmxaQs5BUkHqR3Q', // mitxela
        'UC7hlBf8aKs1OFNWEdWsveFA', // object history
        'UC7Jwj9fkrf1adN4fMmTkpug', // Dankpods
        'UCx6cailiCkg_mlMM7JX5yfA', // James Channel
        'UC5I2hjZYiW9gZPVkvzM8_Cw', // Techmoan
        ],
    "feed_fans" : [
        'UC3_AWXcf2K3l9ILVuQe-XwQ', // Matthias random stuff
        'UCUXW4gT27TOaDzKFyN-1tXQ', // Major Hardware
        'UC4AkVj-qnJxNtKuz3rkq16A', // Robert Murray-Smith
        'UC1E8OmOG17VckoPviOPmkMw', // TNT Omnibus (RMS' second channel)
        'UCtM5z2gkrGRuWd0JQMx76qA', // bigclivedotcom
        'UCg45A-ph7Eu8jQgfrwDkHLg', // Plasma channel (weird dangerous thrusters)
        ],
    "feed_fiction" : [
        'UCncTjqw75krp9j_wRRh5Gvw', // Worldbuilding Notes: Imaginary places
        'UCxXu9tCU63mF1ntk89XPkzA', // Worthikids
        'UCMkbjxvwur30YrFWw8kpSaw', // Homestar Runner
        'UCZdrTo_md37z3iogKYrVgCw', // Monstergarden
        ],
    "feed_bgames" : [
        'UCtT0CIZIXLMlPdQVwmI6RjA', // Shelfside
        'UCmJ6GCpVC6v_cXXIBatFlsw', // Jack Reda
        ],  
}



// Take a channel id, get the xml of rss feed, and apply some fn
// (The fn will be to get the video info from the channel and then push it to some array)
function fetch_channel_rss(channel_id,fn){
    const youtubeRSSprefix = 'https://www.youtube.com/feeds/videos.xml?channel_id=' 
    url = proxyserver + encodeURIComponent(youtubeRSSprefix + channel_id);
    return fetch(url)
        .then(response => response.text())
        .then(text => new window.DOMParser().parseFromString(text, "application/xml"))
        .then(channel_xml => fn(channel_xml))
}
// Grab the info I care about from a channel's rss feed. 
function grab_info_from_rss(channel_xml){
    item = channel_xml.querySelector('entry');
        title = item.querySelector('title').textContent;
        videoId = item.querySelector('videoId').textContent;
        date = item.querySelector('published').textContent;
        channelId = item.querySelector('channelId').textContent;
    author = channel_xml.querySelector('title').textContent;
    console.log(author, videoId);
    return([author, title, videoId, date, channelId]);
}
// Given a channel id, push it to a list (asynchronous). Returns a promise for the arr itself.
function push_channel_info(channel_id,arr){
    fn = (channel_xml => {
        arr.push(grab_info_from_rss(channel_xml));
        return arr;
    })
    return fetch_channel_rss(channel_id,fn);
}





// the following functions take the video info and render it as cute little blocks
function formatBlankVideoBlock(){
    videoBlock = document.createElement('div');
    videoBlock.setAttribute('class', 'videoBlock');
    videoBlock.innerHTML = `
        <a href="">
        <img src="https://i3.ytimg.com/vi/default.jpg"/>
        <div class="mainlink">PLACEHOLDER TITLE</div>
        <div class="metadata">CHANNEL - DATE</div>
        </a>`
    return videoBlock;
}
function formatVideoBlock(author, title, videoId, date, channelId){
    date = new Date(date);
    date = date.toDateString();
    videoBlock = document.createElement('div');
    videoBlock.setAttribute('class', 'videoBlock');
    videoBlock.innerHTML = `
        <a href="https://www.youtube.com/watch?v=${videoId}" target="_blank" rel="noopener noreferrer">
        <img src="https://i3.ytimg.com/vi/${videoId}/default.jpg"/>
        <div class="mainlink">${title}</div>
        <div class="metadata">${author} - ${date}</div>
        </a>`;
    return videoBlock;
}
function render_video_blocks(category,channels,video_array){
    const feedContainer = document.getElementById(category);
    feedContainer.innerHTML = "";
    //sort list in reverse order by date
    video_array.sort(function(a,b){return b[3].localeCompare(a[3]);});
    //create a little entry for each video
    video_array.forEach(video_info => {
        feedContainer.appendChild(formatVideoBlock(...video_info));
    });
    // Next, fill out the rest of the array with placeholder blocks (I hate it when elements change size on a page.)
    missing_videos = channels.length - video_array.length;
    for (var i=0; i < missing_videos; i++){
        feedContainer.appendChild(formatBlankVideoBlock());
    }
}






// Helper function which spaces out function calls with a specified delay.
// This is needed so I don't exceed the rate limit on the cors proxy server.
function apply_fn_with_delay(arr, fn, delay=delay_ms, index = 0) {
    if (index >= arr.length){return};
    fn(arr[index]);
    setTimeout(() => apply_fn_with_delay(arr, fn, delay, index + 1), delay);
}
function promiseChain(arr, fn, delay) {
    return arr.reduce(
        (promise, item, index) => {
            return promise.then(() => {return new Promise((resolve) => {setTimeout(() => {fn(item);resolve();}, delay);});});
        },
        Promise.resolve(),
    );
}







//START BY POPULATING ALL CHANNELS WITH A BLANK
for (const [category, channels] of Object.entries(channel_groups)) {render_video_blocks(category,channels,[]);}

//NEXT FLATTEN THE DICTIONARY OF CHANNELS
category_channel_pairs = [];
for (const [category, channels] of Object.entries(channel_groups)){
    for (channel of channels){
        category_channel_pairs.push([category,channel]);
    }
}

//CREATE THE LISTS NEEDED TO HOLD THE CHANNEL INFO FOR EACH CATEGORY
channel_info = {}; 
for (const key in channel_groups) {channel_info[key]=[]};

//FINALLY, PAUSING IN BETWEEN EACH, ITERATE THROUGH THE CHANNELS, AND PUSH THE INFO INTO MY LITTLE HTML BLOCKS
fn = function(pair){
    category = pair[0];
    channel  = pair[1];
    video_array = channel_info[category];
    channels = channel_groups[category];
    push_channel_info(channel,video_array)
        .then(video_array => render_video_blocks(category,channels,video_array))
        .then(render_video_blocks("feed_combined",category_channel_pairs,Object.entries(channel_info).map(item=>item[1]).flat()));
}
promiseChain(category_channel_pairs,fn,delay_ms);



</script>
-->



<!--
[Vihart](https://www.youtube.com/user/Vihart/videos?disable_polymer=1)
: Math Doodles

[George Hart](https://www.youtube.com/channel/UCTl0dASnxto6j2wlVs5Bs2Q/videos?disable_polymer=1)
: Origami
-->


<!--
[Bon Appétit](https://www.youtube.com/user/BonAppetitDotCom/videos?view=0&sort=p&flow=grid)
: This is the one where they make gourmet skittles *

[Artifexian](https://www.youtube.com/user/Artifexian/videos)
: Strange exoplanets and advice about imagining them
-->


<!--
[PBS Digital Studios](https://www.youtube.com/user/pbsdigitalstudios/videos?disable_polymer=1)
: See also Lindsay Ellis' [personal channel](https://www.youtube.com/user/chezapoctube/videos?disable_polymer=1) *
-->


<!--
[MKBHD](https://www.youtube.com/user/marquesbrownlee/videos?disable_polymer=1)
: Gizmos

[Questing Beast](https://www.youtube.com/channel/UCvYwePdbWSEwUa-Pk02u3Zw/videos?disable_polymer=1)
: Tabletop RPG Books
-->




<!---
### Reviews of Board Games in particular

[Shut Up & Sit Down](https://www.youtube.com/channel/UCyRhIGDUKdIOw07Pd8pHxCw/videos?disable_polymer=1)
: Skit-based board game reviews

[Actuallol](https://www.youtube.com/user/actualol/videos?disable_polymer=1)
: More silly boardgame reviews

[Tolarian Community College](https://www.youtube.com/user/tolariancommunity/videos?disable_polymer=1)
: Card sleeves and whatnot

[marcowargamer](https://www.youtube.com/user/marcowargamer/videos?disable_polymer=1)
: slightly more thoughtful boardgame reviews

[Inside The Box](https://www.youtube.com/user/psychoticeps/videos?disable_polymer=1)
: Really long skit-based reviews



### Animated stuff

[Suncreature Studios](https://www.youtube.com/user/SunCreatureStudio/videos?disable_polymer=1)
: Animated adventure shorts.

[Sam O'Nella](https://www.youtube.com/channel/UC1DTYW241WD64ah5BFWn4JA/videos?disable_polymer=1)
: Honestly, it's more of a slideshow of crudely drawn stick figures.

[Explosm](https://www.youtube.com/user/ExplosmEntertainment/videos?disable_polymer=1)
: Depressing Stick Figure cartoons



### Janky Engineering

[Simone Giertz](https://www.youtube.com/channel/UC3KEoMzNz8eYnwBC34RaKCQ/videos?disable_polymer=1)
: Queen of Shitty Robots *






### Making  Stuff

[Slingshot Channel](https://www.youtube.com/user/JoergSprave/videos)
: Strange Handmade Elastic-powered projectiles


[I Like To Make Stuff](https://www.youtube.com/user/iliketomakestuffcom/videos?disable_polymer=1)
: Woodworking



### Mad Execution of Ordinary Ideas

<div id="feed_craft_mad_competent" class="youtubeFeed"></div>
<script>
channels_craft_mad_competent = [
];
buildFeed(channels_craft_mad_competent, "feed_craft_mad_competent");
</script>


### Chemistry and Metallurgy and whatnot


<div id="feed_chemistry" class="youtubeFeed"></div>
<script>
channels_chemistry = [
];
buildFeed(channels_chemistry, "feed_chemistry");  
</script>

Gloudas
Thrifter's Guide to Geekery
https://www.youtube.com/channel/UC9EPwKHQ9rFpquOGUILwQ2g/videos
no intitive??
https://www.youtube.com/channel/UCD6ERRdXrF2IZ0R888G8PQg/videos
https://www.youtube.com/channel/UCZFipeZtQM5CKUjx6grh54g/videos
Whistlin Diesel
Fact Fiend?
https://www.youtube.com/user/jblow888/videos
The Royal Instituion
animalogic
-->

