---
title: "Bird Scores - Informedness"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
math: katex
---


This BIRDUP scoring system is based on  [Youden's J statistic](https://en.wikipedia.org/wiki/Youden%27s_J_statistic), also called informedness.
It's essentially the difference between how common a bird is in a state and how common that bird is elsewhere in North America.

Youden's J statistic is usually used to evaluate the performance of a diagnostic test.
If we interpret these bird scores that way, we're essentially evaluating birds as diagnostic tests of whether you're in a given state. 

$$\gdef\nBird{🦃}
\gdef\nState{🗽}
\gdef\nTotal{N}
\gdef\nJoint{📋}$$

These scores use observation records from the eBird database[^ebirdcitation].
Each observation is for a specific species of bird in a specific state.
- Let $N$ be the total number of observations in the data.
- Let $\nBird$ be the total number of observations of a specific bird species or genus.
- Let $\nState$ be the total number of observations taking place in a specific state.
- Let $\nJoint$ be the the joint observation count: the total number of observations of that specific type of bird in that specific state.

Here, the Bird Score for a pair of state and bird is 

$$J = \frac{\nJoint}{\nState} - \frac{\nBird - \nJoint}{\nTotal - \nState}$$

The dual of this measurement, called [markedness](markedness), swaps the roll of state and bird in the formula.

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
| AK | 0.0260 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | [Calidris mauri](https://en.wikipedia.org/wiki/Calidris_mauri) | Western Sandpiper |
| AL | 0.0215 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| AR | 0.0106 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| AZ | 0.0186 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove |
| CA | 0.0147 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| CO | 0.0136 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| CT | 0.0083 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| DC | 0.0139 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| DE | 0.0099 | [Tringa](https://en.wikipedia.org/wiki/Tringa) | Tattlers | [Tringa melanoleuca](https://en.wikipedia.org/wiki/Tringa_melanoleuca) | Greater Yellowlegs |
| FL | 0.0400 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| GA | 0.0166 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| HI | 0.0364 | [Pluvialis](https://en.wikipedia.org/wiki/Pluvialis) | Plover | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover |
| IA | 0.0069 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| ID | 0.0152 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| IL | 0.0083 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| IN | 0.0060 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| KS | 0.0060 | [Charadrius](https://en.wikipedia.org/wiki/Charadrius) | Plover | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| KY | 0.0083 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| LA | 0.0168 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| MA | 0.0103 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| MD | 0.0044 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow |
| ME | 0.0286 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler |
| MI | 0.0081 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| MN | 0.0166 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| MO | 0.0152 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| MS | 0.0090 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| MT | 0.0271 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| NC | 0.0229 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| ND | 0.0160 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| NE | 0.0089 | [Icterus](https://en.wikipedia.org/wiki/New_World_oriole)† | Oriole | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula) | Baltimore Oriole |
| NH | 0.0187 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| NJ | 0.0066 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| NM | 0.0195 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| NV | 0.0157 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| NY | 0.0093 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| OH | 0.0034 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |
| OK | 0.0154 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| OR | 0.0179 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| PA | 0.0096 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| RI | 0.0419 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| SC | 0.0110 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| SD | 0.0161 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| TN | 0.0159 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| TX | 0.0094 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| UT | 0.0107 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| VA | 0.0054 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| VT | 0.0199 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| WA | 0.0126 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| WI | 0.0099 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | 0.0123 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| WY | 0.0084 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |





### Top Genera for Alaska  (AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0403 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 293920 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  |
| 0.0260 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 160956 | [Calidris mauri](https://en.wikipedia.org/wiki/Calidris_mauri) | Western Sandpiper |
| 0.0228 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 219036 | [Anas acuta](https://en.wikipedia.org/wiki/Anas_acuta) | Northern Pintail |
| 0.0183 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 114756 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0173 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 96452 | [Gavia pacifica](https://en.wikipedia.org/wiki/Gavia_pacifica) | Pacific Loon |
| 0.0139 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 69532 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll |
| 0.0127 | [Rissa](https://en.wikipedia.org/wiki/Kittiwake) | Kittiwake | 60795 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake |
| 0.0126 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 69491 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0117 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 64928 | [Melanitta perspicillata](https://en.wikipedia.org/wiki/Melanitta_perspicillata) | Surf Scoter |
| 0.0115 | [Bucephala](https://en.wikipedia.org/wiki/Goldeneye_(duck)) | Goldeneye | 86505 | [Bucephala islandica](https://en.wikipedia.org/wiki/Bucephala_islandica) | Barrow's Goldeneye |






### Top Genera for Alabama  (AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0215 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0194 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 127076 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0166 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 167600 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0137 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 127153 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0121 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 84368 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0117 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 100822 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0110 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 205713 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0096 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 59435 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0090 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 140224 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |
| 0.0087 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 60847 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |






### Top Genera for Arkansas  (AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0164 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 133523 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0164 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0154 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 93388 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0138 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 101947 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0112 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 68963 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0106 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 55044 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0103 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 109252 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0092 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 57596 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0074 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 69791 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow |
| 0.0064 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | 68449 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo |






### Top Genera for Arizona  (AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0186 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 916998 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove |
| 0.0172 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 386191 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0170 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 388898 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee |
| 0.0162 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 393373 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0128 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 623372 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| 0.0126 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 613686 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0125 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 296630 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0116 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 342049 | [Toxostoma curvirostre](https://en.wikipedia.org/wiki/Toxostoma_curvirostre) | Curve-billed Thrasher |
| 0.0114 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 422574 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| 0.0090 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 200508 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |






### Top Genera for California  (CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0147 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 176961 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0146 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 239921 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| 0.0129 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 153459 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0112 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 129054 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| 0.0096 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 112390 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0088 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 330232 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull |
| 0.0083 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 106640 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0071 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 237545 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0068 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | 117049 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| 0.0067 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 235347 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |






### Top Genera for Colorado  (CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0201 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0136 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 443193 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0135 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 292668 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0112 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 467084 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0106 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 453161 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0106 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 210475 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0101 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 241188 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0100 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 375157 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0089 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 260926 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |
| 0.0085 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 567517 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |






### Top Genera for Connecticut  (CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0123 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 240563 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0114 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 339172 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0086 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 302089 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0083 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 162362 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0080 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 295889 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0079 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 305895 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0068 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 292446 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0063 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 187078 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0042 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 218316 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| 0.0039 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 275510 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for District of Columbia  (DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0164 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 53975 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0154 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 41998 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0139 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 62170 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0137 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0128 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 74079 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| 0.0127 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 57641 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0111 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 24475 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0097 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 30486 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0091 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 75508 | [Setophaga americana](https://en.wikipedia.org/wiki/Setophaga_americana) | Northern Parula |
| 0.0074 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 25165 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |






### Top Genera for Delaware  (DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0150 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 101378 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0109 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 144722 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0099 | [Tringa](https://en.wikipedia.org/wiki/Tringa) | Tattlers | 71586 | [Tringa melanoleuca](https://en.wikipedia.org/wiki/Tringa_melanoleuca) | Greater Yellowlegs |
| 0.0096 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 94945 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0096 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 114527 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0094 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 84664 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0092 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 53108 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0072 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 42296 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0065 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 54775 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0063 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 48752 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |






### Top Genera for Florida  (FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0400 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 1584817 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| 0.0237 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 2139095 | [Setophaga palmarum](https://en.wikipedia.org/wiki/Setophaga_palmarum) | Palm Warbler |
| 0.0237 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 1419010 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0199 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 748541 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0150 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 833895 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0149 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 553383 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0146 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 678520 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |
| 0.0145 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 1009671 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle |
| 0.0120 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 538801 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0112 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 493180 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |






### Top Genera for Georgia  (GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0223 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0169 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 659981 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0166 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 477796 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0165 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 345328 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0150 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 377667 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0148 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 288903 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0137 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 264143 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0128 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 249060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0111 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 349899 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| 0.0104 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | 179633 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |






### Top Genera for Hawaii  (HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0614 | [Acridotheres](https://en.wikipedia.org/wiki/Acridotheres)* | Myna | 89440 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis) | Common Myna |
| 0.0569 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)* | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus) |  |
| 0.0538 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)* |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata) |  |
| 0.0401 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 63162 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| 0.0389 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata) |  |
| 0.0364 | [Pluvialis](https://en.wikipedia.org/wiki/Pluvialis) | Plover | 55064 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover |
| 0.0325 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 48950 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0245 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | 35689 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| 0.0234 | [Chlorodrepanis](https://en.wikipedia.org/wiki/Chlorodrepanis) |  | 34136 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  |
| 0.0228 | [Pycnonotus](https://en.wikipedia.org/wiki/Pycnonotus) |  | 33210 | [Pycnonotus cafer](https://en.wikipedia.org/wiki/Pycnonotus_cafer) |  |






### Top Genera for Iowa  (IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0131 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 97621 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0104 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 76639 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0097 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 108897 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0096 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 107540 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0086 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 88043 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0070 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 80952 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0070 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 103673 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0069 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 45929 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0064 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 42291 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0056 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 40013 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |






### Top Genera for Idaho  (ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0243 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0152 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 135819 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0115 | [Falco](https://en.wikipedia.org/wiki/Falcon) | Falcon | 81038 | [Falco sparverius](https://en.wikipedia.org/wiki/Falco_sparverius) | American Kestrel |
| 0.0113 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 65286 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0107 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 100127 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0107 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 53404 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |
| 0.0100 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 150663 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0099 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 141997 | [Spinus pinus](https://en.wikipedia.org/wiki/Spinus_pinus) | Pine Siskin |
| 0.0093 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 110631 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0079 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 140857 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |






### Top Genera for Illinois  (IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0100 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 637278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0098 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 434206 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0092 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 650537 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0089 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 520240 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0083 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 499718 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0062 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 433268 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0057 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 559040 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0056 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 430787 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0048 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | 235794 | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |
| 0.0046 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163030 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |






### Top Genera for Indiana  (IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0125 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 350530 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0122 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 282027 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0107 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 224909 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0098 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 326501 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0072 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 247310 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0060 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 173525 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| 0.0057 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 181515 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0048 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 263938 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0045 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 146848 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0043 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | 115449 | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |






### Top Genera for Kansas  (KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0115 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 92201 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0089 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 146299 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0084 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 88177 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0082 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 145143 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0081 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 86342 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird |
| 0.0066 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 85199 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0062 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 171934 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0060 | [Charadrius](https://en.wikipedia.org/wiki/Charadrius) | Plover | 94983 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| 0.0054 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 36284 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0052 | [Icterus](https://en.wikipedia.org/wiki/New_World_oriole)† | Oriole | 67292 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula) | Baltimore Oriole |






### Top Genera for Kentucky  (KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0164 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 158980 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0140 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 105736 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0138 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 98073 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0108 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 109288 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0084 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 101534 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0083 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 84477 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0083 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 121971 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0073 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 127779 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0072 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 51917 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0062 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 71425 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |






### Top Genera for Louisiana  (LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0200 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 171844 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0168 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 223799 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0159 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 164645 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0090 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 126615 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0078 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 63812 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0072 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 67571 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0070 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)‡ | Pelican | 66828 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0063 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 50157 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0059 | [Lanius](https://en.wikipedia.org/wiki/Lanius) | Shrike | 50080 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike |
| 0.0059 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 75119 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |






### Top Genera for Massachusetts  (MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0192 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 953627 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0103 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 731554 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0100 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 497003 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0082 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 682228 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0072 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 346468 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0066 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 704121 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck |
| 0.0063 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 193084 | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter |
| 0.0056 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 147688 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0056 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 530280 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0053 | [Poecile](https://en.wikipedia.org/wiki/Poecile)‡ | Chickadee | 702495 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |






### Top Genera for Maryland  (MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0173 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0118 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 681139 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0096 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 424167 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0080 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 402965 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0071 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 317285 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0069 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 454993 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0066 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 775958 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| 0.0063 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 274339 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0058 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 184681 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0046 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 317229 | [Spizella passerina](https://en.wikipedia.org/wiki/Spizella_passerina) | Chipping Sparrow |






### Top Genera for Maine  (ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0295 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 470161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0286 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 593940 | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler |
| 0.0133 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 412406 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0132 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 127240 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0106 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 253820 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch |
| 0.0097 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 283461 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0097 | [Poecile](https://en.wikipedia.org/wiki/Poecile)‡ | Chickadee | 316366 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0097 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 117292 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |
| 0.0080 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 272283 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0072 | [Nannopterum](https://en.wikipedia.org/wiki/Nannopterum) | Cormorant | 143391 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant |






### Top Genera for Michigan  (MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0098 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 706919 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0096 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 586777 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0089 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 661443 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0081 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 236621 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0074 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 532312 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0067 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 528609 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0065 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 621634 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0063 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 176499 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0061 | [Turdus](https://en.wikipedia.org/wiki/Turdus)‡ | Robin | 653561 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0058 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 614337 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Genera for Minnesota  (MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0166 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 436581 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0151 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 448373 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0122 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 329350 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0091 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 459935 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0080 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 156850 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0072 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 275994 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0066 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 121146 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0065 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 311082 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0064 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 336940 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0058 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 309216 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |






### Top Genera for Missouri  (MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0152 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 275131 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0147 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 328095 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0120 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 209758 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0097 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 175152 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0076 | [Sialia](https://en.wikipedia.org/wiki/Sialia)‡ | Bluebird | 133730 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0074 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 113686 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0067 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 173697 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow |
| 0.0064 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 247494 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0063 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 192465 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0054 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 156699 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |






### Top Genera for Mississippi  (MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0172 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 66564 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0157 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 83150 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0127 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 72864 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0125 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 57768 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0102 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 41057 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0093 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 80897 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0090 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 30763 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0085 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 29491 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0082 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 40007 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0079 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 41515 | [Calidris alba](https://en.wikipedia.org/wiki/Calidris_alba) | Sanderling |






### Top Genera for Montana  (MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0271 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0121 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 123216 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0105 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 183518 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee |
| 0.0099 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 68395 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0097 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 69555 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0093 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 127361 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0081 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 164826 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0078 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 162796 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0077 | [Tachycineta](https://en.wikipedia.org/wiki/Tachycineta) | Swallow | 83401 | [Tachycineta bicolor](https://en.wikipedia.org/wiki/Tachycineta_bicolor) | Tree Swallow |
| 0.0072 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 68215 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |






### Top Genera for North Carolina  (NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0229 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0166 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 416651 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0139 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 535006 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0135 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 307887 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0127 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 731283 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0122 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 295792 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0104 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 386900 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0103 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 281345 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0093 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 394475 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| 0.0068 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 161868 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |






### Top Genera for North Dakota  (ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0160 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 46662 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0150 | [Aythya](https://en.wikipedia.org/wiki/Aythya) | Diving Duck | 48347 | [Aythya americana](https://en.wikipedia.org/wiki/Aythya_americana) | Redhead |
| 0.0123 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 33785 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0120 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 48522 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow |
| 0.0118 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 74444 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0113 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 36519 | [Tyrannus tyrannus](https://en.wikipedia.org/wiki/Tyrannus_tyrannus) | Eastern Kingbird |
| 0.0106 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 24049 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0087 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 30785 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |
| 0.0080 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18180 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0076 | [Charadrius](https://en.wikipedia.org/wiki/Charadrius) | Plover | 36287 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |






### Top Genera for Nebraska  (NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0147 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 52365 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0126 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 103158 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0106 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 47511 | [Tyrannus tyrannus](https://en.wikipedia.org/wiki/Tyrannus_tyrannus) | Eastern Kingbird |
| 0.0101 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 38307 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0093 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 44070 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0089 | [Icterus](https://en.wikipedia.org/wiki/New_World_oriole)† | Oriole | 42241 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula) | Baltimore Oriole |
| 0.0082 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 63494 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |
| 0.0081 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 69060 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0081 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 57660 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0076 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 69715 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |






### Top Genera for New Hampshire  (NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0221 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 285427 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0187 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 174912 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0167 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 202762 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0149 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 182017 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0122 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 163229 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0105 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 107536 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0095 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 152843 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0078 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 141809 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0074 | [Catharus](https://en.wikipedia.org/wiki/Catharus)† | Nightingale-thrush | 65080 | [Catharus guttatus](https://en.wikipedia.org/wiki/Catharus_guttatus) | Hermit Thrush |
| 0.0069 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 188968 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |






### Top Genera for New Jersey  (NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0150 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 759061 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0083 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 524752 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0074 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 318740 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0067 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 340688 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0066 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 193945 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0063 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 288141 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0060 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 607721 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck |
| 0.0056 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 163330 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0052 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 163719 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0046 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 191464 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |






### Top Genera for New Mexico  (NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0195 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 259544 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0161 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 293725 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove |
| 0.0143 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 190879 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0132 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 155739 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0130 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 155963 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe |
| 0.0107 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 90816 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0098 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 97804 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0091 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 79822 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| 0.0080 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 66915 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee |
| 0.0075 | [Archilochus](https://en.wikipedia.org/wiki/Archilochus) |  | 90975 | [Archilochus alexandri](https://en.wikipedia.org/wiki/Archilochus_alexandri) | Black-chinned Hummingbird |






### Top Genera for Nevada  (NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0157 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0141 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | 53207 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| 0.0096 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 33664 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0094 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 29373 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0094 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 71735 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0089 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 48804 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe |
| 0.0088 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 43272 | [Spatula cyanoptera](https://en.wikipedia.org/wiki/Spatula_cyanoptera) | Cinnamon Teal |
| 0.0082 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 28494 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0080 | [Oxyura](https://en.wikipedia.org/wiki/Oxyura) | Stiff-tailed Duck | 29300 | [Oxyura jamaicensis](https://en.wikipedia.org/wiki/Oxyura_jamaicensis) | Ruddy Duck |
| 0.0080 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 32902 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |






### Top Genera for New York  (NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0142 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 1430945 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0093 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 1053772 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0080 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 1158294 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0075 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 598555 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0070 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 1120243 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0065 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 1147961 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0065 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 895261 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0060 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 1117636 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0060 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 1176486 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0059 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 713416 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |






### Top Genera for Ohio  (OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0108 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 791329 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0093 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 1106472 | [Setophaga petechia](https://en.wikipedia.org/wiki/Setophaga_petechia) | Yellow Warbler |
| 0.0092 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 598486 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0068 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 583159 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0068 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 677794 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0064 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 724685 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0062 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 663248 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0059 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 420642 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0055 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 674748 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0054 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 538726 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |






### Top Genera for Oklahoma  (OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0154 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0112 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 65170 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0107 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 107273 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0086 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 78038 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0084 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 81840 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron |
| 0.0082 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 39044 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0080 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 36984 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0071 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 55678 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0066 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 45600 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0063 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 21873 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |






### Top Genera for Oregon  (OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0179 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 374161 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0129 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 398523 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0118 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 448962 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0116 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 261771 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0104 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 427331 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0089 | [Zonotrichia](https://en.wikipedia.org/wiki/Zonotrichia) | Sparrow | 418194 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow |
| 0.0086 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 580962 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0082 | [Tachycineta](https://en.wikipedia.org/wiki/Tachycineta) | Swallow | 320910 | [Tachycineta thalassina](https://en.wikipedia.org/wiki/Tachycineta_thalassina) | Violet-green Swallow |
| 0.0077 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 183400 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0075 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 630532 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee |






### Top Genera for Pennsylvania  (PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0130 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 947363 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0115 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 620147 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0108 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 557667 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0096 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 836000 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0095 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 864555 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0093 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 828162 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0092 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 456717 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0086 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 874142 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0081 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 643812 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0066 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 812703 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove |






### Top Genera for Rhode Island  (RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0419 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 134161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0107 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 67053 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0099 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 37943 | [Calidris alba](https://en.wikipedia.org/wiki/Calidris_alba) | Sanderling |
| 0.0091 | [Nannopterum](https://en.wikipedia.org/wiki/Nannopterum) | Cormorant | 36787 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant |
| 0.0088 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 34788 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0079 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 20964 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |
| 0.0079 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 23304 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |
| 0.0078 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 18190 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0073 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 25376 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |
| 0.0070 | [Bucephala](https://en.wikipedia.org/wiki/Goldeneye_(duck)) | Goldeneye | 28931 | [Bucephala albeola](https://en.wikipedia.org/wiki/Bucephala_albeola) | Bufflehead |






### Top Genera for South Carolina  (SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0202 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)‡ | Carolina Wren | 251184 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0178 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 195795 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0149 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 309495 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0142 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 191263 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0139 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 212440 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0122 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 241432 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0115 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 227590 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0110 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 153302 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0108 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 396109 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| 0.0066 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 90344 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |






### Top Genera for South Dakota  (SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0161 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 28631 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0132 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 27909 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0096 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)‡* | Pheasant | 15094 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0095 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 22533 | [Tyrannus tyrannus](https://en.wikipedia.org/wiki/Tyrannus_tyrannus) | Eastern Kingbird |
| 0.0094 | [Charadrius](https://en.wikipedia.org/wiki/Charadrius) | Plover | 27418 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| 0.0089 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 37111 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0079 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 45321 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0077 | [Hirundo](https://en.wikipedia.org/wiki/Hirundo) |  | 21965 | [Hirundo rustica](https://en.wikipedia.org/wiki/Hirundo_rustica) | Barn Swallow |
| 0.0074 | [Aythya](https://en.wikipedia.org/wiki/Aythya) | Diving Duck | 22240 | [Aythya americana](https://en.wikipedia.org/wiki/Aythya_americana) | Redhead |
| 0.0070 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 44203 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |






### Top Genera for Tennessee  (TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0201 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0159 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 241408 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0155 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 331627 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0140 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 199634 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0132 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 181103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0108 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 233234 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0105 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 161292 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0078 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 256273 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0059 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 99349 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0059 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 150295 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |






### Top Genera for Texas  (TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0183 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 1153435 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0151 | [Zenaida](https://en.wikipedia.org/wiki/Zenaida_doves) | Mourning Dove | 1669430 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove |
| 0.0133 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 810944 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0106 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 713151 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0102 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 1167665 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0094 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 548178 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0091 | [Quiscalus](https://en.wikipedia.org/wiki/Quiscalus) | Grackle | 1007545 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle |
| 0.0076 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 855533 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0070 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 1274534 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0063 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 537558 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |






### Top Genera for Utah  (UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0197 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0123 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 92492 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0117 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 161076 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| 0.0107 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 204544 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0093 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | 80503 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| 0.0092 | [Falco](https://en.wikipedia.org/wiki/Falcon) | Falcon | 94204 | [Falco sparverius](https://en.wikipedia.org/wiki/Falco_sparverius) | American Kestrel |
| 0.0083 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 85820 | [Spatula cyanoptera](https://en.wikipedia.org/wiki/Spatula_cyanoptera) | Cinnamon Teal |
| 0.0073 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 53017 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| 0.0073 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 134064 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0069 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 137266 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |






### Top Genera for Virginia  (VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0201 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0142 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 728016 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0122 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 475019 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0101 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 843977 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0099 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 344496 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0096 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 506585 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0082 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 339498 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0072 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 386942 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0054 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 195902 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0053 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 174913 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |






### Top Genera for Vermont  (VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0199 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 296739 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0172 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 325282 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0160 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 220081 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0157 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 346101 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler |
| 0.0150 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 239918 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0138 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 240266 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0124 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 223533 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0102 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 212404 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0084 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | 143648 | [Vireo olivaceus](https://en.wikipedia.org/wiki/Vireo_olivaceus) | Red-eyed Vireo |
| 0.0079 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 209167 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |






### Top Genera for Washington  (WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0126 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 470463 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0124 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 331274 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0123 | [Junco](https://en.wikipedia.org/wiki/Junco) | Junco | 548378 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco |
| 0.0117 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 789623 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull |
| 0.0113 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 845174 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee |
| 0.0110 | [Bucephala](https://en.wikipedia.org/wiki/Goldeneye_(duck)) | Goldeneye | 412251 | [Bucephala albeola](https://en.wikipedia.org/wiki/Bucephala_albeola) | Bufflehead |
| 0.0099 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 367041 | [Mareca americana](https://en.wikipedia.org/wiki/Mareca_americana) | American Wigeon |
| 0.0095 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 258496 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0094 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 488880 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0093 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 961797 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |






### Top Genera for Wisconsin  (WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0124 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 692533 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0108 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 557294 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0099 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 231517 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0086 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 606573 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0078 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 491683 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0071 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 640244 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0071 | [Turdus](https://en.wikipedia.org/wiki/Turdus)‡ | Robin | 613134 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0055 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 331300 | [Spizella passerina](https://en.wikipedia.org/wiki/Spizella_passerina) | Chipping Sparrow |
| 0.0051 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 234418 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0050 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 447003 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |






### Top Genera for West Virginia  (WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0150 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 67983 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0147 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0123 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 120310 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0121 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 93312 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0109 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 51062 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0096 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 84023 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0094 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | 62010 | [Vireo olivaceus](https://en.wikipedia.org/wiki/Vireo_olivaceus) | Red-eyed Vireo |
| 0.0094 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 55987 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| 0.0092 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 37014 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0087 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 81694 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |






### Top Genera for Wyoming  (WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0168 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 38495 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0143 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 35925 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0114 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 30812 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0112 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 70656 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0104 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 52070 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| 0.0088 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 53174 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0086 | [Anas](https://en.wikipedia.org/wiki/Anas) | Mallard | 65641 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard |
| 0.0085 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 41090 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0084 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 81776 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| 0.0084 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 29121 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |










## Scores for Bird Species

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name |
|--:|---|---|---|
| AK | 0.0226 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven |
| AL | 0.0216 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| AR | 0.0167 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal |
| AZ | 0.0200 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| CA | 0.0168 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe |
| CO | 0.0137 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker |
| CT | 0.0083 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| DC | 0.0142 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin |
| DE | 0.0097 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| FL | 0.0199 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| GA | 0.0223 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| HI | 0.0434 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| IA | 0.0081 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| ID | 0.0123 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk |
| IL | 0.0096 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| IN | 0.0091 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| KS | 0.0074 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| KY | 0.0084 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| LA | 0.0144 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| MA | 0.0083 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| MD | 0.0087 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow |
| ME | 0.0150 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| MI | 0.0074 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| MN | 0.0111 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| MO | 0.0124 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| MS | 0.0080 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher |
| MT | 0.0272 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| NC | 0.0245 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| ND | 0.0092 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| NE | 0.0099 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle |
| NH | 0.0140 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| NJ | 0.0059 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| NM | 0.0194 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |
| NV | 0.0142 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| NY | 0.0058 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull |
| OH | 0.0044 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer |
| OK | 0.0110 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher |
| OR | 0.0187 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| PA | 0.0104 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| RI | 0.0228 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| SC | 0.0120 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| SD | 0.0181 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark |
| TN | 0.0168 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| TX | 0.0168 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle |
| UT | 0.0103 | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus)‡ | California Gull |
| VA | 0.0059 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| VT | 0.0292 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| WA | 0.0176 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| WI | 0.0103 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch |
| WV | 0.0141 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| WY | 0.0115 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee |





### Top Species for Alaska  (AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0226 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 134933 |
| 0.0208 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  | 100304 |
| 0.0184 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull | 91882 |
| 0.0182 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 114247 |
| 0.0126 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 69491 |
| 0.0114 | [Anas acuta](https://en.wikipedia.org/wiki/Anas_acuta) | Northern Pintail | 62130 |
| 0.0113 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake | 54048 |
| 0.0113 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll | 57086 |
| 0.0104 | [Sterna paradisaea](https://en.wikipedia.org/wiki/Sterna_paradisaea) | Arctic Tern | 49261 |
| 0.0102 | [Anas crecca](https://en.wikipedia.org/wiki/Anas_crecca) | Green-winged Teal | 61709 |






### Top Species for Alabama  (AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0216 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 130529 |
| 0.0194 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 127076 |
| 0.0169 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 167600 |
| 0.0165 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 101376 |
| 0.0131 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 84368 |
| 0.0127 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 100822 |
| 0.0117 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 104294 |
| 0.0115 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 69546 |
| 0.0106 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 59435 |
| 0.0096 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 133341 |






### Top Species for Arkansas  (AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0215 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 98316 |
| 0.0167 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 133523 |
| 0.0164 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 91280 |
| 0.0164 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 93388 |
| 0.0124 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 85916 |
| 0.0120 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 109252 |
| 0.0113 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 68963 |
| 0.0103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 57569 |
| 0.0088 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 56717 |
| 0.0084 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 40627 |






### Top Species for Arizona  (AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0200 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.0181 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 431522 |
| 0.0172 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 386191 |
| 0.0143 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 592799 |
| 0.0129 | [Toxostoma curvirostre](https://en.wikipedia.org/wiki/Toxostoma_curvirostre) | Curve-billed Thrasher | 293199 |
| 0.0129 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 323152 |
| 0.0126 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 313824 |
| 0.0126 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 281419 |
| 0.0118 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee | 262829 |
| 0.0110 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 371565 |






### Top Species for California  (CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0168 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe | 186372 |
| 0.0137 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 164610 |
| 0.0135 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 151564 |
| 0.0117 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee | 124793 |
| 0.0096 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit | 112390 |
| 0.0089 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 137305 |
| 0.0088 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird | 106234 |
| 0.0085 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 109742 |
| 0.0082 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 90542 |
| 0.0073 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 108139 |






### Top Species for Colorado  (CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0201 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 387306 |
| 0.0137 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 443193 |
| 0.0136 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 292188 |
| 0.0122 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 240927 |
| 0.0118 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 431640 |
| 0.0101 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 375157 |
| 0.0097 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 334034 |
| 0.0096 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 174912 |
| 0.0091 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 174321 |
| 0.0087 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 422090 |






### Top Species for Connecticut  (CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0133 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 240563 |
| 0.0114 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 272058 |
| 0.0098 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 295889 |
| 0.0089 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 262634 |
| 0.0083 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 162362 |
| 0.0081 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 194557 |
| 0.0079 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 139243 |
| 0.0071 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 292446 |
| 0.0070 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 225415 |
| 0.0065 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 191002 |






### Top Species for District of Columbia  (DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0164 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 53975 |
| 0.0154 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 41998 |
| 0.0142 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 62170 |
| 0.0138 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 42950 |
| 0.0135 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26969 |
| 0.0129 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 57641 |
| 0.0113 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 24475 |
| 0.0099 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 28883 |
| 0.0097 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 30486 |
| 0.0097 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull | 31610 |






### Top Species for Delaware  (DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0109 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 77729 |
| 0.0097 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 53074 |
| 0.0096 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 94945 |
| 0.0094 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 84664 |
| 0.0073 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 37786 |
| 0.0065 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 54775 |
| 0.0063 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey | 48752 |
| 0.0059 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 37426 |
| 0.0059 | [Ardea herodias](https://en.wikipedia.org/wiki/Ardea_herodias) | Great Blue Heron | 73996 |
| 0.0055 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 49968 |






### Top Species for Florida  (FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0199 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 748541 |
| 0.0165 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 769348 |
| 0.0151 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 832859 |
| 0.0149 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 553383 |
| 0.0146 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey | 678520 |
| 0.0146 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 558321 |
| 0.0143 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle | 540152 |
| 0.0136 | [Setophaga palmarum](https://en.wikipedia.org/wiki/Setophaga_palmarum) | Palm Warbler | 553185 |
| 0.0136 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 569544 |
| 0.0127 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 886664 |






### Top Species for Georgia  (GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0223 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 395603 |
| 0.0217 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 351685 |
| 0.0175 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 345328 |
| 0.0169 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |
| 0.0169 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 477796 |
| 0.0148 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 288903 |
| 0.0139 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 248961 |
| 0.0136 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 176715 |
| 0.0133 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 317177 |
| 0.0120 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 176004 |






### Top Species for Hawaii  (HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0614 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis)* | Common Myna | 89440 |
| 0.0569 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* |  | 82840 |
| 0.0538 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* |  | 78346 |
| 0.0434 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove | 63162 |
| 0.0375 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover | 54637 |
| 0.0325 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret | 48950 |
| 0.0273 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata)* |  | 39698 |
| 0.0245 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane | 35689 |
| 0.0206 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 48637 |
| 0.0201 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  | 29234 |






### Top Species for Iowa  (IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0106 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 88770 |
| 0.0099 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 107540 |
| 0.0093 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 69406 |
| 0.0091 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 73023 |
| 0.0088 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 84859 |
| 0.0082 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 68964 |
| 0.0082 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 79689 |
| 0.0081 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren | 44452 |
| 0.0072 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 103673 |
| 0.0070 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 80952 |






### Top Species for Idaho  (ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0243 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |
| 0.0126 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 83497 |
| 0.0123 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 96641 |
| 0.0114 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 65282 |
| 0.0113 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 53065 |
| 0.0108 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 116847 |
| 0.0108 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 100127 |
| 0.0105 | [Falco sparverius](https://en.wikipedia.org/wiki/Falco_sparverius) | American Kestrel | 65361 |
| 0.0082 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 140857 |
| 0.0080 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 42774 |






### Top Species for Illinois  (IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0103 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 637278 |
| 0.0096 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 509568 |
| 0.0095 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 650537 |
| 0.0091 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 419893 |
| 0.0084 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 499718 |
| 0.0075 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 480060 |
| 0.0072 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 446248 |
| 0.0064 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 430124 |
| 0.0061 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull | 306414 |
| 0.0057 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 359493 |






### Top Species for Indiana  (IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0128 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 350530 |
| 0.0122 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 192755 |
| 0.0117 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 224909 |
| 0.0109 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 223851 |
| 0.0105 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 231871 |
| 0.0091 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 247415 |
| 0.0079 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 249012 |
| 0.0065 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 263938 |
| 0.0058 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 181510 |
| 0.0052 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 117217 |






### Top Species for Kansas  (KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0081 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 105980 |
| 0.0074 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 83749 |
| 0.0074 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 57726 |
| 0.0069 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 43167 |
| 0.0065 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 114945 |
| 0.0064 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 171877 |
| 0.0059 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer | 82817 |
| 0.0054 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 36284 |
| 0.0052 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal | 46429 |
| 0.0044 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 155779 |






### Top Species for Kentucky  (KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0205 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0167 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 158980 |
| 0.0150 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 105736 |
| 0.0138 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 98073 |
| 0.0106 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 95179 |
| 0.0100 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 121971 |
| 0.0084 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 101534 |
| 0.0084 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 84477 |
| 0.0081 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 52593 |
| 0.0081 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 121295 |






### Top Species for Louisiana  (LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0160 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 164645 |
| 0.0144 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 133593 |
| 0.0116 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 123872 |
| 0.0090 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret | 78150 |
| 0.0090 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 126615 |
| 0.0078 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 63812 |
| 0.0074 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 65839 |
| 0.0063 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret | 50157 |
| 0.0063 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 52377 |
| 0.0062 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike | 50080 |






### Top Species for Massachusetts  (MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0149 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 702147 |
| 0.0121 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 411691 |
| 0.0110 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 497003 |
| 0.0100 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 682228 |
| 0.0099 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 625921 |
| 0.0083 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 248999 |
| 0.0073 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 556268 |
| 0.0072 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 346468 |
| 0.0069 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 418553 |
| 0.0066 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 399481 |






### Top Species for Maryland  (MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0173 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 543555 |
| 0.0160 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0121 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 681139 |
| 0.0106 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 424167 |
| 0.0093 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 434872 |
| 0.0087 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 326126 |
| 0.0080 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 402965 |
| 0.0074 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 203375 |
| 0.0073 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 274036 |
| 0.0072 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 317285 |






### Top Species for Maine  (ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0217 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 250547 |
| 0.0188 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 312621 |
| 0.0150 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 340077 |
| 0.0131 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 126024 |
| 0.0109 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 252247 |
| 0.0103 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 117454 |
| 0.0094 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer)† | Common Loon | 107073 |
| 0.0092 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 240739 |
| 0.0081 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch | 116498 |
| 0.0078 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant | 143391 |






### Top Species for Michigan  (MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0153 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 672265 |
| 0.0107 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 661443 |
| 0.0093 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 447738 |
| 0.0091 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 565721 |
| 0.0078 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 524815 |
| 0.0074 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 532312 |
| 0.0072 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 492756 |
| 0.0071 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 491750 |
| 0.0068 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 420150 |
| 0.0064 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)‡ | American Robin | 653561 |






### Top Species for Minnesota  (MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0242 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 443332 |
| 0.0134 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 398422 |
| 0.0111 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 249129 |
| 0.0092 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 168673 |
| 0.0089 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 271335 |
| 0.0086 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 267907 |
| 0.0082 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 311082 |
| 0.0080 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 156850 |
| 0.0080 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 270765 |
| 0.0073 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 269788 |






### Top Species for Missouri  (MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0149 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 328095 |
| 0.0129 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 209758 |
| 0.0124 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 221133 |
| 0.0097 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 175152 |
| 0.0086 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)‡ | Eastern Bluebird | 133658 |
| 0.0082 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 247494 |
| 0.0077 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 98416 |
| 0.0068 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 197101 |
| 0.0058 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 119362 |
| 0.0054 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 156699 |






### Top Species for Mississippi  (MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0173 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 66564 |
| 0.0125 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 57768 |
| 0.0114 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 47154 |
| 0.0096 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 80897 |
| 0.0093 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 35858 |
| 0.0092 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 40007 |
| 0.0090 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 55068 |
| 0.0088 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 29022 |
| 0.0086 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 36547 |
| 0.0080 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 28631 |






### Top Species for Montana  (MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0272 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 151463 |
| 0.0156 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 112518 |
| 0.0122 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 123216 |
| 0.0118 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 69546 |
| 0.0100 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 68386 |
| 0.0093 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 52991 |
| 0.0085 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 124814 |
| 0.0084 | [Spinus pinus](https://en.wikipedia.org/wiki/Spinus_pinus) | Pine Siskin | 59521 |
| 0.0081 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch | 66612 |
| 0.0081 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 162755 |






### Top Species for North Carolina  (NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0245 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 463009 |
| 0.0229 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 484010 |
| 0.0176 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 416651 |
| 0.0155 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 295774 |
| 0.0145 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 307886 |
| 0.0142 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 535006 |
| 0.0109 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 345214 |
| 0.0104 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 281345 |
| 0.0097 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 154113 |
| 0.0083 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 157308 |






### Top Species for North Dakota  (ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0144 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 33762 |
| 0.0106 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 24049 |
| 0.0092 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal | 24509 |
| 0.0087 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 40765 |
| 0.0087 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 19291 |
| 0.0080 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer | 33125 |
| 0.0080 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 18180 |
| 0.0074 | [Spatula clypeata](https://en.wikipedia.org/wiki/Spatula_clypeata) | Northern Shoveler | 21962 |
| 0.0071 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 47174 |
| 0.0071 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall | 21431 |






### Top Species for Nebraska  (NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0132 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 42141 |
| 0.0129 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 103158 |
| 0.0102 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 38303 |
| 0.0099 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 58694 |
| 0.0081 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 57657 |
| 0.0081 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 69060 |
| 0.0080 | [Buteo jamaicensis](https://en.wikipedia.org/wiki/Buteo_jamaicensis) | Red-tailed Hawk | 49369 |
| 0.0076 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 69715 |
| 0.0069 | [Zenaida macroura](https://en.wikipedia.org/wiki/Zenaida_macroura) | Mourning Dove | 80260 |
| 0.0069 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren | 33982 |






### Top Species for New Hampshire  (NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0252 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 198394 |
| 0.0140 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 163229 |
| 0.0120 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 113296 |
| 0.0116 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 137901 |
| 0.0115 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 107536 |
| 0.0094 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 74627 |
| 0.0079 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch | 61610 |
| 0.0075 | [Sayornis phoebe](https://en.wikipedia.org/wiki/Sayornis_phoebe) | Eastern Phoebe | 66633 |
| 0.0067 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 107390 |
| 0.0067 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 140981 |






### Top Species for New Jersey  (NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0083 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 288779 |
| 0.0078 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 211320 |
| 0.0071 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 193668 |
| 0.0067 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 340688 |
| 0.0063 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 288141 |
| 0.0059 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 149892 |
| 0.0056 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 268400 |
| 0.0056 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 445882 |
| 0.0050 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 319127 |
| 0.0050 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 157113 |






### Top Species for New Mexico  (NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0194 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 239709 |
| 0.0164 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 137112 |
| 0.0150 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 132679 |
| 0.0145 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 152761 |
| 0.0144 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 190730 |
| 0.0135 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 114032 |
| 0.0126 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 100938 |
| 0.0114 | [Archilochus alexandri](https://en.wikipedia.org/wiki/Archilochus_alexandri) | Black-chinned Hummingbird | 90799 |
| 0.0112 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 113186 |
| 0.0099 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 97785 |






### Top Species for Nevada  (NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0142 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot | 53207 |
| 0.0139 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 51745 |
| 0.0130 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 55205 |
| 0.0106 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 36238 |
| 0.0094 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 29373 |
| 0.0094 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle | 33286 |
| 0.0087 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 27884 |
| 0.0081 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 32858 |
| 0.0080 | [Oxyura jamaicensis](https://en.wikipedia.org/wiki/Oxyura_jamaicensis) | Ruddy Duck | 29300 |
| 0.0079 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 24428 |






### Top Species for New York  (NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0107 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 1033854 |
| 0.0098 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 1158294 |
| 0.0078 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 946282 |
| 0.0075 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 598555 |
| 0.0067 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 929023 |
| 0.0066 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 487807 |
| 0.0065 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 895261 |
| 0.0063 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 1117636 |
| 0.0063 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 1176480 |
| 0.0061 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 660580 |






### Top Species for Ohio  (OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0111 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 791329 |
| 0.0093 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 519777 |
| 0.0080 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 663248 |
| 0.0079 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 579046 |
| 0.0069 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 420642 |
| 0.0068 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 577543 |
| 0.0067 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 430730 |
| 0.0067 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 724685 |
| 0.0065 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 524738 |
| 0.0064 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 558210 |






### Top Species for Oklahoma  (OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0144 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 69674 |
| 0.0113 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 65170 |
| 0.0110 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher | 37937 |
| 0.0110 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 107206 |
| 0.0081 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 36943 |
| 0.0071 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 44136 |
| 0.0071 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 55678 |
| 0.0070 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 29688 |
| 0.0063 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 21873 |
| 0.0060 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 72196 |






### Top Species for Oregon  (OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0187 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |
| 0.0175 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 389415 |
| 0.0142 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 303921 |
| 0.0120 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 448962 |
| 0.0117 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 261404 |
| 0.0107 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 540183 |
| 0.0105 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 427331 |
| 0.0085 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow | 178500 |
| 0.0077 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren | 183400 |
| 0.0072 | [Tachycineta thalassina](https://en.wikipedia.org/wiki/Tachycineta_thalassina) | Violet-green Swallow | 162899 |






### Top Species for Pennsylvania  (PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0132 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 947363 |
| 0.0125 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 620147 |
| 0.0114 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 836000 |
| 0.0109 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 625797 |
| 0.0108 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 557667 |
| 0.0104 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 743436 |
| 0.0092 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 456717 |
| 0.0090 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 544357 |
| 0.0089 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 874134 |
| 0.0088 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 690654 |






### Top Species for Rhode Island  (RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0228 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 60029 |
| 0.0164 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 39719 |
| 0.0118 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 60608 |
| 0.0097 | [Nannopterum auritum](https://en.wikipedia.org/wiki/Nannopterum_auritum) | Double-crested Cormorant | 36787 |
| 0.0088 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 34788 |
| 0.0084 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 50314 |
| 0.0077 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 17732 |
| 0.0076 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 38127 |
| 0.0075 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 18958 |
| 0.0073 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey | 25376 |






### Top Species for South Carolina  (SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0208 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 230968 |
| 0.0202 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)‡ | Carolina Wren | 251184 |
| 0.0152 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 309495 |
| 0.0148 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 212440 |
| 0.0143 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 191263 |
| 0.0120 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 153302 |
| 0.0105 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 191190 |
| 0.0100 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 103051 |
| 0.0089 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 120980 |
| 0.0077 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 90344 |






### Top Species for South Dakota  (SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0181 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0102 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 30043 |
| 0.0098 | [Charadrius vociferus](https://en.wikipedia.org/wiki/Charadrius_vociferus) | Killdeer | 25307 |
| 0.0096 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant | 15094 |
| 0.0089 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 37111 |
| 0.0084 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal | 15553 |
| 0.0081 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 45321 |
| 0.0077 | [Hirundo rustica](https://en.wikipedia.org/wiki/Hirundo_rustica) | Barn Swallow | 21965 |
| 0.0066 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 14234 |
| 0.0064 | [Tyrannus tyrannus](https://en.wikipedia.org/wiki/Tyrannus_tyrannus) | Eastern Kingbird | 14363 |






### Top Species for Tennessee  (TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0231 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0201 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 264394 |
| 0.0168 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 241408 |
| 0.0158 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 331627 |
| 0.0142 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 181101 |
| 0.0140 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 199634 |
| 0.0137 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 161073 |
| 0.0113 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 208456 |
| 0.0095 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 256273 |
| 0.0071 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 259006 |






### Top Species for Texas  (TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0184 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 1153426 |
| 0.0168 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle | 794651 |
| 0.0155 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 742445 |
| 0.0094 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture | 548178 |
| 0.0083 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 596851 |
| 0.0082 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse | 365712 |
| 0.0076 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 855529 |
| 0.0072 | [Melanerpes aurifrons](https://en.wikipedia.org/wiki/Melanerpes_aurifrons) | Golden-fronted Woodpecker | 326325 |
| 0.0072 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 327041 |
| 0.0068 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 592533 |






### Top Species for Utah  (UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0197 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 129642 |
| 0.0163 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 132736 |
| 0.0123 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 92453 |
| 0.0104 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch | 138061 |
| 0.0103 | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus)‡ | California Gull | 65861 |
| 0.0093 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot | 80503 |
| 0.0090 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 63292 |
| 0.0086 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 62521 |
| 0.0084 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 53017 |
| 0.0083 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 73078 |






### Top Species for Virginia  (VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0201 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0186 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0145 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 728016 |
| 0.0132 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 475019 |
| 0.0109 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 344469 |
| 0.0106 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 459930 |
| 0.0083 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 339498 |
| 0.0075 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 300867 |
| 0.0072 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture | 386942 |
| 0.0065 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 222621 |






### Top Species for Vermont  (VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0292 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 295586 |
| 0.0167 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 239918 |
| 0.0151 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 247470 |
| 0.0130 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 196825 |
| 0.0114 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 149624 |
| 0.0103 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 182074 |
| 0.0099 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 104397 |
| 0.0082 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 209167 |
| 0.0077 | [Sayornis phoebe](https://en.wikipedia.org/wiki/Sayornis_phoebe) | Eastern Phoebe | 91900 |
| 0.0074 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 119560 |






### Top Species for Washington  (WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0176 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 470005 |
| 0.0125 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 331149 |
| 0.0124 | [Junco hyemalis](https://en.wikipedia.org/wiki/Junco_hyemalis) | Dark-eyed Junco | 548378 |
| 0.0120 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 313794 |
| 0.0112 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull | 281727 |
| 0.0110 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 654472 |
| 0.0107 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 268543 |
| 0.0095 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren | 258496 |
| 0.0095 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 488880 |
| 0.0088 | [Zonotrichia leucophrys](https://en.wikipedia.org/wiki/Zonotrichia_leucophrys) | White-crowned Sparrow | 295210 |






### Top Species for Wisconsin  (WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0167 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 639564 |
| 0.0103 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 538617 |
| 0.0099 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 231517 |
| 0.0098 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 416266 |
| 0.0080 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 603469 |
| 0.0078 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird | 491683 |
| 0.0074 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)‡ | American Robin | 613134 |
| 0.0068 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 252839 |
| 0.0067 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 439694 |
| 0.0058 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 439424 |






### Top Species for West Virginia  (WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0157 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 71638 |
| 0.0150 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 67983 |
| 0.0141 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 51061 |
| 0.0124 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 93312 |
| 0.0113 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 84023 |
| 0.0113 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 49621 |
| 0.0107 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 89653 |
| 0.0106 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow | 75626 |
| 0.0092 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker | 37014 |
| 0.0091 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 58475 |






### Top Species for Wyoming  (WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0196 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 52152 |
| 0.0168 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 38495 |
| 0.0144 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 35919 |
| 0.0135 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 30804 |
| 0.0115 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 25326 |
| 0.0114 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius)† | American Robin | 70656 |
| 0.0099 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 21085 |
| 0.0094 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 52099 |
| 0.0086 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus)† | Northern Flicker | 41090 |
| 0.0086 | [Anas platyrhynchos](https://en.wikipedia.org/wiki/Anas_platyrhynchos) | Mallard | 48538 |






