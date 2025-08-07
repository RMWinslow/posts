wikipedia corpus, labelled by grok
https://github.com/IlyaSemenov/wikipedia-word-frequency/tree/master/results

AI response:

To create a new list containing only the words from the provided document that refer to **physical objects**, I’ll iterate through the given list of words starting with `x`, filter them based on the criteria, and exclude Chinese cities, abbreviations, and non-physical entities (e.g., concepts, names, software, or abstract terms). The resulting list will include only terms that denote tangible, physical items or entities that can be physically interacted with (e.g., products, devices, or substances).

### Criteria for Inclusion
- **Physical Objects**: The word must refer to a tangible item, such as a product, device, machine, or physical substance.
- **Exclusions**:
  - **Chinese cities or place names**: Terms like `xinjiang`, `xiamen`, `xian`, etc., are excluded as they are geographical locations.
  - **Abbreviations**: Terms like `xml`, `xp`, `xs`, `xl`, etc., that are shorthand for concepts, sizes, or software are excluded.
  - **Abstract terms**: Words like `xenophobia`, `xor`, or Roman numerals (`xii`, `xiv`) that represent ideas, numbers, or symbols are excluded.
  - **Names**: Proper names like `xavier`, `xu`, or `xiao` are excluded unless they refer to a physical entity.
  - **Software or media**: Terms like `xemacs`, `x-files`, or `xvid` that refer to software, shows, or digital formats are excluded.
  - **Organizations or events**: Terms like `xfl`, `x-games`, or `xfinity` are excluded as they represent organizations or abstract concepts.
  - **Chemical or biological terms**: Included only if they refer to tangible substances or objects (e.g., `xenon` as a gas, `xylophone` as an instrument).

### Iteration and Filtering

Below, I’ll go through the provided list, evaluate each term, and include only those that meet the criteria for physical objects. I’ll provide a brief explanation for each included or excluded term to ensure clarity.

1. **x (228685)**: Excluded. Roman numeral, variable, or symbol, not a physical object.
2. **xi (47561)**: Excluded. Roman numeral (11) or Greek letter, not physical.
3. **xbox (26379)**: **Included**. Refers to a physical video game console by Microsoft.
4. **xavier (22314)**: Excluded. A proper name (person or institution), not a physical object.
5. **x-ray (20733)**: **Included**. Refers to a physical phenomenon (electromagnetic radiation) or a physical image produced by an X-ray machine.
6. **xii (18737)**: Excluded. Roman numeral (12), not physical.
7. **xiii (17467)**: Excluded. Roman numeral (13), not physical.
8. **xu (16619)**: Excluded. Vietnamese surname or monetary unit, not a physical object.
9. **xv (16080)**: Excluded. Roman numeral (15), not physical.
10. **xiv (15456)**: Excluded. Roman numeral (14), not physical.
11. **xvi (14055)**: Excluded. Roman numeral (16), not physical.
12. **x-men (13758)**: Excluded. Refers to a fictional group or media franchise, not a physical object.
13. **xiao (10817)**: Excluded. Chinese surname or term, not a physical object.
14. **xinjiang (10566)**: Excluded. Chinese province, a geographical location.
15. **xml (8036)**: Excluded. Abbreviation for Extensible Markup Language, a data format.
16. **xx (7769)**: Excluded. Roman numeral (20) or symbol, not physical.
17. **xiang (6344)**: Excluded. Chinese surname or term, not a physical object.
18. **x-rays (6088)**: **Included**. Plural of X-ray, referring to physical electromagnetic radiation or images.
19. **xl (5650)**: Excluded. Abbreviation for extra large or Roman numeral (40), not a specific object.
20. **xia (5557)**: Excluded. Chinese surname or term, not physical.
21. **xviii (5331)**: Excluded. Roman numeral (18), not physical.
22. **xp (5325)**: Excluded. Abbreviation for experience points or Windows XP, not physical.
23. **xin (5013)**: Excluded. Chinese surname or term, not physical.
24. **xm (4989)**: Excluded. Abbreviation (e.g., SiriusXM or model designation), not a specific object.
25. **x-files (4717)**: Excluded. Refers to a TV show or media, not physical.
26. **xxiii (4648)**: Excluded. Roman numeral (23), not physical.
27. **xian (4577)**: Excluded. Chinese city (Xi’an), a geographical location.
28. **xfinity (4500)**: Excluded. Brand name for a service provider, not a physical object.
29. **xxi (4427)**: Excluded. Roman numeral (21), not physical.
30. **xxx (4378)**: Excluded. Symbol for adult content or placeholder, not physical.
31. **xie (3955)**: Excluded. Chinese surname, not physical.
32. **xun (3712)**: Excluded. Chinese surname or term, not physical.
33. **xuan (3689)**: Excluded. Chinese surname or term, not physical.
34. **xix (3627)**: Excluded. Roman numeral (19), not physical.
35. **xi'an (3597)**: Excluded. Chinese city, a geographical location.
36. **xerox (3562)**: **Included**. Refers to a physical photocopying machine or the act of copying, associated with a tangible device.
37. **xing (3451)**: Excluded. Chinese surname or term, not physical.
38. **xvii (3367)**: Excluded. Roman numeral (17), not physical.
39. **xiongnu (3250)**: Excluded. Historical nomadic group, not a physical object.
40. **xue (3189)**: Excluded. Chinese surname, not physical.
41. **xxii (3043)**: Excluded. Roman numeral (22), not physical.
42. **xfl (2981)**: Excluded. Refers to a football league, not a physical object.
43. **xavier's (2815)**: Excluded. Possessive form of the name Xavier, not physical.
44. **xiu (2737)**: Excluded. Chinese surname or term, not physical.
45. **xhosa (2664)**: Excluded. Refers to a people or language, not a physical object.
46. **xiamen (2635)**: Excluded. Chinese city, a geographical location.
47. **xtreme (2600)**: Excluded. Informal spelling of “extreme,” not a specific object.
48. **xenon (2568)**: **Included**. A chemical element (noble gas) used in lighting and other applications, a tangible substance.
49. **xs (2397)**: Excluded. Abbreviation for extra small, not a specific object.
50. **xenophon (2252)**: Excluded. Greek philosopher’s name, not physical.
51. **xander (2223)**: Excluded. Proper name, not physical.
52. **xenia (2159)**: Excluded. Proper name or concept (hospitality in Greek), not physical.
53. **xd (2132)**: Excluded. Emoticon for laughter, not physical.
54. **x's (2119)**: Excluded. Possessive form of `x`, not a specific object.
55. **xenophobia (2099)**: Excluded. Abstract concept (fear of foreigners), not physical.
56. **xxl (2077)**: Excluded. Abbreviation for extra extra large, not a specific object.
57. **xuân (2032)**: Excluded. Vietnamese term (e.g., for spring) or name, not physical.
58. **xuanzong (1954)**: Excluded. Chinese emperor’s name, not physical.
59. **xy (1942)**: Excluded. Refers to chromosome pair or coordinates, not a physical object.
60. **xiong (1936)**: Excluded. Chinese surname, not physical.
61. **xiaoping (1891)**: Excluded. Chinese name (e.g., Deng Xiaoping), not physical.
62. **xinhua (1845)**: Excluded. Chinese news agency or term, not physical.
63. **xerxes (1778)**: Excluded. Persian king’s name, not physical.
64. **xperia (1734)**: **Included**. Sony’s brand of smartphones, a physical device.
65. **xxiv (1697)**: Excluded. Roman numeral (24), not physical.
66. **xtra (1678)**: Excluded. Informal spelling or brand (e.g., Xtra service), not a specific object.
67. **xuxa (1667)**: Excluded. Brazilian entertainer’s name, not physical.
68. **xenophobic (1600)**: Excluded. Adjective describing an abstract attitude, not physical.
69. **x-factor (1570)**: Excluded. Refers to a TV show or abstract quality, not physical.
70. **xxv (1545)**: Excluded. Roman numeral (25), not physical.
71. **xianbei (1519)**: Excluded. Historical nomadic group, not physical.
72. **xt (1454)**: Excluded. Model designation or abbreviation, not a specific object.
73. **x-linked (1435)**: Excluded. Genetic term, not a physical object.
74. **xaver (1428)**: Excluded. Variant of Xavier, a name, not physical.
75. **xanadu (1378)**: Excluded. Mythical place or media reference, not physical.
76. **xor (1353)**: Excluded. Logical operation in computing, not physical.
77. **xe (1336)**: Excluded. Gender-neutral pronoun or model designation, not a specific object.
78. **xo (1290)**: Excluded. Abbreviation (e.g., hugs and kisses) or brand, not physical.
79. **xanthi (1263)**: Excluded. Greek city or name, not physical.
80. **xxvi (1251)**: Excluded. Roman numeral (26), not physical.
81. **xa (1217)**: Excluded. Model designation or placeholder, not a specific object.
82. **xyz (1212)**: Excluded. Placeholder or coordinate system, not physical.
83. **xuanzang (1182)**: Excluded. Chinese monk’s name, not physical.
84. **xuzhou (1174)**: Excluded. Chinese city, a geographical location.
85. **xiaomi (1170)**: **Included**. Chinese brand of smartphones and electronics, referring to physical devices.
86. **xxvii (1158)**: Excluded. Roman numeral (27), not physical.
87. **xylophone (1139)**: **Included**. A musical instrument made of wooden bars, a physical object.
88. **x-force (1139)**: Excluded. Fictional group or media, not physical.
89. **xiahou (1129)**: Excluded. Chinese surname or historical figure, not physical.
90. **xfm (1094)**: Excluded. Radio station or brand, not a physical object.
91. **xi's (1065)**: Excluded. Possessive form of Xi (name), not physical.
92. **xxxi (1062)**: Excluded. Roman numeral (31), not physical.
93. **xr (1058)**: Excluded. Abbreviation (e.g., extended reality or iPhone XR), not a specific object without context.
94. **xeon (1043)**: **Included**. Intel’s brand of processors, physical computer components.
95. **xylem (1038)**: **Included**. A type of plant tissue, a tangible biological structure.
96. **xeric (1003)**: Excluded. Adjective describing dry environments, not a physical object.
97. **xmas (999)**: Excluded. Abbreviation for Christmas, a holiday, not physical.
98. **xxviii (989)**: Excluded. Roman numeral (28), not physical.
99. **xiv's (986)**: Excluded. Possessive form of Roman numeral XIV, not physical.
100. **xuanwu (968)**: Excluded. Mythological figure or place name, not physical.
101. **xhtml (962)**: Excluded. Abbreviation for Extensible HyperText Markup Language, not physical.
102. **xxxx (954)**: Excluded. Placeholder or adult content symbol, not physical.
103. **xcx (946)**: Excluded. Abbreviation or artist name (Charli XCX), not physical.
104. **xenopus (945)**: **Included**. A genus of aquatic frogs, physical living organisms.
105. **xianzong (927)**: Excluded. Chinese emperor’s name, not physical.
106. **xtc (915)**: Excluded. Slang for ecstasy (drug) or band name, not a specific object without context.
107. **xã (909)**: Excluded. Vietnamese administrative term, not physical.
108. **xiangyang (908)**: Excluded. Chinese city, a geographical location.
109. **xalapa (904)**: Excluded. Mexican city, a geographical location.
110. **xpress (896)**: Excluded. Informal spelling or brand (e.g., FedEx Xpress), not a specific object.
111. **xxix (886)**: Excluded. Roman numeral (29), not physical.
112. **xxxiii (873)**: Excluded. Roman numeral (33), not physical.
113. **xang (852)**: Excluded. Likely a name or typo, not clearly a physical object.
114. **xizong (850)**: Excluded. Chinese emperor’s name, not physical.
115. **x-wiki (844)**: Excluded. Refers to Wikipedia or similar, not physical.
116. **xc (832)**: Excluded. Abbreviation (e.g., cross-country) or model, not a specific object.
117. **xinhai (828)**: Excluded. Historical event (Xinhai Revolution), not physical.
118. **xingu (785)**: Excluded. River or indigenous group in Brazil, not a physical object.
119. **xps (779)**: **Included**. Dell’s brand of laptops or computers, physical devices.
120. **xxxv (764)**: Excluded. Roman numeral (35), not physical.
121. **xavi (740)**: Excluded. Proper name, not physical.
122. **xlviii (734)**: Excluded. Roman numeral (48), not physical.
123. **xenakis (730)**: Excluded. Composer’s name, not physical.
124. **xli (724)**: Excluded. Roman numeral (41), not physical.
125. **xamax (720)**: Excluded. Refers to a football club, not a physical object.
126. **xu's (694)**: Excluded. Possessive form of Xu (name), not physical.
127. **xxxii (683)**: Excluded. Roman numeral (32), not physical.
128. **xxxiv (680)**: Excluded. Roman numeral (34), not physical.
129. **xxxviii (676)**: Excluded. Roman numeral (38), not physical.
130. **xlii (675)**: Excluded. Roman numeral (42), not physical.
131. **ximena (675)**: Excluded. Proper name, not physical.
132. **xliii (670)**: Excluded. Roman numeral (43), not physical.
133. **xxxix (659)**: Excluded. Roman numeral (39), not physical.
134. **xxxvi (653)**: Excluded. Roman numeral (36), not physical.
135. **xianfeng (653)**: Excluded. Chinese emperor’s name, not physical.
136. **xlv (646)**: Excluded. Roman numeral (45), not physical.
137. **xlvii (635)**: Excluded. Roman numeral (47), not physical.
138. **xlvi (628)**: Excluded. Roman numeral (46), not physical.
139. **xcel (615)**: Excluded. Brand or company name, not a specific object.
140. **xerez (608)**: Excluded. Variant of Jerez (place or sherry wine), ambiguous without context.
141. **xochimilco (607)**: Excluded. Mexican location, not physical.
142. **xining (604)**: Excluded. Chinese city, a geographical location.
143. **xxxvii (599)**: Excluded. Roman numeral (37), not physical.
144. **xyloryctidae (596)**: **Included**. A family of moths, physical living organisms.
145. **xianyang (589)**: Excluded. Chinese city, a geographical location.
146. **xj (587)**: Excluded. Model designation (e.g., Jaguar XJ), not specific without context.
147. **xinyi (587)**: Excluded. Chinese place or name, not physical.
148. **x-pac (585)**: Excluded. Wrestling persona or media, not physical.
149. **xlix (581)**: Excluded. Roman numeral (49), not physical.
150. **xena (580)**: Excluded. Fictional character or name, not physical.
151. **xii's (568)**: Excluded. Possessive form of Roman numeral XII, not physical.
152. **x-axis (561)**: Excluded. Mathematical concept, not physical.
153. **xmlns (559)**: Excluded. XML namespace, a technical term, not physical.
154. **x-man (556)**: Excluded. Fictional character or media, not physical.
155. **xichuan (552)**: Excluded. Chinese place name, not physical.
156. **x-band (548)**: Excluded. Frequency band in radar, not a physical object.
157. **x-rated (546)**: Excluded. Adjective for adult content, not physical.
158. **xliv (538)**: Excluded. Roman numeral (44), not physical.
159. **xxxtentacion (538)**: Excluded. Artist name, not physical.
160. **x-treme (533)**: Excluded. Variant of “extreme,” not a specific object.
161. **xanthe (525)**: Excluded. Proper name, not physical.
162. **xen (524)**: Excluded. Abbreviation or fictional term, not clearly physical.
163. **xenoblade (523)**: Excluded. Video game title, not physical.
164. **xuchang (516)**: Excluded. Chinese city, a geographical location.
165. **xvi's (504)**: Excluded. Possessive form of Roman numeral XVI, not physical.
166. **xan (500)**: Excluded. Likely a name or abbreviation, not clearly physical.
167. **xk (490)**: Excluded. Model designation (e.g., Jaguar XK), not specific without context.
168. **xuyên (490)**: Excluded. Vietnamese term, not physical.
169. **xenosaga (486)**: Excluded. Video game series, not physical.
170. **xmpp (479)**: Excluded. Messaging protocol, not physical.
171. **xb (472)**: Excluded. Model designation (e.g., Scion xB), not specific without context.
172. **xanten (466)**: Excluded. German town, a geographical location.
173. **xuanzong's (458)**: Excluded. Possessive form of Chinese emperor’s name, not physical.
174. **x-type (451)**: Excluded. Model designation (e.g., Jaguar X-Type), not specific without context.
175. **xml-based (443)**: Excluded. Technical term, not physical.
176. **xlr (438)**: **Included**. A type of electrical connector used in audio equipment, a physical object.
177. **xiaoming (436)**: Excluded. Chinese name, not physical.
178. **ximenes (432)**: Excluded. Proper name, not physical.
179. **xpt (427)**: Excluded. Abbreviation or model (e.g., train service), not specific.
180. **xv's (424)**: Excluded. Possessive form of Roman numeral XV, not physical.
181. **xslt (418)**: Excluded. Extensible Stylesheet Language Transformations, not physical.
182. **xiangtan (417)**: Excluded. Chinese city, a geographical location.
183. **xishan (414)**: Excluded. Chinese place name, not physical.
184. **x-men's (413)**: Excluded. Possessive form of X-Men, a fictional group, not physical.
185. **xf (408)**: Excluded. Model designation (e.g., Jaguar XF), not specific without context.
186. **xiaowu (403)**: Excluded. Chinese name or term, not physical.
187. **xzibit (402)**: Excluded. Artist name, not physical.
188. **xiaobo (398)**: Excluded. Chinese name, not physical.
189. **xenomania (398)**: Excluded. Music production group or term, not physical.
190. **xenoliths (396)**: **Included**. Rock fragments embedded in igneous rock, physical geological objects.
191. **xenophon's (395)**: Excluded. Possessive form of Xenophon, not physical.
192. **xiii's (395)**: Excluded. Possessive form of Roman numeral XIII, not physical.
193. **xanthus (391)**: Excluded. Mythological name or place, not physical.
194. **xn (389)**: Excluded. Abbreviation or placeholder, not physical.
195. **xylota (387)**: **Included**. A genus of hoverflies, physical living organisms.
196. **xcode (382)**: Excluded. Software development tool, not physical.
197. **xscape (381)**: Excluded. Music group or brand, not physical.
198. **xun's (378)**: Excluded. Possessive form of Xun, not physical.
199. **xplosion (377)**: Excluded. Event or brand name, not a specific object.
200. **xiaowen (377)**: Excluded. Chinese name, not physical.
201. **xylophanes (377)**: **Included**. A genus of moths, physical living organisms.
202. **xilinx (373)**: **Included**. Brand of programmable logic devices (e.g., FPGAs), physical electronic components.
203. **xchange (370)**: Excluded. Abstract term or brand, not a specific object.
204. **xylene (370)**: **Included**. A chemical solvent used in industry, a tangible substance.
205. **xanthos (368)**: Excluded. Mythological name or place, not physical.
206. **xiaoyu (365)**: Excluded. Chinese name or term, not physical.
207. **x-shaped (360)**: Excluded. Adjective describing shape, not a specific object.
208. **xanthomonas (360)**: **Included**. A genus of bacteria, physical microorganisms.
209. **xanthine (356)**: **Included**. A chemical compound found in the body and foods, a tangible substance.
210. **xizang (354)**: Excluded. Chinese name for Tibet, a geographical location.
211. **ximénez (353)**: Excluded. Proper name, not physical.
212. **x-wing (351)**: **Included**. A fictional starfighter from Star Wars, a physical object in its narrative context.
213. **xm's (348)**: Excluded. Possessive form of XM, not a specific object.
214. **xiangqi (347)**: **Included**. A Chinese board game (chess variant), involving physical pieces.
215. **xiaolin (346)**: Excluded. Name or fictional reference, not physical.
216. **xaverian (346)**: Excluded. Related to Xavier (e.g., school), not physical.
217. **xuānzong (341)**: Excluded. Variant of Xuanzong, a Chinese emperor’s name.
218. **xna (337)**: Excluded. Software framework or term, not physical.
219. **xis (336)**: Excluded. Plural of Xi (name or letter), not physical.
220. **xanth (326)**: Excluded. Likely a name or abbreviation, not clearly physical.
221. **xbmc (326)**: Excluded. Media player software, not physical.
222. **xfce (323)**: Excluded. Desktop environment software, not physical.
223. **xebec (321)**: **Included**. A type of sailing ship, a physical vessel.
224. **xàtiva (320)**: Excluded. Spanish town, a geographical location.
225. **xinzhuang (317)**: Excluded. Chinese place name, not physical.
226. **xtravaganza (315)**: Excluded. Event or cultural term, not physical.
227. **x-y (315)**: Excluded. Coordinate system, not physical.
228. **xuan's (314)**: Excluded. Possessive form of Xuan, not physical.
229. **xincheng (314)**: Excluded. Chinese place name, not physical.
230. **xubuntu (313)**: Excluded. Linux distribution, not physical.
231. **xg (312)**: Excluded. Abbreviation or model, not a specific object.
232. **xingtai (306)**: Excluded. Chinese city, a geographical location.
233. **xueliang (305)**: Excluded. Chinese name, not physical.
234. **xylose (305)**: **Included**. A sugar molecule used in biochemistry, a tangible substance.
235. **xenix (304)**: Excluded. Operating system, not physical.
236. **x-play (303)**: Excluded. TV show or media, not physical.
237. **xiangshan (302)**: Excluded. Chinese place name, not physical.
238. **xicheng (302)**: Excluded. Chinese place name, not physical.
239. **xevious (298)**: Excluded. Video game, not physical.
240. **xz (297)**: Excluded. Abbreviation or model, not a specific object.
241. **xsl (296)**: Excluded. Extensible Stylesheet Language, not physical.
242. **xstrata (296)**: Excluded. Company name, not a physical object.
243. **xist (295)**: Excluded. Likely a typo or abstract term, not physical.
244. **xiaozhuang (295)**: Excluded. Chinese name or term, not physical.
245. **xinyang (294)**: Excluded. Chinese city, a geographical location.
246. **xbrl (290)**: Excluded. Business reporting language, not physical.
247. **xpw (289)**: Excluded. Wrestling promotion, not physical.
248. **xhaka (287)**: Excluded. Proper name, not physical.
249. **xingmi (286)**: Excluded. Chinese name or term, not physical.
250. **x-games (285)**: Excluded. Sporting event, not a physical object.
251. **xabi (285)**: Excluded. Proper name, not physical.
252. **xiaoping's (284)**: Excluded. Possessive form of Xiaoping, not physical.
253. **xanax (283)**: **Included**. A brand name for alprazolam, a physical pharmaceutical drug.
254. **x-chromosome (283)**: Excluded. Genetic structure, not a standalone physical object.
255. **xinyu (282)**: Excluded. Chinese city, a geographical location.
256. **xichang (278)**: Excluded. Chinese city, a geographical location.
257. **xiao's (278)**: Excluded. Possessive form of Xiao, not physical.
258. **xeno (277)**: Excluded. Prefix or fictional term, not a specific object.
259. **xin's (277)**: Excluded. Possessive form of Xin, not physical.
260. **xenogears (275)**: Excluded. Video game, not physical.
261. **xrd (273)**: Excluded. Abbreviation for X-ray diffraction, a technique, not an object.
262. **xerophytic (271)**: Excluded. Adjective for plants, not a physical object.
263. **xiangsheng (271)**: Excluded. Chinese comedic performance, not physical.
264. **xoxo (270)**: Excluded. Symbol for hugs and kisses, not physical.
265. **xian's (270)**: Excluded. Possessive form of Xian, a city or name.
266. **xanthoparmelia (270)**: **Included**. A genus of lichens, physical organisms.
267. **xenos (268)**: Excluded. Plural of Xeno (fictional or term), not clearly physical.
268. **xiyu (266)**: Excluded. Chinese place name, not physical.
269. **xueyantuo (265)**: Excluded. Historical group, not physical.
270. **xilai (264)**: Excluded. Chinese name or term, not physical.
271. **xenopol (264)**: Excluded. Likely a name, not physical.
272. **xpath (263)**: Excluded. Query language for XML, not physical.
273. **xishuangbanna (263)**: Excluded. Chinese region, a geographical location.
274. **xenophanes (263)**: Excluded. Greek philosopher’s name, not physical.
275. **xls (261)**: Excluded. File format (Excel spreadsheet), not physical.
276. **xlt (260)**: Excluded. Model designation or abbreviation, not specific.
277. **xylitol (260)**: **Included**. A sugar alcohol used as a sweetener, a tangible substance.
278. **xero (260)**: Excluded. Brand or software, not a specific object.
279. **xianzhi (258)**: Excluded. Chinese name or term, not physical.
280. **xanthorrhoea (257)**: **Included**. A genus of Australian plants (grass trees), physical organisms.
281. **xquery (255)**: Excluded. Query language for XML, not physical.
282. **xenobiotics (254)**: **Included**. Chemical substances foreign to an organism, tangible compounds.
283. **xestia (252)**: **Included**. A genus of moths, physical organisms.
284. **xieng (251)**: Excluded. Likely a place or name (e.g., Xieng Khouang), not physical.
285. **xabier (250)**: Excluded. Variant of Xavier, a name, not physical.
286. **xdr (249)**: Excluded. Data format or tuberculosis type, not a specific object.
287. **xylocopa (248)**: **Included**. A genus of carpenter bees, physical organisms.
288. **xiu's (248)**: Excluded. Possessive form of Xiu, not physical.
289. **xiuquan (248)**: Excluded. Chinese name, not physical.
290. **xinzhou (247)**: Excluded. Chinese city, a geographical location.
291. **xiling (247)**: Excluded. Chinese place or name, not physical.
292. **xiang's (246)**: Excluded. Possessive form of Xiang, not physical.
293. **xindian (246)**: Excluded. Chinese place name, not physical.
294. **xi'e (243)**: Excluded. Chinese term or name, not physical.
295. **xanana (242)**: Excluded. Name (e.g., Xanana Gusmão), not physical.
296. **xuancheng (242)**: Excluded. Chinese city, a geographical location.
297. **xvs (241)**: Excluded. Abbreviation or model, not a specific object.
298. **x-league (240)**: Excluded. Sports league, not physical.
299. **xinghua (239)**: Excluded. Chinese place name, not physical.
300. **xenobiotic (237)**: Excluded. Singular of xenobiotics, but already included as plural.
301. **xenu (237)**: Excluded. Fictional or religious term, not physical.
302. **xin'an (236)**: Excluded. Chinese place name, not physical.
303. **xul (236)**: Excluded. XML user interface language, not physical.
304. **xrco (235)**: Excluded. Adult industry organization, not physical.
305. **x-mansion (232)**: Excluded. Fictional location in X-Men, not physical.
306. **xiaogang (232)**: Excluded. Chinese place or name, not physical.
307. **xplorer (230)**: Excluded. Brand or term (e.g., Ford Explorer), not specific.
308. **xanthophyllum (229)**: **Included**. A genus of tropical plants, physical organisms.
309. **xinxiang (228)**: Excluded. Chinese city, a geographical location.
310. **xá (228)**: Excluded. Vietnamese term, not physical.
311. **xxxholic (227)**: Excluded. Manga/anime series, not physical.
312. **xyy (227)**: Excluded. Chromosomal condition, not a physical object.
313. **x-fly (226)**: Excluded. Likely a brand or term, not clearly physical.
314. **xylophones (225)**: **Included**. Plural of xylophone, musical instruments.
315. **xiaoshan (223)**: Excluded. Chinese place name, not physical.
316. **xorn (223)**: Excluded. Fictional character, not physical.
317. **xiomara (223)**: Excluded. Proper name, not physical.
318. **xsd (222)**: Excluded. XML Schema Definition, not physical.
319. **xda (221)**: Excluded. XDA Developers community, not physical.
320. **xingyu (220)**: Excluded. Chinese name or term, not physical.
321. **xingyang (219)**: Excluded. Chinese place name, not physical.
322. **xuande (216)**: Excluded. Chinese emperor’s name, not physical.
323. **xianzong's (216)**: Excluded. Possessive form of Xianzong, not physical.
324. **ximen (216)**: Excluded. Chinese name or term, not physical.
325. **xizhi (214)**: Excluded. Chinese place name, not physical.
326. **xunzi (214)**: Excluded. Chinese philosopher’s name, not physical.
327. **xeroderma (210)**: Excluded. Medical condition, not a physical object.
328. **xfc (210)**: Excluded. Abbreviation or term, not clearly physical.
329. **xehanort (208)**: Excluded. Fictional character, not physical.
330. **xiaojing (206)**: Excluded. Chinese name or term, not physical.
331. **x-inactivation (206)**: Excluded. Genetic process, not physical.
332. **x-mas (204)**: Excluded. Variant of Xmas, a holiday, not physical.
333. **xia's (202)**: Excluded. Possessive form of Xia, not physical.
334. **x-height (201)**: Excluded. Typographic term, not physical.
335. **xương (201)**: Excluded. Vietnamese term, not physical.
336. **xanthorhoe (200)**: **Included**. A genus of moths, physical organisms.
337. **xsara (199)**: **Included**. Citroën Xsara, a physical car model.
338. **xfl's (198)**: Excluded. Possessive form of XFL, not physical.
339. **xiapi (196)**: Excluded. Historical Chinese place, not physical.
340. **xizong's (196)**: Excluded. Possessive form of Xizong, not physical.
341. **xcom (195)**: Excluded. Video game series, not physical.
342. **xiaoting (194)**: Excluded. Chinese name or term, not physical.
343. **xilie (194)**: Excluded. Chinese term (e.g., series), not physical.
344. **xiaoxiang (193)**: Excluded. Chinese place or term, not physical.
345. **xinjiang's (192)**: Excluded. Possessive form of Xinjiang, a place.
346. **xfs (192)**: Excluded. File system, not physical.
347. **xperience (188)**: Excluded. Abstract term or brand, not physical.
348. **xion (185)**: Excluded. Name or fictional term, not physical.
349. **xprize (185)**: Excluded. Competition or organization, not physical.
350. **xibalba (184)**: Excluded. Mythological place, not physical.
351. **xinmin (183)**: Excluded. Chinese place or term, not physical.
352. **xxxtentacion's (183)**: Excluded. Possessive form of artist name, not physical.
353. **xdrive (182)**: Excluded. BMW technology or term, not a specific object.
354. **xiaodong (182)**: Excluded. Chinese name, not physical.
355. **xiao'erjing (182)**: Excluded. Writing system, not physical.
356. **xyloto (181)**: Excluded. Album title, not physical.
357. **xiaoyanzi (181)**: Excluded. Chinese name or term, not physical.
358. **xunta (180)**: Excluded. Spanish term (e.g., junta), not physical.
359. **xiping (179)**: Excluded. Chinese place or name, not physical.
360. **xray (179)**: Excluded. Variant of X-ray, already included.
361. **xara (179)**: Excluded. Software or name, not clearly physical.
362. **xanthium (179)**: **Included**. A genus of plants (cocklebur), physical organisms.
363. **xindi (179)**: Excluded. Fictional species, not physical.
364. **xenograft (178)**: **Included**. Tissue graft from another species, a physical biological material.
365. **xyris (178)**: **Included**. A genus of flowering plants, physical organisms.
366. **xbiz (178)**: Excluded. Adult industry organization, not physical.
367. **xiaofeng (177)**: Excluded. Chinese name, not physical.
368. **xuefeng (176)**: Excluded. Chinese name or place, not physical.
369. **x-rayed (175)**: Excluded. Verb describing an action, not a physical object.
370. **xseed (174)**: Excluded. Company or fictional term, not physical.
371. **xvid (173)**: Excluded. Video codec, not physical.
372. **xinxing (172)**: Excluded. Chinese place or term, not physical.
373. **xosé (172)**: Excluded. Variant of José, a name, not physical.
374. **xenomorph (171)**: Excluded. Fictional alien species, not physical.
375. **xmp (171)**: Excluded. Metadata platform, not physical.
376. **xam (169)**: Excluded. Likely a name or term, not clearly physical.
377. **xmm-newton (169)**: **Included**. A space telescope, a physical object.
378. **xxy (168)**: Excluded. Chromosomal condition, not a physical object.
379. **xyleutes (168)**: **Included**. A genus of moths, physical organisms.
380. **xsi (167)**: Excluded. Software or abbreviation, not physical.
381. **xuhui (167)**: Excluded. Chinese place name, not physical.
382. **xander's (167)**: Excluded. Possessive form of Xander, not physical.
383. **xihu (166)**: Excluded. Chinese place name (e.g., West Lake), not physical.
384. **xplore (166)**: Excluded. Brand or term, not a specific object.
385. **xenotransplantation (165)**: Excluded. Medical procedure, not a physical object.
386. **xterra (165)**: **Included**. Nissan Xterra, a physical SUV model.
387. **xinghai (165)**: Excluded. Chinese place or term, not physical.
388. **xwb (163)**: Excluded. Model designation (e.g., Airbus A350 XWB), not specific.
389. **xjs (162)**: **Included**. Jaguar XJS, a physical car model.
390. **xitsonga (162)**: Excluded. Language or cultural term, not physical.
391. **xie's (162)**: Excluded. Possessive form of Xie, not physical.
392. **xingyi (162)**: Excluded. Chinese place or martial art, not physical.
393. **xamarin (162)**: Excluded. Software platform, not physical.
394. **xiangzi (162)**: Excluded. Chinese name or term, not physical.
395. **xinhui (161)**: Excluded. Chinese place name, not physical.
396. **xuantong (160)**: Excluded. Chinese emperor’s name, not physical.
397. **xcx's (160)**: Excluded. Possessive form of XCX, not physical.
398. **xilin (159)**: Excluded. Chinese place or name, not physical.
399. **xylopia (159)**: **Included**. A genus of flowering plants, physical organisms.
400. **xueshi (159)**: Excluded. Chinese term or name, not physical.
401. **x-bar (158)**: Excluded. Linguistic or statistical term, not physical.
402. **xue's (158)**: Excluded. Possessive form of Xue, not physical.
403. **xiguang (158)**: Excluded. Chinese name or term, not physical.
404. **xaml (158)**: Excluded. Markup language, not physical.
405. **xerox's (157)**: Excluded. Possessive form of Xerox, already included.
406. **xcor (157)**: Excluded. Aerospace company, not a specific object.
407. **xanthidae (157)**: **Included**. A family of crabs, physical organisms.
408. **xtc's (156)**: Excluded. Possessive form of XTC, not physical.
409. **xss (156)**: Excluded. Cross-site scripting, a security term, not physical.
410. **xou (156)**: Excluded. Likely a name or typo, not clearly physical.
411. **xī (155)**: Excluded. Chinese character or term, not physical.
412. **xolotl (155)**: Excluded. Mythological figure, not physical.
413. **xiaojun (154)**: Excluded. Chinese name, not physical.
414. **xochitl (154)**: Excluded. Name or term, not physical.
415. **xingyuan (153)**: Excluded. Chinese name or term, not physical.
416. **x-fi (153)**: **Included**. Creative Labs’ sound card brand, a physical device.
417. **xixi (153)**: Excluded. Chinese name or term, not physical.
418. **xavierian (153)**: Excluded. Related to Xavier, not physical.
419. **x-press (152)**: Excluded. Brand or term, not a specific object.
420. **xavante (152)**: Excluded. Indigenous group, not a physical object.
421. **x-trail (152)**: **Included**. Nissan X-Trail, a physical SUV model.
422. **xanthan (152)**: **Included**. A polysaccharide used as a food thickener, a tangible substance.
423. **xiaoqing (152)**: Excluded. Chinese name, not physical.
424. **xiangcheng (152)**: Excluded. Chinese place name, not physical.
425. **xerography (152)**: Excluded. Copying process, not a physical object.
426. **xillia (152)**: Excluded. Video game title, not physical.
427. **x-sampa (151)**: Excluded. Phonetic notation system, not physical.
428. **xira (150)**: Excluded. Place or name, not clearly physical.
429. **xianxia (150)**: Excluded. Chinese literary genre, not physical.
430. **xinzheng (150)**: Excluded. Chinese place name, not physical.
431. **xinyuan (150)**: Excluded. Chinese name or term, not physical.
432. **xuereb (149)**: Excluded. Proper name, not physical.
433. **xiangxiang (149)**: Excluded. Chinese place name, not physical.
434. **xetv (149)**: Excluded. TV station, not a physical object.
435. **xth (148)**: Excluded. Ordinal term, not physical.
436. **xianning (148)**: Excluded. Chinese city, a geographical location.
437. **x-com (148)**: Excluded. Variant of XCOM, a video game, not physical.
438. **x-seven (148)**: Excluded. Likely a brand or term, not clearly physical.
439. **xylorycta (148)**: **Included**. A genus of moths, physical organisms.
440. **x-bow (147)**: **Included**. A high-performance car (KTM X-Bow), a physical vehicle.
441. **xlink (146)**: Excluded. XML linking language, not physical.
442. **xpo (146)**: Excluded. Abbreviation or event, not a specific object.
443. **xandria (146)**: Excluded. Band or name, not physical.
444. **xylan (146)**: **Included**. A polysaccharide in plant cell walls, a tangible substance.
445. **xpander (145)**: **Included**. Mitsubishi Xpander, a physical MPV vehicle.
446. **xuanzang's (145)**: Excluded. Possessive form of Xuanzang, not physical.
447. **xiaolong (145)**: Excluded. Chinese name or term, not physical.
448. **xcp (145)**: Excluded. Abbreviation or protocol, not physical.
449. **xunhua (144)**: Excluded. Chinese place name, not physical.
450. **xagħra (144)**: Excluded. Maltese place name, not physical.
451. **xiphophorus (144)**: **Included**. A genus of fish (e.g., swordtails), physical organisms.
452. **xifan (144)**: Excluded. Likely a fictional or cultural term, not physical.
453. **xerocrassa (144)**: **Included**. A genus of snails, physical organisms.
454. **xibe (143)**: Excluded. Ethnic group or language, not physical.
455. **xherdan (143)**: Excluded. Proper name, not physical.
456. **xanatos (143)**: Excluded. Fictional character, not physical.
457. **xiyang (142)**: Excluded. Chinese place or term, not physical.
458. **xueqin (142)**: Excluded. Chinese name, not physical.
459. **xmodem (142)**: Excluded. File transfer protocol, not physical.
460. **xh (140)**: Excluded. Abbreviation or letter, not physical.
461. **xiaoxi (140)**: Excluded. Chinese name or term, not physical.
462. **xio (140)**: Excluded. Likely a name or abbreviation, not physical.
463. **xinwen (139)**: Excluded. Chinese term (e.g., news), not physical.
464. **xing's (139)**: Excluded. Possessive form of Xing, not physical.
465. **xit (138)**: Excluded. Likely a typo or term, not clearly physical.
466. **ximenez (138)**: Excluded. Variant of Ximenes, a name, not physical.
467. **xuyen (138)**: Excluded. Vietnamese term or name, not physical.
468. **xianbei-led (137)**: Excluded. Historical term, not physical.
469. **xenarthrans (137)**: **Included**. A group of mammals (e.g., sloths, anteaters), physical organisms.
470. **xingguo (137)**: Excluded. Chinese place name, not physical.
471. **xelajú (137)**: Excluded. Guatemalan place name, not physical.
472. **xaviers (137)**: Excluded. Plural of Xavier, not physical.
473. **xiaotong (137)**: Excluded. Chinese name, not physical.
474. **xiaoli (137)**: Excluded. Chinese name, not physical.
475. **xavin (136)**: Excluded. Fictional character or name, not physical.
476. **xichong (136)**: Excluded. Chinese place name, not physical.
477. **xiangfan (135)**: Excluded. Chinese city, a geographical location.
478. **xanthogaleruca (135)**: **Included**. A genus of beetles, physical organisms.
479. **xpeng (135)**: **Included**. A Chinese brand of electric vehicles, physical cars.
480. **xetra (134)**: Excluded. Stock exchange system, not physical.
481. **xinca (134)**: Excluded. Indigenous group or language, not physical.
482. **xihe (134)**: Excluded. Chinese mythological term or place, not physical.
483. **xanthippus (134)**: Excluded. Historical name, not physical.
484. **x-o (133)**: Excluded. Likely a term or fictional reference, not physical.
485. **xymox (133)**: Excluded. Band name, not physical.
486. **xrf (133)**: Excluded. X-ray fluorescence, a technique, not a physical object.
487. **xpcc (133)**: Excluded. Abbreviation (e.g., Xinjiang Production Corps), not physical.
488. **xuānzong's (133)**: Excluded. Possessive form of Xuānzong, not physical.
489. **xhamster (133)**: Excluded. Adult website, not physical.
490. **xiaolan (132)**: Excluded. Chinese name or place, not physical.
491. **xiong's (132)**: Excluded. Possessive form of Xiong, not physical.
492. **xuanhua (131)**: Excluded. Chinese place name, not physical.
493. **xingang (131)**: Excluded. Chinese place name, not physical.
494. **xandra (130)**: Excluded. Proper name, not physical.
495. **xyzzy (130)**: Excluded. Fictional or game term, not physical.
496. **xujiahui (130)**: Excluded. Chinese place name, not physical.
497. **xiangkhouang (130)**: Excluded. Laotian place name, not physical.
498. **xikang (130)**: Excluded. Historical Chinese province, not physical.
499. **xiguan (129)**: Excluded. Chinese place or term, not physical.
500. **xxe (129)**: Excluded. XML external entity, a security term, not physical.
501. **xylazine (129)**: **Included**. A veterinary sedative drug, a tangible substance.
502. **xingjian (129)**: Excluded. Chinese name or term, not physical.
503. **xrs (129)**: Excluded. Model designation, not specific.
504. **xenografts (129)**: Excluded. Plural of xenograft, already included.
505. **xingyiquan (129)**: Excluded. Chinese martial art, not physical.
506. **xiangxi (129)**: Excluded. Chinese place name, not physical.
507. **x-series (127)**: Excluded. Model series, not a specific object.
508. **xuthus (127)**: Excluded. Mythological name, not physical.
509. **xoom (126)**: **Included**. Motorola Xoom, a physical tablet device.
510. **xew (126)**: Excluded. Likely a place or term, not clearly physical.
511. **xmb (126)**: Excluded. Cross-media bar, a software interface, not physical.
512. **xewkija (126)**: Excluded. Maltese place name, not physical.
513. **xixe (125)**: Excluded. Likely a typo or term, not physical.
514. **xunyang (125)**: Excluded. Chinese place name, not physical.
515. **xiannian (123)**: Excluded. Chinese name, not physical.
516. **x-tra (123)**: Excluded. Brand or term, not a specific object.
517. **xiaoling (123)**: Excluded. Chinese name or term, not physical.
518. **x-plane (123)**: Excluded. Flight simulator software, not physical.
519. **xerostomia (123)**: Excluded. Medical condition, not a physical object.
520. **xylouris (123)**: Excluded. Proper name, not physical.
521. **xxxxi (122)**: Excluded. Roman numeral or typo, not physical.
522. **xiaomin (122)**: Excluded. Chinese name or term, not physical.
523. **xscale (121)**: Excluded. Processor architecture, not a specific object.
524. **xincun (121)**: Excluded. Chinese place name, not physical.
525. **x-gene (120)**: Excluded. Genetic or fictional term, not physical.
526. **xms (119)**: Excluded. Memory specification, not physical.
527. **xiaogong (119)**: Excluded. Chinese name or term, not physical.
528. **xenorhabdus (118)**: **Included**. A genus of bacteria, physical microorganisms.
529. **xiaopeng (118)**: Excluded. Chinese name or brand (already included as Xpeng).
530. **xebecs (118)**: Excluded. Plural of xebec, already included.
531. **xkcd (118)**: Excluded. Webcomic, not physical.
532. **xylosma (118)**: **Included**. A genus of shrubs, physical plants.
533. **xiaoyan (117)**: Excluded. Chinese name, not physical.
534. **x-class (117)**: Excluded. Designation (e.g., solar flare), not a specific object.
535. **xlib (117)**: Excluded. X Window System library, not physical.
536. **xmrv (117)**: Excluded. Virus name, not a standalone physical object.
537. **xindu (116)**: Excluded. Chinese place name, not physical.
538. **xw (116)**: Excluded. Abbreviation or model, not physical.
539. **xeriscaping (116)**: Excluded. Landscaping technique, not a physical object.
540. **xiangru (116)**: Excluded. Chinese name or term, not physical.
541. **xenocrates (116)**: Excluded. Greek philosopher’s name, not physical.
542. **xiaowei (116)**: Excluded. Chinese name, not physical.
543. **xerocomus (116)**: **Included**. A genus of fungi, physical organisms.
544. **xinglong (115)**: Excluded. Chinese place name, not physical.
545. **xiphias (115)**: **Included**. A genus of fish (swordfish), physical organisms.
546. **xcelsior (114)**: **Included**. A model of bus by New Flyer, a physical vehicle.
547. **xaviera (114)**: Excluded. Proper name, not physical.
548. **xandar (114)**: Excluded. Fictional planet, not physical.
549. **xinshi (114)**: Excluded. Chinese place or term, not physical.
550. **xanthopoulos (113)**: Excluded. Proper name, not physical.
551. **xintong (113)**: Excluded. Chinese name or term, not physical.
552. **xwa (113)**: Excluded. Abbreviation or term, not clearly physical.
553. **x-division (112)**: Excluded. Wrestling division, not physical.
554. **xinye (112)**: Excluded. Chinese place name, not physical.
555. **xiph (112)**: Excluded. Likely abbreviation, not clearly physical.
556. **xuv (111)**: Excluded. Model designation (e.g., Mahindra XUV), not specific.
557. **xenomorphs (111)**: Excluded. Plural of xenomorph, already excluded.
558. **xiakou (111)**: Excluded. Chinese place name, not physical.
559. **xinsheng (111)**: Excluded. Chinese term or name, not physical.
560. **xiangxue (111)**: Excluded. Chinese name or term, not physical.
561. **xanthippe (110)**: Excluded. Historical name, not physical.
562. **xiaofei (110)**: Excluded. Chinese name, not physical.
563. **xkr (110)**: **Included**. Jaguar XKR, a physical car model.
564. **xtr (110)**: Excluded. Model designation, not specific.
565. **xiangzhou (109)**: Excluded. Chinese place name, not physical.
566. **xbase (109)**: Excluded. Database software, not physical.
567. **xingning (109)**: Excluded. Chinese place name, not physical.
568. **x'trapolis (109)**: **Included**. A model of train by Alstom, a physical vehicle.
569. **xingbu (109)**: Excluded. Chinese historical term, not physical.
570. **xizhou (109)**: Excluded. Chinese place or term, not physical.
571. **xas (108)**: Excluded. Abbreviation or term, not clearly physical.
572. **xinjian (108)**: Excluded. Chinese place or term, not physical.
573. **xanthosoma (108)**: **Included**. A genus of tropical plants, physical organisms.
574. **xinfeng (108)**: Excluded. Chinese place name, not physical.
575. **xidan (108)**: Excluded. Chinese place name, not physical.
576. **xinyun (107)**: Excluded. Chinese name or term, not physical.
577. **xxxxx (107)**: Excluded. Placeholder or typo, not physical.
578. **xiaoyi (107)**: Excluded. Chinese name or place, not physical.
579. **xico (107)**: Excluded. Likely a name or place, not clearly physical.
580. **xpressmusic (107)**: Excluded. Nokia brand feature, not a specific object.
581. **x-prize (107)**: Excluded. Variant of XPRIZE, a competition, not physical.
582. **xuangan (107)**: Excluded. Chinese name or term, not physical.
583. **xinping (107)**: Excluded. Chinese place name, not physical.
584. **xana (106)**: Excluded. Name or fictional term, not physical.
585. **xxiii's (106)**: Excluded. Possessive form of Roman numeral XXIII, not physical.
586. **xeni (106)**: Excluded. Likely a name, not physical.
587. **xds (106)**: Excluded. Abbreviation or model, not a specific object.
588. **xserve (105)**: **Included**. Apple’s server hardware, a physical device.
589. **xango (105)**: Excluded. Brand or mythological term, not clearly physical.
590. **xolo (105)**: **Included**. Xoloitzcuintli, a breed of dog, a physical organism.
591. **xiphos (105)**: **Included**. A type of ancient Greek sword, a physical weapon.
592. **xers (105)**: Excluded. Generational term, not physical.
593. **xiangguo (105)**: Excluded. Chinese name or term, not physical.
594. **xiaogan (105)**: Excluded. Chinese city, a geographical location.
595. **xinyao (105)**: Excluded. Chinese music genre, not physical.
596. **xploration (104)**: Excluded. Abstract term or brand, not physical.
597. **xingcheng (104)**: Excluded. Chinese place name, not physical.
598. **xandros (104)**: Excluded. Operating system, not physical.
599. **xxth (103)**: Excluded. Ordinal term, not physical.
600. **xianzhong (103)**: Excluded. Chinese name, not physical.
601. **xd's (103)**: Excluded. Possessive form of XD, not physical.
602. **xfire (103)**: Excluded. Gaming platform, not physical.
603. **xuanwu's (103)**: Excluded. Possessive form of Xuanwu, not physical.
604. **xanthate (103)**: **Included**. A chemical compound used in mining, a tangible substance.
605. **xeelee (103)**: Excluded. Fictional species, not physical.
606. **xisheng (103)**: Excluded. Chinese term or name, not physical.
607. **xhafaj (103)**: Excluded. Likely a name, not physical.
608. **x_ (102)**: Excluded. Placeholder or typo, not physical.
609. **xaverians (102)**: Excluded. Plural of Xaverian, not physical.
610. **xiaohe (102)**: Excluded. Chinese place or name, not physical.
611. **xbox's (101)**: Excluded. Possessive form of Xbox, already included.
612. **xipe (101)**: Excluded. Mythological figure, not physical.
613. **xmi (101)**: Excluded. Metadata interchange format, not physical.
614. **xanh (101)**: Excluded. Vietnamese term (e.g., green), not physical.
615. **xiaozhao (101)**: Excluded. Chinese name or term, not physical.
616. **xiaomi's (101)**: Excluded. Possessive form of Xiaomi, already included.
617. **xiahe (100)**: Excluded. Chinese place name, not physical.
618. **xiangdong (100)**: Excluded. Chinese name or place, not physical.
619. **xīn (100)**: Excluded. Chinese character or term, not physical.
620. **xaba (100)**: Excluded. Likely a name or term, not clearly physical.
621. **xehanort's (100)**: Excluded. Possessive form of Xehanort, not physical.
622. **xmm (100)**: Excluded. Abbreviation or model, not a specific object.
623. **xar (100)**: Excluded. Likely a term or abbreviation, not physical.
624. **xinning (100)**: Excluded. Chinese place name, not physical.
625. **xuanwei (100)**: Excluded. Chinese place name, not physical.
626. **xerophytes (99)**: **Included**. Plants adapted to dry environments, physical organisms.
627. **xingshi (99)**: Excluded. Chinese term or name, not physical.
628. **xforms (99)**: Excluded. Web form standard, not physical.
629. **xiaguan (99)**: Excluded. Chinese place name, not physical.
630. **xpf (99)**: Excluded. Currency code or abbreviation, not physical.
631. **xecl (99)**: Excluded. Likely a chemical or term, not clearly physical.
632. **xochicalco (99)**: Excluded. Mexican archaeological site, not physical.
633. **xinjing (99)**: Excluded. Chinese place name, not physical.
634. **xianlin (99)**: Excluded. Chinese place name, not physical.
635. **xuanxue (99)**: Excluded. Chinese philosophical school, not physical.
636. **xkeyscore (99)**: Excluded. Surveillance program, not physical.
637. **xiyin (99)**: Excluded. Chinese name or term, not physical.
638. **xangongo (98)**: Excluded. Angolan place name, not physical.
639. **xq (98)**: Excluded. Abbreviation or term, not physical.
640. **xiangning (98)**: Excluded. Chinese place name, not physical.
641. **x-giants (98)**: Excluded. Likely a team or fictional term, not physical.
642. **xhafer (98)**: Excluded. Proper name, not physical.
643. **xle (98)**: Excluded. Model designation, not specific.
644. **xx's (98)**: Excluded. Possessive form of XX, not physical.
645. **xysticus (98)**: **Included**. A genus of crab spiders, physical organisms.
646. **xored (98)**: Excluded. Verb (logical operation), not physical.
647. **xiaozong (98)**: Excluded. Chinese name or term, not physical.
648. **xiangyu (98)**: Excluded. Chinese name, not physical.
649. **xuanyi (98)**: Excluded. Chinese name or term, not physical.
650. **xiaowu's (97)**: Excluded. Possessive form of Xiaowu, not physical.
651. **xci (97)**: Excluded. Roman numeral (91), not physical.
652. **x-team (97)**: Excluded. Group or brand, not physical.
653. **xifeng (97)**: Excluded. Chinese place or name, not physical.
654. **xiaohui (97)**: Excluded. Chinese name, not physical.
655. **xitun (97)**: Excluded. Chinese place name, not physical.
656. **xingzhou (97)**: Excluded. Chinese place name, not physical.
657. **xmlhttprequest (96)**: Excluded. Web API, not physical.
658. **xai (96)**: Excluded. Company or term (e.g., xAI), not a specific object.
659. **xiaolian (96)**: Excluded. Chinese historical term, not physical.
660. **xiaoyao (96)**: Excluded. Chinese term or name, not physical.
661. **xylariaceae (96)**: **Included**. A family of fungi, physical organisms.
662. **xisha (95)**: Excluded. Chinese place name, not physical.
663. **xwf (94)**: Excluded. Abbreviation or term, not physical.
664. **xinqiao (94)**: Excluded. Chinese place name, not physical.
665. **x-ecutioners (93)**: Excluded. Music group, not physical.
666. **xpl (93)**: Excluded. Abbreviation or term, not physical.
667. **x-file (93)**: Excluded. Variant of X-Files, not physical.
668. **xxxxviii (93)**: Excluded. Roman numeral or typo, not physical.
669. **xiphoid (92)**: **Included**. A cartilage structure in the sternum, a physical anatomical part.
670. **xjr (92)**: **Included**. Jaguar XJR, a physical car model.
671. **xuantu (92)**: Excluded. Historical Chinese place, not physical.
672. **xiǎo (92)**: Excluded. Chinese character (small), not physical.
673. **xts (91)**: **Included**. Cadillac XTS, a physical car model.
674. **xdsl (91)**: Excluded. Broadband technology, not a physical object.
675. **xfa (91)**: Excluded. Form format, not physical.
676. **xvth (91)**: Excluded. Ordinal term, not physical.
677. **xga (91)**: Excluded. Display standard, not physical.
678. **xiaoshi (91)**: Excluded. Chinese name or term, not physical.
679. **xxxxxx (91)**: Excluded. Placeholder or typo, not physical.
680. **xat (91)**: Excluded. Chat platform or term, not physical.
681. **xolos (91)**: Excluded. Plural of Xolo, already included.
682. **xianyu (90)**: Excluded. Chinese name or term, not physical.
683. **xinchang (90)**: Excluded. Chinese place name, not physical.
684. **xeer (90)**: Excluded. Somali legal system, not physical.
685. **xhuvani (90)**: Excluded. Proper name, not physical.
686. **xposé (89)**: Excluded. Magazine or show, not physical.
687. **xiàn (89)**: Excluded. Chinese term (county), not physical.
688. **xxxxix (89)**: Excluded. Roman numeral or typo, not physical.
689. **xawery (89)**: Excluded. Variant of Xavier, not physical.
690. **xiaoshuai (89)**: Excluded. Chinese name, not physical.
691. **xenophrys (89)**: **Included**. A genus of frogs, physical organisms.
692. **xiapu (89)**: Excluded. Chinese place name, not physical.
693. **xiaoyun (89)**: Excluded. Chinese name, not physical.
694. **xing'an (89)**: Excluded. Chinese place name, not physical.
695. **xanthophyll (88)**: **Included**. A pigment in plants, a tangible substance.
696. **xliff (88)**: Excluded. Localization file format, not physical.
697. **xijing (88)**: Excluded. Chinese place or term, not physical.
698. **xdr-tb (88)**: Excluded. Drug-resistant tuberculosis, not a physical object.
699. **xns (88)**: Excluded. Network protocol, not physical.
700. **xiaolu (88)**: Excluded. Chinese name, not physical.
701. **xiaotian (87)**: Excluded. Chinese name, not physical.
702. **x-cup (87)**: Excluded. Event or term, not clearly physical.
703. **xianwen (87)**: Excluded. Chinese name, not physical.
704. **xri (87)**: Excluded. Identifier system, not physical.
705. **xla (87)**: Excluded. Abbreviation or term, not physical.
706. **xingxing (87)**: Excluded. Chinese term or name, not physical.
707. **xmu (86)**: Excluded. Abbreviation (e.g., university), not physical.
708. **xerces (86)**: Excluded. Software library, not physical.
709. **xiangyun (86)**: Excluded. Chinese place or name, not physical.
710. **xaverius (86)**: Excluded. Variant of Xavier, not physical.
711. **xingtang (86)**: Excluded. Chinese place name, not physical.
712. **xíng (86)**: Excluded. Chinese character or term, not physical.
713. **xperiment (85)**: Excluded. Abstract term or brand, not physical.
714. **xiaoguang (85)**: Excluded. Chinese name, not physical.
715. **xenarthra (85)**: Excluded. Variant of xenarthrans, already included.
716. **xiaochun (85)**: Excluded. Chinese name, not physical.
717. **xylocarpa (85)**: **Included**. A species of tree, a physical plant.
718. **xiyuan (85)**: Excluded. Chinese place or name, not physical.
719. **xiaoqian (85)**: Excluded. Chinese name, not physical.
720. **xisco (85)**: Excluded. Proper name, not physical.
721. **xantia (85)**: **Included**. Citroën Xantia, a physical car model.
722. **xinwu (85)**: Excluded. Chinese place name, not physical.
723. **xyletobius (85)**: **Included**. A genus of beetles, physical organisms.
724. **xoanon (84)**: **Included**. A wooden statue in ancient Greece, a physical object.
725. **xsl-fo (84)**: Excluded. Formatting standard, not physical.
726. **xterm (84)**: Excluded. Terminal emulator, not physical.
727. **xoxe (84)**: Excluded. Name or term, not physical.
728. **xenotime (84)**: **Included**. A rare-earth mineral, a physical substance.
729. **xié (84)**: Excluded. Chinese character or name, not physical.
730. **xpd (83)**: Excluded. Abbreviation or term, not physical.
731. **xtrac (83)**: Excluded. Brand or technology, not a specific object.
732. **xantho (83)**: Excluded. Likely a name or genus, not specific without context.
733. **xel'naga (83)**: Excluded. Fictional species, not physical.
734. **xuntian (83)**: Excluded. Chinese name or term, not physical.
735. **xangsane (82)**: Excluded. Typhoon name, not a physical object.
736. **xuanling (82)**: Excluded. Chinese name, not physical.
737. **xbl (82)**: Excluded. Xbox Live or abbreviation, not physical.
738. **xiantao (82)**: Excluded. Chinese city, a geographical location.
739. **xdcam (82)**: **Included**. A professional video camera format, physical equipment.
740. **xanthophylls (82)**: Excluded. Plural of xanthophyll, already included.
741. **xixia (82)**: Excluded. Historical Chinese dynasty, not physical.
742. **xide (82)**: Excluded. Likely a name or term, not clearly physical.
743. **xacml (81)**: Excluded. Access control language, not physical.
744. **xylenes (81)**: Excluded. Plural of xylene, already included.
745. **xiumin (81)**: Excluded. Proper name, not physical.
746. **xizhimen (81)**: Excluded. Chinese place name, not physical.
747. **xhelal (81)**: Excluded. Proper name, not physical.
748. **x-faktor (81)**: Excluded. Variant of X-Factor, a show, not physical.
749. **xuesen (80)**: Excluded. Chinese name, not physical.
750. **xcii (80)**: Excluded. Roman numeral (92), not physical.
751. **xoài (80)**: **Included**. Vietnamese for mango, a physical fruit.
752. **xon (80)**: Excluded. Abbreviation or term, not physical.
753. **xceed (80)**: Excluded. Brand or term, not a specific object.
754. **xiaoxiao (80)**: Excluded. Chinese name, not physical.
755. **xylanase (79)**: **Included**. An