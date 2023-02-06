---
title: The Universal Color Language
subtitle: A table of hexadecimal color codes roughly corresponding to the ISCC–NBS System of Color Designation.
parent: Art and Culture
date: 2021-02-15
last_modified_date: 2023-02-06
table_wrappers: false
---






The [ISCC–NBS System of Color Designation](https://en.wikipedia.org/wiki/ISCC%E2%80%93NBS_system) is an attempt to build a dictionary of surface colors by combining basic color names with adjectives.
It was described by the National Bureau of Standards in the 1976 publication [Color: Universal Language and Dictionary of Names](https://archive.org/details/coloruniversalla00kell/page/50/mode/2up)
The system is meant to be perceptually uniform and is based on the [Munsell color system](https://en.wikipedia.org/wiki/Munsell_color_system), which describes colors in terms of hue, chroma, and value.
<!--As perceptually uniform color spaces, these systems has been largely superseded by work by the <a href="https://en.wikipedia.org/wiki/International_Commission_on_Illumination">the CIE</a>.
But I really enjoy the adjective+base color names in the NBS system.-->

Below, I've reproduced some tables of hexidecimal color codes from various attempts to convert this system to sRGB






  <style>
    .colorTable {
        border-collapse:collapse;
        border-color: #0000;
        margin-left: auto;
        margin-right: auto;
    }
    .colorTable td {
        padding: 0.25rem;
        text-align: center;
        font-size: small;
        color: black;
        border: none;
        vertical-align: middle;
        line-height: 1;
    }
    .colorTable th {
        padding: 0.25rem;
        text-align: center;
        font-size: small;
        vertical-align: middle;
        line-height: 1;
    }

    .colorcol {
        width: 6rem;
    }
    .spacer {
        width: 0px ;
    }

    .dark-mode .colorTable{
        background-color: black;
        color: white;
    }
    .bright-mode .colorTable{
        background-color: white;
        color: black;
    }
    .dark-text .colorTable td {
        color:white;
    }
    .invis-text .colorTable td {
        color: rgba(0, 0, 0, 0);
    }
    .no-border .colorTable {
        border-collapse:separate;
    }
</style>






## Paul Centore's sRGB Conversion (2016)

Paul Centore constructed a set of representative RGB values for each of the colors in the ISCC-NBS system.
The details are <a href="https://www.munsellcolourscienceforpainters.com/ISCCNBS/ISCCNBSSystem.html">here</a>, 
the text file of color codes is <a href="https://www.munsellcolourscienceforpainters.com/MunsellAndKubelkaMunkToolbox/MunsellAndKubelkaMunkToolboxFeb2017/DataFiles/sRGBcentroidsForISCCNBS.txt">here</a>,
and a set of data files can be found <a href="https://munsellcolourscienceforpainters.com/MunsellAndKubelkaMunkToolbox/MunsellAndKubelkaMunkToolbox.html">here</a>.

### My slightly modified version

I'm using this as a pallette of colors, so I've made a few tweaks to make the table more compact and consistent. Details below.



Table Display options:
<button onclick='nightmode()'>Darken BG</button>
<button onclick='brightmode()'>Brighten BG</button>
<button onclick='nighttext()'>Invert Text</button>
<button onclick='invisitext()'>Hide Text</button>
<button onclick='tightentable()'>Table Spacing</button>
<script>
    function nightmode(){
        document.body.classList.remove("bright-mode")
        document.body.classList.toggle("dark-mode")
    }
    function brightmode(){
        document.body.classList.remove("dark-mode")
        document.body.classList.toggle("bright-mode")
    }
    function nighttext(){
        document.body.classList.toggle("dark-text")
    }
    function invisitext(){
        document.body.classList.toggle("invis-text")
    }
    function tightentable(){
        document.body.classList.toggle("no-border")
    }
</script>

<!--


    console.log("AAAAAAA");
    document.documentElement.style.setProperty('--bordercolor', 'red');
    localStorage.setItem("prefers-color-scheme", "dark");
    console.log("AAAAAAA");
-->


<table class="colorTable" border="1"><col><col class="colorcol"><col class="spacer"><col class="colorcol"><col class="spacer"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="spacer"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="spacer"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol">
<tr><th></th><th>luminous</th><th></th><th>vivid</th><th></th><th>brilliant</th><th>strong</th><th>deep</th><th>very deep</th><th></th><th>very light</th><th>light</th><th>moderate</th><th>dark</th><th>very dark</th><th></th><th>very pale</th><th>pale</th><th>grayish</th><th>dark grayish</th><th>blackish</th></tr>
<tr><th>red</th><td bgcolor="#ff0039">※<br>#ff0039</td><td></td><td bgcolor="#d51c3c">11<br>#d51c3c</td><td></td><td></td><td bgcolor="#bf344b">12<br>#bf344b</td><td bgcolor="#87122d">13<br>#87122d</td><td bgcolor="#5c0625">14<br>#5c0625</td><td></td><td></td><td></td><td bgcolor="#b14955">15<br>#b14955</td><td bgcolor="#742434">16<br>#742434</td><td bgcolor="#481127">17<br>#481127</td><td></td><td></td><td bgcolor="#b4888d">18*<br>#b4888d</td><td bgcolor="#985d62">19<br>#985d62</td><td bgcolor="#53383e">20<br>#53383e</td><td bgcolor="#332127">21<br>#332127</td></tr>
<tr><th>reddish orange</th><td bgcolor="#ff5b00">※<br>#ff5b00</td><td></td><td bgcolor="#e83b1b">34<br>#e83b1b</td><td></td><td></td><td bgcolor="#db5d3b">35<br>#db5d3b</td><td bgcolor="#af3318">36<br>#af3318</td><td></td><td></td><td></td><td></td><td bgcolor="#cd6952">37<br>#cd6952</td><td bgcolor="#a2402b">38<br>#a2402b</td><td></td><td></td><td></td><td></td><td bgcolor="#b97565">39<br>#b97565</td><td></td><td></td></tr>
<tr><th>orange</th><td bgcolor="#ff7f00">※<br>#ff7f00</td><td></td><td bgcolor="#f7760b">48<br>#f7760b</td><td></td><td bgcolor="#ff9d50">49†<br>#ff9d50</td><td bgcolor="#ea8127">50<br>#ea8127</td><td bgcolor="#c26012">51<br>#c26012</td><td></td><td></td><td></td><td bgcolor="#fbaf82">52<br>#fbaf82</td><td bgcolor="#de8d5c">53<br>#de8d5c</td><td bgcolor="#b26633">54*<br>#b26633</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>orange yellow</th><td bgcolor="#ffa300">※<br>#ffa300</td><td></td><td bgcolor="#f39e11">66†<br>#f39e11</td><td></td><td bgcolor="#ffbe50">67<br>#ffbe50</td><td bgcolor="#f0a121">68<br>#f0a121</td><td bgcolor="#d08511">69<br>#d08511</td><td></td><td></td><td></td><td bgcolor="#fcc27c">70<br>#fcc27c</td><td bgcolor="#e7a75d">71<br>#e7a75d</td><td bgcolor="#c38639">72<br>#c38639</td><td></td><td></td><td></td><td bgcolor="#eec6a6">73<br>#eec6a6</td><td></td><td></td><td></td></tr>
<tr><th>yellow</th><td bgcolor="#ffdf00">※<br>#ffdf00</td><td></td><td bgcolor="#f1bf15">82<br>#f1bf15</td><td></td><td bgcolor="#f7ce50">83<br>#f7ce50</td><td bgcolor="#d9ae2f">84<br>#d9ae2f</td><td bgcolor="#b88f16">85<br>#b88f16</td><td></td><td></td><td></td><td bgcolor="#f4d284">86<br>#f4d284</td><td bgcolor="#d2af63">87<br>#d2af63</td><td bgcolor="#b08f42">88<br>#b08f42</td><td></td><td></td><td></td><td bgcolor="#efd7b2">89<br>#efd7b2</td><td bgcolor="#c8b18b">90<br>#c8b18b</td><td bgcolor="#a99066">91<br>#a99066</td><td></td></tr>
<tr><th>greenish yellow</th><td bgcolor="#fdff00">※<br>#fdff00</td><td></td><td bgcolor="#ebdd21">97<br>#ebdd21</td><td></td><td bgcolor="#e9dc55">98<br>#e9dc55</td><td bgcolor="#c4b827">99<br>#c4b827</td><td bgcolor="#a29812">100<br>#a29812</td><td></td><td></td><td></td><td bgcolor="#e9dd8a">101<br>#e9dd8a</td><td bgcolor="#c0b55e">102<br>#c0b55e</td><td bgcolor="#9e953c">103<br>#9e953c</td><td></td><td></td><td></td><td bgcolor="#e6dcab">104<br>#e6dcab</td><td bgcolor="#beb584">105<br>#beb584</td><td></td><td></td></tr>
<tr><th>yellow green</th><td bgcolor="#d3ff00">※<br>#d3ff00</td><td></td><td bgcolor="#a7dc26">115<br>#a7dc26</td><td></td><td bgcolor="#c3df69">116<br>#c3df69</td><td bgcolor="#82a12b">117<br>#82a12b</td><td bgcolor="#486c0e">118<br>#486c0e</td><td></td><td></td><td></td><td bgcolor="#cedb9f">119<br>#cedb9f</td><td bgcolor="#8b9a5f">120<br>#8b9a5f</td><td></td><td></td><td></td><td></td><td bgcolor="#d7d7c1">121<br>#d7d7c1</td><td bgcolor="#979a85">122<br>#979a85</td><td></td><td></td></tr>
<tr><th>yellowish green</th><td bgcolor="#59ff00">※<br>#59ff00</td><td></td><td bgcolor="#3fd740">129<br>#3fd740</td><td></td><td bgcolor="#87d989">130<br>#87d989</td><td bgcolor="#39964a">131<br>#39964a</td><td bgcolor="#176a1e">132<br>#176a1e</td><td bgcolor="#054208">133<br>#054208</td><td></td><td bgcolor="#c5edc4">134<br>#c5edc4</td><td bgcolor="#9cc69c">135<br>#9cc69c</td><td bgcolor="#669069">136<br>#669069</td><td bgcolor="#2f5d3a">137<br>#2f5d3a</td><td bgcolor="#10361a">138<br>#10361a</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>green</th><td bgcolor="#00ff83">※<br>#00ff83</td><td></td><td bgcolor="#23eaa5">139<br>#23eaa5</td><td></td><td bgcolor="#49d0a3">140<br>#49d0a3</td><td bgcolor="#158a66">141<br>#158a66</td><td bgcolor="#085e40">142†<br>#085e40</td><td></td><td></td><td bgcolor="#a6e2ca">143<br>#a6e2ca</td><td bgcolor="#6fac95">144<br>#6fac95</td><td bgcolor="#337762">145<br>#337762</td><td bgcolor="#164e3d">146<br>#164e3d</td><td bgcolor="#0c2e24">147<br>#0c2e24</td><td></td><td bgcolor="#c7d9d6">148<br>#c7d9d6</td><td bgcolor="#94a6a3">149<br>#94a6a3</td><td bgcolor="#61716e">150<br>#61716e</td><td bgcolor="#394746">151<br>#394746</td><td bgcolor="#1f2a2a">152<br>#1f2a2a</td></tr>
<tr><th>bluish green</th><td bgcolor="#00ffc6">※<br>#00ffc6</td><td></td><td bgcolor="#13fcd5">158<br>#13fcd5</td><td></td><td bgcolor="#35d7ce">159<br>#35d7ce</td><td bgcolor="#0d8f82">160<br>#0d8f82</td><td bgcolor="#0a5043">161†<br>#0a5043</td><td></td><td></td><td bgcolor="#98e1e0">162<br>#98e1e0</td><td bgcolor="#5fabab">163<br>#5fabab</td><td bgcolor="#297a7b">164<br>#297a7b</td><td bgcolor="#154b4d">165<br>#154b4d</td><td bgcolor="#0a2d2e">166<br>#0a2d2e</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>greenish blue</th><td bgcolor="#00ddff">※<br>#00ddff</td><td></td><td bgcolor="#00adc5">167†<br>#00adc5</td><td></td><td bgcolor="#2dbce2">168<br>#2dbce2</td><td bgcolor="#1385af">169<br>#1385af</td><td bgcolor="#05424c">170†<br>#05424c</td><td></td><td></td><td bgcolor="#94d6ef">171<br>#94d6ef</td><td bgcolor="#65a8c3">172<br>#65a8c3</td><td bgcolor="#2a7691">173<br>#2a7691</td><td bgcolor="#134a60">174<br>#134a60</td><td bgcolor="#0b2c3b">175<br>#0b2c3b</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>blue</th><td bgcolor="#0088ff">※<br>#0088ff</td><td></td><td bgcolor="#1b5cd7">176<br>#1b5cd7</td><td></td><td bgcolor="#419ded">177<br>#419ded</td><td bgcolor="#276cbd">178<br>#276cbd</td><td bgcolor="#113074">179<br>#113074</td><td></td><td></td><td bgcolor="#99c6f9">180<br>#99c6f9</td><td bgcolor="#73a4dc">181<br>#73a4dc</td><td bgcolor="#34689e">182<br>#34689e</td><td bgcolor="#173459">183<br>#173459</td><td></td><td></td><td bgcolor="#c2d2ec">184<br>#c2d2ec</td><td bgcolor="#91a2bb">185<br>#91a2bb</td><td bgcolor="#54687f">186<br>#54687f</td><td bgcolor="#323f4e">187<br>#323f4e</td><td bgcolor="#1e2531">188<br>#1e2531</td></tr>
<tr><th>purplish blue</th><td bgcolor="#0049ff">※<br>#0049ff</td><td></td><td bgcolor="#4436d1">194<br>#4436d1</td><td></td><td bgcolor="#8088e2">195<br>#8088e2</td><td bgcolor="#5359b5">196<br>#5359b5</td><td bgcolor="#2a286f">197<br>#2a286f</td><td></td><td></td><td bgcolor="#b7c0f8">198<br>#b7c0f8</td><td bgcolor="#8991cb">199<br>#8991cb</td><td bgcolor="#4d4e87">200<br>#4d4e87</td><td bgcolor="#222248">201<br>#222248</td><td></td><td></td><td bgcolor="#c5c9f0">202<br>#c5c9f0</td><td bgcolor="#8e92b7">203<br>#8e92b7</td><td bgcolor="#494d71">204<br>#494d71</td><td></td><td></td></tr>
<tr><th>violet</th><td bgcolor="#9200ff">※<br>#9200ff</td><td></td><td bgcolor="#7931d3">205<br>#7931d3</td><td></td><td bgcolor="#987fdc">206<br>#987fdc</td><td bgcolor="#61419c">207<br>#61419c</td><td bgcolor="#3c1668">208<br>#3c1668</td><td></td><td></td><td bgcolor="#c9baf8">209<br>#c9baf8</td><td bgcolor="#9b8cca">210<br>#9b8cca</td><td bgcolor="#5c4985">211<br>#5c4985</td><td bgcolor="#34254d">212<br>#34254d</td><td></td><td></td><td bgcolor="#d0c6ef">213<br>#d0c6ef</td><td bgcolor="#9a90b5">214<br>#9a90b5</td><td bgcolor="#584e72">215<br>#584e72</td><td></td><td></td></tr>
<tr><th>purple</th><td bgcolor="#dd00ff">※<br>#dd00ff</td><td></td><td bgcolor="#b935d5">216<br>#b935d5</td><td></td><td bgcolor="#ce8ce3">217<br>#ce8ce3</td><td bgcolor="#9352a8">218<br>#9352a8</td><td bgcolor="#652277">219<br>#652277</td><td bgcolor="#460a55">220<br>#460a55</td><td></td><td bgcolor="#e4b9f3">221<br>#e4b9f3</td><td bgcolor="#bc93cc">222<br>#bc93cc</td><td bgcolor="#875e96">223<br>#875e96</td><td bgcolor="#563762">224<br>#563762</td><td bgcolor="#371b41">225<br>#371b41</td><td></td><td bgcolor="#e0cbeb">226<br>#e0cbeb</td><td bgcolor="#ad97b3">227<br>#ad97b3</td><td bgcolor="#7b667e">228<br>#7b667e</td><td bgcolor="#513f51">229<br>#513f51</td><td bgcolor="#2f2231">230<br>#2f2231</td></tr>
<tr><th>reddish purple</th><td bgcolor="#ff00f5">※<br>#ff00f5</td><td></td><td bgcolor="#d429b9">236<br>#d429b9</td><td></td><td></td><td bgcolor="#a74994">237<br>#a74994</td><td bgcolor="#761a6a">238<br>#761a6a</td><td bgcolor="#4f094a">239<br>#4f094a</td><td></td><td></td><td bgcolor="#bd80ae">240<br>#bd80ae</td><td bgcolor="#965888">241<br>#965888</td><td bgcolor="#5f3458">242<br>#5f3458</td><td bgcolor="#3f183c">243<br>#3f183c</td><td></td><td></td><td bgcolor="#ad89a5">244<br>#ad89a5</td><td bgcolor="#86627e">245<br>#86627e</td><td></td><td></td></tr>
<tr><th>purplish red</th><td bgcolor="#ff00a7">※<br>#ff00a7</td><td></td><td bgcolor="#dd2388">254<br>#dd2388</td><td></td><td></td><td bgcolor="#b83773">255<br>#b83773</td><td bgcolor="#881055">256<br>#881055</td><td bgcolor="#54063c">257<br>#54063c</td><td></td><td></td><td></td><td bgcolor="#ab4b74">258<br>#ab4b74</td><td bgcolor="#6e294c">259<br>#6e294c</td><td bgcolor="#431432">260<br>#431432</td><td></td><td></td><td bgcolor="#b2879b">261*<br>#b2879b</td><td bgcolor="#945c73">262<br>#945c73</td><td></td><td></td></tr>
<tr><th></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>purplish pink</th><td></td><td></td><td></td><td></td><td bgcolor="#fca1e7">246<br>#fca1e7</td><td bgcolor="#f483cd">247<br>#f483cd</td><td bgcolor="#df6aac">248<br>#df6aac</td><td></td><td></td><td></td><td bgcolor="#f5b2db">249<br>#f5b2db</td><td bgcolor="#de98bf">250<br>#de98bf</td><td bgcolor="#c67d9d">251<br>#c67d9d</td><td></td><td></td><td></td><td bgcolor="#ebc8df">252<br>#ebc8df</td><td bgcolor="#c7a3b9">253<br>#c7a3b9</td><td></td><td></td></tr>
<tr><th>pink</th><td></td><td></td><td bgcolor="#fd7992">1<br>#fd7992</td><td></td><td></td><td bgcolor="#f48fa0">2<br>#f48fa0</td><td bgcolor="#e66980">3<br>#e66980</td><td></td><td></td><td></td><td bgcolor="#f8c3ce">4<br>#f8c3ce</td><td bgcolor="#e2a3ae">5<br>#e2a3ae</td><td bgcolor="#c5808a">6<br>#c5808a</td><td></td><td></td><td></td><td bgcolor="#efd1dc">7<br>#efd1dc</td><td bgcolor="#cbadb7">8<br>#cbadb7</td><td></td><td></td></tr>
<tr><th>yellowish pink</th><td></td><td></td><td bgcolor="#fd7e5d">25<br>#fd7e5d</td><td></td><td></td><td bgcolor="#f59080">26<br>#f59080</td><td bgcolor="#ef6366">27<br>#ef6366</td><td></td><td></td><td></td><td bgcolor="#f8c4b6">28<br>#f8c4b6</td><td bgcolor="#e2a698">29<br>#e2a698</td><td bgcolor="#c9807e">30<br>#c9807e</td><td></td><td></td><td></td><td bgcolor="#f1d3d1">31<br>#f1d3d1</td><td bgcolor="#cbacac">32<br>#cbacac</td><td bgcolor="#cbafa7">33*<br>#cbafa7</td><td></td></tr>
<tr><th></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>reddish brown</th><td></td><td></td><td></td><td></td><td></td><td bgcolor="#8b1c0e">40<br>#8b1c0e</td><td bgcolor="#610f12">41<br>#610f12</td><td></td><td></td><td></td><td bgcolor="#ac7a73">42<br>#ac7a73</td><td bgcolor="#7d423b">43<br>#7d423b</td><td bgcolor="#461d1e">44<br>#461d1e</td><td></td><td></td><td></td><td bgcolor="#9e7f7a">45*<br>#9e7f7a</td><td bgcolor="#6c4d4b">46<br>#6c4d4b</td><td bgcolor="#43292a">47<br>#43292a</td><td></td></tr>
<tr><th>brown</th><td></td><td></td><td></td><td></td><td></td><td bgcolor="#8a4416">55<br>#8a4416</td><td bgcolor="#571a07">56<br>#571a07</td><td></td><td></td><td></td><td bgcolor="#ad7c63">57<br>#ad7c63</td><td bgcolor="#724a38">58<br>#724a38</td><td bgcolor="#442112">59<br>#442112</td><td></td><td></td><td></td><td bgcolor="#997f75">60*<br>#997f75</td><td bgcolor="#674f48">61<br>#674f48</td><td bgcolor="#3e2c28">62<br>#3e2c28</td><td></td></tr>
<tr><th>yellowish brown</th><td></td><td></td><td></td><td></td><td></td><td bgcolor="#9e671d">74<br>#9e671d</td><td bgcolor="#673f0b">75<br>#673f0b</td><td></td><td></td><td></td><td bgcolor="#c49a74">76<br>#c49a74</td><td bgcolor="#886648">77<br>#886648</td><td bgcolor="#50341a">78<br>#50341a</td><td></td><td></td><td></td><td bgcolor="#b49b8d">79*<br>#b49b8d</td><td bgcolor="#7e695d">80<br>#7e695d</td><td bgcolor="#4d3d33">81<br>#4d3d33</td><td></td></tr>
<tr><th>olive brown</th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td bgcolor="#997736">94<br>#997736</td><td bgcolor="#705420">95<br>#705420</td><td bgcolor="#3f2c10">96<br>#3f2c10</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><th>olive</th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td bgcolor="#8b7d2e">106<br>#8b7d2e</td><td bgcolor="#64591a">107<br>#64591a</td><td bgcolor="#352e0a">108<br>#352e0a</td><td></td><td></td><td></td><td bgcolor="#8e856f">109*<br>#8e856f</td><td bgcolor="#5d553f">110<br>#5d553f</td><td bgcolor="#35301c">111<br>#35301c</td><td></td></tr>
<tr><th>olive green</th><td></td><td></td><td></td><td></td><td></td><td bgcolor="#2c5506">123<br>#2c5506</td><td bgcolor="#223604">124†<br>#223604</td><td></td><td></td><td></td><td></td><td bgcolor="#495b22">125<br>#495b22</td><td bgcolor="#20340b">126<br>#20340b</td><td></td><td></td><td></td><td></td><td bgcolor="#545947">127<br>#545947</td><td bgcolor="#2f3326">128<br>#2f3326</td><td></td></tr>
</table>


This is a test to see whether things break less with a paragraph here.


<table class="colorTable">
    <col><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol"><col class="colorcol">
    <tr><th></th><th>... white</th><th>light... gray</th><th>... gray</th><th>dark... gray</th><th>... black</th></tr>
    <tr><th></th>
        <td bgcolor="#e7e1e9">263<br>#e7e1e9</td>
        <td bgcolor="#bdb7bf">264<br>#bdb7bf</td>
        <td bgcolor="#8a8489">265<br>#8a8489</td>
        <td bgcolor="#585458">266<br>#585458</td>
        <td bgcolor="#2b292b">267<br>#2b292b</td>
    </tr>
    <tr><th>pinkish</th>
        <td bgcolor="#efdde5">9<br>#efdde5</td>
        <td bgcolor="#c7b6bd">10*<br>#c7b6bd</td>
        <td bgcolor="#8a8489"></td>
        <td bgcolor="#585458"></td>
        <td bgcolor="#2b292b"></td>
    </tr>
    <tr><th>reddish</th>
        <td bgcolor="#e7e1e9"></td>
        <td bgcolor="#bdb7bf"></td>
        <td bgcolor="#928186">22<br>#928186</td>
        <td bgcolor="#5d4e53">23<br>#5d4e53</td>
        <td bgcolor="#30262b">24<br>#30262b</td>
    </tr>
    <tr><th>brownish</th>
        <td bgcolor="#e7e1e9"></td>
        <td bgcolor="#bdb7bf"></td>
        <td bgcolor="#928281">63*<br>#928281</td>
        <td bgcolor="#605251">64*<br>#605251</td>
        <td bgcolor="#2b211e">65<br>#2b211e</td>
    </tr>
    <tr><th>yellowish</th>
        <td bgcolor="#eedfda">92<br>#eedfda</td>
        <td bgcolor="#c6b9b1">93<br>#c6b9b1</td>
        <td bgcolor="#8a8489"></td>
        <td bgcolor="#585458"></td>
        <td bgcolor="#2b292b"></td>
    </tr>
    <tr><th>olive</th>
        <td bgcolor="#e7e1e9"></td>
        <td bgcolor="#bdb7bf"></td>
        <td bgcolor="#8f877f">112*<br>#8f877f</td>
        <td bgcolor="#58514a">113*<br>#58514a</td>
        <td bgcolor="#23211c">114<br>#23211c</td>
    </tr>
    <tr><th>greenish</th>
        <td bgcolor="#e0e2e5">153<br>#e0e2e5</td>
        <td bgcolor="#babec1">154<br>#babec1</td>
        <td bgcolor="#848888">155<br>#848888</td>
        <td bgcolor="#545858">156<br>#545858</td>
        <td bgcolor="#212626">157<br>#212626</td>
    </tr>
    <tr><th>bluish</th>
        <td bgcolor="#e1e1f1">189<br>#e1e1f1</td>
        <td bgcolor="#b7b8c6">190<br>#b7b8c6</td>
        <td bgcolor="#838793">191<br>#838793</td>
        <td bgcolor="#50545f">192<br>#50545f</td>
        <td bgcolor="#24272e">193<br>#24272e</td>
    </tr>
    <tr><th>purplish</th>
        <td bgcolor="#ebdfef">231<br>#ebdfef</td>
        <td bgcolor="#c3b7c6">232<br>#c3b7c6</td>
        <td bgcolor="#8f8490">233<br>#8f8490</td>
        <td bgcolor="#5c525e">234<br>#5c525e</td>
        <td bgcolor="#2b2630">235<br>#2b2630</td>
    </tr>
</table>


Compared to Centore's original set of color labels,
I have made the following changes:

- Colors marked with * have been relabelled.
    - Brownish orange (54) has been relabelled "dark orange".
    - Brownish pink (33) has been relabelled "dark grayish yellowish pink".
    - The "light grayish" column has been combined into the "pale" column.
    - The neutral grayish colors have been shuffled around a bit to make each column have consistent luminance.
- Colors marked with † have had color codes added. Centore's method didn't yield RGB codes for some of the color labels, (because the centroid fell outside of RGB space,) So I chose some 'close-enough' looking colors to fill out the table.
- Colors marked with ※ are not present in the original table or system of colors.








