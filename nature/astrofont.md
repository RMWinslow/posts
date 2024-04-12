---
title: Astro Fonts
subtitle: A font which uses ligatures to encode symbols for the major moons.
parent: Astro Symbols
grand_parent: Science and Nature
layout: post
date: 2022-09-24
last_modified_date: 2022-09-28
toc: true
---

## Astromoony Font

I created a font that uses ligatures to include symbols for the moons.
For example, "♂I" will be rendered as a symbol for Phobos, the first moon of Mars.

<!--TODO: Details about copyright and credit-->

### Download

[Sans Serif v1.2]({{site.webfontdirectory}}/astro/AstromoonySans.ttf) ([Github Repo](https://github.com/RobertWinslow/Astromoony-Font))


### Table of Characters

<style>
    @font-face {
        font-family: Astromoony;
        src: url("{{site.webfontdirectory}}/astro/AstromoonySans.ttf");
    }
    .AstroFontTable td {
        vertical-align: middle;
        padding: 0 0.4rem
    }
    .AstroFontTable td:nth-child(1) {
        font-family: Astromoony;
        text-align: center;
        font-size: x-large;
    }
    .AstroFontTable td:nth-child(2) {
        text-align: left;
    }
    .AstroFontTable td:nth-child(3), .AstroFontTable td:nth-child(4) {
        text-align: center;
    }
    .MoonRow {
        background-color: var(--boxcolor);
    }
</style>

<table class="AstroFontTable">
    <thead>
    <tr>
        <th>Symbol</th>
        <th>Object Name</th>
        <th>No Font</th>
        <th>Codepoint(s)</th>
    </tr>
    </thead>
    <tbody>
        <tr class="MajorPlanetRow">
            <td>☉︎</td>
            <td>Sol, The Sun</td>
            <td>☉︎</td>
            <td>2609</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>☿</td>
            <td>Mercury</td>
            <td>☿</td>
            <td>263F</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♀</td>
            <td>Venus</td>
            <td>♀</td>
            <td>2640</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>🜨</td>
            <td>Terra, The Earth</td>
            <td>🜨</td>
            <td>1F728</td>
        </tr>
        <tr class="MoonRow">
            <td>☾</td>
            <td>Luna, The Moon (Terra I)</td>
            <td>☾</td>
            <td>263e</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♁</td>
            <td>Terra (Alternate)</td>
            <td>♁</td>
            <td>2641</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♂</td>
            <td>Mars</td>
            <td>♂</td>
            <td>2642</td>
        </tr>
        <tr class="MoonRow">
            <td>♂I</td>
            <td>Phobos (Mars I)</td>
            <td>♂I</td>
            <td>2642-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♂II</td>
            <td>Deimos (Mars II)</td>
            <td>♂II</td>
            <td>2642-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⚳</td>
            <td>Ceres</td>
            <td>⚳</td>
            <td>26B3</td>
        </tr>
        <tr class="MinorPlanetRow">
            <td>⚴</td>
            <td>2 Pallas</td>
            <td>⚴</td>
            <td>26B4</td>
        </tr>
        <tr class="MinorPlanetRow">
            <td>⚵</td>
            <td>3 Juno</td>
            <td>⚵</td>
            <td>26B5</td>
        </tr>
        <tr class="MinorPlanetRow">
            <td>⚶</td>
            <td>4 Vesta</td>
            <td>⚶</td>
            <td>26B6</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♃</td>
            <td>Jupiter</td>
            <td>♃</td>
            <td>2643</td>
        </tr>
        <tr class="MoonRow">
            <td>♃I</td>
            <td>Io (Jupiter I)</td>
            <td>♃I</td>
            <td>2643-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♃II</td>
            <td>Europa (Jupiter II)</td>
            <td>♃II</td>
            <td>2643-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♃III</td>
            <td>Ganymede (Jupiter III)</td>
            <td>♃III</td>
            <td>2643-49-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♃IV</td>
            <td>Callisto (Jupiter IV)</td>
            <td>♃IV</td>
            <td>2643-49-56</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♄</td>
            <td>Saturn</td>
            <td>♄</td>
            <td>2644</td>
        </tr>
        <tr class="MoonRow">
            <td>♄I</td>
            <td>Mimas (Saturn I)</td>
            <td>♄I</td>
            <td>2644-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♄II</td>
            <td>Enceladus (Saturn II)</td>
            <td>♄II</td>
            <td>2644-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♄III</td>
            <td>Tethys (Saturn III)</td>
            <td>♄III</td>
            <td>2644-49-49-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♄IV</td>
            <td>Dione (Saturn IV)</td>
            <td>♄IV</td>
            <td>2644-49-56</td>
        </tr>
        <tr class="MoonRow">
            <td>♄V</td>
            <td>Rhea (Saturn V)</td>
            <td>♄V</td>
            <td>2644-56</td>
        </tr>
        <tr class="MoonRow">
            <td>♄VI</td>
            <td>Titan (Saturn VI)</td>
            <td>♄VI</td>
            <td>2644-56-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♄VII</td>
            <td>Hyperion (Saturn VII)</td>
            <td>♄VII</td>
            <td>2644-56-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♄VIII</td>
            <td>Iapetus (Saturn VIII)</td>
            <td>♄VIII</td>
            <td>2644-56-49-49-49</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♅</td>
            <td>Uranus</td>
            <td>♅</td>
            <td>2645</td>
        </tr>
        <tr class="MoonRow">
            <td>♅V</td>
            <td>Miranda (Uranus V)</td>
            <td>♅V</td>
            <td>2645-56</td>
        </tr>
        <tr class="MoonRow">
            <td>♅I</td>
            <td>Ariel (Uranus I)</td>
            <td>♅I</td>
            <td>2645-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♅II</td>
            <td>Umbriel (Uranus II)</td>
            <td>♅II</td>
            <td>2645-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♅III</td>
            <td>Titania (Uranus III)</td>
            <td>♅III</td>
            <td>2645-49-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♅IV</td>
            <td>Oberon (Uranus IV)</td>
            <td>♅IV</td>
            <td>2645-49-56</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>⛢</td>
            <td>Uranus (Alternate)</td>
            <td>⛢</td>
            <td>26E2</td>
        </tr>
        <tr class="MoonRow">
            <td>⛢V</td>
            <td>Miranda (Uranus V) (Alternate)</td>
            <td>⛢V</td>
            <td>26E2-56</td>
        </tr>
        <tr class="MoonRow">
            <td>⛢I</td>
            <td>Ariel (Uranus I) (Alternate)</td>
            <td>⛢I</td>
            <td>26E2-49</td>
        </tr>
        <tr class="MoonRow">
            <td>⛢II</td>
            <td>Umbriel (Uranus II) (Alternate)</td>
            <td>⛢II</td>
            <td>26E2-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>⛢III</td>
            <td>Titania (Uranus III) (Alternate)</td>
            <td>⛢III</td>
            <td>26E2-49-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>⛢IV</td>
            <td>Oberon (Uranus IV) (Alternate)</td>
            <td>⛢IV</td>
            <td>26E2-49-56</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>♆</td>
            <td>Neptune</td>
            <td>♆</td>
            <td>2646</td>
        </tr>
        <tr class="MoonRow">
            <td>♆I</td>
            <td>Triton (Neptune I)</td>
            <td>♆I</td>
            <td>2645-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♆II</td>
            <td>Nereid (Neptune II)</td>
            <td>♆II</td>
            <td>2645-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♆VIII</td>
            <td>Proteus (Neptune VIII)</td>
            <td>♆VIII</td>
            <td>2645-56-49-49-49</td>
        </tr>
        <tr class="MajorPlanetRow">
            <td>⯉</td>
            <td>Neptune (Alternate)</td>
            <td>⯉</td>
            <td>2BC9</td>
        </tr>
        <tr class="MoonRow">
            <td>⯉I</td>
            <td>Triton (Neptune I) (Alternate)</td>
            <td>⯉I</td>
            <td>2BC9-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>🝿</td>
            <td>Orcus</td>
            <td>🝿</td>
            <td>1F77F</td>
        </tr>
        <tr class="MoonRow">
            <td>🝿I</td>
            <td>Vanth (Orcus I)</td>
            <td>🝿I</td>
            <td>1F77F-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>♇</td>
            <td>Pluto</td>
            <td>♇</td>
            <td>2647</td>
        </tr>
        <tr class="MoonRow">
            <td>♇I</td>
            <td>Charon (Pluto I)</td>
            <td>♇I</td>
            <td>2647-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♇V</td>
            <td>Styx (Pluto V)</td>
            <td>♇V</td>
            <td>2647-56</td>
        </tr>
        <tr class="MoonRow">
            <td>♇II</td>
            <td>Nix (Pluto II)</td>
            <td>♇II</td>
            <td>2647-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>♇IV</td>
            <td>Kerberos (Pluto IV)</td>
            <td>♇IV</td>
            <td>2647-49-56</td>
        </tr>
        <tr class="MoonRow">
            <td>♇III</td>
            <td>Hydra (Pluto III)</td>
            <td>♇III</td>
            <td>2647-49-49-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯓</td>
            <td>Pluto (Alternate)</td>
            <td>⯓</td>
            <td>2BD3</td>
        </tr>
        <tr class="MoonRow">
            <td>⯓I</td>
            <td>Charon (Pluto I) (Alternate)</td>
            <td>⯓I</td>
            <td>2BD3-49</td>
        </tr>
        <tr class="MoonRow">
            <td>⯓V</td>
            <td>Styx (Pluto V) (Alternate)</td>
            <td>⯓V</td>
            <td>2BD3-56</td>
        </tr>
        <tr class="MoonRow">
            <td>⯓II</td>
            <td>Nix (Pluto II) (Alternate)</td>
            <td>⯓II</td>
            <td>2BD3-49-49</td>
        </tr>
        <tr class="MoonRow">
            <td>⯓IV</td>
            <td>Kerberos (Pluto IV) (Alternate)</td>
            <td>⯓IV</td>
            <td>2BD3-49-56</td>
        </tr>
        <tr class="MoonRow">
            <td>⯓III</td>
            <td>Hydra (Pluto III) (Alternate)</td>
            <td>⯓III</td>
            <td>2BD3-49-49-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯔</td>
            <td>Pluto (Alternate)</td>
            <td>⯔</td>
            <td>2BD4</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯕</td>
            <td>Pluto (Alternate)</td>
            <td>⯕</td>
            <td>2BD5</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯖</td>
            <td>Pluto (Alternate)</td>
            <td>⯖</td>
            <td>2BD6-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>🝻</td>
            <td>Haumea</td>
            <td>🝻</td>
            <td>1F77B</td>
        </tr>
        <tr class="MoonRow">
            <td>🝻I</td>
            <td>Hi'iaka (Haumea I)</td>
            <td>🝻I</td>
            <td>1F77B</td>
        </tr>
        <tr class="MoonRow">
            <td>🝻II</td>
            <td>Namaka (Haumea II)</td>
            <td>🝻II</td>
            <td>1F77B</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>🝾</td>
            <td>Quaoar</td>
            <td>🝾</td>
            <td>1F77E</td>
        </tr>
        <tr class="MoonRow">
            <td>🝾I</td>
            <td>Weywot (Quaoar I)</td>
            <td>🝾I</td>
            <td>1F77E-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>🝼</td>
            <td>Makemake</td>
            <td>🝼</td>
            <td>1F77C</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>🝽</td>
            <td>Gonggong</td>
            <td>🝽</td>
            <td>1F77D</td>
        </tr>
        <tr class="MoonRow">
            <td>🝽I</td>
            <td>Xiangliu (Gonggong I)</td>
            <td>🝽I</td>
            <td>1F77D-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯰</td>
            <td>Eris</td>
            <td>⯰</td>
            <td>2BF0</td>
        </tr>
        <tr class="MoonRow">
            <td>⯰I</td>
            <td>Dysnomia (Eris I)</td>
            <td>⯰I</td>
            <td>2BF0-49</td>
        </tr>
        <tr class="DwarfPlanetRow">
            <td>⯲</td>
            <td>Sedna</td>
            <td>⯲</td>
            <td>2BF2</td>
        </tr>
        <tr class="LetterRow">
            <td>I</td>
            <td>Capital Letter I (for ligatures)</td>
            <td>I</td>
            <td>49</td>
        </tr>
        <tr class="LetterRow">
            <td>V</td>
            <td>Capital Letter V (for ligatures)</td>
            <td>V</td>
            <td>56</td>
        </tr>
    </tbody>
</table>

### Symbol Credit

Most of the modern designs above (for dwarf planets and major moons) are based on the public-domain symbol 
[designs by Denis Moskowitz](https://suberic.net/~dmm/astro/index.html).
Note that my glyphs for some objects (namely Europa, Ganymede, Callisto, Kerberos, and Orcus)
are substantial deviations from Moskowitz' designs, though they still keep to the 'core idea' of his designs.

## Other Fonts

The [Catrinity Font](https://catrinity-font.de/index.html) by Alexander Lange contains all official unicode astro symbols, as well as a large number of asteroid symbols in its Private-Use-Area.
When making the glyphs in the Astromoony Sans font,  I designed them to be stylistically similar to the astro symbols from Catrinity.

