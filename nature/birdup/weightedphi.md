---
title: "Bird Scores - Weighted Phi"
parent: New State Birds
grand_parent: Science and Nature
has_children: false
math: katex
---


This BIRDUP scoring system uses a modified version of the [phi coefficient](phi),
but with a parameter tweaked to give slightly more weight to the uniqueness of a bird to a state.

This scoring system uses observation records from the eBird database[^ebirdcitation].

For top-scoring birds, the standard phi coefficient can be written as 

$$\phi = {\Delta p}^{0.5}\times{J}^{0.5}$$

where $J$ is the [informedness](informedness) and $\Delta p$ is the [markedness](markedness).

This weighted variant tweaks the formula to 

$$\phi_w = {\Delta p}^{0.65}\times{J}^{0.35}$$

Why these exponents? There's no real mathematical justification.
I'm using these tools for a qualitative purpose for which they were not designed.
I just fiddled with the formula until I got a list of state birds that *felt right*.
But as mentioned above, you can interpret this formula as the correlation between state and bird, with additional weight placed on a term related to the uniqueness of a bird to a state.


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
| US-AK | 0.1705 | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet |
| US-AL | 0.0170 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| US-AR | 0.0099 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| US-AZ | 0.1867 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| US-CA | 0.1098 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| US-CO | 0.0953 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| US-CT | 0.0140 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| US-DC | 0.0082 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| US-DE | 0.0147 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| US-FL | 0.1734 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| US-GA | 0.0261 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| US-HI | 0.2727 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| US-IA | 0.0055 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| US-ID | 0.0173 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| US-IL | 0.0286 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| US-IN | 0.0115 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| US-KS | 0.0304 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| US-KY | 0.0069 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| US-LA | 0.0274 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| US-MA | 0.0367 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter |
| US-MD | 0.0220 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| US-ME | 0.0760 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| US-MI | 0.0370 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| US-MN | 0.0153 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| US-MO | 0.0159 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| US-MS | 0.0119 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| US-MT | 0.0403 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| US-NC | 0.0360 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  |
| US-ND | 0.0314 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| US-NE | 0.0152 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| US-NH | 0.0103 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch |
| US-NJ | 0.0312 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| US-NM | 0.0462 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| US-NV | 0.0330 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| US-NY | 0.0261 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| US-OH | 0.0158 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| US-OK | 0.0305 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| US-OR | 0.1090 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| US-PA | 0.0312 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| US-RI | 0.0225 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| US-SC | 0.0303 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| US-SD | 0.0164 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| US-TN | 0.0183 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| US-TX | 0.1250 | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| US-UT | 0.0301 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| US-VA | 0.0391 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| US-VT | 0.0151 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| US-WA | 0.0764 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet |
| US-WI | 0.0558 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| US-WV | 0.0083 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| US-WY | 0.0321 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |





### Top Genera for Alaska (US-AK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1705 | [Aethia](https://en.wikipedia.org/wiki/Aethia) | Auklet | 31286 | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet |
| 0.1290 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 48084 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned Puffin |
| 0.1189 | [Rissa](https://en.wikipedia.org/wiki/Kittiwake) | Kittiwake | 60795 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake |
| 0.1101 | [Motacilla](https://en.wikipedia.org/wiki/Motacilla) |  | 11750 | [Motacilla tschutschensis](https://en.wikipedia.org/wiki/Motacilla_tschutschensis) | Eastern Yellow Wagtail |
| 0.0987 | [Polysticta](https://en.wikipedia.org/wiki/Polysticta) |  | 7277 | [Polysticta stelleri](https://en.wikipedia.org/wiki/Polysticta_stelleri) | Steller's Eider |
| 0.0933 | [Phylloscopus](https://en.wikipedia.org/wiki/Phylloscopus) |  | 6210 | [Phylloscopus borealis](https://en.wikipedia.org/wiki/Phylloscopus_borealis) | Arctic Warbler |
| 0.0923 | [Lagopus](https://en.wikipedia.org/wiki/Lagopus)‡ |  | 20473 | [Lagopus lagopus](https://en.wikipedia.org/wiki/Lagopus_lagopus) | Willow Ptarmigan |
| 0.0858 | [Brachyramphus](https://en.wikipedia.org/wiki/Brachyramphus) |  | 32064 | [Brachyramphus brevirostris](https://en.wikipedia.org/wiki/Brachyramphus_brevirostris) | Kittlitz's Murrelet |
| 0.0850 | [Stercorarius](https://en.wikipedia.org/wiki/Stercorarius) |  | 52502 | [Stercorarius longicaudus](https://en.wikipedia.org/wiki/Stercorarius_longicaudus) | Long-tailed Jaeger |
| 0.0774 | [Luscinia](https://en.wikipedia.org/wiki/Luscinia) |  | 3311 | [Luscinia svecica](https://en.wikipedia.org/wiki/Luscinia_svecica) | Bluethroat |






### Top Genera for Alabama (US-AL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0170 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 130529 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0141 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 127076 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0129 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 24522 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0122 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 59435 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0121 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 2905 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0106 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 84368 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0096 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 39243 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0094 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 60847 | [Passerina caerulea](https://en.wikipedia.org/wiki/Passerina_caerulea) | Blue Grosbeak |
| 0.0092 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 9976 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0090 | [Grus](https://en.wikipedia.org/wiki/Grus_(genus)) | Crane | 1504 | [Grus americana](https://en.wikipedia.org/wiki/Grus_americana) | Whooping Crane |






### Top Genera for Arkansas (US-AR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0135 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 10710 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0103 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 91280 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0099 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 55044 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0095 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 10491 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0088 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 93388 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0076 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 68963 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0074 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 17013 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0073 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10221 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0070 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 7000 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0070 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 57596 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |






### Top Genera for Arizona (US-AZ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1867 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 386191 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.1552 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 200508 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.1521 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 388898 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee |
| 0.1383 | [Cynanthus](https://en.wikipedia.org/wiki/Cynanthus) | Hummingbird | 169527 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed Hummingbird |
| 0.1282 | [Campylorhynchus](https://en.wikipedia.org/wiki/Campylorhynchus)‡ |  | 200611 | [Campylorhynchus brunneicapillus](https://en.wikipedia.org/wiki/Campylorhynchus_brunneicapillus) | Cactus Wren |
| 0.1082 | [Pyrocephalus](https://en.wikipedia.org/wiki/Pyrocephalus) |  | 194003 | [Pyrocephalus rubinus](https://en.wikipedia.org/wiki/Pyrocephalus_rubinus) | Vermilion Flycatcher |
| 0.1072 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 137441 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.1057 | [Eugenes](https://en.wikipedia.org/wiki/Eugenes) |  | 59354 | [Eugenes fulgens](https://en.wikipedia.org/wiki/Eugenes_fulgens) | Rivoli's Hummingbird |
| 0.0966 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 296630 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0961 | [Myioborus](https://en.wikipedia.org/wiki/Myioborus) |  | 73445 | [Myioborus pictus](https://en.wikipedia.org/wiki/Myioborus_pictus) | Painted Redstart |






### Top Genera for California (US-CA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1098 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 57649 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.0648 | [Elanus](https://en.wikipedia.org/wiki/Elanus) |  | 40693 | [Elanus leucurus](https://en.wikipedia.org/wiki/Elanus_leucurus) | White-tailed Kite |
| 0.0629 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 129054 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| 0.0544 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 112390 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0533 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 153459 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0523 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 176961 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0483 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) |  | 8665 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.0397 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 70336 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe |
| 0.0380 | [Numenius](https://en.wikipedia.org/wiki/Numenius) |  | 56560 | [Numenius americanus](https://en.wikipedia.org/wiki/Numenius_americanus) | Long-billed Curlew |
| 0.0344 | [Euplectes](https://en.wikipedia.org/wiki/Euplectes)* | Bishop | 1315 | [Euplectes franciscanus](https://en.wikipedia.org/wiki/Euplectes_franciscanus) | Northern Red Bishop |






### Top Genera for Colorado (US-CO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0953 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 387306 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0625 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 210475 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0487 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 292668 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0478 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 73348 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0428 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)‡ | Lark Bunting | 28847 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0423 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 92411 | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| 0.0391 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 21537 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch |
| 0.0338 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 241188 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0307 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 31182 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0302 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 24773 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |






### Top Genera for Connecticut (US-CT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0140 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 240563 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0122 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 162362 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0115 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 22502 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0104 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 47578 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0100 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 21206 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0098 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 64233 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0091 | [Myiopsitta](https://en.wikipedia.org/wiki/Myiopsitta)* |  | 6889 | [Myiopsitta monachus](https://en.wikipedia.org/wiki/Myiopsitta_monachus) | Monk Parakeet |
| 0.0087 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 7306 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0086 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 339172 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0074 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 9088 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |






### Top Genera for District of Columbia (US-DC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0082 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 24475 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0060 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 41998 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0047 | [Sturnus](https://en.wikipedia.org/wiki/Sturnus)* | Starling | 53975 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris) | European Starling |
| 0.0047 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 42950 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0041 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 30486 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0035 | [Polioptila](https://en.wikipedia.org/wiki/Polioptila) | Gnatcatcher | 16764 | [Polioptila caerulea](https://en.wikipedia.org/wiki/Polioptila_caerulea) | Blue-gray Gnatcatcher |
| 0.0034 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 25165 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0032 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)‡ | Wood Thrush | 7815 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0031 | [Turdus](https://en.wikipedia.org/wiki/Turdus)† | Robin | 62170 | [Turdus migratorius](https://en.wikipedia.org/wiki/Turdus_migratorius) | American Robin |
| 0.0030 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 57641 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Genera for Delaware (US-DE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0147 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 53108 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0130 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 42296 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0124 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 10452 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0124 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 101378 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper |
| 0.0119 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 16285 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0104 | [Limnodromus](https://en.wikipedia.org/wiki/Limnodromus) |  | 21701 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher |
| 0.0095 | [Tringa](https://en.wikipedia.org/wiki/Tringa) | Tattlers | 71586 | [Tringa melanoleuca](https://en.wikipedia.org/wiki/Tringa_melanoleuca) | Greater Yellowlegs |
| 0.0090 | [Progne](https://en.wikipedia.org/wiki/Progne) |  | 26358 | [Progne subis](https://en.wikipedia.org/wiki/Progne_subis) | Purple Martin |
| 0.0081 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 14755 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |
| 0.0076 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 22379 | [Anser caerulescens](https://en.wikipedia.org/wiki/Anser_caerulescens) | Snow Goose |






### Top Genera for Florida (US-FL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1734 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 553383 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.1734 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 748541 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.1594 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 1584817 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron |
| 0.1438 | [Aramus](https://en.wikipedia.org/wiki/Aramus) |  | 184399 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin |
| 0.1373 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 284639 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.1101 | [Gallinula](https://en.wikipedia.org/wiki/Gallinula) |  | 389658 | [Gallinula galeata](https://en.wikipedia.org/wiki/Gallinula_galeata) | Common Gallinule |
| 0.1041 | [Elanoides](https://en.wikipedia.org/wiki/Elanoides) |  | 111055 | [Elanoides forficatus](https://en.wikipedia.org/wiki/Elanoides_forficatus) | Swallow-tailed Kite |
| 0.0989 | [Porphyrio](https://en.wikipedia.org/wiki/Porphyrio) |  | 107853 | [Porphyrio martinica](https://en.wikipedia.org/wiki/Porphyrio_martinica) | Purple Gallinule |
| 0.0934 | [Aratinga](https://en.wikipedia.org/wiki/Aratinga)* | Conure | 47057 | [Aratinga nenday](https://en.wikipedia.org/wiki/Aratinga_nenday) | Nanday Parakeet |
| 0.0873 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 314435 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |






### Top Genera for Georgia (US-GA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0318 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 395603 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0261 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)‡ | Thrasher | 179633 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0229 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 288903 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0228 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 264143 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0222 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 249060 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0214 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 345328 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0160 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 113127 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0159 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 377667 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0157 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 28067 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0146 | [Sayornis](https://en.wikipedia.org/wiki/Sayornis) | Phoebe | 208616 | [Sayornis phoebe](https://en.wikipedia.org/wiki/Sayornis_phoebe) | Eastern Phoebe |






### Top Genera for Hawaii (US-HI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.3662 | [Zosterops](https://en.wikipedia.org/wiki/Zosterops)* | White-Eyes | 82840 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus) |  |
| 0.3591 | [Geopelia](https://en.wikipedia.org/wiki/Geopelia)* |  | 78346 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata) |  |
| 0.3464 | [Acridotheres](https://en.wikipedia.org/wiki/Acridotheres)* | Myna | 89440 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis) | Common Myna |
| 0.3207 | [Paroaria](https://en.wikipedia.org/wiki/Paroaria)* |  | 56710 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata) |  |
| 0.2727 | [Himatione](https://en.wikipedia.org/wiki/Himatione) |  | 35689 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane |
| 0.2685 | [Chlorodrepanis](https://en.wikipedia.org/wiki/Chlorodrepanis) |  | 34136 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  |
| 0.2428 | [Estrilda](https://en.wikipedia.org/wiki/Estrilda) |  | 25798 | [Estrilda astrild](https://en.wikipedia.org/wiki/Estrilda_astrild) |  |
| 0.2280 | [Sicalis](https://en.wikipedia.org/wiki/Sicalis) |  | 23701 | [Sicalis flaveola](https://en.wikipedia.org/wiki/Sicalis_flaveola) |  |
| 0.2280 | [Pycnonotus](https://en.wikipedia.org/wiki/Pycnonotus) |  | 33210 | [Pycnonotus cafer](https://en.wikipedia.org/wiki/Pycnonotus_cafer) |  |
| 0.2234 | [Padda](https://en.wikipedia.org/wiki/Padda) |  | 20197 | [Padda oryzivora](https://en.wikipedia.org/wiki/Padda_oryzivora) |  |






### Top Genera for Iowa (US-IA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0161 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 21293 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0158 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 15850 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0061 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 97621 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0057 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 76639 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| 0.0055 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 45929 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0055 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 42291 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0050 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 1961 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0047 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 40013 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0046 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 9534 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0046 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 15618 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |






### Top Genera for Idaho (US-ID)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0476 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 118106 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0298 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 53404 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica) | California Quail |
| 0.0179 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 3634 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.0173 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 23444 | [Aechmophorus occidentalis](https://en.wikipedia.org/wiki/Aechmophorus_occidentalis) | Western Grebe |
| 0.0169 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 65286 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0162 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6303 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0154 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 38584 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0141 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18567 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0134 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 1305 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0127 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3493 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |






### Top Genera for Illinois (US-IL)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0286 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 18756 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0215 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 46626 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0170 | [Carduelis](https://en.wikipedia.org/wiki/Carduelis)* | Goldfinch | 1798 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis) | European Goldfinch |
| 0.0168 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163030 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0166 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 434206 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| 0.0162 | [Hydroprogne](https://en.wikipedia.org/wiki/Hydroprogne) |  | 70704 | [Hydroprogne caspia](https://en.wikipedia.org/wiki/Hydroprogne_caspia) | Caspian Tern |
| 0.0155 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 94643 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0120 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 520240 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |
| 0.0116 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 637278 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0115 | [Molothrus](https://en.wikipedia.org/wiki/Molothrus) | Cowbird | 235794 | [Molothrus ater](https://en.wikipedia.org/wiki/Molothrus_ater) | Brown-headed Cowbird |






### Top Genera for Indiana (US-IN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0141 | [Centronyx](https://en.wikipedia.org/wiki/Centronyx) | Sparrow | 7607 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| 0.0122 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 224909 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0115 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 282027 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0094 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 350530 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0093 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 15774 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0082 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 83946 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0081 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 42933 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0080 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 16357 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0073 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 326501 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |
| 0.0072 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 12791 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |






### Top Genera for Kansas (US-KS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0304 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 36284 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0212 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 22554 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0194 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 92201 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0150 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 24003 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0147 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 8401 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0144 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 14481 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0119 | [Eremophila](https://en.wikipedia.org/wiki/Eremophila) |  | 34440 | [Eremophila alpestris](https://en.wikipedia.org/wiki/Eremophila_alpestris) | Horned Lark |
| 0.0115 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 12774 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0102 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 88177 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |
| 0.0101 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 86342 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird |






### Top Genera for Kentucky (US-KY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0097 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 98073 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0090 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 105736 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0076 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 51917 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0072 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8107 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0071 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 35716 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0069 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 158980 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0067 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 10504 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0059 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 6725 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0057 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 109288 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0056 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 15629 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |






### Top Genera for Louisiana (US-LA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0281 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 27044 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0274 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 171844 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret |
| 0.0241 | [Bubulcus](https://en.wikipedia.org/wiki/Bubulcus)* | Cattle Egret | 50157 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis) | Cattle Egret |
| 0.0235 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 63812 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0189 | [Platalea](https://en.wikipedia.org/wiki/Platalea) |  | 22937 | [Platalea ajaja](https://en.wikipedia.org/wiki/Platalea_ajaja) | Roseate Spoonbill |
| 0.0185 | [Lanius](https://en.wikipedia.org/wiki/Lanius) | Shrike | 50080 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike |
| 0.0183 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 37903 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0181 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 28529 | [Dendrocygna autumnalis](https://en.wikipedia.org/wiki/Dendrocygna_autumnalis) | Black-bellied Whistling-Duck |
| 0.0173 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 20585 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0167 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 164645 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |






### Top Genera for Massachusetts (US-MA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0590 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 147688 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0367 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 193084 | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter |
| 0.0362 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 16342 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0321 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 17049 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.0299 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 28983 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0287 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 13352 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx Shearwater |
| 0.0275 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 19874 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0254 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 45864 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0245 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 953627 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0215 | [Ardenna](https://en.wikipedia.org/wiki/Ardenna) | Shearwater | 27804 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) |  |






### Top Genera for Maryland (US-MD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0337 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 543555 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0220 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 184681 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0170 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 424167 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0151 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 317285 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0148 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 274339 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0138 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 681139 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0137 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 402965 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |
| 0.0129 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 82855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0102 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 60128 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0101 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 150385 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |






### Top Genera for Maine (US-ME)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0760 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 127240 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0487 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 58921 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot |
| 0.0352 | [Fratercula](https://en.wikipedia.org/wiki/Fratercula) | Puffin | 17505 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  |
| 0.0297 | [Alca](https://en.wikipedia.org/wiki/Alca) | Razorbill | 14447 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill |
| 0.0284 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 18634 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0235 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 117292 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |
| 0.0222 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8358 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |
| 0.0210 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 25405 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0207 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 470161 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull |
| 0.0185 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 71853 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |






### Top Genera for Michigan (US-MI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0376 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 176499 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0370 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 236621 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0221 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 125158 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0144 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147923 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0139 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 586777 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0121 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 167208 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0120 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 706919 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0114 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 90666 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0113 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 661443 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0108 | [Agelaius](https://en.wikipedia.org/wiki/Agelaius) | Blackbird | 532312 | [Agelaius phoeniceus](https://en.wikipedia.org/wiki/Agelaius_phoeniceus) | Red-winged Blackbird |






### Top Genera for Minnesota (US-MN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0214 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 46603 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0153 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 121146 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0147 | [Haliaeetus](https://en.wikipedia.org/wiki/Haliaeetus) | Sea Eagle | 156850 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle |
| 0.0133 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 436581 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0128 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 79849 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| 0.0126 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 5462 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0121 | [Acanthis](https://en.wikipedia.org/wiki/Redpoll) | Redpoll | 32330 | [Acanthis flammea](https://en.wikipedia.org/wiki/Acanthis_flammea) | Common Redpoll |
| 0.0115 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 329350 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0113 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 448373 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0105 | [Pinicola](https://en.wikipedia.org/wiki/Pinicola) |  | 13668 | [Pinicola enucleator](https://en.wikipedia.org/wiki/Pinicola_enucleator) | Pine Grosbeak |






### Top Genera for Missouri (US-MO)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0235 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 34191 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0159 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 21081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0131 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 275131 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| 0.0130 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 42272 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0128 | [Passerina](https://en.wikipedia.org/wiki/Passerina) | Bunting | 113686 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting |
| 0.0126 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 209758 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0123 | [Anser](https://en.wikipedia.org/wiki/Anser) | Grey Goose | 46182 | [Anser albifrons](https://en.wikipedia.org/wiki/Anser_albifrons) | Greater White-fronted Goose |
| 0.0112 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 175152 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0112 | [Strix](https://en.wikipedia.org/wiki/Strix_(bird)) | Wood Owl | 29694 | [Strix varia](https://en.wikipedia.org/wiki/Strix_varia) | Barred Owl |
| 0.0108 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22318 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |






### Top Genera for Mississippi (US-MS)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0119 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 17938 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0111 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 8333 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0101 | [Pelecanus](https://en.wikipedia.org/wiki/Pelecanus)† | Pelican | 30763 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis) | Brown Pelican |
| 0.0098 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 8279 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0097 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 66564 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0096 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 29491 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0095 | [Gelochelidon](https://en.wikipedia.org/wiki/Gelochelidon) |  | 3142 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern |
| 0.0087 | [Sternula](https://en.wikipedia.org/wiki/Sternula) |  | 7879 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0085 | [Limnothlypis](https://en.wikipedia.org/wiki/Limnothlypis) |  | 1697 | [Limnothlypis swainsonii](https://en.wikipedia.org/wiki/Limnothlypis_swainsonii) | Swainson's Warbler |
| 0.0077 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 5820 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |






### Top Genera for Montana (US-MT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0585 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 151463 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0403 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 24361 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0259 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 7149 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0255 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 3501 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.0233 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 23231 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0226 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 17889 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0216 | [Pooecetes](https://en.wikipedia.org/wiki/Pooecetes) |  | 31238 | [Pooecetes gramineus](https://en.wikipedia.org/wiki/Pooecetes_gramineus) | Vesper Sparrow |
| 0.0216 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 32921 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0189 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 25367 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0184 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 9534 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |






### Top Genera for North Carolina (US-NC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0367 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 484010 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0360 | [Pterodroma](https://en.wikipedia.org/wiki/Pterodroma) | Gadfly Petrel | 7392 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  |
| 0.0326 | [Calonectris](https://en.wikipedia.org/wiki/Calonectris) | Shearwater | 12415 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater |
| 0.0261 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 307887 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0243 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 416651 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0229 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 295792 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0225 | [Puffinus](https://en.wikipedia.org/wiki/Puffinus) | Shearwater | 8919 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) |  |
| 0.0191 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 161868 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0180 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 281345 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0178 | [Oceanites](https://en.wikipedia.org/wiki/Oceanites) | Storm Petrel | 8420 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  |






### Top Genera for North Dakota (US-ND)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0314 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 6539 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0231 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 24049 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0199 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 18180 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0194 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 7042 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0179 | [Perdix](https://en.wikipedia.org/wiki/Perdix)* | Partridge | 3576 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix) | Gray Partridge |
| 0.0151 | [Chlidonias](https://en.wikipedia.org/wiki/Chlidonias) |  | 9608 | [Chlidonias niger](https://en.wikipedia.org/wiki/Chlidonias_niger) | Black Tern |
| 0.0124 | [Limosa](https://en.wikipedia.org/wiki/Limosa) |  | 9230 | [Limosa fedoa](https://en.wikipedia.org/wiki/Limosa_fedoa) | Marbled Godwit |
| 0.0121 | [Calcarius](https://en.wikipedia.org/wiki/Calcarius) | Longspur | 6966 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur |
| 0.0120 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8173 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0119 | [Phalaropus](https://en.wikipedia.org/wiki/Phalaropus) |  | 11671 | [Phalaropus tricolor](https://en.wikipedia.org/wiki/Phalaropus_tricolor) | Wilson's Phalarope |






### Top Genera for Nebraska (US-NE)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0217 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 19658 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0177 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 4213 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| 0.0152 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)†* | Pheasant | 18728 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0152 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)‡ | Meadowlark | 52365 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0124 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5257 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0122 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 10081 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0113 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 38307 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0111 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 13158 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0107 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 8437 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0080 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)† | Kingbird/Flycatcher | 47511 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird |






### Top Genera for New Hampshire (US-NH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0110 | [Tadorna](https://en.wikipedia.org/wiki/Tadorna)* | Shelduck | 179 | [Tadorna tadorna](https://en.wikipedia.org/wiki/Tadorna_tadorna) | Common Shelduck |
| 0.0103 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 174912 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch |
| 0.0099 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 16705 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0093 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 34197 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0082 | [Catharus](https://en.wikipedia.org/wiki/Catharus)† | Nightingale-thrush | 65080 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| 0.0076 | [Setophaga](https://en.wikipedia.org/wiki/Setophaga) | Warbler | 285427 | [Setophaga caerulescens](https://en.wikipedia.org/wiki/Setophaga_caerulescens) | Black-throated Blue Warbler |
| 0.0075 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 107536 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0073 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 202762 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0070 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 182017 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0065 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 35332 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer) | Common Loon |






### Top Genera for New Jersey (US-NJ)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0312 | [Haematopus](https://en.wikipedia.org/wiki/Haematopus) | Oystercatcher | 68430 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| 0.0285 | [Leucophaeus](https://en.wikipedia.org/wiki/Leucophaeus) | Gull | 193945 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull |
| 0.0273 | [Sterna](https://en.wikipedia.org/wiki/Sterna) | Tern | 163330 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern |
| 0.0240 | [Rynchops](https://en.wikipedia.org/wiki/Rynchops) | Skimmer | 40882 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer |
| 0.0229 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 163719 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0212 | [Morus](https://en.wikipedia.org/wiki/Gannet) | Gannet | 37469 | [Morus bassanus](https://en.wikipedia.org/wiki/Morus_bassanus) | Northern Gannet |
| 0.0209 | [Ammospiza](https://en.wikipedia.org/wiki/Ammospiza) |  | 32984 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| 0.0177 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 759061 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0172 | [Sternula](https://en.wikipedia.org/wiki/Sternula) |  | 37555 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |
| 0.0166 | [Calidris](https://en.wikipedia.org/wiki/Calidris) | Sandpiper | 318740 | [Calidris maritima](https://en.wikipedia.org/wiki/Calidris_maritima) | Purple Sandpiper |






### Top Genera for New Mexico (US-NM)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0462 | [Geococcyx](https://en.wikipedia.org/wiki/Geococcyx)‡ | Roadrunner | 46838 | [Geococcyx californianus](https://en.wikipedia.org/wiki/Geococcyx_californianus) | Greater Roadrunner |
| 0.0403 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 13673 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0364 | [Selasphorus](https://en.wikipedia.org/wiki/Selasphorus) | Hummingbird | 90816 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| 0.0357 | [Melozone](https://en.wikipedia.org/wiki/Melozone) |  | 66915 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee |
| 0.0301 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 57229 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0299 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 79822 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| 0.0285 | [Myadestes](https://en.wikipedia.org/wiki/Myadestes) |  | 32323 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire |
| 0.0271 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 61432 | [Callipepla squamata](https://en.wikipedia.org/wiki/Callipepla_squamata) | Scaled Quail |
| 0.0262 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 10584 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0251 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 23571 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |






### Top Genera for Nevada (US-NV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0533 | [Tetraogallus](https://en.wikipedia.org/wiki/Tetraogallus)* | Snowcock | 672 | [Tetraogallus himalayensis](https://en.wikipedia.org/wiki/Tetraogallus_himalayensis) |  |
| 0.0330 | [Callipepla](https://en.wikipedia.org/wiki/Callipepla)† | Crested Quail | 49041 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail |
| 0.0282 | [Artemisiospiza](https://en.wikipedia.org/wiki/Artemisiospiza) | Sparrow | 5324 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow |
| 0.0277 | [Auriparus](https://en.wikipedia.org/wiki/Auriparus) | Verdin | 29373 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin |
| 0.0223 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 5444 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0219 | [Phainopepla](https://en.wikipedia.org/wiki/Phainopepla) | Phainopepla | 14504 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla |
| 0.0198 | [Amphispiza](https://en.wikipedia.org/wiki/Amphispiza) |  | 12902 | [Amphispiza bilineata](https://en.wikipedia.org/wiki/Amphispiza_bilineata) | Black-throated Sparrow |
| 0.0197 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 6385 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0170 | [Salpinctes](https://en.wikipedia.org/wiki/Salpinctes) |  | 11031 | [Salpinctes obsoletus](https://en.wikipedia.org/wiki/Salpinctes_obsoletus) | Rock Wren |
| 0.0151 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 7780 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |






### Top Genera for New York (US-NY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0261 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 598555 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0254 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 1430945 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0195 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 1053772 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| 0.0171 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 150414 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0165 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 210030 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0154 | [Passer](https://en.wikipedia.org/wiki/Passer)* | True Sparrow | 713416 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus) | House Sparrow |
| 0.0150 | [Clangula](https://en.wikipedia.org/wiki/Clangula) |  | 69918 | [Clangula hyemalis](https://en.wikipedia.org/wiki/Clangula_hyemalis) | Long-tailed Duck |
| 0.0150 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 61677 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler |
| 0.0150 | [Columba](https://en.wikipedia.org/wiki/Columba_(bird)) | Pigeon | 431557 | [Columba livia](https://en.wikipedia.org/wiki/Columba_livia) | Rock Pigeon |
| 0.0147 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 1158294 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |






### Top Genera for Ohio (US-OH)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0158 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 36537 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0151 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 598486 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0144 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 98855 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0141 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 791329 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0129 | [Chaetura](https://en.wikipedia.org/wiki/Chaetura) | Swift | 163264 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift |
| 0.0117 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 420642 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0114 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 91542 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0107 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 288123 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0105 | [Aix](https://en.wikipedia.org/wiki/Aix_(bird)) | Wood Duck | 168915 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck |
| 0.0104 | [Branta](https://en.wikipedia.org/wiki/Branta)† | Black Goose | 583159 | [Branta canadensis](https://en.wikipedia.org/wiki/Branta_canadensis) | Canada Goose |






### Top Genera for Oklahoma (US-OK)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0305 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 21873 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0145 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 14500 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0128 | [Tyrannus](https://en.wikipedia.org/wiki/Tyrannus)‡ | Kingbird/Flycatcher | 70179 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus) | Scissor-tailed Flycatcher |
| 0.0124 | [Chondestes](https://en.wikipedia.org/wiki/Chondestes) |  | 15360 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow |
| 0.0110 | [Colinus](https://en.wikipedia.org/wiki/Colinus) | Bobwhite | 9753 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite |
| 0.0098 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 36984 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |
| 0.0093 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 39044 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark |
| 0.0083 | [Tadorna](https://en.wikipedia.org/wiki/Tadorna)* | Shelduck | 118 | [Tadorna ferruginea](https://en.wikipedia.org/wiki/Tadorna_ferruginea) |  |
| 0.0081 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 3825 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0074 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 65170 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |






### Top Genera for Oregon (US-OR)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1090 | [Aphelocoma](https://en.wikipedia.org/wiki/Aphelocoma) | Scrub Jay | 374161 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| 0.0607 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 261771 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0575 | [Chamaea](https://en.wikipedia.org/wiki/Chamaea) | Wrentit | 38911 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit |
| 0.0527 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 141123 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0484 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 82130 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.0441 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 183400 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0410 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 76024 | [Urile penicillatus](https://en.wikipedia.org/wiki/Urile_penicillatus) | Brandt's Cormorant |
| 0.0385 | [Oreortyx](https://en.wikipedia.org/wiki/Oreortyx) |  | 8746 | [Oreortyx pictus](https://en.wikipedia.org/wiki/Oreortyx_pictus) | Mountain Quail |
| 0.0372 | [Euphagus](https://en.wikipedia.org/wiki/Euphagus) | Blackbird | 157785 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird |
| 0.0365 | [Patagioenas](https://en.wikipedia.org/wiki/Patagioenas) |  | 57823 | [Patagioenas fasciata](https://en.wikipedia.org/wiki/Patagioenas_fasciata) | Band-tailed Pigeon |






### Top Genera for Pennsylvania (US-PA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0312 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 171036 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0254 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 557667 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0253 | [Dumetella](https://en.wikipedia.org/wiki/Dumetella) | Gray Catbird | 456717 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird |
| 0.0246 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 620147 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0183 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 947363 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0143 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 643812 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0142 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 127243 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0139 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 836000 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0135 | [Melospiza](https://en.wikipedia.org/wiki/Melospiza) | Song Sparrow | 828162 | [Melospiza melodia](https://en.wikipedia.org/wiki/Melospiza_melodia) | Song Sparrow |
| 0.0133 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 864555 | [Dryobates pubescens](https://en.wikipedia.org/wiki/Dryobates_pubescens) | Downy Woodpecker |






### Top Genera for Rhode Island (US-RI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0433 | [Cuculus](https://en.wikipedia.org/wiki/Cuculus)* | Cuckoo | 672 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus) | Common Cuckoo |
| 0.0225 | [Phalacrocorax](https://en.wikipedia.org/wiki/Phalacrocorax) | Cormorant | 8422 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| 0.0174 | [Somateria](https://en.wikipedia.org/wiki/Somateria) | Eider | 18190 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| 0.0165 | [Xenus](https://en.wikipedia.org/wiki/Xenus) |  | 194 | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  |
| 0.0114 | [Larus](https://en.wikipedia.org/wiki/Larus)† | Gull | 134161 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull |
| 0.0097 | [Melanitta](https://en.wikipedia.org/wiki/Melanitta) | Scoter | 20964 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter |
| 0.0078 | [Histrionicus](https://en.wikipedia.org/wiki/Histrionicus) |  | 4628 | [Histrionicus histrionicus](https://en.wikipedia.org/wiki/Histrionicus_histrionicus) | Harlequin Duck |
| 0.0074 | [Gavia](https://en.wikipedia.org/wiki/Loon)† | Loon | 23304 | [Gavia stellata](https://en.wikipedia.org/wiki/Gavia_stellata) | Red-throated Loon |
| 0.0065 | [Cygnus](https://en.wikipedia.org/wiki/Swan) | Swan | 19549 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| 0.0065 | [Sternula](https://en.wikipedia.org/wiki/Sternula) |  | 5667 | [Sternula antillarum](https://en.wikipedia.org/wiki/Sternula_antillarum) | Least Tern |






### Top Genera for South Carolina (US-SC)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0303 | [Mycteria](https://en.wikipedia.org/wiki/Mycteria) | Stork | 40234 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork |
| 0.0281 | [Egretta](https://en.wikipedia.org/wiki/Egretta) | Egret | 195795 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron |
| 0.0243 | [Anhinga](https://en.wikipedia.org/wiki/Anhinga) | Darter | 52941 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| 0.0224 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)‡ | Carolina Wren | 251184 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0181 | [Ictinia](https://en.wikipedia.org/wiki/Ictinia) | Mississippi Kite | 20288 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| 0.0171 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 191263 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0159 | [Eudocimus](https://en.wikipedia.org/wiki/Eudocimus) | Ibis | 52824 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis |
| 0.0157 | [Rallus](https://en.wikipedia.org/wiki/Rallus) |  | 33856 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail |
| 0.0151 | [Thalasseus](https://en.wikipedia.org/wiki/Thalasseus) | Crested Tern | 38639 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern |
| 0.0147 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 153302 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |






### Top Genera for South Dakota (US-SD)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0176 | [Tympanuchus](https://en.wikipedia.org/wiki/Tympanuchus) | Prarie Chicken | 3235 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| 0.0164 | [Phasianus](https://en.wikipedia.org/wiki/Phasianus)‡* | Pheasant | 15094 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus) | Ring-necked Pheasant |
| 0.0164 | [Bartramia](https://en.wikipedia.org/wiki/Bartramia_(bird)) | Upland Sandpiper | 5213 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper |
| 0.0124 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 3391 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0116 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 9544 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0107 | [Sturnella](https://en.wikipedia.org/wiki/Sturnella)† | Meadowlark | 28631 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta) | Western Meadowlark |
| 0.0071 | [Athene](https://en.wikipedia.org/wiki/Athene) |  | 1976 | [Athene cunicularia](https://en.wikipedia.org/wiki/Athene_cunicularia) | Burrowing Owl |
| 0.0069 | [Spiza](https://en.wikipedia.org/wiki/Spiza) | Dickcissel | 5350 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| 0.0066 | [Ammodramus](https://en.wikipedia.org/wiki/Ammodramus) |  | 4140 | [Ammodramus savannarum](https://en.wikipedia.org/wiki/Ammodramus_savannarum) | Grasshopper Sparrow |
| 0.0064 | [Spatula](https://en.wikipedia.org/wiki/Spatula_(bird)) | Shoveler/Teal | 27909 | [Spatula discors](https://en.wikipedia.org/wiki/Spatula_discors) | Blue-winged Teal |






### Top Genera for Tennessee (US-TN)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0231 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 264394 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0183 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 181103 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0175 | [Mimus](https://en.wikipedia.org/wiki/Mimus)‡ | Mockingbird | 199634 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0165 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 241408 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0141 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 161292 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0119 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 77257 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0115 | [Toxostoma](https://en.wikipedia.org/wiki/Toxostoma)† | Thrasher | 87297 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum) | Brown Thrasher |
| 0.0115 | [Protonotaria](https://en.wikipedia.org/wiki/Protonotaria) | Prothonotary warbler | 16980 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler |
| 0.0111 | [Icteria](https://en.wikipedia.org/wiki/Icteria) | Yellow-breasted Chat | 22678 | [Icteria virens](https://en.wikipedia.org/wiki/Icteria_virens) | Yellow-breasted Chat |
| 0.0107 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)† | Cardinal | 331627 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |






### Top Genera for Texas (US-TX)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.1250 | [Caracara](https://en.wikipedia.org/wiki/Caracara_(genus)) | Caracara | 249608 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara |
| 0.1026 | [Dendrocygna](https://en.wikipedia.org/wiki/Dendrocygna) |  | 286302 | [Dendrocygna autumnalis](https://en.wikipedia.org/wiki/Dendrocygna_autumnalis) | Black-bellied Whistling-Duck |
| 0.0990 | [Cyanocorax](https://en.wikipedia.org/wiki/Cyanocorax) |  | 150450 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay |
| 0.0940 | [Pitangus](https://en.wikipedia.org/wiki/Pitangus) |  | 187667 | [Pitangus sulphuratus](https://en.wikipedia.org/wiki/Pitangus_sulphuratus) | Great Kiskadee |
| 0.0895 | [Arremonops](https://en.wikipedia.org/wiki/Arremonops) |  | 82550 | [Arremonops rufivirgatus](https://en.wikipedia.org/wiki/Arremonops_rufivirgatus) | Olive Sparrow |
| 0.0849 | [Geranoaetus](https://en.wikipedia.org/wiki/Geranoaetus) |  | 54492 | [Geranoaetus albicaudatus](https://en.wikipedia.org/wiki/Geranoaetus_albicaudatus) | White-tailed Hawk |
| 0.0780 | [Parabuteo](https://en.wikipedia.org/wiki/Parabuteo) |  | 80483 | [Parabuteo unicinctus](https://en.wikipedia.org/wiki/Parabuteo_unicinctus) | Harris's Hawk |
| 0.0764 | [Tachybaptus](https://en.wikipedia.org/wiki/Tachybaptus) |  | 65119 | [Tachybaptus dominicus](https://en.wikipedia.org/wiki/Tachybaptus_dominicus) | Least Grebe |
| 0.0726 | [Ortalis](https://en.wikipedia.org/wiki/Ortalis) |  | 88258 | [Ortalis vetula](https://en.wikipedia.org/wiki/Ortalis_vetula) | Plain Chachalaca |
| 0.0718 | [Leptotila](https://en.wikipedia.org/wiki/Leptotila) |  | 83884 | [Leptotila verreauxi](https://en.wikipedia.org/wiki/Leptotila_verreauxi) | White-tipped Dove |






### Top Genera for Utah (US-UT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0464 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 129642 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0321 | [Alectoris](https://en.wikipedia.org/wiki/Alectoris)* | Rock Partridge | 7064 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar) | Chukar |
| 0.0301 | [Recurvirostra](https://en.wikipedia.org/wiki/Recurvirostra) | Avocet | 41087 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet |
| 0.0286 | [Aechmophorus](https://en.wikipedia.org/wiki/Aechmophorus) | Grebe | 41176 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe |
| 0.0285 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 23315 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0282 | [Xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus) | Yellow-headed Blackbird | 38183 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird |
| 0.0250 | [Gymnorhinus](https://en.wikipedia.org/wiki/Gymnorhinus) | Pinyon Jay | 7974 | [Gymnorhinus cyanocephalus](https://en.wikipedia.org/wiki/Gymnorhinus_cyanocephalus) | Pinyon Jay |
| 0.0225 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 9559 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0224 | [Salpinctes](https://en.wikipedia.org/wiki/Salpinctes) |  | 19107 | [Salpinctes obsoletus](https://en.wikipedia.org/wiki/Salpinctes_obsoletus) | Rock Wren |
| 0.0221 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 92492 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |






### Top Genera for Virginia (US-VA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0391 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 597727 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0232 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 344496 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0216 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 475019 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0202 | [Coragyps](https://en.wikipedia.org/wiki/Coragyps) | Black Vulture | 174913 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture |
| 0.0177 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 195902 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0175 | [Mimus](https://en.wikipedia.org/wiki/Mimus)† | Mockingbird | 339498 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos) | Northern Mockingbird |
| 0.0166 | [Cardinalis](https://en.wikipedia.org/wiki/Cardinalis)‡ | Cardinal | 728016 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis) | Northern Cardinal |
| 0.0139 | [Melanerpes](https://en.wikipedia.org/wiki/Melanerpes) | Woodpecker | 506585 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker |
| 0.0132 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 68865 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0123 | [Cathartes](https://en.wikipedia.org/wiki/Cathartes) | Turkey Vulture | 386942 | [Cathartes aura](https://en.wikipedia.org/wiki/Cathartes_aura) | Turkey Vulture |






### Top Genera for Vermont (US-VT)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0151 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 56705 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |
| 0.0115 | [Bonasa](https://en.wikipedia.org/wiki/Bonasa)† | Ruffed Grouse | 16963 | [Bonasa umbellus](https://en.wikipedia.org/wiki/Bonasa_umbellus) | Ruffed Grouse |
| 0.0108 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 220081 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0106 | [Poecile](https://en.wikipedia.org/wiki/Poecile)† | Chickadee | 296739 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| 0.0093 | [Dolichonyx](https://en.wikipedia.org/wiki/Dolichonyx) |  | 18269 | [Dolichonyx oryzivorus](https://en.wikipedia.org/wiki/Dolichonyx_oryzivorus) | Bobolink |
| 0.0092 | [Sphyrapicus](https://en.wikipedia.org/wiki/Sphyrapicus) |  | 46917 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker |
| 0.0089 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 34849 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0088 | [Cyanocitta](https://en.wikipedia.org/wiki/Cyanocitta) | Blue Jay | 239918 | [Cyanocitta cristata](https://en.wikipedia.org/wiki/Cyanocitta_cristata) | Blue Jay |
| 0.0088 | [Catharus](https://en.wikipedia.org/wiki/Catharus)‡ | Nightingale-thrush | 82690 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| 0.0079 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 240266 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |






### Top Genera for Washington (US-WA)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0764 | [Cerorhinca](https://en.wikipedia.org/wiki/Cerorhinca) | Rhinoceros Puffin | 56517 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet |
| 0.0729 | [Calypte](https://en.wikipedia.org/wiki/Calypte) | Hummingbird | 331274 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird |
| 0.0685 | [Urile](https://en.wikipedia.org/wiki/Urile) |  | 128798 | [Urile pelagicus](https://en.wikipedia.org/wiki/Urile_pelagicus) | Pelagic Cormorant |
| 0.0605 | [Thryomanes](https://en.wikipedia.org/wiki/Thryomanes) |  | 258496 | [Thryomanes bewickii](https://en.wikipedia.org/wiki/Thryomanes_bewickii) | Bewick's Wren |
| 0.0544 | [Ixoreus](https://en.wikipedia.org/wiki/Ixoreus) |  | 98229 | [Ixoreus naevius](https://en.wikipedia.org/wiki/Ixoreus_naevius) | Varied Thrush |
| 0.0522 | [Cepphus](https://en.wikipedia.org/wiki/Cepphus) | Guillemot | 92260 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot |
| 0.0473 | [Psaltriparus](https://en.wikipedia.org/wiki/Psaltriparus) |  | 139869 | [Psaltriparus minimus](https://en.wikipedia.org/wiki/Psaltriparus_minimus) | Bushtit |
| 0.0397 | [Patagioenas](https://en.wikipedia.org/wiki/Patagioenas) |  | 67343 | [Patagioenas fasciata](https://en.wikipedia.org/wiki/Patagioenas_fasciata) | Band-tailed Pigeon |
| 0.0348 | [Uria](https://en.wikipedia.org/wiki/Uria) |  | 42624 | [Uria aalge](https://en.wikipedia.org/wiki/Uria_aalge) | Common Murre |
| 0.0323 | [Brachyramphus](https://en.wikipedia.org/wiki/Brachyramphus) |  | 23672 | [Brachyramphus marmoratus](https://en.wikipedia.org/wiki/Brachyramphus_marmoratus) | Marbled Murrelet |






### Top Genera for Wisconsin (US-WI)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0558 | [Antigone](https://en.wikipedia.org/wiki/Antigone_(bird)) | Crane | 231517 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| 0.0272 | [Parus](https://en.wikipedia.org/wiki/Parus)* |  | 729 | [Parus major](https://en.wikipedia.org/wiki/Parus_major) | Great Tit |
| 0.0211 | [Meleagris](https://en.wikipedia.org/wiki/Meleagris) | Turkey | 120796 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey |
| 0.0165 | [Vermivora](https://en.wikipedia.org/wiki/Vermivora) | Warbler | 43527 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler |
| 0.0162 | [Pheucticus](https://en.wikipedia.org/wiki/Pheucticus) |  | 147853 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak |
| 0.0147 | [Sitta](https://en.wikipedia.org/wiki/Sitta) | Nuthatch | 557294 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch |
| 0.0143 | [Dryobates](https://en.wikipedia.org/wiki/Dryobates) | Woodpecker | 692533 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker |
| 0.0129 | [Spizelloides](https://en.wikipedia.org/wiki/Spizelloides) | Winter Sparrow | 85985 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow |
| 0.0129 | [Troglodytes](https://en.wikipedia.org/wiki/Troglodytes_(bird)) | House Wren | 234418 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren |
| 0.0111 | [Seiurus](https://en.wikipedia.org/wiki/Seiurus) | Ovenbird | 91531 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird |






### Top Genera for West Virginia (US-WV)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0086 | [Hylocichla](https://en.wikipedia.org/wiki/Hylocichla)† | Wood Thrush | 20027 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina) | Wood Thrush |
| 0.0083 | [Dryocopus](https://en.wikipedia.org/wiki/Dryocopus) | Woodpecker | 37014 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker |
| 0.0081 | [Thryothorus](https://en.wikipedia.org/wiki/Thryothorus)† | Carolina Wren | 67983 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus) | Carolina Wren |
| 0.0072 | [Baeolophus](https://en.wikipedia.org/wiki/Baeolophus) | Titmouse | 71638 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| 0.0069 | [Pipilo](https://en.wikipedia.org/wiki/Pipilo) | Towhee | 51062 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| 0.0053 | [Helmitheros](https://en.wikipedia.org/wiki/Helmitheros) |  | 3533 | [Helmitheros vermivorum](https://en.wikipedia.org/wiki/Helmitheros_vermivorum) | Worm-eating Warbler |
| 0.0047 | [Spizella](https://en.wikipedia.org/wiki/Spizella) | Sparrow | 55987 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| 0.0044 | [Coccyzus](https://en.wikipedia.org/wiki/Coccyzus) | Cuckoo | 10480 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo |
| 0.0044 | [Sialia](https://en.wikipedia.org/wiki/Sialia)† | Bluebird | 38524 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis) | Eastern Bluebird |
| 0.0042 | [Vireo](https://en.wikipedia.org/wiki/Vireo) | Vireo | 62010 | [Vireo solitarius](https://en.wikipedia.org/wiki/Vireo_solitarius) | Blue-headed Vireo |






### Top Genera for Wyoming (US-WY)

| Score | Bird | Common Name | Count | Example Species | Common Name |
|---|---|---|---|---|---|
| 0.0328 | [Nucifraga](https://en.wikipedia.org/wiki/Nucifraga) | Nutcracker | 14068 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |
| 0.0321 | [Centrocercus](https://en.wikipedia.org/wiki/Centrocercus) | Sage-grouse | 2281 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse |
| 0.0228 | [Rhynchophanes](https://en.wikipedia.org/wiki/Rhynchophanes) | Longspur | 2228 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur |
| 0.0218 | [Aquila](https://en.wikipedia.org/wiki/Aquila_(bird)) | True Eagle | 11895 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle |
| 0.0207 | [Oreoscoptes](https://en.wikipedia.org/wiki/Oreoscoptes) | Sage Thrasher | 5825 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher |
| 0.0197 | [Pica](https://en.wikipedia.org/wiki/Pica_(genus)) | Magpie | 38495 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| 0.0196 | [Leucosticte](https://en.wikipedia.org/wiki/Leucosticte) |  | 4885 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch |
| 0.0165 | [Calamospiza](https://en.wikipedia.org/wiki/Calamospiza)† | Lark Bunting | 5086 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys) | Lark Bunting |
| 0.0150 | [Cinclus](https://en.wikipedia.org/wiki/Cinclus) |  | 5444 | [Cinclus mexicanus](https://en.wikipedia.org/wiki/Cinclus_mexicanus) | American Dipper |
| 0.0129 | [Streptopelia](https://en.wikipedia.org/wiki/Streptopelia)* | Collared Dove | 35925 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto) | Eurasian Collared-Dove |










## Scores for Bird Species

### Top Scoring Unique State Birds

| State | Score | Bird | Common Name |
|--:|---|---|---|
| US-AK | 0.1510 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned Puffin |
| US-AL | 0.0171 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird |
| US-AR | 0.0159 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager |
| US-AZ | 0.2356 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker |
| US-CA | 0.1930 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee |
| US-CO | 0.1144 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird |
| US-CT | 0.0203 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan |
| US-DC | 0.0175 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  |
| US-DE | 0.0248 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow |
| US-FL | 0.1734 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga |
| US-GA | 0.0964 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch |
| US-HI | 0.3210 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove |
| US-IA | 0.0158 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel |
| US-ID | 0.0679 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill |
| US-IL | 0.0323 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow |
| US-IN | 0.0173 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker |
| US-KS | 0.0637 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow |
| US-KY | 0.0101 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse |
| US-LA | 0.0282 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite |
| US-MA | 0.0612 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider |
| US-MD | 0.0330 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow |
| US-ME | 0.0853 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot |
| US-MI | 0.0454 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler |
| US-MN | 0.0398 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan |
| US-MO | 0.0836 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow |
| US-MS | 0.0129 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican |
| US-MT | 0.0590 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie |
| US-NC | 0.0496 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee |
| US-ND | 0.0374 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse |
| US-NE | 0.0292 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken |
| US-NH | 0.0308 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush |
| US-NJ | 0.0408 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher |
| US-NM | 0.0765 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse |
| US-NV | 0.0339 | [Toxostoma crissale](https://en.wikipedia.org/wiki/Toxostoma_crissale) | Crissal Thrasher |
| US-NY | 0.0381 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant |
| US-OH | 0.0199 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow |
| US-OK | 0.0396 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher |
| US-OR | 0.1714 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay |
| US-PA | 0.0312 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush |
| US-RI | 0.0225 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant |
| US-SC | 0.0331 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting |
| US-SD | 0.0207 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark |
| US-TN | 0.0258 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee |
| US-TX | 0.1763 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse |
| US-UT | 0.0510 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay |
| US-VA | 0.0391 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren |
| US-VT | 0.0209 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee |
| US-WA | 0.0965 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull |
| US-WI | 0.0558 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane |
| US-WV | 0.0095 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager |
| US-WY | 0.0328 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker |





### Top Species for Alaska (US-AK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1510 | [Fratercula corniculata](https://en.wikipedia.org/wiki/Fratercula_corniculata) | Horned Puffin | 22891 |
| 0.1288 | [Sterna paradisaea](https://en.wikipedia.org/wiki/Sterna_paradisaea) | Arctic Tern | 49261 |
| 0.1254 | [Calidris ptilocnemis](https://en.wikipedia.org/wiki/Calidris_ptilocnemis) | Rock Sandpiper | 18728 |
| 0.1233 | [Urile urile](https://en.wikipedia.org/wiki/Urile_urile) |  | 12099 |
| 0.1228 | [Fratercula cirrhata](https://en.wikipedia.org/wiki/Fratercula_cirrhata) | Tufted Puffin | 25193 |
| 0.1169 | [Aethia psittacula](https://en.wikipedia.org/wiki/Aethia_psittacula) | Parakeet auklet | 11024 |
| 0.1156 | [Aethia cristatella](https://en.wikipedia.org/wiki/Aethia_cristatella) |  | 10114 |
| 0.1132 | [Aethia pusilla](https://en.wikipedia.org/wiki/Aethia_pusilla) |  | 9479 |
| 0.1087 | [Rissa tridactyla](https://en.wikipedia.org/wiki/Rissa_tridactyla) | Black-legged Kittiwake | 54048 |
| 0.1078 | [Larus brachyrhynchus](https://en.wikipedia.org/wiki/Larus_brachyrhynchus) |  | 100304 |






### Top Species for Alabama (US-AL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0239 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 32313 |
| 0.0171 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 130529 |
| 0.0163 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 59435 |
| 0.0155 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 28464 |
| 0.0153 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 46854 |
| 0.0151 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 101376 |
| 0.0148 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo | 40372 |
| 0.0141 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 127076 |
| 0.0140 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican | 30802 |
| 0.0136 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 69546 |






### Top Species for Arkansas (US-AR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0183 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 19125 |
| 0.0170 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 98316 |
| 0.0159 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 26191 |
| 0.0136 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 10710 |
| 0.0129 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 7297 |
| 0.0106 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 40627 |
| 0.0103 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 91280 |
| 0.0103 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 28129 |
| 0.0099 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 93388 |
| 0.0095 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 10491 |






### Top Species for Arizona (US-AZ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.2356 | [Melanerpes uropygialis](https://en.wikipedia.org/wiki/Melanerpes_uropygialis) | Gila Woodpecker | 443649 |
| 0.1952 | [Melozone aberti](https://en.wikipedia.org/wiki/Melozone_aberti) | Abert's Towhee | 262829 |
| 0.1867 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 386191 |
| 0.1735 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 281419 |
| 0.1630 | [Baeolophus wollweberi](https://en.wikipedia.org/wiki/Baeolophus_wollweberi) | Bridled Titmouse | 147289 |
| 0.1552 | [Phainopepla nitens](https://en.wikipedia.org/wiki/Phainopepla_nitens) | Phainopepla | 200508 |
| 0.1494 | [Aphelocoma wollweberi](https://en.wikipedia.org/wiki/Aphelocoma_wollweberi) | Mexican Jay | 130540 |
| 0.1474 | [Toxostoma curvirostre](https://en.wikipedia.org/wiki/Toxostoma_curvirostre) | Curve-billed Thrasher | 293199 |
| 0.1464 | [Cynanthus latirostris](https://en.wikipedia.org/wiki/Cynanthus_latirostris) | Broad-billed Hummingbird | 169527 |
| 0.1423 | [Campylorhynchus brunneicapillus](https://en.wikipedia.org/wiki/Campylorhynchus_brunneicapillus)‡ | Cactus Wren | 200611 |






### Top Species for California (US-CA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1930 | [Melozone crissalis](https://en.wikipedia.org/wiki/Melozone_crissalis) | California Towhee | 124793 |
| 0.1711 | [Dryobates nuttallii](https://en.wikipedia.org/wiki/Dryobates_nuttallii) | Nuttall's Woodpecker | 74045 |
| 0.1452 | [Baeolophus inornatus](https://en.wikipedia.org/wiki/Baeolophus_inornatus) | Oak Titmouse | 64598 |
| 0.1261 | [Selasphorus sasin](https://en.wikipedia.org/wiki/Selasphorus_sasin) | Allen's Hummingbird | 37169 |
| 0.1204 | [Toxostoma redivivum](https://en.wikipedia.org/wiki/Toxostoma_redivivum) | California Thrasher | 30314 |
| 0.1098 | [Chamaea fasciata](https://en.wikipedia.org/wiki/Chamaea_fasciata) | Wrentit | 57649 |
| 0.1058 | [Sayornis nigricans](https://en.wikipedia.org/wiki/Sayornis_nigricans) | Black Phoebe | 186372 |
| 0.1056 | [Pica nuttalli](https://en.wikipedia.org/wiki/Pica_nuttalli) | Yellow-billed Magpie | 17869 |
| 0.0947 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 90542 |
| 0.0840 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 151564 |






### Top Species for Colorado (US-CO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1144 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 174912 |
| 0.0961 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 387306 |
| 0.0726 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 174321 |
| 0.0703 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 240927 |
| 0.0633 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 99324 |
| 0.0591 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 86998 |
| 0.0579 | [Leucosticte australis](https://en.wikipedia.org/wiki/Leucosticte_australis) | Brown-capped Rosy-Finch | 9642 |
| 0.0543 | [Sitta pygmaea](https://en.wikipedia.org/wiki/Sitta_pygmaea) | Pygmy Nuthatch | 74209 |
| 0.0538 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire | 73348 |
| 0.0535 | [Empidonax occidentalis](https://en.wikipedia.org/wiki/Empidonax_occidentalis) | Cordilleran Flycatcher | 38951 |






### Top Species for Connecticut (US-CT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0234 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 34897 |
| 0.0203 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 63483 |
| 0.0169 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck | 80412 |
| 0.0160 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 240563 |
| 0.0157 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 22502 |
| 0.0140 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 73992 |
| 0.0139 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 139243 |
| 0.0135 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler | 21020 |
| 0.0134 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 41165 |
| 0.0131 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 5067 |






### Top Species for District of Columbia (US-DC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0175 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 10911 |
| 0.0119 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 26969 |
| 0.0097 | [Branta leucopsis](https://en.wikipedia.org/wiki/Branta_leucopsis) |  | 536 |
| 0.0088 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 24475 |
| 0.0060 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 41998 |
| 0.0054 | [Larus michahellis](https://en.wikipedia.org/wiki/Larus_michahellis) |  | 33 |
| 0.0047 | [Passer domesticus](https://en.wikipedia.org/wiki/Passer_domesticus)* | House Sparrow | 42950 |
| 0.0047 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 27503 |
| 0.0047 | [Sturnus vulgaris](https://en.wikipedia.org/wiki/Sturnus_vulgaris)* | European Starling | 53975 |
| 0.0046 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 28883 |






### Top Species for Delaware (US-DE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0248 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 9067 |
| 0.0193 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 37786 |
| 0.0173 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 53074 |
| 0.0167 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 12429 |
| 0.0156 | [Limnodromus griseus](https://en.wikipedia.org/wiki/Limnodromus_griseus) | Short-billed Dowitcher | 19031 |
| 0.0131 | [Plegadis falcinellus](https://en.wikipedia.org/wiki/Plegadis_falcinellus) | Glossy Ibis | 15414 |
| 0.0130 | [Egretta garzetta](https://en.wikipedia.org/wiki/Egretta_garzetta)* | Little Egret | 503 |
| 0.0127 | [Passerina caerulea](https://en.wikipedia.org/wiki/Passerina_caerulea) | Blue Grosbeak | 21757 |
| 0.0127 | [Calidris pusilla](https://en.wikipedia.org/wiki/Calidris_pusilla) | Semipalmated Sandpiper | 22300 |
| 0.0126 | [Calidris alpina](https://en.wikipedia.org/wiki/Calidris_alpina) | Dunlin | 21218 |






### Top Species for Florida (US-FL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1734 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 553383 |
| 0.1734 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 748541 |
| 0.1514 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle | 540152 |
| 0.1438 | [Aramus guarauna](https://en.wikipedia.org/wiki/Aramus_guarauna) | Limpkin | 184399 |
| 0.1373 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 284639 |
| 0.1349 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 558321 |
| 0.1296 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron | 454977 |
| 0.1172 | [Cairina moschata](https://en.wikipedia.org/wiki/Cairina_moschata) | Muscovy Duck | 97493 |
| 0.1101 | [Gallinula galeata](https://en.wikipedia.org/wiki/Gallinula_galeata) | Common Gallinule | 389658 |
| 0.1045 | [Plegadis falcinellus](https://en.wikipedia.org/wiki/Plegadis_falcinellus) | Glossy Ibis | 231267 |






### Top Species for Georgia (US-GA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0964 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 176715 |
| 0.0427 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 176004 |
| 0.0395 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 264079 |
| 0.0390 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 351685 |
| 0.0347 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)‡ | Brown Thrasher | 179633 |
| 0.0318 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 395603 |
| 0.0264 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 248961 |
| 0.0239 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 345328 |
| 0.0232 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)† | Northern Mockingbird | 288903 |
| 0.0224 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo | 93851 |






### Top Species for Hawaii (US-HI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.3662 | [Zosterops japonicus](https://en.wikipedia.org/wiki/Zosterops_japonicus)* |  | 82840 |
| 0.3591 | [Geopelia striata](https://en.wikipedia.org/wiki/Geopelia_striata)* |  | 78346 |
| 0.3515 | [Acridotheres tristis](https://en.wikipedia.org/wiki/Acridotheres_tristis)* | Common Myna | 89440 |
| 0.3210 | [Streptopelia chinensis](https://en.wikipedia.org/wiki/Streptopelia_chinensis) | Spotted Dove | 63162 |
| 0.2831 | [Paroaria coronata](https://en.wikipedia.org/wiki/Paroaria_coronata)* |  | 39698 |
| 0.2727 | [Himatione sanguinea](https://en.wikipedia.org/wiki/Himatione_sanguinea) | Apapane | 35689 |
| 0.2575 | [Pluvialis fulva](https://en.wikipedia.org/wiki/Pluvialis_fulva) | Pacific Golden-Plover | 54637 |
| 0.2543 | [Chlorodrepanis virens](https://en.wikipedia.org/wiki/Chlorodrepanis_virens) |  | 29234 |
| 0.2419 | [Estrilda astrild](https://en.wikipedia.org/wiki/Estrilda_astrild) |  | 25340 |
| 0.2358 | [Sicalis flaveola](https://en.wikipedia.org/wiki/Sicalis_flaveola) |  | 23701 |






### Top Species for Iowa (US-IA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0338 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 7675 |
| 0.0161 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 21293 |
| 0.0158 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 15850 |
| 0.0139 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 24590 |
| 0.0097 | [Pelecanus erythrorhynchos](https://en.wikipedia.org/wiki/Pelecanus_erythrorhynchos) | American White Pelican | 20786 |
| 0.0078 | [Troglodytes aedon](https://en.wikipedia.org/wiki/Troglodytes_aedon) | House Wren | 44452 |
| 0.0078 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 5050 |
| 0.0075 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 5205 |
| 0.0072 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 23330 |
| 0.0068 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 9468 |






### Top Species for Idaho (US-ID)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0679 | [Loxia sinesciuris](https://en.wikipedia.org/wiki/Loxia_sinesciuris) | Cassia Crossbill | 2084 |
| 0.0487 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 53065 |
| 0.0480 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 118106 |
| 0.0280 | [Haemorhous cassinii](https://en.wikipedia.org/wiki/Haemorhous_cassinii) | Cassin's Finch | 20202 |
| 0.0247 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 10890 |
| 0.0235 | [Passerina amoena](https://en.wikipedia.org/wiki/Passerina_amoena) | Lazuli Bunting | 20762 |
| 0.0226 | [Buteo swainsoni](https://en.wikipedia.org/wiki/Buteo_swainsoni) | Swainson's Hawk | 25401 |
| 0.0212 | [Euphagus cyanocephalus](https://en.wikipedia.org/wiki/Euphagus_cyanocephalus) | Brewer's Blackbird | 38461 |
| 0.0189 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 42774 |
| 0.0187 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 29550 |






### Top Species for Illinois (US-IL)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0323 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 18756 |
| 0.0318 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 14313 |
| 0.0215 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 46626 |
| 0.0189 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 161280 |
| 0.0186 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 163028 |
| 0.0178 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 73692 |
| 0.0170 | [Carduelis carduelis](https://en.wikipedia.org/wiki/Carduelis_carduelis)* | European Goldfinch | 1798 |
| 0.0163 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 122446 |
| 0.0162 | [Hydroprogne caspia](https://en.wikipedia.org/wiki/Hydroprogne_caspia) | Caspian Tern | 70704 |
| 0.0159 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 101314 |






### Top Species for Indiana (US-IN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0192 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 192755 |
| 0.0173 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 50156 |
| 0.0160 | [Centronyx henslowii](https://en.wikipedia.org/wiki/Centronyx_henslowii) | Henslow's Sparrow | 7607 |
| 0.0146 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 76320 |
| 0.0141 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 224909 |
| 0.0127 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 223851 |
| 0.0115 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 231871 |
| 0.0110 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 77749 |
| 0.0105 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 10117 |
| 0.0102 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 23122 |






### Top Species for Kansas (US-KS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0637 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 43167 |
| 0.0304 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 36284 |
| 0.0248 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 26149 |
| 0.0215 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 22554 |
| 0.0182 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 57726 |
| 0.0179 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2429 |
| 0.0150 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow | 24003 |
| 0.0147 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 8401 |
| 0.0144 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 14481 |
| 0.0141 | [Calidris bairdii](https://en.wikipedia.org/wiki/Calidris_bairdii) | Baird's Sandpiper | 11235 |






### Top Species for Kentucky (US-KY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0182 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 113140 |
| 0.0101 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 105736 |
| 0.0100 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 42976 |
| 0.0097 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 98073 |
| 0.0094 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 52593 |
| 0.0093 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 34045 |
| 0.0092 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 5928 |
| 0.0091 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 28330 |
| 0.0090 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 18248 |
| 0.0078 | [Setophaga dominica](https://en.wikipedia.org/wiki/Setophaga_dominica) | Yellow-throated Warbler | 11719 |






### Top Species for Louisiana (US-LA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0282 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 27044 |
| 0.0241 | [Bubulcus ibis](https://en.wikipedia.org/wiki/Bubulcus_ibis)* | Cattle Egret | 50157 |
| 0.0235 | [Eudocimus albus](https://en.wikipedia.org/wiki/Eudocimus_albus) | White Ibis | 63812 |
| 0.0226 | [Lanius ludovicianus](https://en.wikipedia.org/wiki/Lanius_ludovicianus) | Loggerhead Shrike | 50080 |
| 0.0203 | [Egretta thula](https://en.wikipedia.org/wiki/Egretta_thula) | Snowy Egret | 78150 |
| 0.0201 | [Ardea alba](https://en.wikipedia.org/wiki/Ardea_alba) | Great Egret | 133593 |
| 0.0200 | [Egretta caerulea](https://en.wikipedia.org/wiki/Egretta_caerulea) | Little Blue Heron | 52377 |
| 0.0196 | [Rallus elegans](https://en.wikipedia.org/wiki/Rallus_elegans) | King Rail | 6306 |
| 0.0189 | [Platalea ajaja](https://en.wikipedia.org/wiki/Platalea_ajaja) | Roseate Spoonbill | 22937 |
| 0.0183 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 37903 |






### Top Species for Massachusetts (US-MA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0612 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 143177 |
| 0.0416 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 248999 |
| 0.0407 | [Ardenna gravis](https://en.wikipedia.org/wiki/Ardenna_gravis) |  | 19121 |
| 0.0381 | [Puffinus puffinus](https://en.wikipedia.org/wiki/Puffinus_puffinus) | Manx Shearwater | 9833 |
| 0.0362 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater | 16342 |
| 0.0362 | [Melanitta deglandi](https://en.wikipedia.org/wiki/Melanitta_deglandi) | White-winged Scoter | 81877 |
| 0.0359 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 411691 |
| 0.0355 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 14117 |
| 0.0348 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 145179 |
| 0.0321 | [Oceanites oceanicus](https://en.wikipedia.org/wiki/Oceanites_oceanicus) |  | 17049 |






### Top Species for Maryland (US-MD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0392 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 455890 |
| 0.0337 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 543555 |
| 0.0330 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 203375 |
| 0.0318 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 53171 |
| 0.0279 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 61388 |
| 0.0220 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture | 184681 |
| 0.0203 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 326126 |
| 0.0198 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 424167 |
| 0.0190 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 274036 |
| 0.0176 | [Buteo lineatus](https://en.wikipedia.org/wiki/Buteo_lineatus) | Red-shouldered Hawk | 151661 |






### Top Species for Maine (US-ME)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0853 | [Cepphus grylle](https://en.wikipedia.org/wiki/Cepphus_grylle) | Black Guillemot | 58921 |
| 0.0803 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 126024 |
| 0.0735 | [Fratercula arctica](https://en.wikipedia.org/wiki/Fratercula_arctica) |  | 17498 |
| 0.0376 | [Sterna dougallii](https://en.wikipedia.org/wiki/Sterna_dougallii) | Roseate Tern | 10380 |
| 0.0356 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 250547 |
| 0.0297 | [Hydrobates leucorhous](https://en.wikipedia.org/wiki/Hydrobates_leucorhous) | Leach's Storm-Petrel | 7558 |
| 0.0297 | [Alca torda](https://en.wikipedia.org/wiki/Alca_torda) | Razorbill | 14447 |
| 0.0286 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 117454 |
| 0.0284 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 18634 |
| 0.0273 | [Gavia immer](https://en.wikipedia.org/wiki/Gavia_immer)† | Common Loon | 107073 |






### Top Species for Michigan (US-MI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0454 | [Setophaga kirtlandii](https://en.wikipedia.org/wiki/Setophaga_kirtlandii) | Kirtland's Warbler | 7644 |
| 0.0428 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 165631 |
| 0.0376 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 176499 |
| 0.0236 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 672265 |
| 0.0234 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147717 |
| 0.0221 | [Spizelloides arborea](https://en.wikipedia.org/wiki/Spizelloides_arborea) | American Tree Sparrow | 125158 |
| 0.0177 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 447738 |
| 0.0167 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 48981 |
| 0.0161 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 159953 |
| 0.0151 | [Tringa erythropus](https://en.wikipedia.org/wiki/Tringa_erythropus) |  | 521 |






### Top Species for Minnesota (US-MN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0398 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 69864 |
| 0.0243 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 443332 |
| 0.0231 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 34266 |
| 0.0222 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 22221 |
| 0.0214 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 46603 |
| 0.0183 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 13045 |
| 0.0173 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 168673 |
| 0.0153 | [Aix sponsa](https://en.wikipedia.org/wiki/Aix_sponsa) | Wood Duck | 121146 |
| 0.0147 | [Haliaeetus leucocephalus](https://en.wikipedia.org/wiki/Haliaeetus_leucocephalus) | Bald Eagle | 156850 |
| 0.0137 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 249129 |






### Top Species for Missouri (US-MO)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0836 | [Passer montanus](https://en.wikipedia.org/wiki/Passer_montanus) | Eurasian Tree Sparrow | 26402 |
| 0.0237 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 18709 |
| 0.0235 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 34191 |
| 0.0207 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 53929 |
| 0.0180 | [Passerina cyanea](https://en.wikipedia.org/wiki/Passerina_cyanea) | Indigo Bunting | 98416 |
| 0.0169 | [Piranga rubra](https://en.wikipedia.org/wiki/Piranga_rubra) | Summer Tanager | 43217 |
| 0.0161 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 21081 |
| 0.0156 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 62789 |
| 0.0155 | [Parkesia motacilla](https://en.wikipedia.org/wiki/Parkesia_motacilla) | Louisiana Waterthrush | 21483 |
| 0.0153 | [Coccyzus americanus](https://en.wikipedia.org/wiki/Coccyzus_americanus) | Yellow-billed Cuckoo | 40958 |






### Top Species for Mississippi (US-MS)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0129 | [Pelecanus occidentalis](https://en.wikipedia.org/wiki/Pelecanus_occidentalis)† | Brown Pelican | 22486 |
| 0.0121 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 7469 |
| 0.0121 | [Thalasseus maximus](https://en.wikipedia.org/wiki/Thalasseus_maximus) | Royal Tern | 14849 |
| 0.0112 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 29022 |
| 0.0111 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer | 8333 |
| 0.0109 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 17796 |
| 0.0098 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 8279 |
| 0.0098 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 66564 |
| 0.0097 | [Vireo griseus](https://en.wikipedia.org/wiki/Vireo_griseus) | White-eyed Vireo | 22530 |
| 0.0095 | [Gelochelidon nilotica](https://en.wikipedia.org/wiki/Gelochelidon_nilotica) | Gull-billed Tern | 3142 |






### Top Species for Montana (US-MT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0590 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 151463 |
| 0.0403 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 24361 |
| 0.0339 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 52991 |
| 0.0309 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 69546 |
| 0.0308 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 29319 |
| 0.0306 | [Selasphorus calliope](https://en.wikipedia.org/wiki/Selasphorus_calliope) | Calliope Hummingbird | 14066 |
| 0.0281 | [Sphyrapicus nuchalis](https://en.wikipedia.org/wiki/Sphyrapicus_nuchalis) | Red-naped Sapsucker | 16678 |
| 0.0279 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 6066 |
| 0.0262 | [Myadestes townsendi](https://en.wikipedia.org/wiki/Myadestes_townsendi) | Townsend's Solitaire | 23231 |
| 0.0259 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 7149 |






### Top Species for North Carolina (US-NC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0771 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 154113 |
| 0.0496 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 463009 |
| 0.0462 | [Pterodroma hasitata](https://en.wikipedia.org/wiki/Pterodroma_hasitata) |  | 6000 |
| 0.0407 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 295774 |
| 0.0367 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 484010 |
| 0.0359 | [Puffinus lherminieri](https://en.wikipedia.org/wiki/Puffinus_lherminieri) |  | 7090 |
| 0.0333 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 157308 |
| 0.0326 | [Calonectris diomedea](https://en.wikipedia.org/wiki/Calonectris_diomedea) | Cory's Shearwater | 12415 |
| 0.0311 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 307886 |
| 0.0272 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 416651 |






### Top Species for North Dakota (US-ND)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0374 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 6240 |
| 0.0306 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 4748 |
| 0.0265 | [Spizella pallida](https://en.wikipedia.org/wiki/Spizella_pallida) | Clay-colored Sparrow | 19291 |
| 0.0263 | [Centronyx bairdii](https://en.wikipedia.org/wiki/Centronyx_bairdii) | Baird's Sparrow | 1986 |
| 0.0231 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 24049 |
| 0.0211 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 33762 |
| 0.0207 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 14372 |
| 0.0199 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 18180 |
| 0.0194 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 7042 |
| 0.0179 | [Perdix perdix](https://en.wikipedia.org/wiki/Perdix_perdix)* | Gray Partridge | 3576 |






### Top Species for Nebraska (US-NE)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0292 | [Tympanuchus cupido](https://en.wikipedia.org/wiki/Tympanuchus_cupido) | Greater Prairie-Chicken | 2934 |
| 0.0252 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 13378 |
| 0.0234 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)‡ | Western Meadowlark | 42141 |
| 0.0217 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 19658 |
| 0.0152 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)†* | Ring-necked Pheasant | 18728 |
| 0.0126 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 20934 |
| 0.0124 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 10081 |
| 0.0124 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5257 |
| 0.0118 | [Tyrannus verticalis](https://en.wikipedia.org/wiki/Tyrannus_verticalis) | Western Kingbird | 17491 |
| 0.0116 | [Streptopelia decaocto](https://en.wikipedia.org/wiki/Streptopelia_decaocto)* | Eurasian Collared-Dove | 38303 |






### Top Species for New Hampshire (US-NH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0308 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3457 |
| 0.0148 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 198394 |
| 0.0148 | [Tadorna tadorna](https://en.wikipedia.org/wiki/Tadorna_tadorna)* | Common Shelduck | 179 |
| 0.0123 | [Buteo platypterus](https://en.wikipedia.org/wiki/Buteo_platypterus) | Broad-winged Hawk | 19622 |
| 0.0110 | [Troglodytes hiemalis](https://en.wikipedia.org/wiki/Troglodytes_hiemalis) | Winter Wren | 20250 |
| 0.0105 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 16306 |
| 0.0103 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 74627 |
| 0.0100 | [Sitta canadensis](https://en.wikipedia.org/wiki/Sitta_canadensis) | Red-breasted Nuthatch | 61610 |
| 0.0098 | [Vireo solitarius](https://en.wikipedia.org/wiki/Vireo_solitarius) | Blue-headed Vireo | 24126 |
| 0.0096 | [Empidonax flaviventris](https://en.wikipedia.org/wiki/Empidonax_flaviventris) | Yellow-bellied Flycatcher | 5766 |






### Top Species for New Jersey (US-NJ)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0408 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 68430 |
| 0.0393 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 149892 |
| 0.0389 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 73643 |
| 0.0364 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 211320 |
| 0.0343 | [Leucophaeus atricilla](https://en.wikipedia.org/wiki/Leucophaeus_atricilla) | Laughing Gull | 193668 |
| 0.0323 | [Ammospiza maritima](https://en.wikipedia.org/wiki/Ammospiza_maritima) | Seaside Sparrow | 21461 |
| 0.0297 | [Sterna forsteri](https://en.wikipedia.org/wiki/Sterna_forsteri) | Forster's Tern | 111498 |
| 0.0269 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 37087 |
| 0.0240 | [Rynchops niger](https://en.wikipedia.org/wiki/Rynchops_niger) | Black Skimmer | 40882 |
| 0.0238 | [Plegadis falcinellus](https://en.wikipedia.org/wiki/Plegadis_falcinellus) | Glossy Ibis | 51995 |






### Top Species for New Mexico (US-NM)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0765 | [Baeolophus ridgwayi](https://en.wikipedia.org/wiki/Baeolophus_ridgwayi) | Juniper Titmouse | 31338 |
| 0.0700 | [Melozone fusca](https://en.wikipedia.org/wiki/Melozone_fusca) | Canyon Towhee | 66423 |
| 0.0689 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 76727 |
| 0.0593 | [Sialia mexicana](https://en.wikipedia.org/wiki/Sialia_mexicana) | Western Bluebird | 70275 |
| 0.0592 | [Corvus cryptoleucus](https://en.wikipedia.org/wiki/Corvus_cryptoleucus) | Chihuahuan Raven | 26986 |
| 0.0590 | [Archilochus alexandri](https://en.wikipedia.org/wiki/Archilochus_alexandri) | Black-chinned Hummingbird | 90799 |
| 0.0578 | [Sayornis saya](https://en.wikipedia.org/wiki/Sayornis_saya) | Say's Phoebe | 100938 |
| 0.0509 | [Callipepla squamata](https://en.wikipedia.org/wiki/Callipepla_squamata) | Scaled Quail | 19220 |
| 0.0505 | [Selasphorus platycercus](https://en.wikipedia.org/wiki/Selasphorus_platycercus) | Broad-tailed Hummingbird | 58293 |
| 0.0494 | [Corvus sp. (raven sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 13606 |






### Top Species for Nevada (US-NV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0533 | [Tetraogallus himalayensis](https://en.wikipedia.org/wiki/Tetraogallus_himalayensis)* |  | 672 |
| 0.0339 | [Toxostoma crissale](https://en.wikipedia.org/wiki/Toxostoma_crissale) | Crissal Thrasher | 8275 |
| 0.0317 | [Artemisiospiza nevadensis](https://en.wikipedia.org/wiki/Artemisiospiza_nevadensis) | Sagebrush Sparrow | 5068 |
| 0.0317 | [Polioptila melanura](https://en.wikipedia.org/wiki/Polioptila_melanura) | Black-tailed Gnatcatcher | 14326 |
| 0.0297 | [Callipepla gambelii](https://en.wikipedia.org/wiki/Callipepla_gambelii) | Gambel's Quail | 24428 |
| 0.0279 | [Calypte costae](https://en.wikipedia.org/wiki/Calypte_costae) | Costa's Hummingbird | 10397 |
| 0.0277 | [Auriparus flaviceps](https://en.wikipedia.org/wiki/Auriparus_flaviceps) | Verdin | 29373 |
| 0.0257 | [Callipepla californica](https://en.wikipedia.org/wiki/Callipepla_californica)† | California Quail | 24613 |
| 0.0248 | [Spizella breweri](https://en.wikipedia.org/wiki/Spizella_breweri) | Brewer's Sparrow | 13506 |
| 0.0223 | [Podiceps nigricollis](https://en.wikipedia.org/wiki/Podiceps_nigricollis) | Eared Grebe | 19208 |






### Top Species for New York (US-NY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0381 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 98677 |
| 0.0341 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 289559 |
| 0.0289 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 169881 |
| 0.0274 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 487807 |
| 0.0261 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 598555 |
| 0.0241 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 1033854 |
| 0.0212 | [Anas rubripes](https://en.wikipedia.org/wiki/Anas_rubripes) | American Black Duck | 210454 |
| 0.0194 | [Haematopus palliatus](https://en.wikipedia.org/wiki/Haematopus_palliatus) | American Oystercatcher | 54113 |
| 0.0194 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 261454 |
| 0.0193 | [Vermivora cyanoptera](https://en.wikipedia.org/wiki/Vermivora_cyanoptera) | Blue-winged Warbler | 56745 |






### Top Species for Ohio (US-OH)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0208 | [Cygnus buccinator](https://en.wikipedia.org/wiki/Cygnus_buccinator) | Trumpeter Swan | 59931 |
| 0.0199 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 154740 |
| 0.0192 | [Setophaga castanea](https://en.wikipedia.org/wiki/Setophaga_castanea) | Bay-breasted Warbler | 41766 |
| 0.0176 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 519777 |
| 0.0172 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 175963 |
| 0.0164 | [Melanerpes erythrocephalus](https://en.wikipedia.org/wiki/Melanerpes_erythrocephalus) | Red-headed Woodpecker | 78708 |
| 0.0158 | [Protonotaria citrea](https://en.wikipedia.org/wiki/Protonotaria_citrea) | Prothonotary Warbler | 36537 |
| 0.0147 | [Chaetura pelagica](https://en.wikipedia.org/wiki/Chaetura_pelagica) | Chimney Swift | 163264 |
| 0.0146 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)‡ | Northern Cardinal | 791329 |
| 0.0146 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 293507 |






### Top Species for Oklahoma (US-OK)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0396 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)‡ | Scissor-tailed Flycatcher | 37937 |
| 0.0317 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 17544 |
| 0.0306 | [Ictinia mississippiensis](https://en.wikipedia.org/wiki/Ictinia_mississippiensis) | Mississippi Kite | 21873 |
| 0.0162 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 13547 |
| 0.0161 | [Tadorna ferruginea](https://en.wikipedia.org/wiki/Tadorna_ferruginea) |  | 114 |
| 0.0145 | [Spiza americana](https://en.wikipedia.org/wiki/Spiza_americana) | Dickcissel | 14500 |
| 0.0142 | [Vireo atricapilla](https://en.wikipedia.org/wiki/Vireo_atricapilla) | Black-capped Vireo | 1693 |
| 0.0124 | [Chondestes grammacus](https://en.wikipedia.org/wiki/Chondestes_grammacus) | Lark Sparrow | 15360 |
| 0.0115 | [Sturnella magna](https://en.wikipedia.org/wiki/Sturnella_magna) | Eastern Meadowlark | 29688 |
| 0.0111 | [Colinus virginianus](https://en.wikipedia.org/wiki/Colinus_virginianus) | Northern Bobwhite | 9753 |






### Top Species for Oregon (US-OR)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1714 | [Aphelocoma californica](https://en.wikipedia.org/wiki/Aphelocoma_californica) | California Scrub-Jay | 374161 |
| 0.0838 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 303921 |
| 0.0828 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow | 178500 |
| 0.0770 | [Larus occidentalis](https://en.wikipedia.org/wiki/Larus_occidentalis) | Western Gull | 93667 |
| 0.0741 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 389415 |
| 0.0686 | [Chaetura vauxi](https://en.wikipedia.org/wiki/Chaetura_vauxi) | Vaux's Swift | 69677 |
| 0.0649 | [Sphyrapicus ruber](https://en.wikipedia.org/wiki/Sphyrapicus_ruber) | Red-breasted Sapsucker | 70159 |
| 0.0648 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 261404 |
| 0.0583 | [Branta hutchinsii](https://en.wikipedia.org/wiki/Branta_hutchinsii) | Cackling Goose | 105811 |
| 0.0576 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 158394 |






### Top Species for Pennsylvania (US-PA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0312 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 171036 |
| 0.0282 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 620147 |
| 0.0254 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 557667 |
| 0.0253 | [Dumetella carolinensis](https://en.wikipedia.org/wiki/Dumetella_carolinensis) | Gray Catbird | 456717 |
| 0.0227 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 282381 |
| 0.0222 | [Melanerpes carolinus](https://en.wikipedia.org/wiki/Melanerpes_carolinus) | Red-bellied Woodpecker | 625797 |
| 0.0209 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 115306 |
| 0.0198 | [Zonotrichia albicollis](https://en.wikipedia.org/wiki/Zonotrichia_albicollis) | White-throated Sparrow | 393881 |
| 0.0196 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 544357 |
| 0.0188 | [Cardinalis cardinalis](https://en.wikipedia.org/wiki/Cardinalis_cardinalis)† | Northern Cardinal | 947363 |






### Top Species for Rhode Island (US-RI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0471 | [Cuculus canorus](https://en.wikipedia.org/wiki/Cuculus_canorus)* | Common Cuckoo | 672 |
| 0.0225 | [Phalacrocorax carbo](https://en.wikipedia.org/wiki/Phalacrocorax_carbo) | Great Cormorant | 8422 |
| 0.0182 | [Somateria mollissima](https://en.wikipedia.org/wiki/Somateria_mollissima) | Common Eider | 17732 |
| 0.0175 | [Larus marinus](https://en.wikipedia.org/wiki/Larus_marinus) | Great Black-backed Gull | 39719 |
| 0.0165 | [Xenus cinereus](https://en.wikipedia.org/wiki/Xenus_cinereus) |  | 194 |
| 0.0147 | [Ammospiza caudacuta](https://en.wikipedia.org/wiki/Ammospiza_caudacuta) | Saltmarsh Sparrow | 2966 |
| 0.0144 | [Larus argentatus](https://en.wikipedia.org/wiki/Larus_argentatus) | Herring Gull | 60029 |
| 0.0116 | [Melanitta americana](https://en.wikipedia.org/wiki/Melanitta_americana) | Black Scoter | 8733 |
| 0.0116 | [Branta bernicla](https://en.wikipedia.org/wiki/Branta_bernicla) | Brant | 9532 |
| 0.0115 | [Cygnus olor](https://en.wikipedia.org/wiki/Cygnus_olor) | Mute Swan | 18958 |






### Top Species for South Carolina (US-SC)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0408 | [Sitta pusilla](https://en.wikipedia.org/wiki/Sitta_pusilla) | Brown-headed Nuthatch | 68558 |
| 0.0331 | [Passerina ciris](https://en.wikipedia.org/wiki/Passerina_ciris) | Painted Bunting | 38067 |
| 0.0326 | [Rallus crepitans](https://en.wikipedia.org/wiki/Rallus_crepitans) | Clapper Rail | 29691 |
| 0.0303 | [Mycteria americana](https://en.wikipedia.org/wiki/Mycteria_americana) | Wood Stork | 40234 |
| 0.0291 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 230968 |
| 0.0277 | [Setophaga pinus](https://en.wikipedia.org/wiki/Setophaga_pinus) | Pine Warbler | 103051 |
| 0.0245 | [Egretta tricolor](https://en.wikipedia.org/wiki/Egretta_tricolor) | Tricolored Heron | 57484 |
| 0.0243 | [Anhinga anhinga](https://en.wikipedia.org/wiki/Anhinga_anhinga) | Anhinga | 52941 |
| 0.0224 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)‡ | Carolina Wren | 251184 |
| 0.0222 | [Quiscalus major](https://en.wikipedia.org/wiki/Quiscalus_major) | Boat-tailed Grackle | 54746 |






### Top Species for South Dakota (US-SD)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0207 | [Sturnella neglecta](https://en.wikipedia.org/wiki/Sturnella_neglecta)† | Western Meadowlark | 28423 |
| 0.0171 | [Tympanuchus phasianellus](https://en.wikipedia.org/wiki/Tympanuchus_phasianellus) | Sharp-tailed Grouse | 2538 |
| 0.0164 | [Phasianus colchicus](https://en.wikipedia.org/wiki/Phasianus_colchicus)‡* | Ring-necked Pheasant | 15094 |
| 0.0164 | [Bartramia longicauda](https://en.wikipedia.org/wiki/Bartramia_longicauda) | Upland Sandpiper | 5213 |
| 0.0124 | [Calamospiza melanocorys](https://en.wikipedia.org/wiki/Calamospiza_melanocorys)† | Lark Bunting | 3391 |
| 0.0116 | [Xanthocephalus xanthocephalus](https://en.wikipedia.org/wiki/Xanthocephalus_xanthocephalus) | Yellow-headed Blackbird | 9544 |
| 0.0102 | [Leucophaeus pipixcan](https://en.wikipedia.org/wiki/Leucophaeus_pipixcan) | Franklin's Gull | 6443 |
| 0.0093 | [Zonotrichia querula](https://en.wikipedia.org/wiki/Zonotrichia_querula) | Harris's Sparrow | 4057 |
| 0.0088 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 5601 |
| 0.0087 | [Calcarius ornatus](https://en.wikipedia.org/wiki/Calcarius_ornatus) | Chestnut-collared Longspur | 1232 |






### Top Species for Tennessee (US-TN)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0335 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 264148 |
| 0.0258 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 161073 |
| 0.0231 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 264394 |
| 0.0218 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 181101 |
| 0.0186 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 83481 |
| 0.0186 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 241408 |
| 0.0177 | [Mimus polyglottos](https://en.wikipedia.org/wiki/Mimus_polyglottos)‡ | Northern Mockingbird | 199634 |
| 0.0165 | [Toxostoma rufum](https://en.wikipedia.org/wiki/Toxostoma_rufum)† | Brown Thrasher | 87297 |
| 0.0159 | [Grus monacha](https://en.wikipedia.org/wiki/Grus_monacha) |  | 154 |
| 0.0154 | [Geothlypis formosa](https://en.wikipedia.org/wiki/Geothlypis_formosa) | Kentucky Warbler | 12863 |






### Top Species for Texas (US-TX)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.1763 | [Baeolophus atricristatus](https://en.wikipedia.org/wiki/Baeolophus_atricristatus) | Black-crested Titmouse | 365712 |
| 0.1449 | [Quiscalus mexicanus](https://en.wikipedia.org/wiki/Quiscalus_mexicanus) | Great-tailed Grackle | 794651 |
| 0.1390 | [Melanerpes aurifrons](https://en.wikipedia.org/wiki/Melanerpes_aurifrons) | Golden-fronted Woodpecker | 326325 |
| 0.1351 | [Tyrannus forficatus](https://en.wikipedia.org/wiki/Tyrannus_forficatus)† | Scissor-tailed Flycatcher | 327041 |
| 0.1340 | [Zenaida asiatica](https://en.wikipedia.org/wiki/Zenaida_asiatica) | White-winged Dove | 742445 |
| 0.1250 | [Caracara plancus](https://en.wikipedia.org/wiki/Caracara_plancus) | Crested Caracara | 249608 |
| 0.1182 | [Toxostoma longirostre](https://en.wikipedia.org/wiki/Toxostoma_longirostre) | Long-billed Thrasher | 118995 |
| 0.1114 | [Cyanocorax yncas](https://en.wikipedia.org/wiki/Cyanocorax_yncas) | Green Jay | 150450 |
| 0.1003 | [Tyrannus couchii](https://en.wikipedia.org/wiki/Tyrannus_couchii) | Couch's Kingbird | 110055 |
| 0.0986 | [Nannopterum brasilianum](https://en.wikipedia.org/wiki/Nannopterum_brasilianum) | Neotropic Cormorant | 234429 |






### Top Species for Utah (US-UT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0510 | [Aphelocoma woodhouseii](https://en.wikipedia.org/wiki/Aphelocoma_woodhouseii) | Woodhouse's Scrub-Jay | 53017 |
| 0.0468 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 129642 |
| 0.0461 | [Larus californicus](https://en.wikipedia.org/wiki/Larus_californicus)‡ | California Gull | 65861 |
| 0.0350 | [Aechmophorus clarkii](https://en.wikipedia.org/wiki/Aechmophorus_clarkii) | Clark's Grebe | 15670 |
| 0.0321 | [Alectoris chukar](https://en.wikipedia.org/wiki/Alectoris_chukar)* | Chukar | 7064 |
| 0.0306 | [Plegadis chihi](https://en.wikipedia.org/wiki/Plegadis_chihi) | White-faced Ibis | 33048 |
| 0.0301 | [Recurvirostra americana](https://en.wikipedia.org/wiki/Recurvirostra_americana) | American Avocet | 41087 |
| 0.0285 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle | 23315 |
| 0.0285 | [Spatula cyanoptera](https://en.wikipedia.org/wiki/Spatula_cyanoptera) | Cinnamon Teal | 38472 |
| 0.0284 | [Passerina amoena](https://en.wikipedia.org/wiki/Passerina_amoena) | Lazuli Bunting | 27716 |






### Top Species for Virginia (US-VA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0457 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 507768 |
| 0.0391 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 597727 |
| 0.0283 | [Sialia sialis](https://en.wikipedia.org/wiki/Sialia_sialis)† | Eastern Bluebird | 344469 |
| 0.0261 | [Corvus ossifragus](https://en.wikipedia.org/wiki/Corvus_ossifragus) | Fish Crow | 173005 |
| 0.0251 | [Corvus sp. (crow sp.)](https://en.wikipedia.org/wiki/Corvus) |  | 43910 |
| 0.0247 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 475019 |
| 0.0238 | [Empidonax virescens](https://en.wikipedia.org/wiki/Empidonax_virescens) | Acadian Flycatcher | 54363 |
| 0.0208 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 222621 |
| 0.0202 | [Coragyps atratus](https://en.wikipedia.org/wiki/Coragyps_atratus) | Black Vulture | 174913 |
| 0.0179 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker | 195902 |






### Top Species for Vermont (US-VT)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0250 | [Catharus bicknelli](https://en.wikipedia.org/wiki/Catharus_bicknelli) | Bicknell's Thrush | 3176 |
| 0.0209 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 295586 |
| 0.0170 | [Setophaga pensylvanica](https://en.wikipedia.org/wiki/Setophaga_pensylvanica) | Chestnut-sided Warbler | 44511 |
| 0.0151 | [Seiurus aurocapilla](https://en.wikipedia.org/wiki/Seiurus_aurocapilla) | Ovenbird | 56705 |
| 0.0146 | [Catharus fuscescens](https://en.wikipedia.org/wiki/Catharus_fuscescens) | Veery | 35063 |
| 0.0135 | [Troglodytes hiemalis](https://en.wikipedia.org/wiki/Troglodytes_hiemalis) | Winter Wren | 27544 |
| 0.0132 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 104397 |
| 0.0122 | [Empidonax alnorum](https://en.wikipedia.org/wiki/Empidonax_alnorum) | Alder Flycatcher | 15915 |
| 0.0122 | [Sphyrapicus varius](https://en.wikipedia.org/wiki/Sphyrapicus_varius) | Yellow-bellied Sapsucker | 46917 |
| 0.0118 | [Setophaga caerulescens](https://en.wikipedia.org/wiki/Setophaga_caerulescens) | Black-throated Blue Warbler | 25660 |






### Top Species for Washington (US-WA)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0965 | [Larus glaucescens](https://en.wikipedia.org/wiki/Larus_glaucescens) | Glaucous-winged Gull | 281727 |
| 0.0959 | [Poecile rufescens](https://en.wikipedia.org/wiki/Poecile_rufescens) | Chestnut-backed Chickadee | 268543 |
| 0.0840 | [Pipilo maculatus](https://en.wikipedia.org/wiki/Pipilo_maculatus) | Spotted Towhee | 470005 |
| 0.0825 | [Cepphus columba](https://en.wikipedia.org/wiki/Cepphus_columba) | Pigeon Guillemot | 92260 |
| 0.0796 | [Cyanocitta stelleri](https://en.wikipedia.org/wiki/Cyanocitta_stelleri) | Steller's Jay | 313794 |
| 0.0778 | [Calypte anna](https://en.wikipedia.org/wiki/Calypte_anna) | Anna's Hummingbird | 331149 |
| 0.0764 | [Cerorhinca monocerata](https://en.wikipedia.org/wiki/Cerorhinca_monocerata) | Rhinoceros Auklet | 56517 |
| 0.0764 | [Troglodytes pacificus](https://en.wikipedia.org/wiki/Troglodytes_pacificus) | Pacific Wren | 152848 |
| 0.0683 | [Zonotrichia atricapilla](https://en.wikipedia.org/wiki/Zonotrichia_atricapilla) | Golden-crowned Sparrow | 161932 |
| 0.0621 | [Tachycineta thalassina](https://en.wikipedia.org/wiki/Tachycineta_thalassina) | Violet-green Swallow | 208982 |






### Top Species for Wisconsin (US-WI)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0558 | [Antigone canadensis](https://en.wikipedia.org/wiki/Antigone_canadensis) | Sandhill Crane | 231517 |
| 0.0272 | [Parus major](https://en.wikipedia.org/wiki/Parus_major)* | Great Tit | 729 |
| 0.0254 | [Pheucticus ludovicianus](https://en.wikipedia.org/wiki/Pheucticus_ludovicianus) | Rose-breasted Grosbeak | 147827 |
| 0.0243 | [Poecile atricapillus](https://en.wikipedia.org/wiki/Poecile_atricapillus) | Black-capped Chickadee | 639564 |
| 0.0226 | [Cistothorus stellaris](https://en.wikipedia.org/wiki/Cistothorus_stellaris) | Sedge Wren | 29448 |
| 0.0212 | [Vermivora chrysoptera](https://en.wikipedia.org/wiki/Vermivora_chrysoptera) | Golden-winged Warbler | 19108 |
| 0.0211 | [Meleagris gallopavo](https://en.wikipedia.org/wiki/Meleagris_gallopavo) | Wild Turkey | 120796 |
| 0.0186 | [Dryobates villosus](https://en.wikipedia.org/wiki/Dryobates_villosus) | Hairy Woodpecker | 252839 |
| 0.0185 | [Icterus galbula](https://en.wikipedia.org/wiki/Icterus_galbula)† | Baltimore Oriole | 162685 |
| 0.0175 | [Sitta carolinensis](https://en.wikipedia.org/wiki/Sitta_carolinensis) | White-breasted Nuthatch | 416266 |






### Top Species for West Virginia (US-WV)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0124 | [Pipilo erythrophthalmus](https://en.wikipedia.org/wiki/Pipilo_erythrophthalmus) | Eastern Towhee | 51061 |
| 0.0095 | [Piranga olivacea](https://en.wikipedia.org/wiki/Piranga_olivacea) | Scarlet Tanager | 19032 |
| 0.0086 | [Hylocichla mustelina](https://en.wikipedia.org/wiki/Hylocichla_mustelina)† | Wood Thrush | 20027 |
| 0.0085 | [Setophaga cerulea](https://en.wikipedia.org/wiki/Setophaga_cerulea) | Cerulean Warbler | 3557 |
| 0.0084 | [Dryocopus pileatus](https://en.wikipedia.org/wiki/Dryocopus_pileatus) | Pileated Woodpecker | 37014 |
| 0.0081 | [Baeolophus bicolor](https://en.wikipedia.org/wiki/Baeolophus_bicolor) | Tufted Titmouse | 71638 |
| 0.0081 | [Thryothorus ludovicianus](https://en.wikipedia.org/wiki/Thryothorus_ludovicianus)† | Carolina Wren | 67983 |
| 0.0081 | [Setophaga citrina](https://en.wikipedia.org/wiki/Setophaga_citrina) | Hooded Warbler | 9288 |
| 0.0076 | [Poecile carolinensis](https://en.wikipedia.org/wiki/Poecile_carolinensis) | Carolina Chickadee | 49621 |
| 0.0074 | [Spizella pusilla](https://en.wikipedia.org/wiki/Spizella_pusilla) | Field Sparrow | 23130 |






### Top Species for Wyoming (US-WY)

| Score | Bird | Common Name | Count |
|---|---|---|---|
| 0.0328 | [Nucifraga columbiana](https://en.wikipedia.org/wiki/Nucifraga_columbiana) | Clark's Nutcracker | 14068 |
| 0.0321 | [Centrocercus urophasianus](https://en.wikipedia.org/wiki/Centrocercus_urophasianus) | Greater Sage-Grouse | 2281 |
| 0.0320 | [Sialia currucoides](https://en.wikipedia.org/wiki/Sialia_currucoides)† | Mountain Bluebird | 21085 |
| 0.0247 | [Leucosticte atrata](https://en.wikipedia.org/wiki/Leucosticte_atrata) | Black Rosy-Finch | 1876 |
| 0.0229 | [Poecile gambeli](https://en.wikipedia.org/wiki/Poecile_gambeli) | Mountain Chickadee | 25326 |
| 0.0228 | [Rhynchophanes mccownii](https://en.wikipedia.org/wiki/Rhynchophanes_mccownii) | Thick-billed Longspur | 2228 |
| 0.0218 | [Aquila chrysaetos](https://en.wikipedia.org/wiki/Aquila_chrysaetos) | Golden Eagle | 11895 |
| 0.0207 | [Oreoscoptes montanus](https://en.wikipedia.org/wiki/Oreoscoptes_montanus) | Sage Thrasher | 5825 |
| 0.0199 | [Pica hudsonia](https://en.wikipedia.org/wiki/Pica_hudsonia) | Black-billed Magpie | 38495 |
| 0.0199 | [Dendragapus obscurus](https://en.wikipedia.org/wiki/Dendragapus_obscurus) | Dusky Grouse | 2239 |






