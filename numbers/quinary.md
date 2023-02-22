---
title: Silly Pronouncable Numbers
subtitle: A goofy quinary² numeral system where number's names are the same as their representation.
date: 2023-02-21
layout: post
parent: Numbers
---

Silly idea I just thought of while look at hex codes: 
A quinary² number system where numerals in even positions are consonants (jklmn) and odd positions vowels (aeiou). 
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

## Converter


<fieldset>
    <legend>Converter</legend>
    
    <div title="Height of your eyes.">
    <label for="personHeight">Decimal:</label>
    <input type="number" id="digitalInput" name="digitalInput" value="" min="0" step="1" onchange="digitalValue = parseInt(this.value); updateQuinary();" />
    </div>
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






