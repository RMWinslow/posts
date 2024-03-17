---
title: YouTube Channels
description: "This is a list of Youtube channels I like to check back to watch."
parent: Media Recommendations
grand_parent: Art and Culture
layout: post
toc: true
date: 2021-06-24
last_modified_date: 2023-05-16
permalink: /youtube
redirect_from:
  - /media/youtube
---

<!--
last_modified_date: 2022-11-27-->

Youtube's recommendation algorithm is a mess, and an unsorted list of every subscription isn't great for finding stuff I want to watch, so I made a categorized list of youtube channels that I like to check occasionally.

I also find that the YouTube experience is improved by a third-party client.
I use [FreeTube](https://freetubeapp.io/) on desktop,
and [NewPipe](https://newpipe.net/) on Android.

It takes a bit to load because I have to go through a CORS proxy to grab the youtube RSS feeds using only javascript.





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




## Educational 

### A Man Walks About Describing Things

(aka the Tom Scott genre)

<div id="feed_walkingMen" class="youtubeFeed"></div>

### Math

<div id="feed_math" class="youtubeFeed"></div>

### Physics, Chemistry, and Engineering

<div id="feed_engineering" class="youtubeFeed"></div>

### Life Sciences

<div id="feed_biology" class="youtubeFeed"></div>

### Space!

<div id="feed_space" class="youtubeFeed"></div>

### Misc Educational and Semi-Educational

<div id="feed_miscedu" class="youtubeFeed"></div>

## Just Entertainment

### Cute Animals

<div id="feed_animals" class="youtubeFeed"></div>

### Birds in particular

<div id="feed_birds" class="youtubeFeed"></div>

### Food and Cookery

<div id="feed_food" class="youtubeFeed"></div>

### Media Commentary

<div id="feed_film" class="youtubeFeed"></div>

### Media Commentary Specifically about Fights

<div id="feed_fights" class="youtubeFeed"></div>

### Comedy

<div id="feed_sketch" class="youtubeFeed"></div>

### Mostly Musical Comedy

<div id="feed_music" class="youtubeFeed"></div>
### Interesting objects

<div id="feed_tat" class="youtubeFeed"></div>

### The Fan Fandom

<div id="feed_fans" class="youtubeFeed"></div>

### Original Fictional Content

<div id="feed_fiction" class="youtubeFeed"></div>

### Board Games

<div id="feed_bgames" class="youtubeFeed"></div>






<script>
//const proxyserver = 'https://corsproxy.io/?' // was acting up. Trying another one.
//const proxyserver = 'https://corsproxy.org/?'
const proxyserver = 'https://api.allorigins.win/raw?url='
const youtubeRSSprefix = 'https://www.youtube.com/feeds/videos.xml?channel_id=' 
function channelIdToUrl(id){ return proxyserver + encodeURIComponent(youtubeRSSprefix + id);};

function formatVideoBlock(author, title, videoId, date, channelId){
  date = new Date(date);
  date = date.toDateString();
  return `
    <a href="https://www.youtube.com/watch?v=${videoId}">
      <img src="https://i3.ytimg.com/vi/${videoId}/default.jpg"/>
      <div class="mainlink">${title}</div>
      <div class="metadata">${author} - ${date}</div>
    </a>
    `
}

const blankVideoBlock = `
    <a href="">
      <img src="https://i3.ytimg.com/vi/default.jpg"/>
      <div class="mainlink">PLACEHOLDER TITLE</div>
      <div class="metadata">CHANNEL - DATE</div>
    </a>
    `

function buildFeed(channelIdList, containerId) {
  const feedContainer = document.getElementById(containerId);

  // Create placeholder blocks
  channelIdList.forEach(id => {
      videoBlock = document.createElement('div');
      videoBlock.setAttribute('class', 'videoBlock');
      videoBlock.innerHTML = blankVideoBlock;
      feedContainer.appendChild(videoBlock);
    });
  
  promises = channelIdList.map(id => fetch(channelIdToUrl(id))
    .then(response => response.text())
    .then(text => new window.DOMParser().parseFromString(text, "application/xml"))
  );

  Promise.all(promises).then(data => {
    feedContainer.innerHTML = "";
    videoList = []; 
    //grab data for first video from each channel
    data.forEach(feed => {
      try{
      item = feed.querySelector('entry');
        title = item.querySelector('title').textContent;
        videoId = item.querySelector('videoId').textContent;
        date = item.querySelector('published').textContent;
        channelId = item.querySelector('channelId').textContent;
      author = feed.querySelector('title').textContent;
      console.log(author, videoId);
      videoList.push([author, title, videoId, date, channelId]);
      }
      catch (error){console.log(error)} // Just ignore the channels that weren't parsed right.
    });
    //sort list in reverse order by date
    videoList.sort(function(a,b){return b[3].localeCompare(a[3]);});
    //create a little entry for each video
    videoList.forEach(video => {
      videoBlock = document.createElement('div');
      videoBlock.setAttribute('class', 'videoBlock');
      videoBlock.innerHTML = formatVideoBlock(video[0],video[1],video[2], video[3], video[4]);
      feedContainer.appendChild(videoBlock);
    });
  }); 
}
</script>




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

