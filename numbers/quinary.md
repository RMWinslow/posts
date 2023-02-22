---
title: Syllabic Quinary
subtitle: A goofy quinary² numeral system where number names are the same as their numeral representation.
date: 2023-02-21
layout: post
parent: Numbers
---

Silly idea I just thought of while look at hex codes: 
A base-5 (or really base-25) numeral system where numerals in even positions are consonants (jklmn) and odd positions vowels (aeiou). 
Then the name of each number is the same as its representation.

Leading `j`s and `a`s are optional. So 0-4 can be `a`,`e`,`i`,`o`,`u` or `ja`,`je`,`ji`,`jo`,`ju`.

A similar base-6 system is also described below.


## Examples

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

(Pronounce each vowel in its own syllable. Use the IPA or Spanish pronunciation of each vowel.)


## Converter

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
    return (numberString.includes('.') ? numberString.indexOf('.') : numberString.length;); //ternary operator
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
    document.getElementById("quinaryOutput").innerHTML = quinary;
    document.getElementById("goofyOutput").innerHTML = result;
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








## A Senary (Base-6) Version


For the senary version, use `{aeiouy}` for even numeral positions, and `{zwthrf}` for odd numeral positions.


### Letter Choice

To do the same thing in base-6, we need a sixth vowel.
English has semivowels in `y` and `w`, so let's use the ol' "Somtimes y".
To make sounds less ambiguous, it may help to pronounce `y` 
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

This time, for fun, I'll use letters corresponding to the sounds of each digit name.
Use `z` in place of zero, `w` for one ("wun"), `t` two, `h` three, `r` four, `f` five.
(I thought about using `f` for four and `v` for five, but `f` and `v` sound too similar.)


<!--
rst vw z

zero z
one w
two t
three h
four
five

z, w, t, r, f, v
zwtsrf

ar san 

rtsdp
srtdgphbfv

wikis cite:
tshrd wf

Herbert Zim
ETAON RISHD LFCMU GYPWB VKJXZQ
T     R SHD  FC   G PWB V  XZQ

 b d fgh       p rst vwx z

-->



### Base-6 Converter

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
    '0': 'z',
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
            result += consonantDict6[c]] || c;
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




