---
title: Syllabic Quinary
subtitle: A goofy quinary² numeral system where number names are the same as their numeral representation.
date: 2023-02-21
layout: post
parent: Language
toc: true
---

Silly idea I just thought of while look at hex codes: 
A numeral system where numerals in even positions are consonants and odd positions vowels. 
Then the name of each number is the same as its numeral representation.

<!--There are typically said to be five or six vowels in the English Alphabet-->
Base-5 and Base-6 versions are described below.

I'm calling these "syllabic" numeral systems each pair of numerals can be 
represented by a distinct syllable.


## Syllabic Quinary (Base-5²)

In this base-5 (or arguably base-25) system, 
even numerals positions use the consonants `{j,k,l,m,n}` and odd positions use the vowels `{a,e,i,o,u}`. 
Then the name of each number is the same as its representation.

Leading `j`s and `a`s are optional. So 0-4 can be `a`,`e`,`i`,`o`,`u` or `ja`,`je`,`ji`,`jo`,`ju`.


### Base-5² Examples

0 is `a` or `ja`. The next 150 numbers are as follows:

```
1-10:       e,    i,    o,    u,   ka,   ke,   ki,   ko,   ku,   la, 
11-20:     le,   li,   lo,   lu,   ma,   me,   mi,   mo,   mu,   na, 
21-30:     ne,   ni,   no,   nu,  eja,  eje,  eji,  ejo,  eju,  eka, 
31-40:    eke,  eki,  eko,  eku,  ela,  ele,  eli,  elo,  elu,  ema, 
41-50:    eme,  emi,  emo,  emu,  ena,  ene,  eni,  eno,  enu,  ija, 
51-60:    ije,  iji,  ijo,  iju,  ika,  ike,  iki,  iko,  iku,  ila, 
61-70:    ile,  ili,  ilo,  ilu,  ima,  ime,  imi,  imo,  imu,  ina, 
71-80:    ine,  ini,  ino,  inu,  oja,  oje,  oji,  ojo,  oju,  oka, 
81-90:    oke,  oki,  oko,  oku,  ola,  ole,  oli,  olo,  olu,  oma, 
91-100:   ome,  omi,  omo,  omu,  ona,  one,  oni,  ono,  onu,  uja, 
101-110:  uje,  uji,  ujo,  uju,  uka,  uke,  uki,  uko,  uku,  ula, 
111-120:  ule,  uli,  ulo,  ulu,  uma,  ume,  umi,  umo,  umu,  una, 
121-130:  une,  uni,  uno,  unu, kaja, kaje, kaji, kajo, kaju, kaka, 
131-140: kake, kaki, kako, kaku, kala, kale, kali, kalo, kalu, kama, 
141-150: kame, kami, kamo, kamu, kana, kane, kani, kano, kanu, keja
```

(Pronounce each vowel in its own syllable. I suggest using the Spanish pronunciation of each vowel, which coincide with the IPA pronunciations. For the pronunciation of `j`, just follow your heart.)


### Base-5² Converter

<fieldset>
    <legend>Decimal to Syllabic Quinary</legend>
    Decimal: <input type="number" id="decToQuinInput" step="1" onchange="decToQuinUpdate(parseInt(this.value));" /><br>
    Normal Quinary: <span id="decToQuinIntermediate"></span><br>
    Syllabic Quinary²: <span id="decToQuinOutput" style="font-style: italic;"></span>
</fieldset>

<fieldset>
    <legend>Syllabic Quinary to Decimal</legend>
    Syllabic Senary²: <input type="text" id="quinToDecInput" onchange="quinToDecUpdate(this.value);" /><br>
    Normal Senary: <span id="quinToDecIntermediate"></span><br>
    Decimal: <span id="quinToDecOutput" style="font-style: italic;"></span>
</fieldset>

<script>
function getAnchorPoint(numberString) {
    return (numberString.includes('.') ? numberString.indexOf('.') : numberString.length); //ternary operator
}

vowelDict5 = {
    '0': 'a',
    '1': 'e',
    '2': 'i',
    '3': 'o',
    '4': 'u',
};
consonantDict5 = {
    '0': 'j',
    '1': 'k',
    '2': 'l',
    '3': 'm',
    '4': 'n',
};
var reverseQuinaryDict = {};
for (const [key, value] of Object.entries(vowelDict5))     {reverseQuinaryDict[value] = key;}
for (const [key, value] of Object.entries(consonantDict5)) {reverseQuinaryDict[value] = key;}

function decimalToGoofySenary(digitalValue){
    quinary = digitalValue.toString(5);
    result = "";
    anchor = getAnchorPoint(quinary);
    for (var j=0; j < quinary.length; j++){
        c = quinary[j];
        if ((anchor - j)%2 == 0){
            result += consonantDict5[c] || c;
        } else {
            result += vowelDict5[c] || c;
        }
    }
    return result;
}

function goofyQuinaryToQuinary(goofyQuinaryString){
    quinary = "";
    for (c of goofyQuinaryString){quinary += reverseQuinaryDict[c] || c;}
    return quinary;
} 
function goofyQuinaryToDecimal(goofyQuinaryString){
    return parseInt(goofyQuinaryToQuinary(goofyQuinaryString), 5);
}

function decimalToGoofyQuinary(digitalValue){
    quinary = digitalValue.toString(5);
    result = "";
    for (var j=0; j < quinary.length; j++){
        if ((quinary.length - j)%2 == 0){
            result += consonantDict5[quinary[j]];
        } else {
            result += vowelDict5[quinary[j]];
        }
    }
    return result;
}

function decToQuinUpdate(decimal5Input){
    document.getElementById("decToQuinIntermediate").textContent = decimal5Input.toString(5);
    document.getElementById("decToQuinOutput").textContent = decimalToGoofyQuinary(decimal5Input);
}
function quinToDecUpdate(quinaryInput){
    document.getElementById("quinToDecIntermediate").textContent = goofySenaryToSenary(quinaryInput);
    document.getElementById("quinToDecOutput").textContent = goofyQuinaryToDecimal(quinaryInput);
}
</script>








## Syllabic Senary (Base-6²)


For the senary version, use `{a,e,i,o,u,y}` for even numeral positions, and `{s,w,t,h,r,f}` for odd numeral positions.


### Why These Letters?

To do this thing in base-6, we need a sixth vowel.
English has semivowels `y` and `w`, so let's use the ol' "Sometimes y" as vowel number 6.
To make the sounds less ambiguous, it may help to pronounce `y` 
[as it is pronounced in the IPA](https://en.wikipedia.org/wiki/Close_front_rounded_vowel).
In IPA, `y` represents a sort of "ew" sound, as in "few".
(In Pinyin, the same sound is written as `ü` or `v`.)

In the base-5 version, I used the first sequence of 5 back-to-back consonants in the alphabet.
But if we're using IPA, the IPA sound `j` is written as `y` in English, so let's swap out that out as well.
Actually, let's just swap out all the consonants.

<aside>
If we swap out all the consonants then the two numeral systems avoid cross-ambiguity, as least for the integers.
The quinary and senary systems write numbers 0-4 the same way. (That's fine. Most numeral systems write 1 the same way.)
The number 5 is written `y` in the senary version, and `ka` in the quinary, which are unambiguous.
And for any integer ≥ 6, each representation contains at least one consonant.
</aside>

This time, I chose a consonant set which can be used to make many common english words. The best option was `{swthrf}`.[^corpusSource]

[^corpusSource]: I looked at words appearing in the *Brown Corpus* (W. N. Francis and H. Kucera, 1979), as distributed in the Natural Language Toolkit (nltk) library for python. For each set of 6 consonants, I looked at the total count of words in the corpus which contain only those consonants (along with vowels, including `y`). Excluding any of `{jklmn}` from consideration, the consonant set `{fhrstw}` results in the highest total word count. 
    
    Looking only at words which alternate between consonant and vowel, the result is the same: `{fhrstw}`
    Looking only at words which alternate between consonant and vowel *and which begin or end with a vowel*, the result is `{bfhrst}`.

<!--Using the nltk Gutenberg corpus yields the same result: `fhrstw`. Using the Reuters corpus gives `dfhrst` as the best result. And the NPS Chat corpus gives `hprstw`.

Allowing for all consonants, the best set would be dhnrst, fnrstw if we alternate vowels/consonants, or bfnrst with alternation and begin/end with vowel
-->


<aside>
What's the longest English word that could be written as a number in this system?
With the consonants `{swthrf}`, the longest word I've found is "heretofore".
Using any set of 6 consonants: "unimaginatively".
Using the numerals in the Quinary system above, it's a tie between "linelike", "limonene", and "kakemono".
</aside>

<!--
unimaginatively
[('uninominal', {'l', 'm', 'n'}, 10),
 ('linelike', {'k', 'l', 'n'}, 8),
 ('aluminum', {'l', 'm', 'n'}, 8),
 ('kakemono', {'k', 'm', 'n'}, 8),
 ('limonene', {'l', 'm', 'n'}, 8),
[('supererogatory', {'g', 'p', 'r', 's', 't'}, 14),
 ('heterozygosity', {'g', 'h', 'r', 's', 't', 'z'}, 14),
 ('caricatured', {'c', 'd', 'r', 't'}, 11),
 ('ivy-covered', {'c', 'd', 'r', 'v'}, 11),
 ('categorized', {'c', 'd', 'g', 'r', 't', 'z'}, 11),
 ('evaporative', {'p', 'r', 't', 'v'}, 11),
 ('redecorated', {'c', 'd', 'r', 't'}, 11),
with aeiou+fnrst:
[('anatotitan', {'n', 't'}, 10),
 ('ureteritis', {'r', 's', 't'}, 10),
 ('resonator', {'n', 'r', 's', 't'}, 9),
 ('retinitis', {'n', 'r', 's', 't'}, 9),
 ('serotonin', {'n', 'r', 's', 't'}, 9),

https://www.nltk.org/book/ch02.html
http://www.nltk.org/nltk_data/
-->




I've mapped them to the digits like so:
`s` is mapped to zero (because `s` and `z` sound similar), `w` to one ("wan"), `t` **t**wo, `h` t**h**ree, `r` fou**r**, `f` **f**ive.
<!--(I thought about using `f` for four and `v` for five, but `f` and `v` sound too similar.)-->


### Base-6² Examples

0 is `a` or `sa`.

The next 150 numbers are as follows:

```
1-10:        e,    i,    o,    u,    y,   wa,   we,   wi,   wo,   wu,
11-20:      wy,   ta,   te,   ti,   to,   tu,   ty,   ha,   he,   hi,
21-30:      ho,   hu,   hy,   ra,   re,   ri,   ro,   ru,   ry,   fa,
31-40:      fe,   fi,   fo,   fu,   fy,  esa,  ese,  esi,  eso,  esu,
41-50:     esy,  ewa,  ewe,  ewi,  ewo,  ewu,  ewy,  eta,  ete,  eti,
51-60:     eto,  etu,  ety,  eha,  ehe,  ehi,  eho,  ehu,  ehy,  era,
61-70:     ere,  eri,  ero,  eru,  ery,  efa,  efe,  efi,  efo,  efu,
71-80:     efy,  isa,  ise,  isi,  iso,  isu,  isy,  iwa,  iwe,  iwi,
81-90:     iwo,  iwu,  iwy,  ita,  ite,  iti,  ito,  itu,  ity,  iha,
91-100:    ihe,  ihi,  iho,  ihu,  ihy,  ira,  ire,  iri,  iro,  iru,
101-110:   iry,  ifa,  ife,  ifi,  ifo,  ifu,  ify,  osa,  ose,  osi,
111-120:   oso,  osu,  osy,  owa,  owe,  owi,  owo,  owu,  owy,  ota,
121-130:   ote,  oti,  oto,  otu,  oty,  oha,  ohe,  ohi,  oho,  ohu,
131-140:   ohy,  ora,  ore,  ori,  oro,  oru,  ory,  ofa,  ofe,  ofi,
141-150:   ofo,  ofu,  ofy,  usa,  use,  usi,  uso,  usu,  usy,  uwa,
151-160:   uwe,  uwi,  uwo,  uwu,  uwy,  uta,  ute,  uti,  uto,  utu,
161-170:   uty,  uha,  uhe,  uhi,  uho,  uhu,  uhy,  ura,  ure,  uri,
171-180:   uro,  uru,  ury,  ufa,  ufe,  ufi,  ufo,  ufu,  ufy,  ysa,
181-190:   yse,  ysi,  yso,  ysu,  ysy,  ywa,  ywe,  ywi,  ywo,  ywu,
191-200:   ywy,  yta,  yte,  yti,  yto,  ytu,  yty,  yha,  yhe,  yhi,
201-210:   yho,  yhu,  yhy,  yra,  yre,  yri,  yro,  yru,  yry,  yfa,
211-220:   yfe,  yfi,  yfo,  yfu,  yfy, wasa, wase, wasi, waso, wasu,
221-230:  wasy, wawa, wawe, wawi, wawo, wawu, wawy, wata, wate, wati,
231-240:  wato, watu, waty, waha, wahe, wahi, waho, wahu, wahy, wara,
241-250:  ware, wari, waro, waru, wary, wafa, wafe, wafi, wafo, wafu,
251-260:  wafy, wesa, wese, wesi, weso, wesu, wesy, wewa, wewe, wewi,
261-270:  wewo, wewu, wewy, weta, wete, weti, weto, wetu, wety, weha,
271-280:  wehe, wehi, weho, wehu, wehy, wera, were, weri, wero, weru,
281-290:  wery, wefa, wefe, wefi, wefo, wefu, wefy, wisa, wise, wisi,
291-300:  wiso, wisu, wisy, wiwa, wiwe, wiwi, wiwo, wiwu, wiwy, wita,
```


<!--
mystring="";
for (var i=0; i<301; i++){
        ss = decimalToGoofySenary(i);
        mystring += ss.padStart(5);
    mystring += ',';
    if (i%10 == 0){
        mystring += "\n";
        mystring += (i+1).toString();
        mystring += "-";
        mystring += (i+10).toString();
        mystring += ": ";
    }
}
alert(mystring);
-->




### Base-6² Converter

<fieldset>
    <legend>Decimal to Syllabic Senary</legend>
    Decimal: <input type="number" id="decToSenInput" step="1" onchange="decToSenUpdate(parseInt(this.value));" /><br>
    Normal Senary: <span id="decToSenIntermediate"></span><br>
    Syllabic Senary²: <span id="decToSenOutput" style="font-style: italic;"></span>
</fieldset>

<fieldset>
    <legend>Syllabic Senary to Decimal</legend>
    Syllabic Senary²: <input type="text" id="senToDecInput" onchange="senToDecUpdate(this.value);" /><br>
    Normal Senary: <span id="senToDecIntermediate"></span><br>
    Decimal: <span id="senToDecOutput" style="font-style: italic;"></span>
</fieldset>

<script>
const vowelDict6 = {
    '0': 'a',
    '1': 'e',
    '2': 'i',
    '3': 'o',
    '4': 'u',
    '5': 'y',
};
const consonantDict6 = {
    '0': 's',
    '1': 'w',
    '2': 't',
    '3': 'h',
    '4': 'r',
    '5': 'f',
};
var reverseSenaryDict = {};
for (const [key, value] of Object.entries(vowelDict6))     {reverseSenaryDict[value] = key;}
for (const [key, value] of Object.entries(consonantDict6)) {reverseSenaryDict[value] = key;}

function decimalToGoofySenary(digitalValue){
    senary = digitalValue.toString(6);
    result = "";
    anchor = getAnchorPoint(senary);
    for (var j=0; j < senary.length; j++){
        c = senary[j];
        if ((anchor - j)%2 == 0){
            result += consonantDict6[c] || c;
        } else {
            result += vowelDict6[c] || c;
        }
    }
    return result
}

function goofySenaryToSenary(goofySenaryString){
    //console.log(quinary);
    senary = "";
    for (c of goofySenaryString){senary += reverseSenaryDict[c] || c;}
    return senary;
} 
function goofySenaryToDecimal(goofySenaryString){
    return parseInt(goofySenaryToSenary(goofySenaryString), 6);
}

function decToSenUpdate(decimal6Input){
    document.getElementById("decToSenIntermediate").textContent = decimal6Input.toString(6);
    document.getElementById("decToSenOutput").textContent = decimalToGoofySenary(decimal6Input);
}
function senToDecUpdate(senaryInput){
    document.getElementById("senToDecIntermediate").textContent = goofySenaryToSenary(senaryInput);
    document.getElementById("senToDecOutput").textContent = goofySenaryToDecimal(senaryInput);
}
</script>








