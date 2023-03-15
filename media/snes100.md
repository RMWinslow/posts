---
title: SNES Top 100
subtitle: "A rank-aggregation of several lists of Top 100 Super Nintendo Games."
parent: Media Recommendations
grand_parent: Art and Culture
nav_exclude: true
layout: post
date: 2023-03-09
---

Below are some lists of the best 100 games for the Super Nintendo,
made by aggregating several other top 100 lists.

(I don't go into any detail about the games here.
I did this just to play around with some rank aggregation algorithms.)

## The Combined Rankings

Each Column uses a different metric to aggregate the rankings.


| Borda Count                                      | Copeland                                         | Tideman (unstable)                               | Geo Mean                                         | Arith Mean                                       |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|
| Legend of Zelda: A Link to the Past              | Legend of Zelda: A Link to the Past              | Legend of Zelda: A Link to the Past              | Legend of Zelda: A Link to the Past              | Legend of Zelda: A Link to the Past              |
| Super Mario World                                | Super Mario World                                | Super Mario World                                | Super Mario World                                | Super Mario World                                |
| Super Metroid                                    | Chrono Trigger                                   | Chrono Trigger                                   | Super Metroid                                    | Super Metroid                                    |
| Chrono Trigger                                   | Super Metroid                                    | Super Metroid                                    | Chrono Trigger                                   | Chrono Trigger                                   |
| Yoshi's Island                                   | Final Fantasy III                                | Final Fantasy III                                | EarthBound                                       | Yoshi's Island                                   |
| EarthBound                                       | Yoshi's Island                                   | Yoshi's Island                                   | Yoshi's Island                                   | EarthBound                                       |
| Secret of Mana                                   | EarthBound                                       | Super Mario RPG                                  | Final Fantasy III                                | Secret of Mana                                   |
| Super Mario Kart                                 | Super Mario RPG (TIE)                            | EarthBound                                       | Super Mario Kart                                 | Super Mario Kart                                 |
| Donkey Kong Country                              | Super Mario Kart                                 | Super Mario Kart                                 | Super Mario RPG                                  | Donkey Kong Country                              |
| Teenage Mutant Ninja Turtles IV: Turtles in Time | Super Mario All-Stars (TIE)                      | Super Mario All-Stars                            | Super Mario All-Stars                            | Teenage Mutant Ninja Turtles IV: Turtles in Time |
| Mega Man X                                       | Mega Man X                                       | Mega Man X                                       | Mega Man X                                       | Mega Man X                                       |
| Super Castlevania IV                             | Donkey Kong Country                              | Donkey Kong Country 2                            | Secret of Mana                                   | Super Mario All-Stars                            |
| Contra III: The Alien Wars                       | Donkey Kong Country 2 (TIE)                      | Donkey Kong Country                              | Teenage Mutant Ninja Turtles IV: Turtles in Time | Super Castlevania IV                             |
| Star Fox                                         | Teenage Mutant Ninja Turtles IV: Turtles in Time | Teenage Mutant Ninja Turtles IV: Turtles in Time | Donkey Kong Country                              | Contra III: The Alien Wars                       |
| F-Zero                                           | Secret of Mana                                   | Secret of Mana                                   | Donkey Kong Country 2                            | Super Mario RPG                                  |
| ActRaiser                                        | Street Fighter II Turbo                          | Super Castlevania IV                             | Street Fighter II Turbo                          | Star Fox                                         |
| Kirby Super Star                                 | Super Castlevania IV                             | Contra III: The Alien Wars                       | Super Castlevania IV                             | Donkey Kong Country 2                            |
| Super Mario All-Stars                            | Contra III: The Alien Wars                       | Final Fantasy II                                 | Contra III: The Alien Wars                       | F-Zero                                           |
| Illusion of Gaia                                 | Final Fantasy II (TIE)                           | Street Fighter II Turbo                          | Star Fox                                         | Street Fighter II Turbo                          |
| Breath of Fire II                                | Star Fox                                         | Star Fox                                         | Final Fantasy II                                 | ActRaiser                                        |
| Zombies Ate My Neighbors                         | F-Zero                                           | F-Zero                                           | F-Zero                                           | Final Fantasy III                                |
| Harvest Moon                                     | Mortal Kombat II                                 | Mega Man X2                                      | Mega Man X2                                      | Kirby Super Star                                 |
| Tetris Attack                                    | Kirby Super Star                                 | ActRaiser                                        | Mortal Kombat II                                 | Mega Man X2                                      |
| SimCity                                          | Mega Man X2                                      | Mortal Kombat II                                 | Kirby Super Star                                 | Mortal Kombat II                                 |
| Ogre Battle                                      | Super Punch-Out (TIE)                            | Super Punch-Out                                  | ActRaiser                                        | Final Fantasy II                                 |
| Mega Man X2                                      | ActRaiser                                        | Kirby Super Star                                 | Super Punch-Out                                  | Super Punch-Out                                  |
| Super Bomberman                                  | Lufia II: Rise of the Sinistrals                 | Zombies Ate My Neighbors                         | Lufia II: Rise of the Sinistrals                 | Illusion of Gaia                                 |
| Mortal Kombat II                                 | Breath of Fire II                                | Lufia II: Rise of the Sinistrals                 | Illusion of Gaia                                 | Breath of Fire II                                |
| Sunset Riders (TIE)                              | Zombies Ate My Neighbors                         | Breath of Fire II                                | Breath of Fire II                                | Lufia II: Rise of the Sinistrals                 |
| Demon's Crest                                    | Illusion of Gaia                                 | Illusion of Gaia                                 | Tetris Attack                                    | Zombies Ate My Neighbors                         |
| Killer Instinct                                  | Tetris Attack                                    | Harvest Moon                                     | Terranigma                                       | Harvest Moon                                     |
| Super Mario RPG                                  | Terranigma                                       | Super Bomberman                                  | Harvest Moon                                     | Tetris Attack                                    |
| Donkey Kong Country 2                            | Harvest Moon                                     | Terranigma                                       | Final Fantasy VI                                 | SimCity                                          |
| Lufia II: Rise of the Sinistrals                 | SimCity (TIE)                                    | Tetris Attack                                    | Zombies Ate My Neighbors                         | Ogre Battle                                      |
| Street Fighter II Turbo[^sffoot]                 | Ogre Battle                                      | Ogre Battle                                      | Soul Blazer                                      | Super Bomberman                                  |
| Secret of Evermore                               | Super Bomberman                                  | Soul Blazer                                      | SimCity                                          | Secret of Evermore                               |
| Super Ghouls n Ghosts                            | Secret of Evermore (TIE)                         | Super Ghouls n Ghosts                            | Super Bomberman                                  | Sunset Riders                                    |
| Shadowrun                                        | Super Ghouls n Ghosts                            | Sunset Riders                                    | Ogre Battle                                      | Super Ghouls n Ghosts (TIE)                      |
| Mega Man X3 (TIE)                                | Sunset Riders                                    | Secret of Evermore                               | Sunset Riders                                    | Demon's Crest                                    |
| Super Punch-Out                                  | Soul Blazer                                      | SimCity                                          | Donkey Kong Country 3                            | Terranigma                                       |
| UN Squadron (TIE)                                | Legend of the Mystical Ninja (TIE)               | Legend of the Mystical Ninja                     | Secret of Evermore                               | Killer Instinct                                  |
| Legend of the Mystical Ninja                     | Donkey Kong Country 3 (TIE)                      | NBA Jam                                          | Super Ghouls n Ghosts                            | Soul Blazer                                      |
| Breath of Fire                                   | Super Street Fighter II                          | Super Street Fighter II                          | Super Street Fighter II                          | Shadowrun                                        |
| Gradius III                                      | UN Squadron                                      | Demon's Crest                                    | Legend of the Mystical Ninja                     | Mega Man X3 (TIE)                                |
| Final Fantasy III                                | Demon's Crest                                    | Donkey Kong Country 3                            | Shadowrun                                        | UN Squadron                                      |
| Final Fantasy II                                 | Killer Instinct                                  | Mega Man X3                                      | Demon's Crest                                    | Legend of the Mystical Ninja                     |
| Soul Blazer                                      | Mega Man X3                                      | Shadowrun                                        | Breath of Fire                                   | Donkey Kong Country 3                            |
| NBA Jam                                          | Shadowrun                                        | UN Squadron                                      | Mega Man X3                                      | Breath of Fire (TIE)                             |
| R-Type III                                       | Breath of Fire                                   | Killer Instinct                                  | UN Squadron                                      | Super Street Fighter II                          |
| PilotWings                                       | NBA Jam                                          | Lost Vikings                                     | Killer Instinct                                  | NBA Jam                                          |
| Donkey Kong Country 3                            | Gradius III                                      | Wild Guns                                        | NBA Jam                                          | Gradius III                                      |
| Uniracers                                        | R-Type III                                       | EVO                                              | Final Fantasy IV                                 | R-Type III                                       |
| Earthworm Jim                                    | PilotWings                                       | Breath of Fire                                   | R-Type III                                       | Earthworm Jim                                    |
| Terranigma                                       | Earthworm Jim                                    | Gradius III                                      | Wild Guns                                        | PilotWings                                       |
| Rock n Roll Racing                               | EVO                                              | R-Type III                                       | Earthworm Jim                                    | Wild Guns                                        |
| Lost Vikings                                     | Rock n Roll Racing (TIE)                         | Mario Paint                                      | Gradius III                                      | Mario Paint                                      |
| EVO                                              | Lost Vikings                                     | Earthworm Jim                                    | Super Mario RPG: Legend of the Seven Stars       | Final Fantasy VI                                 |
| Super Street Fighter II                          | Mario Paint                                      | Aladdin                                          | PilotWings                                       | Rock n Roll Racing                               |
| The Adventures of Batman and Robin               | Aladdin                                          | Rock n Roll Racing                               | Mario Paint                                      | Kirby's Dream Land 3                             |
| Wild Guns                                        | Kirby's Dream Land 3 (TIE)                       | PilotWings                                       | Trials of Mana                                   | Lost Vikings                                     |
| Mario Paint                                      | Wild Guns (TIE)                                  | Street Fighter II                                | Street Fighter II                                | Street Fighter II                                |
| Kirby's Dream Land 3                             | Ultimate Mortal Kombat 3 (TIE)                   | Ultimate Mortal Kombat 3                         | Kirby's Dream Land 3                             | EVO                                              |
| Ultimate Mortal Kombat 3                         | Super Bomberman 2                                | Kirby's Dream Land 3                             | Final Fantasy V                                  | Ultimate Mortal Kombat 3                         |
| Super Bomberman 2                                | Final Fantasy V                                  | Super Bomberman 2                                | Ultimate Mortal Kombat 3                         | Final Fantasy IV                                 |
| Aladdin                                          | Street Fighter II                                | The Adventures of Batman and Robin               | Lost Vikings                                     | Final Fantasy V                                  |
| Cybernator                                       | Uniracers (TIE)                                  | Axelay                                           | Axelay                                           | Trials of Mana                                   |
| Spider-Man and Venom: Maximum Carnage            | The Adventures of Batman and Robin (TIE)         | Final Fantasy V                                  | Rock n Roll Racing                               | Super Bomberman 2                                |
| Mega Man 7                                       | Axelay                                           | Goof Troop                                       | Aladdin                                          | The Adventures of Batman and Robin               |
| Super Star Wars                                  | Spider-Man and Venom: Maximum Carnage            | Cybernator                                       | NBA Jam: Tournament Edition                      | Aladdin (TIE)                                    |
| Street Fighter Alpha 2                           | Super Star Wars (TIE)                            | Super Star Wars                                  | EVO                                              | Axelay                                           |
| Final Fight                                      | Mega Man 7                                       | Uniracers                                        | Super Bomberman 2                                | NBA Jam: Tournament Edition                      |
| Final Fantasy: Mystic Quest                      | Cybernator (TIE)                                 | Super Smash TV                                   | The Adventures of Batman and Robin               | Cybernator                                       |
| Super Double Dragon                              | NBA Jam: Tournament Edition                      | Mega Man 7                                       | Spider-Man and Venom: Maximum Carnage            | Spider-Man and Venom: Maximum Carnage            |
| Castlevania: Dracula X                           | Street Fighter Alpha 2                           | Flashback                                        | Super Turrican 2                                 | Mega Man 7                                       |
| Street Fighter II                                | Goof Troop                                       | Spider-Man and Venom: Maximum Carnage            | Tetris and Dr. Mario                             | Uniracers                                        |
| Final Fantasy V                                  | Super Double Dragon                              | Super Double Dragon                              | Fire Emblem: Genealogy of the Holy War           | Tetris and Dr. Mario                             |
| Axelay                                           | Final Fight (TIE)                                | NBA Jam: Tournament Edition                      | Lufia and the Fortress of Doom                   | Goof Troop                                       |
| Goof Troop                                       | Trials of Mana (TIE)                             | Final Fantasy: Mystic Quest                      | Mega Man 7                                       | Super Star Wars                                  |
| Super Smash TV                                   | Super Smash TV                                   | Street Fighter Alpha 2                           | Cybernator                                       | Lufia and the Fortress of Doom                   |
| Flashback                                        | Castlevania: Dracula X                           | Castlevania: Dracula X                           | Super Star Wars                                  | Super Turrican 2                                 |
| Sparkster                                        | Final Fantasy: Mystic Quest                      | Trials of Mana                                   | The Magical Quest Starring Mickey Mouse          | Street Fighter Alpha 2                           |
| NHL 94                                           | Flashback                                        | Tetris and Dr. Mario                             | Goof Troop                                       | Super Mario RPG: Legend of the Seven Stars       |
| Trials of Mana                                   | Tetris and Dr. Mario                             | Super Turrican 2                                 | Uniracers                                        | Final Fight 3                                    |
| Batman Returns                                   | Final Fight 3                                    | Final Fight 3                                    | International Superstar Soccer Deluxe            | Super Smash TV (TIE)                             |
| Ken Griffey Jr Presents Major League Baseball    | Lufia and the Fortress of Doom                   | Final Fight                                      | Street Fighter Alpha 2                           | The Magical Quest Starring Mickey Mouse          |
| NBA Jam: Tournament Edition                      | Final Fantasy VI                                 | Super R-Type                                     | Space Megaforce                                  | International Superstar Soccer Deluxe            |
| Tetris and Dr. Mario                             | Super Turrican 2 (TIE)                           | International Superstar Soccer Deluxe            | Super Smash TV                                   | Space Megaforce (TIE)                            |
| Lufia and the Fortress of Doom                   | Batman Returns (TIE)                             | New Horizons                                     | Super Star Wars: Return of the Jedi              | Flashback                                        |
| Super Turrican 2                                 | The Magical Quest Starring Mickey Mouse (TIE)    | Tecmo Super Bowl                                 | Final Fight                                      | Final Fight (TIE)                                |
| Final Fight 3                                    | Final Fantasy IV                                 | Ken Griffey Jr Presents Major League Baseball    | Super Star Wars: The Empire Strikes Back         | Fire Emblem: Genealogy of the Holy War           |
| The Magical Quest Starring Mickey Mouse          | Space Megaforce                                  | Final Fantasy VI                                 | Donkey Kong Country 2: Diddy's Kong Quest        | Super Star Wars: Return of the Jedi              |
| Space Megaforce                                  | Sparkster (TIE)                                  | Space Megaforce                                  | Final Fight 3                                    | Battletoads in Battlemaniacs                     |
| International Superstar Soccer Deluxe (TIE)      | Kirby's Dream Course                             | Final Fantasy IV                                 | Street Fighter II: The World Warrior             | Kirby's Avalanche                                |
| Super Star Wars: Return of the Jedi              | Super Star Wars: Return of the Jedi              | The Magical Quest Starring Mickey Mouse          | Flashback                                        | Kirby's Dream Course                             |
| Battletoads in Battlemaniacs                     | NHL 94 (TIE)                                     | Kirby's Avalanche                                | Battletoads in Battlemaniacs                     | Final Fantasy: Mystic Quest                      |
| Kirby's Avalanche                                | New Horizons                                     | Lufia and the Fortress of Doom                   | Kirby's Avalanche                                | Super Star Wars: The Empire Strikes Back (TIE)   |
| Kirby's Dream Course                             | Battletoads in Battlemaniacs (TIE)               | Sparkster                                        | Hagane                                           | Sparkster                                        |
| Super Star Wars: The Empire Strikes Back         | International Superstar Soccer Deluxe (TIE)      | Battletoads in Battlemaniacs                     | Kirby's Dream Course                             | Pocky and Rocky (TIE)                            |
| Final Fantasy VI                                 | Mortal Kombat 3                                  | Pocky and Rocky                                  | Street Fighter II' Turbo: Hyper Fighting         | Hagane                                           |
| Metal Warriors                                   | Top Gear                                         | Hagane                                           | Pocky and Rocky                                  | Super Double Dragon                              |


(Nothing super chaotic going on near the top between rankings, as *Link to the Past* is the Candorcet winner, and has a plurality of #1 slots.)


## The Source Lists

Some of these sources have more than 100 games listed. 

- [Retro-Sanctuary](https://www.retro-sanctuary.com/Top-100-SNES-Games-Page-1.html)
- [IGN](https://www.ign.com/lists/top-100-snes-games/100)
- [Ranker](https://www.ranker.com/crowdranked-list/best-super-nintendo-_snes_-games), retrieved 2023-03-09
- [Complex](https://www.complex.com/pop-culture/the-100-best-super-nintendo-games)
- [Gamefaqs 1](https://gamefaqs.gamespot.com/boards/916396-super-nintendo/76022917)
- [Gamefaqs 2](https://gamefaqs.gamespot.com/boards/916396-super-nintendo/78764676)
- [Reddit](https://www.reddit.com/r/snes/comments/l7yzdc/the_snes_subreddit_top_100_games_of_all_time/)
- [Sydlexia](http://www.sydlexia.com/top100snes.htm)
- [Nintendo Life, User Ratings](https://www.nintendolife.com/games/browse?sort=rating&style=table&system=snes), retrieved 2023-03-09
- [Nintendo Life, Popularity](https://www.nintendolife.com/games/browse?sort=popular&system=snes&style=table), retrieved 2023-03-09

It's also worth noting that some of these source lists are themselves the aggregate rankings of many people.
So this isn't the most conceptually sound exercise. 
But ah well, I had fun. 

<!--TODO: More details about algorithms, especially my complaints about Schulze.-->


[^sffoot]: As I found out during de-duplication of the data, Street Fighter II Turbo, Super Street Fighter II, Street Fighter II, and Street Fighter Alpha 2 are all apparently seperate games.
