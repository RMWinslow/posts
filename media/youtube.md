---
title: YouTube Channels
description: "This is a list of Youtube channels I like to check back to watch."
parent: Media Recommendations
grand_parent: Art and Culture
layout: post
toc: true
date: 2021-06-24
last_modified_date: 2023-01-31
nav_exclude: true
---

<!--
last_modified_date: 2022-11-27-->

Youtube's recommendation algorithm is a mess, and an unsorted list of every subscription isn't great for finding stuff I want to watch, so I made a categorized list of youtube channels that I like to check occasionally.

I also find that the YouTube experience is improved by a third-party client.
I use [FreeTube](https://freetubeapp.io/) on desktop,
and [NewPipe](https://newpipe.net/) on Android.







<style>
  .videoBlock {
    border: 1px solid var(--bordercolor);
    min-height: 60px;
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
  }
  .videoBlock img {
    float: left;
    margin-right: 1rem;
    height: 60px;
  }
  .videoBlock .metadata {
    color: var(--textcolor);
  }
</style>

<script>
const proxyserver = 'https://corsproxy.io/?'
const youtubeRSSprefix = 'https://www.youtube.com/feeds/videos.xml?channel_id=' 
function channelIdToUrl(id){ return proxyserver + youtubeRSSprefix + id;};

function formatVideoBlock(author, title, videoId, date, channelId){
  date = new Date(date);
  date = date.toDateString();
  return `
    <a href="https://www.youtube.com/v/${videoId}">
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







## Educational 



### A Man Describes What Strikes His Fancy

<div id="feed_walkingMen" class="youtubeFeed"></div>
<script>
channels_walkingMen = [
  'UCUMQFUkgaEE68_ujIdW2wAw', // Dime Store Adventures: Investigating local history and folklore!
  'UCBa659QWEk1AI4Tg--mrJ2A', // Tom Scott: Amazing Places
  'UCbCq5Y0WPGimG2jNXhoQxGw', // Atomic Frontier: Tom Scott's Doppelganger
  'UCbbQalJ4OaC0oQ0AqRaOJ9g', // Jay Foreman: Map Men and Unfinished London
  'UC2LVhJH_9cT2XKp0VAfsKOQ', // Tim Traveler: Uninteresting Places
  'UCyhOl6uRlxryALlT5yifldw', // JJ McCullough
  'UC2C_jShtL725hvbm1arSV9w', // CGP Grey: Mostly about flags and borders, but also about all sorts of stuff
];
buildFeed(channels_walkingMen, "feed_walkingMen");
</script>




### Math

<div id="feed_math" class="youtubeFeed"></div>
<script>
channels_math = [
  'UCYO_jab_esuFRV4b17AJtAw', // 3blue1brown: Beautiful theorems
  'UCoxcjq-8xIDTYp3uz647V5A', // Numberphile: Videos about numbers
  'UCSju5G2aFaWMqn-_0YBtq5A', // Stand Up Maths: More videos about numbers. Took me a while to realize it's not the same channel as Numberphile.
];
buildFeed(channels_math, "feed_math");  
</script>


<!--
[Vihart](https://www.youtube.com/user/Vihart/videos?disable_polymer=1)
: Math Doodles

[George Hart](https://www.youtube.com/channel/UCTl0dASnxto6j2wlVs5Bs2Q/videos?disable_polymer=1)
: Origami
-->


### Physics and Engineering


<!--
[Illinois EnergyProf](https://www.youtube.com/channel/UCKH_iLhhkTyt8Dk4dmeCQ9w/videos?disable_polymer=1)
: Clear lectures from Professor David Ruzic
-->



<div id="feed_engineering" class="youtubeFeed"></div>
<script>
channels_engineering = [
  'UCHnyfMqiRRG1u-2MsSQLbXA', // veritasium: Assorted videos about science and education.
  'UCMOqf8ab-42UUQIdVoKwjlQ', // Practical Engineering: Small-scale demonstrations of civil engineering challenges
  'UC6107grRI4m0o2-emgoDnAA', // Smarter Every Day: Dude makin' videos on all sorts of stuff that interests him.
  'UCEIwxahdLz7bap-VDs9h35A', // Steve Mould: Various Physics Visualizations
  'UC2bkHVIDjXS7sgrgjFtzOXQ', // Engineer Guy: Elegant videos about everyday engineering marvels
];
buildFeed(channels_engineering, "feed_engineering");
</script>



### Life Sciences

<div id="feed_animals" class="youtubeFeed"></div>
<script>
channels_animals = [
  'UCDjdXwT-KrFPsqOSg4KL8Nw', // Leslie Bird Nerd
  'UCNo_xQ7NvTr31naPAcjQWjg', // OctoLab: Chill vids of little octodudes
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
  //'', // 
];
buildFeed(channels_animals, "feed_animals");
</script>




### Space!


<div id="feed_space" class="youtubeFeed"></div>
<script>
channels_space = [
  'UCDW13ycIiHcl4QVN-YwVy0w', // Astro Pro 
  'UC7_gcs09iThXybpVgjHZ_7g', // PBS Space time
  'UC-9b7aDP6ZN0coj9-xFnrtw', // Astrum: Videos about the sensational weirdness of space. The titles are clickbaity, but the content is very good. For example, the author takes care to clearly indicate which footage is cgi, photoenhanced, etc. <!--I did notice in one video they confused "amines" for "amino acids"-->
  'UCciQ8wFcVoIIMi-lfu8-cjQ', // Anton Petrov: Science discovery explainers, most space-related.
  //'', // 
  //'', // 
];
buildFeed(channels_space, "feed_space");  
</script>




### Chemistry and Metallurgy and whatnot


<div id="feed_chemistry" class="youtubeFeed"></div>
<script>
channels_chemistry = [
  'UC1VLQPn9cYSqx8plbk9RxxQ', // Action Lab: The titles are always clickbait, but the videos are still interesting.
  'UCu6mSoMNzHQiBIOCkHUa2Aw', // Cody's Lab: Also features weird gardening experiments
  'UCtESv1e7ntJaLJYKIO1FoYw', // Periodic Videos: Videos about all the elements
  'UCfIqCzQJXvYj9ssCoHq327g', // How to Make Everything: Was originally about making a sandwich completely from scratch. 
  'UCFhXFikryT4aFcLkLw2LBLA', // Nile Red
  'UCA0mlN90EHCizvo101nbr-g', // Nile Red Shorts
  'UC1D3yD4wlPMico0dss264XA', // Nile Blue
  'UC1_kuFbEBdHtf7_c2wIdNVg', // Pyrotechnical
  'UCV5vCi3jPJdURZwAOO_FNfQ', // Thought Emporium
];
buildFeed(channels_chemistry, "feed_chemistry");  
</script>







## Entertainment



## Food and Cookery

<!--
[Bon Appétit](https://www.youtube.com/user/BonAppetitDotCom/videos?view=0&sort=p&flow=grid)
: This is the one where they make gourmet skittles *
-->


<div id="feed_food" class="youtubeFeed"></div>
<script>
channels_food = [
  'UC9_p50tH3WmMslWRWKnM7dQ', // Adam Ragusea
  'UCsaGKqPZnGp_7N80hcHySGQ', // Tasting history: Historically accurate recipes, along with discussion of adjacent history.
  'UCJHA_jMfCvEnv-3kRjTCQXw', // Babish: Mostly makes meme food
  'UCRIZtPl9nb9RiXc9btSTQNw', // Food Wishes: Straightforward recipe videos
  'UCJLKwTg0IaSMoq6hLHT3CAA', // Ordinary Sausage
];
buildFeed(channels_food, "feed_food");  
</script>




<!--
[Artifexian](https://www.youtube.com/user/Artifexian/videos)
: Strange exoplanets and advice about imagining them
-->

[Worldbuilding Notes](https://www.youtube.com/channel/UCncTjqw75krp9j_wRRh5Gvw/videos?disable_polymer=1)
: Imaginary places








### Media Commentary

<!--
[PBS Digital Studios](https://www.youtube.com/user/pbsdigitalstudios/videos?disable_polymer=1)
: See also Lindsay Ellis' [personal channel](https://www.youtube.com/user/chezapoctube/videos?disable_polymer=1) *
-->


<div id="feed_film" class="youtubeFeed"></div>
<script>
channels_film = [
  'UCrTNhL_yO3tPTdQ5XgmmWjA', // red letter media: Wisconsin's finest cultural output
  'UCEOXxzW2vU0P-0THehuIIeg', // Captain D: Like a 90s childrens science show, but about digital effects
  'UCSc16oMxxlcJSb9SXkjwMjA', // YMS : His "Top Ten Films of 2015" list has 39 entries and was published in 2018.
  'UC7-E5xhZBZdW-8d7V80mzfg', // Jenny Nicholson: Why does she have so many porgs?
  'UCSUf5_EPEfl4zlBKZHkZdmw', // Danny Gonzales * 
  'UCTSRIY3GLFYIpkR2QwyeklA', // Drew Gooden *
  'UCZXAVdAplsu1tFZ9OqQhJFg', // Virtual Frog *
  'UCGeIjGngCkErevSNHdZYD5Q', // Expleen
];
buildFeed(channels_film, "feed_film");  
</script>




### Comedy

<div id="feed_sketch" class="youtubeFeed"></div>
<script>
channels_sketch = [
  'UC_mneEC0wc29EGGmIsN_xLA', // Aunty Donna: Austrailian Sketch Comedy
  'UC9gFih9rw0zNCK3ZtoKQQyA', // Jenna Marbles: I love her horrible dogs.
  'UC3izYCSBcfi2LfdIr-qg0gQ', // Dragon's Tomb: Completely accurate board game tutorials.
  'UCq6aw03lNILzV96UvEAASfQ', // Bill Wurtz: Music? 
  'UCWk68Uw6V990fjnTbcOHeoA', // Alex Ernst: Something something apple cider vinegar
  'UCv3mh2P-q3UCtR9-2q8B-ZA', // Urban Rescue Ranch *
  'UCto7D1L-MiRoOziCXK9uT5Q', // Game it Out: "As always, we're going to try to play this game as wrong as possible."
];
buildFeed(channels_sketch, "feed_sketch");  
</script>



### Interesting collections


<div id="feed_tat" class="youtubeFeed"></div>
<script>
channel_tat = [
  'UCtwKon9qMt5YLVgQt1tvJKg', // Objectivity: old artifacts
  'UCxt9Pvye-9x_AIcb1UtmF1Q', // Ashens: reviews of dollar store crud
  'UCnmgSO_4g6QcRzy0yFeglyA', // Grand Illusion: Tim's Toy Collection
  '', // 
];
buildFeed(channel_tat, "feed_tat");  
</script>





<!--
[MKBHD](https://www.youtube.com/user/marquesbrownlee/videos?disable_polymer=1)
: Gizmos

[Questing Beast](https://www.youtube.com/channel/UCvYwePdbWSEwUa-Pk02u3Zw/videos?disable_polymer=1)
: Tabletop RPG Books
-->




<!---->
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
-->




<!---->
### Animated stuff

[Suncreature Studios](https://www.youtube.com/user/SunCreatureStudio/videos?disable_polymer=1)
: Animated adventure shorts.

[Sam O'Nella](https://www.youtube.com/channel/UC1DTYW241WD64ah5BFWn4JA/videos?disable_polymer=1)
: Honestly, it's more of a slideshow of crudely drawn stick figures.

[Explosm](https://www.youtube.com/user/ExplosmEntertainment/videos?disable_polymer=1)
: Depressing Stick Figure cartoons
-->



<!--
### Making  Stuff

[Slingshot Channel](https://www.youtube.com/user/JoergSprave/videos)
: Strange Handmade Elastic-powered projectiles

[Pocket83](https://www.youtube.com/user/pocket83/videos?disable_polymer=1)
: Neat little doodads

[I Like To Make Stuff](https://www.youtube.com/user/iliketomakestuffcom/videos?disable_polymer=1)
: Woodworking

-->



### Making Horrible Stuff

<!--
[Simone Giertz](https://www.youtube.com/channel/UC3KEoMzNz8eYnwBC34RaKCQ/videos?disable_polymer=1)
: Queen of Shitty Robots *

[Ian Hubert](https://www.youtube.com/channel/mrdodobird/videos?disable_polymer=1)
: Blender Tutorials which are either awful or amazing. *
-->


<div id="feed_jankyEngineering" class="youtubeFeed"></div>
<script>
channels_jankyEngineering = [
  'UCtHaxi4GTYDpJgMSGy7AeSw', // Michael Reeves: William Osman's angrier housemate 
  'UCfMJ2MchTSW2kWaT0kK94Yw', // William Osman: Reckless disregard for laser safety
  'UCVS89U86PwqzNkK2qYNbk5A', // Failed Mythbuster Allen Pan
  'UCoQBtJ24OUqB4O285xp9ZrQ', // Good Inventions: Very practical. Great Job.
  'UCJLZe_NoiG0hT7QCX_9vmqw', // I did a Thing
  'UCJYJgj7rzsn0vdR7fkgjuIA', // StopPyro: Nevermind. <i>This</i> is reckless disregard for laser safety 
  'UCVovvq34gd0ps5cVYNZrc7A', // Explosions and Fire
  'UCgO8vdeWcywARd99Od-H_8A', // /Tom Wildenhain: Using MS Office to commit crimes against nature
  'UCB4NFn-8oipHct0IfAQBQrQ', // Unnecessary Inventions *
  'UC3azLjQuz9s5qk76KEXaTvA', // suckerpinch
  'UCJ0-OtVpF0wOKEqT2Z1HEtA', // Electroboom
];
buildFeed(channels_jankyEngineering, "feed_jankyEngineering");
</script>
















<!--Gloudas
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

