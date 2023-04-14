---
title: Commuting Correlations
subtitle: Correlates with commuting time in the ATUS and PSID
layout: post
parent: Econ
date: 2023-04-10
last_modified_date: 2023-03-13
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






## LASSO Regressions on ATUS Work From Home Module

[LASSO](https://en.wikipedia.org/wiki/Lasso_(statistics)) is a kind of regularized linear regression.
It adds a penalty for large coefficients, and sets a lot of coefficients to zero when fit.

In 2017 and 2018, ATUS included a [leave module](https://www.bls.gov/tus/modules/lvdatafiles.htm), 
which asked some respondants about their work schedules, including their situation 
regarding working from home.

In this section, I fit a few of these leave module variables to a LASSO regression.
The `y` variable is the dummy for the affirmative reponse to the question in the header.
LASSO parameters was chosen via 5-fold cross validation.
Variables were scaled before being plugged into the regression, and so the coefficients in the full tables aren't directly interpretable.







### As part of your (main) job, can you work at home?

Biggest positive predictors of ability to work from home:
- working in a compsci/math occupation
- working in business or finance
- working in arts / entertainment / media
- having flexible work hours
- working in the insurance industry

Biggest negative predictors
- being paid hourly
- being a healthcare practitioner
- being a local government work
- working in production occupations
- working in transportation


<details markdown="block"><summary>Click for full list of coeficients.</summary>

| Variable Name | coef |
|:-:|:-:|
| paidhour_paid hourly | -0.178 |
| occ2_healthcare practitioner and technical occupations | -0.138 |
| clwkr_government, local | -0.089 |
| occ2_production occupations | -0.086 |
| occ2_transportation and material moving occupations | -0.085 |
| occ2_installation, maintenance, and repair occupations | -0.078 |
| occ2_construction and extraction occupations | -0.077 |
| ind2_retail trade | -0.066 |
| ind2_transportation and warehousing | -0.062 |
| occ2_building and grounds cleaning and maintenance occupations | -0.062 |
| wrkflexfreq_rarely | -0.057 |
| ind2_food services and drinking places | -0.055 |
| wrkschedsat_yes | -0.054 |
| wrkflexinput_employer decides | -0.051 |
| wrknumus_5 days | -0.046 |
| wrkschedvary_yes | -0.039 |
| wrknumus_4 days | -0.039 |
| educyrs_twelfth grade | -0.033 |
| metro_nonmetropolitan | -0.033 |
| ind2_hospitals | -0.03 |
| kidund1_yes | -0.026 |
| ind2_arts, entertainment, and recreation | -0.025 |
| statefip_california | -0.024 |
| statefip_illinois | -0.024 |
| educyrs_eleventh grade | -0.023 |
| educyrs_college--two years | -0.023 |
| clwkr_government, federal | -0.021 |
| rcvpdlv_no | -0.019 |
| region_northeast | -0.018 |
| ind2_construction | -0.015 |
| occ2_healthcare support occupations | -0.014 |
| ind2_agriculture | -0.013 |
| marst_widowed | -0.012 |
| rcvunpdlv_no | -0.012 |
| famincome_$30,000 to $34,999 | -0.012 |
| statefip_pennsylvania | -0.011 |
| race_black only | -0.011 |
| hh_size | -0.01 |
| famincome_$75,000 to $99,999 | -0.01 |
| diffany_no difficulty | -0.01 |
| wrkschedus_rotating shift- hours change periodically | -0.009 |
| famincome_$15,000 to $19,999 | -0.009 |
| statefip_alabama | -0.009 |
| spusualhrs_40 | -0.008 |
| multjobs_yes | -0.007 |
| msasize_100,000 - 249,999 | -0.007 |
| citizen_foreign born, u.s. citizen by naturalization | -0.007 |
| msasize_5,000,000+ | -0.007 |
| statefip_florida | -0.006 |
| wrkshiftrsn_nature of the job | -0.006 |
| month_may | -0.006 |
| day_thursday | -0.005 |
| otpay | -0.005 |
| kidund13_yes | -0.004 |
| hhtenure_owned or being bought by a household member | -0.004 |
| occ2_personal care and service occupations | -0.004 |
| statefip_new york | -0.004 |
| occ2_food preparation and serving related occupations | -0.003 |
| month_december | -0.003 |
| famincome_$20,000 to $24,999 | -0.003 |
| ind2_public administration | -0.002 |
| tklvwk_no | -0.002 |
| wrkschedtue_yes | -0.001 |
| hh_numadults | -0.001 |
| wrkschedsun_yes | -0.001 |
| educyrs_tenth grade | -0.001 |
| wrkflexpol_blank | -0.0 |
| speduc_high school graduate - diploma | -0.0 |
| region_midwest | -0.0 |
| wrkflexfreq_blank | -0.0 |
| ageychild | 0.0 |
| citizen_foreign born, not a u.s. citizen | -0.0 |
| citizen_native, born abroad of american parent or parents | 0.0 |
| citizen_native, born in puerto rico or u.s. outlying area | -0.0 |
| clwkr_government, state | 0.0 |
| day_friday | -0.0 |
| day_monday | -0.0 |
| day_saturday | -0.0 |
| day_tuesday | 0.0 |
| diffmob_no mobility limitation | -0.0 |
| educyrs_college--one year | 0.0 |
| educyrs_college--three years | 0.0 |
| educyrs_fifth through sixth grade | -0.0 |
| educyrs_first through fourth grade | -0.0 |
| educyrs_ninth grade | -0.0 |
| educyrs_seventh through eighth grade | -0.0 |
| empstat_employed - at work | 0.0 |
| fambus_no family business | -0.0 |
| fambus_pay_niu (not in universe) | 0.0 |
| fambus_pay_no | -0.0 |
| famincome_$10,000 to $12,499 | 0.0 |
| famincome_$12,500 to $14,999 | 0.0 |
| famincome_$25,000 to $29,999 | -0.0 |
| famincome_$35,000 to $39,999 | 0.0 |
| famincome_$40,000 to $49,999 | -0.0 |
| famincome_$5,000 to $7,499 | -0.0 |
| famincome_$7,500 to $9,999 | 0.0 |
| famincome_less than $5,000 | -0.0 |
| fullpart_part time | 0.0 |
| hh_numkids | -0.0 |
| hhtenure_rented for cash | 0.0 |
| holiday_yes | -0.0 |
| housetype_mobile home or trailer with 1 or more rooms added | 0.0 |
| housetype_mobile home or trailer with no permanent room added | -0.0 |
| hrslvwk | -0.0 |
| ind2_beverage and tobacco product mfg | 0.0 |
| ind2_broadcasting (except internet) | 0.0 |
| ind2_chemical manufacturing | 0.0 |
| ind2_computer and electronic product mfg | 0.0 |
| ind2_educational services | -0.0 |
| ind2_electrical equipment, appliance mfg | 0.0 |
| ind2_food manufacturing | -0.0 |
| ind2_forestry, logging, fishing, hunting, and trapping | 0.0 |
| ind2_furniture and fixtures manufacturing | 0.0 |
| ind2_health care services, except hospitals | -0.0 |
| ind2_machinery manufacturing | -0.0 |
| ind2_management of companies and enterprises | -0.0 |
| ind2_mining | -0.0 |
| ind2_miscellaneous and not specified mfg | 0.0 |
| ind2_motion picture and sound recording industries | -0.0 |
| ind2_nonmetallic mineral product manufacturing | -0.0 |
| ind2_other information services | -0.0 |
| ind2_paper manufacturing and printing | 0.0 |
| ind2_personal and laundry services | 0.0 |
| ind2_petroleum and coal products manufacturing | -0.0 |
| ind2_plastics and rubber products manufacturing | 0.0 |
| ind2_primary metals and fabricated metal products | -0.0 |
| ind2_private households | -0.0 |
| ind2_publishing industries (except internet) | 0.0 |
| ind2_rental and leasing services | 0.0 |
| ind2_repair and maintenance | -0.0 |
| ind2_social assistance | 0.0 |
| ind2_telecommunications | 0.0 |
| ind2_textile, apparel, and leather manufacturing | 0.0 |
| ind2_transportation equipment manufacturing | 0.0 |
| ind2_traveler accommodation | -0.0 |
| ind2_utilities | -0.0 |
| ind2_waste management and remediation services | -0.0 |
| ind2_wholesale trade | 0.0 |
| ind2_wood product manufacturing | -0.0 |
| kid1to2_yes | 0.0 |
| kid3to5_yes | 0.0 |
| marst_divorced | 0.0 |
| marst_married - spouse absent | 0.0 |
| marst_married - spouse present | 0.0 |
| marst_never married | -0.0 |
| marst_separated | 0.0 |
| metro_metropolitan, central city | -0.0 |
| metro_not identified | -0.0 |
| month_august | 0.0 |
| month_january | -0.0 |
| month_july | -0.0 |
| month_june | -0.0 |
| month_march | -0.0 |
| month_november | 0.0 |
| month_september | -0.0 |
| msasize_1,000,000 - 2,499,999 | 0.0 |
| msasize_250,000 - 499,999 | -0.0 |
| msasize_500,000 - 999,999 | 0.0 |
| msasize_not identified or non-metropolitan | -0.0 |
| occ2_farming, fishing, and forestry occupations | -0.0 |
| occ2_legal occupations | 0.0 |
| occ2_life, physical, and social science occupations | 0.0 |
| occ2_protective service occupations | -0.0 |
| race_american indian, alaskan native | 0.0 |
| race_asian only | -0.0 |
| race_hawaiian pacific islander only | 0.0 |
| race_white-american indian | -0.0 |
| race_white-asian | 0.0 |
| race_white-black | -0.0 |
| rcvpdlv_don't know | 0.0 |
| rcvpdlv_yes | 0.0 |
| rcvunpdlv_don't know | -0.0 |
| schlcoll_college/university full time | 0.0 |
| schlcoll_college/university part time | 0.0 |
| schlcoll_high school full time | -0.0 |
| schlcoll_niu (not in universe) | -0.0 |
| schlcoll_not enrolled | -0.0 |
| sex_male | -0.0 |
| speduc_10th grade | -0.0 |
| speduc_11th grade | -0.0 |
| speduc_12th grade - no diploma | -0.0 |
| speduc_1st, 2nd, 3rd, or 4th grade | -0.0 |
| speduc_5th or 6th grade | 0.0 |
| speduc_7th or 8th grade | -0.0 |
| speduc_9th grade | -0.0 |
| speduc_associate degree - academic program | 0.0 |
| speduc_associate degree - occupational vocational | 0.0 |
| speduc_bachelor's degree (ba, ab, bs, etc.) | 0.0 |
| speduc_doctoral degree (phd, edd, etc.) | 0.0 |
| speduc_high school graduate - ged | 0.0 |
| speduc_master's degree (ma, ms, meng, med, msw, etc.) | 0.0 |
| speduc_niu (not in universe) | -0.0 |
| speduc_not available (see description) | 0.0 |
| speduc_professional school degree (md, dds, dvm, etc.) | -0.0 |
| speduc_some college but no degree | 0.0 |
| spempnot_employed | -0.0 |
| spempnot_niu (not in universe) | -0.0 |
| spempstat_disabled | 0.0 |
| spempstat_employed - at work | 0.0 |
| spempstat_employed - not at work | -0.0 |
| spempstat_niu (not in universe) | -0.0 |
| spempstat_not employed | 0.0 |
| spempstat_retired | 0.0 |
| spousepres_no spouse or unmarried partner present | -0.0 |
| spousepres_unmarried partner present | -0.0 |
| sprace_american indian, alaskan native | -0.0 |
| sprace_asian only | -0.0 |
| sprace_black only | 0.0 |
| sprace_hawaiian pacific islander only | 0.0 |
| sprace_niu (not in universe) | -0.0 |
| sprace_not available (see description) | 0.0 |
| sprace_white-american indian | -0.0 |
| sprace_white-asian | -0.0 |
| sprace_white-black | 0.0 |
| spsex_female | -0.0 |
| spsex_niu (not in universe) | -0.0 |
| spusualhrs_10 | 0.0 |
| spusualhrs_12 | -0.0 |
| spusualhrs_15 | 0.0 |
| spusualhrs_16 | -0.0 |
| spusualhrs_20 | -0.0 |
| spusualhrs_24 | 0.0 |
| spusualhrs_25 | -0.0 |
| spusualhrs_32 | 0.0 |
| spusualhrs_35 | -0.0 |
| spusualhrs_36 | -0.0 |
| spusualhrs_37 | 0.0 |
| spusualhrs_38 | -0.0 |
| spusualhrs_4 | -0.0 |
| spusualhrs_42 | 0.0 |
| spusualhrs_44 | -0.0 |
| spusualhrs_45 | -0.0 |
| spusualhrs_46 | 0.0 |
| spusualhrs_48 | -0.0 |
| spusualhrs_55 | 0.0 |
| spusualhrs_65 | 0.0 |
| spusualhrs_70 | -0.0 |
| spusualhrs_8 | -0.0 |
| spusualhrs_99 | -0.0 |
| spusualhrs_hours vary | -0.0 |
| spusualhrs_niu (not in universe) | 0.0 |
| statefip_alaska | 0.0 |
| statefip_arizona | -0.0 |
| statefip_arkansas | -0.0 |
| statefip_colorado | 0.0 |
| statefip_connecticut | -0.0 |
| statefip_delaware | 0.0 |
| statefip_district of columbia | 0.0 |
| statefip_georgia | -0.0 |
| statefip_hawaii | 0.0 |
| statefip_idaho | 0.0 |
| statefip_indiana | -0.0 |
| statefip_iowa | 0.0 |
| statefip_kansas | -0.0 |
| statefip_kentucky | 0.0 |
| statefip_louisiana | 0.0 |
| statefip_maine | -0.0 |
| statefip_maryland | -0.0 |
| statefip_michigan | 0.0 |
| statefip_minnesota | -0.0 |
| statefip_mississippi | 0.0 |
| statefip_missouri | -0.0 |
| statefip_montana | 0.0 |
| statefip_nebraska | -0.0 |
| statefip_nevada | -0.0 |
| statefip_new hampshire | -0.0 |
| statefip_new mexico | 0.0 |
| statefip_north carolina | 0.0 |
| statefip_north dakota | -0.0 |
| statefip_ohio | -0.0 |
| statefip_oklahoma | -0.0 |
| statefip_rhode island | -0.0 |
| statefip_south carolina | 0.0 |
| statefip_south dakota | -0.0 |
| statefip_texas | 0.0 |
| statefip_utah | -0.0 |
| statefip_vermont | 0.0 |
| statefip_virginia | 0.0 |
| statefip_washington | -0.0 |
| statefip_west virginia | 0.0 |
| statefip_wyoming | 0.0 |
| tklvwk_yes | 0.0 |
| tklvwktype_blank | -0.0 |
| tklvwktype_paid for all | 0.0 |
| tklvwktype_paid for some | -0.0 |
| tklvwktype_unpaid for all | -0.0 |
| vetstat_niu (not in universe) | -0.0 |
| vetstat_veteran | -0.0 |
| wrkflexinput_other | 0.0 |
| wrkflexinput_worker has some input | -0.0 |
| wrkflexpol_formal program or policy | 0.0 |
| wrkflexpol_informal arrangement | 0.0 |
| wrknumus_1 day | 0.0 |
| wrknumus_2 days | -0.0 |
| wrknumus_3 days | -0.0 |
| wrknumus_6 days | 0.0 |
| wrkschedfri_yes | -0.0 |
| wrkschedthu_yes | 0.0 |
| wrkschedus_evening shift- most work done b/w 2p & 12a | -0.0 |
| wrkschedus_night shift- most work done b/w 9p & 8a | -0.0 |
| wrkschedus_some other shift | -0.0 |
| wrkschedus_split shift- two distinct periods each day | 0.0 |
| wrkshiftrsn_allows time for school | -0.0 |
| wrkshiftrsn_better arrangements for family or childcare | 0.0 |
| wrkshiftrsn_better pay | -0.0 |
| wrkshiftrsn_could not get any other shift | 0.0 |
| wrkshiftrsn_other | 0.0 |
| wrkshiftrsn_personal preference | -0.0 |
| wrkflexinput_blank | 0.0 |
| wrkflexfreq_occasionally | 0.0 |
| kid13to17_yes | 0.0 |
| metro_metropolitan, balance of msa | 0.0 |
| ind2_finance | 0.0 |
| rcvunpdlv_yes | 0.002 |
| region_south | 0.002 |
| month_april | 0.002 |
| wrkschedmon_yes | 0.002 |
| region_west | 0.003 |
| age | 0.003 |
| uhrsworkt | 0.004 |
| logearnweek | 0.005 |
| statefip_new jersey | 0.005 |
| spusualhrs_60 | 0.005 |
| spempnot_not employed | 0.006 |
| wrkshiftrsn_blank | 0.006 |
| famincome_$100,000 to $149,999 | 0.006 |
| metro_metropolitan, not identified | 0.007 |
| race_white only | 0.007 |
| spousepres_spouse present | 0.008 |
| statefip_tennessee | 0.008 |
| spusualhrs_50 | 0.008 |
| famincome_$50,000 to $59,999 | 0.008 |
| day_sunday | 0.009 |
| ind2_administrative and support services | 0.009 |
| famincome_$60,000 to $74,999 | 0.009 |
| hh_numownkids | 0.01 |
| wrknumus_7 days | 0.01 |
| spearnweek | 0.01 |
| wrkdaysavg | 0.01 |
| month_february | 0.011 |
| occ2_community and social service occupations | 0.011 |
| famincome_$150,000 and over | 0.011 |
| month_october | 0.011 |
| day_wednesday | 0.013 |
| msasize_2,500,000 - 4,999,999 | 0.013 |
| wrkschedus_daytime- most work done b/w 6a & 6p | 0.013 |
| statefip_massachusetts | 0.013 |
| clwkr_private, for profit | 0.014 |
| wrkschedwed_yes | 0.015 |
| sprace_white only | 0.015 |
| statefip_wisconsin | 0.015 |
| spusualhrs_28 | 0.017 |
| kid6to12_yes | 0.018 |
| housetype_house, apartment, flat | 0.02 |
| spsex_male | 0.021 |
| occ2_architecture and engineering occupations | 0.021 |
| hourwage | 0.022 |
| statefip_oregon | 0.023 |
| vetstat_non-veteran | 0.024 |
| tklvwk_blank | 0.025 |
| occ2_office and administrative support occupations | 0.025 |
| spusualhrs_30 | 0.025 |
| citizen_native, born in united states | 0.028 |
| fambus_family business | 0.029 |
| clwkr_private, nonprofit | 0.031 |
| wrkschedus_irregular schedule | 0.033 |
| educyrs_college--four years | 0.038 |
| wrkschedwk_yes | 0.039 |
| occ2_education, training, and library occupations | 0.042 |
| educyrs_bachelor's degree | 0.043 |
| occ2_sales and related occupations | 0.048 |
| earnweek | 0.05 |
| hhtenure_occupied without payment of cash rent | 0.051 |
| ind2_professional, scientific, and technical services | 0.077 |
| ind2_membership associations and organizations | 0.082 |
| educyrs_professional degree | 0.084 |
| ind2_real estate | 0.085 |
| educyrs_master's degree | 0.088 |
| educyrs_doctoral degree | 0.101 |
| occ2_management occupations | 0.111 |
| wrkflexfreq_frequent basis | 0.121 |
| ind2_insurance | 0.126 |
| wrkflexhrs_yes | 0.14 |
| occ2_arts, design, entertainment, sports, and media occupations | 0.142 |
| occ2_business and financial operations occupations | 0.185 |
| occ2_computer and mathematical science occupations | 0.236 |

</details>











### Are there days when you work only at home?


Biggest positive predictors of having days where you work from home:
- working in a compsci/math occupation
- working in the insurance industry
- working in business or finance
- having flexible work start/stop times
- working in professional, scientific, and technical services

Biggest negative predictors
- being paid hourly
- being a local government work
- being a healthcare practitioner
- having inflexible work start/stop times
- working in retail 


<details markdown="block"><summary>Click for full list of coeficients.</summary>

| Variable Name | coef |
|:-:|:-:|
| paidhour_paid hourly | -0.078 |
| clwkr_government, local | -0.078 |
| occ2_healthcare practitioner and technical occupations | -0.066 |
| wrkflexfreq_rarely | -0.05 |
| ind2_retail trade | -0.04 |
| wrknumus_5 days | -0.039 |
| ind2_food services and drinking places | -0.033 |
| citizen_foreign born, u.s. citizen by naturalization | -0.026 |
| sex_male | -0.024 |
| ind2_transportation and warehousing | -0.021 |
| occ2_installation, maintenance, and repair occupations | -0.021 |
| clwkr_government, federal | -0.021 |
| logearnweek | -0.017 |
| statefip_pennsylvania | -0.017 |
| wrkflexinput_employer decides | -0.015 |
| wrknumus_4 days | -0.015 |
| educyrs_twelfth grade | -0.015 |
| occ2_transportation and material moving occupations | -0.013 |
| educyrs_college--two years | -0.012 |
| wrkschedsat_yes | -0.011 |
| statefip_california | -0.011 |
| famincome_$20,000 to $24,999 | -0.01 |
| month_july | -0.009 |
| hh_size | -0.009 |
| diffany_no difficulty | -0.009 |
| tklvwk_no | -0.008 |
| spusualhrs_40 | -0.008 |
| hhtenure_owned or being bought by a household member | -0.008 |
| marst_never married | -0.007 |
| ind2_construction | -0.007 |
| educyrs_eleventh grade | -0.007 |
| ind2_hospitals | -0.006 |
| ind2_educational services | -0.006 |
| month_september | -0.005 |
| occ2_production occupations | -0.005 |
| metro_nonmetropolitan | -0.004 |
| rcvunpdlv_no | -0.004 |
| otpay | -0.004 |
| uhrsworkt | -0.004 |
| statefip_florida | -0.003 |
| hh_numadults | -0.003 |
| kidund13_yes | -0.002 |
| wrkschedfri_yes | -0.002 |
| msasize_100,000 - 249,999 | -0.002 |
| ind2_arts, entertainment, and recreation | -0.002 |
| statefip_alabama | -0.002 |
| hh_numkids | -0.001 |
| statefip_idaho | -0.001 |
| day_saturday | -0.001 |
| spusualhrs_niu (not in universe) | -0.0 |
| famincome_$75,000 to $99,999 | -0.0 |
| wrkflexpol_blank | -0.0 |
| age | -0.0 |
| ageychild | 0.0 |
| citizen_foreign born, not a u.s. citizen | 0.0 |
| citizen_native, born abroad of american parent or parents | 0.0 |
| citizen_native, born in puerto rico or u.s. outlying area | -0.0 |
| clwkr_government, state | 0.0 |
| day_monday | -0.0 |
| day_sunday | -0.0 |
| day_thursday | -0.0 |
| day_tuesday | 0.0 |
| diffmob_no mobility limitation | 0.0 |
| educyrs_college--one year | -0.0 |
| educyrs_college--three years | 0.0 |
| educyrs_fifth through sixth grade | -0.0 |
| educyrs_first through fourth grade | 0.0 |
| educyrs_ninth grade | -0.0 |
| educyrs_seventh through eighth grade | -0.0 |
| educyrs_tenth grade | -0.0 |
| empstat_employed - at work | 0.0 |
| fambus_no family business | -0.0 |
| fambus_pay_niu (not in universe) | -0.0 |
| fambus_pay_no | 0.0 |
| famincome_$10,000 to $12,499 | 0.0 |
| famincome_$12,500 to $14,999 | -0.0 |
| famincome_$15,000 to $19,999 | -0.0 |
| famincome_$25,000 to $29,999 | -0.0 |
| famincome_$30,000 to $34,999 | -0.0 |
| famincome_$40,000 to $49,999 | -0.0 |
| famincome_$5,000 to $7,499 | 0.0 |
| famincome_$60,000 to $74,999 | -0.0 |
| famincome_$7,500 to $9,999 | 0.0 |
| famincome_less than $5,000 | -0.0 |
| fullpart_part time | -0.0 |
| hhtenure_occupied without payment of cash rent | 0.0 |
| hhtenure_rented for cash | 0.0 |
| holiday_yes | -0.0 |
| housetype_house, apartment, flat | 0.0 |
| housetype_mobile home or trailer with 1 or more rooms added | 0.0 |
| housetype_mobile home or trailer with no permanent room added | -0.0 |
| ind2_administrative and support services | 0.0 |
| ind2_agriculture | -0.0 |
| ind2_beverage and tobacco product mfg | 0.0 |
| ind2_broadcasting (except internet) | 0.0 |
| ind2_computer and electronic product mfg | -0.0 |
| ind2_electrical equipment, appliance mfg | 0.0 |
| ind2_finance | 0.0 |
| ind2_food manufacturing | -0.0 |
| ind2_forestry, logging, fishing, hunting, and trapping | -0.0 |
| ind2_furniture and fixtures manufacturing | 0.0 |
| ind2_health care services, except hospitals | 0.0 |
| ind2_machinery manufacturing | -0.0 |
| ind2_management of companies and enterprises | -0.0 |
| ind2_mining | -0.0 |
| ind2_motion picture and sound recording industries | -0.0 |
| ind2_nonmetallic mineral product manufacturing | -0.0 |
| ind2_other information services | -0.0 |
| ind2_paper manufacturing and printing | -0.0 |
| ind2_personal and laundry services | -0.0 |
| ind2_petroleum and coal products manufacturing | 0.0 |
| ind2_plastics and rubber products manufacturing | -0.0 |
| ind2_primary metals and fabricated metal products | -0.0 |
| ind2_private households | -0.0 |
| ind2_public administration | -0.0 |
| ind2_rental and leasing services | -0.0 |
| ind2_repair and maintenance | -0.0 |
| ind2_social assistance | -0.0 |
| ind2_textile, apparel, and leather manufacturing | -0.0 |
| ind2_transportation equipment manufacturing | -0.0 |
| ind2_traveler accommodation | -0.0 |
| ind2_utilities | -0.0 |
| ind2_waste management and remediation services | 0.0 |
| ind2_wholesale trade | 0.0 |
| ind2_wood product manufacturing | 0.0 |
| kid3to5_yes | -0.0 |
| kid6to12_yes | 0.0 |
| kidund1_yes | 0.0 |
| marst_divorced | 0.0 |
| marst_married - spouse absent | -0.0 |
| marst_married - spouse present | -0.0 |
| marst_separated | -0.0 |
| marst_widowed | 0.0 |
| metro_metropolitan, balance of msa | -0.0 |
| metro_metropolitan, not identified | 0.0 |
| metro_not identified | -0.0 |
| month_august | 0.0 |
| month_december | -0.0 |
| month_january | 0.0 |
| month_june | -0.0 |
| month_march | 0.0 |
| month_may | -0.0 |
| month_november | 0.0 |
| month_october | -0.0 |
| msasize_1,000,000 - 2,499,999 | -0.0 |
| msasize_250,000 - 499,999 | -0.0 |
| msasize_500,000 - 999,999 | 0.0 |
| msasize_not identified or non-metropolitan | -0.0 |
| multjobs_yes | -0.0 |
| occ2_architecture and engineering occupations | -0.0 |
| occ2_building and grounds cleaning and maintenance occupations | -0.0 |
| occ2_community and social service occupations | 0.0 |
| occ2_construction and extraction occupations | -0.0 |
| occ2_farming, fishing, and forestry occupations | -0.0 |
| occ2_food preparation and serving related occupations | -0.0 |
| occ2_healthcare support occupations | -0.0 |
| occ2_legal occupations | 0.0 |
| occ2_life, physical, and social science occupations | -0.0 |
| occ2_personal care and service occupations | -0.0 |
| occ2_protective service occupations | 0.0 |
| race_american indian, alaskan native | -0.0 |
| race_asian only | -0.0 |
| race_black only | -0.0 |
| race_hawaiian pacific islander only | 0.0 |
| race_white-american indian | -0.0 |
| race_white-asian | 0.0 |
| race_white-black | -0.0 |
| rcvpdlv_don't know | -0.0 |
| rcvpdlv_no | -0.0 |
| rcvunpdlv_don't know | 0.0 |
| region_midwest | -0.0 |
| region_northeast | 0.0 |
| region_west | -0.0 |
| schlcoll_college/university full time | -0.0 |
| schlcoll_college/university part time | 0.0 |
| schlcoll_high school full time | -0.0 |
| schlcoll_niu (not in universe) | -0.0 |
| speduc_10th grade | 0.0 |
| speduc_11th grade | 0.0 |
| speduc_12th grade - no diploma | -0.0 |
| speduc_1st, 2nd, 3rd, or 4th grade | -0.0 |
| speduc_5th or 6th grade | -0.0 |
| speduc_7th or 8th grade | -0.0 |
| speduc_9th grade | -0.0 |
| speduc_associate degree - academic program | 0.0 |
| speduc_associate degree - occupational vocational | -0.0 |
| speduc_doctoral degree (phd, edd, etc.) | 0.0 |
| speduc_high school graduate - diploma | -0.0 |
| speduc_high school graduate - ged | -0.0 |
| speduc_niu (not in universe) | -0.0 |
| speduc_not available (see description) | -0.0 |
| speduc_professional school degree (md, dds, dvm, etc.) | 0.0 |
| speduc_some college but no degree | -0.0 |
| spempnot_niu (not in universe) | -0.0 |
| spempnot_not employed | -0.0 |
| spempstat_disabled | -0.0 |
| spempstat_employed - not at work | 0.0 |
| spempstat_niu (not in universe) | -0.0 |
| spempstat_not employed | -0.0 |
| spempstat_retired | 0.0 |
| spousepres_no spouse or unmarried partner present | -0.0 |
| spousepres_spouse present | 0.0 |
| spousepres_unmarried partner present | -0.0 |
| sprace_american indian, alaskan native | -0.0 |
| sprace_asian only | -0.0 |
| sprace_black only | 0.0 |
| sprace_hawaiian pacific islander only | 0.0 |
| sprace_niu (not in universe) | -0.0 |
| sprace_not available (see description) | -0.0 |
| sprace_white-american indian | -0.0 |
| sprace_white-asian | 0.0 |
| sprace_white-black | -0.0 |
| spsex_female | -0.0 |
| spsex_male | 0.0 |
| spsex_niu (not in universe) | -0.0 |
| spusualhrs_10 | -0.0 |
| spusualhrs_12 | 0.0 |
| spusualhrs_15 | 0.0 |
| spusualhrs_16 | 0.0 |
| spusualhrs_20 | 0.0 |
| spusualhrs_24 | 0.0 |
| spusualhrs_25 | -0.0 |
| spusualhrs_28 | 0.0 |
| spusualhrs_32 | -0.0 |
| spusualhrs_35 | 0.0 |
| spusualhrs_36 | 0.0 |
| spusualhrs_37 | -0.0 |
| spusualhrs_38 | -0.0 |
| spusualhrs_4 | 0.0 |
| spusualhrs_42 | 0.0 |
| spusualhrs_44 | -0.0 |
| spusualhrs_45 | 0.0 |
| spusualhrs_46 | -0.0 |
| spusualhrs_48 | -0.0 |
| spusualhrs_50 | 0.0 |
| spusualhrs_55 | 0.0 |
| spusualhrs_65 | 0.0 |
| spusualhrs_70 | -0.0 |
| spusualhrs_8 | -0.0 |
| spusualhrs_99 | -0.0 |
| spusualhrs_hours vary | -0.0 |
| statefip_alaska | -0.0 |
| statefip_arizona | 0.0 |
| statefip_arkansas | -0.0 |
| statefip_colorado | 0.0 |
| statefip_connecticut | -0.0 |
| statefip_delaware | -0.0 |
| statefip_district of columbia | 0.0 |
| statefip_georgia | 0.0 |
| statefip_hawaii | -0.0 |
| statefip_illinois | 0.0 |
| statefip_indiana | -0.0 |
| statefip_iowa | -0.0 |
| statefip_kansas | -0.0 |
| statefip_kentucky | -0.0 |
| statefip_louisiana | 0.0 |
| statefip_maine | 0.0 |
| statefip_michigan | 0.0 |
| statefip_minnesota | -0.0 |
| statefip_mississippi | -0.0 |
| statefip_missouri | 0.0 |
| statefip_montana | -0.0 |
| statefip_nebraska | -0.0 |
| statefip_nevada | 0.0 |
| statefip_new hampshire | -0.0 |
| statefip_new jersey | 0.0 |
| statefip_new mexico | -0.0 |
| statefip_north dakota | -0.0 |
| statefip_ohio | -0.0 |
| statefip_oklahoma | 0.0 |
| statefip_oregon | 0.0 |
| statefip_rhode island | -0.0 |
| statefip_south carolina | -0.0 |
| statefip_south dakota | -0.0 |
| statefip_tennessee | 0.0 |
| statefip_texas | -0.0 |
| statefip_utah | -0.0 |
| statefip_vermont | 0.0 |
| statefip_virginia | -0.0 |
| statefip_west virginia | 0.0 |
| statefip_wisconsin | 0.0 |
| statefip_wyoming | -0.0 |
| tklvwk_blank | 0.0 |
| tklvwk_yes | 0.0 |
| tklvwktype_blank | -0.0 |
| tklvwktype_paid for all | 0.0 |
| tklvwktype_paid for some | -0.0 |
| tklvwktype_unpaid for all | -0.0 |
| vetstat_niu (not in universe) | -0.0 |
| vetstat_veteran | -0.0 |
| wrkflexfreq_blank | -0.0 |
| wrkflexinput_other | -0.0 |
| wrkflexinput_worker has some input | 0.0 |
| wrkflexpol_informal arrangement | 0.0 |
| wrknumus_1 day | 0.0 |
| wrknumus_2 days | 0.0 |
| wrknumus_3 days | 0.0 |
| wrknumus_6 days | 0.0 |
| wrkschedmon_yes | -0.0 |
| wrkschedtue_yes | 0.0 |
| wrkschedus_daytime- most work done b/w 6a & 6p | -0.0 |
| wrkschedus_evening shift- most work done b/w 2p & 12a | 0.0 |
| wrkschedus_night shift- most work done b/w 9p & 8a | -0.0 |
| wrkschedus_rotating shift- hours change periodically | -0.0 |
| wrkschedus_some other shift | -0.0 |
| wrkschedus_split shift- two distinct periods each day | 0.0 |
| wrkschedvary_yes | -0.0 |
| wrkshiftrsn_allows time for school | 0.0 |
| wrkshiftrsn_better arrangements for family or childcare | 0.0 |
| wrkshiftrsn_better pay | -0.0 |
| wrkshiftrsn_blank | -0.0 |
| wrkshiftrsn_could not get any other shift | 0.0 |
| wrkshiftrsn_nature of the job | -0.0 |
| wrkshiftrsn_other | 0.0 |
| wrkshiftrsn_personal preference | 0.0 |
| wrkflexinput_blank | 0.0 |
| clwkr_private, nonprofit | 0.0 |
| wrkflexfreq_occasionally | 0.0 |
| famincome_$50,000 to $59,999 | 0.0 |
| rcvunpdlv_yes | 0.0 |
| metro_metropolitan, central city | 0.0 |
| month_february | 0.0 |
| spempstat_employed - at work | 0.001 |
| kid1to2_yes | 0.002 |
| ind2_publishing industries (except internet) | 0.002 |
| hrslvwk | 0.002 |
| spempnot_employed | 0.002 |
| day_wednesday | 0.003 |
| month_april | 0.003 |
| wrkschedthu_yes | 0.003 |
| kid13to17_yes | 0.004 |
| statefip_washington | 0.004 |
| speduc_bachelor's degree (ba, ab, bs, etc.) | 0.004 |
| day_friday | 0.004 |
| famincome_$35,000 to $39,999 | 0.005 |
| occ2_office and administrative support occupations | 0.005 |
| statefip_north carolina | 0.007 |
| hh_numownkids | 0.007 |
| wrkschedsun_yes | 0.007 |
| race_white only | 0.007 |
| spearnweek | 0.008 |
| clwkr_private, for profit | 0.008 |
| wrkdaysavg | 0.009 |
| region_south | 0.009 |
| hourwage | 0.01 |
| famincome_$100,000 to $149,999 | 0.012 |
| rcvpdlv_yes | 0.014 |
| vetstat_non-veteran | 0.014 |
| educyrs_college--four years | 0.015 |
| schlcoll_not enrolled | 0.015 |
| wrkschedwed_yes | 0.015 |
| statefip_new york | 0.015 |
| sprace_white only | 0.017 |
| spusualhrs_30 | 0.017 |
| msasize_5,000,000+ | 0.019 |
| citizen_native, born in united states | 0.019 |
| ind2_membership associations and organizations | 0.019 |
| wrkschedwk_yes | 0.019 |
| educyrs_bachelor's degree | 0.021 |
| speduc_master's degree (ma, ms, meng, med, msw, etc.) | 0.024 |
| ind2_miscellaneous and not specified mfg | 0.024 |
| wrkflexpol_formal program or policy | 0.025 |
| wrkschedus_irregular schedule | 0.027 |
| educyrs_master's degree | 0.028 |
| ind2_telecommunications | 0.031 |
| spusualhrs_60 | 0.035 |
| statefip_massachusetts | 0.035 |
| ind2_chemical manufacturing | 0.036 |
| educyrs_professional degree | 0.037 |
| msasize_2,500,000 - 4,999,999 | 0.039 |
| ind2_real estate | 0.04 |
| statefip_maryland | 0.043 |
| fambus_family business | 0.044 |
| occ2_sales and related occupations | 0.046 |
| educyrs_doctoral degree | 0.047 |
| earnweek | 0.049 |
| occ2_management occupations | 0.05 |
| famincome_$150,000 and over | 0.05 |
| wrknumus_7 days | 0.056 |
| occ2_education, training, and library occupations | 0.061 |
| occ2_arts, design, entertainment, sports, and media occupations | 0.063 |
| wrkflexhrs_yes | 0.087 |
| ind2_professional, scientific, and technical services | 0.092 |
| wrkflexfreq_frequent basis | 0.117 |
| occ2_business and financial operations occupations | 0.12 |
| ind2_insurance | 0.151 |
| occ2_computer and mathematical science occupations | 0.205 |

</details>


























