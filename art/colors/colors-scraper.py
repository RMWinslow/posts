# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:01:25 2021
tintuit color scheme generator
@author: RobertWinslow
"""

import urllib.request
from bs4 import BeautifulSoup
import re
#%%
def urlToStr(url):
    "This function returns a webpage's source as just a big ol' string."
    #load Url text
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    urlStr = mybytes.decode("ANSI")
    fp.close()  
    return urlStr
#%%
colorsoup = BeautifulSoup(urlToStr('https://web.archive.org/web/20121103030619/http://tx4.us/nbs-iscc.htm'), 'html.parser')

#%%
'''
colorrows = colorsoup.find_all('tr')
colorlist = []


def find_category(shortname):
    #categories are v., brill., s., deep, v. deep, v.l., l., m., d., v.d., v.p.,  
    #p., gy., d. gy., bk., 
    #ish white, l. ish gy., ish
    # Examples
    #   v.R 11 Vivid Red
    #   brill.O 49 Brilliant Orange
    #   s.O 50 Strong Orange
    #   deep O 51 Deep Orange
    #   v.deep yG 133 Very Deep Yellowish Green
    #
    #
    #
    #
    #
    #
    return None
    
    

def parse_namestring(namestring):
    altname = None
    if ',' in namestring:
        altname = namestring[namestring.find(',')+2:]
        namestring =  namestring[:namestring.find(',')]
    
    numberPos = re.search(r'\d+', namestring)
    shortname = namestring[:numberPos.start()-1]
    number = namestring[numberPos.start():numberPos.end()]
    fullname = namestring[numberPos.end():]
    
    #print(find_category(shortname))
    
    return shortname, number, fullname, altname



for row in colorrows:
     if row.td:
         cells = row.find_all('td')
         if cells[0].strong:
             namestring = cells[0].strong.contents[0]
             #first two are just OCT and 2011.
             if namestring not in ['Oct','2011']:
                 print(parse_namestring(namestring))
                 shortname, number, fullname, altname, category = parse_namestring(namestring)









'''

#%%
colorStr = urlToStr("http://people.csail.mit.edu/jaffer/Color/NBS-ISCC-rgb.txt")
colorLines = colorStr.split('\n')

#%%
#modifiers are v., brill., s., deep, v. deep, v.l., l., m., d., v.d., v.p.,  
#p., gy., d. gy., bk., 
#ish white, l. ish gy., ish
#Examples
'''
    vividgreenishblue
    brilliantgreenishblue
    strongyellowishgreen
    deepolivegreen
    verydeepreddishpurple
    verylightblue
    lightblue
    moderateyellowgreen
    verydarkbluishgreen
    verypalegreen
    paleyellowishpink
    lightgrayishred
    grayishbrown
    darkgrayishyellow
    blackishpurple
    
    greenishwhite
    lightgreenishgray
    greenishgray
    darkgreenishgray
    greenishblack
    
'''
#pale and light greyish are basically the same.

startmodifiers = ['brownish','lightgrayish','darkgrayish','vivid','brilliant','strong','deep','verydeep','verylight','light','moderate','dark','verydark','verypale','pale','grayish','blackish',]
#light  and dark grayish must come first because of reasons. That is, there is also light and dark.

endmodifiers = ['ishwhite','ishgray','ishblack',]
#ishgray has three variations depending on prefix darkishgray or lightishgray

def grab_mod(name):
    #Sadly, some names contain others, and there are special cases, so we're just going to have a bunch of cases.
    if name in ['white','lightgray','mediumgray','darkgray','black', 'oliveblack', 'olivegray']:
        return "nuetral"
    elif name.endswith('ishgray'):
        if name.startswith('dark'):
            return "darkishgray"
        elif name.startswith('light'):
            return "lightishgray"
        else:
            return "ishgray"
    elif name.endswith('ishwhite'): 
            return "ishwhite"
    elif name.endswith('ishblack'): 
            return "ishblack"
    else:
        for modifier in startmodifiers:
            if name.startswith(modifier):
                return modifier
    print(name)
    return "AAAAAAAAAAAAAAAAAAAA"
            
#%%
categories = ['red','orange','chartreuse','yellow','green','blue','purple','pink','brown','olive','white','gray','black',]
#moved special cases 'brownishpink','brownishorange' to brownish modifier
# I should rename the yellow-green to chartreuse. Just did
# Also, the yellowgreen needs to be checked first or else the simple parsing won't work.
#brown and pink need to come before gray
mixedcats = ['reddishorange','orangeyellow','yellowishpink','reddishbrown','yellowishbrown','olivebrown','greenishyellow','olivegreen','yellowishgreen','bluishgreen','greenishblue','purplishblue','violet','reddishpurple','purplishpink','purplishred']

def grab_cat(name):
    for cat in mixedcats+categories:
        if cat in name:
            return cat
    print("FOLLOW YOUR DREAMS")
    return "FOLLOW YOUR DREAMS"
#%%
colorDict = dict()
for count,line in enumerate(colorLines[9:-1]):
    if line[0] != '!':
        r,g,b,name = line.split()
        namereplacements = {
                'yellowgreen': 'chartreuse', #easier name distinction
                'pinkishgray': 'lightpinkishgray', #wrong luminosities
                'yellowishgray': 'lightyellowishgray',
                'brownishgray': 'darkbrownishgray',
                'lightbrownishgray': 'brownishgray',
                'olivegray': 'darkolivegray',
                'yellowgreen': 'chartreuse',
                'lightolivegray': 'olivegray',
                }
        if name in namereplacements:
            name = namereplacements[name]
        name = name.replace('yellowgreen','chartreuse') #easier name distinction
        if name == 'deepyellowishpink':
            b = '97' #typo in source e66761, not e66721
        if name == 'deepgreenishblue':
            r,g,b = '0','68','79' #bad guess
        if name == 'vividblue':
            r,g,b = '54','124','199' #bad guess
        if name == 'vividpurplishblue':
            r,g,b = '115','106','208' #too dark, increased L*
            
        hexnumber = 256*256*int(r) + 256*int(g) + int(b)
        hexcolor = '#' + f'{hexnumber:x}'.zfill(6)
        modifier = grab_mod(name)
        category = grab_cat(name)
        if modifier == 'lightgrayish':
            modifier = 'pale' #lightgrayish and pale are similar
        colorDict[(category,modifier)] = [name, r,g,b,hexcolor, category, modifier,count] 
        colorDict[name] = [name, r,g,b,hexcolor, category, modifier,count]  
        
        
#manually fill out the grays
colorDict['yellowishgray'] = ['yellowishgray','','','', '#898375','gray','yellowish',]
colorDict['darkyellowishgray'] = ['yellowishgray','','','', '#565249','darkgray','yellowish',]
colorDict['yellowishblack'] = ['yellowishgray','','','', '#23211d','black','yellowish',]
        
#%%Build the html
tableordermods = ['brilliant','vivid','strong','deep','verydeep','verylight','light','moderate','dark','verydark','verypale','pale','grayish','darkgrayish','blackish','brownish',]

tableordercats = [
    'red',
    'reddishorange',    
    'orange',    
    'orangeyellow',    
    'yellow',    
    'greenishyellow',    
    'chartreuse',    
    'yellowishgreen',
    'green',
    'bluishgreen',
    'greenishblue',
    'blue',
    'purplishblue',
    'violet',
    'purple',
    'reddishpurple',
    'purplishred',
    
    '',
    'purplishpink',
    'pink',   
    'yellowishpink', 
    
    '',
    #'white',
    #'gray',
    #'black',
    
    'reddishbrown',
    'brown',
    'yellowishbrown',
    'olivebrown',
    'olive',
    'olivegreen',
    ]

#keep track of covered colors.
coveredcolors = dict()

output = ''

output += '<table border="1">'

#header row
output += '<tr><th></th>'
for mod in tableordermods: 
    output += '<th>'+mod+'</th>'
output += '</tr>'
#row for each color category
for cat in tableordercats:
    output += '<tr><th>'+cat+'</th>'
    for mod in tableordermods:
        if (cat,mod) in colorDict:
            data = colorDict[(cat,mod)]
            output += '<td bgcolor="'+data[4]+'">'+str(data[7])+'<br>'+data[4]+'<br><span style="color:white;">'+data[4]+'</span></td>'
            coveredcolors[(cat,mod)] = 1
        else:
            output += '<td></td>'
    output += '</tr>'
output += '</table>'

print(output)




for color in colorDict:
    if color not in coveredcolors:
        if len(color) == 2:
            continue
            #print(colorDict[color])
            
            


#%%print the second neutral table
nuetrallist = [
        ['white','lightgray','mediumgray','darkgray','black',],
        ['','','reddishgray','darkreddishgray','reddishblack',],
        ['yellowishwhite','lightyellowishgray','yellowishgray','darkyellowishgray','yellowishblack',],
        ['greenishwhite','lightgreenishgray','greenishgray','darkgreenishgray','greenishblack',],
        ['bluishwhite','lightbluishgray','bluishgray','darkbluishgray','bluishblack',],
        ['purplishwhite','lightpurplishgray','purplishgray','darkpurplishgray','purplishblack',],
        ['pinkishwhite','lightpinkishgray','pinkishgray','','',],
        ['','lightbrownishgray','brownishgray','darkbrownishgray','brownishblack',],
        ['','lightolivegray','olivegray','darkolivegray','oliveblack',],
        ]
nrowlist = ['','reddish','yellowish','greenish','bluish','purplish','pinkish','brownish','olive-',]

output = ''

output += '<table border="1">'

#header row
output += '<tr><th></th>'
for mod in ['white','lightgray','mediumgray','darkgray','black',]: 
    output += '<th>'+mod+'</th>'
output += '</tr>'
#row for each color category
for j,rowlist in enumerate(nuetrallist):
    output += '<tr><th>'+nrowlist[j]+'</th>'
    for i,color in enumerate(rowlist):
        if color in colorDict:
            data = colorDict[color]
            output += '<td bgcolor="'+data[4]+'">'+data[4]+'<br><span style="color:white;">'+data[4]+'</span></td>'
        else:
            colcolor = colorDict[nuetrallist[0][i]][4]
            output += '<td bgcolor="'+colcolor+'">'+''+'</td>'
    output += '</tr>'
output += '</table>'

print(output)

#%%tiered rows


'''
output = ''

output += '<table border="1">'

#header row
output += '<tr><th></th>'
for mod in startmodifiers: 
    output += '<th  rowspan="2">'+mod+'</th>'
output += '</tr>'
#row for each color category
for cat in mixedcats+categories:
    output += '<tr><th>'+cat+'</th>'
    for mod in startmodifiers:
        if (cat,mod) in colorDict:
            data = colorDict[(cat,mod)]
            output += '<td bgcolor="'+data[4]+'">'+data[4]+'</td>'
        else:
            output += '<td></td>'
    output += '</tr>'
output += '</table>'




print(output)
'''


#%%TODO: Export to JSON




