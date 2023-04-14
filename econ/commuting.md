---
title: Commuting Correlations
subtitle: Correlates with commuting time in the ATUS and PSID
layout: post
parent: Econ
date: 2023-04-10
last_modified_date: 2023-03-12
---

<!---->
<!--TODO: INCLUDE OTHER DEMOGRAPHIC FACTORS-->
<!--TODO: Redo with harmonized PSID-->
<!--TODO: Instead of Correlations, look at conditional averages for ind, occ, etc.-->

What determines the amount of time spent commuting? 
This post doesn't attempt to answer that question.

What this post does is simply look at the things which are *correlated* with time spent on commuting.

## American Time Use Survey

<!--The [Current Population Survey](https://www.bls.gov/cps/) is what the BLS uses to calculate employment statistics.
For some of the households surveyed for the CPS, 
one of the household members is selected to participate in a supplemental survey call the American Time Use Survey.-->

For the [American Time Use Survey (ATUS)](https://www.bls.gov/tus/), respondents are asked to describe a 'diary' of how they spent the previous day.

For the tables in this section, I look at the subset of ATUS Respondants who:
- Were interviewed between 2004 and 2019, inclusive.
- Spent at least one hour working during the diary day.

<!--- Were interviewed on a non-holiday weekday.
Have empstat == 'employed - at work'. There were a thousand respondants with working time > 0 who aren't employed. Confusing!-->

The latter condition is so we're not *just* looking at the difference 
between people who did and did not work on a given day. 
Though I don't do anything to exclude people who EG just do a few minutes of work at home.

There are a few different ways in which commuting can be measured in the ATUS data.
I describe several possibilities below 
and list the variables which are most strongly correlated with each measure
(within the subset of data described above).

<!--I list some the variables which are most strongly correlated (positively or negatively) with time spent on commuting.-->



### Travel Related to Work.

<!--Where can commuting data be found in the ATUS?-->

One of the statistics published by the BLS is time spent on *"Travel Related To Work".*
That sounds like commute time, and is related, but that measurement doesn't work quite how you might expect.

Here is how the ATUS assigns a purpose to travel time:
- If the travel ends at home, the travel is counted as being related to the last activity the person was doing before they left.
- Otherwise, if the travel ends somewhere else, the travel is counted as being related to whatever activity they do next.

Here are the time-use categories which are most strongly correlated with *Travel Related to Work*.
I've also thrown weekly earnings and hourly wages into the table as well.

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| bls_work |  | 0.38 |
| bls_work_working |  | 0.167 |
| msasize_5,000,000+ |  | 0.103 |
| sex_male |  | 0.099 |
| spsex_female |  | 0.097 |
| ind2_construction |  | 0.094 |
| fullpart_full time |  | 0.087 |
| occ2_construction and extraction occupations |  | 0.087 |
| fambus_no family business |  | 0.075 |
| clwkr_private, for profit |  | 0.073 |
| metro_metropolitan, balance of msa |  | 0.069 |
| fambus_resp_no |  | 0.069 |
| wt20 |  | 0.066 |
| citizen_foreign born, not a u.s. citizen |  | 0.065 |
| bls_work_workrel |  | 0.062 |
| spempstat_not employed |  | 0.057 |
| spempnot_not employed |  | 0.055 |
| statefip_new york |  | 0.051 |
| bls_pcare_groom |  | 0.05 |
| empstat_employed - at work |  | 0.047 |
| region_northeast |  | 0.047 |
| paidhour_not paid hourly |  | 0.047 |
| msasize_2,500,000 - 4,999,999 |  | 0.047 |
| fambus_spouse_no |  | 0.046 |
| day_tuesday |  | 0.045 |
| bpl_mexico |  | 0.044 |
| citizen_foreign born, u.s. citizen by naturalization |  | 0.043 |
|  | ... |  |
| hourwage |  | 0.001 |
|  | ... |  |
| uhrsworkt |  | -0.021 |
|  | ... |  |
| earnweek |  | -0.068 |
|  | ... |  |
| citizen_native, born in united states |  | -0.08 |
| bls_leis_soccom |  | -0.083 |
| fullpart_part time |  | -0.083 |
| bls_leis_travel |  | -0.084 |
| bls_leis_tv |  | -0.085 |
| bls_hhact_food |  | -0.087 |
| bls_purch_groc |  | -0.092 |
| sex_female |  | -0.099 |
| bls_hhact_hwork |  | -0.104 |
| bls_pcare |  | -0.106 |
| day_sunday |  | -0.108 |
| bls_leis_relax |  | -0.114 |
| scc_own |  | -0.116 |
| bls_pcare_sleep |  | -0.12 |
| scc_all |  | -0.123 |
| bls_purch |  | -0.124 |
| bls_purch_cons |  | -0.125 |
| bls_hhact |  | -0.142 |
| bls_leis_soc |  | -0.153 |
| bls_leis |  | -0.174 |

<!--
### Dwell 15 Travel Time

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| 'bls_work' |  | 0.364 |
| 'bls_work_working' |  | 0.222 |
| 'bls_carehh_travel' |  | 0.079 |
| 'bls_work_workrel' |  | 0.049 |
| 'bls_pcare_groom' |  | 0.043 |
| 'bls_pcare_travel' |  | 0.027 |
| 'bls_purch_travel' |  | 0.02 |
| 'bls_carehh_kideduc' |  | 0.013 |
| 'bls_hhact_travel' |  | 0.012 |
| 'bls_comm_travel' |  | 0.009 |
| 'bls_work_other' |  | 0.004 |
| 'dwell15_telephone' |  | 0.002 |
| 'bls_social_civic' |  | 0.001 |
|  | ... |  |
| 'hourwage' |  | -0.022 |
|  | ... |  |
| 'earnweek' |  | -0.085 |
|  | ... |  |
| 'bls_leis_sport' |  | -0.092 |
| 'bls_leis_tv' |  | -0.093 |
| 'bls_leis_soccom' |  | -0.1 |
| 'dwell15_purchcons' |  | -0.102 |
| 'bls_purch_groc' |  | -0.105 |
| 'bls_hhact_hwork' |  | -0.121 |
| 'bls_leis_relax' |  | -0.127 |
| 'bls_purch_cons' |  | -0.138 |
| 'bls_pcare' |  | -0.146 |
| 'bls_hhact' |  | -0.152 |
| 'bls_pcare_sleep' |  | -0.161 |
| 'bls_leis_soc' |  | -0.175 |
| 'bls_leis' |  | -0.197 |
-->

### Dwell 30 Travel Time


An alternate way to code travel time is described in [this article](https://www.bls.gov/opub/mlr/2018/article/what-is-the-impact-of-recoding-travel-activities-in-the-american-time-use-survey.htm).

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| 'dwell30_work' |  | 1.0 |
| 'bls_work' |  | 0.29 |
| 'bls_work_working' |  | 0.135 |
| 'bls_carehh_travel' |  | 0.11 |
| 'bls_purch_travel' |  | 0.105 |
| 'msasize_5,000,000+' |  | 0.096 |
| 'fambus_no family business' |  | 0.085 |
| 'fambus_resp_no' |  | 0.084 |
| 'ind2_construction' |  | 0.08 |
| 'occ2_construction and extraction occupations' |  | 0.079 |
| 'fullpart_full time' |  | 0.075 |
| 'clwkr_private, for profit' |  | 0.071 |
| 'spsex_female' |  | 0.069 |
| 'metro_metropolitan, balance of msa' |  | 0.068 |
| 'kidund18_yes' |  | 0.062 |
| 'kidund13_yes' |  | 0.056 |
| 'statefip_new york' |  | 0.055 |
| 'day_tuesday' |  | 0.053 |
| 'empstat_employed - at work' |  | 0.051 |
| 'sex_male' |  | 0.05 |
| 'region_northeast' |  | 0.049 |
|  | ... |  |
| 'hourwage' |  | -0.01 |
|  | ... |  |
| 'uhrsworkt' |  | -0.026 |
|  | ... |  |
| 'earnweek' |  | -0.085 |
| 'dwell30_social' |  | -0.086 |
| 'dwell30_purchcons' |  | -0.087 |
| 'bls_leis_soccom' |  | -0.09 |
| 'bls_leis_sport' |  | -0.09 |
| 'scc_all' |  | -0.092 |
| 'bls_leis_relax' |  | -0.095 |
| 'bls_hhact_hwork' |  | -0.096 |
| 'day_saturday' |  | -0.099 |
| 'bls_purch_cons' |  | -0.101 |
| 'bls_hhact' |  | -0.104 |
| 'day_sunday' |  | -0.133 |
| 'bls_pcare' |  | -0.134 |
| 'bls_leis_soc' |  | -0.141 |
| 'bls_pcare_sleep' |  | -0.151 |
| 'bls_leis' |  | -0.162 |



A few things I notice change with this recoding:
- Variables related to taking kids to school (*`kidund18_yes`*, *`bls_carehh_travel`*) are now correlated with this measure of commute time. This makes sense. If you go out of your way to drop your kids off mid-commute, then the standard rule cuts your commute time in half, while this rules extends it.
- Likewise, the strength of the *`sex_male`* correlation is weakened.



<!--
## PSID

Correlations of time spent commuting by primary respondant.

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| 'time_commute2' |  | 0.149 |
| 'realcost_transportation_variable' |  | 0.122 |
| 'cost_transportation_variable' |  | 0.121 |
| 'cost_total' |  | 0.091 |
| 'realcost_total' |  | 0.091 |
| 'realcost_transportation' |  | 0.088 |
| 'cost_transportation' |  | 0.087 |
| 'realtotallaborincome1' |  | 0.07 |
| 'totallaborincome1' |  | 0.069 |
| 'realwageandsal1' |  | 0.067 |
| 'wageandsal1' |  | 0.067 |
| 'realcost_housing' |  | 0.065 |
| 'realwagerate1' |  | 0.065 |
| 'cost_housing' |  | 0.064 |
| 'wagerate1' |  | 0.064 |
| 'realcost_telecom' |  | 0.058 |
| 'cost_telecom' |  | 0.057 |
| 'time_work1' |  | 0.053 |
| 'realcost_food' |  | 0.05 |
| 'cost_food' |  | 0.049 |
| 'race2' |  | 0.046 |
| 'sex2' |  | 0.046 |
| 'realfamilyincome' |  | 0.044 |
| 'familyincome' |  | 0.044 |
| 'time_housework2' |  | 0.043 |
| 'actualhourlywage1' |  | 0.042 |
| 'realactualhourlywage1' |  | 0.042 |
| 'realcost_utility' |  | 0.04 |
| 'cost_utility' |  | 0.039 |
| 'time_work1_alt' |  | 0.039 |
| 'realcost_clothing' |  | 0.038 |
| 'cost_clothing' |  | 0.038 |
| 'time_childcare2' |  | 0.037 |
| 'realcost_childcare' |  | 0.036 |
| 'cost_childcare' |  | 0.036 |
| 'realcost_health' |  | 0.035 |
| 'cost_health' |  | 0.035 |
| 'time_totalhours1' |  | 0.034 |
| 'time_work1_altalt' |  | 0.034 |
| 'cohort2' |  | 0.033 |
| 'age2' |  | 0.032 |
| 'realcost_homeinsurance' |  | 0.032 |
| 'cost_homeinsurance' |  | 0.032 |
| 'nkids' |  | 0.032 |
| 'time_work2_alt' |  | 0.031 |
| 'realcost_trips' |  | 0.029 |
| 'cost_trips' |  | 0.029 |
| 'time_pcare2' |  | 0.027 |
| 'time_work2' |  | 0.027 |
| 'time_totalhours2' |  | 0.025 |
| 'time_work2_altalt' |  | 0.025 |
| 'race1' |  | 0.024 |
| 'month' |  | 0.023 |
| 'time_education2' |  | 0.023 |
| 'time_leisure2' |  | 0.02 |
| 'totallaborincome2' |  | 0.019 |
| 'realtotallaborincome2' |  | 0.019 |
| 'Unnamed: 0' |  | 0.019 |
| 'wageandsal2' |  | 0.018 |
| 'realwageandsal2' |  | 0.018 |
| 'time_shopping2' |  | 0.016 |
| 'cost_education' |  | 0.016 |
| 'realcost_education' |  | 0.016 |
| 'wagerate2' |  | 0.013 |
| 'realwagerate2' |  | 0.013 |
| 'time_volunteering2' |  | 0.013 |
| 'realactualhourlywage2' |  | 0.012 |
| 'actualhourlywage2' |  | 0.012 |
| 'realcost_homerepair' |  | 0.012 |
| 'cost_homerepair' |  | 0.011 |
| 'id' |  | 0.009 |
| 'realcost_recreation' |  | 0.008 |
| 'cost_recreation' |  | 0.008 |
| 'time_childcare1' |  | 0.008 |
| 'realcost_furnish' |  | 0.007 |
| 'cost_furnish' |  | 0.006 |
| 'time_adultcare2' |  | -0.002 |
| 'time_volunteering1' |  | -0.008 |
| 'cohort1' |  | -0.009 |
| 'age1' |  | -0.011 |
| 'time_education1' |  | -0.013 |
| 'CPI99' |  | -0.016 |
| 'year' |  | -0.016 |
| 'time_adultcare1' |  | -0.016 |
| 'realcost_home' |  | -0.017 |
| 'cost_home' |  | -0.017 |
| 'time_pcare1' |  | -0.02 |
| 'time_housework1' |  | -0.028 |
| 'time_shopping1' |  | -0.028 |
| 'time_leisure1' |  | -0.032 |
| 'sex1' |  | -0.033 |
| 'weight' |  | -0.035 |
-->
