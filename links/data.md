---
title: Online Data Sources
description: This is a short list of online data sources with which I am familiar. The focus is on sources of economics data, such as IPUMS
parent: Links
layout: post
toc: true
date: 2022-12-05
---

## Econ Data Sources


[FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/)
: Collects a bunch of different economics time series, mostly focused on US data. If you want to quickly see a graph of some US economic variable, your best bet is probably to google something like "FRED inflation" or "FRED gdp". 
: FRED also lets you compare and combine variables using the "Edit Graph" widget.
: Another nice feature of FRED are the 'release tables', which organize links to related data series. [Here's the table for annual GDP components](https://fred.stlouisfed.org/release/tables?rid=53&eid=41047), as an example. If a variable is part of one of these tables, you can find a link to the table by scrolling down on the variable's page.

[BEA's National Accounts](https://www.bea.gov/data)
: The Bureau of Economic Analysis is responsible for preparing the National Accounts for the US. 
: They publish [news releases](https://www.bea.gov/news/glance) which summarize economic changes.
: They also have their own [online data visualizer for national data](https://www.bea.gov/itable), though the interface is a bit janky. [Here is a link to a table of GDP components](https://apps.bea.gov/iTable/?reqid=19&step=2&isuri=1&categories=survey#eyJhcHBpZCI6MTksInN0ZXBzIjpbMSwyLDMsM10sImRhdGEiOltbImNhdGVnb3JpZXMiLCJTdXJ2ZXkiXSxbIk5JUEFfVGFibGVfTGlzdCIsIjUiXSxbIkZpcnN0X1llYXIiLCIxOTg2Il0sWyJMYXN0X1llYXIiLCIyMDIxIl0sWyJTY2FsZSIsIi05Il0sWyJTZXJpZXMiLCJBIl1dfQ==). To see a graph, click the 'chart' button, then select items on the left.

[stats.oecd.org](https://stats.oecd.org/)
: The OECD is like the group of 'rich countries'. This page provides tables of statistics from members of the OECD and several other countries as well. The site can be a bit slow, and doesn't play well on large screen, but I enjoy the dense nature of it.
: To find the table of GDP components, Click the expand `National Accounts` in the left sidebar, then `Annual National Accounts > Main Aggregates > 1. Gross domestic product (GDP)`. The view defaults to current price (nominal) GDP for Australia from 2015 to 2021. The country, measure, and years can all be changed by clicking on the arrows in the table header. 'Real' GDP can be found by changing the measure to "Constant prices, OECD Base Year".
: After adjusting the variables in a table, the data can be downloaded using the Export menu near the top of the page.

[Penn World Table v10.0](https://www.rug.nl/ggdc/productivity/pwt/)
: A relatively small spreadsheet that compiles time series on output, prices, and capital stocks from many different countries for the years 1950-2019.
: Has a focus on PPP-adjusted comparisons between countries. 

[Panel Study on Income Dynamics](https://simba.isr.umich.edu/data/data.aspx)
: Really long running panel data.

I've used data from the OECD stats page, FRED, and the Penn World Table to construct homework assignments or in-class exercises.

<!--
https://www.bls.gov/data/
https://data.worldbank.org/
https://tradingeconomics.com/


https://www.brookings.edu/events/graduate-workshop-health-economics-data-and-research-from-the-agency-for-healthcare-research-and-quality/
Medical Expenditure Panel Survey (MEPS) – Household Component (HC)
Healthcare Cost and Utilization Project (HCUP)
MEPS-Insurance Component (IC)

-->


### IPUMS (Integrated Public Use Microdata Series)

[IPUMS](https://www.ipums.org/)
is a great way to access the data from several different censuses and surveys.
The IPUMS website provides clean documentation for the survey questions,
and allows you to choose specific variables and samples to download.

*(I like to download data in the Stata .dta format, even though I don't like using Stata. It's easy to import into Python Pandas, and the files are more compact than a CSV.)*

<!--Although IPUMS is great, there are cases where going to the original data source is desired.
As such, I've included some links to the original surveys below as well.

[^blsexample][^blsexample]: For example, the American Time Use Survey collects 'diaries'-->

Here are a few of the data sets from IPUMS which I am familiar with:

[IPUMS USA](https://usa.ipums.org/usa-action/variables/group)
: Microdata from the US Census, as well as the Census Bureau's *[American Community Survey](https://www.census.gov/programs-surveys/acs/guidance/subjects.html)*.
: The Census also has [their own data portal](https://data.census.gov/), though I haven't explored its features.

<!--[Census quick facts](https://www.census.gov/quickfacts/fact/table/US/PST045221)-->


[IPUMS CPS](https://cps.ipums.org/cps-action/variables/group)
: Data from the BLS' [Current Population Survey](https://www.census.gov/programs-surveys/cps/data/datasets.html). 
: (The CPS is the source of the headline Labor Force Statistics for the US.)

[IPUMS Time Use](https://www.atusdata.org/atus-action/variables/group)
: The data set here I am most familiar with is the [American Time Use Survey](https://www.bls.gov/tus/#data), which is a supplement to the CPS. After their last CPS interview, some of the respondents are asked to describe a 'diary' of how they spent their time on the previous day.
: IPUMS also has [two other sources of Time Use data](https://timeuse.ipums.org/), which cover larger spans of time or include more countries. I haven't spent too much time looking at those.

Here is an [example documentation page](https://cps.ipums.org/cps-action/variables/EMPSTAT) for seeing what a data variable looks like on IPUMS.
The *codes* tab maps data codes to response descriptions, 
the *description* tab gives more details about what the variable is trying to measure, 
and the *universe* tab describes the set of people who were eligible to be asked this question. 
If someone in a survey was not eligible to be asked a question, then their response is coded as 'NIU' ('Not in Universe').



## GIS Data

[USGS Maps Online](https://www.usgs.gov/faqs/how-do-i-find-download-or-order-topographic-maps?qt-news_science_products=3#qt-news_science_products)
: The USGS used to publish paper maps of little snippets of the US. Nowadays, those maps are automatically generated from computerized data. [Here's a map viewer](https://apps.nationalmap.gov/viewer/); the GMNA Geological Map is very striking. 
: The USGS also lets you view historical geological survey maps with their "[topoview](https://ngmdb.usgs.gov/topoview/viewer/)" viewer; just click on an area and historical maps will appear. 
: [Here's a strange location](https://ngmdb.usgs.gov/topoview/viewer/#15/40.6639/-74.1003), where you can see ship wrecks build up over the decades until they're cleared out, and the bay is turned into a golf course.


[North American Environmental Atlas](http://www.cec.org/north-american-environmental-atlas/)
: Cec is NAFTA's environmental org. They have lots of interesting maps of the North American Environment.


[Natural Earth](https://www.naturalearthdata.com/)
: A small collection of simple, public domain world map datasets. Handy if you want to make a quick and simple map in something like QGIS.

<!--Weather data?-->


<!--
World Values Survey
https://www.worldvaluessurvey.org/wvs.jsp
Here's an attempt to visualize some of this data to get a "cultural distance". Seems a bit janky though.
http://culturaldistance.muth.io/
-->



## Links to Similar Lists

The above list contains only data sources that I am directly familiar with.
Here are some links to larger collections of data sources.


### Similar Lists with a Focus on Econ Data

[American Economics Association's Data Resources page](https://www.aeaweb.org/resources/data)
: Lists of resources for [US macro data](https://www.aeaweb.org/resources/data/us-macro-regional/us-macro-regional-more), [other US data](https://www.aeaweb.org/resources/data/us-other-data/us-other-data-more), and [international data](https://www.aeaweb.org/resources/data/intl/intl-more).

[University Library Guides](https://libguides.umn.edu/econdata)
: The above link goes to the UMN Library's page on Economics Data Resources. University libraries will often have similar pages for this and many other topics. [Here's the analogous page from the University of Kansas library](https://guides.lib.ku.edu/economics/web), for example.

<!--https://econdata.net/ linked above, but many of the links on the Ten Best Sites page are broken or point to strange places.-->


<!--
https://library.law.yale.edu/news/75-sources-economic-data-statistics-reports-and-commentary              *
https://www.quora.com/What-are-some-of-the-best-online-sources-for-raw-economic-data?share=1
https://guides.lib.virginia.edu/economics/data
https://economicsnetwork.ac.uk/data_sets
https://krannert.purdue.edu/centers/pcee/economics-help/economic-data-sources.php                          *
https://guides.lib.vt.edu/subject-guides/econ/data-sources
-->


### Eclectic Collections of Data Sets

[Kaggle's Datasets](https://www.kaggle.com/datasets)
: Kaggle is a website which runs online Machine-Learning competitions. To facilitate this, it hosts all manner of eclectic datasets.

[Stalib Datasets](http://lib.stat.cmu.edu/datasets/)
: A collection of open datasets, as well as links to other resources. Last updated in 2005; many of the links are broken. 

[NBER's Public Use Data Archive](https://www.nber.org/research/data?page=1&perPage=100)
: Mirrors of public data sources. Oddly organized and sometimes out of date.

[Papers with Code](https://paperswithcode.com/datasets)
: Datasets from machine learning papers.
