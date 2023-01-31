---
title: YouTube Channels
description: "This is a list of Youtube channels I like to check back to watch."
parent: Media Recommendations
grand_parent: Art and Culture
layout: post
toc: true
date: 2021-06-24
last_modified_date: 2023-01-30
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












## A Man Walks About Whilst Describing Something

[Dime Store Adventures](https://www.youtube.com/@DimeStoreAdventures/videos)
: Investigating local history and folklore!

[Tom Scott](https://www.youtube.com/@TomScottGo/videos)
: Amazing Places

[Atomic Frontier](https://www.youtube.com/@AtomicFrontier/videos)
: Tom Scott's Doppelganger

[Jay Foreman](https://www.youtube.com/user/jayforeman51/videos?disable_polymer=1)
: Map Men and Unfinished London

[The Tim Traveller](https://www.youtube.com/user/UC2LVhJH_9cT2XKp0VAfsKOQ/videos?disable_polymer=1)
: Uninteresting Places


<div id="feed_walkingMen" class="youtubeFeed"></div>
<script>
channels_walkingMen = [
  'UCUMQFUkgaEE68_ujIdW2wAw', // Dime Store Adventures
  'UCBa659QWEk1AI4Tg--mrJ2A', // Tom Scott
  'UCbCq5Y0WPGimG2jNXhoQxGw', // Atomic Frontier
  'UCbbQalJ4OaC0oQ0AqRaOJ9g', // Jay Foreman
  'UC2LVhJH_9cT2XKp0VAfsKOQ', // Tim Traveler
];
buildFeed(channels_walkingMen, "feed_walkingMen");
</script>




## Math

[3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw/videos?disable_polymer=1)
: Beautiful theorems

[Numberphile](https://www.youtube.com/user/numberphile/videos?disable_polymer=1)
: Videos about numbers

[Matt Parker](https://www.youtube.com/user/standupmaths/videos?disable_polymer=1)
: More videos about numbers. Took me a while to realize it's not the same channel as Numberphile.


<div id="feed_math" class="youtubeFeed"></div>
<script>
channels_math = [
  'UCYO_jab_esuFRV4b17AJtAw', // 3blue1brown
  'UCoxcjq-8xIDTYp3uz647V5A', // Numberphile
  'UCSju5G2aFaWMqn-_0YBtq5A', // Stand Up Maths
];
buildFeed(channels_math, "feed_math");  
</script>


<!--
[Vihart](https://www.youtube.com/user/Vihart/videos?disable_polymer=1)
: Math Doodles

[George Hart](https://www.youtube.com/channel/UCTl0dASnxto6j2wlVs5Bs2Q/videos?disable_polymer=1)
: Origami
-->


## Physics and Engineering

[engineerguy](https://www.youtube.com/user/engineerguyvideo/videos?disable_polymer=1)
: Elegant videos about everyday engineering marvels

<!--
[Illinois EnergyProf](https://www.youtube.com/channel/UCKH_iLhhkTyt8Dk4dmeCQ9w/videos?disable_polymer=1)
: Clear lectures from Professor David Ruzic
-->
[Steve Mould](https://www.youtube.com/user/steventhebrave/videos)
: Various Physics Visualizations

[Smarter Every Day](https://www.youtube.com/user/destinws2/videos)
: Dude makin' videos on all sorts of stuff that interests him.

[Practical Engineering](https://www.youtube.com/user/gradyhillhouse/videos)
: Small-scale demonstrations of civil engineering challenges

[Veritasium](https://www.youtube.com/user/1veritasium/videos)
: Assorted videos about science and education.



<div id="feed_engineering" class="youtubeFeed"></div>
<script>
channels_engineering = [
  'UCHnyfMqiRRG1u-2MsSQLbXA', // veritasium
  'UCMOqf8ab-42UUQIdVoKwjlQ', // Practical Engineering
  'UC6107grRI4m0o2-emgoDnAA', // Smarter Every Day
  'UCEIwxahdLz7bap-VDs9h35A', // Steve Mould
  'UC2bkHVIDjXS7sgrgjFtzOXQ', // Engineer Guy
];
buildFeed(channels_engineering, "feed_engineering");
</script>



## Biology
[Ben G Thomas](https://www.youtube.com/channel/UCDSzwZqgtJEnUzacq3ddoOQ/videos?disable_polymer=1)
: Dino news

[Trey the Explainer](https://www.youtube.com/user/GamerCreator12345/videos?disable_polymer=1)
: Paleontology speculation

[PBS Eons](https://www.youtube.com/channel/UCzR-rom72PHN9Zg7RML9EbA/videos?disable_polymer=1)
: Old timey animals 

[Tier Zoo](https://www.youtube.com/channel/UCHsRtomD4twRf5WVHHk-cMw/videos?disable_polymer=1)
: Talking about animals as if they were characters in a fighting game

[Shed Science](https://www.youtube.com/user/shedscience/videos)
:  

[Ze frank](https://www.youtube.com/user/zefrank1/videos)
: True facts about animals 

[Deep Look](https://www.youtube.com/user/KQEDDeepLook/videos?disable_polymer=1)
: Footage of small things


[Nautilus](https://www.youtube.com/user/EVNautilus/videos?disable_polymer=1)
: Deep Sea Livestreams

[Octolab TV](https://www.youtube.com/channel/UCNo_xQ7NvTr31naPAcjQWjg/videos?disable_polymer=1)
: Chill vids of little octodudes


<div id="feed_animals" class="youtubeFeed"></div>
<script>
channels_animals = [
  'UCDjdXwT-KrFPsqOSg4KL8Nw', // Leslie Bird Nerd
  'UCNo_xQ7NvTr31naPAcjQWjg', // OctoLab
  'UCDSzwZqgtJEnUzacq3ddoOQ', // Ben G Thomas
  'UCOuWeOkMrq84u5LY6apWQ8Q', // Trey the explainer
  'UCzR-rom72PHN9Zg7RML9EbA', // PBS Eons
  'UCHsRtomD4twRf5WVHHk-cMw', // Tier Zoo
  'UC9AUeAvdEVJfyS9rd9pvp8g', // Shed Science
  'UCVpankR4HtoAVtYnFDUieYA', // Ze Frank 
  'UC-3SbfTPJsL8fJAPKiVqBLg', // Deep Look
  'UC1KOOWHthbQVXH2kZue3_xA', // EV Nautilus
  'UC9Lp_AA5M2cMGrlvnnIns-g', // Bizarre Beasts
  //'', // 
];
buildFeed(channels_animals, "feed_animals");
</script>




## Space!
[Astrum](https://www.youtube.com/c/astrumspace/videos)
: Videos about the sensational weirdness of space. The titles are clickbaity, but the content is very good. For example, the author takes care to clearly indicate which footage is cgi, photoenhanced, etc. <!--I did notice in one video they confused "amines" for "amino acids"-->

[Anton Petrov](https://www.youtube.com/c/whatdamath/videos)
: Science discovery explainers, most space-related.


## Chemistry and Metallurgy and whatnot

[Periodic Videos](https://www.youtube.com/user/periodicvideos/videos?disable_polymer=1)
: Videos about all the elements

[Cody's Lab](https://www.youtube.com/user/theCodyReeder/videos?disable_polymer=1)
: Also features weird gardening experiments

[How to Make Everything](https://www.youtube.com/channel/UCfIqCzQJXvYj9ssCoHq327g/videos?disable_polymer=1)
: Was originally about making a sandwich completely from scratch. 

[Action Lab](https://www.youtube.com/@TheActionLab/videos)
: The titles are always clickbait, but the videos are still interesting.


<div id="feed_chemistry" class="youtubeFeed"></div>
<script>
channels_chemistry = [
  'UC1VLQPn9cYSqx8plbk9RxxQ', // Action Lab
  'UCu6mSoMNzHQiBIOCkHUa2Aw', // Cody's Lab
  'UCtESv1e7ntJaLJYKIO1FoYw', // Periodic Videos
  'UCfIqCzQJXvYj9ssCoHq327g', // How to Make Everything
  'UCA0mlN90EHCizvo101nbr-g', // Nile Red Shorts
  'UC1D3yD4wlPMico0dss264XA', // Nile Blue
  'UC1_kuFbEBdHtf7_c2wIdNVg', // Pyrotechnical
];
buildFeed(channels_chemistry, "feed_chemistry");  
</script>






## Food and Cookery

[Food Wishes](https://www.youtube.com/user/foodwishes/videos?disable_polymer=1)
: Straightforward recipe videos

[Binging with Babish](https://www.youtube.com/user/bgfilms/videos?disable_polymer=1)
: Mostly makes meme food

[Bon Appétit](https://www.youtube.com/user/BonAppetitDotCom/videos?view=0&sort=p&flow=grid)
: This is the one where they make gourmet skittles *

[Tasting History](https://www.youtube.com/c/TastingHistory/videos)
: Historically accurate recipes, along with discussion of adjacent history.

<div id="feed_food" class="youtubeFeed"></div>
<script>
channels_food = [
  'UC9_p50tH3WmMslWRWKnM7dQ', // Adam Ragusea
  'UCsaGKqPZnGp_7N80hcHySGQ', // Tasting history
  'UCJHA_jMfCvEnv-3kRjTCQXw', // Babish
  'UCRIZtPl9nb9RiXc9btSTQNw', // Food Wishes
  'UCJLKwTg0IaSMoq6hLHT3CAA', // Ordinary Sausage
];
buildFeed(channels_food, "feed_food");  
</script>



## Interesting Places



[Artifexian](https://www.youtube.com/user/Artifexian/videos)
: Strange exoplanets and advice about imagining them

[CGP Grey](https://www.youtube.com/user/CGPGrey/videos?disable_polymer=1)
: Mostly about flags and borders, but also about all sorts of stuff

[Worldbuilding Notes](https://www.youtube.com/channel/UCncTjqw75krp9j_wRRh5Gvw/videos?disable_polymer=1)
: Imaginary places








## Media Commentary

[YMS](https://www.youtube.com/user/YourMovieSucksDOTorg/videos?disable_polymer=1)
: His "Top Ten Films of 2015" list has 39 entries and was published in 2018.

[Red Letter Media](https://www.youtube.com/user/RedLetterMedia/videos?disable_polymer=1)
: Wisconsin's finest cultural output

[PBS Digital Studios](https://www.youtube.com/user/pbsdigitalstudios/videos?disable_polymer=1)
: See also Lindsay Ellis' [personal channel](https://www.youtube.com/user/chezapoctube/videos?disable_polymer=1) *

[Captain Disillusion](https://www.youtube.com/user/CaptainDisillusion/videos?disable_polymer=1)
: Like a 90s childrens science show, but about digital effects

[Jenny Nicholson](https://www.youtube.com/user/JennyENicholson/videos?disable_polymer=1)
: Why does she have so many porgs?

<div id="feed_film" class="youtubeFeed"></div>
<script>
channels_film = [
  'UCrTNhL_yO3tPTdQ5XgmmWjA', // red letter media
  'UCEOXxzW2vU0P-0THehuIIeg', // Captain D
  'UCSc16oMxxlcJSb9SXkjwMjA', // YMS 
  'UC7-E5xhZBZdW-8d7V80mzfg', // Jenny Nicholson
  'UCSUf5_EPEfl4zlBKZHkZdmw', // Danny Gonzales * 
  'UCTSRIY3GLFYIpkR2QwyeklA', // Drew Gooden *
  'UCZXAVdAplsu1tFZ9OqQhJFg', // Virtual Frog *
  'UCGeIjGngCkErevSNHdZYD5Q', // Expleen
];
buildFeed(channels_film, "feed_film");  
</script>




## Comedy

[Aunty Donna](https://www.youtube.com/user/TheAuntyDonnaChannel/videos?disable_polymer=1)
: Austrailian Sketch Comedy

[Jenna Marbles](https://www.youtube.com/user/JennaMarbles/videos?disable_polymer=1)
: I love her horrible dogs.

[The Dragon's Tomb](https://www.youtube.com/channel/UC3izYCSBcfi2LfdIr-qg0gQ/videos?disable_polymer=1)
: Completely accurate board game tutorials.

[Bill Wurtz](https://www.youtube.com/user/billwurtz/videos?disable_polymer=1)
: Music? 

[Let's Game it Out](https://www.youtube.com/channel/UCto7D1L-MiRoOziCXK9uT5Q/videos?disable_polymer=1)
: "As always, we're going to try to play this game as wrong as possible."

[Alex Ernst](https://www.youtube.com/user/TheAlexErnstShow/videos)
: Something something apple cider vinegar

<div id="feed_sketch" class="youtubeFeed"></div>
<script>
channels_sketch = [
  'UC_mneEC0wc29EGGmIsN_xLA', // Aunty Donna
  'UC7-E5xhZBZdW-8d7V80mzfg', // Jenny Nicholson
  'UC9gFih9rw0zNCK3ZtoKQQyA', // Jenna Marbles
  'UC3izYCSBcfi2LfdIr-qg0gQ', // Dragon's Tomb
  'UCq6aw03lNILzV96UvEAASfQ', // Bill Wurtz
  'UCWk68Uw6V990fjnTbcOHeoA', // Alex Ernst
  'UCv3mh2P-q3UCtR9-2q8B-ZA', // Urban Rescue Ranch *
  'UCto7D1L-MiRoOziCXK9uT5Q', // Game it Out
];
buildFeed(channels_sketch, "feed_sketch");  
</script>



## Interesting collections

[Grand Illusions](https://www.youtube.com/user/henders007/videos)
: Tim's Toy Collection

[Objectivity](https://www.youtube.com/channel/UCtwKon9qMt5YLVgQt1tvJKg/videos?disable_polymer=1)
: Old artifacts 





## Reviews of stuff

[Ashens](https://www.youtube.com/user/ashens/videos?disable_polymer=1)
: Reviews of dollar-store crud

[MKBHD](https://www.youtube.com/user/marquesbrownlee/videos?disable_polymer=1)
: Gizmos

[Questing Beast](https://www.youtube.com/channel/UCvYwePdbWSEwUa-Pk02u3Zw/videos?disable_polymer=1)
: Tabletop RPG Books






## Reviews of Board Games in particular

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






## Animated stuff

[Suncreature Studios](https://www.youtube.com/user/SunCreatureStudio/videos?disable_polymer=1)
: Animated adventure shorts.

[Sam O'Nella](https://www.youtube.com/channel/UC1DTYW241WD64ah5BFWn4JA/videos?disable_polymer=1)
: Honestly, it's more of a slideshow of crudely drawn stick figures.

[Explosm](https://www.youtube.com/user/ExplosmEntertainment/videos?disable_polymer=1)
: Depressing Stick Figure cartoons





## Making  Stuff

[Slingshot Channel](https://www.youtube.com/user/JoergSprave/videos)
: Strange Handmade Elastic-powered projectiles

[Pocket83](https://www.youtube.com/user/pocket83/videos?disable_polymer=1)
: Neat little doodads

[I Like To Make Stuff](https://www.youtube.com/user/iliketomakestuffcom/videos?disable_polymer=1)
: Woodworking





## Making Horrible Stuff

[William Osman](https://www.youtube.com/channel/UCfMJ2MchTSW2kWaT0kK94Yw/videos?disable_polymer=1)
: Reckless disregard for laser safety

[StyroPyro](https://www.youtube.com/user/styropyro/videos?disable_polymer=1)
: Nevermind. <i>This</i> is reckless disregard for laser safety 

[Michael Reeves](https://www.youtube.com/channel/UCtHaxi4GTYDpJgMSGy7AeSw/videos?disable_polymer=1)
: William Osman's angrier housemate 

[Simone Giertz](https://www.youtube.com/channel/UC3KEoMzNz8eYnwBC34RaKCQ/videos?disable_polymer=1)
: Queen of Shitty Robots *

[Electroboom](https://www.youtube.com/user/msadaghd/videos?disable_polymer=1)
: How not to do electrical engineering 

[Good Inventions](https://www.youtube.com/channel/UCoQBtJ24OUqB4O285xp9ZrQ/videos?disable_polymer=1)
: Very practical. Great Job.

[Tom Wildenhain](https://www.youtube.com/channel/UCgO8vdeWcywARd99Od-H_8A/videos?disable_polymer=1)
: Using MS Office to commit crimes against nature

[Ian Hubert](https://www.youtube.com/channel/mrdodobird/videos?disable_polymer=1)
: Blender Tutorials which are either awful or amazing. *



<div id="feed_jankyEngineering" class="youtubeFeed"></div>
<script>
channels_jankyEngineering = [
  'UCtHaxi4GTYDpJgMSGy7AeSw', // Michael Reeves
  'UCfMJ2MchTSW2kWaT0kK94Yw', // William Osman
  'UCVS89U86PwqzNkK2qYNbk5A', // Failed Mythbuster Allen Pan
  'UCoQBtJ24OUqB4O285xp9ZrQ', // Good Inventions
  'UCJLZe_NoiG0hT7QCX_9vmqw', // I did a Thing
  'UCJYJgj7rzsn0vdR7fkgjuIA', // StopPyro
  'UCVovvq34gd0ps5cVYNZrc7A', // Explosions and Fire
  'UCgO8vdeWcywARd99Od-H_8A', // Rom Wildenhain
  'UCB4NFn-8oipHct0IfAQBQrQ', // Unnecessary Inventions *
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

