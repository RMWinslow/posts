---
title: YouTube Channels
description: "Experimental Little In-browser Feed."
parent: Media Recommendations
grand_parent: Art and Culture
layout: post
toc: true
date: 2021-06-24
last_modified_date: 2025-02-10
permalink: /youtube
redirect_from:
  - /media/youtube
nav_exclude: false
search_exclude: false
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




## Categorized Videos

<div id="youtube_feeds"></div>

## Uncategorized Feed

<details>
<summary>All channels. Click to expand.</summary>
<div id="feed_combined" class="youtubeFeed"></div>
</details>

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
    margin-top: 0.3rem;
    margin-right: 0.3rem;
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
    margin-right: 0.8rem;
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




<script>
const channel_groups = new Map();

fetch('https://www.rmwinslow.com/ytrss/latest_videos.json')
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

  // Sort each category by date.
  channel_groups.forEach((category_channels, category) => {
    category_channels.sort(channel_date_sorter);
  });

  // Create a header and feed for each category.
  feed_div = document.getElementById('youtube_feeds');
  channel_groups.forEach((category_channels, category) => { // When using forEach on a Map, parameters are value,key,map.
    // Header
    category_header = document.createElement('h3');
    category_header.textContent = category;
    feed_div.appendChild(category_header);
    // Feed
    category_feed = document.createElement('div');
    category_channels.forEach(channel => {
      category_feed.appendChild(create_video_block(channel));
    });
    feed_div.appendChild(category_feed);
  });

  // Finally, do the process again for the giant combined feed. 
  channels.sort(channel_date_sorter);
  channels.forEach(channel => {
    document.getElementById('feed_combined').appendChild(create_video_block(channel));
  });
}


function create_video_block(channel) {
  video_block = document.createElement('div');
  video_block.className = 'videoBlock';
  video_block.innerHTML = `
  <a href="https://www.youtube.com/embed/${channel.video_id}" target="_blank" rel="noopener noreferrer">
    <img src="https://i3.ytimg.com/vi/${channel.video_id}/mqdefault.jpg" alt="Thumbnail">
    <div class="mainlink">${channel.title}</div>
    <div class="metadata">${channel.author} - ${channel.date.slice(0, 10)}</div>
  </a>
  `;
  return video_block;
}

function channel_date_sorter (a,b) {
    return new Date(b.date) - new Date(a.date);
}

</script>



<!--

    "feed_miscedu" : [
        //'UCvG04Y09q0HExnIjdgaqcDQ', // Because Science (Doesn't really belong in this category)
        'UCGaVdbSav8xWuFWTadK6loA', // Vlog Brothers
        'UCjD_dIlYBil51LU42cl3EkA', // Greg McCahon, the long distance motorbike guy
        ],
    "feed_film" : [
        'UCSc16oMxxlcJSb9SXkjwMjA', // YMS : His "Top Ten Films of 2015" list has 39 entries and was published in 2018.
        'UCGeIjGngCkErevSNHdZYD5Q', // Expleen
        'UCE1jXbVAGJQEORz9nZqb5bQ', // Ahoy
        'UCweDKPSF65wRw5VHFUJYiow', // Curious Archive
        ],
    "feed_fights" : [
        'UCkmMACUKpQeIxN9D9ARli1Q', // Shadiversity
        ],
    "feed_sketch" : [
        'UCcMXHcc7fikiJ-PhrGUeQoQ', // Gatis Kandis
        'UCG_vclOrIHcW1dWF_h4WsLA', // Taskmaster Minnesota
        ],
        ],  


}



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

-->




<!---


### Animated stuff

[Suncreature Studios](https://www.youtube.com/user/SunCreatureStudio/videos?disable_polymer=1)
: Animated adventure shorts.

[Sam O'Nella](https://www.youtube.com/channel/UC1DTYW241WD64ah5BFWn4JA/videos?disable_polymer=1)
: Honestly, it's more of a slideshow of crudely drawn stick figures.

[Explosm](https://www.youtube.com/user/ExplosmEntertainment/videos?disable_polymer=1)
: Depressing Stick Figure cartoons



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

