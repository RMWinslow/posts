---
title: "Bird Scores - Phi"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
math: katex
---


This BIRDUP scoring system uses the [phi coefficient](https://en.wikipedia.org/wiki/Phi_coefficient). 
It's essentially the correlation across observations between a bird and a state.

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

Here, the Bird Score for a pair of state and bird is 

$$\phi = \frac{\nTotal\times\nJoint - \nState\times\nBird}{\sqrt{\nState\times\nBird\times(\nTotal-\nState)\times(\nTotal-\nBird)}}$$

For the top scores, the formula is equivalent to

$$\phi = {\Delta p}^{0.5}\times{J}^{0.5}$$

where $J$ is the [informedness](informedness) and $\Delta p$ is the [markedness](markedness).  
If the exponents are adjusted, then we get my [Weighted Phi](weightedphi) metric.


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

| State | Bird | Common Name | Example Species | Common Name |
|--:|---|---|---|---|
| AK | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet |
| AL | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| AR | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| AZ | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| CA | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| CO | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| CT | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| DC | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| DE | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| FL | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| GA | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| HI | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| IA | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| ID | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| IL | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| KS | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| KY | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| LA | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| MA | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter |
| MD | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| ME | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| MI | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| MN | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| MO | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| MS | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| MT | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| NC | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| ND | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| NH | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch |
| NJ | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| NM | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| NV | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| NY | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| OH | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| OK | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| OR | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| PA | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| RI | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| SC | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| SD | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| TX | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| UT | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| VA | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| VT | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| WA | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| WI | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| WY | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |





### Top Scoring Bird Genera for Alaska (AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0806 | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | 31286 | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet |
| 0.0717 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 48084 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned Puffin |
| 0.0710 | [Rissa](https://en.wikipedia.org/wiki/Kittiwake) | Kittiwake | 60795 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake |
| 0.0529 | [Stercorarius](https://en.wikipedia.org/wiki/Stercorarius) |  | 52502 | [Stercorarius longicaudus](https://en.wikipedia.org/wiki/Stercorarius_longicaudus) | Long-tailed Jaeger |
| 0.0476 | [Brachyramphus](https://en.wikipedia.org/wiki/Brachyramphus) |  | 32064 | [Brachyramphus marmoratus](https://en.wikipedia.org/wiki/Brachyramphus_marmoratus) | Marbled Murrelet |
| 0.0459 | [Motacilla](https://en.wikipedia.org/wiki/Motacilla) |  | 11750 | [Motacilla tschutschensis](https://en.wikipedia.org/wiki/Motacilla_tschutschensis) | Eastern Yellow Wagtail |
| 0.0458 | [Uria](https://en.wikipedia.org/wiki/Uria) |  | 45365 | [Uria lomvia](https://en.wikipedia.org/wiki/Uria_lomvia) | Thick-billed Murre |
| 0.0455 | [Lagopus](https://en.wikipedia.org/wiki/Lagopus)‡ |  | 20473 | [Lagopus lagopus](https://en.wikipedia.org/wiki/Lagopus_lagopus) | Willow Ptarmigan |
| 0.0436 | [Calcarius](https://en.wikipedia.org/wiki/Calcarius) | Longspur | 48011 | [Calcarius lapponicus](https://en.wikipedia.org/wiki/Calcarius_lapponicus) | Lapland Longspur |
| 0.0399 | [Histrionicus](https://en.wikipedia.org/wiki/Histrionicus) |  | 43598 | [Histrionicus histrionicus](https://en.wikipedia.org/wiki/Histrionicus_histrionicus) | Harlequin Duck |






### Top Scoring Bird Genera for Alabama (AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0179 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0152 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 127076 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0115 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 59435 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0109 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 84368 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0101 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 24522 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0092 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 60847 | [Passerina caerulea](https://en.wikipedia.org/wiki/Passerina_caerulea) | Blue Grosbeak |
| 0.0088 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 167600 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0086 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 39243 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0086 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 127153 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0085 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 100822 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Scoring Bird Genera for Arkansas (AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0115 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0100 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 55044 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0100 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 93388 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0093 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10710 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0084 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 68963 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0078 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 133523 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0077 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 101947 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0075 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 57596 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0070 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 10491 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0062 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 17013 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |






### Top Scoring Bird Genera for Arizona (AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1077 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 386191 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0918 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 388898 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee |
| 0.0804 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 200508 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.0707 | [Cynanthus](https://en.wikipedia.org/wiki/Cynanthus) | Hummingbird | 169527 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed Hummingbird |
| 0.0691 | [Campylorhynchus](https://en.wikipedia.org/wiki/Campylorhynchus)‡ |  | 200611 | [Campylorhynchus brunneicapillus](https://en.wikipedia.org/wiki/Campylorhynchus_brunneicapillus) | Cactus Wren |
| 0.0613 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 393373 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0603 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 296630 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0600 | [Pyrocephalus](https://en.wikipedia.org/wiki/Pyrocephalus) |  | 194003 | [Pyrocephalus rubinus](https://en.wikipedia.org/wiki/Pyrocephalus_rubinus) | Vermilion Flycatcher |
| 0.0552 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 137441 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0452 | [Eugenes](https://en.wikipedia.org/wiki/Eugenes) |  | 59354 | [Eugenes fulgens](https://en.wikipedia.org/wiki/Eugenes_fulgens) | Rivoli's Hummingbird |






### Top Scoring Bird Genera for California (CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0546 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 57649 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.0423 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 129054 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| 0.0390 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 176961 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0384 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 153459 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0365 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 112390 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0334 | [Elanus](https://en.wikipedia.org/wiki/Elanus) |  | 40693 | [Elanus leucurus](https://en.wikipedia.org/wiki/Elanus_leucurus) | White-tailed Kite |
| 0.0255 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 70336 | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| 0.0238 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 106640 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0235 | [Numenius](https://en.wikipedia.org/wiki/Numenius) |  | 56560 | [Numenius americanus](https://en.wikipedia.org/wiki/Numenius_americanus) | Long-billed Curlew |
| 0.0214 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)‡ | Crested Quail | 80309 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |






### Top Scoring Bird Genera for Colorado (CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0665 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0415 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 210475 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0362 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 292668 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0266 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 73348 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0256 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 241188 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0253 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 92411 | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| 0.0198 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)‡ | Lark Bunting | 28847 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0197 | [Colaptes](https://en.wikipedia.org/wiki/Colaptes)† | Woodpecker | 443193 | [Colaptes auratus](https://en.wikipedia.org/wiki/Colaptes_auratus) | Northern Flicker |
| 0.0180 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 260926 | [Mareca strepera](https://en.wikipedia.org/wiki/Mareca_strepera) | Gadwall |
| 0.0173 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 21537 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |






### Top Scoring Bird Genera for Connecticut (CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0136 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 240563 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0112 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 162362 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0092 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 339172 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0077 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 64233 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0077 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 47578 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0073 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 22502 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0071 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 302089 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0068 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 187078 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0066 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 295889 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0064 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 21206 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |






### Top Scoring Bird Genera for District of Columbia (DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0088 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 24475 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0075 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 41998 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0063 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 53975 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0060 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0050 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 30486 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0044 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 62170 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0041 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 57641 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0040 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 25165 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0038 | [Polioptila](https://en.wikipedia.org/wiki/Polioptila) | Gnatcatcher | 16764 | [Polioptila caerulea](https://en.wikipedia.org/wiki/Polioptila_caerulea) | Blue-gray Gnatcatcher |
| 0.0035 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 74079 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  |






### Top Scoring Bird Genera for Delaware (DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0132 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 53108 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0130 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 101378 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0114 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 42296 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0096 | [Tringa](https://en.wikipedia.org/wiki/Tringa) | Tattlers | 71586 | [Tringa melanoleuca](https://en.wikipedia.org/wiki/Tringa_melanoleuca) | Greater Yellowlegs |
| 0.0087 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 16285 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0082 | [Limnodromus](https://en.wikipedia.org/wiki/Limnodromus) |  | 21701 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher |
| 0.0082 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 10452 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0076 | [Progne](https://en.wikipedia.org/wiki/Progne) |  | 26358 | [Progne subis](https://en.wikipedia.org/wiki/Progne_subis) | Purple Martin |
| 0.0074 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 84664 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0071 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 48752 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |






### Top Scoring Bird Genera for Florida (FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1158 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 1584817 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| 0.1053 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 748541 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0985 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 553383 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0706 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 284639 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0664 | [Aramus](https://en.wikipedia.org/wiki/Aramus) |  | 184399 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin |
| 0.0634 | [Gallinula](https://en.wikipedia.org/wiki/Gallinula) |  | 389658 | [Gallinula galeata](https://en.wikipedia.org/wiki/Gallinula_galeata) | Common Gallinule |
| 0.0501 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 314435 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0497 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 312301 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0463 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 678520 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |
| 0.0459 | [Elanoides](https://en.wikipedia.org/wiki/Elanoides) |  | 111055 | [Elanoides forficatus](https://en.wikipedia.org/wiki/Elanoides_forficatus) | Swallow-tailed Kite |






### Top Scoring Bird Genera for Georgia (GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0293 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0211 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | 179633 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0207 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 288903 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0203 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 264143 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0201 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 345328 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0195 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 249060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0157 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 377667 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0147 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 477796 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0130 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 208616 | [Sayornis phoebe](https://en.wikipedia.org/wiki/Sayornis_phoebe) | Eastern Phoebe |
| 0.0126 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 113127 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |






### Top Scoring Bird Genera for Hawaii (HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2383 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)* | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus) |  |
| 0.2324 | [Acridotheres](https://en.wikipedia.org/wiki/Acridotheres)* | Myna | 89440 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis) | Common Myna |
| 0.2317 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)* |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata) |  |
| 0.1972 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata) |  |
| 0.1564 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | 35689 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| 0.1530 | [Chlorodrepanis](https://en.wikipedia.org/wiki/Chlorodrepanis) |  | 34136 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  |
| 0.1340 | [Pycnonotus](https://en.wikipedia.org/wiki/Pycnonotus) |  | 33210 | [Pycnonotus cafer](https://en.wikipedia.org/wiki/Pycnonotus_cafer) |  |
| 0.1327 | [Estrilda](https://en.wikipedia.org/wiki/Estrilda) |  | 25798 | [Estrilda astrild](https://en.wikipedia.org/wiki/Estrilda_astrild) |  |
| 0.1240 | [Sicalis](https://en.wikipedia.org/wiki/Sicalis) |  | 23701 | [Sicalis flaveola](https://en.wikipedia.org/wiki/Sicalis_flaveola) |  |
| 0.1176 | [Padda](https://en.wikipedia.org/wiki/Padda) |  | 20197 | [Padda oryzivora](https://en.wikipedia.org/wiki/Padda_oryzivora) |  |






### Top Scoring Bird Genera for Iowa (IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0125 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 21293 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0115 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 15850 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0073 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 97621 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0065 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 76639 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| 0.0058 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 45929 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0057 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 42291 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0049 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 40013 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0045 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 88043 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0045 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 108897 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0045 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 107540 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Scoring Bird Genera for Idaho (ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0408 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0235 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 53404 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |
| 0.0154 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 65286 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0128 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 38584 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0126 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 23444 | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| 0.0111 | [Falco](https://en.wikipedia.org/wiki/Falcon) | Falcon | 81038 | [Falco sparverius](https://en.wikipedia.org/wiki/Falco_sparverius) | American Kestrel |
| 0.0102 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18567 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0097 | [Buteo](https://en.wikipedia.org/wiki/Buteo) | Hawk | 135819 | [Buteo swainsoni](https://en.wikipedia.org/wiki/Buteo_swainsoni) | Swainson's Hawk |
| 0.0090 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6303 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0088 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18645 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |






### Top Scoring Bird Genera for Illinois (IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0147 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 434206 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0127 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 18756 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0124 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163030 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0121 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 46626 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0112 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 637278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0112 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 520240 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0106 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 499718 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0105 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 94643 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0103 | [Hydroprogne](https://en.wikipedia.org/wiki/Hydroprogne) |  | 70704 | [Hydroprogne caspia](https://en.wikipedia.org/wiki/Hydroprogne_caspia) | Caspian Tern |
| 0.0100 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 650537 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |






### Top Scoring Bird Genera for Indiana (IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0118 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 224909 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0116 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 282027 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0101 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 350530 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0079 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 326501 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0069 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 83946 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0069 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7607 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0068 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 173525 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| 0.0065 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 247310 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0062 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 181515 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0060 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | 115449 | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |






### Top Scoring Bird Genera for Kansas (KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0204 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 36284 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0172 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 92201 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0138 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 22554 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0105 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 24003 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0098 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 88177 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0096 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 86342 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird |
| 0.0093 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 34440 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |
| 0.0091 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 14481 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0082 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 8401 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0079 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 32432 | [Anser albifrons](https://en.wikipedia.org/wiki/Anser_albifrons) | Greater White-fronted Goose |






### Top Scoring Bird Genera for Kentucky (KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0105 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 98073 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0100 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 105736 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0084 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 158980 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0075 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 51917 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0066 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 35716 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0066 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 109288 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0058 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 84477 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0051 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 101534 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0050 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8107 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0049 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10504 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |






### Top Scoring Bird Genera for Louisiana (LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0255 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 171844 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0182 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 63812 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0177 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 50157 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0176 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 27044 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0165 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 164645 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0142 | [Lanius](https://en.wikipedia.org/wiki/Lanius) | Shrike | 50080 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike |
| 0.0133 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 37903 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0127 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 67571 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0127 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 223799 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0124 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 28529 | [Dendrocygna autumnalis](https://en.wikipedia.org/wiki/Dendrocygna_autumnalis) | Black-bellied Whistling-Duck |






### Top Scoring Bird Genera for Massachusetts (MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0343 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 147688 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0245 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 193084 | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter |
| 0.0232 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 953627 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0166 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 497003 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0146 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 346468 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0144 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 16342 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0139 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 28983 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0134 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 45864 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0131 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 17049 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.0127 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 731554 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |






### Top Scoring Bird Genera for Maryland (MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0289 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0162 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 184681 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0149 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 424167 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0133 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 681139 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0127 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 317285 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0121 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 274339 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0121 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 402965 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0093 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 454993 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0086 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 82855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0078 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 176493 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |






### Top Scoring Bird Genera for Maine (ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0507 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 127240 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0300 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 58921 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot |
| 0.0225 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 470161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0191 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 117292 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |
| 0.0177 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 17505 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  |
| 0.0172 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 593940 | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler |
| 0.0151 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 18634 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0148 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 14447 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0141 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 71853 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |
| 0.0127 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 25405 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |






### Top Scoring Bird Genera for Michigan (MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0261 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 236621 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0248 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 176499 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0147 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 125158 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0127 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 586777 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0115 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 706919 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0107 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 661443 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0103 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147923 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0099 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 532312 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0090 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 167208 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0089 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 528609 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |






### Top Scoring Bird Genera for Minnesota (MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0140 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 436581 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0139 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 46603 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0128 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 156850 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0126 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 121146 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0121 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 448373 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0117 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 329350 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0099 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 79849 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| 0.0079 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 32330 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll |
| 0.0069 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 275994 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0069 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 48205 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |






### Top Scoring Bird Genera for Missouri (MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0149 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 34191 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0136 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 275131 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0124 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 209758 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0113 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 113686 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0111 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 328095 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0109 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 175152 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0098 | [Sialia](https://en.wikipedia.org/wiki/Sialia)‡ | Bluebird | 133730 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0097 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 21081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0095 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 42272 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0092 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 46182 | [Anser albifrons](https://en.wikipedia.org/wiki/Anser_albifrons) | Greater White-fronted Goose |






### Top Scoring Bird Genera for Mississippi (MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0110 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 66564 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0101 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 17938 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0098 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 30763 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0094 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 29491 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0081 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 8333 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0081 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 41057 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0075 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 57768 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0073 | [Ardea](https://en.wikipedia.org/wiki/Ardea_(bird)) | Heron | 83150 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| 0.0073 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8279 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0065 | [Sternula](https://en.wikipedia.org/wiki/Sternula) |  | 7879 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |






### Top Scoring Bird Genera for Montana (MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0490 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0243 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 24361 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0157 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 32921 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0156 | [Pooecetes](https://en.wikipedia.org/wiki/Pooecetes) |  | 31238 | [Pooecetes gramineus](https://en.wikipedia.org/wiki/Pooecetes_gramineus) | Vesper Sparrow |
| 0.0156 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 23231 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0145 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 68395 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0143 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 17889 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0134 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 69555 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0133 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 25367 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0130 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 7149 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |






### Top Scoring Bird Genera for North Carolina (NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0329 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0224 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 307887 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0222 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 416651 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0198 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 295792 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0158 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 281345 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0150 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 161868 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0138 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 12415 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0135 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 535006 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0133 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | 7392 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  |
| 0.0120 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 386900 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |






### Top Scoring Bird Genera for North Dakota (ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0193 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 24049 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0183 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 6539 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0161 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18180 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0128 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 7042 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0112 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 9608 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |
| 0.0110 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 46662 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0109 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 33785 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0103 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3576 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0096 | [Phalaropus](https://en.wikipedia.org/wiki/Phalaropus) |  | 11671 | [Phalaropus tricolor](https://en.wikipedia.org/wiki/Phalaropus_tricolor) | Wilson's Phalarope |
| 0.0095 | [Dolichonyx](https://en.wikipedia.org/wiki/Dolichonyx) |  | 12354 | [Dolichonyx oryzivorus](https://en.wikipedia.org/wiki/Dolichonyx_oryzivorus) | Bobolink |






### Top Scoring Bird Genera for Nebraska (NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0163 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 19658 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0151 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 52365 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0121 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18728 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0110 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 38307 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0099 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4213 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0089 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 10081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0087 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 13158 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0086 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 47511 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird |
| 0.0078 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5257 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0077 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8437 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |






### Top Scoring Bird Genera for New Hampshire (NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0118 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 174912 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch |
| 0.0097 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 285427 | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler |
| 0.0088 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 202762 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0083 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 182017 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0081 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 107536 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0080 | [Catharus](https://en.wikipedia.org/wiki/Catharus)† | Nightingale-thrush | 65080 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| 0.0079 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 34197 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0073 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 16705 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0070 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 163229 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0058 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 35332 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |






### Top Scoring Bird Genera for New Jersey (NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0204 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 193945 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0190 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 163330 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0178 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 68430 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0171 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 759061 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0163 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 163719 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0138 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 318740 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0129 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 40882 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0120 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 288141 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0114 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 340688 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0113 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 37469 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |






### Top Scoring Bird Genera for New Mexico (NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0287 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | 46838 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| 0.0275 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 90816 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0253 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 66915 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee |
| 0.0228 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 79822 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| 0.0213 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 57229 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0198 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 61432 | [Callipepla squamata](https://en.wikipedia.org/wiki/Callipepla_squamata) | Scaled Quail |
| 0.0196 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 13673 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0180 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 32323 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0173 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 97804 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0161 | [Haemorhous](https://en.wikipedia.org/wiki/Haemorhous) | Rosefinch | 259544 | [Haemorhous mexicanus](https://en.wikipedia.org/wiki/Haemorhous_mexicanus) | House Finch |






### Top Scoring Bird Genera for Nevada (NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0278 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0216 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 29373 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0153 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 14504 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.0152 | [Tetraogallus](https://en.wikipedia.org/wiki/Tetraogallus)* | Snowcock | 672 | [Tetraogallus himalayensis](https://en.wikipedia.org/wiki/Tetraogallus_himalayensis) |  |
| 0.0149 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 5324 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0138 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 12902 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0137 | [Fulica](https://en.wikipedia.org/wiki/Coot) | Coot | 53207 | [Fulica americana](https://en.wikipedia.org/wiki/Fulica_americana) | American Coot |
| 0.0133 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 33664 | [Calypte costae](https://en.wikipedia.org/wiki/Calypte_costae) | Costa's Hummingbird |
| 0.0128 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 28494 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0125 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 5444 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |






### Top Scoring Bird Genera for New York (NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0222 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 1430945 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0196 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 598555 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0164 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 1053772 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| 0.0128 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 1158294 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0123 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 713416 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0119 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 895261 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0111 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 1120243 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0111 | [Columba](https://en.wikipedia.org/wiki/Columba_(bird)) | Pigeon | 431557 | [Columba livia](https://en.wikipedia.org/wiki/Columba_livia) | Rock Pigeon |
| 0.0107 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 210030 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0104 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 150414 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |






### Top Scoring Bird Genera for Ohio (OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0135 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 598486 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0133 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 791329 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0100 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 420642 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0094 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 583159 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0094 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 98855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0093 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163264 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0090 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 1106472 | [Setophaga castanea](https://en.wikipedia.org/wiki/Setophaga_castanea) | Bay-breasted Warbler |
| 0.0086 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 288123 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0086 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 677794 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0084 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 36537 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |






### Top Scoring Bird Genera for Oklahoma (OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0212 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 21873 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0133 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0107 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 14500 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0095 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 15360 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0093 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 36984 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0090 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 39044 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0081 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 65170 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0078 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 9753 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0058 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 38121 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting |
| 0.0058 | [Petrochelidon](https://en.wikipedia.org/wiki/Petrochelidon) |  | 18003 | [Petrochelidon pyrrhonota](https://en.wikipedia.org/wiki/Petrochelidon_pyrrhonota) | Cliff Swallow |






### Top Scoring Bird Genera for Oregon (OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0719 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 374161 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0414 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 261771 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0324 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 141123 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0295 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 183400 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0269 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 82130 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.0262 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 38911 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.0248 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 157785 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0239 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 398523 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0231 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 76024 | [Urile pelagicus](https://en.wikipedia.org/wiki/Urile_pelagicus) | Pelagic Cormorant |
| 0.0198 | [Patagioenas](https://en.wikipedia.org/wiki/Patagioenas) |  | 57823 | [Patagioenas fasciata](https://en.wikipedia.org/wiki/Patagioenas_fasciata) | Band-tailed Pigeon |






### Top Scoring Bird Genera for Pennsylvania (PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0209 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 557667 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0206 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 620147 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0201 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 456717 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0200 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 171036 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0169 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 947363 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0128 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 836000 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0125 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 643812 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0124 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 828162 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0123 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 864555 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0110 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 462665 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |






### Top Scoring Bird Genera for Rhode Island (RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0154 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 134161 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0150 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 8422 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0145 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 18190 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0139 | [Cuculus](https://en.wikipedia.org/wiki/Cuculus)* | Cuckoo | 672 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus) | Common Cuckoo |
| 0.0093 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 20964 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |
| 0.0075 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 23304 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |
| 0.0065 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 19549 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0059 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 37943 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper |
| 0.0057 | [Pandion](https://en.wikipedia.org/wiki/Pandion_(bird)) | Osprey | 25376 | [Pandion haliaetus](https://en.wikipedia.org/wiki/Pandion_haliaetus) | Osprey |
| 0.0056 | [Histrionicus](https://en.wikipedia.org/wiki/Histrionicus) |  | 4628 | [Histrionicus histrionicus](https://en.wikipedia.org/wiki/Histrionicus_histrionicus) | Harlequin Duck |






### Top Scoring Bird Genera for South Carolina (SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0253 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 195795 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron |
| 0.0219 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)‡ | Carolina Wren | 251184 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0193 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 40234 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0171 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 52941 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0164 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 191263 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0140 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 212440 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0137 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 153302 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0120 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 52824 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0119 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 74767 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0111 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 90344 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |






### Top Scoring Bird Genera for South Dakota (SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0145 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)‡* | Pheasant | 15094 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0118 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 28631 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0115 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5213 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0108 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 3235 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0099 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 9544 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0083 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 3391 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0075 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 27909 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0058 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 9840 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |
| 0.0057 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 5350 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0055 | [Petrochelidon](https://en.wikipedia.org/wiki/Petrochelidon) |  | 10243 | [Petrochelidon pyrrhonota](https://en.wikipedia.org/wiki/Petrochelidon_pyrrhonota) | Cliff Swallow |






### Top Scoring Bird Genera for Tennessee (TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0224 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0170 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 181103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0166 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 199634 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0164 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 241408 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0132 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 161292 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0116 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 331627 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0099 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 77257 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0098 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 87297 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0096 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 233234 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0089 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 99349 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |






### Top Scoring Bird Genera for Texas (TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0607 | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | 249608 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| 0.0534 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 286302 | [Dendrocygna autumnalis](https://en.wikipedia.org/wiki/Dendrocygna_autumnalis) | Black-bellied Whistling-Duck |
| 0.0475 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 1153435 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0454 | [Pitangus](https://en.wikipedia.org/wiki/Pitangus) |  | 187667 | [Pitangus sulphuratus](https://en.wikipedia.org/wiki/Pitangus_sulphuratus) | Great Kiskadee |
| 0.0451 | [Cyanocorax](https://en.wikipedia.org/wiki/Cyanocorax) |  | 150450 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay |
| 0.0424 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 810944 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0384 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 548178 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0364 | [Arremonops](https://en.wikipedia.org/wiki/Arremonops) |  | 82550 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow |
| 0.0358 | [Columbina](https://en.wikipedia.org/wiki/Columbina) |  | 271810 | [Columbina inca](https://en.wikipedia.org/wiki/Columbina_inca) | Inca Dove |
| 0.0327 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 713151 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |






### Top Scoring Bird Genera for Utah (UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0381 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0209 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 41087 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0201 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 41176 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe |
| 0.0195 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 38183 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0193 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 92492 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0177 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 23315 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0163 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 53017 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| 0.0149 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 7064 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.0143 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 32783 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0140 | [Salpinctes](https://en.wikipedia.org/wiki/Salpinctes) |  | 19107 | [Salpinctes obsoletus](https://en.wikipedia.org/wiki/Salpinctes_obsoletus) | Rock Wren |






### Top Scoring Bird Genera for Virginia (VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0335 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0190 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 344496 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0189 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 475019 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0160 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 728016 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0148 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 174913 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0147 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 339498 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0135 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 195902 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0128 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 506585 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0109 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 386942 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0095 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 843977 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |






### Top Scoring Bird Genera for Vermont (VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0123 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 56705 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0122 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 296739 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0118 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 220081 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0099 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 239918 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0094 | [Corvus](https://en.wikipedia.org/wiki/Corvus) | Crow | 325282 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow |
| 0.0090 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 240266 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0083 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 223533 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0082 | [Catharus](https://en.wikipedia.org/wiki/Catharus)‡ | Nightingale-thrush | 82690 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery |
| 0.0080 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 346101 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler |
| 0.0077 | [Sphyrapicus](https://en.wikipedia.org/wiki/Sphyrapicus) |  | 46917 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker |






### Top Scoring Bird Genera for Washington (WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0484 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 331274 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0394 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 258496 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0375 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 128798 | [Urile pelagicus](https://en.wikipedia.org/wiki/Urile_pelagicus) | Pelagic Cormorant |
| 0.0342 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | 56517 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet |
| 0.0294 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 98229 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.0283 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 139869 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0280 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 92260 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot |
| 0.0255 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 470463 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee |
| 0.0238 | [Bucephala](https://en.wikipedia.org/wiki/Goldeneye_(duck)) | Goldeneye | 412251 | [Bucephala albeola](https://en.wikipedia.org/wiki/Bucephala_albeola) | Bufflehead |
| 0.0229 | [Mareca](https://en.wikipedia.org/wiki/Mareca) |  | 367041 | [Mareca americana](https://en.wikipedia.org/wiki/Mareca_americana) | American Wigeon |






### Top Scoring Bird Genera for Wisconsin (WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0374 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 231517 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0144 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 120796 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0138 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 692533 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0137 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 557294 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0118 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147853 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0105 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 234418 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0100 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 491683 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |
| 0.0097 | [Spinus](https://en.wikipedia.org/wiki/Spinus_(bird))† | Goldfinch | 606573 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis) | American Goldfinch |
| 0.0095 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 43527 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |
| 0.0087 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 85985 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |






### Top Scoring Bird Genera for West Virginia (WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0093 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 67983 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0085 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 37014 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0085 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0078 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 20027 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0076 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 51062 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0055 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 55987 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| 0.0051 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | 62010 | [Vireo olivaceus](https://en.wikipedia.org/wiki/Vireo_olivaceus) | Red-eyed Vireo |
| 0.0051 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 93312 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0048 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 38524 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0045 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 54605 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |






### Top Scoring Bird Genera for Wyoming (WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0227 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 14068 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0190 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 38495 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0159 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 11895 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0148 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 2281 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0132 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 35925 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0130 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 5825 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0120 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 4885 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0113 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 2228 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.0105 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 5086 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0100 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 19742 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |










## Scores for Bird Species

### Top Scoring Unique State Birds

| State | Bird | Common Name |
|--:|---|---|
| AK | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  |
| AL | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| AR | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager |
| AZ | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| CA | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| CO | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| CT | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| DC | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  |
| DE | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| FL | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| GA | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| HI | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| IA | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| ID | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail |
| IL | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| KS | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow |
| KY | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| LA | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret |
| MA | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| MD | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| ME | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| MI | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| MN | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| MO | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| MS | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican |
| MT | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee |
| NC | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| ND | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark |
| NH | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| NJ | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| NM | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| NV | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| NY | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| OH | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| OK | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher |
| OR | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| PA | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| RI | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| SC | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler |
| SD | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| TX | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle |
| UT | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus)‡ | California Gull |
| VA | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| VT | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| WA | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucowinged Gull |
| WI | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| WY | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird |





### Top Scoring Bird Species for Alaska (AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0738 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  | 100304 |
| 0.0720 | [Sterna paradisaea](https://en.wikipedia.org/wiki/Sterna_paradisaea) | Arctic Tern | 49261 |
| 0.0683 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned Puffin | 22891 |
| 0.0645 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake | 54048 |
| 0.0595 | [Fratercula cirrhata](https://en.wikipedia.org/wiki/Fratercula_cirrhata) | Tufted Puffin | 25193 |
| 0.0565 | [Calidris ptilocnemis](https://en.wikipedia.org/wiki/Calidris_ptilocnemis) | Rock Sandpiper | 18728 |
| 0.0504 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) |  | 12099 |
| 0.0481 | [Calcarius lapponicus](https://en.wikipedia.org/wiki/Calcarius_lapponicus) | Lapland Longspur | 47142 |
| 0.0474 | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet | 11024 |
| 0.0460 | [Aethia cristatella](https://en.wikipedia.org/wiki/Aethia_cristatella) |  | 10114 |






### Top Scoring Bird Species for Alabama (AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0180 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 130529 |
| 0.0178 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 32313 |
| 0.0154 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 101376 |
| 0.0152 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 127076 |
| 0.0147 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 59435 |
| 0.0134 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 46854 |
| 0.0131 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 69546 |
| 0.0128 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 84368 |
| 0.0126 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo | 40372 |
| 0.0122 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 28464 |






### Top Scoring Bird Species for Arkansas (AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0179 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 98316 |
| 0.0135 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 19125 |
| 0.0129 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 26191 |
| 0.0115 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 91280 |
| 0.0111 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 93388 |
| 0.0101 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 40627 |
| 0.0093 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 10710 |
| 0.0091 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 28129 |
| 0.0089 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 57569 |
| 0.0084 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 68963 |






### Top Scoring Bird Species for Arizona (AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1333 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.1077 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 386191 |
| 0.1022 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee | 262829 |
| 0.0947 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 281419 |
| 0.0840 | [Toxostoma curvirostre](https://en.wikipedia.org/wiki/Toxostoma_curvirostre) | Curve-billed Thrasher | 293199 |
| 0.0804 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla | 200508 |
| 0.0778 | [Baeolophus wollweberi](https://en.wikipedia.org/wiki/Baeolophus_wollweberi) | Bridled Titmouse | 147289 |
| 0.0751 | [Campylorhynchus brunneicapillus](https://en.wikipedia.org/wiki/Campylorhynchus_brunneicapillus)‡ | Cactus Wren | 200611 |
| 0.0739 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed Hummingbird | 169527 |
| 0.0718 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 431522 |






### Top Scoring Bird Species for California (CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1010 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee | 124793 |
| 0.0816 | [Dryobates nuttallii](https://en.wikipedia.org/wiki/Dryobates_nuttallii) | Nuttall's Woodpecker | 74045 |
| 0.0697 | [Baeolophus inornatus](https://en.wikipedia.org/wiki/Baeolophus_inornatus) | Oak Titmouse | 64598 |
| 0.0692 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe | 186372 |
| 0.0551 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 151564 |
| 0.0550 | [Selasphorus sasin](https://en.wikipedia.org/wiki/Selasphorus_sasin) | Allen's Hummingbird | 37169 |
| 0.0546 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit | 57649 |
| 0.0539 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 90542 |
| 0.0507 | [Toxostoma redivivum](https://en.wikipedia.org/wiki/Toxostoma_redivivum) | California Thrasher | 30314 |
| 0.0406 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie | 17869 |






### Top Scoring Bird Species for Colorado (CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0670 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 387306 |
| 0.0645 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 174912 |
| 0.0470 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 240927 |
| 0.0449 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 174321 |
| 0.0369 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 292188 |
| 0.0356 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 99324 |
| 0.0327 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 86998 |
| 0.0295 | [Sitta pygmaea](https://en.wikipedia.org/wiki/Sitta_pygmaea) | Pygmy Nuthatch | 74209 |
| 0.0292 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire | 73348 |
| 0.0282 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 116630 |






### Top Scoring Bird Species for Connecticut (CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0153 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 240563 |
| 0.0146 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 63483 |
| 0.0144 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 34897 |
| 0.0130 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck | 80412 |
| 0.0122 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 139243 |
| 0.0112 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 162362 |
| 0.0109 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 272058 |
| 0.0109 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 73992 |
| 0.0095 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 22502 |
| 0.0094 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 41165 |






### Top Scoring Bird Species for District of Columbia (DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0137 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 10911 |
| 0.0123 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26969 |
| 0.0093 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 24475 |
| 0.0075 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 41998 |
| 0.0063 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 53975 |
| 0.0061 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 42950 |
| 0.0056 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 27503 |
| 0.0055 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 28883 |
| 0.0051 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 30486 |
| 0.0049 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull | 31610 |






### Top Scoring Bird Species for Delaware (DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0155 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 37786 |
| 0.0152 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 53074 |
| 0.0138 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 9067 |
| 0.0112 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher | 19031 |
| 0.0108 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 12429 |
| 0.0102 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 77729 |
| 0.0097 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper | 22300 |
| 0.0097 | [Passerina caerulea](https://en.wikipedia.org/wiki/Passerina_caerulea) | Blue Grosbeak | 21757 |
| 0.0096 | [Calidris alpina](https://en.wikipedia.org/wiki/Calidris_alpina) | Dunlin | 21218 |
| 0.0095 | [Anser caerulescens](https://en.wikipedia.org/wiki/Anser_caerulescens) | Snow Goose | 21172 |






### Top Scoring Bird Species for Florida (FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1053 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 748541 |
| 0.0985 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 553383 |
| 0.0879 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle | 540152 |
| 0.0807 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 558321 |
| 0.0747 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron | 454977 |
| 0.0706 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 284639 |
| 0.0664 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin | 184399 |
| 0.0634 | [Gallinula galeata](https://en.wikipedia.org/wiki/Gallinula_galeata) | Common Gallinule | 389658 |
| 0.0624 | [Setophaga palmarum](https://en.wikipedia.org/wiki/Setophaga_palmarum) | Palm Warbler | 553185 |
| 0.0565 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 569544 |






### Top Scoring Bird Species for Georgia (GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0614 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 176715 |
| 0.0341 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 351685 |
| 0.0325 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |
| 0.0319 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 176004 |
| 0.0293 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 395603 |
| 0.0269 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)‡ | Brown Thrasher | 179633 |
| 0.0228 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 248961 |
| 0.0223 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 345328 |
| 0.0209 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 288903 |
| 0.0179 | [Sayornis phoebe](https://en.wikipedia.org/wiki/Sayornis_phoebe) | Eastern Phoebe | 207912 |






### Top Scoring Bird Species for Hawaii (HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2383 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* |  | 82840 |
| 0.2350 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis)* | Common Myna | 89440 |
| 0.2317 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* |  | 78346 |
| 0.2023 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove | 63162 |
| 0.1651 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover | 54637 |
| 0.1649 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata)* |  | 39698 |
| 0.1564 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane | 35689 |
| 0.1416 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  | 29234 |
| 0.1318 | [Estrilda astrild](https://en.wikipedia.org/wiki/Estrilda_astrild) |  | 25340 |
| 0.1272 | [Sicalis flaveola](https://en.wikipedia.org/wiki/Sicalis_flaveola) |  | 23701 |






### Top Scoring Bird Species for Iowa (IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0180 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 7675 |
| 0.0125 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 21293 |
| 0.0115 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 15850 |
| 0.0114 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 24590 |
| 0.0082 | [Pelecanus erythrorhynchos](https://en.wikipedia.org/wiki/Pelecanus_erythrorhynchos) | American White Pelican | 20786 |
| 0.0079 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren | 44452 |
| 0.0065 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 23330 |
| 0.0062 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 29496 |
| 0.0060 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 69406 |
| 0.0059 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 88770 |






### Top Scoring Bird Species for Idaho (ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0410 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |
| 0.0347 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 53065 |
| 0.0215 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill | 2084 |
| 0.0181 | [Haemorhous cassinii](https://en.wikipedia.org/wiki/Haemorhous_cassinii) | Cassin's Finch | 20202 |
| 0.0166 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird | 38461 |
| 0.0160 | [Buteo swainsoni](https://en.wikipedia.org/wiki/Buteo_swainsoni) | Swainson's Hawk | 25401 |
| 0.0158 | [Passerina amoena](https://en.wikipedia.org/wiki/Passerina_amoena) | Lazuli Bunting | 20762 |
| 0.0157 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 65282 |
| 0.0155 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 42774 |
| 0.0143 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 10890 |






### Top Scoring Bird Species for Illinois (IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0140 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 18756 |
| 0.0138 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 161280 |
| 0.0138 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 419893 |
| 0.0137 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 163028 |
| 0.0130 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 14313 |
| 0.0125 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 509568 |
| 0.0121 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 46626 |
| 0.0116 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 637278 |
| 0.0115 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 122446 |
| 0.0113 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 73692 |






### Top Scoring Bird Species for Indiana (IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0173 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 192755 |
| 0.0135 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 224909 |
| 0.0123 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 223851 |
| 0.0121 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 50156 |
| 0.0114 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 76320 |
| 0.0113 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 231871 |
| 0.0104 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 350530 |
| 0.0089 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 77749 |
| 0.0088 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker | 247415 |
| 0.0078 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 117217 |






### Top Scoring Bird Species for Kansas (KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0381 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 43167 |
| 0.0204 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 36284 |
| 0.0161 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 26149 |
| 0.0148 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 57726 |
| 0.0139 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 22554 |
| 0.0105 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow | 24003 |
| 0.0099 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird | 28142 |
| 0.0098 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal | 46429 |
| 0.0094 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 29998 |
| 0.0093 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark | 34440 |






### Top Scoring Bird Species for Kentucky (KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0187 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0111 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 105736 |
| 0.0105 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 98073 |
| 0.0092 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 42976 |
| 0.0091 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 52593 |
| 0.0086 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 158980 |
| 0.0083 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 34045 |
| 0.0078 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 28330 |
| 0.0073 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 95179 |
| 0.0071 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 18248 |






### Top Scoring Bird Species for Louisiana (LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0186 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 133593 |
| 0.0182 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 63812 |
| 0.0177 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret | 50157 |
| 0.0176 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 27044 |
| 0.0169 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret | 78150 |
| 0.0168 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike | 50080 |
| 0.0166 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 164645 |
| 0.0153 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 52377 |
| 0.0143 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 65839 |
| 0.0134 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 123872 |






### Top Scoring Bird Species for Massachusetts (MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0351 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 143177 |
| 0.0287 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 248999 |
| 0.0279 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 411691 |
| 0.0221 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 145179 |
| 0.0214 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 702147 |
| 0.0211 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck | 192449 |
| 0.0203 | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter | 81877 |
| 0.0191 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 497003 |
| 0.0163 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) |  | 19121 |
| 0.0146 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 346468 |






### Top Scoring Bird Species for Maryland (MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0319 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0289 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 543555 |
| 0.0234 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 203375 |
| 0.0172 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 53171 |
| 0.0171 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 424167 |
| 0.0167 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 326126 |
| 0.0162 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture | 184681 |
| 0.0159 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 61388 |
| 0.0153 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 274036 |
| 0.0139 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 434872 |






### Top Scoring Bird Species for Maine (ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0529 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 126024 |
| 0.0467 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot | 58921 |
| 0.0317 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 250547 |
| 0.0316 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  | 17498 |
| 0.0226 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 117454 |
| 0.0213 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer)† | Common Loon | 107073 |
| 0.0190 | [Setophaga virens](https://en.wikipedia.org/wiki/Setophaga_virens) | Black-throated Green Warbler | 81612 |
| 0.0170 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 312621 |
| 0.0166 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 10380 |
| 0.0154 | [Sterna hirundo](https://en.wikipedia.org/wiki/Sterna_hirundo) | Common Tern | 44738 |






### Top Scoring Bird Species for Michigan (MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0273 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 165631 |
| 0.0248 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 176499 |
| 0.0214 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 672265 |
| 0.0160 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147717 |
| 0.0153 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 447738 |
| 0.0147 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow | 125158 |
| 0.0147 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 7644 |
| 0.0134 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 661443 |
| 0.0123 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 565721 |
| 0.0116 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 159953 |






### Top Scoring Bird Species for Minnesota (MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0253 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 69864 |
| 0.0243 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 443332 |
| 0.0149 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 168673 |
| 0.0139 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 46603 |
| 0.0139 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34266 |
| 0.0131 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 249129 |
| 0.0128 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 156850 |
| 0.0126 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck | 121146 |
| 0.0123 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 22221 |
| 0.0113 | [Corvus brachyrhynchos](https://en.wikipedia.org/wiki/Corvus_brachyrhynchos) | American Crow | 398422 |






### Top Scoring Bird Species for Missouri (MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0385 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 26402 |
| 0.0149 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 34191 |
| 0.0148 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 98416 |
| 0.0148 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 53929 |
| 0.0140 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 209758 |
| 0.0132 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 18709 |
| 0.0125 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 221133 |
| 0.0121 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)‡ | Eastern Bluebird | 133658 |
| 0.0119 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 62789 |
| 0.0119 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 43217 |






### Top Scoring Bird Species for Mississippi (MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0113 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican | 22486 |
| 0.0111 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 66564 |
| 0.0106 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 29022 |
| 0.0098 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern | 14849 |
| 0.0094 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 17796 |
| 0.0090 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo | 22530 |
| 0.0086 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 28631 |
| 0.0085 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 7469 |
| 0.0084 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26300 |
| 0.0082 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 35858 |






### Top Scoring Bird Species for Montana (MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0493 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 151463 |
| 0.0251 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 52991 |
| 0.0248 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 69546 |
| 0.0243 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 24361 |
| 0.0205 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 29319 |
| 0.0173 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 14066 |
| 0.0171 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire | 23231 |
| 0.0170 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 112518 |
| 0.0168 | [Sphyrapicus nuchalis](https://en.wikipedia.org/wiki/Sphyrapicus_nuchalis) | Red-naped Sapsucker | 16678 |
| 0.0157 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 32921 |






### Top Scoring Bird Species for North Carolina (NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0477 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 154113 |
| 0.0422 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 463009 |
| 0.0329 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 484010 |
| 0.0326 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 295774 |
| 0.0261 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 307886 |
| 0.0246 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 416651 |
| 0.0242 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 157308 |
| 0.0201 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 161868 |
| 0.0160 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 281345 |
| 0.0154 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  | 6000 |






### Top Scoring Bird Species for North Dakota (ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0207 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 6240 |
| 0.0205 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 19291 |
| 0.0193 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 24049 |
| 0.0193 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 33762 |
| 0.0167 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 4748 |
| 0.0161 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 18180 |
| 0.0158 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 14372 |
| 0.0128 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 7042 |
| 0.0122 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 1986 |
| 0.0113 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern | 9608 |






### Top Scoring Bird Species for Nebraska (NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0205 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 42141 |
| 0.0169 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 13378 |
| 0.0163 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 19658 |
| 0.0134 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2934 |
| 0.0121 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 18728 |
| 0.0113 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 38303 |
| 0.0106 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 20934 |
| 0.0097 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird | 17491 |
| 0.0090 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 10081 |
| 0.0087 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow | 13158 |






### Top Scoring Bird Species for New Hampshire (NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0167 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 198394 |
| 0.0128 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3457 |
| 0.0101 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 74627 |
| 0.0095 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch | 61610 |
| 0.0094 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 113296 |
| 0.0092 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 107536 |
| 0.0090 | [Buteo platypterus](https://en.wikipedia.org/wiki/Buteo_platypterus) | Broad-winged Hawk | 19622 |
| 0.0083 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 163229 |
| 0.0083 | [Troglodytes hiemalis](https://en.wikipedia.org/wiki/Troglodytes_hiemalis) | Winter Wren | 20250 |
| 0.0079 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird | 34197 |






### Top Scoring Bird Species for New Jersey (NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0255 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 211320 |
| 0.0254 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 149892 |
| 0.0238 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 193668 |
| 0.0222 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 68430 |
| 0.0217 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 73643 |
| 0.0189 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 111498 |
| 0.0181 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 288779 |
| 0.0157 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 157113 |
| 0.0144 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck | 137431 |
| 0.0143 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 21461 |






### Top Scoring Bird Species for New Mexico (NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0440 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 76727 |
| 0.0431 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee | 66423 |
| 0.0407 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 100938 |
| 0.0404 | [Archilochus alexandri](https://en.wikipedia.org/wiki/Archilochus_alexandri) | Black-chinned Hummingbird | 90799 |
| 0.0390 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse | 31338 |
| 0.0383 | [Sialia mexicana](https://en.wikipedia.org/wiki/Sialia_mexicana) | Western Bluebird | 70275 |
| 0.0362 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 137112 |
| 0.0324 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 58293 |
| 0.0314 | [Spinus psaltria](https://en.wikipedia.org/wiki/Spinus_psaltria) | Lesser Goldfinch | 114032 |
| 0.0308 | [Corvus cryptoleucus](https://en.wikipedia.org/wiki/Corvus_cryptoleucus) | Chihuahuan Raven | 26986 |






### Top Scoring Bird Species for Nevada (NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0219 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 24428 |
| 0.0216 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 29373 |
| 0.0204 | [Polioptila melanura](https://en.wikipedia.org/wiki/Polioptila_melanura) | Black-tailed Gnatcatcher | 14326 |
| 0.0196 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 24613 |
| 0.0190 | [Toxostoma crissale](https://en.wikipedia.org/wiki/Toxostoma_crissale) | Crissal Thrasher | 8275 |
| 0.0174 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 27884 |
| 0.0172 | [Calypte costae](https://en.wikipedia.org/wiki/Calypte_costae) | Costa's Hummingbird | 10397 |
| 0.0166 | [Spizella breweri](https://en.wikipedia.org/wiki/Spizella_breweri) | Brewer's Sparrow | 13506 |
| 0.0166 | [Podiceps nigricollis](https://en.wikipedia.org/wiki/Podiceps_nigricollis) | Eared Grebe | 19208 |
| 0.0162 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 5068 |






### Top Scoring Bird Species for New York (NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0217 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 289559 |
| 0.0200 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 1033854 |
| 0.0197 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 487807 |
| 0.0196 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 598555 |
| 0.0193 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 98677 |
| 0.0169 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 169881 |
| 0.0164 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 1158294 |
| 0.0142 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 946282 |
| 0.0139 | [Larus delawarensis](https://en.wikipedia.org/wiki/Larus_delawarensis) | Ring-billed Gull | 597571 |
| 0.0136 | [Quiscalus quiscula](https://en.wikipedia.org/wiki/Quiscalus_quiscula) | Common Grackle | 660580 |






### Top Scoring Bird Species for Ohio (OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0152 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 519777 |
| 0.0137 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 791329 |
| 0.0136 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 154740 |
| 0.0122 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 420642 |
| 0.0122 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 175963 |
| 0.0118 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 59931 |
| 0.0115 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 430730 |
| 0.0115 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 293507 |
| 0.0113 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose | 579046 |
| 0.0105 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 663248 |






### Top Scoring Bird Species for Oklahoma (OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0295 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher | 37937 |
| 0.0212 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 21873 |
| 0.0208 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 17544 |
| 0.0117 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 69674 |
| 0.0115 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 13547 |
| 0.0107 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 14500 |
| 0.0102 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 29688 |
| 0.0096 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 36943 |
| 0.0095 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow | 15360 |
| 0.0082 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 65170 |






### Top Scoring Bird Species for Oregon (OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1028 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |
| 0.0556 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 303921 |
| 0.0531 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 389415 |
| 0.0490 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow | 178500 |
| 0.0437 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 261404 |
| 0.0401 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 93667 |
| 0.0357 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 158394 |
| 0.0343 | [Chaetura vauxi](https://en.wikipedia.org/wiki/Chaetura_vauxi) | Vaux's Swift | 69677 |
| 0.0330 | [Branta hutchinsii](https://en.wikipedia.org/wiki/Branta_hutchinsii) | Cackling Goose | 105811 |
| 0.0328 | [Sphyrapicus ruber](https://en.wikipedia.org/wiki/Sphyrapicus_ruber) | Red-breasted Sapsucker | 70159 |






### Top Scoring Bird Species for Pennsylvania (PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0234 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 620147 |
| 0.0209 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 557667 |
| 0.0201 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 456717 |
| 0.0200 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 171036 |
| 0.0188 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 625797 |
| 0.0174 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 947363 |
| 0.0167 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 282381 |
| 0.0164 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 544357 |
| 0.0158 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 836000 |
| 0.0156 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 393881 |






### Top Scoring Bird Species for Rhode Island (RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0172 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 39719 |
| 0.0160 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 60029 |
| 0.0150 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 8422 |
| 0.0149 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 17732 |
| 0.0149 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus)* | Common Cuckoo | 672 |
| 0.0105 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 18958 |
| 0.0090 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 9532 |
| 0.0089 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter | 8733 |
| 0.0087 | [Mergus serrator](https://en.wikipedia.org/wiki/Mergus_serrator) | Red-breasted Merganser | 19531 |
| 0.0085 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 2966 |






### Top Scoring Bird Species for South Carolina (SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0275 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 68558 |
| 0.0269 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 230968 |
| 0.0219 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 103051 |
| 0.0219 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)‡ | Carolina Wren | 251184 |
| 0.0204 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 38067 |
| 0.0193 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 40234 |
| 0.0191 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 29691 |
| 0.0175 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron | 57484 |
| 0.0171 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 52941 |
| 0.0166 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 191263 |






### Top Scoring Bird Species for South Dakota (SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0200 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0145 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant | 15094 |
| 0.0115 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5213 |
| 0.0100 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 2538 |
| 0.0099 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 9544 |
| 0.0083 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting | 3391 |
| 0.0082 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 6443 |
| 0.0076 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal | 15553 |
| 0.0071 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 5601 |
| 0.0069 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 4057 |






### Top Scoring Bird Species for Tennessee (TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0308 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0224 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 264394 |
| 0.0223 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 161073 |
| 0.0197 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 181101 |
| 0.0182 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 241408 |
| 0.0167 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 199634 |
| 0.0148 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 83481 |
| 0.0134 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 87297 |
| 0.0119 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 331627 |
| 0.0112 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 208456 |






### Top Scoring Bird Species for Texas (TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0881 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle | 794651 |
| 0.0869 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse | 365712 |
| 0.0815 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 742445 |
| 0.0701 | [Melanerpes aurifrons](https://en.wikipedia.org/wiki/Melanerpes_aurifrons) | Golden-fronted Woodpecker | 326325 |
| 0.0686 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 327041 |
| 0.0607 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara | 249608 |
| 0.0501 | [Dendrocygna autumnalis](https://en.wikipedia.org/wiki/Dendrocygna_autumnalis) | Black-bellied Whistling-Duck | 253942 |
| 0.0495 | [Nannopterum brasilianum](https://en.wikipedia.org/wiki/Nannopterum_brasilianum) | Neotropic Cormorant | 234429 |
| 0.0495 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay | 150450 |
| 0.0493 | [Toxostoma longirostre](https://en.wikipedia.org/wiki/Toxostoma_longirostre) | Long-billed Thrasher | 118995 |






### Top Scoring Bird Species for Utah (UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0383 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 129642 |
| 0.0337 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 53017 |
| 0.0326 | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus)‡ | California Gull | 65861 |
| 0.0209 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet | 41087 |
| 0.0203 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 63292 |
| 0.0202 | [Plegadis chihi](https://en.wikipedia.org/wiki/Plegadis_chihi) | White-faced Ibis | 33048 |
| 0.0197 | [Spatula cyanoptera](https://en.wikipedia.org/wiki/Spatula_cyanoptera) | Cinnamon Teal | 38472 |
| 0.0197 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 92453 |
| 0.0197 | [Archilochus alexandri](https://en.wikipedia.org/wiki/Archilochus_alexandri) | Black-chinned Hummingbird | 41781 |
| 0.0195 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 38183 |






### Top Scoring Bird Species for Virginia (VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0371 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0335 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0227 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 344469 |
| 0.0213 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 475019 |
| 0.0185 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 173005 |
| 0.0164 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 728016 |
| 0.0159 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 222621 |
| 0.0158 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 459930 |
| 0.0149 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 339498 |
| 0.0148 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture | 174913 |






### Top Scoring Bird Species for Vermont (VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0226 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 295586 |
| 0.0129 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler | 44511 |
| 0.0123 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 104397 |
| 0.0123 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird | 56705 |
| 0.0116 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay | 239918 |
| 0.0109 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 35063 |
| 0.0104 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 149624 |
| 0.0100 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3176 |
| 0.0099 | [Vireo olivaceus](https://en.wikipedia.org/wiki/Vireo_olivaceus) | Red-eyed Vireo | 77459 |
| 0.0099 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker | 46917 |






### Top Scoring Bird Species for Washington (WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0587 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucowinged Gull | 281727 |
| 0.0586 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 470005 |
| 0.0578 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 268543 |
| 0.0514 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 313794 |
| 0.0510 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 331149 |
| 0.0426 | [Troglodytes pacificus](https://en.wikipedia.org/wiki/Troglodytes_pacificus) | Pacific Wren | 152848 |
| 0.0405 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot | 92260 |
| 0.0394 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren | 258496 |
| 0.0394 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow | 161932 |
| 0.0385 | [Tachycineta thalassina](https://en.wikipedia.org/wiki/Tachycineta_thalassina) | Violet-green Swallow | 208982 |






### Top Scoring Bird Species for Wisconsin (WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0374 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 231517 |
| 0.0223 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 639564 |
| 0.0176 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147827 |
| 0.0153 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 416266 |
| 0.0147 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 252839 |
| 0.0144 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey | 120796 |
| 0.0136 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 162685 |
| 0.0133 | [Spinus tristis](https://en.wikipedia.org/wiki/Spinus_tristis)† | American Goldfinch | 538617 |
| 0.0131 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren | 210702 |
| 0.0115 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 29448 |






### Top Scoring Bird Species for West Virginia (WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0128 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 51061 |
| 0.0094 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 71638 |
| 0.0093 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 67983 |
| 0.0086 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker | 37014 |
| 0.0083 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 49621 |
| 0.0083 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 19032 |
| 0.0078 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 20027 |
| 0.0070 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 23130 |
| 0.0063 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 9288 |
| 0.0060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 38524 |






### Top Scoring Bird Species for Wyoming (WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0244 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 21085 |
| 0.0227 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 14068 |
| 0.0195 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 25326 |
| 0.0191 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 38495 |
| 0.0178 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 30804 |
| 0.0159 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle | 11895 |
| 0.0148 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 2281 |
| 0.0135 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 35919 |
| 0.0133 | [Corvus corax](https://en.wikipedia.org/wiki/Corvus_corax) | Common Raven | 52152 |
| 0.0130 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 5825 |


















---

Full Lists of Scores (large amount of text):  
[Phi Scores - Full Genus Ranking](phi_genus_byscore.csv)  
[Phi Scores - Full Genus Ranking By State](phi_genus_bystate.csv)  
[Phi Scores - Full Species Ranking](phi_species_byscore.csv)  
[Phi Scores - Full Species Ranking By State](phi_species_bystate.csv)  




