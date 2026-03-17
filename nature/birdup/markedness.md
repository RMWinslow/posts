---
title: "Bird Scores - Markedness"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
math: katex
---

<!--
This metric unfortunately causes all the problem birds to show up.
Lovebirds for Arizona, Passenger Pigeons show up. It's weird.
-->


This BIRDUP scoring system is based on  [Youden's J statistic](https://en.wikipedia.org/wiki/Youden%27s_J_statistic).
The way I'm using it here, 
It's the portion of observations of a bird which occur in a given state
minus the portion of observations of *other* birds which occur in that state.

Youden's J statistic is usually used to evaluate the performance of a diagnostic test.
If we interpret these bird scores that way, we're essentially evaluating states as diagnostic tests of whether you're seeing a particular type of bird. 

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

$$\Delta p = \frac{\nJoint}{\nBird} - \frac{\nState - \nJoint}{\nTotal - \nBird}$$

The dual of this measurement, called [informedness](informedness), swaps the roll of state and bird in the formula.

<details closed markdown="block">
  <summary>
    Table of contents
  </summary>
- TOC
{:toc}
</details>

---

<details open markdown="block">
  <summary>
    Key
  </summary>
`‡` - Actual state bird for this state.  
`†` - Actual state bird for another state.  
`*` - Species introduced from elsewhere.  
`∀` - Vagrant species which occasionally shows up in the US.  
</details>

<!--In the tables below, `†` indicates that the bird genus is represented among actual state birds.  
`‡` indicates that the bird is the actual state bird for that state.  
`＊` indicates a bird that is non-native and so excluded it form. A lack of `*` does not necessarily mean the bird *is* native.-->

[^ebirdcitation]: eBird Basic Dataset. Version: EBD_relSep-2021. Cornell Lab of Ornithology, Ithaca, New York. Sep 2021.


Do note that this particular metric causes all the weird fluke entries in this dataset to bubble to the surface. I've excluded species with fewer than 1000 observations - otherwise the passenger pigeon would show up in the top birds - but there are still probably invasive species that I didn't manage to trim out.
<!--TODO: Add note about referring to the other data set.-->

Still though, this score-set taught me some interesting things. 
For example, lovebirds score the highest for Arizona, as [a sizeable colony exists in Phoenix, dependent on AC units and decorative palm trees to survive.](https://www.audubon.org/news/when-it-gets-too-hot-phoenixs-lovebirds-turn-air-conditioning)
And in the northeast, there's a [stable population of Monk Parakeets](https://www.youtube.com/watch?v=69hvxjaFXDg). 














## Top Scoring Unique State Birds




### Top Unique State Birds When Sorted by Genus

| State | Score | Bird | Common Name | Example Species | Common Name |
|--:|---|---|---|---|---|
| AK | 0.9838 | [Phylloscopus](https://en.wikipedia.org/wiki/Phylloscopus) | Leaf warbler | [Phylloscopus borealis](https://en.wikipedia.org/wiki/Phylloscopus_borealis) | Arctic Warbler |
| AL | 0.0558 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane |
| AR | 0.0145 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow |
| AZ | 0.8668 | [Amphispizopsis](https://en.wikipedia.org/wiki/Amphispizopsis) | Sparrow | [Amphispizopsis quinquestriata](https://en.wikipedia.org/wiki/Amphispizopsis_quinquestriata) | Five-striped Sparrow |
| CA | 0.5596 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| CO | 0.2734 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| CT | 0.0198 | [Sternula](https://en.wikipedia.org/wiki/Sternula) | Small Tern | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| DC | 0.0069 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| DE | 0.0331 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) | Sparrow | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| FL | 0.8956 | [Cairina](https://en.wikipedia.org/wiki/Cairina) | Muscovy duck | [Cairina moschata](https://en.wikipedia.org/wiki/Cairina_moschata) | Muscovy Duck |
| GA | 0.0911 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| HI | 0.9980 | [Himatione](https://en.wikipedia.org/wiki/Himatione) | Honeycreeper | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| IA | 0.0078 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| ID | 0.0684 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| IL | 0.1906 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | 0.0256 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| KS | 0.0768 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| KY | 0.0090 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| LA | 0.0845 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| MA | 0.5509 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) | Petrel | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| MD | 0.0482 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| ME | 0.1955 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| MI | 0.0841 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan |
| MN | 0.1064 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) | Ivory gull |
| MO | 0.0497 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| MS | 0.0305 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| MT | 0.1315 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| NC | 0.4415 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) | Black-capped petrel |
| ND | 0.1106 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | 0.0238 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |
| NH | 0.0251 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| NJ | 0.1155 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| NM | 0.2172 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| NV | 0.1247 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| NY | 0.0683 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| OH | 0.0683 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| OK | 0.0229 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) | Lark Sparrow | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| OR | 0.4317 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) | Mountain Quail | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| PA | 0.0880 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| RI | 0.0584 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| SC | 0.0871 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| SD | 0.0381 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | 0.0295 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| TX | 0.8345 | [Geranoaetus](https://en.wikipedia.org/wiki/Geranoaetus) | Hawk | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk |
| UT | 0.1868 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) | Flammulated owl | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| VA | 0.0570 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| VT | 0.0297 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse |
| WA | 0.5008 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros auklet |
| WI | 0.1415 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| WV | 0.0079 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| WY | 0.1964 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |



### Top Unique State Birds When Sorted by Species

| State | Score | Bird | Common Name |
|--:|---|---|---|
| AK | 0.9934 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) | Violet Shag |
| AL | 0.0607 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| AR | 0.0372 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher |
| AZ | 0.9356 | [Peucaea carpalis](https://en.wikipedia.org/wiki/Peucaea_carpalis) | Rufous-winged Sparrow |
| CA | 0.9850 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie |
| CO | 0.7192 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |
| CT | 0.0817 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow |
| DC | 0.0112 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| DE | 0.0974 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| FL | 0.9492 | [Aphelocoma coerulescens](https://en.wikipedia.org/wiki/Aphelocoma_coerulescens) | Florida Scrub-Jay |
| GA | 0.2767 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| HI | 0.9980 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| IA | 0.0218 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| ID | 0.9937 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill |
| IL | 0.2270 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| IN | 0.0700 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur |
| KS | 0.2114 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow |
| KY | 0.0169 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| LA | 0.1051 | [Rallus elegans](https://en.wikipedia.org/wiki/Rallus_elegans) | King Rail |
| MA | 0.5509 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| MD | 0.1034 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher |
| ME | 0.5279 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) | Atlantic puffin |
| MI | 0.6333 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler |
| MN | 0.1150 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| MO | 0.0933 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler |
| MS | 0.0305 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| MT | 0.1975 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow |
| NC | 0.5993 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) | Black-capped petrel |
| ND | 0.1474 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| NE | 0.0422 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| NH | 0.2372 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| NJ | 0.2621 | [Tringa nebularia](https://en.wikipedia.org/wiki/Tringa_nebularia) | Common greenshank |
| NM | 0.3686 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse |
| NV | 0.1529 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| NY | 0.1862 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| OH | 0.0827 | [Setophaga castanea](https://en.wikipedia.org/wiki/Setophaga_castanea) | Bay-breasted Warbler |
| OK | 0.0864 | [Vireo atricapilla](https://en.wikipedia.org/wiki/Vireo_atricapilla) | Black-capped Vireo |
| OR | 0.5643 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| PA | 0.0880 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| RI | 0.0584 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| SC | 0.1377 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker |
| SD | 0.0381 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| TN | 0.0408 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| TX | 0.9187 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse |
| UT | 0.1868 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| VA | 0.1371 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) | Black-tailed godwit |
| VT | 0.0333 | [Empidonax alnorum](https://en.wikipedia.org/wiki/Empidonax_alnorum) | Alder Flycatcher |
| WA | 0.5008 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros auklet |
| WI | 0.1848 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| WV | 0.0249 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler |
| WY | 0.1964 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |









## Scores for Bird Genera by State

### Top Genera for Alaska  (AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9838 | [Phylloscopus](https://en.wikipedia.org/wiki/Phylloscopus) | Leaf warbler | 5694 | [Phylloscopus borealis](https://en.wikipedia.org/wiki/Phylloscopus_borealis) | Arctic Warbler |
| 0.9806 | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | 30617 | [Aethia pusilla](https://en.wikipedia.org/wiki/Aethia_pusilla) | Least auklet |
| 0.9741 | [Luscinia](https://en.wikipedia.org/wiki/Luscinia) |  | 3311 | [Luscinia svecica](https://en.wikipedia.org/wiki/Luscinia_svecica) | Bluethroat |
| 0.9283 | [Polysticta](https://en.wikipedia.org/wiki/Polysticta) |  | 7277 | [Polysticta stelleri](https://en.wikipedia.org/wiki/Polysticta_stelleri) | Steller's Eider |
| 0.8570 | [Motacilla](https://en.wikipedia.org/wiki/Motacilla) | Wagtail | 11596 | [Motacilla tschutschensis](https://en.wikipedia.org/wiki/Motacilla_tschutschensis) | Eastern Yellow Wagtail |
| 0.5080 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 48084 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned puffin |
| 0.5055 | [Fringilla](https://en.wikipedia.org/wiki/Fringilla)∀ |  | 2344 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla)∀ | Brambling |
| 0.4898 | [Oenanthe](https://en.wikipedia.org/wiki/Oenanthe) | wheatear | 5543 | [Oenanthe oenanthe](https://en.wikipedia.org/wiki/Oenanthe_oenanthe) | Northern Wheatear |
| 0.4783 | [Lagopus](https://en.wikipedia.org/wiki/Lagopus)‡ | Ptarmigan | 20161 | [Lagopus muta](https://en.wikipedia.org/wiki/Lagopus_muta) | Rock Ptarmigan |
| 0.3956 | [Rissa](https://en.wikipedia.org/wiki/Kittiwake) | Kittiwake | 60795 | [Rissa brevirostris](https://en.wikipedia.org/wiki/Rissa_brevirostris) | Red-legged kittiwake |






### Top Genera for Alabama  (AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0607 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 2905 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0558 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | 1504 | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane |
| 0.0311 | [Lonchura](https://en.wikipedia.org/wiki/Lonchura)* |  | 1693 | [Lonchura punctulata](https://en.wikipedia.org/wiki/Lonchura_punctulata)* | Scaly-breasted Munia |
| 0.0257 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | 2926 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0227 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 24522 | [Thalasseus sandvicensis](https://en.wikipedia.org/wiki/Thalasseus_sandvicensis) | Sandwich Tern |
| 0.0219 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 9976 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0163 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 4757 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0149 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| 0.0142 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10981 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0138 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 59435 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher |






### Top Genera for Arkansas  (AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0323 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10710 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0198 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 10491 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0158 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 7000 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0145 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | 4347 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow |
| 0.0140 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10221 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0132 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 6445 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0112 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 17013 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0095 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 55044 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0080 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0076 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 541 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |






### Top Genera for Arizona  (AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9038 | [Agapornis](https://en.wikipedia.org/wiki/Agapornis)* | Lovebird | 23043 | [Agapornis roseicollis](https://en.wikipedia.org/wiki/Agapornis_roseicollis)* | Rosy-faced lovebird |
| 0.8668 | [Amphispizopsis](https://en.wikipedia.org/wiki/Amphispizopsis) | Sparrow | 5685 | [Amphispizopsis quinquestriata](https://en.wikipedia.org/wiki/Amphispizopsis_quinquestriata) | Five-striped Sparrow |
| 0.7679 | [Eugenes](https://en.wikipedia.org/wiki/Eugenes) |  | 59354 | [Eugenes fulgens](https://en.wikipedia.org/wiki/Eugenes_fulgens) | Rivoli's Hummingbird |
| 0.7563 | [Cyrtonyx](https://en.wikipedia.org/wiki/Cyrtonyx) |  | 13850 | [Cyrtonyx montezumae](https://en.wikipedia.org/wiki/Cyrtonyx_montezumae) | Montezuma Quail |
| 0.7212 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 200508 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.6745 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 386191 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.6634 | [Euptilotis](https://en.wikipedia.org/wiki/Euptilotis)∀ |  | 1168 | [Euptilotis neoxenus](https://en.wikipedia.org/wiki/Euptilotis_neoxenus)∀ | Eared quetzal |
| 0.6623 | [Cynanthus](https://en.wikipedia.org/wiki/Cynanthus) | Hummingbird | 169527 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed hummingbird |
| 0.6260 | [Micrathene](https://en.wikipedia.org/wiki/Micrathene) |  | 13070 | [Micrathene whitneyi](https://en.wikipedia.org/wiki/Micrathene_whitneyi) | Elf owl |
| 0.6087 | [Gymnogyps](https://en.wikipedia.org/wiki/Gymnogyps) | California condor | 5524 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor |






### Top Genera for California  (CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.7176 | [Euplectes](https://en.wikipedia.org/wiki/Euplectes)* | Bishop | 1315 | [Euplectes franciscanus](https://en.wikipedia.org/wiki/Euplectes_franciscanus)* | Northern red bishop |
| 0.5596 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 57649 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.4400 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) | Mountain Quail | 8665 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.3036 | [Elanus](https://en.wikipedia.org/wiki/Elanus) | Kite | 40693 | [Elanus leucurus](https://en.wikipedia.org/wiki/Elanus_leucurus) | White-tailed Kite |
| 0.2122 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 5326 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's auklet |
| 0.2079 | [Brotogeris](https://en.wikipedia.org/wiki/Brotogeris)* |  | 2407 | [Brotogeris chiriri](https://en.wikipedia.org/wiki/Brotogeris_chiriri)* | Yellow-chevroned Parakeet |
| 0.1668 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 7516 | [Artemisiospiza belli](https://en.wikipedia.org/wiki/Artemisiospiza_belli) | Bell's Sparrow |
| 0.1595 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 129054 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| 0.1418 | [Gymnogyps](https://en.wikipedia.org/wiki/Gymnogyps) | California condor | 1354 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor |
| 0.1380 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 112390 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |






### Top Genera for Colorado  (CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2734 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 5484 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.2622 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 21537 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |
| 0.2581 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)‡ | Lark Bunting | 28847 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)‡ | Lark Bunting |
| 0.2200 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.1881 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 73348 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.1809 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 12356 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1692 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 17639 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.1675 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 24773 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.1629 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 210475 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.1527 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 31182 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |






### Top Genera for Connecticut  (CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0429 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 6889 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet |
| 0.0390 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 7306 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0333 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 22502 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0286 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 21206 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0286 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 9088 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0209 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 47578 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0198 | [Sternula](https://en.wikipedia.org/wiki/Sternula) | Small Tern | 13080 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0194 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) | Sparrow | 8950 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow |
| 0.0170 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 64233 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan |
| 0.0168 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 17906 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |






### Top Genera for District of Columbia  (DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0069 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 24475 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0036 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 188 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0036 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 41998 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0035 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)‡ | Wood Thrush | 7815 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)‡ | Wood Thrush |
| 0.0027 | [Polioptila](https://en.wikipedia.org/wiki/Polioptila) | Gnatcatcher | 16764 | [Polioptila caerulea](https://en.wikipedia.org/wiki/Polioptila_caerulea) | Blue-gray Gnatcatcher |
| 0.0026 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow |
| 0.0026 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 30486 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| 0.0026 | [Xema](https://en.wikipedia.org/wiki/Xema) | Xeme | 207 | [Xema sabini](https://en.wikipedia.org/wiki/Xema_sabini) | Sabine's gull |
| 0.0024 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 53975 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling |
| 0.0022 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 25165 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |






### Top Genera for Delaware  (DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0331 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) | Sparrow | 10447 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0250 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 16285 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0196 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 3537 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0192 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) | Petrel | 45 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| 0.0189 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 53108 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0181 | [Limnodromus](https://en.wikipedia.org/wiki/Limnodromus) |  | 21701 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher |
| 0.0179 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 42296 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0161 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | 381 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| 0.0161 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 6969 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern gannet |
| 0.0154 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 14751 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |






### Top Genera for Florida  (FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9492 | [Melanospiza](https://en.wikipedia.org/wiki/Melanospiza)∀ |  | 1164 | [Melanospiza bicolor](https://en.wikipedia.org/wiki/Melanospiza_bicolor)∀ | Black-faced grassquit |
| 0.9487 | [Gracula](https://en.wikipedia.org/wiki/Gracula)* | Hill Myna | 2142 | [Gracula religiosa](https://en.wikipedia.org/wiki/Gracula_religiosa)* | Common Hill Myna |
| 0.9384 | [Thectocercus](https://en.wikipedia.org/wiki/Thectocercus)∀ |  | 6770 | [Thectocercus acuticaudatus](https://en.wikipedia.org/wiki/Thectocercus_acuticaudatus)∀ |  |
| 0.9345 | [Ara](https://en.wikipedia.org/wiki/Ara)∀ |  | 2611 | [Ara ararauna](https://en.wikipedia.org/wiki/Ara_ararauna)∀ | Blue-and-yellow Macaw |
| 0.9340 | [Aratinga](https://en.wikipedia.org/wiki/Aratinga)* | Conure | 47057 | [Aratinga nenday](https://en.wikipedia.org/wiki/Aratinga_nenday)* | Nanday Parakeet |
| 0.8956 | [Cairina](https://en.wikipedia.org/wiki/Cairina) | Muscovy duck | 97493 | [Cairina moschata](https://en.wikipedia.org/wiki/Cairina_moschata) | Muscovy Duck |
| 0.8711 | [Aramus](https://en.wikipedia.org/wiki/Aramus_(bird)) | Limpkin | 184399 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin |
| 0.8277 | [Pavo](https://en.wikipedia.org/wiki/Pavo)* |  | 9473 | [Pavo cristatus](https://en.wikipedia.org/wiki/Pavo_cristatus)* | Indian peafowl |
| 0.7299 | [Rostrhamus](https://en.wikipedia.org/wiki/Rostrhamus) |  | 32354 | [Rostrhamus sociabilis](https://en.wikipedia.org/wiki/Rostrhamus_sociabilis) | Snail Kite |
| 0.7011 | [Elanoides](https://en.wikipedia.org/wiki/Elanoides) | Swallow-tailed Kite | 111055 | [Elanoides forficatus](https://en.wikipedia.org/wiki/Elanoides_forficatus) | Swallow-tailed Kite |






### Top Genera for Georgia  (GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0911 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 4722 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0647 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus)∀ |  | 167 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing |
| 0.0516 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 28067 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0426 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | 179633 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)‡ | Brown Thrasher |
| 0.0397 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 16431 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0384 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0300 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 264143 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0297 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 249060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| 0.0290 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 288903 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| 0.0288 | [Antrostomus](https://en.wikipedia.org/wiki/Antrostomus) | Nightjar | 10356 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow |






### Top Genera for Hawaii  (HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.9981 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)∀ | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* | Warbling white-eye |
| 0.9981 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)∀ |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* | Zebra dove |
| 0.9980 | [Himatione](https://en.wikipedia.org/wiki/Himatione) | Honeycreeper | 35689 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| 0.9980 | [Chlorodrepanis](https://en.wikipedia.org/wiki/Chlorodrepanis) |  | 34136 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) | Hawaii amakihi |
| 0.9980 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria capitata](https://en.wikipedia.org/wiki/Paroaria_capitata)* | Yellow-billed cardinal |
| 0.9980 | [Copsychus](https://en.wikipedia.org/wiki/Copsychus)* |  | 18329 | [Copsychus malabaricus](https://en.wikipedia.org/wiki/Copsychus_malabaricus)* | White-rumped shama |
| 0.9980 | [Leiothrix](https://en.wikipedia.org/wiki/Leiothrix)* |  | 17965 | [Leiothrix lutea](https://en.wikipedia.org/wiki/Leiothrix_lutea)* | Red-billed leiothrix |
| 0.9980 | [Chasiempis](https://en.wikipedia.org/wiki/Chasiempis) |  | 17400 | [Chasiempis sandwichensis](https://en.wikipedia.org/wiki/Chasiempis_sandwichensis) | Hawaii elepaio |
| 0.9980 | [Drepanis](https://en.wikipedia.org/wiki/Drepanis) |  | 17194 | [Drepanis coccinea](https://en.wikipedia.org/wiki/Drepanis_coccinea) | Iiwi |
| 0.9980 | [Ortygornis](https://en.wikipedia.org/wiki/Ortygornis)* |  | 16235 | [Ortygornis pondicerianus](https://en.wikipedia.org/wiki/Ortygornis_pondicerianus)* | Gray francolin |






### Top Genera for Iowa  (IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0325 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 15850 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0290 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 21293 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant |
| 0.0245 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) | Ross's gull | 76 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's gull |
| 0.0181 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 1961 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0082 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 679 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge |
| 0.0078 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 9534 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0068 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 13476 | [Anser albifrons](https://en.wikipedia.org/wiki/Anser_albifrons) | Greater White-fronted Goose |
| 0.0062 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 15618 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0057 | [Petrochelidon](https://en.wikipedia.org/wiki/Petrochelidon) |  | 13799 | [Petrochelidon pyrrhonota](https://en.wikipedia.org/wiki/Petrochelidon_pyrrhonota) | Cliff Swallow |
| 0.0050 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 23362 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |






### Top Genera for Idaho  (ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1077 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1305 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0973 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 3634 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar |
| 0.0684 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0631 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6303 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0603 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3493 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge |
| 0.0517 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 53404 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail |
| 0.0471 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 2206 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0467 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) | Flammulated owl | 575 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| 0.0391 | [Prunella](https://en.wikipedia.org/wiki/Prunella)∀ |  | 51 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella)∀ | Siberian accentor |
| 0.0380 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 7777 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |






### Top Genera for Illinois  (IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2942 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 1798 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch |
| 0.1906 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 18756 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0999 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 4029 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0816 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 46626 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0676 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 11545 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet |
| 0.0466 | [Hydroprogne](https://en.wikipedia.org/wiki/Hydroprogne) |  | 70704 | [Hydroprogne caspia](https://en.wikipedia.org/wiki/Hydroprogne_caspia) | Caspian Tern |
| 0.0385 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 94643 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0340 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 233 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) | Ivory gull |
| 0.0336 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163028 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0256 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 16647 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |






### Top Genera for Indiana  (IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0744 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7607 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0299 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 15774 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0256 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 1255 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0242 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 16357 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0235 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 12791 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0159 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 42933 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0143 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 38634 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0141 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 15339 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0137 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 32496 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |
| 0.0130 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 224909 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |






### Top Genera for Kansas  (KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0768 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 36284 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0580 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 22554 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0561 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 8401 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0418 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 14481 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0343 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) | Lark Sparrow | 24003 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0337 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 2429 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0326 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 12774 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0257 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 92201 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0216 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18980 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant |
| 0.0211 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 34440 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |






### Top Genera for Kentucky  (KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0169 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8107 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0162 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 959 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0140 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 6725 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0136 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10504 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0114 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 3656 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0090 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 15628 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0085 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 35716 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0080 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 98073 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0077 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 51917 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0077 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 5726 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |






### Top Genera for Louisiana  (LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0845 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 27044 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0722 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 3553 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0664 | [Coturnicops](https://en.wikipedia.org/wiki/Coturnicops) | Rail | 942 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail |
| 0.0636 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | 6719 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0515 | [Platalea](https://en.wikipedia.org/wiki/Platalea) |  | 22937 | [Platalea ajaja](https://en.wikipedia.org/wiki/Platalea_ajaja) | Roseate Spoonbill |
| 0.0495 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 50157 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret |
| 0.0483 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 20585 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0437 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 28527 | [Dendrocygna bicolor](https://en.wikipedia.org/wiki/Dendrocygna_bicolor) | Fulvous Whistling-Duck |
| 0.0423 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 63812 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0386 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 37903 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |






### Top Genera for Massachusetts  (MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.5509 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) | Petrel | 1036 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| 0.3147 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 16342 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater |
| 0.2586 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 13352 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx shearwater |
| 0.2579 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 17049 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.2391 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus)∀ |  | 553 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing |
| 0.2283 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | 4466 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| 0.2090 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 147686 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.1909 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 19874 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.1782 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 28983 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.1147 | [Ardenna](https://en.wikipedia.org/wiki/Ardenna) | Shearwater | 27804 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) | Great shearwater |






### Top Genera for Maryland  (MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0482 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0453 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 184681 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0391 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 14340 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0338 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 3652 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.0330 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 19100 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0328 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 82855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0315 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 2816 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater |
| 0.0304 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 20992 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0303 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | 1004 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| 0.0283 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 60125 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |






### Top Genera for Maine  (ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1955 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 127239 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.1745 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 17505 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) | Atlantic puffin |
| 0.1504 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 58921 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black guillemot |
| 0.1498 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 14447 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.1297 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8358 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.1228 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 18634 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0907 | [Hydrobates](https://en.wikipedia.org/wiki/Hydrobates) | Storm Petrel | 7558 | [Hydrobates leucorhous](https://en.wikipedia.org/wiki/Hydrobates_leucorhous) | Leach's storm-petrel |
| 0.0682 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 25405 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern gannet |
| 0.0479 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 2786 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx shearwater |
| 0.0463 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 34160 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |






### Top Genera for Michigan  (MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0984 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 176499 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0841 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 236621 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan |
| 0.0570 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 125158 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0475 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 295 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) | Ivory gull |
| 0.0309 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147923 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0288 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 90666 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0285 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 29441 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0243 | [Plectrophenax](https://en.wikipedia.org/wiki/Plectrophenax) |  | 19806 | [Plectrophenax nivalis](https://en.wikipedia.org/wiki/Plectrophenax_nivalis) | Snow Bunting |
| 0.0241 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 4728 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0239 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 167208 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |






### Top Genera for Minnesota  (MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1064 | [Pagophila](https://en.wikipedia.org/wiki/Pagophila) | Ivory gull | 459 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) | Ivory gull |
| 0.0791 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 5462 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0582 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 46603 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant |
| 0.0533 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 2176 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0454 | [Picoides](https://en.wikipedia.org/wiki/Picoides) | Woodpecker | 6040 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker |
| 0.0397 | [Pinicola](https://en.wikipedia.org/wiki/Pinicola) |  | 13668 | [Pinicola enucleator](https://en.wikipedia.org/wiki/Pinicola_enucleator) | Pine Grosbeak |
| 0.0371 | [Perisoreus](https://en.wikipedia.org/wiki/Perisoreus) |  | 14026 | [Perisoreus canadensis](https://en.wikipedia.org/wiki/Perisoreus_canadensis) | Canada Jay |
| 0.0321 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 32330 | [Acanthis hornemanni](https://en.wikipedia.org/wiki/Acanthis_hornemanni) | Hoary Redpoll |
| 0.0272 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 21256 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |
| 0.0265 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 12204 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |






### Top Genera for Missouri  (MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0678 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 34191 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0497 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 21081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0351 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 4090 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0287 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22318 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0274 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 42272 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0265 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 29694 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0255 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 13589 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0253 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 44077 | [Anser albifrons](https://en.wikipedia.org/wiki/Anser_albifrons) | Greater White-fronted Goose |
| 0.0229 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10221 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0179 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 15065 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |






### Top Genera for Mississippi  (MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0354 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 1697 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0305 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | 3142 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0234 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 8333 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0196 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8279 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0174 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 17938 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0169 | [Sternula](https://en.wikipedia.org/wiki/Sternula) | Small Tern | 7879 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0166 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 5820 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0107 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 30763 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican |
| 0.0104 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 9571 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |
| 0.0103 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 29491 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |






### Top Genera for Montana  (MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1831 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 3501 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.1315 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 24361 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.1289 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 7149 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge |
| 0.1130 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1377 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0885 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0679 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4325 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0668 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 9534 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.0657 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 17889 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0602 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 23231 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0501 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 4307 | [Leucosticte tephrocotis](https://en.wikipedia.org/wiki/Leucosticte_tephrocotis) | Gray-crowned Rosy-Finch |






### Top Genera for North Carolina  (NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.4415 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | 6000 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) | Black-capped petrel |
| 0.2431 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 12415 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater |
| 0.1737 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 8919 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) | Audubon's shearwater |
| 0.1226 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8420 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.1059 | [Onychoprion](https://en.wikipedia.org/wiki/Onychoprion) | Brown-back Tern | 3740 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) | Bridled tern |
| 0.0745 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 4154 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0570 | [Hydrobates](https://en.wikipedia.org/wiki/Hydrobates) | Storm Petrel | 5691 | [Hydrobates castro](https://en.wikipedia.org/wiki/Hydrobates_castro) | Band-rumped storm-petrel |
| 0.0473 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0439 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus)∀ |  | 132 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing |
| 0.0413 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 22210 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |






### Top Genera for North Dakota  (ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1106 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 6539 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0652 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3576 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge |
| 0.0513 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 7042 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0352 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 24049 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant |
| 0.0326 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18180 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0303 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 9608 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |
| 0.0280 | [Coturnicops](https://en.wikipedia.org/wiki/Coturnicops) | Rail | 385 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail |
| 0.0259 | [Calcarius](https://en.wikipedia.org/wiki/Calcarius) | Longspur | 6966 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur |
| 0.0239 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 2739 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |
| 0.0234 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8173 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |






### Top Genera for Nebraska  (NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0692 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4213 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0422 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 19658 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0365 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5257 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0258 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 10081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0257 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18728 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant |
| 0.0238 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 2834 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |
| 0.0232 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8437 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0195 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) | Lark Sparrow | 13158 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0155 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 52365 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark |
| 0.0125 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) | Ross's gull | 43 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's gull |






### Top Genera for New Hampshire  (NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0251 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | 546 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| 0.0226 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 4048 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0205 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 16704 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0178 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 1443 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.0135 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 1811 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0135 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 8834 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse |
| 0.0134 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 34197 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0121 | [Canachites](https://en.wikipedia.org/wiki/Canachites) | Fool Hen | 675 | [Canachites canadensis](https://en.wikipedia.org/wiki/Canachites_canadensis) | Spruce Grouse |
| 0.0120 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 5077 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0091 | [Picoides](https://en.wikipedia.org/wiki/Picoides) | Woodpecker | 1578 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker |






### Top Genera for New Jersey  (NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2425 | [Vanellus](https://en.wikipedia.org/wiki/Vanellus)∀ |  | 552 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing |
| 0.1155 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 68430 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.1034 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 40882 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0979 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | 11666 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0950 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) | Sparrow | 32951 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0931 | [Alle](https://en.wikipedia.org/wiki/Alle) | Dovekie | 2087 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie |
| 0.0906 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 37469 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern gannet |
| 0.0731 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) | Petrel | 181 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| 0.0710 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 13721 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0686 | [Sternula](https://en.wikipedia.org/wiki/Sternula) | Small Tern | 37555 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |






### Top Genera for New Mexico  (NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2172 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 13673 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1401 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | 46838 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus)‡ | Greater Roadrunner |
| 0.1306 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 10584 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0834 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 32323 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0815 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 23571 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0802 | [Salpinctes](https://en.wikipedia.org/wiki/Salpinctes) |  | 22761 | [Salpinctes obsoletus](https://en.wikipedia.org/wiki/Salpinctes_obsoletus) | Rock Wren |
| 0.0800 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 66915 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee |
| 0.0767 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 14189 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0754 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 3551 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0715 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 8353 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |






### Top Genera for Nevada  (NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1247 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 5324 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0866 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 5444 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0662 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6385 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0523 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 645 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0504 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 14504 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.0496 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 29373 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0492 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0475 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 1810 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar |
| 0.0463 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 12902 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0402 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 7780 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |






### Top Genera for New York  (NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.2969 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 1971 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch |
| 0.1048 | [Pelagodroma](https://en.wikipedia.org/wiki/Pelagodroma) | Petrel | 286 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel |
| 0.0683 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 61677 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0656 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 16757 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0648 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 69918 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |
| 0.0578 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 54113 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0548 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 150414 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0527 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 13166 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet |
| 0.0517 | [Rhodostethia](https://en.wikipedia.org/wiki/Rhodostethia) | Ross's gull | 281 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's gull |
| 0.0510 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 598555 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |






### Top Genera for Ohio  (OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1040 | [Fringilla](https://en.wikipedia.org/wiki/Fringilla)∀ |  | 632 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla)∀ | Brambling |
| 0.0683 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 36537 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0549 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7629 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0466 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 21715 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0390 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 98855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0333 | [Oporornis](https://en.wikipedia.org/wiki/Oporornis) | Connecticut Warbler | 2121 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler |
| 0.0303 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 91542 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0300 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 31737 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0297 | [Chroicocephalus](https://en.wikipedia.org/wiki/Chroicocephalus) |  | 56168 | [Chroicocephalus philadelphia](https://en.wikipedia.org/wiki/Chroicocephalus_philadelphia) | Bonaparte's Gull |
| 0.0276 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163264 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |






### Top Genera for Oklahoma  (OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0714 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 21873 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0311 | [Nomonyx](https://en.wikipedia.org/wiki/Nomonyx)∀ |  | 46 | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus)∀ | Masked Duck |
| 0.0295 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 14500 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0249 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 3825 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0242 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 9753 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0229 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) | Lark Sparrow | 15360 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0119 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)† | Roadrunner | 5124 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus)† | Greater Roadrunner |
| 0.0115 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher |
| 0.0111 | [Aimophila](https://en.wikipedia.org/wiki/Aimophila) |  | 2308 | [Aimophila ruficeps](https://en.wikipedia.org/wiki/Aimophila_ruficeps) | Rufous-crowned Sparrow |
| 0.0108 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)∀ | Collared Dove | 36943 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove |






### Top Genera for Oregon  (OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.4317 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) | Mountain Quail | 8746 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.3604 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 38911 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.2881 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 374161 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.2327 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 6098 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's auklet |
| 0.2181 | [Phoebastria](https://en.wikipedia.org/wiki/Phoebastria) |  | 8774 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) | Black-footed albatross |
| 0.1914 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 82130 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.1646 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 141123 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.1564 | [Urile](https://en.wikipedia.org/wiki/Urile) | Cormorant | 76024 | [Urile penicillatus](https://en.wikipedia.org/wiki/Urile_penicillatus) | Brandt's Cormorant |
| 0.1523 | [Patagioenas](https://en.wikipedia.org/wiki/Patagioenas) |  | 57823 | [Patagioenas fasciata](https://en.wikipedia.org/wiki/Patagioenas_fasciata) | Band-tailed Pigeon |
| 0.1480 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 261771 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |






### Top Genera for Pennsylvania  (PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0880 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 171036 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0435 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 456717 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0401 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 557667 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0370 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 127243 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0368 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 620147 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0282 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 14138 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0256 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 169324 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0227 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 323557 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| 0.0218 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 947363 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal |
| 0.0204 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 29095 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |






### Top Genera for Rhode Island  (RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0584 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 8422 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0268 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 18187 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0167 | [Histrionicus](https://en.wikipedia.org/wiki/Histrionicus) |  | 4628 | [Histrionicus histrionicus](https://en.wikipedia.org/wiki/Histrionicus_histrionicus) | Harlequin Duck |
| 0.0163 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 907 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater |
| 0.0138 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 1489 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0122 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) | Sparrow | 4026 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow |
| 0.0118 | [Sternula](https://en.wikipedia.org/wiki/Sternula) | Small Tern | 5667 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0109 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 20964 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |
| 0.0102 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 771 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel |
| 0.0100 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 4047 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern gannet |






### Top Genera for South Carolina  (SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0871 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 40234 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0598 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 3114 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0587 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 20288 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0552 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 52941 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0383 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 15485 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0377 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 33849 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |
| 0.0369 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) | Tern | 4480 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0359 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 195795 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron |
| 0.0350 | [Elanoides](https://en.wikipedia.org/wiki/Elanoides) | Swallow-tailed Kite | 6901 | [Elanoides forficatus](https://en.wikipedia.org/wiki/Elanoides_forficatus) | Swallow-tailed Kite |
| 0.0335 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 38639 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |






### Top Genera for South Dakota  (SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0542 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 3235 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0381 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5213 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0312 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 3391 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |
| 0.0219 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)‡* | Pheasant | 15094 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant |
| 0.0181 | [Athene](https://en.wikipedia.org/wiki/Athene) |  | 1976 | [Athene cunicularia](https://en.wikipedia.org/wiki/Athene_cunicularia) | Burrowing Owl |
| 0.0167 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 9544 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0119 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 2257 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0113 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 4140 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0106 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 5350 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0091 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 3198 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |






### Top Genera for Tennessee  (TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0424 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 2385 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0352 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 16980 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0295 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22678 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0252 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 12762 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0249 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0246 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 7863 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0218 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 181103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| 0.0197 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 9261 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0196 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 199634 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird |
| 0.0184 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 77257 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |






### Top Genera for Texas  (TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.8345 | [Geranoaetus](https://en.wikipedia.org/wiki/Geranoaetus) | Hawk | 54492 | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk |
| 0.7275 | [Arremonops](https://en.wikipedia.org/wiki/Arremonops) |  | 82550 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow |
| 0.6729 | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | 249608 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| 0.6548 | [Nyctidromus](https://en.wikipedia.org/wiki/Nyctidromus) |  | 31129 | [Nyctidromus albicollis](https://en.wikipedia.org/wiki/Nyctidromus_albicollis) | Common Pauraque |
| 0.6519 | [Tachybaptus](https://en.wikipedia.org/wiki/Tachybaptus) |  | 65119 | [Tachybaptus dominicus](https://en.wikipedia.org/wiki/Tachybaptus_dominicus) | Least Grebe |
| 0.6198 | [Cyanocorax](https://en.wikipedia.org/wiki/Cyanocorax) |  | 150450 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay |
| 0.6030 | [Parabuteo](https://en.wikipedia.org/wiki/Parabuteo) |  | 80483 | [Parabuteo unicinctus](https://en.wikipedia.org/wiki/Parabuteo_unicinctus) | Harris's Hawk |
| 0.5377 | [Nomonyx](https://en.wikipedia.org/wiki/Nomonyx)∀ |  | 774 | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus)∀ | Masked Duck |
| 0.5253 | [Chloroceryle](https://en.wikipedia.org/wiki/Chloroceryle) |  | 42946 | [Chloroceryle americana](https://en.wikipedia.org/wiki/Chloroceryle_americana) | Green Kingfisher |
| 0.5253 | [Leptotila](https://en.wikipedia.org/wiki/Leptotila) |  | 83884 | [Leptotila verreauxi](https://en.wikipedia.org/wiki/Leptotila_verreauxi) | White-tipped Dove |






### Top Genera for Utah  (UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1930 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 7064 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar |
| 0.1868 | [Psiloscops](https://en.wikipedia.org/wiki/Psiloscops) | Flammulated owl | 2119 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl |
| 0.1671 | [Gymnogyps](https://en.wikipedia.org/wiki/Gymnogyps) | California condor | 1515 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor |
| 0.1244 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 7974 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.1187 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1455 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0968 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 9559 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0868 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 23315 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0751 | [Aeronautes](https://en.wikipedia.org/wiki/Aeronautes) |  | 13570 | [Aeronautes saxatalis](https://en.wikipedia.org/wiki/Aeronautes_saxatalis) | White-throated Swift |
| 0.0736 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0707 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 5931 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |






### Top Genera for Virginia  (VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0570 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 18144 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0559 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0414 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 174913 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0385 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 23888 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0367 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 344496 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird |
| 0.0366 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 68861 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0336 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 195902 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0292 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 475019 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0280 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 17519 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0261 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 339498 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |






### Top Genera for Vermont  (VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0297 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 16963 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse |
| 0.0243 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 56705 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0216 | [Dolichonyx](https://en.wikipedia.org/wiki/Dolichonyx) |  | 18269 | [Dolichonyx oryzivorus](https://en.wikipedia.org/wiki/Dolichonyx_oryzivorus) | Bobolink |
| 0.0198 | [Canachites](https://en.wikipedia.org/wiki/Canachites) | Fool Hen | 1039 | [Canachites canadensis](https://en.wikipedia.org/wiki/Canachites_canadensis) | Spruce Grouse |
| 0.0180 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 7351 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0152 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 34849 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0144 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 16066 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll |
| 0.0139 | [Sphyrapicus](https://en.wikipedia.org/wiki/Sphyrapicus) |  | 46917 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker |
| 0.0138 | [Botaurus](https://en.wikipedia.org/wiki/Botaurus) |  | 6920 | [Botaurus lentiginosus](https://en.wikipedia.org/wiki/Botaurus_lentiginosus) | American Bittern |
| 0.0123 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 16443 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |






### Top Genera for Washington  (WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.5008 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | 56517 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros auklet |
| 0.4906 | [Prunella](https://en.wikipedia.org/wiki/Prunella)∀ |  | 589 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella)∀ | Siberian accentor |
| 0.2924 | [Ptychoramphus](https://en.wikipedia.org/wiki/Ptychoramphus) |  | 7628 | [Ptychoramphus aleuticus](https://en.wikipedia.org/wiki/Ptychoramphus_aleuticus) | Cassin's auklet |
| 0.2785 | [Urile](https://en.wikipedia.org/wiki/Urile) | Cormorant | 128798 | [Urile penicillatus](https://en.wikipedia.org/wiki/Urile_penicillatus) | Brandt's Cormorant |
| 0.2287 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 98229 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.2227 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 92260 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot |
| 0.2225 | [Brachyramphus](https://en.wikipedia.org/wiki/Brachyramphus) |  | 23655 | [Brachyramphus marmoratus](https://en.wikipedia.org/wiki/Brachyramphus_marmoratus) | Marbled Murrelet |
| 0.2003 | [Phoebastria](https://en.wikipedia.org/wiki/Phoebastria) |  | 8337 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) | Black-footed albatross |
| 0.1925 | [Cypseloides](https://en.wikipedia.org/wiki/Cypseloides) | Swift | 5354 | [Cypseloides niger](https://en.wikipedia.org/wiki/Cypseloides_niger) | Black Swift |
| 0.1891 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 331274 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |






### Top Genera for Wisconsin  (WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1415 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 231517 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.1071 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 755 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch |
| 0.0698 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 8403 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0598 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 43527 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |
| 0.0515 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 120796 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0364 | [Scolopax](https://en.wikipedia.org/wiki/Scolopax) | Woodcock | 17392 | [Scolopax minor](https://en.wikipedia.org/wiki/Scolopax_minor) | American Woodcock |
| 0.0354 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 18353 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus)∀ | White-winged Tern |
| 0.0344 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 27246 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse |
| 0.0337 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147853 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0323 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 85985 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |






### Top Genera for West Virginia  (WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0157 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) | Swainson's warbler | 850 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0128 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) | Warbler | 3533 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0110 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 20027 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| 0.0079 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 37014 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0061 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 10480 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0058 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 67983 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| 0.0053 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 51062 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0049 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0045 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 4123 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0036 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 12467 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |






### Top Genera for Wyoming  (WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1964 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 2281 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.1183 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 2228 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.0773 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 14068 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0623 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 4885 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0612 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 5825 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0470 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 5086 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting |
| 0.0457 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 11895 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0404 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 1788 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0394 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 5444 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.0385 | [Dendragapus](https://en.wikipedia.org/wiki/Dendragapus) |  | 2239 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse |










## Scores for Bird Species by State

### Top Species for Alaska  (AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9934 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) | Violet Shag | 12099 |
| 0.9934 | [Onychoprion aleuticus](https://en.wikipedia.org/wiki/Onychoprion_aleuticus) | Aleutian Tern | 7065 |
| 0.9932 | [Somateria fischeri](https://en.wikipedia.org/wiki/Somateria_fischeri) | Spectacled Eider | 5432 |
| 0.9932 | [Aethia pusilla](https://en.wikipedia.org/wiki/Aethia_pusilla) | Least auklet | 9479 |
| 0.9898 | [Aethia cristatella](https://en.wikipedia.org/wiki/Aethia_cristatella) | Crested auklet | 10114 |
| 0.9894 | [Rissa brevirostris](https://en.wikipedia.org/wiki/Rissa_brevirostris) | Red-legged kittiwake | 6747 |
| 0.9885 | [Brachyramphus brevirostris](https://en.wikipedia.org/wiki/Brachyramphus_brevirostris) | Kittlitz's murrelet | 5066 |
| 0.9838 | [Phylloscopus borealis](https://en.wikipedia.org/wiki/Phylloscopus_borealis) | Arctic Warbler | 5694 |
| 0.9741 | [Luscinia svecica](https://en.wikipedia.org/wiki/Luscinia_svecica) | Bluethroat | 3311 |
| 0.9621 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned puffin | 22891 |






### Top Species for Alabama  (AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0607 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 2905 |
| 0.0605 | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane | 1504 |
| 0.0477 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 32313 |
| 0.0418 | [Lonchura punctulata](https://en.wikipedia.org/wiki/Lonchura_punctulata)* | Scaly-breasted Munia | 1693 |
| 0.0418 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 1689 |
| 0.0327 | [Charadrius nivosus](https://en.wikipedia.org/wiki/Charadrius_nivosus) | Snowy Plover | 3533 |
| 0.0295 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 6284 |
| 0.0274 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 28464 |
| 0.0266 | [Thalasseus sandvicensis](https://en.wikipedia.org/wiki/Thalasseus_sandvicensis) | Sandwich Tern | 6175 |
| 0.0262 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 16340 |






### Top Species for Arkansas  (AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0462 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 575 |
| 0.0372 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 19125 |
| 0.0364 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 7297 |
| 0.0323 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 10710 |
| 0.0260 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 26191 |
| 0.0236 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 970 |
| 0.0233 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow | 2627 |
| 0.0198 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 10491 |
| 0.0197 | [Ammospiza leconteii](https://en.wikipedia.org/wiki/Ammospiza_leconteii) | LeConte's Sparrow | 1422 |
| 0.0162 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 7000 |






### Top Species for Arizona  (AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9356 | [Peucaea carpalis](https://en.wikipedia.org/wiki/Peucaea_carpalis) | Rufous-winged Sparrow | 73068 |
| 0.9134 | [Baeolophus wollweberi](https://en.wikipedia.org/wiki/Baeolophus_wollweberi) | Bridled Titmouse | 147289 |
| 0.9038 | [Agapornis roseicollis](https://en.wikipedia.org/wiki/Agapornis_roseicollis)* | Rosy-faced lovebird | 23043 |
| 0.8972 | [Dryobates arizonae](https://en.wikipedia.org/wiki/Arizona_woodpecker) | Arizona Woodpecker | 47770 |
| 0.8900 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.8837 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee | 262829 |
| 0.8668 | [Amphispizopsis quinquestriata](https://en.wikipedia.org/wiki/Amphispizopsis_quinquestriata) | Five-striped Sparrow | 5685 |
| 0.8617 | [Megascops trichopsis](https://en.wikipedia.org/wiki/Megascops_trichopsis) | Whiskered Screech-Owl | 10842 |
| 0.8541 | [Aphelocoma wollweberi](https://en.wikipedia.org/wiki/Aphelocoma_wollweberi) | Mexican Jay | 130540 |
| 0.8451 | [Colaptes chrysoides](https://en.wikipedia.org/wiki/Colaptes_chrysoides) | Gilded Flicker | 47179 |






### Top Species for California  (CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9850 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie | 17869 |
| 0.9624 | [Dryobates nuttallii](https://en.wikipedia.org/wiki/Dryobates_nuttallii) | Nuttall's Woodpecker | 74045 |
| 0.9206 | [Hydrobates homochroa](https://en.wikipedia.org/wiki/Hydrobates_homochroa) | Ashy storm-petrel | 2162 |
| 0.9066 | [Toxostoma redivivum](https://en.wikipedia.org/wiki/Toxostoma_redivivum) | California Thrasher | 30314 |
| 0.8753 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee | 124793 |
| 0.8725 | [Selasphorus sasin](https://en.wikipedia.org/wiki/Selasphorus_sasin) | Allen's Hummingbird | 37169 |
| 0.8058 | [Baeolophus inornatus](https://en.wikipedia.org/wiki/Baeolophus_inornatus) | Oak Titmouse | 64598 |
| 0.7206 | [Artemisiospiza belli](https://en.wikipedia.org/wiki/Artemisiospiza_belli) | Bell's Sparrow | 6672 |
| 0.7176 | [Euplectes franciscanus](https://en.wikipedia.org/wiki/Euplectes_franciscanus)* | Northern red bishop | 1315 |
| 0.6556 | [Agelaius tricolor](https://en.wikipedia.org/wiki/Agelaius_tricolor) | Tricolored Blackbird | 10914 |






### Top Species for Colorado  (CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.7192 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch | 9642 |
| 0.4863 | [Lagopus leucura](https://en.wikipedia.org/wiki/Lagopus_leucura) | White-tailed Ptarmigan | 3927 |
| 0.4350 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 174912 |
| 0.4321 | [Leucosticte sp.](https://en.wikipedia.org/wiki/Leucosticte) |  | 1152 |
| 0.3093 | [Charadrius montanus](https://en.wikipedia.org/wiki/Charadrius_montanus) | Mountain Plover | 4008 |
| 0.3072 | [Empidonax occidentalis](https://en.wikipedia.org/wiki/Empidonax_occidentalis) | Cordilleran Flycatcher | 38951 |
| 0.2936 | [Spizella sp.](https://en.wikipedia.org/wiki/Spizella) |  | 4251 |
| 0.2734 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 5484 |
| 0.2581 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)‡ | Lark Bunting | 28847 |
| 0.2427 | [Sialia sp.](https://en.wikipedia.org/wiki/Sialia)† |  | 1311 |






### Top Species for Connecticut  (CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0910 | [Anser brachyrhynchus](https://en.wikipedia.org/wiki/Anser_brachyrhynchus)∀ | Pink-footed goose | 948 |
| 0.0817 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 5067 |
| 0.0782 | [Larus canus](https://en.wikipedia.org/wiki/Larus_canus) | Common gull | 240 |
| 0.0725 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 627 |
| 0.0716 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 34897 |
| 0.0639 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis)∀ | Barnacle Goose | 656 |
| 0.0526 | [Falco sp. (small falcon sp.)](https://en.wikipedia.org/wiki/Falcon) |  | 413 |
| 0.0509 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 22502 |
| 0.0442 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan | 63483 |
| 0.0429 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet | 6889 |






### Top Species for District of Columbia  (DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0615 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis)∀ | Barnacle Goose | 536 |
| 0.0308 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 10911 |
| 0.0112 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26969 |
| 0.0076 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 24475 |
| 0.0066 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 4171 |
| 0.0055 | [Setophaga caerulescens](https://en.wikipedia.org/wiki/Setophaga_caerulescens) | Black-throated Blue Warbler | 5766 |
| 0.0054 | [Setophaga striata](https://en.wikipedia.org/wiki/Setophaga_striata) | Blackpoll Warbler | 5085 |
| 0.0045 | [Setophaga tigrina](https://en.wikipedia.org/wiki/Setophaga_tigrina) | Cape May Warbler | 2647 |
| 0.0040 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 7228 |
| 0.0036 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler | 188 |






### Top Species for Delaware  (DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1686 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta) | Little egret | 503 |
| 0.1585 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus)∀ | White-winged Tern | 186 |
| 0.0974 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 9067 |
| 0.0532 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) | Curlew sandpiper | 265 |
| 0.0483 | [Calidris pugnax](https://en.wikipedia.org/wiki/Calidris_pugnax) | Ruff | 841 |
| 0.0461 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 12429 |
| 0.0351 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) | Black-tailed godwit | 61 |
| 0.0339 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher | 19031 |
| 0.0326 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 37786 |
| 0.0294 | [Plegadis falcinellus](https://en.wikipedia.org/wiki/Plegadis_falcinellus) | Glossy Ibis | 15414 |






### Top Species for Florida  (FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9492 | [Amazona amazonica](https://en.wikipedia.org/wiki/Amazona_amazonica)∀ | Orange-winged parrot | 2592 |
| 0.9492 | [Myiarchus sagrae](https://en.wikipedia.org/wiki/Myiarchus_sagrae)∀ | La Sagra's flycatcher | 1277 |
| 0.9492 | [Melanospiza bicolor](https://en.wikipedia.org/wiki/Melanospiza_bicolor)∀ | Black-faced grassquit | 1164 |
| 0.9492 | [Aphelocoma coerulescens](https://en.wikipedia.org/wiki/Aphelocoma_coerulescens) | Florida Scrub-Jay | 30709 |
| 0.9490 | [Porphyrio poliocephalus](https://en.wikipedia.org/wiki/Porphyrio_poliocephalus)* | Gray-headed Swamphen | 24556 |
| 0.9487 | [Gracula religiosa](https://en.wikipedia.org/wiki/Gracula_religiosa)* | Common Hill Myna | 2142 |
| 0.9471 | [Ara ararauna](https://en.wikipedia.org/wiki/Ara_ararauna)∀ | Blue-and-yellow Macaw | 1458 |
| 0.9384 | [Thectocercus acuticaudatus](https://en.wikipedia.org/wiki/Thectocercus_acuticaudatus)∀ |  | 6770 |
| 0.9348 | [Brotogeris versicolurus](https://en.wikipedia.org/wiki/Brotogeris_versicolurus)* | White-winged Parakeet | 1916 |
| 0.9340 | [Aratinga nenday](https://en.wikipedia.org/wiki/Aratinga_nenday)* | Nanday Parakeet | 47057 |






### Top Species for Georgia  (GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2767 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 176715 |
| 0.0911 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 4722 |
| 0.0902 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 3798 |
| 0.0848 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 176004 |
| 0.0647 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing | 167 |
| 0.0636 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 2761 |
| 0.0627 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)‡ | Brown Thrasher | 179633 |
| 0.0624 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |
| 0.0585 | [Antrostomus carolinensis](https://en.wikipedia.org/wiki/Antrostomus_carolinensis) | Chuck-will's-widow | 7091 |
| 0.0535 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 351685 |






### Top Species for Hawaii  (HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9981 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* | Warbling white-eye | 82840 |
| 0.9981 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* | Zebra dove | 78346 |
| 0.9980 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane | 35689 |
| 0.9980 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) | Hawaii amakihi | 29234 |
| 0.9980 | [Fulica alai](https://en.wikipedia.org/wiki/Fulica_alai) | Hawaiian coot | 22293 |
| 0.9980 | [Branta sandvicensis](https://en.wikipedia.org/wiki/Branta_sandvicensis)‡ | Hawaiian goose | 18412 |
| 0.9980 | [Copsychus malabaricus](https://en.wikipedia.org/wiki/Copsychus_malabaricus)* | White-rumped shama | 18329 |
| 0.9980 | [Leiothrix lutea](https://en.wikipedia.org/wiki/Leiothrix_lutea)* | Red-billed leiothrix | 17965 |
| 0.9980 | [Drepanis coccinea](https://en.wikipedia.org/wiki/Drepanis_coccinea) | Iiwi | 17194 |
| 0.9980 | [Paroaria capitata](https://en.wikipedia.org/wiki/Paroaria_capitata)* | Yellow-billed cardinal | 17012 |






### Top Species for Iowa  (IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1469 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus)* | Eurasian Tree Sparrow | 7675 |
| 0.0378 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 47 |
| 0.0325 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 15850 |
| 0.0290 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 21293 |
| 0.0266 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 353 |
| 0.0245 | [Rhodostethia rosea](https://en.wikipedia.org/wiki/Rhodostethia_rosea) | Ross's gull | 76 |
| 0.0219 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 1960 |
| 0.0218 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 24590 |
| 0.0210 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 5050 |
| 0.0196 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 5205 |






### Top Species for Idaho  (ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9937 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill | 2084 |
| 0.1077 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1305 |
| 0.1072 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 53065 |
| 0.0973 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar | 3634 |
| 0.0891 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 10890 |
| 0.0778 | [Haemorhous cassinii](https://en.wikipedia.org/wiki/Haemorhous_cassinii) | Cassin's Finch | 20202 |
| 0.0726 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 1794 |
| 0.0692 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |
| 0.0631 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 6303 |
| 0.0620 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 2206 |






### Top Species for Illinois  (IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2942 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 1798 |
| 0.2549 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus)* | Eurasian Tree Sparrow | 14313 |
| 0.2270 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 18756 |
| 0.0999 | [Oporornis agilis](https://en.wikipedia.org/wiki/Oporornis_agilis) | Connecticut Warbler | 4029 |
| 0.0816 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 46626 |
| 0.0793 | [Catharus minimus](https://en.wikipedia.org/wiki/Catharus_minimus) | Gray-cheeked Thrush | 19054 |
| 0.0789 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 13460 |
| 0.0706 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 109 |
| 0.0676 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus)* | Monk Parakeet | 11545 |
| 0.0671 | [Catharus sp.](https://en.wikipedia.org/wiki/Catharus)† |  | 3364 |






### Top Species for Indiana  (IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0892 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 7607 |
| 0.0819 | [Grus grus](https://en.wikipedia.org/wiki/Grus_grus)∀ | Common crane | 165 |
| 0.0700 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 949 |
| 0.0675 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) | Black-tailed godwit | 121 |
| 0.0430 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 10117 |
| 0.0399 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 50156 |
| 0.0389 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 6585 |
| 0.0299 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 15774 |
| 0.0283 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 23122 |
| 0.0273 | [Catharus minimus](https://en.wikipedia.org/wiki/Catharus_minimus) | Gray-cheeked Thrush | 7373 |






### Top Species for Kansas  (KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2114 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 43167 |
| 0.1426 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2429 |
| 0.0897 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 710 |
| 0.0768 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 36284 |
| 0.0677 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 26149 |
| 0.0592 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 22554 |
| 0.0561 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 8401 |
| 0.0507 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 667 |
| 0.0505 | [Charadrius nivosus](https://en.wikipedia.org/wiki/Charadrius_nivosus) | Snowy Plover | 5380 |
| 0.0459 | [Calidris bairdii](https://en.wikipedia.org/wiki/Calidris_bairdii) | Baird's Sandpiper | 11235 |






### Top Species for Kentucky  (KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0278 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 5928 |
| 0.0170 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0169 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 8107 |
| 0.0162 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 959 |
| 0.0158 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 11719 |
| 0.0157 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 18248 |
| 0.0151 | [Piranga sp.](https://en.wikipedia.org/wiki/Piranga) |  | 69 |
| 0.0144 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 6725 |
| 0.0136 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat | 10504 |
| 0.0133 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 6812 |






### Top Species for Louisiana  (LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1090 | [Quiscalus sp.](https://en.wikipedia.org/wiki/Quiscalus) |  | 1442 |
| 0.1051 | [Rallus elegans](https://en.wikipedia.org/wiki/Rallus_elegans) | King Rail | 6306 |
| 0.0845 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 27044 |
| 0.0842 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 3190 |
| 0.0793 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) | Bridled tern | 677 |
| 0.0722 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 3553 |
| 0.0664 | [Coturnicops noveboracensis](https://en.wikipedia.org/wiki/Coturnicops_noveboracensis) | Yellow Rail | 942 |
| 0.0636 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern | 6719 |
| 0.0627 | [Dendrocygna bicolor](https://en.wikipedia.org/wiki/Dendrocygna_bicolor) | Fulvous Whistling-Duck | 4135 |
| 0.0534 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 5500 |






### Top Species for Massachusetts  (MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5509 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel | 1036 |
| 0.4408 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx shearwater | 9833 |
| 0.3481 | [Puffinus sp. (black-and-white shearwater sp.)](https://en.wikipedia.org/wiki/Puffinus) |  | 499 |
| 0.3437 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) | Great shearwater | 19121 |
| 0.3286 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 14117 |
| 0.3147 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater | 16342 |
| 0.2646 | [Setophaga sp.](https://en.wikipedia.org/wiki/Setophaga) |  | 745 |
| 0.2579 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel | 17049 |
| 0.2391 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing | 553 |
| 0.2343 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 14108 |






### Top Species for Maryland  (MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1329 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 53171 |
| 0.1034 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 61388 |
| 0.0811 | [Hydrobates castro](https://en.wikipedia.org/wiki/Hydrobates_castro) | Band-rumped storm-petrel | 1059 |
| 0.0733 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 203375 |
| 0.0656 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) | Audubon's shearwater | 1684 |
| 0.0634 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0592 | [Cygnus columbianus](https://en.wikipedia.org/wiki/Cygnus_columbianus) | Tundra Swan | 36221 |
| 0.0540 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 29442 |
| 0.0482 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 543555 |
| 0.0474 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 6635 |






### Top Species for Maine  (ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5279 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) | Atlantic puffin | 17498 |
| 0.4030 | [Turdus iliacus](https://en.wikipedia.org/wiki/Turdus_iliacus)∀ | Redwing | 600 |
| 0.3474 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black guillemot | 58921 |
| 0.3373 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta) | Little egret | 1008 |
| 0.3335 | [Stercorarius skua](https://en.wikipedia.org/wiki/Stercorarius_skua) | Great skua | 525 |
| 0.3306 | [Phaethon aethereus](https://en.wikipedia.org/wiki/Phaethon_aethereus) | Red-billed tropicbird | 1364 |
| 0.2529 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 10380 |
| 0.2128 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 126024 |
| 0.2097 | [Hydrobates leucorhous](https://en.wikipedia.org/wiki/Hydrobates_leucorhous) | Leach's storm-petrel | 7558 |
| 0.1498 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill | 14447 |






### Top Species for Michigan  (MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.6333 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 7644 |
| 0.1605 | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  | 3920 |
| 0.1266 | [Aythya sp.](https://en.wikipedia.org/wiki/Aythya) |  | 2875 |
| 0.1213 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan | 165631 |
| 0.0986 | [Larus sp. (white-winged gull sp.)](https://en.wikipedia.org/wiki/Larus)† |  | 232 |
| 0.0984 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 176499 |
| 0.0833 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 826 |
| 0.0607 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 48981 |
| 0.0570 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147717 |
| 0.0570 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow | 125158 |






### Top Species for Minnesota  (MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1150 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 69864 |
| 0.1064 | [Pagophila eburnea](https://en.wikipedia.org/wiki/Pagophila_eburnea) | Ivory gull | 459 |
| 0.0987 | [Aegolius funereus](https://en.wikipedia.org/wiki/Aegolius_funereus) | Boreal owl | 1218 |
| 0.0882 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 22221 |
| 0.0878 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 13045 |
| 0.0877 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 1663 |
| 0.0835 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker | 5030 |
| 0.0758 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 3799 |
| 0.0752 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34266 |
| 0.0582 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 46603 |






### Top Species for Missouri  (MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5093 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus)* | Eurasian Tree Sparrow | 26402 |
| 0.0933 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 18709 |
| 0.0678 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 34191 |
| 0.0507 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 21081 |
| 0.0480 | [Poecile sp.](https://en.wikipedia.org/wiki/Poecile)† | western chickadee | 1731 |
| 0.0476 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 21483 |
| 0.0456 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 53929 |
| 0.0431 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 4090 |
| 0.0383 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 43217 |
| 0.0366 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 9640 |






### Top Species for Mississippi  (MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0354 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 1697 |
| 0.0305 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern | 3142 |
| 0.0278 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 7469 |
| 0.0234 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer | 8333 |
| 0.0227 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 897 |
| 0.0216 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 2211 |
| 0.0196 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 8279 |
| 0.0196 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern | 14849 |
| 0.0175 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican | 22486 |
| 0.0175 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 744 |






### Top Species for Montana  (MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1975 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 2510 |
| 0.1831 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 3501 |
| 0.1574 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 6066 |
| 0.1315 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 24361 |
| 0.1289 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 7149 |
| 0.1211 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 2920 |
| 0.1159 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 14066 |
| 0.1130 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1377 |
| 0.0970 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 4325 |
| 0.0938 | [Sphyrapicus nuchalis](https://en.wikipedia.org/wiki/Sphyrapicus_nuchalis) | Red-naped Sapsucker | 16678 |






### Top Species for North Carolina  (NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5993 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) | Black-capped petrel | 6000 |
| 0.3751 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) | Audubon's shearwater | 7090 |
| 0.3449 | [Hydrobates castro](https://en.wikipedia.org/wiki/Hydrobates_castro) | Band-rumped storm-petrel | 3538 |
| 0.2607 | [Puffinus sp. (black-and-white shearwater sp.)](https://en.wikipedia.org/wiki/Puffinus) |  | 369 |
| 0.2548 | [Onychoprion anaethetus](https://en.wikipedia.org/wiki/Onychoprion_anaethetus) | Bridled tern | 2104 |
| 0.2431 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's shearwater | 12415 |
| 0.2355 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 154113 |
| 0.1226 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) | Wilson's storm-petrel | 8420 |
| 0.1215 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus)∀ | White-winged Tern | 161 |
| 0.1116 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 4514 |






### Top Species for North Dakota  (ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1591 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 1986 |
| 0.1474 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 6240 |
| 0.1259 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 4748 |
| 0.0652 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 3576 |
| 0.0573 | [Anthus spragueii](https://en.wikipedia.org/wiki/Anthus_spragueii) | Sprague's Pipit | 1636 |
| 0.0513 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 7042 |
| 0.0483 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 19291 |
| 0.0389 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 14372 |
| 0.0352 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 24049 |
| 0.0335 | [Ammospiza leconteii](https://en.wikipedia.org/wiki/Ammospiza_leconteii) | LeConte's Sparrow | 2114 |






### Top Species for Nebraska  (NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1785 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2934 |
| 0.0816 | [Grus grus](https://en.wikipedia.org/wiki/Grus_grus)∀ | Common crane | 147 |
| 0.0642 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 13378 |
| 0.0422 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 19658 |
| 0.0365 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5257 |
| 0.0319 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 42141 |
| 0.0268 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 1279 |
| 0.0263 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 10081 |
| 0.0257 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 18728 |
| 0.0238 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting | 2834 |






### Top Species for New Hampshire  (NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2372 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3457 |
| 0.0331 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta) | Little egret | 115 |
| 0.0328 | [Empidonax flaviventris](https://en.wikipedia.org/wiki/Empidonax_flaviventris) | Yellow-bellied Flycatcher | 5766 |
| 0.0320 | [Turdus iliacus](https://en.wikipedia.org/wiki/Turdus_iliacus)∀ | Redwing | 56 |
| 0.0305 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper | 2912 |
| 0.0270 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 1322 |
| 0.0254 | [Buteo platypterus](https://en.wikipedia.org/wiki/Buteo_platypterus) | Broad-winged Hawk | 19622 |
| 0.0251 | [Alle alle](https://en.wikipedia.org/wiki/Alle_alle) | Dovekie | 546 |
| 0.0242 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker | 1571 |
| 0.0226 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 4048 |






### Top Species for New Jersey  (NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2621 | [Tringa nebularia](https://en.wikipedia.org/wiki/Tringa_nebularia) | Common greenshank | 325 |
| 0.2425 | [Vanellus vanellus](https://en.wikipedia.org/wiki/Vanellus_vanellus)∀ | Northern Lapwing | 552 |
| 0.2162 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 21461 |
| 0.1839 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) | Curlew sandpiper | 950 |
| 0.1690 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 68430 |
| 0.1521 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 73643 |
| 0.1415 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper | 13276 |
| 0.1387 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 8853 |
| 0.1270 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 37087 |
| 0.1089 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan | 149892 |






### Top Species for New Mexico  (NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3686 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse | 31338 |
| 0.2964 | [Corvus sp. (raven sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 13606 |
| 0.2709 | [Corvus cryptoleucus](https://en.wikipedia.org/wiki/Corvus_cryptoleucus) | Chihuahuan Raven | 26986 |
| 0.2584 | [Callipepla squamata](https://en.wikipedia.org/wiki/Callipepla_squamata) | Scaled Quail | 19220 |
| 0.2430 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 3183 |
| 0.2299 | [Leucosticte sp.](https://en.wikipedia.org/wiki/Leucosticte) |  | 606 |
| 0.2183 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch | 2965 |
| 0.2172 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 13673 |
| 0.2170 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee | 66423 |
| 0.2142 | [Leiothlypis virginiae](https://en.wikipedia.org/wiki/Leiothlypis_virginiae) | Virginia's Warbler | 15696 |






### Top Species for Nevada  (NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1529 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 5068 |
| 0.1357 | [Toxostoma lecontei](https://en.wikipedia.org/wiki/Toxostoma_lecontei) | LeConte's Thrasher | 901 |
| 0.1303 | [Toxostoma crissale](https://en.wikipedia.org/wiki/Toxostoma_crissale) | Crissal Thrasher | 8275 |
| 0.0938 | [Dryobates albolarvatus](https://en.wikipedia.org/wiki/Dryobates_albolarvatus) | White-headed Woodpecker | 2560 |
| 0.0880 | [Polioptila melanura](https://en.wikipedia.org/wiki/Polioptila_melanura) | Black-tailed Gnatcatcher | 14326 |
| 0.0866 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 5444 |
| 0.0859 | [Calypte costae](https://en.wikipedia.org/wiki/Calypte_costae) | Costa's Hummingbird | 10397 |
| 0.0694 | [Empidonax wrightii](https://en.wikipedia.org/wiki/Empidonax_wrightii) | Gray Flycatcher | 6588 |
| 0.0662 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 6385 |
| 0.0628 | [Spizella breweri](https://en.wikipedia.org/wiki/Spizella_breweri) | Brewer's Sparrow | 13506 |






### Top Species for New York  (NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2969 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 1971 |
| 0.1862 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 98677 |
| 0.1554 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 2999 |
| 0.1138 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 8990 |
| 0.1048 | [Pelagodroma marina](https://en.wikipedia.org/wiki/Pelagodroma_marina) | White-faced storm-petrel | 286 |
| 0.1002 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 54113 |
| 0.0998 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor)* | Mute Swan | 169881 |
| 0.0974 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler | 56745 |
| 0.0972 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 289559 |
| 0.0933 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis)∀ | Barnacle Goose | 1257 |






### Top Species for Ohio  (OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1040 | [Fringilla montifringilla](https://en.wikipedia.org/wiki/Fringilla_montifringilla)∀ | Brambling | 632 |
| 0.1035 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 152 |
| 0.0959 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 1496 |
| 0.0827 | [Setophaga castanea](https://en.wikipedia.org/wiki/Setophaga_castanea) | Bay-breasted Warbler | 41766 |
| 0.0816 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 14331 |
| 0.0787 | [Cygnus sp.](https://en.wikipedia.org/wiki/Swan) |  | 2309 |
| 0.0781 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 59931 |
| 0.0770 | [Calidris ferruginea](https://en.wikipedia.org/wiki/Calidris_ferruginea) | Curlew sandpiper | 496 |
| 0.0697 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 7628 |
| 0.0683 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 36537 |






### Top Species for Oklahoma  (OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0864 | [Vireo atricapilla](https://en.wikipedia.org/wiki/Vireo_atricapilla) | Black-capped Vireo | 1693 |
| 0.0848 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 17544 |
| 0.0788 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher | 37937 |
| 0.0743 | [Calcarius pictus](https://en.wikipedia.org/wiki/Calcarius_pictus) | Smith's Longspur | 889 |
| 0.0714 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 21873 |
| 0.0516 | [Quiscalus sp.](https://en.wikipedia.org/wiki/Quiscalus) |  | 685 |
| 0.0358 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 13547 |
| 0.0327 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 600 |
| 0.0311 | [Nomonyx dominicus](https://en.wikipedia.org/wiki/Nomonyx_dominicus)∀ | Masked Duck | 46 |
| 0.0295 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 14500 |






### Top Species for Oregon  (OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5643 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |
| 0.4317 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail | 8746 |
| 0.3639 | [Setophaga occidentalis](https://en.wikipedia.org/wiki/Setophaga_occidentalis) | Hermit Warbler | 27518 |
| 0.3604 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit | 38911 |
| 0.3524 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 93667 |
| 0.3464 | [Chaetura vauxi](https://en.wikipedia.org/wiki/Chaetura_vauxi) | Vaux's Swift | 69677 |
| 0.3176 | [Sphyrapicus ruber](https://en.wikipedia.org/wiki/Sphyrapicus_ruber) | Red-breasted Sapsucker | 70159 |
| 0.3159 | [Anser serrirostris](https://en.wikipedia.org/wiki/Anser_serrirostris)∀ | Tundra bean-goose | 719 |
| 0.3002 | [Dryobates albolarvatus](https://en.wikipedia.org/wiki/Dryobates_albolarvatus) | White-headed Woodpecker | 8575 |
| 0.2972 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) | Black-footed albatross | 7426 |






### Top Species for Pennsylvania  (PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3117 | [Anser serrirostris](https://en.wikipedia.org/wiki/Anser_serrirostris)∀ | Tundra bean-goose | 733 |
| 0.2422 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus)∀ | White-winged Tern | 317 |
| 0.1601 | [Poecile sp.](https://en.wikipedia.org/wiki/Poecile)† | western chickadee | 5671 |
| 0.0880 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 171036 |
| 0.0651 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 34112 |
| 0.0624 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 115306 |
| 0.0534 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 46535 |
| 0.0469 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 282381 |
| 0.0455 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 29950 |
| 0.0436 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 620147 |






### Top Species for Rhode Island  (RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1120 | [Calidris minuta](https://en.wikipedia.org/wiki/Calidris_minuta)∀ | Little stint | 179 |
| 0.0584 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 8422 |
| 0.0532 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 2966 |
| 0.0496 | [Calidris sp.](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 380 |
| 0.0496 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 58 |
| 0.0457 | [Tringa glareola](https://en.wikipedia.org/wiki/Tringa_glareola) | Wood sandpiper | 154 |
| 0.0361 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 1524 |
| 0.0337 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper | 2852 |
| 0.0291 | [Calidris ruficollis](https://en.wikipedia.org/wiki/Calidris_ruficollis) | Red-necked Stint | 116 |
| 0.0288 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 17732 |






### Top Species for South Carolina  (SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1377 | [Dryobates borealis](https://en.wikipedia.org/wiki/Dryobates_borealis) | Red-cockaded Woodpecker | 5091 |
| 0.1130 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 29691 |
| 0.1023 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 68558 |
| 0.1017 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 38067 |
| 0.0871 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 40234 |
| 0.0668 | [Peucaea aestivalis](https://en.wikipedia.org/wiki/Peucaea_aestivalis) | Bachman's Sparrow | 2776 |
| 0.0598 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 3114 |
| 0.0587 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 20288 |
| 0.0552 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 52941 |
| 0.0538 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron | 57484 |






### Top Species for South Dakota  (SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0591 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 2538 |
| 0.0413 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 697 |
| 0.0381 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5213 |
| 0.0314 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 1232 |
| 0.0312 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting | 3391 |
| 0.0222 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0219 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant | 15094 |
| 0.0187 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 4057 |
| 0.0181 | [Athene cunicularia](https://en.wikipedia.org/wiki/Athene_cunicularia) | Burrowing Owl | 1976 |
| 0.0168 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 6443 |






### Top Species for Tennessee  (TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0604 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 12863 |
| 0.0424 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 2385 |
| 0.0408 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0362 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 161073 |
| 0.0352 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 16980 |
| 0.0329 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 22961 |
| 0.0318 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 83481 |
| 0.0312 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 37115 |
| 0.0295 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat | 22678 |
| 0.0274 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 181101 |






### Top Species for Texas  (TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.9187 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse | 365712 |
| 0.9089 | [Toxostoma longirostre](https://en.wikipedia.org/wiki/Toxostoma_longirostre) | Long-billed Thrasher | 118995 |
| 0.9033 | [Setophaga chrysoparia](https://en.wikipedia.org/wiki/Setophaga_chrysoparia) | Golden-cheeked Warbler | 21281 |
| 0.8345 | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk | 54492 |
| 0.7677 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow | 82550 |
| 0.7475 | [Leiothlypis crissalis](https://en.wikipedia.org/wiki/Leiothlypis_crissalis) | Colima Warbler | 3032 |
| 0.7429 | [Tyrannus couchii](https://en.wikipedia.org/wiki/Tyrannus_couchii) | Couch's Kingbird | 110055 |
| 0.7371 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay | 150450 |
| 0.7106 | [Psittacara holochlorus](https://en.wikipedia.org/wiki/Psittacara_holochlorus)∀ | Green parakeet | 15912 |
| 0.7079 | [Amazona oratrix](https://en.wikipedia.org/wiki/Amazona_oratrix)∀ | Yellow-headed parrot | 2312 |






### Top Species for Utah  (UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1930 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar | 7064 |
| 0.1868 | [Psiloscops flammeolus](https://en.wikipedia.org/wiki/Psiloscops_flammeolus) | Flammulated Owl | 2119 |
| 0.1671 | [Gymnogyps californianus](https://en.wikipedia.org/wiki/Gymnogyps_californianus) | California Condor | 1515 |
| 0.1604 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 2119 |
| 0.1447 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe | 15670 |
| 0.1433 | [Vireo vicinior](https://en.wikipedia.org/wiki/Vireo_vicinior) | Gray Vireo | 2355 |
| 0.1345 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 53017 |
| 0.1244 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay | 7974 |
| 0.1187 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 1455 |
| 0.1137 | [Aix galericulata](https://en.wikipedia.org/wiki/Aix_galericulata)* | Mandarin Duck | 335 |






### Top Species for Virginia  (VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1371 | [Limosa limosa](https://en.wikipedia.org/wiki/Limosa_limosa) | Black-tailed godwit | 245 |
| 0.1049 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 43910 |
| 0.0883 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 54363 |
| 0.0739 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0581 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 173005 |
| 0.0570 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler | 18144 |
| 0.0559 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0558 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 93 |
| 0.0538 | [Setophaga sp.](https://en.wikipedia.org/wiki/Setophaga) |  | 206 |
| 0.0535 | [Rallus elegans](https://en.wikipedia.org/wiki/Rallus_elegans) | King Rail | 4512 |






### Top Species for Vermont  (VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2149 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3176 |
| 0.0776 | [Larus crassirostris](https://en.wikipedia.org/wiki/Larus_crassirostris)∀ | Black-tailed Gull | 96 |
| 0.0409 | [Spatula querquedula](https://en.wikipedia.org/wiki/Spatula_querquedula)∀ | Garganey | 90 |
| 0.0333 | [Empidonax alnorum](https://en.wikipedia.org/wiki/Empidonax_alnorum) | Alder Flycatcher | 15915 |
| 0.0319 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler | 44511 |
| 0.0297 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus)† | Ruffed Grouse | 16963 |
| 0.0294 | [Troglodytes hiemalis](https://en.wikipedia.org/wiki/Troglodytes_hiemalis) | Winter Wren | 27544 |
| 0.0292 | [Picoides arcticus](https://en.wikipedia.org/wiki/Picoides_arcticus) | Black-backed Woodpecker | 1953 |
| 0.0292 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 35063 |
| 0.0254 | [Setophaga caerulescens](https://en.wikipedia.org/wiki/Setophaga_caerulescens) | Black-throated Blue Warbler | 25660 |






### Top Species for Washington  (WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.5008 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros auklet | 56517 |
| 0.4906 | [Prunella montanella](https://en.wikipedia.org/wiki/Prunella_montanella)∀ | Siberian accentor | 589 |
| 0.4771 | [Zonotrichia sp.](https://en.wikipedia.org/wiki/Zonotrichia) |  | 754 |
| 0.4345 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot | 92260 |
| 0.3129 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 268543 |
| 0.3077 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull | 281727 |
| 0.3032 | [Ardenna carneipes](https://en.wikipedia.org/wiki/Ardenna_carneipes) | Flesh-footed shearwater | 935 |
| 0.2995 | [Phoebastria nigripes](https://en.wikipedia.org/wiki/Phoebastria_nigripes) | Black-footed albatross | 7607 |
| 0.2993 | [Hydrobates furcatus](https://en.wikipedia.org/wiki/Hydrobates_furcatus) | Fork-tailed storm-petrel | 7115 |
| 0.2993 | [Troglodytes pacificus](https://en.wikipedia.org/wiki/Troglodytes_pacificus) | Pacific Wren | 152848 |






### Top Species for Wisconsin  (WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1848 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 3424 |
| 0.1415 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 231517 |
| 0.1235 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 19108 |
| 0.1096 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 29448 |
| 0.1071 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 755 |
| 0.0860 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 8396 |
| 0.0797 | [Geothlypis philadelphia](https://en.wikipedia.org/wiki/Geothlypis_philadelphia) | Mourning Warbler | 21105 |
| 0.0636 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34542 |
| 0.0630 | [Chlidonias leucopterus](https://en.wikipedia.org/wiki/Chlidonias_leucopterus)∀ | White-winged Tern | 103 |
| 0.0600 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147827 |






### Top Species for West Virginia  (WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0249 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 3557 |
| 0.0157 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler | 850 |
| 0.0148 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 6640 |
| 0.0145 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 9288 |
| 0.0134 | [Anas bahamensis](https://en.wikipedia.org/wiki/Anas_bahamensis)∀ | White-cheeked Pintail | 18 |
| 0.0128 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 19032 |
| 0.0128 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler | 3533 |
| 0.0125 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 8854 |
| 0.0116 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 51061 |
| 0.0112 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 2661 |






### Top Species for Wyoming  (WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1964 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 2281 |
| 0.1465 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 1876 |
| 0.1183 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 2228 |
| 0.0956 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 2239 |
| 0.0773 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 14068 |
| 0.0612 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 5825 |
| 0.0601 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 21085 |
| 0.0525 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 1788 |
| 0.0524 | [Leucosticte tephrocotis](https://en.wikipedia.org/wiki/Leucosticte_tephrocotis) | Gray-crowned Rosy-Finch | 2596 |
| 0.0499 | [Leucosticte sp.](https://en.wikipedia.org/wiki/Leucosticte) |  | 133 |







