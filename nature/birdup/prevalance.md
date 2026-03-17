---
title: "Bird Scores - Prevalence"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
math: katex
---


This BIRDUP scoring system is incredibly simple, simply ranking birds by their prevalence of observations within a state.

$$\gdef\nBird{🦃}
\gdef\nState{🗽}
\gdef\nTotal{N}
\gdef\nJoint{📋}$$

It uses observation records from the eBird database[^ebirdcitation].
Each observation is for a specific species of bird in a specific state.
- Let $N$ be the total number of observations in the data.
- Let $\nBird$ be the total number of observations of a specific bird species or genus.
- Let $\nState$ be the total number of observations taking place in a specific state.
- Let $\nJoint$ be the the joint observation count: the total number of observations of that specific type of bird in that specific state.

Here, the Bird Score for a pair of state and bird is simply

$$\text{prevalence} = \frac{\nJoint}{\nState}$$

Note that this is not the same as determining which bird is most populous within the state. 
Firstly, I'm counting the number of observation records of each type of bird.
Someone sees a flock of 1000 sparrows? That's one observation record.
Someone sees a single Eagle? One observation record.
Secondly, these records come from voluntary observations, not some careful bird census.
There's a bias towards records of birds that live near people and which people actually care enough about to jot down.
So you can think of this metric as measuring which type of bird people most commonly notice.

<details closed markdown="block">
  <summary>
    Table of contents
  </summary>
- TOC
{:toc}
</details>

In the tables below, `†` indicates that the bird genus is represented among actual state birds.  
`‡` indicates that the bird is the actual state bird for that state.  
`＊` indicates a bird that is non-native and so excluded it form. A lack of `*` does not necessarily mean the bird *is* native.

[^ebirdcitation]: eBird Basic Dataset. Version: EBD_relSep-2021. Cornell Lab of Ornithology, Ithaca, New York. Sep 2021.


















## Scores for Bird Genera

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name | Example Species | Common Name |
|--:|---|---|---|---|---|
| AK | 0.0463 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| AL | 0.0386 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| AR | 0.0315 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| AZ | 0.0414 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| CA | 0.0224 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| CO | 0.0250 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| CT | 0.0082 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |
| DC | 0.0375 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| DE | 0.0231 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| FL | 0.0437 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| GA | 0.0282 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| HI | 0.0378 | [Pluvialis](https://en.wikipedia.org/wiki/Pluvialis) | Plover | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover |
| IA | 0.0135 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| ID | 0.0317 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| IL | 0.0118 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |
| IN | 0.0086 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| KS | 0.0151 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| KY | 0.0204 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| LA | 0.0333 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| MA | 0.0313 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| MD | 0.0096 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| ME | 0.0648 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| MI | 0.0107 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| MN | 0.0388 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| MO | 0.0307 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| MS | 0.0160 | [Charadrius](https://en.wikipedia.org/wiki/Charadrius) | Plover | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| MT | 0.0292 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| NC | 0.0324 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| ND | 0.0231 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | [Spizella passerina](https://en.wikipedia.org/wiki/Spizella_passerina) | Chipping Sparrow |
| NE | 0.0223 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |
| NH | 0.0415 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| NJ | 0.0110 | [Nannopterum](https://en.wikipedia.org/wiki/Nannopterum) | Cormorant | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant |
| NM | 0.0347 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| NV | 0.0184 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| NY | 0.0262 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| OH | 0.0112 | [Tachycineta](https://en.wikipedia.org/wiki/Tachycineta) | Swallow | [Tachycineta bicolor](https://en.wikipedia.org/wiki/Tachycineta_bicolor) | Tree Swallow |
| OK | 0.0215 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| OR | 0.0214 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow |
| PA | 0.0167 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| RI | 0.0640 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| SC | 0.0182 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| SD | 0.0257 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| TN | 0.0272 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| TX | 0.0259 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| UT | 0.0158 | [Falco](https://en.wikipedia.org/wiki/Falcon) | Falcon | [Falco sparverius](https://en.wikipedia.org/wiki/Falco_sparverius) | American Kestrel |
| VA | 0.0110 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| VT | 0.0489 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| WA | 0.0233 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| WI | 0.0115 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | 0.0227 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | [Vireo olivaceus](https://en.wikipedia.org/wiki/Vireo_olivaceus) | Red-eyed Vireo |
| WY | 0.0256 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |





### Top Genera for Alaska (AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0622 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 293920 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  |
| 0.0463 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 219036 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0391 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 184871 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0341 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 160956 | [Calidris mauri](https://en.wikipedia.org/wiki/Calidris_mauri) | Western Sandpiper |
| 0.0247 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 116656 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0243 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 114756 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0226 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 106945 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0204 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 96452 | [Gavia pacifica](https://en.wikipedia.org/wiki/Gavia_pacifica) | Pacific Loon |
| 0.0202 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 95229 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0186 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 87674 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |






### Top Genera for Alabama (AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0474 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 205713 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0386 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 167600 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0323 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 140224 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0301 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0293 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 127153 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0293 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 127076 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0286 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 124298 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0280 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 121684 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0250 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 108375 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0234 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 101378 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |






### Top Genera for Arkansas (AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0385 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 133523 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0377 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 130691 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0327 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 113337 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0315 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 109252 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0294 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 101947 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0283 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 98316 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0269 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 93388 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0263 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0251 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 87167 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0237 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 82265 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |






### Top Genera for Arizona (AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0414 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 916998 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0281 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 623372 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| 0.0277 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 613686 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0263 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 581985 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0240 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 533075 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch |
| 0.0204 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 451457 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0191 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 422574 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| 0.0188 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 417035 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0177 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 393373 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0175 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 388898 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee |






### Top Genera for California (CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0309 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 330232 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull |
| 0.0266 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 284405 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0261 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 278978 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0224 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 239921 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| 0.0222 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 237545 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0220 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 235347 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0210 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 224363 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0201 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 214464 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch |
| 0.0192 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 205154 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow |
| 0.0180 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 192248 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |






### Top Genera for Colorado (CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0320 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 567517 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0315 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 559548 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0302 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 535029 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0290 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 514016 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0263 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 467084 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0255 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 453161 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0253 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 448505 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0250 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 443193 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0239 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 423448 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0218 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |






### Top Genera for Connecticut (CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0346 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 350968 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0334 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 339172 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0324 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 328137 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0302 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 305895 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0298 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 302089 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0292 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 295889 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0288 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 292446 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0272 | [Turdus](https://en.wikipedia.org/wiki/Turdus)‡ | Robin | 275836 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0272 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 275510 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0268 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 272075 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |






### Top Genera for District of Columbia (DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0455 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 75508 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0447 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 74079 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0375 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 62170 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0348 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 57641 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0325 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 53975 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0290 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 48088 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |
| 0.0269 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 44628 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0267 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 44202 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0259 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0257 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 42675 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |






### Top Genera for Delaware (DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0330 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 144722 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |
| 0.0272 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 118924 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0266 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 116557 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0261 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 114527 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0242 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 105825 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0231 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 101378 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0229 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 100524 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0217 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 94945 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0211 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 92301 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0206 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 90088 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for Florida (FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0590 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 2139095 | [Setophaga palmarum](https://en.wikipedia.org/wiki/Setophaga_palmarum) | Palm Warbler |
| 0.0437 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 1584817 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| 0.0391 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 1419010 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0278 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 1009671 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle |
| 0.0275 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 995521 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0273 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 988708 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0264 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 956807 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| 0.0257 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 933160 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0230 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 833895 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0206 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 748541 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |






### Top Genera for Georgia (GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0531 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 659981 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0384 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 477796 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0327 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 406624 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0318 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0304 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 377667 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0283 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 351685 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0282 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 349899 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| 0.0278 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 345328 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0267 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 332445 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0256 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 317902 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for Hawaii (HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0614 | [Acridotheres](https://en.wikipedia.org/wiki/Acridotheres)* | Myna | 89440 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis) | Common Myna |
| 0.0569 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)* | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus) |  |
| 0.0538 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)* |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata) |  |
| 0.0434 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 63162 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| 0.0389 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata) |  |
| 0.0378 | [Pluvialis](https://en.wikipedia.org/wiki/Pluvialis) | Plover | 55064 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover |
| 0.0336 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 48950 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0334 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 48637 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0321 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 46683 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0312 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 45468 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Genera for Iowa (IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0321 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 108897 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0317 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 107540 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0305 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 103673 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0288 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 97621 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0262 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 88772 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0261 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 88459 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0259 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 88043 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0256 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 86938 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0241 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))‡ | Goldfinch | 81782 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0238 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 80952 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |






### Top Genera for Idaho (ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0336 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 150663 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0317 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 141997 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0314 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 140857 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0303 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 135819 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0301 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 135049 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0264 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0251 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 112667 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0247 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 110631 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0241 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 107964 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0226 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 101092 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |






### Top Genera for Illinois (IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0376 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 751287 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0326 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 650537 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0319 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 637278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0280 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 559040 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0264 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 528181 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0260 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 520240 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0258 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 515114 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0250 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 499718 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0238 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 476537 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0232 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 464431 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |






### Top Genera for Indiana (IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0350 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 355976 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0345 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 350530 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0321 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 326501 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0277 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 282027 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0272 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 276324 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0260 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 263938 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0259 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 263089 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0255 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 259597 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0253 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 257325 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0248 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 252542 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |






### Top Genera for Kansas (KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0282 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 171934 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0264 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 160741 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0244 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 148709 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0240 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 146299 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0238 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 145143 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0232 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 140986 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0215 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 131035 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0214 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 130040 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0206 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 125490 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0198 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 120685 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |






### Top Genera for Kentucky (KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0384 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 158980 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0361 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 149416 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0309 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 127779 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0295 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 121971 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0293 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 121431 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0273 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 113183 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0270 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 111602 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0264 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 109288 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0262 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 108517 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0255 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 105736 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Louisiana (LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0374 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 250924 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0333 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 223799 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0278 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 186708 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0274 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 184043 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0256 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 171844 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0246 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 165039 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0245 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 164645 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0241 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 162215 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0199 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 133581 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0188 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 126615 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |






### Top Genera for Massachusetts (MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0408 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 953627 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0390 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 911865 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0313 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 731554 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0301 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 704121 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0300 | [Poecile](https://en.wikipedia.org/wiki/Poecile)‡ | Chickadee | 702495 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0292 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 682228 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0291 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 679947 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0285 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 667120 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0273 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 638712 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0268 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 626570 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Genera for Maryland (MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0382 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 775958 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0336 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 681139 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0324 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 657192 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0268 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0245 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 497529 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0238 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 481971 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0237 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 480019 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0236 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 478998 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0230 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 466148 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0224 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 454993 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |






### Top Genera for Maine (ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0648 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 593940 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0513 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 470161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0450 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 412406 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0345 | [Poecile](https://en.wikipedia.org/wiki/Poecile)‡ | Chickadee | 316366 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0309 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 283461 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0297 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 272283 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0277 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 253820 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0267 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 245049 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0266 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 243841 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0252 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 230965 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for Michigan (MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0379 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 838775 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0320 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 706919 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0304 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 673380 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0299 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 661443 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0295 | [Turdus](https://en.wikipedia.org/wiki/Turdus)‡ | Robin | 653561 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0291 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 644482 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0281 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 621634 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0278 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 614337 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0268 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 592620 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0265 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 586777 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |






### Top Genera for Minnesota (MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0409 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 459935 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0398 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 448373 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0388 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 436581 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0374 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 420879 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0299 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 336940 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0293 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 329350 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0281 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 315782 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0276 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 311082 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0275 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 309216 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0245 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 275994 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |






### Top Genera for Missouri (MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0366 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 328095 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0307 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 275131 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0276 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 247494 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0276 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 247328 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0269 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 241056 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0255 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 228335 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0254 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 227981 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0246 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 220221 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0239 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 214458 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0234 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 209758 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Mississippi (MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0383 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 98694 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0323 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 83150 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0314 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 80897 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0283 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 72864 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0278 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 71468 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0271 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 69862 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0259 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 66564 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0244 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 62910 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0224 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 57768 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0183 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 47154 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |






### Top Genera for Montana (MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0353 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 183518 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0343 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 178038 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0317 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 164826 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0313 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 162796 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0292 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0249 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 129452 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0245 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 127361 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0237 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 123216 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0221 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 114578 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0218 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 113045 | [Spinus pinus](https://en.wikipedia.org/wiki/Spinus_pinus) | Pine Siskin |






### Top Genera for North Carolina (NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0489 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 731283 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0374 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 559762 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0358 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 535006 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0324 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0310 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 464196 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0279 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 416651 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0264 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 394475 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0259 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 386900 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0251 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 375697 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0232 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 347236 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for North Dakota (ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0354 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 74444 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0269 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 56654 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0257 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 54140 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0233 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 49058 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0231 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 48522 | [Spizella passerina](https://en.wikipedia.org/wiki/Spizella_passerina) | Chipping Sparrow |
| 0.0230 | [Aythya](https://en.wikipedia.org/wiki/Aythya) | Diving Duck | 48347 | [Aythya americana](https://en.wikipedia.org/wiki/Aythya_americana) | Redhead |
| 0.0229 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 48107 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0222 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 46662 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0220 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 46320 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0214 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 45002 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |






### Top Genera for Nebraska (NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0362 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 103158 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0283 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 80755 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0248 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 70609 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0246 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 70284 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0244 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 69715 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0244 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 69662 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0242 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 69060 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0230 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 65703 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0223 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 63727 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0223 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 63494 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |






### Top Genera for New Hampshire (NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0584 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 285427 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0415 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 202762 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0387 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 188968 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0372 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 182017 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0358 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 174912 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0334 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 163229 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0313 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 152843 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0290 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 141809 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0269 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 131473 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0242 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 118294 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for New Jersey (NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0407 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 839718 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0368 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 759061 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0295 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 607721 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0260 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 536449 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0254 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 524752 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0238 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 491469 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0231 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 477350 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0230 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 474951 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0227 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 468748 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0206 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 425901 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for New Mexico (NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0393 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 293725 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0389 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 291113 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0347 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 259544 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0283 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 211201 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch |
| 0.0255 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 190879 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0209 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 155963 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe |
| 0.0208 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 155739 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0206 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 154356 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0201 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 150197 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0189 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 141525 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |






### Top Genera for Nevada (NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0308 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 89198 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0260 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 75350 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0248 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 71735 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0237 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 68660 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0236 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 68449 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0195 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 56573 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow |
| 0.0194 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 56076 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0186 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 53746 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch |
| 0.0184 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | 53207 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| 0.0169 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |






### Top Genera for New York (NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0414 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 1663565 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0356 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 1430945 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |
| 0.0326 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 1310063 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0293 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 1176486 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0288 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 1158294 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0286 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 1147961 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0279 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 1120243 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0278 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 1117636 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0277 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 1115253 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0262 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 1053772 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |






### Top Genera for Ohio (OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0455 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 1106472 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0325 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 791329 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0298 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 724685 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0279 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 677794 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0278 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 674748 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0273 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 663248 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0246 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 598486 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0240 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 583159 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0239 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 581539 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0239 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 581511 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for Oklahoma (OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0328 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 107273 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0309 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 101166 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0281 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 92077 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0250 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 81840 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0239 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 78038 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0224 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 73163 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0221 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 72196 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0219 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 71695 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0215 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0214 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 69853 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |






### Top Genera for Oregon (OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0353 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 690822 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0322 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 630532 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0302 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 590649 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0297 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 580962 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0288 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 563713 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0256 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 501562 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0229 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 448962 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0219 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 429488 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0218 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 427331 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0214 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 418194 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow |






### Top Genera for Pennsylvania (PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0379 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 1038146 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0350 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 959157 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0346 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 947363 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0319 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 874142 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0316 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 864555 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0305 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 836000 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0302 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 828162 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0297 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 812703 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0268 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 733734 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0247 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 677538 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |






### Top Genera for Rhode Island (RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0640 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 134161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0328 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 68888 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0320 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 67053 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0282 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 59098 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0277 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 58142 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0262 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 55041 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0240 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 50314 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0236 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 49501 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0232 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 48648 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0210 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 44049 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for South Carolina (SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0471 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 396109 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0368 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 309495 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0337 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 283585 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0299 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)‡ | Carolina Wren | 251184 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0287 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 241432 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0275 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 230968 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0271 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 227590 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0257 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 215627 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0253 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 212440 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0233 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 195795 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |






### Top Genera for South Dakota (SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0314 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 45321 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0307 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 44203 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0257 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 37111 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0234 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 33659 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0230 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 33100 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0229 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 32984 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0213 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 30633 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0210 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 30259 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |
| 0.0208 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 29980 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0203 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 29193 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |






### Top Genera for Tennessee (TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0400 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 354544 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0374 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 331627 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0315 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 279190 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0299 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 264864 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0298 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0289 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 256273 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0272 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 241408 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0264 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 234257 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0263 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 233234 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0258 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 229026 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |






### Top Genera for Texas (TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0375 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 1669430 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0287 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 1274534 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0263 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 1167665 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0259 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 1153435 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0251 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 1116554 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0227 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 1007545 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle |
| 0.0192 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 855533 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0186 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 828074 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0182 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 810944 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0172 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 767047 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |






### Top Genera for Utah (UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0343 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 204544 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0281 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 167797 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0279 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 166490 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0270 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 161076 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0263 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 156794 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch |
| 0.0231 | [Larus](https://en.wikipedia.org/wiki/Larus)‡ | Gull | 137567 | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus) | California Gull |
| 0.0230 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 137266 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0225 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 134064 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0217 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0211 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 126148 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |






### Top Genera for Virginia (VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0416 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 843977 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0360 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 729582 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0359 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 728016 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0295 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0259 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 524847 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0256 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 520026 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0255 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 517564 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0250 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 506585 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0242 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 491506 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0240 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 486346 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |






### Top Genera for Vermont (VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0521 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 346101 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0489 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 325282 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0446 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 296739 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0361 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 240266 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0361 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 239918 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0336 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 223533 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0331 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 220081 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0319 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 212404 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0315 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 209167 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0238 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 158082 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for Washington (WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0408 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 961797 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0359 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 845174 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0335 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 789623 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucowinged Gull |
| 0.0319 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 750809 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0299 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 704419 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0294 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 693119 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0233 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 548378 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0219 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 516051 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0219 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))‡ | Goldfinch | 515458 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0208 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 488880 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |






### Top Genera for Wisconsin (WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0386 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 775840 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0344 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 692533 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0331 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 664979 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0318 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 640244 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0305 | [Turdus](https://en.wikipedia.org/wiki/Turdus)‡ | Robin | 613134 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0302 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 606573 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0277 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 557294 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0265 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 532475 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0255 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 512160 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0253 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 508813 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for West Virginia (WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0441 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 120310 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0424 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 115586 | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler |
| 0.0342 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 93312 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0308 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 84023 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0299 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 81694 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0291 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 79461 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0279 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 76100 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0270 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 73762 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| 0.0268 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 73060 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0262 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Wyoming (WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0402 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 81776 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0347 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 70656 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0323 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 65641 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0261 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 53174 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0258 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 52437 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| 0.0256 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 52070 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0251 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 51015 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0229 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 46520 | [Spinus pinus](https://en.wikipedia.org/wiki/Spinus_pinus) | Pine Siskin |
| 0.0215 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 43642 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0202 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 41090 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |










## Scores for Bird Species

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name |
|--:|---|---|---|
| AK | 0.0286 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| AL | 0.0386 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal |
| AR | 0.0248 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| AZ | 0.0200 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| CA | 0.0174 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| CO | 0.0250 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker |
| CT | 0.0160 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| DC | 0.0375 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin |
| DE | 0.0217 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| FL | 0.0212 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| GA | 0.0278 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| HI | 0.0434 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| IA | 0.0138 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| ID | 0.0261 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| IL | 0.0153 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |
| IN | 0.0243 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| KS | 0.0174 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| KY | 0.0104 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| LA | 0.0127 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler |
| MA | 0.0176 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| MD | 0.0161 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow |
| ME | 0.0371 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| MI | 0.0097 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| MN | 0.0221 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| MO | 0.0111 | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |
| MS | 0.0181 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| MT | 0.0292 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| NC | 0.0324 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| ND | 0.0160 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark |
| NE | 0.0206 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |
| NH | 0.0334 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| NJ | 0.0110 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant |
| NM | 0.0321 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| NV | 0.0184 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| NY | 0.0107 | [Columba livia](https://en.wikipedia.org/wiki/Columba_livia) | Rock Pigeon |
| OH | 0.0112 | [Tachycineta bicolor](https://en.wikipedia.org/wiki/Tachycineta_bicolor) | Tree Swallow |
| OK | 0.0116 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher |
| OR | 0.0199 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| PA | 0.0297 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| RI | 0.0289 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| SC | 0.0182 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| SD | 0.0257 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| TN | 0.0298 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| TX | 0.0259 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird |
| UT | 0.0123 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow |
| VA | 0.0102 | [Spizella passerina](https://en.wikipedia.org/wiki/Spizella_passerina) | Chipping Sparrow |
| VT | 0.0445 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| WA | 0.0233 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| WI | 0.0268 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch |
| WV | 0.0187 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| WY | 0.0256 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |





### Top Species for Alaska (AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0286 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 134933 |
| 0.0242 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 114247 |
| 0.0212 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  | 100304 |
| 0.0201 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 94976 |
| 0.0199 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 94146 |
| 0.0194 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucowinged Gull | 91882 |
| 0.0186 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 87674 |
| 0.0147 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 69491 |
| 0.0131 | [Anas acuta](https://en.wikipedia.org/wiki/Anas_acuta) | Northern Pintail | 62130 |
| 0.0131 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 61971 |






### Top Species for Alabama (AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0386 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 167600 |
| 0.0307 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 133341 |
| 0.0301 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 130529 |
| 0.0293 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 127076 |
| 0.0280 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 121684 |
| 0.0240 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 104294 |
| 0.0234 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 101376 |
| 0.0232 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 100822 |
| 0.0213 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 92532 |
| 0.0194 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 84368 |






### Top Species for Arkansas (AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0385 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 133523 |
| 0.0315 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 109252 |
| 0.0301 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 104560 |
| 0.0283 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 98316 |
| 0.0269 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 93388 |
| 0.0263 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 91280 |
| 0.0248 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 86146 |
| 0.0248 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 85916 |
| 0.0203 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 70259 |
| 0.0199 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 68963 |






### Top Species for Arizona (AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0268 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 593846 |
| 0.0267 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 592799 |
| 0.0200 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.0195 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 431522 |
| 0.0174 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 386191 |
| 0.0168 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 371565 |
| 0.0146 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 323152 |
| 0.0142 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 313824 |
| 0.0141 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 311895 |
| 0.0136 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler | 301068 |






### Top Species for California (CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0182 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 194403 |
| 0.0174 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe | 186372 |
| 0.0165 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 176672 |
| 0.0154 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 164610 |
| 0.0142 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 151564 |
| 0.0142 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler | 151496 |
| 0.0139 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 148682 |
| 0.0138 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 147588 |
| 0.0133 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 142480 |
| 0.0132 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 140781 |






### Top Species for Colorado (CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0290 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 514016 |
| 0.0250 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 443193 |
| 0.0243 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 431640 |
| 0.0238 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 422090 |
| 0.0219 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 388420 |
| 0.0218 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 387306 |
| 0.0218 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 387189 |
| 0.0212 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 375157 |
| 0.0203 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 359219 |
| 0.0188 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 334034 |






### Top Species for Connecticut (CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0292 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 295889 |
| 0.0288 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 292446 |
| 0.0272 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)‡ | American Robin | 275834 |
| 0.0272 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 275382 |
| 0.0268 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 272058 |
| 0.0259 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 262634 |
| 0.0237 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 240563 |
| 0.0232 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 234876 |
| 0.0231 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 234438 |
| 0.0222 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 225415 |






### Top Species for District of Columbia (DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0375 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 62170 |
| 0.0348 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 57641 |
| 0.0325 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 53975 |
| 0.0267 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 44202 |
| 0.0259 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 42950 |
| 0.0253 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 41998 |
| 0.0242 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 40148 |
| 0.0235 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 39014 |
| 0.0216 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 35866 |
| 0.0215 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 35578 |






### Top Species for Delaware (DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0242 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 105825 |
| 0.0217 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 94945 |
| 0.0211 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 92301 |
| 0.0206 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 90069 |
| 0.0201 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 88198 |
| 0.0193 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 84664 |
| 0.0187 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 81803 |
| 0.0177 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 77729 |
| 0.0169 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 74054 |
| 0.0169 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron | 73996 |






### Top Species for Florida (FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0275 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 995521 |
| 0.0250 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 907976 |
| 0.0245 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 886664 |
| 0.0230 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 832859 |
| 0.0212 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 769348 |
| 0.0206 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 748541 |
| 0.0206 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 747757 |
| 0.0204 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 738354 |
| 0.0187 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey | 678520 |
| 0.0179 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron | 649662 |






### Top Species for Georgia (GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0384 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 477796 |
| 0.0318 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 395603 |
| 0.0283 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 351685 |
| 0.0278 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 345328 |
| 0.0267 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 332016 |
| 0.0256 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 317902 |
| 0.0255 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 317177 |
| 0.0240 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 297817 |
| 0.0232 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 288903 |
| 0.0212 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |






### Top Species for Hawaii (HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0614 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis)* | Common Myna | 89440 |
| 0.0569 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* |  | 82840 |
| 0.0538 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* |  | 78346 |
| 0.0434 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove | 63162 |
| 0.0375 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover | 54637 |
| 0.0336 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret | 48950 |
| 0.0334 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 48637 |
| 0.0321 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 46683 |
| 0.0312 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 45468 |
| 0.0273 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata)* |  | 39698 |






### Top Species for Iowa (IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0317 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 107540 |
| 0.0305 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 103673 |
| 0.0262 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 88770 |
| 0.0256 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 86938 |
| 0.0250 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 84859 |
| 0.0238 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 80952 |
| 0.0235 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 79689 |
| 0.0232 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 78771 |
| 0.0225 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)‡ | American Goldfinch | 76405 |
| 0.0215 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 73023 |






### Top Species for Idaho (ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0314 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 140857 |
| 0.0264 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |
| 0.0261 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 116847 |
| 0.0237 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 106334 |
| 0.0226 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 101092 |
| 0.0223 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 100127 |
| 0.0216 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 96641 |
| 0.0214 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 95897 |
| 0.0206 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 92431 |
| 0.0201 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 90291 |






### Top Species for Illinois (IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0326 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 650537 |
| 0.0319 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 637278 |
| 0.0255 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 509568 |
| 0.0250 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 499718 |
| 0.0240 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 480060 |
| 0.0228 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 455911 |
| 0.0223 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 446248 |
| 0.0216 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 430787 |
| 0.0215 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 430124 |
| 0.0210 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 420287 |






### Top Species for Indiana (IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0345 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 350530 |
| 0.0272 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 276324 |
| 0.0260 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 263938 |
| 0.0255 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 259466 |
| 0.0245 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 249012 |
| 0.0243 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 247415 |
| 0.0228 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 231871 |
| 0.0225 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 228593 |
| 0.0221 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 224909 |
| 0.0220 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 223851 |






### Top Species for Kansas (KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0282 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 171877 |
| 0.0256 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 155779 |
| 0.0244 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 148709 |
| 0.0232 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 140947 |
| 0.0201 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 122445 |
| 0.0194 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 118269 |
| 0.0193 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 117208 |
| 0.0189 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 114945 |
| 0.0184 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 111884 |
| 0.0183 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 111412 |






### Top Species for Kentucky (KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0384 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 158980 |
| 0.0309 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 127779 |
| 0.0295 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 121971 |
| 0.0293 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 121295 |
| 0.0273 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0261 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 108035 |
| 0.0255 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 105736 |
| 0.0245 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 101534 |
| 0.0237 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 98073 |
| 0.0230 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 95179 |






### Top Species for Louisiana (LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 186684 |
| 0.0245 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 164645 |
| 0.0241 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 162215 |
| 0.0209 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 140662 |
| 0.0199 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 133593 |
| 0.0188 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 126615 |
| 0.0184 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 123872 |
| 0.0182 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 122384 |
| 0.0174 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 117040 |
| 0.0167 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 111898 |






### Top Species for Massachusetts (MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0300 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 702147 |
| 0.0292 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 682228 |
| 0.0285 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 666937 |
| 0.0268 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 626570 |
| 0.0268 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 625921 |
| 0.0244 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 570593 |
| 0.0241 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 563582 |
| 0.0238 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 556268 |
| 0.0212 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 497003 |
| 0.0206 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 482841 |






### Top Species for Maryland (MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0336 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 681139 |
| 0.0268 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 543555 |
| 0.0243 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 492131 |
| 0.0237 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 481726 |
| 0.0237 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 480019 |
| 0.0230 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 466148 |
| 0.0225 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0214 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 434872 |
| 0.0209 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 424167 |
| 0.0208 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 421448 |






### Top Species for Maine (ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0371 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 340077 |
| 0.0341 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 312621 |
| 0.0275 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 252247 |
| 0.0273 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 250547 |
| 0.0262 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 240739 |
| 0.0252 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 230965 |
| 0.0224 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 205319 |
| 0.0216 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 197805 |
| 0.0157 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 143856 |
| 0.0156 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant | 143391 |






### Top Species for Michigan (MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0304 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 672265 |
| 0.0299 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 661443 |
| 0.0295 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)‡ | American Robin | 653561 |
| 0.0278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 614337 |
| 0.0262 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 579069 |
| 0.0257 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 569474 |
| 0.0256 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 565721 |
| 0.0241 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 532312 |
| 0.0237 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 524815 |
| 0.0223 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 492756 |






### Top Species for Minnesota (MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0394 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 443332 |
| 0.0354 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 398422 |
| 0.0299 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 336937 |
| 0.0276 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 311082 |
| 0.0241 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 271335 |
| 0.0241 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 270765 |
| 0.0240 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 269788 |
| 0.0238 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 267907 |
| 0.0224 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 252395 |
| 0.0221 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 249129 |






### Top Species for Missouri (MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0366 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 328095 |
| 0.0276 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 247494 |
| 0.0255 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 228335 |
| 0.0253 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 227158 |
| 0.0247 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 221133 |
| 0.0234 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 209758 |
| 0.0220 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 197211 |
| 0.0220 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 197101 |
| 0.0214 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 191714 |
| 0.0195 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 175152 |






### Top Species for Mississippi (MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0314 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 80897 |
| 0.0271 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 69862 |
| 0.0259 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 66564 |
| 0.0241 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 62118 |
| 0.0224 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 57768 |
| 0.0214 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 55068 |
| 0.0183 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 47154 |
| 0.0181 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron | 46603 |
| 0.0179 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 46111 |
| 0.0177 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 45672 |






### Top Species for Montana (MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0313 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 162755 |
| 0.0292 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 151463 |
| 0.0240 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 124814 |
| 0.0237 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 123216 |
| 0.0229 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 119152 |
| 0.0217 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 112907 |
| 0.0217 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 112518 |
| 0.0206 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 107175 |
| 0.0198 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 102842 |
| 0.0157 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 81427 |






### Top Species for North Carolina (NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0358 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 535006 |
| 0.0324 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 484010 |
| 0.0310 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 463009 |
| 0.0279 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 417411 |
| 0.0279 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 416651 |
| 0.0251 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 375428 |
| 0.0232 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 347236 |
| 0.0231 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 345214 |
| 0.0206 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 307886 |
| 0.0204 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 304420 |






### Top Species for North Dakota (ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0257 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 54140 |
| 0.0229 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 48107 |
| 0.0224 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 47174 |
| 0.0220 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 46307 |
| 0.0217 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 45726 |
| 0.0194 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 40765 |
| 0.0165 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 34683 |
| 0.0160 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 33762 |
| 0.0157 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer | 33125 |
| 0.0156 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 32877 |






### Top Species for Nebraska (NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0362 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 103158 |
| 0.0281 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 80260 |
| 0.0248 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 70609 |
| 0.0244 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 69715 |
| 0.0244 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 69612 |
| 0.0242 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 69060 |
| 0.0218 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 62185 |
| 0.0206 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 58694 |
| 0.0202 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 57657 |
| 0.0197 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 56148 |






### Top Species for New Hampshire (NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0406 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 198394 |
| 0.0334 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 163229 |
| 0.0288 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 140981 |
| 0.0282 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 137901 |
| 0.0269 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 131417 |
| 0.0242 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 118235 |
| 0.0232 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 113296 |
| 0.0231 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 112921 |
| 0.0220 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 107536 |
| 0.0220 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 107390 |






### Top Species for New Jersey (NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0238 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 491469 |
| 0.0231 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 476809 |
| 0.0227 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 468748 |
| 0.0216 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 445882 |
| 0.0206 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 425901 |
| 0.0189 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 389938 |
| 0.0179 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 370128 |
| 0.0168 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 346091 |
| 0.0165 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 340688 |
| 0.0164 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 337485 |






### Top Species for New Mexico (NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0321 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 239709 |
| 0.0255 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 190730 |
| 0.0210 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 156613 |
| 0.0206 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 154302 |
| 0.0204 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 152761 |
| 0.0183 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 137112 |
| 0.0178 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 132792 |
| 0.0177 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 132679 |
| 0.0153 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 114032 |
| 0.0151 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 113186 |






### Top Species for Nevada (NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0229 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 66448 |
| 0.0207 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 59965 |
| 0.0201 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 58368 |
| 0.0191 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 55205 |
| 0.0184 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot | 53207 |
| 0.0179 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 51745 |
| 0.0161 | [Setophaga coronata](https://en.wikipedia.org/wiki/Setophaga_coronata) | Yellow-rumped Warbler | 46561 |
| 0.0159 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 46056 |
| 0.0157 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 45621 |
| 0.0147 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 42522 |






### Top Species for New York (NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0293 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 1176480 |
| 0.0288 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 1158294 |
| 0.0278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 1117636 |
| 0.0259 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 1042591 |
| 0.0257 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 1033854 |
| 0.0252 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 1014758 |
| 0.0235 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 946282 |
| 0.0231 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 929023 |
| 0.0228 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 917812 |
| 0.0223 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 895261 |






### Top Species for Ohio (OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0325 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 791329 |
| 0.0298 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 724685 |
| 0.0273 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 663248 |
| 0.0239 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 581247 |
| 0.0238 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 579046 |
| 0.0238 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 577543 |
| 0.0230 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 558210 |
| 0.0222 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 538726 |
| 0.0216 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 524738 |
| 0.0214 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 519777 |






### Top Species for Oklahoma (OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0328 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 107206 |
| 0.0251 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 82216 |
| 0.0247 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 80937 |
| 0.0223 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 73058 |
| 0.0221 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 72196 |
| 0.0213 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 69674 |
| 0.0208 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 68087 |
| 0.0199 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 65170 |
| 0.0187 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 61009 |
| 0.0179 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 58503 |






### Top Species for Oregon (OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0288 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 563712 |
| 0.0276 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 540183 |
| 0.0238 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 466067 |
| 0.0229 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 448962 |
| 0.0218 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 427331 |
| 0.0202 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 395491 |
| 0.0199 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 389415 |
| 0.0198 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 387988 |
| 0.0192 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 376658 |
| 0.0191 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |






### Top Species for Pennsylvania (PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0346 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 947363 |
| 0.0319 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 874134 |
| 0.0305 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 836000 |
| 0.0297 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 812632 |
| 0.0292 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 800582 |
| 0.0271 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 743436 |
| 0.0252 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 690654 |
| 0.0232 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 635611 |
| 0.0228 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 625797 |
| 0.0226 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 620147 |






### Top Species for Rhode Island (RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0289 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 60608 |
| 0.0286 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 60029 |
| 0.0262 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 55041 |
| 0.0240 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 50314 |
| 0.0232 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 48648 |
| 0.0210 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 44092 |
| 0.0210 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 44049 |
| 0.0190 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 39936 |
| 0.0190 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 39931 |
| 0.0189 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 39719 |






### Top Species for South Carolina (SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0368 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 309495 |
| 0.0299 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)‡ | Carolina Wren | 251184 |
| 0.0275 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 230968 |
| 0.0256 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 215380 |
| 0.0253 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 212440 |
| 0.0239 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 200883 |
| 0.0228 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 191263 |
| 0.0228 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 191190 |
| 0.0220 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 184841 |
| 0.0182 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 153302 |






### Top Species for South Dakota (SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0314 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 45321 |
| 0.0257 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 37111 |
| 0.0229 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 33080 |
| 0.0215 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 31043 |
| 0.0214 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 30798 |
| 0.0208 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 30043 |
| 0.0197 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0177 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 25485 |
| 0.0177 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 25466 |
| 0.0176 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer | 25307 |






### Top Species for Tennessee (TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0374 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 331627 |
| 0.0298 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 264394 |
| 0.0298 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0292 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 259006 |
| 0.0289 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 256273 |
| 0.0272 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 241408 |
| 0.0264 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 234136 |
| 0.0258 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 229026 |
| 0.0235 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 208456 |
| 0.0225 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 199634 |






### Top Species for Texas (TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0269 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 1198373 |
| 0.0259 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 1153426 |
| 0.0208 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 926985 |
| 0.0192 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 855529 |
| 0.0179 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle | 794651 |
| 0.0167 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 742445 |
| 0.0138 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 613701 |
| 0.0134 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 596851 |
| 0.0133 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 592533 |
| 0.0132 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 585128 |






### Top Species for Utah (UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0281 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 167789 |
| 0.0231 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 138061 |
| 0.0230 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 137266 |
| 0.0227 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 135285 |
| 0.0223 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 132736 |
| 0.0217 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 129642 |
| 0.0188 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 111858 |
| 0.0182 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 108584 |
| 0.0169 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 100948 |
| 0.0169 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 100592 |






### Top Species for Virginia (VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0359 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 728016 |
| 0.0295 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0281 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 569767 |
| 0.0259 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 524643 |
| 0.0256 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 520026 |
| 0.0250 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0240 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 486346 |
| 0.0234 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 475019 |
| 0.0227 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 459930 |
| 0.0212 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 429241 |






### Top Species for Vermont (VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0445 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 295586 |
| 0.0372 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 247470 |
| 0.0361 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 239918 |
| 0.0315 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 209167 |
| 0.0296 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 196825 |
| 0.0274 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 182074 |
| 0.0238 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 158080 |
| 0.0235 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 156460 |
| 0.0225 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 149624 |
| 0.0222 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 147707 |






### Top Species for Washington (WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0299 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 704290 |
| 0.0292 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 688825 |
| 0.0278 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 654472 |
| 0.0233 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 548378 |
| 0.0224 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 527793 |
| 0.0209 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 493104 |
| 0.0208 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 488880 |
| 0.0200 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 470005 |
| 0.0195 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 459524 |
| 0.0162 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 381336 |






### Top Species for Wisconsin (WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0318 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 639564 |
| 0.0305 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)‡ | American Robin | 613134 |
| 0.0300 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 603469 |
| 0.0268 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 538617 |
| 0.0265 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 532474 |
| 0.0253 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 508643 |
| 0.0247 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 497270 |
| 0.0245 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 491683 |
| 0.0219 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 439694 |
| 0.0219 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 439424 |






### Top Species for West Virginia (WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0342 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 93312 |
| 0.0328 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 89653 |
| 0.0308 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 84023 |
| 0.0291 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 79461 |
| 0.0277 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 75626 |
| 0.0262 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 71638 |
| 0.0258 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 70340 |
| 0.0252 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 68808 |
| 0.0249 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 67983 |
| 0.0214 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 58475 |






### Top Species for Wyoming (WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0347 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 70656 |
| 0.0256 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 52152 |
| 0.0256 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 52099 |
| 0.0239 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 48538 |
| 0.0202 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 41090 |
| 0.0201 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 40888 |
| 0.0189 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 38495 |
| 0.0183 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 37212 |
| 0.0177 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 35919 |
| 0.0176 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 35806 |































---

Full Lists of Scores (large amount of text):  
[Prevalence Scores - Full Genus Ranking](prevalence_genus_byscore)  
[Prevalence Scores - Full Genus Ranking By State](prevalence_genus_bystate)  
[Prevalence Scores - Full Species Ranking](prevalance_species_byscore)  
[Prevalence Scores - Full Species Ranking By State](prevalence_species_bystate)  




