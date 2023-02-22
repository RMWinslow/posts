---
title: Pronouncable Quinary
subtitle: A goofy quinary² numeral system where number's names are the same as their representation.
date: 2023-02-21
layout: post
parent: Numbers
---

Silly idea I just thought of while look at hex codes: 
A base-5 (or really base-25) numeral system where numerals in even positions are consonants (jklmn) and odd positions vowels (aeiou). 
Then the name of each number is the same as its representation.

Leading `j`s and `a`s are optional. So 0-4 can be `a`,`e`,`i`,`o`,`u` or `ja`,`je`,`ji`,`jo`,`ju`.


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

(Pronounce each vowel in its own syllable.)


## Converter


<fieldset>
    <legend>Converter</legend>
    <label for="digitalInput">Decimal:</label>
    <input type="number" id="digitalInput" name="digitalInput" value="" min="0" step="1" onchange="digitalValue = parseInt(this.value); updateQuinary();" /><br>
    Normal Quinary: <span id="quinaryOutput"></span> <br>
    Goofy Quinary²: <span id="goofyOutput" style="font-style: italic;"></span>
</fieldset>


<script>

vowelDict = {
    '0': 'a',
    '1': 'e',
    '2': 'i',
    '3': 'o',
    '4': 'u',
};
consonantDict = {
    '0': 'j',
    '1': 'k',
    '2': 'l',
    '3': 'm',
    '4': 'n',
};
    
var digitalValue = 0;

function updateQuinary(){
    quinary = digitalValue.toString(5);
    //console.log(quinary);
    result = "";
    for (var j=0; j < quinary.length; j++){
        if ((quinary.length - j)%2 == 0){
            result += consonantDict[quinary[j]];
        } else {
            result += vowelDict[quinary[j]];
        }
    }
    document.getElementById("quinaryOutput").innerHTML = quinary;
    document.getElementById("goofyOutput").innerHTML = result;
}
</script>




## A Senary (Base-6) Version


For the senary version, use `{aeiouy}` for even numeral positions, and `{zwthrf}` for odd numeral positions.


### Why these letters?

To do the same thing in base-6, we need a sixth vowel.
English has semivowels in `y` and `w`, so let's use the ol' "Somtimes y".

To make things less ambiguous, it may help to pronounce `y` 
[as it is pronounced in the IPA](https://en.wikipedia.org/wiki/Close_front_rounded_vowel).
In IPA, `y` represents a sort of "ew" sound, as in "few".
(In Pinyin, the same sound is written as `ü` or `v`.)

In the base-5 version, I used the first sequence of 5 back-to-back consonants in the alphabet.

But if we're using IPA,  the IPA sound `j` is written as `y` in English, so let's swap out that out as well.
Actually, if we swap out all the consonants then the two numeral systems can't contradict each other.

<aside>
The quinary and senary systems write numbers 0-4 the same way. 
The number 5 is written in the `y` senary version, and `ka` in the quinary, which are unambiguous.
And for any integer $\geq 6$, the representation contains at least one consonant.
</aside>

I'll try something else for fun. Use letters cooresponding to the sounds of each digit name.

Use `z` in place zero, `w` for one ("wun"), `t` two, `h` three, `r` four, `f` five.
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

wiki's cite:
tshrd wf

Herbert Zim
ETAON RISHD LFCMU GYPWB VKJXZQ
T     R SHD  FC   G PWB V  XZQ

 b d fgh       p rst vwx z

-->



### Base-6 Converter


<fieldset>
    <legend>Converter</legend>
    <label for="digitalInput6">Decimal:</label>
    <input type="number" id="digitalInput6" name="digitalInput6" value="" min="0" step="1" onchange="digitalValue6 = parseInt(this.value); updateSenary();" /><br>
    Normal Senary: <span id="senaryOutput"></span> <br>
    Goofy Senary²: <span id="goofyOutput6" style="font-style: italic;"></span>
</fieldset>


<script>

vowelDict6 = {
    '0': 'a',
    '1': 'e',
    '2': 'i',
    '3': 'o',
    '4': 'u',
    '5': 'y',
};
consonantDict6 = {
    '0': 'z',
    '1': 'w',
    '2': 't',
    '3': 'h',
    '4': 'r',
    '5': 'f',
};
    
var digitalValue6 = 0;

function updateSenary(){
    senary = digitalValue.toString(6);
    //console.log(quinary);
    result = "";
    for (var j=0; j < quinary.length; j++){
        if ((quinary.length - j)%2 == 0){
            result += consonantDict6[senary[j]];
        } else {
            result += vowelDict6[senary[j]];
        }
    }
    document.getElementById("senaryOutput").innerHTML = senary;
    document.getElementById("goofyOutput6").innerHTML = result;
}
</script>




