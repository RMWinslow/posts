---
title: Commuting Correlations
subtitle: Correlates with commuting time in the ATUS and PSID
layout: post
parent: Econ
date: 2023-04-10
last_modified_date: 2023-03-14
search_exclude: True
toc: True
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
| bls_work |  | 0.364 |
| bls_work_working |  | 0.222 |
| bls_carehh_travel |  | 0.079 |
| bls_work_workrel |  | 0.049 |
| bls_pcare_groom |  | 0.043 |
| bls_pcare_travel |  | 0.027 |
| bls_purch_travel |  | 0.02 |
| bls_carehh_kideduc |  | 0.013 |
| bls_hhact_travel |  | 0.012 |
| bls_comm_travel |  | 0.009 |
| bls_work_other |  | 0.004 |
| dwell15_telephone |  | 0.002 |
| bls_social_civic |  | 0.001 |
|  | ... |  |
| hourwage |  | -0.022 |
|  | ... |  |
| earnweek |  | -0.085 |
|  | ... |  |
| bls_leis_sport |  | -0.092 |
| bls_leis_tv |  | -0.093 |
| bls_leis_soccom |  | -0.1 |
| dwell15_purchcons |  | -0.102 |
| bls_purch_groc |  | -0.105 |
| bls_hhact_hwork |  | -0.121 |
| bls_leis_relax |  | -0.127 |
| bls_purch_cons |  | -0.138 |
| bls_pcare |  | -0.146 |
| bls_hhact |  | -0.152 |
| bls_pcare_sleep |  | -0.161 |
| bls_leis_soc |  | -0.175 |
| bls_leis |  | -0.197 |
-->

### Dwell 30 Travel Time


An alternate way to code travel time is described in [this article](https://www.bls.gov/opub/mlr/2018/article/what-is-the-impact-of-recoding-travel-activities-in-the-american-time-use-survey.htm).

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| dwell30_work |  | 1.0 |
| bls_work |  | 0.29 |
| bls_work_working |  | 0.135 |
| bls_carehh_travel |  | 0.11 |
| bls_purch_travel |  | 0.105 |
| msasize_5,000,000+ |  | 0.096 |
| fambus_no family business |  | 0.085 |
| fambus_resp_no |  | 0.084 |
| ind2_construction |  | 0.08 |
| occ2_construction and extraction occupations |  | 0.079 |
| fullpart_full time |  | 0.075 |
| clwkr_private, for profit |  | 0.071 |
| spsex_female |  | 0.069 |
| metro_metropolitan, balance of msa |  | 0.068 |
| kidund18_yes |  | 0.062 |
| kidund13_yes |  | 0.056 |
| statefip_new york |  | 0.055 |
| day_tuesday |  | 0.053 |
| empstat_employed - at work |  | 0.051 |
| sex_male |  | 0.05 |
| region_northeast |  | 0.049 |
|  | ... |  |
| hourwage |  | -0.01 |
|  | ... |  |
| uhrsworkt |  | -0.026 |
|  | ... |  |
| earnweek |  | -0.085 |
| dwell30_social |  | -0.086 |
| dwell30_purchcons |  | -0.087 |
| bls_leis_soccom |  | -0.09 |
| bls_leis_sport |  | -0.09 |
| scc_all |  | -0.092 |
| bls_leis_relax |  | -0.095 |
| bls_hhact_hwork |  | -0.096 |
| day_saturday |  | -0.099 |
| bls_purch_cons |  | -0.101 |
| bls_hhact |  | -0.104 |
| day_sunday |  | -0.133 |
| bls_pcare |  | -0.134 |
| bls_leis_soc |  | -0.141 |
| bls_pcare_sleep |  | -0.151 |
| bls_leis |  | -0.162 |



A few things I notice change with this recoding:
- Variables related to taking kids to school (*`kidund18_yes`*, *`bls_carehh_travel`*) are now correlated with this measure of commute time. This makes sense. If you go out of your way to drop your kids off mid-commute, then the standard rule cuts your commute time in half, while this rules extends it.
- Likewise, the strength of the *`sex_male`* correlation is weakened.

### Dwell 30 Anchor method.

Using the anchor method, only travel chains which take place between home and work (or vice versa) are counted as commuting.

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| bls_work |  | 0.232 |
| bls_carehh_travel |  | 0.137 |
| bls_work_working |  | 0.133 |
| fambus_resp_no |  | 0.104 |
| fambus_no family business |  | 0.103 |
| kidund18_yes |  | 0.088 |
| kidund13_yes |  | 0.083 |
| occ2_construction and extraction occupations |  | 0.077 |
| bls_carehh |  | 0.074 |
| | ... | |
| hourwage |  | -0.035 |
| | ... | |
| earnweek |  | -0.1 |
| | ... | |
| bls_purch_cons |  | -0.103 |
| fambus_family business |  | -0.104 |
| fambus_resp_yes |  | -0.104 |
| day_saturday |  | -0.114 |
| bls_leis |  | -0.121 |
| day_sunday |  | -0.131 |
| bls_pcare |  | -0.132 |
| bls_pcare_sleep |  | -0.135 |

<details mardown="block"><summary>Click for full list of correlations.</summary>

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| dwell30_anchorCommute |  | 1.0 |
| dwell15_anchorCommute |  | 0.871 |
| dwell30_work |  | 0.746 |
| dwell15_work |  | 0.649 |
| bls_work_travel |  | 0.5 |
| bls_work |  | 0.232 |
| bls_carehh_travel |  | 0.137 |
| bls_work_working |  | 0.133 |
| fambus_resp_no |  | 0.104 |
| fambus_no family business |  | 0.103 |
| kidund18_yes |  | 0.088 |
| kidund13_yes |  | 0.083 |
| occ2_construction and extraction occupations |  | 0.077 |
| bls_carehh |  | 0.074 |
| clwkr_private, for profit |  | 0.072 |
| ind2_construction |  | 0.071 |
| hh_child_yes |  | 0.069 |
| bls_purch_travel |  | 0.066 |
| msasize_5,000,000+ |  | 0.065 |
| otusual_no |  | 0.065 |
| fullpart_full time |  | 0.063 |
| spsex_female |  | 0.061 |
| spousepres_spouse present |  | 0.06 |
| day_tuesday |  | 0.058 |
| metro_metropolitan, balance of msa |  | 0.058 |
| marst_married - spouse present |  | 0.057 |
| kid6to12_yes |  | 0.054 |
| day_wednesday |  | 0.052 |
| day_monday |  | 0.051 |
| wt06 |  | 0.05 |
| empstat_employed - at work |  | 0.05 |
| kid3to5_yes |  | 0.05 |
| multjobs_no |  | 0.049 |
| fambus_pay_niu (not in universe) |  | 0.046 |
| bls_carehh_kid |  | 0.046 |
| day_thursday |  | 0.045 |
| msasize_2,500,000 - 4,999,999 |  | 0.045 |
| fambus_spouse_no |  | 0.045 |
| statefip_new york |  | 0.045 |
| region_northeast |  | 0.044 |
| citizen_foreign born, not a u.s. citizen |  | 0.044 |
| kid1to2_yes |  | 0.044 |
| schlcoll_not enrolled |  | 0.044 |
| bls_carehh_kidother |  | 0.041 |
| clwkr_government, federal |  | 0.04 |
| hh_numkids_2 |  | 0.039 |
| bls_carehh_kideduc |  | 0.039 |
| sprace_white only |  | 0.037 |
| spempnot_employed |  | 0.036 |
| spempstat_employed - at work |  | 0.036 |
| hh_numadults_2 |  | 0.036 |
| paidhour_paid hourly |  | 0.035 |
| sprace_asian only |  | 0.033 |
| spempstat_not employed |  | 0.033 |
| citizen_foreign born, u.s. citizen by naturalization |  | 0.033 |
| ind2_public administration |  | 0.033 |
| spempnot_not employed |  | 0.033 |
| paidhour_not paid hourly |  | 0.033 |
| kid13to17_yes |  | 0.031 |
| bpl_el salvador |  | 0.031 |
| race_asian only |  | 0.03 |
| hh_size_4 |  | 0.03 |
| occ2_architecture and engineering occupations |  | 0.03 |
| statefip_maryland |  | 0.029 |
| occ2_office and administrative support occupations |  | 0.029 |
| ageychild_2 |  | 0.029 |
| ageychild_1 |  | 0.029 |
| sex_male |  | 0.028 |
| educ_5th or 6th grade |  | 0.028 |
| educyrs_fifth through sixth grade |  | 0.028 |
| hh_numkids_1 |  | 0.028 |
| statefip_new jersey |  | 0.027 |
| wt20 |  | 0.026 |
| ageychild_3 |  | 0.026 |
| bls_hhact_travel |  | 0.026 |
| bpl_mexico |  | 0.026 |
| day_friday |  | 0.025 |
| hh_numkids_3 |  | 0.025 |
| wrknumus_5 days |  | 0.024 |
| hh_size_3 |  | 0.024 |
| holiday_no |  | 0.024 |
| dwell15_hhact |  | 0.023 |
| bls_hhact_food |  | 0.023 |
| ageychild_4 |  | 0.023 |
| occ2_business and financial operations occupations |  | 0.022 |
| occ2_installation, maintenance, and repair occupations |  | 0.022 |
| hh_size_5 |  | 0.022 |
| looking_niu (not in universe) |  | 0.022 |
| speduc_high school graduate - diploma |  | 0.022 |
| ind2_finance |  | 0.021 |
| sprace_black only |  | 0.021 |
| occ2_building and grounds cleaning and maintenance occupations |  | 0.021 |
| ind2_mining |  | 0.019 |
| retired_niu (not in universe) |  | 0.019 |
| kidund1_yes |  | 0.019 |
| bls_pcare_travel |  | 0.019 |
| ind2_transportation equipment manufacturing |  | 0.019 |
| occ2_computer and mathematical science occupations |  | 0.018 |
| wrkhomeoften_blank |  | 0.018 |
| ageychild_0 |  | 0.018 |
| occ2_life, physical, and social science occupations |  | 0.018 |
| educyrs_first through fourth grade |  | 0.018 |
| educ_1st, 2nd, 3rd, or 4th grade |  | 0.018 |
| ind2_insurance |  | 0.018 |
| famincome_$75,000 to $99,999 |  | 0.018 |
| speduc_associate degree - academic program |  | 0.017 |
| ageychild_5 |  | 0.017 |
| ind2_computer and electronic product mfg |  | 0.016 |
| bpl_ecuador |  | 0.015 |
| statefip_california |  | 0.015 |
| bpl_china |  | 0.015 |
| speduc_5th or 6th grade |  | 0.015 |
| bpl_honduras |  | 0.015 |
| ind2_administrative and support services |  | 0.015 |
| wrkhomedays_blank |  | 0.015 |
| wrkhomepd_blank |  | 0.015 |
| bpl_trinidad and tobago |  | 0.015 |
| famincome_$100,000 to $149,999 |  | 0.014 |
| ageychild_6 |  | 0.014 |
| speduc_bachelor's degree (ba, ab, bs, etc.) |  | 0.014 |
| vetstat_veteran |  | 0.014 |
| bpl_armenia |  | 0.014 |
| month_february |  | 0.014 |
| wrkflexhrs_no |  | 0.014 |
| wrkhomeev_blank |  | 0.013 |
| ageychild_10 |  | 0.013 |
| wrkhomeable_no |  | 0.013 |
| speduc_some college but no degree |  | 0.013 |
| ind2_rental and leasing services |  | 0.013 |
| speduc_1st, 2nd, 3rd, or 4th grade |  | 0.013 |
| speduc_master's degree (ma, ms, meng, med, msw, etc.) |  | 0.012 |
| educ_associate degree - academic program |  | 0.012 |
| statefip_massachusetts |  | 0.012 |
| educ_less than 1st grade |  | 0.012 |
| bpl_dominican republic |  | 0.012 |
| bpl_colombia |  | 0.012 |
| bpl_west indies |  | 0.012 |
| bpl_india |  | 0.012 |
| wrkhomedays_no |  | 0.012 |
| otusual_yes |  | 0.012 |
| bpl_europe, n.s |  | 0.012 |
| educyrs_less than first grade |  | 0.012 |
| ind2_telecommunications |  | 0.011 |
| bpl_guatemala |  | 0.011 |
| bpl_grenada |  | 0.011 |
| hh_numkids_4 |  | 0.011 |
| ageychild_8 |  | 0.011 |
| housetype_mobile home or trailer with 1 or more rooms added |  | 0.011 |
| bls_comm_travel |  | 0.011 |
| speduc_12th grade - no diploma |  | 0.011 |
| ageychild_9 |  | 0.011 |
| speduc_less than 1st grade |  | 0.011 |
| ind2_chemical manufacturing |  | 0.011 |
| bpl_ukraine |  | 0.01 |
| bpl_haiti |  | 0.01 |
| bpl_north america, n.s |  | 0.01 |
| hh_size_6 |  | 0.01 |
| bpl_korea |  | 0.01 |
| statefip_illinois |  | 0.01 |
| ind2_hospitals |  | 0.01 |
| wrkhomeoften_less than once a month |  | 0.01 |
| bpl_nepal |  | 0.009 |
| ind2_private households |  | 0.009 |
| bpl_ireland |  | 0.009 |
| speduc_doctoral degree (phd, edd, etc.) |  | 0.009 |
| occ2_production occupations |  | 0.009 |
| bpl_cambodia |  | 0.009 |
| educ_high school graduate - ged |  | 0.009 |
| bpl_barbados |  | 0.009 |
| bpl_hong kong |  | 0.009 |
| bpl_indonesia |  | 0.009 |
| bpl_central america, n.s |  | 0.008 |
| ageychild_13 |  | 0.008 |
| bpl_nicaragua |  | 0.008 |
| bpl_cuba |  | 0.008 |
| bpl_cyprus |  | 0.008 |
| speduc_9th grade |  | 0.008 |
| bpl_burma (myanmar) |  | 0.008 |
| ageychild_7 |  | 0.008 |
| bpl_malaysia |  | 0.008 |
| race_black only |  | 0.008 |
| wrkhomepd_both |  | 0.008 |
| bpl_belarus |  | 0.008 |
| bpl_taiwan |  | 0.008 |
| citizen_native, born in puerto rico or u.s. outlying area |  | 0.008 |
| ind2_waste management and remediation services |  | 0.008 |
| bpl_puerto rico |  | 0.008 |
| educ_high school graduate - diploma |  | 0.008 |
| educyrs_college--two years |  | 0.007 |
| spempstat_disabled |  | 0.007 |
| bpl_philippines |  | 0.007 |
| bpl_brazil |  | 0.007 |
| statefip_district of columbia |  | 0.007 |
| ind2_management of companies and enterprises |  | 0.007 |
| speduc_not available (see description) |  | 0.007 |
| bpl_ghana |  | 0.007 |
| statefip_georgia |  | 0.007 |
| ind2_nonmetallic mineral product manufacturing |  | 0.007 |
| outcome_complete interview |  | 0.007 |
| occ2_legal occupations |  | 0.007 |
| ind2_beverage and tobacco product mfg |  | 0.007 |
| famincome_$150,000 and over |  | 0.007 |
| sprace_white-asian-hawaiian |  | 0.007 |
| statefip_pennsylvania |  | 0.006 |
| wrkhomeoften_at least once a week |  | 0.006 |
| statefip_new hampshire |  | 0.006 |
| bpl_vietnam |  | 0.006 |
| diffany_no difficulty |  | 0.006 |
| bpl_nigeria |  | 0.006 |
| hh_numadults_7 |  | 0.006 |
| wrkhomeev_no |  | 0.006 |
| fambus_refused |  | 0.006 |
| statefip_florida |  | 0.006 |
| educyrs_twelfth grade |  | 0.006 |
| statefip_hawaii |  | 0.006 |
| sprace_not available (see description) |  | 0.006 |
| speduc_10th grade |  | 0.006 |
| bpl_australia |  | 0.006 |
| bpl_bolivia |  | 0.006 |
| ind2_utilities |  | 0.006 |
| statefip_washington |  | 0.006 |
| sprace_american indian, alaskan native |  | 0.006 |
| fambus_don't know |  | 0.006 |
| wrkhomeable_blank |  | 0.006 |
| bpl_asia, n.e.c. or n.s |  | 0.006 |
| speduc_11th grade |  | 0.006 |
| statefip_virginia |  | 0.006 |
| bpl_netherlands |  | 0.005 |
| bpl_jamaica |  | 0.005 |
| ind2_wholesale trade |  | 0.005 |
| ind2_electrical equipment, appliance mfg |  | 0.005 |
| ind2_paper manufacturing and printing |  | 0.005 |
| ind2_machinery manufacturing |  | 0.005 |
| bpl_panama |  | 0.005 |
| month_january |  | 0.005 |
| bpl_portugal |  | 0.005 |
| wrkhomeoften_once a month |  | 0.005 |
| month_march |  | 0.005 |
| educyrs_college--four years |  | 0.005 |
| educyrs_master's degree |  | 0.005 |
| bpl_liberia |  | 0.005 |
| metro_metropolitan, central city |  | 0.004 |
| bpl_africa, n.s |  | 0.004 |
| sprace_black-american indian |  | 0.004 |
| famincome_$30,000 to $34,999 |  | 0.004 |
| looking_refused |  | 0.004 |
| ind2_petroleum and coal products manufacturing |  | 0.004 |
| speduc_high school graduate - ged |  | 0.004 |
| famincome_don't know |  | 0.004 |
| hh_size_12 |  | 0.004 |
| bpl_libya |  | 0.004 |
| bpl_latvia |  | 0.004 |
| sprace_white-asian |  | 0.004 |
| housetype_housing unit in nontransient hotel, motel, etc |  | 0.004 |
| ageychild_11 |  | 0.004 |
| clwkr_government, state |  | 0.004 |
| bpl_guyana/british guiana |  | 0.004 |
| educ_associate degree - occupational vocational |  | 0.004 |
| bpl_italy |  | 0.004 |
| speduc_professional school degree (md, dds, dvm, etc.) |  | 0.004 |
| bpl_norway |  | 0.004 |
| bpl_japan |  | 0.004 |
| race_4 or 5 races, unspecified |  | 0.004 |
| diffmob_no mobility limitation |  | 0.004 |
| ind2_miscellaneous and not specified mfg |  | 0.004 |
| spempstat_employed - not at work |  | 0.004 |
| sprace_black-asian |  | 0.004 |
| educ_master's degree (ma, ms, meng, med, msw, etc.) |  | 0.004 |
| bpl_congo |  | 0.004 |
| dataqual_blank |  | 0.004 |
| wrkflexhrs_yes |  | 0.003 |
| bpl_south korea |  | 0.003 |
| bpl_zimbabwe |  | 0.003 |
| hh_numadults_6 |  | 0.003 |
| housetype_mobile home or trailer with no permanent room added |  | 0.003 |
| hhtenure_owned or being bought by a household member |  | 0.003 |
| race_white-asian |  | 0.003 |
| bpl_bosnia and herzegovina |  | 0.003 |
| dwell15_carehh |  | 0.003 |
| bpl_south america, n.s |  | 0.003 |
| bpl_antigua and barbuda |  | 0.003 |
| bpl_dominica |  | 0.003 |
| age |  | 0.003 |
| ind2_traveler accommodation |  | 0.003 |
| sprace_white-black-american indian |  | 0.003 |
| bpl_romania |  | 0.003 |
| hh_numadults_8 |  | 0.003 |
| sprace_white-black |  | 0.003 |
| year |  | 0.003 |
| educ_12th grade - no diploma |  | 0.003 |
| dataqual_other |  | 0.003 |
| caseid |  | 0.003 |
| citizen_native, born abroad of american parent or parents |  | 0.003 |
| hh_size_13 |  | 0.003 |
| bpl_guam |  | 0.003 |
| ind2_wood product manufacturing |  | 0.003 |
| bpl_greece |  | 0.002 |
| bls_comm_msgmail |  | 0.002 |
| speduc_associate degree - occupational vocational |  | 0.002 |
| hh_numkids_7 |  | 0.002 |
| month_september |  | 0.002 |
| bpl_france |  | 0.002 |
| race_black-american indian |  | 0.002 |
| ind2_broadcasting (except internet) |  | 0.002 |
| race_white-hawaiian |  | 0.002 |
| statefip_delaware |  | 0.002 |
| bpl_sierra leone |  | 0.002 |
| bpl_switzerland |  | 0.002 |
| bpl_iran |  | 0.002 |
| bpl_costa rica |  | 0.002 |
| index |  | 0.002 |
| Unnamed__0_y |  | 0.002 |
| Unnamed__0_x |  | 0.002 |
| race_american indian-asian |  | 0.002 |
| bpl_bermuda |  | 0.002 |
| bpl_ivory coast |  | 0.002 |
| bpl_pacific islands |  | 0.002 |
| bpl_albania |  | 0.002 |
| fambus_niu (not in universe) |  | 0.002 |
| bpl_croatia |  | 0.002 |
| bpl_u.s. virgin islands |  | 0.002 |
| bpl_slovakia |  | 0.002 |
| bpl_laos |  | 0.002 |
| hhtenure_rented for cash |  | 0.002 |
| bpl_somalia |  | 0.002 |
| bpl_south africa (union of) |  | 0.002 |
| ind2_primary metals and fabricated metal products |  | 0.002 |
| educyrs_ninth grade |  | 0.002 |
| bpl_england |  | 0.002 |
| bpl_northern ireland |  | 0.002 |
| bpl_kosovo |  | 0.002 |
| bpl_belize/british honduras |  | 0.002 |
| wrkhomeoften_once every 2 weeks |  | 0.002 |
| bls_pcare_groom |  | 0.002 |
| bpl_st. lucia |  | 0.002 |
| housetype_housing unit in rooming house |  | 0.002 |
| hh_size_7 |  | 0.002 |
| bpl_bulgaria |  | 0.002 |
| bpl_st. kitts--nevis |  | 0.002 |
| marst_married - spouse absent |  | 0.002 |
| bpl_other ussr/russia |  | 0.001 |
| bpl_peru |  | 0.001 |
| spsex_male |  | 0.001 |
| bpl_zambia |  | 0.001 |
| bpl_kuwait |  | 0.001 |
| statefip_tennessee |  | 0.001 |
| dataqual_no data quality problems identified |  | 0.001 |
| bpl_uruguay |  | 0.001 |
| wrkhomeable_yes |  | 0.001 |
| ind2_repair and maintenance |  | 0.001 |
| month_december |  | 0.001 |
| ind2_plastics and rubber products manufacturing |  | 0.001 |
| bpl_sri lanka |  | 0.001 |
| race_white-black-asian |  | 0.001 |
| ind2_textile, apparel, and leather manufacturing |  | 0.001 |
| bpl_bangladesh |  | 0.001 |
| ageychild_12 |  | 0.001 |
| ind2_food manufacturing |  | 0.001 |
| bpl_georgia |  | 0.001 |
| sprace_white-hawaiian |  | 0.001 |
| bpl_senegal |  | 0.001 |
| bpl_argentina |  | 0.001 |
| educyrs_master's degree--three+ year program |  | 0.001 |
| speduc_7th or 8th grade |  | 0.001 |
| bpl_poland |  | 0.001 |
| sprace_american indian-asian |  | 0.001 |
| bpl_paraguay |  | 0.001 |
| race_2 or 3 races, unspecified |  | 0.001 |
| bpl_sweden |  | 0.001 |
| bpl_moldova |  | 0.0 |
| bpl_st. vincent and the grenadi |  | 0.0 |
| bpl_ussr, n.s |  | 0.0 |
| bpl_uganda |  | 0.0 |
| famincome_$12,500 to $14,999 |  | 0.0 |
| ind2_professional, scientific, and technical services |  | 0.0 |
| statefip_west virginia |  | 0.0 |
| hh_numadults_4 |  | 0.0 |
| bpl_tanzania |  | 0.0 |
| bpl_yugoslavia |  | 0.0 |
| bpl_ethiopia |  | 0.0 |
| bpl_serbia |  | 0.0 |
| bpl_u.s. outlying areas, n.s |  | 0.0 |
| bpl_algeria |  | 0.0 |
| famincome_$50,000 to $59,999 |  | 0.0 |
| vetstat_refused |  | 0.0 |
| race_white-asian-hawaiian |  | 0.0 |
| bpl_other, n.e.c. and unknown |  | 0.0 |
| region_west |  | 0.0 |
| bls_carenhh_travel |  | -0.0 |
| famincome_blank |  | -0.0 |
| month_october |  | -0.0 |
| bpl_new zealand |  | -0.0 |
| race_black-asian |  | -0.0 |
| spempstat_don't know |  | -0.0 |
| hh_numkids_10 |  | -0.0 |
| bpl_azerbaijan |  | -0.0 |
| sprace_asian-hawaiian |  | -0.0 |
| wrkhomepd_paid |  | -0.0 |
| race_white-black-hawaiian |  | -0.0 |
| sprace_white-american indian |  | -0.0 |
| month_april |  | -0.0 |
| bpl_chile |  | -0.0 |
| bpl_saudi arabia |  | -0.0 |
| month_may |  | -0.0 |
| bpl_bhutan |  | -0.0 |
| statefip_colorado |  | -0.0 |
| bpl_lebanon |  | -0.0 |
| famincome_$7,500 to $9,999 |  | -0.0 |
| spempstat_retired |  | -0.001 |
| bpl_united kingdom, n.s |  | -0.001 |
| hh_numadults_5 |  | -0.001 |
| educ_bachelor's degree (ba, ab, bs, etc.) |  | -0.001 |
| bpl_singapore |  | -0.001 |
| ind2_other information services |  | -0.001 |
| housetype_quarters not housing unit in rooming boarding house |  | -0.001 |
| bpl_thailand |  | -0.001 |
| housetype_other unit not specified above |  | -0.001 |
| bpl_yemen |  | -0.001 |
| spousepres_unmarried partner present |  | -0.001 |
| housetype_housing unit not specified above |  | -0.001 |
| hh_size_10 |  | -0.001 |
| bpl_fiji |  | -0.001 |
| race_asian-hawaiian |  | -0.001 |
| race_black-hawaiian |  | -0.001 |
| spempstat_blank |  | -0.001 |
| bpl_kenya |  | -0.001 |
| bpl_egypt/united arab rep |  | -0.001 |
| marst_separated |  | -0.001 |
| hh_size_8 |  | -0.001 |
| bpl_cape verde |  | -0.001 |
| bpl_hungary |  | -0.001 |
| housetype_housing unit permanent in transient hotel, motel |  | -0.001 |
| wrkhomeev_yes |  | -0.001 |
| housetype_unoccupied tent site or trailer site |  | -0.001 |
| educ_9th grade |  | -0.001 |
| bpl_tonga |  | -0.001 |
| hh_size_11 |  | -0.001 |
| vetstat_non-veteran |  | -0.001 |
| bpl_guinea |  | -0.001 |
| bpl_togo |  | -0.001 |
| sprace_white-black-asian |  | -0.001 |
| bpl_denmark |  | -0.001 |
| bpl_spain |  | -0.001 |
| month_august |  | -0.001 |
| bls_comm_msg |  | -0.002 |
| bpl_azores |  | -0.002 |
| retired_blank |  | -0.002 |
| educyrs_bachelor's degree |  | -0.002 |
| wrknumus_6 days |  | -0.002 |
| bpl_scotland |  | -0.002 |
| bpl_pakistan |  | -0.002 |
| ind2_forestry, logging, fishing, hunting, and trapping |  | -0.002 |
| race_white-black-american indian |  | -0.002 |
| bpl_bahamas |  | -0.002 |
| statefip_arizona |  | -0.002 |
| bpl_american samoa |  | -0.002 |
| vetstat_don't know |  | -0.002 |
| hh_numkids_11 |  | -0.002 |
| bpl_belgium |  | -0.002 |
| hh_size_9 |  | -0.002 |
| race_white-american indian |  | -0.002 |
| hh_numkids_8 |  | -0.002 |
| bpl_czechoslavakia |  | -0.002 |
| bpl_americas, n.s |  | -0.002 |
| occ2_healthcare practitioner and technical occupations |  | -0.002 |
| bpl_canada |  | -0.002 |
| spempstat_unable to work |  | -0.002 |
| bpl_syria |  | -0.002 |
| statefip_minnesota |  | -0.002 |
| bpl_morocco |  | -0.002 |
| hh_numkids_9 |  | -0.002 |
| ind2_internet svc providers and data processing svcs |  | -0.002 |
| spempstat_refused |  | -0.002 |
| hh_numadults_9 |  | -0.002 |
| bpl_palestine |  | -0.002 |
| wrkhomeoften_1 to 2 days a week |  | -0.002 |
| bpl_oceania, n.s |  | -0.002 |
| bpl_turkey |  | -0.002 |
| bpl_isreal/palestine |  | -0.002 |
| bpl_cameroon |  | -0.002 |
| statefip_maine |  | -0.003 |
| famincome_less than $5,000 |  | -0.003 |
| statefip_connecticut |  | -0.003 |
| hh_numadults_3 |  | -0.003 |
| race_hawaiian pacific islander only |  | -0.003 |
| bpl_czech republic |  | -0.003 |
| ind2_internet publishing and broadcasting |  | -0.003 |
| bpl_uzbekistan |  | -0.003 |
| bpl_germany |  | -0.003 |
| statefip_wyoming |  | -0.003 |
| hh_numadults_0 |  | -0.003 |
| looking_don't know |  | -0.003 |
| retired_no |  | -0.003 |
| bpl_middle east, n.s |  | -0.003 |
| looking_unable to work |  | -0.003 |
| bpl_mongolia |  | -0.003 |
| retired_was not retired last time |  | -0.003 |
| race_white-black-american indian-asian |  | -0.003 |
| bpl_zaire |  | -0.003 |
| bpl_venezuala |  | -0.003 |
| bpl_northern africa |  | -0.003 |
| ind2_furniture and fixtures manufacturing |  | -0.003 |
| bpl_iraq |  | -0.003 |
| ageychild_15 |  | -0.003 |
| race_white-black |  | -0.003 |
| statefip_alabama |  | -0.003 |
| bpl_eritrea |  | -0.003 |
| statefip_nevada |  | -0.003 |
| bls_comm_msgemail |  | -0.003 |
| bpl_estonia |  | -0.003 |
| famincome_$35,000 to $39,999 |  | -0.003 |
| race_american indian, alaskan native |  | -0.004 |
| race_white-american indian-asian |  | -0.004 |
| diffmob_niu (not in universe) |  | -0.004 |
| diffany_niu (not in universe) |  | -0.004 |
| ind2_health care services, except hospitals |  | -0.004 |
| bpl_afghanistan |  | -0.004 |
| housetype_student quarters in college dorm |  | -0.004 |
| schlcoll_refused |  | -0.004 |
| bls_hhact_tool |  | -0.004 |
| dwell15_hhserve |  | -0.004 |
| bpl_finland |  | -0.004 |
| ageychild_14 |  | -0.004 |
| empstat_unemployed - on layoff |  | -0.004 |
| famincome_$60,000 to $74,999 |  | -0.004 |
| educyrs_seventh through eighth grade |  | -0.004 |
| bpl_united arab emirates |  | -0.004 |
| ind2_transportation and warehousing |  | -0.004 |
| month_november |  | -0.004 |
| hh_numkids_5 |  | -0.004 |
| statefip_michigan |  | -0.004 |
| bpl_sudan |  | -0.004 |
| educyrs_master's degree--two year program |  | -0.004 |
| ind2_motion picture and sound recording industries |  | -0.004 |
| bpl_caribbean, n.s |  | -0.004 |
| bpl_jordan |  | -0.005 |
| educyrs_master's degree--one year program |  | -0.005 |
| educ_7th or 8th grade |  | -0.005 |
| educyrs_college--one year |  | -0.005 |
| hhtenure_niu (not in universe) |  | -0.005 |
| statefip_vermont |  | -0.005 |
| bls_social_civic |  | -0.005 |
| sprace_hawaiian pacific islander only |  | -0.005 |
| bpl_kazakhstan |  | -0.005 |
| bpl_macedonia |  | -0.005 |
| ageychild_17 |  | -0.005 |
| statefip_rhode island |  | -0.005 |
| statefip_alaska |  | -0.005 |
| diffmob_has mobility limitation |  | -0.005 |
| bpl_lithuania |  | -0.006 |
| ind2_publishing industries (except internet) |  | -0.006 |
| statefip_missouri |  | -0.006 |
| bls_pcare_health |  | -0.006 |
| metro_not identified |  | -0.006 |
| region_south |  | -0.006 |
| famincome_refused |  | -0.006 |
| educyrs_college--three years |  | -0.006 |
| bpl_austria |  | -0.006 |
| famincome_$10,000 to $12,499 |  | -0.006 |
| bls_purch_home |  | -0.006 |
| dataqual_r providing wrong answer |  | -0.006 |
| bls_hhact_hhmgmt |  | -0.007 |
| msasize_1,000,000 - 2,499,999 |  | -0.007 |
| wrknumus_1 day |  | -0.007 |
| outcome_sufficient partial |  | -0.007 |
| month_july |  | -0.007 |
| dataqual_r not able to remember activities |  | -0.007 |
| hh_numkids_6 |  | -0.007 |
| housetype_house, apartment, flat |  | -0.007 |
| statefip_utah |  | -0.007 |
| dwell15_civic |  | -0.007 |
| statefip_texas |  | -0.007 |
| famincome_$40,000 to $49,999 |  | -0.007 |
| otpay |  | -0.007 |
| wrknumus_4 days |  | -0.008 |
| wrkhomepd_take home work |  | -0.008 |
| educ_professional school degree (md, dds, dvm, etc.) |  | -0.008 |
| educyrs_professional degree |  | -0.008 |
| occ2_healthcare support occupations |  | -0.008 |
| dwell30_telephone |  | -0.008 |
| dataqual_r reporting long duration activities |  | -0.008 |
| clwkr_without pay |  | -0.008 |
| statefip_mississippi |  | -0.008 |
| schlcoll_college/university part time |  | -0.008 |
| dwell15_telephone |  | -0.008 |
| statefip_oregon |  | -0.009 |
| bls_carehh_adult |  | -0.009 |
| statefip_louisiana |  | -0.009 |
| famincome_$25,000 to $29,999 |  | -0.009 |
| famincome_$5,000 to $7,499 |  | -0.009 |
| statefip_arkansas |  | -0.009 |
| statefip_montana |  | -0.009 |
| educyrs_eleventh grade |  | -0.01 |
| dwell30_civic |  | -0.01 |
| wrknumus_3 days |  | -0.01 |
| occ2_farming, fishing, and forestry occupations |  | -0.01 |
| fambus_pay_yes |  | -0.01 |
| ind2_personal and laundry services |  | -0.01 |
| occ2_protective service occupations |  | -0.01 |
| diffany_has difficulty |  | -0.01 |
| statefip_south carolina |  | -0.011 |
| occ2_management occupations |  | -0.011 |
| bls_hhact_vehic |  | -0.011 |
| statefip_indiana |  | -0.011 |
| wrknumus_2 days |  | -0.011 |
| statefip_kentucky |  | -0.011 |
| schlcoll_high school part time |  | -0.011 |
| bls_pcare_act |  | -0.011 |
| wrkhomedays_yes |  | -0.011 |
| occ2_transportation and material moving occupations |  | -0.011 |
| statefip_oklahoma |  | -0.012 |
| bls_carehh_kidhealth |  | -0.012 |
| msasize_500,000 - 999,999 |  | -0.012 |
| famincome_$15,000 to $19,999 |  | -0.012 |
| bls_work_search |  | -0.012 |
| wrknumus_7 days |  | -0.012 |
| ageychild_16 |  | -0.012 |
| educ_some college but no degree |  | -0.012 |
| statefip_new mexico |  | -0.012 |
| statefip_north carolina |  | -0.013 |
| educyrs_tenth grade |  | -0.013 |
| statefip_nebraska |  | -0.013 |
| bls_purch_gov |  | -0.013 |
| educ_11th grade |  | -0.013 |
| statefip_south dakota |  | -0.013 |
| bls_hhact_pet |  | -0.014 |
| bls_social_mainten |  | -0.014 |
| famincome_$20,000 to $24,999 |  | -0.014 |
| bls_purch_bank |  | -0.014 |
| empstat_unemployed - looking |  | -0.014 |
| bls_hhact_exter |  | -0.014 |
| bls_purch_hhserv |  | -0.014 |
| clwkr_private, nonprofit |  | -0.015 |
| month_june |  | -0.015 |
| statefip_wisconsin |  | -0.015 |
| occ2_community and social service occupations |  | -0.015 |
| bls_purch_vehic |  | -0.015 |
| statefip_north dakota |  | -0.015 |
| marst_widowed |  | -0.015 |
| statefip_idaho |  | -0.016 |
| looking_no |  | -0.016 |
| dwell15_other |  | -0.016 |
| bls_social_admin |  | -0.016 |
| ind2_social assistance |  | -0.016 |
| dwell15_purchcons |  | -0.016 |
| bls_work_other |  | -0.016 |
| statefip_ohio |  | -0.016 |
| statefip_kansas |  | -0.016 |
| dwell30_hhserve |  | -0.017 |
| bls_hhact_inter |  | -0.017 |
| marst_divorced |  | -0.017 |
| looking_yes |  | -0.017 |
| educ_doctoral degree (phd, edd, etc.) |  | -0.017 |
| educyrs_doctoral degree |  | -0.017 |
| educ_10th grade |  | -0.017 |
| wrkhomeoften_3 to 4 days a week |  | -0.018 |
| clwkr_government, local |  | -0.018 |
| statefip_iowa |  | -0.018 |
| ind2_retail trade |  | -0.018 |
| retired_yes |  | -0.018 |
| bls_social_attend |  | -0.019 |
| bls_work_workrel |  | -0.019 |
| kidund1_no |  | -0.019 |
| bls_social_culture |  | -0.019 |
| hh_size_2 |  | -0.019 |
| occ |  | -0.02 |
| bls_comm |  | -0.02 |
| schlcoll_niu (not in universe) |  | -0.021 |
| hhtenure_occupied without payment of cash rent |  | -0.021 |
| race_white only |  | -0.021 |
| bls_carenhh_adultcare |  | -0.021 |
| msasize_250,000 - 499,999 |  | -0.021 |
| ind2_real estate |  | -0.022 |
| ind2_arts, entertainment, and recreation |  | -0.023 |
| msasize_100,000 - 249,999 |  | -0.023 |
| bls_educ_hwork |  | -0.023 |
| occ2_arts, design, entertainment, sports, and media occupations |  | -0.023 |
| holiday_yes |  | -0.024 |
| bls_leis_tv |  | -0.025 |
| dwell15_purchserv |  | -0.025 |
| bls_social_travel |  | -0.025 |
| wrkhomepd_niu (not in universe) |  | -0.025 |
| wrknumus_niu (not in universe) |  | -0.025 |
| wrkhomeable_niu (not in universe) |  | -0.025 |
| wrkhomeev_niu (not in universe) |  | -0.025 |
| wrkflexhrs_niu (not in universe) |  | -0.025 |
| wrkhomeoften_niu (not in universe) |  | -0.025 |
| wrkhomedays_niu (not in universe) |  | -0.025 |
| bls_comm_tele |  | -0.026 |
| empstat_not in labor force |  | -0.026 |
| ind2_membership associations and organizations |  | -0.027 |
| dwell15_carenhh |  | -0.027 |
| sex_female |  | -0.028 |
| dwell15_pcare |  | -0.029 |
| bls_leis_attsport |  | -0.029 |
| clwkr_niu (not in universe) |  | -0.029 |
| fullpart_niu (not in universe) |  | -0.029 |
| multjobs_niu (not in universe) |  | -0.029 |
| occ2_niu (not in universe) |  | -0.029 |
| ind2_niu (not in universe) |  | -0.029 |
| occ2_sales and related occupations |  | -0.029 |
| bls_social_socserv |  | -0.029 |
| occ2_food preparation and serving related occupations |  | -0.03 |
| metro_metropolitan, not identified |  | -0.03 |
| dwell30_other |  | -0.031 |
| bls_educ_travel |  | -0.031 |
| schlcoll_college/university full time |  | -0.031 |
| kid13to17_no |  | -0.031 |
| bls_food_food |  | -0.032 |
| uhrsworkt |  | -0.032 |
| dwell15_spiritual |  | -0.032 |
| dwell30_hhact |  | -0.032 |
| bls_carenhh_kid |  | -0.032 |
| region_midwest |  | -0.032 |
| bls_hhact_lawn |  | -0.032 |
| wrkhomeoften_5 or more days a week |  | -0.033 |
| ind2_educational services |  | -0.034 |
| occ2_personal care and service occupations |  | -0.034 |
| dwell30_educ |  | -0.034 |
| hourwage |  | -0.035 |
| dwell15_educ |  | -0.035 |
| bls_carenhh_adulthelp |  | -0.035 |
| vetstat_niu (not in universe) |  | -0.036 |
| bls_purch_pcare |  | -0.036 |
| ind2_food services and drinking places |  | -0.036 |
| bls_purch_health |  | -0.037 |
| dwell30_spiritual |  | -0.037 |
| hh_numadults_1 |  | -0.038 |
| bls_carenhh_adult |  | -0.04 |
| dwell30_carenhh |  | -0.04 |
| bls_carenhh |  | -0.041 |
| empstat_employed - absent |  | -0.041 |
| bls_food_travel |  | -0.042 |
| bls_food |  | -0.042 |
| bls_leis_relax |  | -0.042 |
| ind |  | -0.043 |
| occ2_education, training, and library occupations |  | -0.043 |
| dwell30_carehh |  | -0.043 |
| bls_other |  | -0.043 |
| multjobs_yes |  | -0.044 |
| kid1to2_no |  | -0.044 |
| fambus_spouse_yes |  | -0.045 |
| dwell15_religious |  | -0.045 |
| bls_leis_attend |  | -0.045 |
| fambus_pay_no |  | -0.045 |
| schlcoll_high school full time |  | -0.046 |
| marst_never married |  | -0.046 |
| dwell30_purchserv |  | -0.047 |
| bls_purch |  | -0.047 |
| dwell30_religious |  | -0.047 |
| bls_hhact |  | -0.048 |
| bls_educ_class |  | -0.048 |
| clwkr_self-employed, incorporated |  | -0.048 |
| bls_educ |  | -0.048 |
| bls_social_volact |  | -0.05 |
| spearnweek |  | -0.05 |
| bls_social_vol |  | -0.05 |
| kid3to5_no |  | -0.05 |
| scc_own |  | -0.052 |
| ind2_agriculture |  | -0.052 |
| bls_purch_prof |  | -0.053 |
| bls_leis_arts |  | -0.053 |
| metro_nonmetropolitan |  | -0.054 |
| hh_size_1 |  | -0.054 |
| kid6to12_no |  | -0.054 |
| dwell15_food |  | -0.057 |
| msasize_not identified or non-metropolitan |  | -0.057 |
| bpl_u.s., n.s |  | -0.058 |
| citizen_native, born in united states |  | -0.058 |
| scc_all |  | -0.058 |
| bls_social_relig |  | -0.058 |
| fullpart_part time |  | -0.059 |
| speduc_niu (not in universe) |  | -0.06 |
| spempnot_niu (not in universe) |  | -0.06 |
| spousepres_no spouse or unmarried partner present |  | -0.06 |
| spsex_niu (not in universe) |  | -0.06 |
| spempstat_niu (not in universe) |  | -0.06 |
| sprace_niu (not in universe) |  | -0.06 |
| spage |  | -0.061 |
| dwell15_sport |  | -0.061 |
| bls_purch_groc |  | -0.062 |
| bls_hhact_hwork |  | -0.066 |
| bls_leis_travel |  | -0.069 |
| hh_child_no |  | -0.069 |
| hh_numkids_0 |  | -0.069 |
| ageychild_niu (not in universe) |  | -0.069 |
| bls_social |  | -0.07 |
| dwell30_sport |  | -0.072 |
| bls_leis_soccomex |  | -0.075 |
| dwell30_food |  | -0.081 |
| clwkr_self-employed, unincorporated |  | -0.081 |
| dwell15_social |  | -0.082 |
| kidund13_no |  | -0.083 |
| bls_leis_partsport |  | -0.084 |
| wrkdaysavg |  | -0.084 |
| avgdur |  | -0.087 |
| bls_leis_soccom |  | -0.087 |
| kidund18_no |  | -0.088 |
| bls_leis_sport |  | -0.089 |
| bls_leis_soc |  | -0.09 |
| dwell30_purchcons |  | -0.093 |
| dwell30_pcare |  | -0.093 |
| dwell30_social |  | -0.099 |
| earnweek |  | -0.1 |
| otusual_niu (not in universe) |  | -0.101 |
| paidhour_niu (not in universe) |  | -0.101 |
| bls_purch_cons |  | -0.103 |
| fambus_family business |  | -0.104 |
| fambus_resp_yes |  | -0.104 |
| day_saturday |  | -0.114 |
| bls_leis |  | -0.121 |
| day_sunday |  | -0.131 |
| bls_pcare |  | -0.132 |
| bls_pcare_sleep |  | -0.135 |
| dwell15_None |  | nan |
| dwell30_None |  | nan |
| hh_size_14 |  | nan |
| hh_size_15 |  | nan |
| hh_size_16 |  | nan |
| hh_numkids_12 |  | nan |
| housetype_unit not permanent, in transient hotel or motel |  | nan |
| hh_numadults_12 |  | nan |
| race_other 3 race combinations |  | nan |
| bpl_nothern marianas |  | nan |
| bpl_iceland |  | nan |
| bpl_wales |  | nan |
| bpl_montenegro |  | nan |
| bpl_marshall islands |  | nan |
| bpl_micronesia |  | nan |
| popstat_adult civilian |  | nan |
| looking_retired |  | nan |
| looking_disabled |  | nan |
| sprace_asian or pacific islander |  | nan |
| sprace_black-hawaiian |  | nan |
| sprace_white-american indian-asian |  | nan |
| sprace_other 3 race combinations |  | nan |
| sprace_2 or 3 races, unspecified |  | nan |
| sprace_4 or 5 races, unspecified |  | nan |

</details>


## PSID

[Panel Study of Income Dynamics](https://psidonline.isr.umich.edu/)

Correlations of time spent commuting by primary respondant in 2019.
Question was "On a typical day, how many minutes is your round trip commute to and from work?"

And this looks only at the subset of primary respondants who answered positively to 
"In a typical week, how many hours do you spend working for pay?"

Some things that are positively correlated with commute time
- time spent commuting by this person in other years
- time spent by spouse commuting in 2019
- the amount of money spent on variable transportation costs (gas)
- total expenditures
- labor income
- family income 

Some things that are negatively correlated:
- amount of social security recieved
- time spent caring for adults
- time spent volunteering
- time spent on leisure
- time spent on housework
- time spent on shopping
- expenditures on the home



<details markdown="block"><summary>Click for full list of correlations.</summary>

Note as of 2023 April 14: Minimal processing has been done. So some of these, especially near the bottom are "correlations" on categorical data which is just coded with numbers. These have no actually meaning.

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|
| 'time_commute1_19' |  | 1.0 |
| 'time_commute1_17' |  | 0.411 |
| 'time_commute1_15' |  | 0.329 |
| 'time_commute1_13' |  | 0.268 |
| 'time_commute1_11' |  | 0.23 |
| 'time_commute2_19' |  | 0.16 |
| 'realcost_transportation_variable_19' |  | 0.124 |
| 'cost_transportation_variable_19' |  | 0.124 |
| 'cost_transportation_variable_17' |  | 0.1 |
| 'realcost_transportation_variable_17' |  | 0.1 |
| 'time_commute2_17' |  | 0.097 |
| 'time_commute2_13' |  | 0.092 |
| 'cost_total_19' |  | 0.088 |
| 'realcost_total_19' |  | 0.088 |
| 'time_commute2_11' |  | 0.088 |
| 'realcost_transportation_19' |  | 0.087 |
| 'cost_transportation_19' |  | 0.087 |
| 'totallaborincome1_19' |  | 0.076 |
| 'realtotallaborincome1_19' |  | 0.076 |
| 'time_commute2_15' |  | 0.074 |
| 'realwageandsal1_19' |  | 0.074 |
| 'wageandsal1_19' |  | 0.074 |
| 'totallaborincome1_17' |  | 0.071 |
| 'realtotallaborincome1_17' |  | 0.071 |
| 'cost_housing_19' |  | 0.071 |
| 'realcost_housing_19' |  | 0.071 |
| 'wageandsal1_17' |  | 0.069 |
| 'realwageandsal1_17' |  | 0.069 |
| 'realwagerate1_17' |  | 0.067 |
| 'wagerate1_17' |  | 0.067 |
| 'realcost_transportation_17' |  | 0.066 |
| 'cost_transportation_17' |  | 0.066 |
| 'realwagerate1_19' |  | 0.064 |
| 'wagerate1_19' |  | 0.064 |
| 'actualhourlywage1_19' |  | 0.064 |
| 'realactualhourlywage1_19' |  | 0.064 |
| 'realcost_telecom_19' |  | 0.063 |
| 'cost_telecom_19' |  | 0.063 |
| 'UP: MONTH LAST IN SCHOOL IF NEITHER 17' |  | 0.062 |
| 'realcost_childcare_17' |  | 0.062 |
| 'cost_childcare_17' |  | 0.062 |
| 'race2_19' |  | 0.062 |
| 'H5N/H50A CKPT WTR INDIVIDUAL IS 65+ 19' |  | 0.06 |
| 'sex2_19' |  | 0.06 |
| 'MARITAL PAIRS INDICATOR 19' |  | 0.059 |
| 'time_work1_19' |  | 0.059 |
| 'cost_transportation_variable_15' |  | 0.058 |
| 'realcost_transportation_variable_15' |  | 0.058 |
| 'cost_housing_17' |  | 0.058 |
| 'realcost_housing_17' |  | 0.058 |
| 'cost_telecom_17' |  | 0.057 |
| 'realcost_telecom_17' |  | 0.057 |
| 'realfamilyincome_19' |  | 0.056 |
| 'familyincome_19' |  | 0.056 |
| 'realcost_telecom_15' |  | 0.056 |
| 'cost_telecom_15' |  | 0.056 |
| 'TYPE OF IND RECORD 95' |  | 0.056 |
| 'WHY NONRESPONSE 95' |  | 0.055 |
| 'cost_housing_15' |  | 0.054 |
| 'realcost_housing_15' |  | 0.054 |
| 'WHY NONRESPONSE 99' |  | 0.054 |
| 'WHY NONRESPONSE 97' |  | 0.053 |
| 'WHY NONRESPONSE 01' |  | 0.053 |
| 'WHY NONRESPONSE 96' |  | 0.053 |
| 'WTR ALWAYS IN RESPONDING FAMILY UNIT' |  | 0.052 |
| 'TYPE OF IND RECORD 01' |  | 0.052 |
| 'WHY NONRESPONSE 94' |  | 0.051 |
| 'TYPE OF IND RECORD 94' |  | 0.051 |
| 'TYPE OF IND RECORD 96' |  | 0.051 |
| 'TYPE OF IND RECORD 99' |  | 0.051 |
| 'TYPE OF IND RECORD 97' |  | 0.051 |
| 'realcost_housing_13' |  | 0.05 |
| 'cost_housing_13' |  | 0.05 |
| 'ACC HOURS UNEMP 1979 80' |  | 0.05 |
| 'realtotallaborincome1_15' |  | 0.049 |
| 'totallaborincome1_15' |  | 0.049 |
| 'realcost_food_19' |  | 0.049 |
| 'cost_food_19' |  | 0.049 |
| 'TYPE OF IND RECORD 93' |  | 0.049 |
| 'realwageandsal1_15' |  | 0.048 |
| 'wageandsal1_15' |  | 0.048 |
| 'WHY NONRESPONSE 03' |  | 0.048 |
| 'WHY NONRESPONSE 05' |  | 0.048 |
| 'familyincome_17' |  | 0.047 |
| 'realfamilyincome_17' |  | 0.047 |
| 'time_housework2_19' |  | 0.047 |
| 'time_work2_alt_19' |  | 0.047 |
| 'realcost_utility_19' |  | 0.047 |
| 'cost_utility_19' |  | 0.047 |
| 'realwagerate1_15' |  | 0.047 |
| 'wagerate1_15' |  | 0.047 |
| 'WHY NONRESPONSE 93' |  | 0.047 |
| 'realcost_transportation_15' |  | 0.046 |
| 'cost_transportation_15' |  | 0.046 |
| 'FOREIGN DEGREE 17' |  | 0.046 |
| 'MARITAL STATUS OF MOTHER AT BIRTH' |  | 0.046 |
| 'realwagerate1_13' |  | 0.046 |
| 'wagerate1_13' |  | 0.046 |
| 'realwageandsal1_11' |  | 0.046 |
| 'wageandsal1_11' |  | 0.046 |
| 'TYPE OF IND RECORD 15' |  | 0.045 |
| 'YEAR MOTHER BORN' |  | 0.045 |
| 'TYPE OF IND RECORD 92' |  | 0.045 |
| 'ORDER OF BIRTH TO MOTHER' |  | 0.045 |
| 'WHY NONRESPONSE 15' |  | 0.045 |
| 'TOTAL # CHILDREN BORN TO MOTHER' |  | 0.045 |
| 'WHY NONRESPONSE 07' |  | 0.045 |
| 'YEAR BIRTH INFO MOST RECENTLY UPDATED' |  | 0.045 |
| 'time_work1_alt_19' |  | 0.045 |
| 'time_work2_19' |  | 0.044 |
| 'TYPE OF IND RECORD 03' |  | 0.044 |
| 'WHY NONRESPONSE 92' |  | 0.044 |
| 'TYPE OF IND RECORD 05' |  | 0.044 |
| 'TYPE OF IND RECORD 88' |  | 0.044 |
| 'cost_telecom_11' |  | 0.044 |
| 'realcost_telecom_11' |  | 0.044 |
| 'WHY NONRESPONSE 88' |  | 0.044 |
| 'age2_19' |  | 0.043 |
| 'cohort2_19' |  | 0.043 |
| 'totallaborincome1_11' |  | 0.043 |
| 'realtotallaborincome1_11' |  | 0.043 |
| 'FOREIGN DEGREE 19' |  | 0.043 |
| 'time_totalhours2_19' |  | 0.043 |
| 'time_work2_altalt_19' |  | 0.043 |
| 'realcost_utility_17' |  | 0.043 |
| 'cost_utility_17' |  | 0.043 |
| 'time_work1_altalt_19' |  | 0.042 |
| 'time_totalhours1_19' |  | 0.042 |
| 'cost_childcare_19' |  | 0.042 |
| 'realcost_childcare_19' |  | 0.042 |
| 'YEAR THIS INDIVIDUAL'S COHORT BEGAN' |  | 0.041 |
| 'cost_health_19' |  | 0.041 |
| 'realcost_health_19' |  | 0.041 |
| 'realcost_childcare_13' |  | 0.041 |
| 'cost_childcare_13' |  | 0.041 |
| 'WHETHER EDUCATED IN US 19' |  | 0.04 |
| 'cost_homeinsurance_19' |  | 0.04 |
| 'realcost_homeinsurance_19' |  | 0.04 |
| 'cost_housing_11' |  | 0.04 |
| 'realcost_housing_11' |  | 0.04 |
| 'race2_17' |  | 0.04 |
| 'WHY NONRESPONSE 09' |  | 0.04 |
| 'TYPE OF IND RECORD 91' |  | 0.04 |
| 'ACC G84D_G94D IMPUTED - WELFARE 13' |  | 0.04 |
| 'WHY NONRESPONSE 87' |  | 0.04 |
| 'WHY NONRESPONSE 91' |  | 0.039 |
| 'actualhourlywage1_13' |  | 0.039 |
| 'realactualhourlywage1_13' |  | 0.039 |
| 'TYPE OF IND RECORD 87' |  | 0.039 |
| 'WTR ORIGINAL SAMPLE/BORN IN/MOVED IN' |  | 0.039 |
| 'MONTH MOVED IN/OUT 17' |  | 0.039 |
| 'UP: GRADE CURRENTLY ENROLLED 17' |  | 0.038 |
| 'realwagerate1_11' |  | 0.038 |
| 'wagerate1_11' |  | 0.038 |
| 'realcost_childcare_15' |  | 0.038 |
| 'cost_childcare_15' |  | 0.038 |
| 'cost_transportation_variable_13' |  | 0.038 |
| 'realcost_transportation_variable_13' |  | 0.038 |
| 'race1_13' |  | 0.037 |
| 'WHY NONRESPONSE 89' |  | 0.037 |
| 'totallaborincome1_13' |  | 0.037 |
| 'realtotallaborincome1_13' |  | 0.037 |
| 'HIGHEST DEGREE MAJOR MEN1 2-DIGIT 19' |  | 0.037 |
| 'WHY NONRESPONSE 90' |  | 0.037 |
| 'YEARS OF FOREIGN EDUCATION 19' |  | 0.037 |
| 'ACC G84M_G94F IMPUTED - OTHER INCOME 11' |  | 0.036 |
| 'TYPE OF IND RECORD 89' |  | 0.036 |
| 'TYPE OF IND RECORD 90' |  | 0.036 |
| 'YEARS OF FOREIGN EDUCATION 17' |  | 0.036 |
| 'TYPE OF IND RECORD 83' |  | 0.036 |
| 'realcost_transportation_variable_11' |  | 0.036 |
| 'cost_transportation_variable_11' |  | 0.036 |
| 'WHY NONRESPONSE 83' |  | 0.036 |
| 'wageandsal1_13' |  | 0.036 |
| 'realwageandsal1_13' |  | 0.036 |
| 'realfamilyincome_15' |  | 0.036 |
| 'familyincome_15' |  | 0.036 |
| 'TYPE OF IND RECORD 81' |  | 0.035 |
| 'ACC TRANSFER Y 76' |  | 0.035 |
| 'WHY NONRESPONSE 72' |  | 0.035 |
| 'realactualhourlywage1_15' |  | 0.035 |
| 'actualhourlywage1_15' |  | 0.035 |
| 'WHY NONRESPONSE 86' |  | 0.035 |
| 'TYPE OF IND RECORD 07' |  | 0.035 |
| 'race2_13' |  | 0.035 |
| 'WTR EVER OUT OF STUDY 1 YEAR OR MORE' |  | 0.035 |
| 'TYPE OF IND RECORD 72' |  | 0.035 |
| 'SAMPLING ERROR STRATUM' |  | 0.035 |
| 'TYPE OF IND RECORD 86' |  | 0.035 |
| 'RESPONDENT? 19' |  | 0.035 |
| 'WHY NONRESPONSE 81' |  | 0.034 |
| 'TYPE OF IND RECORD 84' |  | 0.034 |
| 'WHY NONRESPONSE 69' |  | 0.034 |
| 'GRADE CURRENTLY ENROLLED 17' |  | 0.034 |
| 'time_pcare2_19' |  | 0.034 |
| 'TYPE OF IND RECORD 85' |  | 0.034 |
| 'WHY NONRESPONSE 75' |  | 0.034 |
| 'time_childcare2_19' |  | 0.034 |
| 'TYPE OF IND RECORD 75' |  | 0.034 |
| 'race2_15' |  | 0.033 |
| 'nkids_19' |  | 0.033 |
| 'realfamilyincome_13' |  | 0.033 |
| 'familyincome_13' |  | 0.033 |
| 'WHY NONRESPONSE 85' |  | 0.033 |
| 'WHY NONRESPONSE 80' |  | 0.033 |
| 'race1_11' |  | 0.033 |
| 'WHY NONRESPONSE 68' |  | 0.033 |
| 'WHY NONRESPONSE 11' |  | 0.033 |
| 'FOLLOW STATUS 19' |  | 0.033 |
| 'time_childcare2_17' |  | 0.033 |
| 'realcost_education_15' |  | 0.033 |
| 'cost_education_15' |  | 0.033 |
| 'realcost_transportation_11' |  | 0.033 |
| 'cost_transportation_11' |  | 0.033 |
| 'time_work1_alt_17' |  | 0.032 |
| 'WHY NONRESPONSE 84' |  | 0.032 |
| 'WHY NONRESPONSE 73' |  | 0.032 |
| 'WHY NONRESPONSE 70' |  | 0.032 |
| 'FOLLOW STATUS 17' |  | 0.032 |
| 'TYPE OF IND RECORD 69' |  | 0.032 |
| 'TYPE OF IND RECORD 73' |  | 0.032 |
| 'BACHELOR DEGREE MAJOR MEN1 2-DIGIT 19' |  | 0.032 |
| 'TYPE OF IND RECORD 80' |  | 0.032 |
| 'TYPE OF IND RECORD 68' |  | 0.031 |
| 'WHY NONRESPONSE 71' |  | 0.031 |
| 'time_leisure2_19' |  | 0.031 |
| 'time_work1_altalt_17' |  | 0.031 |
| 'time_totalhours1_17' |  | 0.031 |
| 'WHY NONRESPONSE 13' |  | 0.031 |
| 'YEAR GRADUATED BACHELOR DEGREE 17' |  | 0.031 |
| 'WHY NONRESPONSE 76' |  | 0.031 |
| 'G88 MO LAST IN SCH-IND 91' |  | 0.031 |
| 'MONTH GRADUATED BACHELOR DEGREE 17' |  | 0.031 |
| 'TOT HRS UNEMP 78 79' |  | 0.03 |
| 'BACHELOR DEGREE MAJOR MEN1 17' |  | 0.03 |
| 'WTR COVERED BY TANF PAYMENTS IN 2018 19' |  | 0.03 |
| 'BIRTH WEIGHT OF THIS INDIVIDUAL' |  | 0.03 |
| 'YEAR MOVED IN/OUT 17' |  | 0.03 |
| 'YEAR MOST RECENT MARRIAGE ENDED' |  | 0.03 |
| 'TYPE OF IND RECORD 76' |  | 0.03 |
| 'realcost_homeinsurance_11' |  | 0.03 |
| 'cost_homeinsurance_11' |  | 0.03 |
| 'TYPE OF IND RECORD 70' |  | 0.03 |
| 'MONTH MOST RECENT MARRIAGE ENDED' |  | 0.03 |
| 'UP: BACHELOR DEGREE MAJOR MEN2 15' |  | 0.03 |
| 'time_housework2_15' |  | 0.03 |
| 'cost_clothing_17' |  | 0.03 |
| 'realcost_clothing_17' |  | 0.03 |
| 'realcost_food_17' |  | 0.029 |
| 'cost_food_17' |  | 0.029 |
| 'WHY NONRESPONSE 74' |  | 0.029 |
| 'TYPE OF IND RECORD 71' |  | 0.029 |
| 'WHETHER MOVED IN/OUT 81' |  | 0.029 |
| 'SEQUENCE NUMBER 15' |  | 0.029 |
| 'MONTH GRADUATED BACHELOR DEGREE 15' |  | 0.029 |
| 'realcost_food_11' |  | 0.029 |
| 'cost_food_11' |  | 0.029 |
| 'YEAR GRADUATED BACHELOR DEGREE 19' |  | 0.029 |
| 'ACC G84M_G94F IMPUTED - OTHER INCOME 13' |  | 0.029 |
| 'TYPE OF IND RECORD 09' |  | 0.029 |
| 'BACHELOR DEGREE MAJOR MEN1 15' |  | 0.029 |
| 'TYPE OF IND RECORD 74' |  | 0.029 |
| 'WHY NONRESPONSE 77' |  | 0.029 |
| 'cost_education_13' |  | 0.029 |
| 'realcost_education_13' |  | 0.029 |
| 'WHY NONRESPONSE 82' |  | 0.029 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 05' |  | 0.029 |
| 'WHY NONRESPONSE 79' |  | 0.028 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 05' |  | 0.028 |
| 'WHY NONRESPONSE 78' |  | 0.028 |
| 'ACC HOURS WORKED 1979 80' |  | 0.028 |
| 'MONTH GRADUATED BACHELOR DEGREE 19' |  | 0.028 |
| 'TYPE OF IND RECORD 13' |  | 0.028 |
| 'YEAR SEPARATED MOST RECENT MARRIAGE' |  | 0.028 |
| 'YEAR GRADUATED BACHELOR DEGREE 15' |  | 0.028 |
| 'TYPE OF IND RECORD 82' |  | 0.028 |
| 'ACC G84C_G94C IMPUTED - SSI 07' |  | 0.028 |
| 'R44 WTR RECD GEN ASSISTANCE IN 2003 05' |  | 0.028 |
| 'cost_food_15' |  | 0.028 |
| 'realcost_food_15' |  | 0.028 |
| 'realcost_transportation_13' |  | 0.027 |
| 'cost_transportation_13' |  | 0.027 |
| 'MARITAL PAIRS INDICATOR 17' |  | 0.027 |
| 'cost_trips_19' |  | 0.027 |
| 'realcost_trips_19' |  | 0.027 |
| 'TYPE OF IND RECORD 78' |  | 0.027 |
| 'HIGHEST YEAR COLLEGE COMPLETED 19' |  | 0.027 |
| 'cost_utility_15' |  | 0.027 |
| 'realcost_utility_15' |  | 0.027 |
| 'TYPE OF IND RECORD 79' |  | 0.027 |
| 'id1968_17' |  | 0.027 |
| 'time_work2_alt_13' |  | 0.027 |
| 'realcost_clothing_19' |  | 0.027 |
| 'cost_clothing_19' |  | 0.027 |
| 'Unnamed: 0' |  | 0.026 |
| 'ACC G84B IMPUTED - TANF 09' |  | 0.026 |
| 'H18 B/C OF HEALTH? 92' |  | 0.026 |
| 'H20 B/C OF HEALTH? 92' |  | 0.026 |
| 'ACC G84D_G94D IMPUTED - WELFARE 05' |  | 0.026 |
| 'UP: HIGHEST DEGREE MAJOR MEN2 17' |  | 0.026 |
| 'TYPE OF IND RECORD 77' |  | 0.026 |
| 'cost_home_15' |  | 0.026 |
| 'realcost_home_15' |  | 0.026 |
| 'UP: MONTH GRADUATED BACHELOR DEGREE 19' |  | 0.026 |
| 'FOREIGN DEGREE 15' |  | 0.026 |
| 'realcost_trips_13' |  | 0.026 |
| 'cost_trips_13' |  | 0.026 |
| 'cost_health_17' |  | 0.026 |
| 'realcost_health_17' |  | 0.026 |
| 'realtotallaborincome2_19' |  | 0.026 |
| 'totallaborincome2_19' |  | 0.026 |
| 'MONTH SEPARATED MOST RECENT MARRIAGE' |  | 0.026 |
| 'H5N/H50A CKPT WTR INDIVIDUAL IS 65+ 17' |  | 0.026 |
| 'wageandsal2_19' |  | 0.026 |
| 'realwageandsal2_19' |  | 0.026 |
| 'time_work1_17' |  | 0.026 |
| 'sex2_17' |  | 0.025 |
| 'RELATION TO REFERENCE PERSON 17' |  | 0.025 |
| 'id' |  | 0.025 |
| '1968 INTERVIEW NUMBER' |  | 0.025 |
| 'id1968_19' |  | 0.025 |
| 'cost_food_13' |  | 0.025 |
| 'realcost_food_13' |  | 0.025 |
| 'ACC TOT TRNSFR Y-IND 90' |  | 0.025 |
| 'UP: YEAR GRADUATED BACHELOR DEGREE 15' |  | 0.025 |
| 'UP: YEAR GRADUATED HIGHEST DEGREE 15' |  | 0.025 |
| 'RESPONDENT? 17' |  | 0.024 |
| 'MONTH FIRST/ONLY MARRIAGE ENDED' |  | 0.024 |
| 'cost_telecom_13' |  | 0.024 |
| 'realcost_telecom_13' |  | 0.024 |
| 'MONTH S/O FAM FORMED 19' |  | 0.023 |
| 'id1968_13' |  | 0.023 |
| 'TYPE OF IND RECORD 11' |  | 0.023 |
| 'race1_17' |  | 0.023 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 07' |  | 0.023 |
| 'id1968_15' |  | 0.023 |
| 'realcost_education_11' |  | 0.023 |
| 'cost_education_11' |  | 0.023 |
| 'actualhourlywage1_17' |  | 0.023 |
| 'realactualhourlywage1_17' |  | 0.023 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 8 95' |  | 0.023 |
| 'realcost_homeinsurance_15' |  | 0.023 |
| 'cost_homeinsurance_15' |  | 0.023 |
| 'nkids_17' |  | 0.023 |
| 'sex2_15' |  | 0.023 |
| 'realtotallaborincome2_15' |  | 0.022 |
| 'totallaborincome2_15' |  | 0.022 |
| 'WHETHER MOVED IN/OUT 15' |  | 0.022 |
| 'PERSON NUMBER 68' |  | 0.022 |
| 'MONTH MOVED IN/OUT 03' |  | 0.022 |
| 'FOLLOW STATUS 13' |  | 0.022 |
| 'time_totalhours2_13' |  | 0.022 |
| 'time_work2_altalt_13' |  | 0.022 |
| 'MONTH RECEIVED GED 19' |  | 0.022 |
| 'time_work2_altalt_15' |  | 0.022 |
| 'time_totalhours2_15' |  | 0.022 |
| 'H61F SN 1ST PERSON EMP PROVIDES INS 17' |  | 0.022 |
| 'realfamilyincome_11' |  | 0.022 |
| 'familyincome_11' |  | 0.022 |
| 'cost_utility_11' |  | 0.021 |
| 'realcost_utility_11' |  | 0.021 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 4 95' |  | 0.021 |
| '# WEEKS IN SCHOOL 81' |  | 0.021 |
| 'MONTH GRADUATED HIGH SCHOOL 19' |  | 0.021 |
| 'realwagerate2_19' |  | 0.021 |
| 'wagerate2_19' |  | 0.021 |
| 'G84B IMPUTED TANF 09' |  | 0.021 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 07' |  | 0.021 |
| 'time_education2_19' |  | 0.021 |
| 'YEAR MOVED IN/OUT 03' |  | 0.021 |
| 'realwageandsal2_15' |  | 0.021 |
| 'wageandsal2_15' |  | 0.021 |
| 'YEAR MOVED IN/OUT 07' |  | 0.021 |
| 'month_19' |  | 0.021 |
| 'cost_education_17' |  | 0.021 |
| 'realcost_education_17' |  | 0.021 |
| 'MONTH SEPARATED FIRST/ONLY MARRIAGE' |  | 0.021 |
| 'MAIN FAM ID FOR S/O 96' |  | 0.02 |
| 'YEAR S/O FAM FORMED 19' |  | 0.02 |
| 'R2 WTR RECEIVED PUB ASSTNCE IN 1997 99' |  | 0.02 |
| 'ACC TOT TAXABLE Y 79 80' |  | 0.02 |
| 'race1_15' |  | 0.02 |
| 'ACC TOT TAXBL INC 78' |  | 0.02 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 13' |  | 0.02 |
| 'R48A WTR STOPPED WELFARE IN 1999 01' |  | 0.02 |
| 'race2_11' |  | 0.02 |
| 'WHETHER MOVED IN/OUT 19' |  | 0.02 |
| 'ES3 WTR US CITIZEN OUT OF US IN 68 97' |  | 0.02 |
| 'race1_19' |  | 0.02 |
| 'MONTH S/O FAM FORMED 96' |  | 0.02 |
| 'MOVED IN/OUT 93' |  | 0.02 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 03' |  | 0.019 |
| 'YEARS COMPLETED EDUCATION 19' |  | 0.019 |
| 'realcost_utility_13' |  | 0.019 |
| 'cost_utility_13' |  | 0.019 |
| 'UP: YEAR GRADUATED BACHELOR DEGREE 19' |  | 0.019 |
| 'cohort2_17' |  | 0.019 |
| 'age2_17' |  | 0.019 |
| 'cost_trips_15' |  | 0.019 |
| 'realcost_trips_15' |  | 0.019 |
| 'id1968_11' |  | 0.019 |
| 'MAIN FAM ID FOR S/O 01' |  | 0.019 |
| 'ACC TOT TRANSFER Y 84' |  | 0.019 |
| 'time_work1_altalt_15' |  | 0.019 |
| 'time_totalhours1_15' |  | 0.019 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 07' |  | 0.019 |
| 'YEAR SEPARATED FIRST/ONLY MARRIAGE' |  | 0.019 |
| 'UP: HIGHEST YEAR COLLEGE COMPLETED 15' |  | 0.019 |
| 'HIGHEST YEAR COLLEGE COMPLETED 17' |  | 0.019 |
| 'month_11' |  | 0.019 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 6 95' |  | 0.019 |
| 'MAIN FAM ID FOR S/O 90' |  | 0.018 |
| 'MONTH RECEIVED GED 17' |  | 0.018 |
| 'MONTH LAST ATTENDED COLLEGE 15' |  | 0.018 |
| 'UP: MONTH GRADUATED HIGHEST DEGREE 15' |  | 0.018 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 17' |  | 0.018 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 17' |  | 0.018 |
| 'UP: BACHELOR DEG MAJOR MEN2 2-DIGIT 19' |  | 0.018 |
| 'YEAR FIRST/ONLY MARRIAGE ENDED' |  | 0.018 |
| 'ACC IND WRK HRS 76' |  | 0.018 |
| 'MONTH MOVED IN/OUT 93' |  | 0.018 |
| 'time_work2_alt_17' |  | 0.018 |
| 'UP: WTR ATTENDED COLLEGE 19' |  | 0.018 |
| 'time_housework1_13' |  | 0.018 |
| 'UP: WTR RECEIVED COLLEGE DEGREE 19' |  | 0.018 |
| 'FOLLOW STATUS 11' |  | 0.018 |
| 'cost_furnish_17' |  | 0.017 |
| 'realcost_furnish_17' |  | 0.017 |
| 'UP: MONTH GRADUATED HIGHEST DEGREE 17' |  | 0.017 |
| 'UP: GRADE CURRENTLY ENROLLED 19' |  | 0.017 |
| 'UP: MONTH LAST ATTENDED COLLEGE 19' |  | 0.017 |
| 'HEALTH GOOD? 17' |  | 0.017 |
| 'realcost_childcare_11' |  | 0.017 |
| 'cost_childcare_11' |  | 0.017 |
| 'G84K IMPUTED CHILD SUPPORT 09' |  | 0.017 |
| 'UP: YEAR LAST ATTENDED COLLEGE 19' |  | 0.017 |
| 'time_work2_alt_15' |  | 0.017 |
| 'WTR INDIVIDUAL HAS CENSUS MATCH RECORD' |  | 0.017 |
| 'realtotallaborincome2_13' |  | 0.017 |
| 'totallaborincome2_13' |  | 0.017 |
| '1997 INTERVIEW NUMBER' |  | 0.017 |
| 'time_housework2_17' |  | 0.017 |
| 'R38 WTR RECEIVED WORKERS COMP IN 2003 05' |  | 0.017 |
| 'WHETHER STUDENT 82' |  | 0.017 |
| 'R34 WTR RECEIVED UNEMP COMP IN 2005 07' |  | 0.017 |
| 'FOLLOW STATUS 15' |  | 0.017 |
| 'YEAR GRADUATED HIGH SCHOOL 19' |  | 0.017 |
| 'RESULT OF CDS INTERVIEW 01' |  | 0.017 |
| 'YEAR S/O FAM FORMED 01' |  | 0.017 |
| 'R4 WTR RECD ADC IN 1997 99' |  | 0.016 |
| 'WHETHER STUDENT 93' |  | 0.016 |
| 'G88 YR LAST IN SCH 86' |  | 0.016 |
| 'YEAR MOVED IN/OUT 13' |  | 0.016 |
| 'WHETHER MOVED IN/OUT 13' |  | 0.016 |
| 'G84G IMPUTED PENSION/ANN 05' |  | 0.016 |
| 'ACC G84K IMPUTED - CHILD SUPPORT 09' |  | 0.016 |
| 'YEAR GRADUATED HIGHEST DEGREE 19' |  | 0.016 |
| 'ACC TRANSFER Y 79 80' |  | 0.016 |
| 'time_leisure2_17' |  | 0.016 |
| 'HIGHEST DEGREE MAJOR MEN2 2-DIGIT 19' |  | 0.016 |
| 'MONTH MOVED IN/OUT 07' |  | 0.016 |
| 'M31 MONTH LAST RELEASED 95' |  | 0.016 |
| 'ES1 COUNTY/COUNTRY WHERE BORN 97' |  | 0.016 |
| 'time_housework2_11' |  | 0.016 |
| 'cohort2_15' |  | 0.016 |
| 'age2_15' |  | 0.016 |
| 'wagerate2_15' |  | 0.016 |
| 'realwagerate2_15' |  | 0.016 |
| 'ES2 WHETHER LIVED IN US IN 1968 97' |  | 0.016 |
| 'G84C_G94C IMPUTED SSI 13' |  | 0.016 |
| 'YEAR S/O FAM FORMED 85' |  | 0.016 |
| 'GRADE CURRENTLY ENROLLED 13' |  | 0.016 |
| 'MONTH S/O FAM FORMED 17' |  | 0.016 |
| 'ACC TOT HRS WRKD 79' |  | 0.016 |
| 'YEAR MOVED IN/OUT 93' |  | 0.016 |
| 'MARITAL PAIRS INDICATOR 15' |  | 0.015 |
| 'YEAR LAST ATTENDED COLLEGE 15' |  | 0.015 |
| 'IND A STUDENT? 80' |  | 0.015 |
| 'MONTH S/O FAM FORMED 85' |  | 0.015 |
| 'G84L IMPUTED HELP FROM RELS 13' |  | 0.015 |
| 'YEAR MOVED IN/OUT 77' |  | 0.015 |
| '1987 INTERVIEW NUMBER' |  | 0.015 |
| 'YEARS OF FOREIGN EDUCATION 15' |  | 0.015 |
| 'time_housework1_11' |  | 0.015 |
| 'HRS UNEMP LAST YR 76' |  | 0.015 |
| 'realactualhourlywage2_19' |  | 0.015 |
| 'actualhourlywage2_19' |  | 0.015 |
| 'YEAR LAST IN SCHOOL IF GED 15' |  | 0.015 |
| 'G88 MO LAST IN SCH-IND 90' |  | 0.015 |
| 'YEAR LAST IN SCHOOL IF GED 19' |  | 0.015 |
| 'ES4/ES12 WTR MOM LIVED IN US IN 1968 99' |  | 0.015 |
| 'ES6/ES14 WTR DAD LIVED IN US IN 1968 99' |  | 0.015 |
| 'ES5/ES13 MOM CITIZEN OUT OF US IN 68 99' |  | 0.015 |
| 'ES7/ES15 DAD CITIZEN OUT OF US IN 68 99' |  | 0.015 |
| 'id_family_current_11' |  | 0.015 |
| 'id_11' |  | 0.015 |
| 'time_work2_17' |  | 0.015 |
| 'month_13' |  | 0.015 |
| 'cost_recreation_17' |  | 0.015 |
| 'realcost_recreation_17' |  | 0.015 |
| 'F88 YR LAST IN SCH 85' |  | 0.014 |
| 'G84B IMPUTED TANF 07' |  | 0.014 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 9 95' |  | 0.014 |
| 'realcost_furnish_13' |  | 0.014 |
| 'cost_furnish_13' |  | 0.014 |
| 'R58A WTR STOPPED FOOD STAMPS IN 2001 03' |  | 0.014 |
| 'YEAR MOVED IN/OUT 82' |  | 0.014 |
| 'H61A WTR STATE INSURNCE PLAN FOR KIDS 09' |  | 0.014 |
| 'MONTH MOVED IN/OUT 78' |  | 0.014 |
| 'YEAR GRADUATED HIGHEST DEGREE 17' |  | 0.014 |
| 'UP: MONTH GRADUATED HIGH SCHOOL 17' |  | 0.014 |
| 'time_childcare1_17' |  | 0.014 |
| 'R4 WTR RECD TANF IN 1997 99' |  | 0.014 |
| 'R14 OFUM HRS PER WK WORKED 2005 07' |  | 0.014 |
| 'R15 WTR UNEMPLOYED JUL 2005 07' |  | 0.014 |
| 'H61E TYPE CURRENT HEALTH INS MEN 2 11' |  | 0.014 |
| 'HIGHEST YEAR COLLEGE COMPLETED 15' |  | 0.014 |
| 'R4 WTR RECD OTHER ASSISTANCE IN 2001 03' |  | 0.014 |
| 'TYPE OF IND RECORD 17' |  | 0.014 |
| 'R15 WTR UNEMPLOYED JUN 2005 07' |  | 0.014 |
| 'R15 WTR UNEMPLOYED MAY 2005 07' |  | 0.014 |
| 'R15 WTR UNEMPLOYED APR 2005 07' |  | 0.013 |
| 'R15 WTR UNEMPLOYED SEP 2005 07' |  | 0.013 |
| 'R15 WTR UNEMPLOYED FEB 2005 07' |  | 0.013 |
| 'R15 WTR UNEMPLOYED AUG 2005 07' |  | 0.013 |
| 'BACHELOR DEGREE MAJOR MEN2 2-DIGIT 19' |  | 0.013 |
| 'R15 WTR UNEMPLOYED OCT 2005 07' |  | 0.013 |
| 'cost_health_15' |  | 0.013 |
| 'realcost_health_15' |  | 0.013 |
| 'KL33A/ES1 COUNTY/COUNTRY WHERE BORN 99' |  | 0.013 |
| 'SN 1ST PERSON WHO HELPED WITH IW 19' |  | 0.013 |
| 'YEAR HIGHEST EDUCATION UPDATED 19' |  | 0.013 |
| 'R15 WTR UNEMPLOYED JAN 2005 07' |  | 0.013 |
| 'R15 WTR UNEMPLOYED MAR 2005 07' |  | 0.013 |
| 'MARITAL PAIRS INDICATOR 13' |  | 0.013 |
| 'R15 WTR UNEMPLOYED DEC 2005 07' |  | 0.013 |
| 'G84H IMPUTED UNEMP COMP 11' |  | 0.013 |
| 'YEAR S/O FAM FORMED 92' |  | 0.013 |
| 'wagerate2_13' |  | 0.013 |
| 'realwagerate2_13' |  | 0.013 |
| 'GDS2 WTR AFFECTED BY GOVT SHUTDOWN 19' |  | 0.013 |
| 'realcost_recreation_15' |  | 0.013 |
| 'cost_recreation_15' |  | 0.013 |
| 'R15 WTR UNEMPLOYED NOV 2005 07' |  | 0.013 |
| 'MONTH S/O FAM FORMED 86' |  | 0.013 |
| 'ACC ANN WRK HRS-IND 90' |  | 0.013 |
| 'WHETHER STUDENT 81' |  | 0.013 |
| 'G84C_G94C IMPUTED SSI 11' |  | 0.013 |
| 'G84K IMPUTED CHILD SUPPORT 05' |  | 0.013 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 11' |  | 0.013 |
| 'BACHELOR DEGREE MAJOR MEN2 15' |  | 0.013 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 17' |  | 0.013 |
| 'YEAR MOVED IN/OUT 19' |  | 0.013 |
| 'K4 STUDENT? 79' |  | 0.013 |
| 'G88 MO LAST IN SCH 86' |  | 0.013 |
| 'HIGHEST DEGREE MAJOR 13' |  | 0.013 |
| 'YEAR GRADUATED HIGHEST DEGREE 13' |  | 0.013 |
| 'WHY NONRESPONSE 17' |  | 0.013 |
| 'time_pcare2_17' |  | 0.012 |
| 'YEAR FATHER BORN' |  | 0.012 |
| 'H61A WTR STATE INSURNCE PLAN FOR KIDS 07' |  | 0.012 |
| 'MONTH MOVED IN/OUT 90' |  | 0.012 |
| 'H19 PROB LIGHT HOUSEWORK 92' |  | 0.012 |
| 'H17 PROB HEAVY HOUSEWORK 92' |  | 0.012 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 05' |  | 0.012 |
| 'time_shopping2_17' |  | 0.012 |
| 'H61E TYPE CURRENT HEALTH INS MEN 1 13' |  | 0.012 |
| 'H61F SN 2ND PERSON EMP PROVIDES INS 13' |  | 0.012 |
| 'R4 WTR RECD ADC IN 1999 01' |  | 0.012 |
| 'WEEKS IN SCHOOL(K51)? 80' |  | 0.012 |
| 'H61F SN 1ST PERSON EMP PROVIDES INS 15' |  | 0.012 |
| 'ES8 WTR IN US SINCE JAN 1, 1995 97' |  | 0.012 |
| 'G84M_G94F IMPUTED OTHER INCOME 07' |  | 0.012 |
| 'MONTH LAST IN SCHOOL IF GED 15' |  | 0.012 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 7 95' |  | 0.012 |
| 'time_work1_alt_15' |  | 0.012 |
| 'SN 1ST PERSON WHO HELPED WITH IW 15' |  | 0.012 |
| 'R45 WTR UNEMPLOYED IN AUG 2001 03' |  | 0.012 |
| 'YEAR S/O FAM FORMED 86' |  | 0.012 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 99' |  | 0.012 |
| 'R45 WTR UNEMPLOYED IN JUL 2001 03' |  | 0.012 |
| 'MONTH MOVED IN/OUT 84' |  | 0.012 |
| 'time_housework1_15' |  | 0.012 |
| 'HOURS UNEMP IN 1979 80' |  | 0.012 |
| 'G88 YR LAST IN SCH 87' |  | 0.012 |
| 'cost_education_19' |  | 0.012 |
| 'realcost_education_19' |  | 0.012 |
| 'MAIN FAM ID FOR S/O 07' |  | 0.012 |
| 'TOTAL # CHILDREN BORN TO FATHER' |  | 0.012 |
| 'cost_homeinsurance_17' |  | 0.012 |
| 'realcost_homeinsurance_17' |  | 0.012 |
| 'MAIN FAM ID FOR S/O 89' |  | 0.012 |
| 'time_housework2_13' |  | 0.012 |
| 'R45 WTR UNEMPLOYED IN JUN 2001 03' |  | 0.011 |
| 'realcost_trips_17' |  | 0.011 |
| 'cost_trips_17' |  | 0.011 |
| 'realactualhourlywage2_15' |  | 0.011 |
| 'actualhourlywage2_15' |  | 0.011 |
| 'H61M MONTHS UNINSURED IN 11 13' |  | 0.011 |
| 'R45 WTR UNEMPLOYED IN JAN 2001 03' |  | 0.011 |
| 'time_shopping2_19' |  | 0.011 |
| 'UP: YEAR LAST IN SCHOOL IF NEITHER 17' |  | 0.011 |
| 'R52 WTR RECEIVED OTHER WELFARE IN 05 07' |  | 0.011 |
| 'R45 WTR UNEMPLOYED IN FEB 2001 03' |  | 0.011 |
| 'R45 WTR UNEMPLOYED IN MAR 2001 03' |  | 0.011 |
| 'id_family_current_13' |  | 0.011 |
| 'id_13' |  | 0.011 |
| 'MONTH 4TH YOUNGEST CHILD BORN' |  | 0.011 |
| 'KL33G/ES8/ES16 WTR IN US SINCE 1/1/97 99' |  | 0.011 |
| 'YEAR MOST RECENT PREGNANCY INTENTION REC' |  | 0.011 |
| 'UP: YEARS OF FOREIGN EDUCATION 19' |  | 0.011 |
| 'realcost_furnish_15' |  | 0.011 |
| 'cost_furnish_15' |  | 0.011 |
| 'MONTH S/O FAM FORMED 82' |  | 0.011 |
| 'ACC ANN WRK HRS 92' |  | 0.011 |
| 'ACC TOT TRNSFR EXC SS 92' |  | 0.011 |
| 'time_work2_altalt_17' |  | 0.011 |
| 'time_totalhours2_17' |  | 0.011 |
| 'flag1119' |  | 0.011 |
| 'UP: HIGHEST DEGREE MAJOR MEN1 15' |  | 0.011 |
| 'ORDER OF BIRTH TO FATHER' |  | 0.011 |
| 'R45 WTR UNEMPLOYED IN APR 2001 03' |  | 0.011 |
| 'MONTH MOVED IN/OUT 77' |  | 0.011 |
| 'R45 TOTAL MOS UNEMPLOYED IN 2001 03' |  | 0.011 |
| 'YEAR S/O FAM FORMED 96' |  | 0.011 |
| 'UP: HIGHEST DEGREE MAJOR MEN1 17' |  | 0.011 |
| 'MAIN FAM ID FOR S/O 11' |  | 0.011 |
| 'R5 REPRTD PUB ASSISTNCE AMT-MLY 1999 01' |  | 0.011 |
| 'ACC ANN WRK HRS 86' |  | 0.011 |
| 'ACC TOT TRNSFR Y 81 82' |  | 0.01 |
| 'BACHELOR DEGREE MAJOR MEN2 17' |  | 0.01 |
| 'id_19' |  | 0.01 |
| '2019 INTERVIEW NUMBER' |  | 0.01 |
| 'id_family_current_19' |  | 0.01 |
| 'time_volunteering2_17' |  | 0.01 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 09' |  | 0.01 |
| 'nkids_15' |  | 0.01 |
| 'ACC G84A_G94B IMPUTED -INTEREST 09' |  | 0.01 |
| 'MONTH S/O FAM FORMED 92' |  | 0.01 |
| 'cost_homerepair_19' |  | 0.01 |
| 'realcost_homerepair_19' |  | 0.01 |
| 'R4 WTR RECD ADC IN 2001 03' |  | 0.01 |
| 'YEAR MOVED IN/OUT 73' |  | 0.01 |
| 'YEAR 4TH YOUNGEST CHILD BORN' |  | 0.01 |
| 'R45 WTR UNEMPLOYED IN DEC 2001 03' |  | 0.01 |
| 'RESULT OF TA IW ATTEMPT 13' |  | 0.01 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 11' |  | 0.01 |
| 'UP: WHETHER EDUCATED IN US 19' |  | 0.01 |
| 'R45 WTR UNEMPLOYED IN SEP 2001 03' |  | 0.01 |
| 'G88 MO LAST IN SCHOOL 94' |  | 0.01 |
| 'time_work1_alt_11' |  | 0.01 |
| 'SAMPLING ERROR CLUSTER' |  | 0.01 |
| 'YEAR GRADUATED HIGHEST DEGREE 15' |  | 0.01 |
| 'H61E TYPE CURRENT HEALTH INS MEN 1 15' |  | 0.01 |
| 'H61F SN 2ND PERSON EMP PROVIDES INS 19' |  | 0.01 |
| 'YEAR MOVED IN/OUT 15' |  | 0.01 |
| 'R45 WTR UNEMPLOYED IN MAY 2001 03' |  | 0.01 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 15' |  | 0.01 |
| 'R45 WTR UNEMPLOYED IN OCT 2001 03' |  | 0.01 |
| 'OFUM BUSINESS LABOR INCOME - IMPUTED 13' |  | 0.01 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 13' |  | 0.01 |
| 'age2_13' |  | 0.01 |
| 'cohort2_13' |  | 0.01 |
| 'MONTH GRADUATED HIGH SCHOOL 15' |  | 0.009 |
| 'ACC TOT LABOR INCOME 92' |  | 0.009 |
| 'G88 MO LAST IN SCH-IND 89' |  | 0.009 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 15' |  | 0.009 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 05' |  | 0.009 |
| 'TOT TRNSFR EXC SS-IND 90' |  | 0.009 |
| 'GRADE LEVEL IF GED 19' |  | 0.009 |
| 'R45 WTR UNEMPLOYED IN NOV 2001 03' |  | 0.009 |
| 'YEAR RECEIVED GED 19' |  | 0.009 |
| 'MONTH LAST ATTENDED COLLEGE 19' |  | 0.009 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 10 95' |  | 0.009 |
| 'MAIN FAM ID FOR S/O 84' |  | 0.009 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 09' |  | 0.009 |
| 'UP: FOREIGN DEGREE 19' |  | 0.009 |
| 'GRADE FINISHED 70' |  | 0.009 |
| 'TOT TRNSFR EXC SS-IND 89' |  | 0.009 |
| 'MONTH S/O FAM FORMED 99' |  | 0.009 |
| 'realcost_homerepair_17' |  | 0.009 |
| 'cost_homerepair_17' |  | 0.009 |
| 'MAIN FAM ID FOR S/O 87' |  | 0.009 |
| 'ACC TOT TRNSFR EXC SS 85' |  | 0.009 |
| 'MARITAL PAIRS INDICATOR 11' |  | 0.009 |
| 'MAIN FAM ID FOR S/O 92' |  | 0.009 |
| 'MONTH S/O FAM FORMED 01' |  | 0.009 |
| 'G84K IMPUTED CHILD SUPPORT 17' |  | 0.009 |
| 'H7 CKPT 92' |  | 0.009 |
| 'H9 PROB PREPARE MEALS 92' |  | 0.009 |
| 'H6G USE/GET TO TOILET 92' |  | 0.009 |
| 'H22 IN NURSING HOME 1991 92' |  | 0.009 |
| 'H6A BATHING 92' |  | 0.009 |
| 'H6F GET OUTSIDE 92' |  | 0.009 |
| 'H11 PROB SHOP PERS ITEM 92' |  | 0.009 |
| 'H21 HOME HLTH CARE 1991 92' |  | 0.009 |
| 'H6E WALKING 92' |  | 0.009 |
| 'H13 PROB MANAGE MONEY 92' |  | 0.009 |
| 'H6D GET OUT OF BED/CHAIR 92' |  | 0.009 |
| 'H15 PROB USE PHONE 92' |  | 0.009 |
| 'H6C EATING 92' |  | 0.009 |
| 'H6B DRESSING 92' |  | 0.009 |
| 'WHETHER EDUCATED IN US 17' |  | 0.009 |
| 'RESULT OF CDS 2014 IW ATTEMPT 13' |  | 0.009 |
| 'UP: YEAR GRADUATED HIGHEST DEGREE 17' |  | 0.009 |
| 'UP: BACHELOR DEG MAJOR MEN1 2-DIGIT 19' |  | 0.009 |
| 'YEAR LAST ATTENDED COLLEGE 19' |  | 0.009 |
| 'WHETHER MOVED IN/OUT 07' |  | 0.009 |
| 'MONTH MOVED IN/OUT 69' |  | 0.009 |
| 'YEAR S/O FAM FORMED 88' |  | 0.009 |
| 'G84B IMPUTED TANF 05' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN NOV 1997 99' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN OCT 1997 99' |  | 0.008 |
| 'YEAR S/O FAM FORMED 17' |  | 0.008 |
| 'UP: HIGHEST YEAR COLLEGE COMPLETED 19' |  | 0.008 |
| 'cost_recreation_19' |  | 0.008 |
| 'realcost_recreation_19' |  | 0.008 |
| 'R48A WTR STOPPED WELFARE IN 1997 99' |  | 0.008 |
| 'FOLLOW STATUS 09' |  | 0.008 |
| 'realactualhourlywage2_11' |  | 0.008 |
| 'actualhourlywage2_11' |  | 0.008 |
| 'MONTH RECEIVED GED 15' |  | 0.008 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 11' |  | 0.008 |
| 'GRADE CURRENTLY ENROLLED 19' |  | 0.008 |
| 'YEAR MOVED IN/OUT 05' |  | 0.008 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 11' |  | 0.008 |
| 'SEQUENCE NUMBER 84' |  | 0.008 |
| 'H61A WTR STATE INSURNCE PLAN FOR KIDS 11' |  | 0.008 |
| 'G84H IMPUTED UNEMP COMP 17' |  | 0.008 |
| 'MONTH MOVED IN/OUT 15' |  | 0.008 |
| 'UP: YEAR GRADUATED HIGH SCHOOL 17' |  | 0.008 |
| 'RESPONDENT? 15' |  | 0.008 |
| 'ACC TOT TRNSFR Y 82 83' |  | 0.008 |
| 'R6 TOTAL MOS RECD PUB ASSISTANCE 1997 99' |  | 0.008 |
| 'G34 ACC SOC SEC AMT 11' |  | 0.008 |
| 'MONTH LAST IN SCHOOL IF GED 19' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN AUG 1997 99' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN JUL 1997 99' |  | 0.008 |
| 'HIGHEST GRADE 74' |  | 0.008 |
| 'ACC TOT TXBL INCOME 87' |  | 0.008 |
| 'M31 YEAR LAST RELEASED 95' |  | 0.008 |
| '# YEARS WITH CONDITN 78' |  | 0.008 |
| 'YEAR LAST IN SCHOOL IF GED 17' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN DEC 1997 99' |  | 0.008 |
| 'R6 WTR RECD PUB ASSISTNCE IN MAR 1997 99' |  | 0.008 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 11' |  | 0.008 |
| 'UP: YEAR GRADUATED HIGH SCHOOL 19' |  | 0.007 |
| 'WHETHER STUDENT-IND 90' |  | 0.007 |
| 'MAIN FAM ID FOR S/O 81' |  | 0.007 |
| 'ACC TOT TXBL INC 79' |  | 0.007 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 13' |  | 0.007 |
| 'R6 WTR RECD PUB ASSISTNCE IN JUN 1997 99' |  | 0.007 |
| 'R6 WTR RECD PUB ASSISTNCE IN MAY 1997 99' |  | 0.007 |
| 'time_housework1_17' |  | 0.007 |
| 'MAIN FAM ID FOR S/O 86' |  | 0.007 |
| 'R6 WTR RECD PUB ASSISTNCE IN SEP 1997 99' |  | 0.007 |
| 'WHETHER STUDENT-IND 88' |  | 0.007 |
| 'MONTH S/O FAM FORMED 88' |  | 0.007 |
| 'MO S/O FAM FORMED 79' |  | 0.007 |
| 'R44 WTR RECD OTHER ASSISTANCE IN 2003 05' |  | 0.007 |
| 'month_17' |  | 0.007 |
| 'YEAR S/O FAM FORMED 82' |  | 0.007 |
| 'WHETHER STUDENT 84' |  | 0.007 |
| 'WHETHER MOVED IN/OUT 82' |  | 0.007 |
| 'H17 PROB HEAVY HOUSEWORK 93' |  | 0.007 |
| 'H15 PROB USE PHONE 93' |  | 0.007 |
| 'H21 HOME HLTH CARE 1992 93' |  | 0.007 |
| 'H13 PROB MANAGE MONEY 93' |  | 0.007 |
| 'H11 PROB SHOP PERS ITEM 93' |  | 0.007 |
| 'H9 PROB PREPARE MEALS 93' |  | 0.007 |
| 'H22 IN NURSING HOME 1992 93' |  | 0.007 |
| 'H19 PROB LIGHT HOUSEWORK 93' |  | 0.007 |
| 'H61N MONTHS UNINSURED IN 12 13' |  | 0.007 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 09' |  | 0.007 |
| 'WHETHER MOVED IN/OUT 17' |  | 0.007 |
| 'UP: GRADE SCHOOL FINISHED IF NEITHER 19' |  | 0.007 |
| 'R4 ASSET TYPE RENT 2003 05' |  | 0.007 |
| 'YEAR MOVED IN/OUT 78' |  | 0.007 |
| 'G88 YR LAST IN SCH-IND 89' |  | 0.007 |
| 'UP: MONTH LAST ATTENDED COLLEGE 17' |  | 0.007 |
| 'R6 WTR RECD PUB ASSISTNCE IN APR 1997 99' |  | 0.007 |
| 'UP: TYPE OF HIGHEST DEGREE 15' |  | 0.007 |
| 'YEAR S/O FAM FORMED 81' |  | 0.007 |
| 'HIGHEST DEGREE MAJOR MEN2 17' |  | 0.006 |
| 'G84C_G94C IMPUTED SSI 15' |  | 0.006 |
| '1980 INTERVIEW NUMBER' |  | 0.006 |
| 'ACC ANN WRK HRS 80 81' |  | 0.006 |
| 'UP: MONTH GRADUATED HIGH SCHOOL 19' |  | 0.006 |
| 'MONTH LAST IN SCHOOL 03' |  | 0.006 |
| 'RESPONDENT? 13' |  | 0.006 |
| 'UP: TYPE OF HIGHEST DEGREE 17' |  | 0.006 |
| 'ACC IND UNEMP HRS 76' |  | 0.006 |
| 'G84A_G94B IMPUTED INTEREST 17' |  | 0.006 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 17' |  | 0.006 |
| 'ACC G84C_G94C IMPUTED - SSI 09' |  | 0.006 |
| 'ACC G84A_G94B IMPUTED - INTEREST 17' |  | 0.006 |
| 'R2/R11 EARNINGS IN 2005 ACCURACY 07' |  | 0.006 |
| 'R14 OFUM HRS PER WK WORKED ACC 2005 07' |  | 0.006 |
| 'ACC G84K IMPUTED - CHILD SUPPORT 17' |  | 0.006 |
| 'G34 ACC SOC SEC AMT 09' |  | 0.006 |
| '1978 INTERVIEW NUMBER' |  | 0.006 |
| 'YEAR MOST RECENT MARRIAGE BEGAN' |  | 0.006 |
| 'GRADE LEVEL IF GED 17' |  | 0.006 |
| 'UP: YEARS OF FOREIGN EDUCATION 15' |  | 0.006 |
| 'RESULT OF TA IW ATTEMPT 15' |  | 0.006 |
| 'WTR HCB RECORD FOR SELF 93' |  | 0.006 |
| 'H6B DRESSING 93' |  | 0.006 |
| 'H6A BATHING 93' |  | 0.006 |
| 'H6D GET OUT OF BED/CHAIR 93' |  | 0.006 |
| 'H6E WALKING 93' |  | 0.006 |
| 'H6C EATING 93' |  | 0.006 |
| 'H7 CKPT 93' |  | 0.006 |
| 'H6G USE/GET TO TOILET 93' |  | 0.006 |
| 'H6F GET OUTSIDE 93' |  | 0.006 |
| 'time_adultcare1_17' |  | 0.006 |
| 'R6/R19 WTR ASSET INC APR 2003 05' |  | 0.006 |
| 'MONTH MOVED IN/OUT 11' |  | 0.006 |
| 'G88 MO LAST IN SCH 92' |  | 0.006 |
| 'MONTH MOVED IN/OUT 73' |  | 0.006 |
| 'wagerate2_11' |  | 0.006 |
| 'realwagerate2_11' |  | 0.006 |
| 'G88 YR LAST IN SCH 92' |  | 0.006 |
| 'R12 OFUM WKS WORKED 2005 07' |  | 0.006 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 07' |  | 0.006 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 01' |  | 0.006 |
| 'realcost_homerepair_15' |  | 0.006 |
| 'cost_homerepair_15' |  | 0.006 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 11' |  | 0.006 |
| '1992 INTERVIEW NUMBER' |  | 0.006 |
| 'WHETHER MOVED IN/OUT 84' |  | 0.006 |
| 'UP: WTR REC HS DIPLOMA/GED/NEITHER 19' |  | 0.006 |
| 'YEAR S/O FAM FORMED 95' |  | 0.006 |
| 'UP: MONTH GRADUATED BACHELOR DEGREE 15' |  | 0.006 |
| 'G88 YR LAST IN SCHOOL 94' |  | 0.006 |
| 'WHETHER MOVED IN/OUT 73' |  | 0.006 |
| 'realcost_home_13' |  | 0.006 |
| 'cost_home_13' |  | 0.006 |
| 'R30 WTR RECEIVED VA PENSION IN 2005 07' |  | 0.006 |
| 'ACC ANN WRK HRS 87' |  | 0.006 |
| 'R6/R19 WTR ASSET INC JUL 2003 05' |  | 0.006 |
| 'R48A WTR STOP PUB ASSTNCE SINCE 2001 03' |  | 0.005 |
| 'R6/R19 WTR ASSET INC MAY 2003 05' |  | 0.005 |
| 'ACC G84L IMPUTED - HELP FROM RELS 07' |  | 0.005 |
| 'H61G SN 2ND PERSON POLICY HOLDER 15' |  | 0.005 |
| 'K48 # WKS IN SCHOOL 79' |  | 0.005 |
| 'WHETHER STUDENT-IND 91' |  | 0.005 |
| 'WHETHER MOVED IN/OUT 83' |  | 0.005 |
| '# MARRIAGES OF THIS INDIVIDUAL' |  | 0.005 |
| 'time_education2_17' |  | 0.005 |
| 'UP: TYPE OF HIGHEST DEGREE 19' |  | 0.005 |
| 'YEAR LAST IN SCHOOL 03' |  | 0.005 |
| 'R3/R13 WTR EARNINGS JAN 2005 07' |  | 0.005 |
| 'R3/R13 WTR EARNINGS FEB 2005 07' |  | 0.005 |
| 'R3/R13 WTR EARNINGS MAR 2005 07' |  | 0.005 |
| 'R6/R19 WTR ASSET INC FEB 2003 05' |  | 0.005 |
| 'R6/R19 WTR ASSET INC AUG 2003 05' |  | 0.005 |
| 'WTR COVERED BY TANF PAYMENTS IN 2008 09' |  | 0.005 |
| 'UP: HIGHEST DEG MAJOR MEN1 2-DIGIT 19' |  | 0.005 |
| 'R4 WTR RECD GENERAL ASSISTANCE 1997 99' |  | 0.005 |
| 'R3/R13 WTR EARNINGS DEC 2005 07' |  | 0.005 |
| 'R3/R13 WTR EARNINGS AUG 2005 07' |  | 0.005 |
| 'TYPE TRANSFER Y-IND 90' |  | 0.005 |
| 'R3/R13 WTR EARNINGS NOV 2005 07' |  | 0.005 |
| 'MONTH S/O FAM FORMED 89' |  | 0.005 |
| 'G88 MO LAST IN SCH 87' |  | 0.005 |
| 'MONTH LAST IN SCHOOL IF GED 17' |  | 0.005 |
| 'WHETHER STUDENT 92' |  | 0.005 |
| 'MONTH MOST RECENT MARRIAGE BEGAN' |  | 0.005 |
| 'R6/R19 WTR ASSET INC JAN 2003 05' |  | 0.005 |
| 'R3/R13 WTR EARNINGS SEP 2005 07' |  | 0.005 |
| 'R3 STATE WHERE RECD PUB ASSTNCE 1997 99' |  | 0.005 |
| 'HIGHEST DEGREE MAJOR MEN1 17' |  | 0.004 |
| 'UP: HIGHEST YEAR COLLEGE COMPLETED 17' |  | 0.004 |
| 'HIGHEST GRADE OF SCHOOL COMPLETED 13' |  | 0.004 |
| 'R6/R19 WTR ASSET INC MAR 2003 05' |  | 0.004 |
| 'realcost_home_11' |  | 0.004 |
| 'cost_home_11' |  | 0.004 |
| 'H61M MONTHS UNINSURED IN 15 17' |  | 0.004 |
| 'R3/R13 WTR EARNINGS JUL 2005 07' |  | 0.004 |
| 'YEARS COMPLETED EDUCATION 99' |  | 0.004 |
| 'MAIN FAM ID FOR S/O 94' |  | 0.004 |
| 'R3/R13 WTR EARNINGS OCT 2005 07' |  | 0.004 |
| 'TOTAL ANNUAL EARNINGS IN 1999 01' |  | 0.004 |
| 'MONTH LAST ATTENDED COLLEGE 17' |  | 0.004 |
| 'R3/R13 WTR EARNINGS JUN 2005 07' |  | 0.004 |
| 'R6/R19 WTR ASSET INC JUN 2003 05' |  | 0.004 |
| 'MAIN FAM ID FOR S/O 03' |  | 0.004 |
| 'MAIN FAM ID FOR S/O 85' |  | 0.004 |
| 'ACC G84M_G94F IMPUTED - OTHER INCOME 05' |  | 0.004 |
| '# LIVE BIRTHS TO THIS INDIVIDUAL' |  | 0.004 |
| 'G84A_G94B IMPUTED INTEREST 09' |  | 0.004 |
| 'R6 WTR RECD PUB ASSISTNCE IN JAN 1997 99' |  | 0.004 |
| 'R6 WTR RECD PUB ASSISTNCE IN FEB 1997 99' |  | 0.004 |
| 'R6/R19 WTR ASSET INC OCT 2003 05' |  | 0.004 |
| 'time_totalhours1_11' |  | 0.004 |
| 'time_work1_altalt_11' |  | 0.004 |
| 'G88 YR LAST IN SCH-IND 91' |  | 0.004 |
| 'ACC TOT HRS WRKD 77 78' |  | 0.004 |
| 'G88 YR LAST IN SCH-IND 90' |  | 0.004 |
| 'MONTH S/O FAM FORMED 81' |  | 0.004 |
| 'WHETHER MOVED IN/OUT 01' |  | 0.004 |
| 'R26/R33/R41 REP EARNINGS AMT IN 1999 01' |  | 0.004 |
| 'R2 WTR RECEIVED TANF IN 2001 03' |  | 0.004 |
| 'SEQUENCE NUMBER 94' |  | 0.004 |
| '1981 INTERVIEW NUMBER' |  | 0.004 |
| 'R6/R19 WTR ASSET INC SEP 2003 05' |  | 0.004 |
| 'UP: MONTH GRADUATED HIGHEST DEGREE 19' |  | 0.004 |
| 'ACC TOT TXBL INCOME 86' |  | 0.004 |
| 'G76 NUMBER OF JOBS IN PY 05' |  | 0.004 |
| 'R3/R13 WTR EARNINGS MAY 2005 07' |  | 0.004 |
| 'G33 TYPE SOC SEC RCD 07' |  | 0.004 |
| 'WTR ELIGIBLE FOR DUST 2013 13' |  | 0.004 |
| 'R20 WTR RECEIVED OTHER HELP IN 1997 99' |  | 0.003 |
| 'MONTH S/O FAM FORMED 95' |  | 0.003 |
| 'WHETHER STUDENT 03' |  | 0.003 |
| 'MAIN FAM ID FOR S/O 19' |  | 0.003 |
| 'YEARS COMPLETED EDUCATION 05' |  | 0.003 |
| 'R2 WTR RECEIVED PUB ASSTNCE IN 1999 01' |  | 0.003 |
| 'ANN UNEMP HRS 80 81' |  | 0.003 |
| 'RESULT OF CDS/TA IW ATTEMPT 11' |  | 0.003 |
| 'MAIN FAM ID FOR S/O 13' |  | 0.003 |
| 'ACC HRS WORKED IN 74 75' |  | 0.003 |
| 'WHETHER MOVED IN/OUT 97' |  | 0.003 |
| 'YEAR MOVED IN/OUT 09' |  | 0.003 |
| 'H61G SN 1ST PERSON POLICY HOLDER 11' |  | 0.003 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 99' |  | 0.003 |
| '2011 INTERVIEW NUMBER' |  | 0.003 |
| 'UP: WTR RECEIVED COLLEGE DEGREE 17' |  | 0.003 |
| 'KL33A/ES1 STATE WHERE BORN 99' |  | 0.003 |
| 'MONTH S/O FAM FORMED 09' |  | 0.003 |
| 'R6/R19 WTR ASSET INC NOV 2003 05' |  | 0.003 |
| 'YEAR S/O FAM FORMED 99' |  | 0.003 |
| 'YEAR MOVED IN/OUT 89' |  | 0.003 |
| 'cost_homerepair_13' |  | 0.003 |
| 'realcost_homerepair_13' |  | 0.003 |
| 'ACC G84B IMPUTED - TANF 11' |  | 0.003 |
| 'UP: GRADE CURRENTLY ENROLLED 15' |  | 0.003 |
| '1971 INTERVIEW NUMBER' |  | 0.003 |
| 'FOLLOW STATUS 07' |  | 0.003 |
| 'R6 WTR RECD PUB ASSISTNCE IN AUG 1999 01' |  | 0.003 |
| 'SEQUENCE NUMBER 83' |  | 0.003 |
| 'WHETHER STUDENT 05' |  | 0.003 |
| 'UP: BACHELOR DEGREE MAJOR MEN2 17' |  | 0.003 |
| 'H61E TYPE CURRENT HEALTH INS MEN 3 13' |  | 0.003 |
| 'YEAR S/O FAM FORMED 89' |  | 0.003 |
| 'UP: MONTH LAST IN SCHOOL IF NEITHER 15' |  | 0.003 |
| 'R3/R13 WTR EARNINGS APR 2005 07' |  | 0.003 |
| 'EMPLOYMENT STAT 81' |  | 0.003 |
| 'RESULT OF CDS INTERVIEW 97' |  | 0.003 |
| 'G84C_G94C IMPUTED SSI 05' |  | 0.003 |
| 'YEAR S/O FAM FORMED 97' |  | 0.003 |
| 'RESULT OF CRCS IW ATTEMPT 14 13' |  | 0.003 |
| 'RESULT OF TA IW ATTEMPT 17' |  | 0.002 |
| 'ACC TOT ASSET INCOME 92' |  | 0.002 |
| 'R6/R19 WTR ASSET INC DEC 2003 05' |  | 0.002 |
| 'YEAR MOVED IN/OUT 81' |  | 0.002 |
| 'ACC TAXABLE Y 77' |  | 0.002 |
| 'ACC TAXABLE Y 75' |  | 0.002 |
| 'time_work1_alt_13' |  | 0.002 |
| 'F88 MO LAST IN SCH 85' |  | 0.002 |
| 'UP: YEAR LAST IN SCHOOL IF NEITHER 19' |  | 0.002 |
| 'G84M_G94F IMPUTED OTHER INCOME 09' |  | 0.002 |
| 'M5 FULL-TIME OR PART-TIME STUDENT 95' |  | 0.002 |
| 'SN 1ST PERSON WHO HELPED WITH IW 17' |  | 0.002 |
| 'MONTH S/O FAM FORMED 90' |  | 0.002 |
| 'G84K IMPUTED CHILD SUPPORT 07' |  | 0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN FEB 1999 01' |  | 0.002 |
| 'UP: YEAR LAST ATTENDED COLLEGE 17' |  | 0.002 |
| 'SN 2ND PERSON WHO HELPED WITH IW 13' |  | 0.002 |
| 'G84C_G94C IMPUTED SSI 07' |  | 0.002 |
| 'G76 NUMBER OF JOBS IN PY 09' |  | 0.002 |
| 'R4/R17 WTR REC ASSET INC 2003 05' |  | 0.002 |
| 'YEAR GRADUATED HIGH SCHOOL 15' |  | 0.002 |
| 'YEAR HIGHEST EDUCATION UPDATED 17' |  | 0.002 |
| 'MONTH 2ND YOUNGEST CHILD BORN' |  | 0.002 |
| 'SEQUENCE NUMBER 13' |  | 0.002 |
| 'R5 REPRTD PUB ASSISTNCE AMT-YRLY 1999 01' |  | 0.002 |
| 'MARITAL PAIRS INDICATOR 09' |  | 0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN JUL 1999 01' |  | 0.002 |
| 'MONTH S/O FAM FORMED 84' |  | 0.002 |
| 'YEAR RECEIVED GED 15' |  | 0.002 |
| 'MONTH INDIVIDUAL BORN 19' |  | 0.002 |
| 'realcost_clothing_15' |  | 0.002 |
| 'cost_clothing_15' |  | 0.002 |
| 'HIGHEST DEGREE MAJOR MEN1 15' |  | 0.002 |
| 'WHETHER MOVED IN/OUT 05' |  | 0.002 |
| 'H61F SN 1ST PERSON EMP PROVIDES INS 13' |  | 0.002 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 17' |  | 0.002 |
| 'WHETHER STUDENT 87' |  | 0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN SEP 1999 01' |  | 0.002 |
| 'MAIN FAM ID FOR S/O 05' |  | 0.001 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 03' |  | 0.001 |
| 'MAIN FAM ID FOR S/O 97' |  | 0.001 |
| 'cost_clothing_13' |  | 0.001 |
| 'realcost_clothing_13' |  | 0.001 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 11' |  | 0.001 |
| 'YEAR S/O FAM FORMED 09' |  | 0.001 |
| 'actualhourlywage2_17' |  | 0.001 |
| 'realactualhourlywage2_17' |  | 0.001 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 15' |  | 0.001 |
| 'R6 WTR RECD PUB ASSISTNCE IN NOV 1999 01' |  | 0.001 |
| 'ANNUALIZED PUBLIC ASSISTANCE AMT 1999 01' |  | 0.001 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 12 95' |  | 0.001 |
| 'WHETHER MOVED IN/OUT 80' |  | 0.001 |
| 'G84C_G94C IMPUTED SSI 17' |  | 0.001 |
| 'M14A EVER ATTEND PRIVATE SCHOOL K-12 95' |  | 0.001 |
| '2007 INTERVIEW NUMBER' |  | 0.001 |
| 'MONTH MOVED IN/OUT 89' |  | 0.001 |
| 'STATUS OF MOST RECENT MARRIAGE' |  | 0.001 |
| 'TOTAL TRNSFR Y-IND 90' |  | 0.001 |
| 'TYPE OF HIGHEST DEGREE 13' |  | 0.001 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 5 95' |  | 0.001 |
| '1999 INTERVIEW NUMBER' |  | 0.001 |
| 'WTR EVER CODED INSTITUTIONAL' |  | 0.001 |
| 'R43 WTR RECD EARNINGS IN NOV 2001 03' |  | 0.001 |
| 'SN 2ND PERSON WHO HELPED WITH IW 15' |  | 0.001 |
| 'MONTH LAST IN SCHOOL 95' |  | 0.001 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 11 95' |  | 0.001 |
| 'MONTH S/O FAM FORMED 13' |  | 0.001 |
| 'MONTH GRADUATED HIGH SCHOOL 17' |  | 0.001 |
| 'ACC G84C_G94C IMPUTED -SSI 11' |  | 0.001 |
| 'R43 WTR RECD EARNINGS IN DEC 2001 03' |  | 0.001 |
| 'R3 STATE WHERE RECD PUB ASSTNCE 1999 01' |  | 0.001 |
| 'R6 WTR RECD PUB ASSISTNCE IN OCT 1999 01' |  | 0.001 |
| 'YEAR HIGHEST EDUCATION UPDATED 15' |  | 0.001 |
| 'SEQUENCE NUMBER 93' |  | 0.001 |
| 'MONTH MOVED IN/OUT 96' |  | 0.001 |
| 'cost_clothing_11' |  | 0.001 |
| 'realcost_clothing_11' |  | 0.001 |
| 'G84K IMPUTED CHILD SUPPORT 11' |  | 0.001 |
| 'TOTAL TRNSFR Y-IND 89' |  | 0.001 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 05' |  | 0.001 |
| 'ACCURACY OF PUBLIC ASSISTANCE IN 1999 01' |  | 0.001 |
| 'M23 HOW OLD 1ST ATTEND HEAD START 95' |  | 0.001 |
| 'YEAR 3RD YOUNGEST CHILD BORN' |  | 0.0 |
| 'ACC ANN WRK HRS 81 82' |  | 0.0 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 07' |  | 0.0 |
| 'MONTH 3RD YOUNGEST CHILD BORN' |  | 0.0 |
| 'HIGHEST DEGREE MAJOR MEN2 15' |  | 0.0 |
| 'YEAR MOVED IN/OUT 99' |  | 0.0 |
| 'ACC TAXABLE Y 76' |  | 0.0 |
| 'id_15' |  | 0.0 |
| 'id_family_current_15' |  | 0.0 |
| 'YEAR S/O FAM FORMED 84' |  | 0.0 |
| 'WHETHER EDUCATED IN US 15' |  | 0.0 |
| 'time_childcare1_19' |  | 0.0 |
| 'YEAR S/O FAM FORMED 83' |  | 0.0 |
| 'WHETHER STUDENT 86' |  | 0.0 |
| 'time_totalhours1_13' |  | 0.0 |
| 'time_work1_altalt_13' |  | 0.0 |
| 'id_family_current_17' |  | 0.0 |
| 'id_17' |  | 0.0 |
| 'CALCULATED HOURLY WAGE RATE IN 1999 01' |  | 0.0 |
| 'YEAR S/O FAM FORMED 13' |  | 0.0 |
| 'M11A RECEIVED GED 95' |  | 0.0 |
| 'SEQUENCE NUMBER 97' |  | 0.0 |
| 'realtotallaborincome2_17' |  | 0.0 |
| 'totallaborincome2_17' |  | 0.0 |
| 'YEARS COMPLETED EDUCATION 03' |  | 0.0 |
| 'YEAR MOVED IN/OUT 11' |  | -0.0 |
| 'R6 WTR RECD PUB ASSISTNCE IN DEC 1999 01' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN OCT 2001 03' |  | -0.0 |
| 'KL33E/ES2/ES10 WTR LIVED IN US IN 68 99' |  | -0.0 |
| 'YEAR MOVED IN/OUT 84' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN FEB 2001 03' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN MAY 2001 03' |  | -0.0 |
| 'SEQUENCE NUMBER 07' |  | -0.0 |
| 'R6 TOTAL MOS RECD PUB ASSISTANCE 1999 01' |  | -0.0 |
| 'UP: MONTH LAST IN SCHOOL IF NEITHER 19' |  | -0.0 |
| 'ACC ANN WRK HRS-IND 91' |  | -0.0 |
| 'R5/R18 ASSET INC PER 2003 05' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN APR 2001 03' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN SEP 2001 03' |  | -0.0 |
| 'GRADE FINISHED 72' |  | -0.0 |
| 'R12 WTR RECEIVED CHILD SUPPORT IN 99 01' |  | -0.0 |
| 'M29 TIMES SENT TO YOUTH CORRECT INST 95' |  | -0.0 |
| 'M28 SPENT TIME IN CORRECTIONS INST 95' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN MAR 2001 03' |  | -0.0 |
| 'F34 ACC SOC SEC AMT 84' |  | -0.0 |
| 'ACC G84B IMPUTED - TANF 07' |  | -0.0 |
| 'ACC G84F IMPUTED - VETERANS BEN 13' |  | -0.0 |
| 'MONTH LAST IN SCHOOL 96' |  | -0.0 |
| 'H6D GET OUT OF BED/CHAIR 94' |  | -0.0 |
| 'H7 CKPT 94' |  | -0.0 |
| 'R43 WTR RECD EARNINGS IN JAN 2001 03' |  | -0.0 |
| 'GRADE CURRENTLY ENROLLED 15' |  | -0.0 |
| 'MO S/O FAM FORMED 76' |  | -0.001 |
| 'MONTH MOVED IN/OUT 01' |  | -0.001 |
| 'ACC TOT HRS UNEMP 79' |  | -0.001 |
| 'M19 WHICH GRADE REPEATED 3 95' |  | -0.001 |
| 'month_15' |  | -0.001 |
| 'YEARS COMPLETED EDUCATION 13' |  | -0.001 |
| 'MONTH S/O FAM FORMED 97' |  | -0.001 |
| 'YEAR LAST ATTENDED COLLEGE 17' |  | -0.001 |
| 'MARITAL PAIRS INDICATOR 07' |  | -0.001 |
| 'MAIN FAM ID FOR S/O 95' |  | -0.001 |
| 'R43 TOTAL MOS RECD EARNINGS IN 2001 03' |  | -0.001 |
| 'YEAR S/O FAM FORMED 90' |  | -0.001 |
| 'G88 YR LAST IN SCH-IND 88' |  | -0.001 |
| 'UP: YEAR GRADUATED HIGHEST DEGREE 19' |  | -0.001 |
| 'nkids_13' |  | -0.001 |
| 'WHETHER MOVED IN/OUT 75' |  | -0.001 |
| 'WHETHER MOVED IN/OUT 11' |  | -0.001 |
| 'wageandsal2_17' |  | -0.001 |
| 'realwageandsal2_17' |  | -0.001 |
| 'SEQUENCE NUMBER 17' |  | -0.001 |
| 'CONDITN BETTER OR 78' |  | -0.001 |
| 'EMPLOYMENT STATUS 83' |  | -0.001 |
| 'R26/R33/R41 REP EARNINGS ANT IN 1997 99' |  | -0.001 |
| 'UP: WTR ATTENDED COLLEGE 17' |  | -0.001 |
| 'G88 YR LAST IN SCHOOL 93' |  | -0.001 |
| 'YR S/O FAM FORMED 79' |  | -0.001 |
| 'TYPE TRANSFER INCOME 93' |  | -0.001 |
| 'WTR ELIGIBLE FOR TA 13' |  | -0.001 |
| 'SN 1ST PERSON WHO HELPED WITH IW 11' |  | -0.001 |
| 'H61E TYPE CURRENT HEALTH INS MEN 2 13' |  | -0.001 |
| 'MONTH MOVED IN/OUT 80' |  | -0.001 |
| 'UP: YEAR LAST IN SCHOOL IF GED 15' |  | -0.001 |
| 'G84F IMPUTED VETERANS BEN 13' |  | -0.001 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 07' |  | -0.001 |
| '2013 INTERVIEW NUMBER' |  | -0.001 |
| 'YEAR MOVED IN/OUT 90' |  | -0.001 |
| 'YR S/O FAM FORMED 76' |  | -0.001 |
| 'WHETHER STUDENT 96' |  | -0.001 |
| 'YEARS COMPLETED EDUCATION 07' |  | -0.001 |
| 'M19 WHICH GRADE REPEATED 1 95' |  | -0.001 |
| 'WHETHER STUDENT 94' |  | -0.001 |
| 'SEQUENCE NUMBER 81' |  | -0.001 |
| 'SEQUENCE NUMBER 75' |  | -0.001 |
| 'age1_13' |  | -0.001 |
| 'cohort1_13' |  | -0.001 |
| 'R4 WTR RECD TANF IN 1999 01' |  | -0.001 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 05' |  | -0.001 |
| 'YEARS COMPLETED EDUCATION 01' |  | -0.001 |
| 'WTR COVERED BY TANF PAYMENTS IN 2006 07' |  | -0.001 |
| 'ETHNICITY OF LNPS SAMPLING AREA' |  | -0.002 |
| 'G84D_G94D IMPUTED WELFARE 13' |  | -0.002 |
| 'R4 ASSET TYPE INTEREST 2003 05' |  | -0.002 |
| 'H61G SN 2ND PERSON POLICY HOLDER 13' |  | -0.002 |
| 'ATTRITOR PROJECT SOURCE 07' |  | -0.002 |
| 'realcost_health_13' |  | -0.002 |
| 'cost_health_13' |  | -0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN JAN 1999 01' |  | -0.002 |
| 'MONTH MOVED IN/OUT 81' |  | -0.002 |
| 'cost_homeinsurance_13' |  | -0.002 |
| 'realcost_homeinsurance_13' |  | -0.002 |
| 'M6A GRADUATE, GED, OR NEITHER 95' |  | -0.002 |
| 'YEAR S/O FAM FORMED 87' |  | -0.002 |
| 'WTR ELIG FOR CRCS 2014 13' |  | -0.002 |
| 'G84M_G94F IMPUTED OTHER INCOME 11' |  | -0.002 |
| 'G84L IMPUTED HELP FROM RELS 15' |  | -0.002 |
| 'TRANSFER Y SOURCE 77' |  | -0.002 |
| 'GRADE LEVEL IF GED 15' |  | -0.002 |
| 'ACC G84A_G94B IMPUTED - INTEREST 05' |  | -0.002 |
| 'YEAR 2ND YOUNGEST CHILD BORN' |  | -0.002 |
| 'YEAR MOVED IN/OUT 01' |  | -0.002 |
| 'YEAR MOVED IN/OUT 69' |  | -0.002 |
| 'G84M_G94F IMPUTED OTHER INCOME 13' |  | -0.002 |
| 'TOTAL ANNUAL EARNINGS IN 1997 99' |  | -0.002 |
| 'YEAR RECEIVED GED 17' |  | -0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN MAR 1999 01' |  | -0.002 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 05' |  | -0.002 |
| 'YEARS COMPLETED EDUCATION 11' |  | -0.002 |
| 'WHETHER STUDENT 85' |  | -0.002 |
| 'R43 WTR RECD EARNINGS IN AUG 2001 03' |  | -0.002 |
| 'ACC ANN WRK HRS-IND 88' |  | -0.002 |
| 'MONTH MOVED IN/OUT 87' |  | -0.002 |
| 'EMPLOYMENT STATUS 82' |  | -0.002 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 05' |  | -0.002 |
| 'SEQUENCE NUMBER 05' |  | -0.002 |
| 'UP: YEAR RECEIVED GED 15' |  | -0.002 |
| 'KL33F/ES3/ES11 CITZN OUT OF US IN 68 99' |  | -0.002 |
| 'cost_furnish_19' |  | -0.002 |
| 'realcost_furnish_19' |  | -0.002 |
| 'R6 WTR RECD PUB ASSISTNCE IN JUN 1999 01' |  | -0.002 |
| 'ACC TOT TXBL Y-IND 88' |  | -0.002 |
| 'G84L IMPUTED HELP FROM RELS 09' |  | -0.002 |
| 'UP: YEAR GRADUATED BACHELOR DEGREE 17' |  | -0.002 |
| 'H61G SN 2ND PERSON POLICY HOLDER 17' |  | -0.002 |
| 'TYPE TRANSFER Y 85' |  | -0.002 |
| 'YEAR LAST IN SCHOOL 09' |  | -0.002 |
| 'H61G SN 1ST PERSON POLICY HOLDER 13' |  | -0.002 |
| 'MONTH MOVED IN/OUT 70' |  | -0.002 |
| 'MOVED IN/OUT 92' |  | -0.002 |
| 'UP: MONTH RECEIVED GED 19' |  | -0.002 |
| 'realcost_recreation_13' |  | -0.002 |
| 'cost_recreation_13' |  | -0.002 |
| 'ACC G84M_G94F IMPUTED - OTHER INCOME 09' |  | -0.002 |
| 'MAIN FAM ID FOR S/O 72' |  | -0.002 |
| 'R12 WTR RECEIVED CHILD SUPPORT IN 01 03' |  | -0.003 |
| 'WHETHER STUDENT-IND 89' |  | -0.003 |
| 'UP: BACHELOR DEGREE MAJOR MEN1 15' |  | -0.003 |
| 'TOT TRANSFR EXC SS 85' |  | -0.003 |
| 'cost_homerepair_11' |  | -0.003 |
| 'realcost_homerepair_11' |  | -0.003 |
| 'R34 WTR RECEIVED UNEMP COMP IN 2003 05' |  | -0.003 |
| 'UP: YEAR LAST IN SCHOOL IF GED 19' |  | -0.003 |
| 'UP: GRADE LEVEL IF GED 19' |  | -0.003 |
| 'UP: YEAR RECEIVED GED 19' |  | -0.003 |
| 'R43 WTR RECD EARNINGS IN JUN 2001 03' |  | -0.003 |
| 'YEAR MOVED IN/OUT 96' |  | -0.003 |
| 'RESPONDENT? 07' |  | -0.003 |
| 'MEDICARE PERMISSION 90' |  | -0.003 |
| 'G84M_G94F IMPUTED OTHER INCOME 05' |  | -0.003 |
| 'ARE COSTS SMALL OR 78' |  | -0.003 |
| 'ACC TOT TRANS INC 79' |  | -0.003 |
| 'YEARS COMPLETED EDUCATION 09' |  | -0.003 |
| 'R44 WTR RECD OTHER ASSISTANCE IN 2005 07' |  | -0.003 |
| 'R44 WTR RECD GEN ASSISTANCE IN 2005 07' |  | -0.003 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 3 95' |  | -0.003 |
| 'R4 WTR RECD EMERG ASSISTANCE IN 2001 03' |  | -0.003 |
| 'R43 WTR RECD EARNINGS IN JUL 2001 03' |  | -0.003 |
| 'MAIN FAM ID FOR S/O 83' |  | -0.003 |
| 'EMPLOYMENT STATUS 05' |  | -0.003 |
| 'TYPE TRANSFER Y-IND 89' |  | -0.003 |
| 'MONTH MOVED IN/OUT 82' |  | -0.003 |
| 'RESPONDENT? 11' |  | -0.003 |
| 'R6 WTR RECD PUB ASSISTNCE IN MAY 1999 01' |  | -0.003 |
| 'MONTH LAST IN SCHOOL 05' |  | -0.003 |
| 'G84D_G94D IMPUTED WELFARE 05' |  | -0.003 |
| 'UP: MONTH LAST IN SCHOOL IF GED 15' |  | -0.003 |
| 'M30 TIMES SENT TO ADULT CORRECT INST 95' |  | -0.003 |
| '1979 INTERVIEW NUMBER' |  | -0.003 |
| 'realcost_recreation_11' |  | -0.003 |
| 'cost_recreation_11' |  | -0.003 |
| 'H61C MOS COVERED BY INSURANCE IN 10 11' |  | -0.003 |
| 'G84H IMPUTED UNEMP COMP 13' |  | -0.003 |
| 'YEAR S/O FAM FORMED 07' |  | -0.003 |
| 'YEAR LAST IN SCHOOL 05' |  | -0.003 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 13' |  | -0.003 |
| 'SN 2ND PERSON WHO HELPED WITH IW 11' |  | -0.003 |
| '2017 INTERVIEW NUMBER' |  | -0.003 |
| 'YEAR MOVED IN/OUT 85' |  | -0.003 |
| 'WTR CURRENTLY ENROLLED IN SCHOOL 19' |  | -0.003 |
| 'YEAR MOVED IN/OUT 76' |  | -0.003 |
| 'YEAR LAST IN SCHOOL 11' |  | -0.004 |
| 'time_volunteering2_19' |  | -0.004 |
| 'SEQUENCE NUMBER 03' |  | -0.004 |
| 'H6F GET OUTSIDE 94' |  | -0.004 |
| 'H11 PROB SHOP PERS ITEM 94' |  | -0.004 |
| 'H6G USE/GET TO TOILET 94' |  | -0.004 |
| 'H6E WALKING 94' |  | -0.004 |
| 'H6C EATING 94' |  | -0.004 |
| 'H9 PROB PREPARE MEALS 94' |  | -0.004 |
| 'H6B DRESSING 94' |  | -0.004 |
| 'H13 PROB MANAGE MONEY 94' |  | -0.004 |
| 'H6A BATHING 94' |  | -0.004 |
| 'H15 PROB USE PHONE 94' |  | -0.004 |
| '1989 INTERVIEW NUMBER' |  | -0.004 |
| 'EMPLOYMENT STAT-IND 90' |  | -0.004 |
| 'ACC TOT TRNSFR Y 80 81' |  | -0.004 |
| 'OFUM BUSINESS LABOR INCOME - IMPUTED 15' |  | -0.004 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 15' |  | -0.004 |
| 'G76 NUMBER OF JOBS IN PY 15' |  | -0.004 |
| 'MOVED IN/OUT 90' |  | -0.004 |
| 'time_adultcare2_19' |  | -0.004 |
| 'HOW MUCH LIMIT? 78' |  | -0.004 |
| 'MONTH S/O FAM FORMED 83' |  | -0.004 |
| 'G84A_G94B IMPUTED INTEREST 13' |  | -0.004 |
| 'G88 MO LAST IN SCH-IND 88' |  | -0.004 |
| 'nkids_11' |  | -0.004 |
| 'G84D_G94D IMPUTED WELFARE 15' |  | -0.004 |
| 'ACC G84A_G94B IMPUTED -INTEREST 11' |  | -0.004 |
| 'R2/R11 EARNINGS ACCURACY 2003 05' |  | -0.004 |
| 'G84F IMPUTED VETERANS BEN 05' |  | -0.004 |
| 'G34 ACC SOC SEC AMT 86' |  | -0.004 |
| 'R44 WTR RECD INDIAN ASSIST IN 2005 07' |  | -0.004 |
| 'R44 WTR RECD CUBAN/HAITIAN REF 2005 07' |  | -0.004 |
| 'ACC TOT TRNSFR EXC SS 87' |  | -0.004 |
| 'UP: FOREIGN DEGREE 17' |  | -0.004 |
| 'R4 WTR RECD EMERGENCY ASSISTANCE 1997 99' |  | -0.004 |
| 'ACC G84C_G94C IMPUTED - SSI 15' |  | -0.004 |
| 'ACC G84F IMPUTED - VETERANS BEN 17' |  | -0.004 |
| 'G84F IMPUTED VETERANS BEN 17' |  | -0.004 |
| 'G84A_G94B IMPUTED INTEREST 05' |  | -0.004 |
| 'PERSON # OF MOTHER' |  | -0.004 |
| 'WHETHER STUDENT 07' |  | -0.004 |
| 'UP: WTR REC HS DIPLOMA/GED/NEITHER 17' |  | -0.004 |
| 'YEAR LAST IN SCHOOL 96' |  | -0.004 |
| 'GRADE OF SCHOOL FINISHED IF NEITHER 15' |  | -0.004 |
| 'MAIN FAM ID FOR S/O 79' |  | -0.004 |
| 'UP: YEAR LAST ATTENDED COLLEGE 15' |  | -0.004 |
| 'YEARS COMPLETED EDUCATION 17' |  | -0.004 |
| 'UP: BACHELOR DEGREE MAJOR MEN1 17' |  | -0.004 |
| 'YEAR MOVED IN/OUT 91' |  | -0.004 |
| 'YEAR GRADUATED HIGH SCHOOL 17' |  | -0.004 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 07' |  | -0.004 |
| 'MONTH MOVED IN/OUT 91' |  | -0.004 |
| 'R5 REPRTD PUB ASSISTNCE AMT-MLY 1997 99' |  | -0.004 |
| 'G34 ACC SOC SEC AMT 19' |  | -0.004 |
| 'MAIN FAM ID FOR S/O 80' |  | -0.004 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 2 95' |  | -0.004 |
| 'MAIN FAM ID FOR S/O 17' |  | -0.004 |
| 'MONTH GRADUATED HIGHEST DEGREE 17' |  | -0.004 |
| 'H17 PROB HEAVY HOUSEWORK 94' |  | -0.004 |
| 'WHETHER STUDENT 83' |  | -0.004 |
| 'R30/R37/R45 WTR UNEMPLOYED MAY 1997 99' |  | -0.004 |
| 'UP: HIGHEST DEGREE MAJOR MEN2 15' |  | -0.004 |
| 'UP: GRADE SCHOOL FINISHED IF NEITHER 17' |  | -0.004 |
| 'H61D3 WTR COVERED BY INSURANCE NOW 13' |  | -0.004 |
| 'M16 NON-RELIG, CATHOLIC, ANOTHER REL 95' |  | -0.004 |
| 'cohort1_15' |  | -0.004 |
| 'age1_15' |  | -0.004 |
| 'MONTH MOVED IN/OUT 13' |  | -0.004 |
| 'TYPE TRANSFR INCOM 78' |  | -0.004 |
| 'YEAR MOVED IN/OUT 70' |  | -0.004 |
| 'MONTH MOVED IN/OUT 85' |  | -0.005 |
| 'SEQUENCE NUMBER 82' |  | -0.005 |
| 'YEAR FIRST BECAME NONRESPONSE' |  | -0.005 |
| 'MONTH GRADUATED HIGHEST DEGREE 19' |  | -0.005 |
| 'R6 WTR RECD PUB ASSISTNCE IN APR 1999 01' |  | -0.005 |
| 'FOLLOW STATUS 05' |  | -0.005 |
| 'YEAR OF MOST RECENT NONRESPONSE' |  | -0.005 |
| 'WHETHER MOVED IN/OUT 86' |  | -0.005 |
| 'MOVED IN/OUT 89' |  | -0.005 |
| '1972 INTERVIEW NUMBER' |  | -0.005 |
| 'R44 WTR RECD ADC IN 2005 07' |  | -0.005 |
| 'TOT HRS UNEMPLYD 77 78' |  | -0.005 |
| 'R30 WTR RECEIVED VA PENSION IN 2003 05' |  | -0.005 |
| 'R42 WTR RECEIVED TANF/GA IN 2003 05' |  | -0.005 |
| 'G84A_G94B IMPUTED INTEREST 07' |  | -0.005 |
| 'WHETHER MOVED IN/OUT 03' |  | -0.005 |
| 'WHETHER MOVED IN/OUT 95' |  | -0.005 |
| '1969 INTERVIEW NUMBER' |  | -0.005 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 01' |  | -0.005 |
| 'HEALTH GOOD? 13' |  | -0.005 |
| 'MAIN FAM ID FOR S/O 99' |  | -0.005 |
| 'UP: MONTH LAST ATTENDED COLLEGE 15' |  | -0.005 |
| 'H19 PROB LIGHT HOUSEWORK 94' |  | -0.005 |
| 'UP: GRADE LEVEL IF GED 15' |  | -0.005 |
| 'head2013' |  | -0.005 |
| 'head2011' |  | -0.005 |
| 'WHETHER MOVED IN/OUT 99' |  | -0.005 |
| 'MONTH GRADUATED BACHELOR DEGREE 13' |  | -0.005 |
| 'MOVED IN/OUT 94' |  | -0.005 |
| 'R44 WTR RECD EMERG ASSISTANCE IN 2005 07' |  | -0.005 |
| 'G88 MO LAST IN SCHOOL 93' |  | -0.005 |
| 'HEALTH GOOD? 09' |  | -0.005 |
| 'ACC G84M_G94F IMPUTED - OTHER INCOME 07' |  | -0.005 |
| 'H18 B/C OF HEALTH? 95' |  | -0.005 |
| 'YEAR S/O FAM FORMED 05' |  | -0.005 |
| 'MONTH MOVED IN/OUT 83' |  | -0.005 |
| 'G84B IMPUTED TANF 13' |  | -0.005 |
| 'R30/R37/R45 WTR UNEMPLOYED NOV 1999 01' |  | -0.005 |
| 'BACHELOR DEGREE MAJOR 13' |  | -0.005 |
| 'MONTH MOVED IN/OUT 71' |  | -0.005 |
| 'G84M_G94F IMPUTED OTHER INCOME 15' |  | -0.005 |
| 'R2/R11 EARNINGS AMT REPORTED IN 2005 07' |  | -0.005 |
| 'R30/R37/R45 WTR UNEMPLOYED APR 1997 99' |  | -0.006 |
| 'H13 OFUM HEALTH GOOD 90' |  | -0.006 |
| 'R4 WTR RECD TANF IN 2001 03' |  | -0.006 |
| 'R44 WTR RECD ADC IN 2003 05' |  | -0.006 |
| 'time_totalhours2_11' |  | -0.006 |
| 'time_work2_altalt_11' |  | -0.006 |
| 'MO S/O FAM FORMED 73' |  | -0.006 |
| 'R30/R37/R45 WTR UNEMPLOYED JUN 1997 99' |  | -0.006 |
| 'SEQUENCE NUMBER 73' |  | -0.006 |
| 'realtotallaborincome2_11' |  | -0.006 |
| 'totallaborincome2_11' |  | -0.006 |
| 'SN 3RD PERSON WHO HELPED WITH IW 19' |  | -0.006 |
| 'WHETHER STUDENT 09' |  | -0.006 |
| '1988 INTERVIEW NUMBER' |  | -0.006 |
| 'YEARS COMPLETED EDUCATION 15' |  | -0.006 |
| 'G84C_G94C IMPUTED SSI 09' |  | -0.006 |
| 'SN 1ST PERSON WHO HELPED WITH IW 09' |  | -0.006 |
| 'R42 WEEKS WORKED IN 2001 03' |  | -0.006 |
| 'UP: WHETHER EDUCATED IN US 15' |  | -0.006 |
| 'R30/R37/R45 WTR UNEMPLOYED MAR 1997 99' |  | -0.006 |
| 'M24 TOTAL MONTHS ATTENDED HEAD START 95' |  | -0.006 |
| 'UP: MONTH GRADUATED BACHELOR DEGREE 17' |  | -0.006 |
| 'MONTH MOVED IN/OUT 75' |  | -0.006 |
| 'MAIN FAM ID FOR S/O 76' |  | -0.006 |
| 'MONTH MOVED IN/OUT 05' |  | -0.006 |
| 'R3 STATE WHERE RECD PUB ASSTNCE 2001 03' |  | -0.006 |
| 'R30/R37/R45 WTR UNEMPLOYED JAN 1997 99' |  | -0.006 |
| 'OFUM TOTAL LABOR INCOME- IMPUTED 13' |  | -0.006 |
| 'HEALTH GOOD? 11' |  | -0.006 |
| 'R5 REPRTD PUB ASSISTNCE AMT-YRLY 1997 99' |  | -0.006 |
| 'RESPONDENT? 79' |  | -0.006 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 17' |  | -0.006 |
| 'RESPONDENT? 09' |  | -0.006 |
| 'MONTH LAST IN SCHOOL 99' |  | -0.006 |
| '1984 INTERVIEW NUMBER' |  | -0.006 |
| 'SEQUENCE NUMBER 95' |  | -0.006 |
| 'R12 OFUM WKS WORKED 2003 05' |  | -0.006 |
| 'YEAR MOVED IN/OUT 86' |  | -0.006 |
| 'R30/R37/R45 WTR UNEMPLOYED FEB 1997 99' |  | -0.006 |
| '1968 ID OF FATHER' |  | -0.006 |
| 'H61N MONTHS UNINSURED IN 16 17' |  | -0.006 |
| 'G84A_G94B IMPUTED INTEREST 11' |  | -0.006 |
| 'time_adultcare2_17' |  | -0.006 |
| 'YEAR MOVED IN/OUT 71' |  | -0.006 |
| 'UP: WHETHER EDUCATED IN US 17' |  | -0.006 |
| 'OFUM TOTAL TAXABLE INCOME - IMPUTED 13' |  | -0.006 |
| '2009 INTERVIEW NUMBER' |  | -0.006 |
| 'MAIN FAM ID FOR S/O 78' |  | -0.006 |
| 'YEAR GRADUATED BACHELOR DEGREE 13' |  | -0.007 |
| 'sex1_11' |  | -0.007 |
| 'R28/R35/R43 WTR RECD ERNGS OCT 1999 01' |  | -0.007 |
| 'R30/R37/R45 TOTAL MOS UNEMPLOYED 1997 99' |  | -0.007 |
| 'R28/R35/R43 WTR RECD ERNGS APR 1999 01' |  | -0.007 |
| 'YEAR LAST IN SCHOOL 13' |  | -0.007 |
| 'MONTH LAST IN SCHOOL 07' |  | -0.007 |
| 'TOTAL ANNUAL EARNINGS IN 2001 03' |  | -0.007 |
| 'WTR ELGBLE FOR CDS/TA 11' |  | -0.007 |
| 'R48 WTR RECEIVED SSI IN 2003 05' |  | -0.007 |
| 'R30/R37/R45 WTR UNEMPLOYED AUG 1999 01' |  | -0.007 |
| 'NEED EXTRA CARE? 78' |  | -0.007 |
| 'UP: MONTH LAST IN SCHOOL IF GED 19' |  | -0.007 |
| 'ACC TOT TXBL Y-IND 90' |  | -0.007 |
| 'actualhourlywage1_11' |  | -0.007 |
| 'realactualhourlywage1_11' |  | -0.007 |
| 'R28/R35/R43 WTR RECD ERNGS JAN 1999 01' |  | -0.007 |
| 'R28/R35/R43 WTR RECD ERNGS JUL 1999 01' |  | -0.007 |
| 'EMPLOYMENT STAT 92' |  | -0.007 |
| 'MONTH INDIVIDUAL BORN 17' |  | -0.007 |
| 'MONTH S/O FAM FORMED 07' |  | -0.007 |
| 'wagerate2_17' |  | -0.007 |
| 'realwagerate2_17' |  | -0.007 |
| 'R4 ASSET TYPE FUND/ROYALTY 2003 05' |  | -0.007 |
| 'R26/R41 REPORTED ERNINGS AMOUNT IN 01 03' |  | -0.007 |
| 'R30/R37/R45 WTR UNEMPLOYED OCT 1999 01' |  | -0.007 |
| 'UP: YEARS OF FOREIGN EDUCATION 17' |  | -0.007 |
| 'time_work2_alt_11' |  | -0.007 |
| 'R30/R37/R45 WTR UNEMPLOYED JUL 1997 99' |  | -0.007 |
| 'G84B IMPUTED TANF 17' |  | -0.007 |
| 'ACC G84K IMPUTED - CHILD SUPPORT 07' |  | -0.007 |
| 'ACC TOT TRANF INCOME 78' |  | -0.007 |
| 'ACC G84L IMPUTED - HELP FROM RELS 17' |  | -0.007 |
| 'WTR ELIGIBLE FOR TA 15' |  | -0.007 |
| 'M6 WHAT GRADE 95' |  | -0.007 |
| 'YR S/O FAM FORMED 73' |  | -0.007 |
| 'H61A WTR STATE INSURNCE PLAN FOR KIDS 05' |  | -0.007 |
| 'RESPONDENT? 78' |  | -0.007 |
| 'R60 WTR RECD HELP FRM RELS/OTRS IN 05 07' |  | -0.007 |
| 'G84B IMPUTED-TANF 11' |  | -0.007 |
| 'MONTH MOVED IN/OUT 09' |  | -0.007 |
| 'MEAN EXTRA COSTS? 78' |  | -0.007 |
| 'HRS/WK HSWRK 72' |  | -0.007 |
| 'R30/R37/R45 WTR UNEMPLOYED DEC 1999 01' |  | -0.007 |
| 'R28/R35/R43 WTR RECD ERNGS AUG 1999 01' |  | -0.007 |
| 'SEQUENCE NUMBER 91' |  | -0.007 |
| 'MONTH LAST IN SCHOOL 13' |  | -0.007 |
| 'R38 WTR RECEIVED WORKERS COMP IN 2005 07' |  | -0.007 |
| 'YEAR S/O FAM FORMED 94' |  | -0.007 |
| 'age1_17' |  | -0.007 |
| 'cohort1_17' |  | -0.007 |
| 'WHETHER MOVED IN/OUT 78' |  | -0.007 |
| 'MOVED IN/OUT 88' |  | -0.007 |
| 'WTR INCLUDED IN ATTRITOR PROJECT 07' |  | -0.007 |
| 'ANNUALIZED PUBLIC ASSISTANCE AMT 1997 99' |  | -0.007 |
| 'H61F SN 1ST PERSON EMP PROVIDES INS 11' |  | -0.007 |
| 'R30/R37/R45 WTR UNEMPLOYED JUL 1999 01' |  | -0.008 |
| 'HRS/WK HOUSEWORK 74' |  | -0.008 |
| 'G34 ACC SOC SEC AMT 05' |  | -0.008 |
| 'R56 WTR RECEIVED CHILD SUPPORT IN 05 07' |  | -0.008 |
| 'YEAR S/O FAM FORMED 11' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED JUN 1999 01' |  | -0.008 |
| 'R30/R37/R45 TOTAL MOS UNEMPLOYED 1999 01' |  | -0.008 |
| 'age2_11' |  | -0.008 |
| 'cohort2_11' |  | -0.008 |
| 'R26 WTR RECEIVED NON-VA PENSION IN 03 05' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS MAR 1999 01' |  | -0.008 |
| 'H61B MOS COVERED BY INSURANCE IN 09 11' |  | -0.008 |
| '1973 INTERVIEW NUMBER' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED SEP 1999 01' |  | -0.008 |
| 'RESULT OF TA IW ATTEMPT 09' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED APR 1999 01' |  | -0.008 |
| 'R43 STATE WHERE RECD PUB ASSTNCE 2003 05' |  | -0.008 |
| '2015 INTERVIEW NUMBER' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS NOV 1999 01' |  | -0.008 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 07' |  | -0.008 |
| 'OFUM BUSINESS LABOR INCOME - IMPUTED 07' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS JUN 1999 01' |  | -0.008 |
| 'R28/R35/R43 TOT MOS RECD ERNGS 1999 01' |  | -0.008 |
| 'RESULT OF DUST IW ATTEMPT 09' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS MAY 1999 01' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED MAR 1999 01' |  | -0.008 |
| 'ACC G84C_G94C IMPUTED - SSI 13' |  | -0.008 |
| 'H61F SN 2ND PERSON EMP PROVIDES INS 11' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED FEB 1999 01' |  | -0.008 |
| 'G84L IMPUTED HELP FROM RELS 17' |  | -0.008 |
| 'H61G SN 1ST PERSON POLICY HOLDER 17' |  | -0.008 |
| 'YEAR MOVED IN/OUT 80' |  | -0.008 |
| 'MONTH IND BORN 83' |  | -0.008 |
| 'UP: MONTH RECEIVED GED 15' |  | -0.008 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 09' |  | -0.008 |
| 'G76 NUMBER OF JOBS IN PY 07' |  | -0.008 |
| 'MONTH MOVED IN/OUT 19' |  | -0.008 |
| 'UP: GRADE SCHOOL FINISHED IF NEITHER 15' |  | -0.008 |
| 'H6E WALKING 95' |  | -0.008 |
| 'H6F GET OUTSIDE 95' |  | -0.008 |
| 'H9 PROB PREPARE MEALS 95' |  | -0.008 |
| 'H7 CKPT 95' |  | -0.008 |
| 'H6D GET OUT OF BED/CHAIR 95' |  | -0.008 |
| 'H6B DRESSING 95' |  | -0.008 |
| 'H6G USE/GET TO TOILET 95' |  | -0.008 |
| 'H6C EATING 95' |  | -0.008 |
| 'H6A BATHING 95' |  | -0.008 |
| 'H11 PROB SHOP PERS ITEM 95' |  | -0.008 |
| 'H19 PROB LIGHT HOUSEWORK 95' |  | -0.008 |
| 'H13 PROB MANAGE MONEY 95' |  | -0.008 |
| 'H15 PROB USE PHONE 95' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS DEC 1999 01' |  | -0.008 |
| 'R30/R37/R45 WTR UNEMPLOYED JAN 1999 01' |  | -0.008 |
| '1977 INTERVIEW NUMBER' |  | -0.008 |
| 'YEAR MOVED IN/OUT 74' |  | -0.008 |
| 'WHETHER MOVED IN/OUT 09' |  | -0.008 |
| 'OFUM BUSINESS LABOR INCOME - IMPUTED 11' |  | -0.008 |
| 'MONTH MOVED IN/OUT 95' |  | -0.008 |
| 'MONTH LAST IN SCHOOL 11' |  | -0.008 |
| 'COMPLETED EDUCATION 92' |  | -0.008 |
| '1980 EMPL STATUS 80' |  | -0.008 |
| 'MONTH MOVED IN/OUT 99' |  | -0.008 |
| 'H17 PROB HEAVY HOUSEWORK 95' |  | -0.008 |
| 'R28/R35/R43 WTR RECD ERNGS FEB 1999 01' |  | -0.009 |
| 'time_volunteering1_17' |  | -0.009 |
| 'time_pcare1_17' |  | -0.009 |
| '1990 INTERVIEW NUMBER' |  | -0.009 |
| 'COMPLETED EDUCATION 75' |  | -0.009 |
| '1985 INTERVIEW NUMBER' |  | -0.009 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 07' |  | -0.009 |
| 'R28/R35/R43 WTR RECD ERNGS SEP 1999 01' |  | -0.009 |
| 'MONTH S/O FAM FORMED 94' |  | -0.009 |
| 'MAIN FAM ID FOR S/O 09' |  | -0.009 |
| 'H13 OFUM HEALTH GOOD 91' |  | -0.009 |
| 'R58A WTR STOPPED FOOD STAMPS IN 1999 01' |  | -0.009 |
| 'MAIN FAM ID FOR S/O 82' |  | -0.009 |
| 'H61E TYPE CURRENT HEALTH INS MEN 1 17' |  | -0.009 |
| 'WHETHER STUDENT 97' |  | -0.009 |
| 'OFUM BUSINESS ASSET INCOME - IMPUTED 09' |  | -0.009 |
| 'G84G IMPUTED PENSION/ANN 13' |  | -0.009 |
| 'ACC G84H IMPUTED - UNEMP COMP 05' |  | -0.009 |
| 'G84H IMPUTED UNEMP COMP 05' |  | -0.009 |
| 'H61E2 WTR STATE INSURNCE PLN FOR KIDS 15' |  | -0.009 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 03' |  | -0.009 |
| 'WHETHER MOVED IN/OUT 87' |  | -0.009 |
| 'ACC TOT TXBL Y-IND 89' |  | -0.009 |
| 'SEQUENCE NUMBER 85' |  | -0.009 |
| 'R30/R37/R45 WTR UNEMPLOYED NOV 1997 99' |  | -0.009 |
| 'H61M MONTHS UNINSURED IN 15 19' |  | -0.009 |
| 'WTR COVERED BY TANF PAYMENTS IN 2004 05' |  | -0.009 |
| 'R30/R37/R45 WTR UNEMPLOYED DEC 1997 99' |  | -0.009 |
| 'SN 2ND PERSON WHO HELPED WITH IW 19' |  | -0.009 |
| 'G31 TYPE SOC SEC RCD 90' |  | -0.009 |
| 'UP: YEAR LAST IN SCHOOL IF NEITHER 15' |  | -0.009 |
| 'YEAR MOVED IN/OUT 75' |  | -0.009 |
| 'MONTH MOVED IN/OUT 88' |  | -0.009 |
| 'R44 WTR RECD TANF IN 2003 05' |  | -0.009 |
| 'R30/R37/R45 WTR UNEMPLOYED OCT 1997 99' |  | -0.009 |
| 'UP: MONTH RECEIVED GED 17' |  | -0.009 |
| 'MONTH MOVED IN/OUT 92' |  | -0.009 |
| '2005 INTERVIEW NUMBER' |  | -0.009 |
| 'R20 WTR RECEIVED OTHER HELP IN 1999 01' |  | -0.009 |
| 'R30/R37/R45 WTR UNEMPLOYED MAY 1999 01' |  | -0.009 |
| 'TOTAL TRANSFER Y 77' |  | -0.009 |
| 'G84K IMPUTED CHILD SUPPORT 13' |  | -0.009 |
| 'R20 WTR RECEIVED OTHER HELP IN 2001 03' |  | -0.009 |
| 'YEAR LAST IN SCHOOL 07' |  | -0.009 |
| 'OFUM BUSINESS LABOR INCOME - IMPUTED 09' |  | -0.009 |
| 'TYPE TRANSFER Y BUILT 92' |  | -0.009 |
| 'R12 WTR RECEIVED CHILD SUPPORT IN 97 99' |  | -0.009 |
| 'YEAR LAST IN SCHOOL 99' |  | -0.009 |
| 'UP: MONTH LAST IN SCHOOL IF GED 17' |  | -0.009 |
| 'HEALTH GOOD? 07' |  | -0.009 |
| 'R28/R35/R43 WTR RECD ERNGS AUG 1997 99' |  | -0.009 |
| 'MAIN FAM ID FOR S/O 70' |  | -0.009 |
| 'WTR ELIGIBLE FOR TA 09' |  | -0.01 |
| 'EMPL STATUS 79' |  | -0.01 |
| 'WHETHER STUDENT 95' |  | -0.01 |
| 'SEQUENCE NUMBER 80' |  | -0.01 |
| 'R27/R34/R42 WEEKS WORKED IN 1999 01' |  | -0.01 |
| 'TOTAL MONEY INCOME 74' |  | -0.01 |
| 'SEQUENCE NUMBER 86' |  | -0.01 |
| 'H61F SN 2ND PERSON EMP PROVIDES INS 15' |  | -0.01 |
| 'H61E TYPE CURRENT HEALTH INS MEN 3 19' |  | -0.01 |
| 'MONTH MOVED IN/OUT 79' |  | -0.01 |
| 'R4 WTR RECD GEN ASSISTANCE IN 2001 03' |  | -0.01 |
| 'R2/R11 EARNINGS PER UNIT IN 2005 07' |  | -0.01 |
| 'EMPLOYMENT STATUS 99' |  | -0.01 |
| 'EMPLOYMENT STATUS 93' |  | -0.01 |
| 'MAIN FAM ID FOR S/O 73' |  | -0.01 |
| 'RELATIONSHIP TO HEAD 82' |  | -0.01 |
| 'ACC TOT LABOR Y-IND 91' |  | -0.01 |
| 'TOTAL TRANSFER Y 79 80' |  | -0.01 |
| 'R28/R35/R43 WTR RECD ERNGS SEP 1997 99' |  | -0.01 |
| 'R28/R35/R43 WTR RECD ERNGS DEC 1997 99' |  | -0.01 |
| 'ACC TRANSFER Y 77' |  | -0.01 |
| 'YEARS COMPLETED EDUCATION 97' |  | -0.01 |
| 'head2017' |  | -0.01 |
| 'R30/R37/R45 WTR UNEMPLOYED SEP 1997 99' |  | -0.01 |
| 'CALCULATED HOURLY WAGE RATE IN 2001 03' |  | -0.01 |
| 'YRS COMPLETED EDUC 94' |  | -0.01 |
| 'RESPONDENT? 82' |  | -0.01 |
| 'CALCULATED HOURLY WAGE RATE IN 1997 99' |  | -0.01 |
| 'R30/R37/R45 WTR UNEMPLOYED AUG 1997 99' |  | -0.01 |
| 'H61E TYPE CURRENT HEALTH INS MEN 2 17' |  | -0.01 |
| 'RESULT OF CDS/TA IW ATTEMPT 07' |  | -0.01 |
| 'RESPONDENT? 77' |  | -0.01 |
| 'YR S/O FAM FORMED 80' |  | -0.01 |
| 'MAIN FAM ID FOR S/O 91' |  | -0.01 |
| 'R28/R35/R43 WTR RECD ERNGS NOV 1997 99' |  | -0.01 |
| 'H61D3 WTR COVERED BY INSURANCE NOW 17' |  | -0.01 |
| '1994 INTERVIEW NUMBER' |  | -0.01 |
| 'ACC G84B IMPUTED - TANF 15' |  | -0.01 |
| 'ACC TOT HRS UNEMP 77 78' |  | -0.01 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 99' |  | -0.01 |
| 'G84D_G94D IMPUTED WELFARE 17' |  | -0.01 |
| 'SEQUENCE NUMBER 90' |  | -0.01 |
| 'AGE OF INDIVIDUAL 19' |  | -0.011 |
| 'age1_19' |  | -0.011 |
| 'cohort1_19' |  | -0.011 |
| 'RELATION TO HEAD 11' |  | -0.011 |
| 'realactualhourlywage2_13' |  | -0.011 |
| 'actualhourlywage2_13' |  | -0.011 |
| 'G84L IMPUTED HELP FROM RELS 05' |  | -0.011 |
| 'MONTH S/O FAM FORMED 87' |  | -0.011 |
| 'R58A WTR STOPPED FOOD STAMPS IN 1997 99' |  | -0.011 |
| 'G76 NUMBER OF JOBS IN PY 17' |  | -0.011 |
| 'M13D WTR DECIDER FOR CHARITABLE GIVNG 03' |  | -0.011 |
| 'WHETHER MOVED IN/OUT 72' |  | -0.011 |
| 'ACC TOT ASSET Y-IND 91' |  | -0.011 |
| 'MONTH LAST IN SCHOOL 01' |  | -0.011 |
| 'MONTH INDIVIDUAL BORN 90' |  | -0.011 |
| 'MONTH S/O FAM FORMED 03' |  | -0.011 |
| 'G76 NUMBER OF JOBS IN PY 11' |  | -0.011 |
| 'R29/R36/R44 HRS PER WK WORKED 1999 01' |  | -0.011 |
| 'MONTH S/O FAM FORMED 11' |  | -0.011 |
| 'R28/R35/R43 WTR RECD ERNGS JUL 1997 99' |  | -0.011 |
| 'ACC ANN WRK HRS-IND 89' |  | -0.011 |
| 'realcost_home_17' |  | -0.011 |
| 'cost_home_17' |  | -0.011 |
| 'ACC G84D_G94D IMPUTED - WELFARE 11' |  | -0.011 |
| 'YEAR MOVED IN/OUT 87' |  | -0.011 |
| 'UP: YEAR GRADUATED HIGH SCHOOL 15' |  | -0.011 |
| 'RESULT OF TA IW ATTEMPT 19' |  | -0.011 |
| 'ACC G84D_G94D IMPUTED -WELFARE 09' |  | -0.011 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 09' |  | -0.011 |
| 'R28/R35/R43 WTR RECD ERNGS OCT 1997 99' |  | -0.011 |
| 'G84D_G94D IMPUTED WELFARE 11' |  | -0.011 |
| 'MONTH 1ST/ONLY CHILD BORN' |  | -0.011 |
| 'TYPE TRANSFER Y 86' |  | -0.011 |
| 'MONTH MOVED IN/OUT 74' |  | -0.011 |
| 'MONTH S/O FAM FORMED 05' |  | -0.011 |
| 'ACC G84L IMPUTED - HELP FROM RELS 09' |  | -0.011 |
| 'YEAR MOVED IN/OUT 92' |  | -0.011 |
| 'G33 TYPE SOC SEC RCD 87' |  | -0.011 |
| 'SN 2ND PERSON WHO HELPED WITH IW 09' |  | -0.011 |
| 'SEQUENCE NUMBER 99' |  | -0.011 |
| 'ACC TOT TRNSFR Y-IND 91' |  | -0.011 |
| 'LOOKING LAST 4 WKS? 78' |  | -0.011 |
| 'OFUM TOTAL TRANSFER INCOME -IMPUTED 09' |  | -0.011 |
| 'MOVED IN/OUT 91' |  | -0.011 |
| 'MARITAL PAIRS INDICATOR 01' |  | -0.011 |
| 'R8 WTR RECEIVED SSI IN 1999 01' |  | -0.011 |
| 'WTR COVERED BY TANF PAYMENTS IN 2016 17' |  | -0.011 |
| 'EMPLOYMENT STAT 87' |  | -0.011 |
| 'COMPLETED EDUC-IND 89' |  | -0.011 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 13' |  | -0.011 |
| 'YR S/O FAM FORMED 75' |  | -0.011 |
| 'cost_furnish_11' |  | -0.011 |
| 'realcost_furnish_11' |  | -0.011 |
| 'GRADE FINISHED 71' |  | -0.011 |
| 'H13 OFUM HEALTH GOOD 89' |  | -0.011 |
| 'R4 WTR RECD EMERGENCY ASSISTANCE 1999 01' |  | -0.011 |
| 'MONTH MOVED IN/OUT 76' |  | -0.011 |
| 'TOTAL TRNSFR INCOME 85' |  | -0.011 |
| 'G84K IMPUTED CHILD SUPPORT 15' |  | -0.011 |
| 'MONTH GRADUATED HIGHEST DEGREE 13' |  | -0.012 |
| 'H61G SN 1ST PERSON POLICY HOLDER 15' |  | -0.012 |
| 'MO S/O FAM FORMED 80' |  | -0.012 |
| '1982 INTERVIEW NUMBER' |  | -0.012 |
| 'H13 OFUM HEALTH GOOD 88' |  | -0.012 |
| 'WHETHER SELECTED FOR CDS 97' |  | -0.012 |
| 'UP: FOREIGN DEGREE 15' |  | -0.012 |
| 'WHETHER ELIGIBLE FOR CDS 97' |  | -0.012 |
| 'MAIN FAM ID FOR S/O 75' |  | -0.012 |
| 'G34 AMT SOC SEC RCD 87' |  | -0.012 |
| 'H61E2 WTR STATE INSURNCE PLN FOR KIDS 13' |  | -0.012 |
| 'H61F SN 1ST PERSON EMP PROVIDES INS 19' |  | -0.012 |
| 'OFUM TOTAL ASSET INCOME - IMPUTED 15' |  | -0.012 |
| 'R29/R36/R44 HRS PER WK WORKED 1997 99' |  | -0.012 |
| 'MONTH S/O FAM FORMED 15' |  | -0.012 |
| 'cohort1_11' |  | -0.012 |
| 'age1_11' |  | -0.012 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 15' |  | -0.012 |
| 'WTR ELGBLE FOR CDS TRANSITN TO ADULT 05' |  | -0.012 |
| 'ACCURACY OF PUBLIC ASSISTANCE IN 1997 99' |  | -0.012 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 09' |  | -0.012 |
| 'weight_13' |  | -0.012 |
| 'RELATIONSHIP TO HEAD 77' |  | -0.012 |
| 'UP: WTR ATTENDED COLLEGE 15' |  | -0.012 |
| 'SN 2ND PERSON WHO HELPED WITH IW 17' |  | -0.012 |
| 'MO S/O FAM FORMED 75' |  | -0.012 |
| 'G31 TYPE SOC SEC RCD 89' |  | -0.012 |
| 'G84J IMPUTED WORKERS COMP 07' |  | -0.012 |
| 'ACC G84H IMPUTED - UNEMP COMP 09' |  | -0.012 |
| 'TOT TRANSFER EXC SS 84' |  | -0.012 |
| 'MAIN FAM ID FOR S/O 77' |  | -0.012 |
| 'WHETHER STUDENT 99' |  | -0.012 |
| 'TYPE TRANSFER Y 79 80' |  | -0.012 |
| '1970 INTERVIEW NUMBER' |  | -0.012 |
| 'R5/R18 ASSET INC AMT 2003 05' |  | -0.012 |
| 'H61B MOS COVERED BY INSURANCE IN 03 05' |  | -0.012 |
| 'EMPLOYMENT STATUS 03' |  | -0.012 |
| '1968 ID OF MOTHER' |  | -0.012 |
| 'ACC TOT TXBL Y 84' |  | -0.012 |
| 'YEAR S/O FAM FORMED 15' |  | -0.012 |
| 'UP: YEAR LAST IN SCHOOL IF GED 17' |  | -0.012 |
| 'UP: HIGHEST DEG MAJOR MEN2 2-DIGIT 19' |  | -0.012 |
| 'G84B IMPUTED TANF 15' |  | -0.013 |
| 'G84L IMPUTED HELP FROM RELS 07' |  | -0.013 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 19' |  | -0.013 |
| 'SEQUENCE NUMBER 87' |  | -0.013 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 09' |  | -0.013 |
| '2003 INTERVIEW NUMBER' |  | -0.013 |
| 'MO S/O FAM FORMED 70' |  | -0.013 |
| 'UP: MONTH GRADUATED HIGH SCHOOL 15' |  | -0.013 |
| 'G84L IMPUTED HELP FROM RELS 11' |  | -0.013 |
| 'H61C MOS COVERED BY INSURANCE IN 04 05' |  | -0.013 |
| 'H61F SN 2ND PERSON EMP PROVIDES INS 17' |  | -0.013 |
| 'R28/R35/R43 TOT MOS RECD ERNGS 1997 99' |  | -0.013 |
| 'RELATIONSHIP TO HEAD 78' |  | -0.013 |
| 'TYPE OF HIGHEST DEGREE 19' |  | -0.013 |
| 'WHETHER MOVED IN/OUT 85' |  | -0.013 |
| 'ACC TOT TXBL INCOME 85' |  | -0.013 |
| 'MAIN FAM ID FOR S/O 71' |  | -0.013 |
| 'R28/R35/R43 WTR RECD ERNGS MAR 1997 99' |  | -0.013 |
| 'WHETHER MOVED IN/OUT 76' |  | -0.013 |
| 'R28/R35/R43 WTR RECD ERNGS JAN 1997 99' |  | -0.013 |
| 'MAIN FAM ID FOR S/O 69' |  | -0.013 |
| 'H17 PROB HEAVY HOUSEWORK 96' |  | -0.013 |
| 'HRS UNEMP IN 74 75' |  | -0.013 |
| 'R26/R33/R41 REP EARNINGS UNIT 1999 01' |  | -0.013 |
| 'YEAR INDIVIDUAL BORN 19' |  | -0.013 |
| 'RESPONDENT? 76' |  | -0.013 |
| 'ACC TOT TRNSFR EXC SS 86' |  | -0.013 |
| 'RESULT OF DUST 2013 IW ATTEMPT 13' |  | -0.013 |
| 'ACCURACY OFUM TOTAL LABOR INCOME 15' |  | -0.013 |
| 'COMPLETED EDUCATION 87' |  | -0.013 |
| 'GRADE FINISHED 73' |  | -0.013 |
| 'R8 WTR RECEIVED SSI IN 2001 03' |  | -0.013 |
| 'sex1_17' |  | -0.013 |
| 'MARITAL PAIRS INDICATOR 05' |  | -0.013 |
| 'head2015' |  | -0.013 |
| 'time_pcare1_19' |  | -0.013 |
| 'SEQUENCE NUMBER 72' |  | -0.013 |
| 'M9 LAST ENROLLED FULL OR PART TIME 95' |  | -0.013 |
| 'R28/R35/R43 WTR RECD ERNGS FEB 1997 99' |  | -0.013 |
| 'G34 ACC SOC SEC AMT 92' |  | -0.013 |
| 'H61E TYPE CURRENT HEALTH INS MEN 1 19' |  | -0.013 |
| 'MONTH YOUNGEST CHILD BORN' |  | -0.014 |
| '1974 INTERVIEW NUMBER' |  | -0.014 |
| 'UP: YEAR RECEIVED GED 17' |  | -0.014 |
| 'SEQUENCE NUMBER 78' |  | -0.014 |
| 'RESPONDENT? 80' |  | -0.014 |
| 'YEAR MOVED IN/OUT 83' |  | -0.014 |
| 'SEQUENCE NUMBER 92' |  | -0.014 |
| 'WTR ELGBLE FOR CDS/TA 07' |  | -0.014 |
| 'G34 ACC SOC SEC AMT 07' |  | -0.014 |
| 'WTR COVERED BY TANF PAYMENTS IN 2012 13' |  | -0.014 |
| 'MONTH IND BORN 87' |  | -0.014 |
| 'SEQUENCE NUMBER 88' |  | -0.014 |
| 'YEAR 1ST/ONLY CHILD BORN' |  | -0.014 |
| 'H8 GET HELP W ACTIVITIES 94' |  | -0.014 |
| 'H20 B/C OF HEALTH? 94' |  | -0.014 |
| 'ACC TOT TRNSFR Y-IND 89' |  | -0.014 |
| 'H8 GET HELP W ACTIVITIES 96' |  | -0.014 |
| 'G84A_G94B IMPUTED INTEREST 15' |  | -0.014 |
| 'MONTH INDIVIDUAL BORN 15' |  | -0.014 |
| 'M25 OTHER NURSERY PRESCHOOL DAY CARE 95' |  | -0.014 |
| 'YEAR MOVED IN/OUT 95' |  | -0.014 |
| 'TOTAL TRANSFR INCOM 78' |  | -0.014 |
| 'R21 WTR RECEIVED SOCL SECURITY IN 05 07' |  | -0.014 |
| 'R28/R35/R43 WTR RECD ERNGS JUN 1997 99' |  | -0.014 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 11' |  | -0.014 |
| 'HRS UNEMP LAST YR 77' |  | -0.014 |
| 'WTR EVER MOVED OUT OF FU OR DIED' |  | -0.014 |
| 'WTR ELIGIBLE FOR CDS 2014 13' |  | -0.014 |
| 'G31 TYPE SOC SEC RCD 88' |  | -0.014 |
| 'UP: GRADE LEVEL IF GED 17' |  | -0.014 |
| 'HEALTH GOOD? 93' |  | -0.014 |
| 'R3/R13 WTR EARNINGS DEC 2003 05' |  | -0.014 |
| 'YEAR INDIVIDUAL BORN 17' |  | -0.014 |
| 'TYPE TRANSFER Y-IND 91' |  | -0.014 |
| 'H61D WTR COVERED BY INSURANCE NOW 11' |  | -0.014 |
| 'TYPE OF HIGHEST DEGREE 17' |  | -0.014 |
| '1995 INTERVIEW NUMBER' |  | -0.014 |
| 'YEAR LAST IN SCHOOL 97' |  | -0.014 |
| 'R26/R33/R41 REP EARNINGS UNIT 1997 99' |  | -0.014 |
| 'WHETHER MOVED IN/OUT 71' |  | -0.014 |
| 'H61 TYPE HEALTH INSURANCE MENTION 3 11' |  | -0.014 |
| 'EMPLOYMENT STAT-IND 89' |  | -0.014 |
| 'R17 WTR RECEIVED ASSET INCOME IN 05 07' |  | -0.014 |
| 'cost_health_11' |  | -0.015 |
| 'realcost_health_11' |  | -0.015 |
| 'R14 OFUM HRS PER WK WORKED 2003 05' |  | -0.015 |
| 'YR S/O FAM FORMED 70' |  | -0.015 |
| 'H61E2 WTR STATE INSURNCE PLN FOR KIDS 17' |  | -0.015 |
| 'YEAR S/O FAM FORMED 91' |  | -0.015 |
| 'YEARS COMPLETED EDUCATION 95' |  | -0.015 |
| 'sex1_13' |  | -0.015 |
| 'MONTH MOVED IN/OUT 86' |  | -0.015 |
| 'WHETHER STUDENT 01' |  | -0.015 |
| 'SEQUENCE NUMBER 01' |  | -0.015 |
| 'MONTH INDIVIDUAL BORN 13' |  | -0.015 |
| 'H53 OFUM HEALTH GOOD 92' |  | -0.015 |
| 'RELATIONSHIP TO HEAD 76' |  | -0.015 |
| 'R28/R35/R43 WTR RECD ERNGS MAY 1997 99' |  | -0.015 |
| 'M13D WTR DECIDER FOR CHARITABLE GIVNG 05' |  | -0.015 |
| 'R28/R35/R43 WTR RECD ERNGS APR 1997 99' |  | -0.015 |
| 'K31 TYPE SOC SEC RCD 85' |  | -0.015 |
| 'G34 ACC SOC SEC AMT 13' |  | -0.015 |
| 'H6C EATING 96' |  | -0.015 |
| 'H6B DRESSING 96' |  | -0.015 |
| 'H6D GET OUT OF BED/CHAIR 96' |  | -0.015 |
| 'H6E WALKING 96' |  | -0.015 |
| 'H6F GET OUTSIDE 96' |  | -0.015 |
| 'H6A BATHING 96' |  | -0.015 |
| 'H19 PROB LIGHT HOUSEWORK 96' |  | -0.015 |
| 'H7 CKPT 96' |  | -0.015 |
| 'H9 PROB PREPARE MEALS 96' |  | -0.015 |
| 'R15 WTR OFUM UNEMP JUN 2003 05' |  | -0.015 |
| 'TOTAL ASSET INCOME 93' |  | -0.015 |
| 'MO S/O FAM FORMED 78' |  | -0.015 |
| 'RESPONDENT? 74' |  | -0.015 |
| 'R15 WTR OFUM UNEMP SEP 2003 05' |  | -0.015 |
| 'R15 WTR OFUM UNEMP MAY 2003 05' |  | -0.015 |
| 'EMPLOYMENT STAT 86' |  | -0.015 |
| 'R15 WTR OFUM UNEMP OCT 2003 05' |  | -0.015 |
| 'H61 TYPE HEALTH INSURANCE MENTION 2 05' |  | -0.015 |
| 'EMPLOYMENT STAT-IND 91' |  | -0.015 |
| 'time_shopping1_17' |  | -0.015 |
| 'RELATIONSHIP TO HEAD 74' |  | -0.015 |
| 'R15 WTR OFUM UNEMP AUG 2003 05' |  | -0.015 |
| '1993 INTERVIEW NUMBER' |  | -0.015 |
| 'R3/R13 WTR EARNINGS OCT 2003 05' |  | -0.015 |
| 'R8 WTR RECEIVED SSI IN 1997 99' |  | -0.015 |
| 'MO S/O FAM FORMED 74' |  | -0.015 |
| 'YEAR YOUNGEST CHILD BORN' |  | -0.015 |
| 'WTR COVERED BY TANF PAYMENTS IN 2010 11' |  | -0.015 |
| 'weight_11' |  | -0.015 |
| 'R15 WTR OFUM UNEMP NOV 2003 05' |  | -0.016 |
| 'TOT TRANSFR EXC SS 86' |  | -0.016 |
| 'R48 WTR RECEIVED SSI IN 2005 07' |  | -0.016 |
| 'R44 WTR RECD TANF IN 2005 07' |  | -0.016 |
| 'R15 WTR OFUM UNEMP JUL 2003 05' |  | -0.016 |
| 'GRADE OF SCHOOL FINISHED IF NEITHER 17' |  | -0.016 |
| 'SEQUENCE NUMBER 11' |  | -0.016 |
| 'YR S/O FAM FORMED 77' |  | -0.016 |
| 'MONTH GRADUATED HIGHEST DEGREE 15' |  | -0.016 |
| 'R3/R13 WTR EARNINGS SEP 2003 05' |  | -0.016 |
| 'WTR CDS 2014 IW CODED COMPLETE 13' |  | -0.016 |
| 'M19 WHICH GRADE REPEATED 2 95' |  | -0.016 |
| 'TOT TRANSFER Y 82 83' |  | -0.016 |
| 'RESPONDENT? 05' |  | -0.016 |
| 'R3/R13 WTR EARNINGS FEB 2003 05' |  | -0.016 |
| 'MONTH MOVED IN/OUT 72' |  | -0.016 |
| 'R3/R13 WTR EARNINGS NOV 2003 05' |  | -0.016 |
| 'R52 WTR RECEIVED OTHER WELFARE IN 03 05' |  | -0.016 |
| 'MONTH MOVED IN 68' |  | -0.016 |
| 'M20 EVER CLASSIFIED NEED SPECIAL ED 95' |  | -0.016 |
| 'ES4 WHETHER MOM LIVED IN US IN 1968 97' |  | -0.016 |
| 'RELATION TO HEAD 07' |  | -0.016 |
| 'RELATIONSHIP TO HEAD 79' |  | -0.016 |
| 'WHETHER MOVED IN/OUT 79' |  | -0.016 |
| 'MONTH LAST IN SCHOOL 97' |  | -0.016 |
| 'ACC G84K IMPUTED - CHILD SUPPORT 15' |  | -0.016 |
| 'COMPLETED EDUC-IND 91' |  | -0.016 |
| 'M21 LEARN DISAB PERCEPT/SPEECH IMPAIR 95' |  | -0.016 |
| 'M15 GRADE ATTENDED PRIVATE SCHOOL 1 95' |  | -0.016 |
| 'ACC TRANSFER Y 75' |  | -0.016 |
| 'YEAR MOVED IN/OUT 94' |  | -0.016 |
| 'MO S/O FAM FORMED 77' |  | -0.016 |
| 'ES1 STATE WHERE BORN 97' |  | -0.016 |
| 'MONTH LAST IN SCHOOL IF NEITHER 15' |  | -0.016 |
| 'MONTH S/O FAM FORMED 91' |  | -0.016 |
| 'R3/R13 WTR EARNINGS MAR 2003 05' |  | -0.016 |
| 'G84D_G94D IMPUTED WELFARE 09' |  | -0.016 |
| 'R15 WTR OFUM UNEMP DEC 2003 05' |  | -0.016 |
| 'UP: WTR CURRENTLY ENROLLED IN SCHOOL 15' |  | -0.016 |
| 'YEAR MOVED IN/OUT 79' |  | -0.016 |
| 'F34 AMT SOC SEC RCD 84' |  | -0.016 |
| 'R42 WTR RECEIVED TANF/GA IN 2005 07' |  | -0.016 |
| 'RELATION TO HEAD 15' |  | -0.016 |
| 'R80A WTR REC SCHOOL LUNCH IN 2002 03' |  | -0.016 |
| 'YEAR LAST IN SCHOOL 95' |  | -0.016 |
| 'R44 WTR RECD EMERG ASSISTANCE IN 2003 05' |  | -0.016 |
| 'R15 WTR OFUM UNEMP FEB 2003 05' |  | -0.016 |
| 'TOT TRNSFR EXC SS-IND 91' |  | -0.016 |
| 'YEAR S/O FAM FORMED 93' |  | -0.016 |
| 'WHETHER MOVED IN/OUT 69' |  | -0.017 |
| 'flag_allyears' |  | -0.017 |
| 'R2/R11 EARNINGS AMT REPORTED IN 2003 05' |  | -0.017 |
| 'SEQUENCE NUMBER 09' |  | -0.017 |
| 'TOT TRANSFR EXC SS 92' |  | -0.017 |
| 'R15 WTR OFUM UNEMP MAR 2003 05' |  | -0.017 |
| 'G34 AMT SOC SEC RCD 90' |  | -0.017 |
| 'time_education1_19' |  | -0.017 |
| 'R15 WTR OFUM UNEMP APR 2003 05' |  | -0.017 |
| 'ES5 WTR MOM US CITIZEN OUT OF US IN 6897' |  | -0.017 |
| 'UP: WTR RECEIVED COLLEGE DEGREE 15' |  | -0.017 |
| 'MAIN FAM ID FOR S/O 88' |  | -0.017 |
| 'WTR ELIGIBLE FOR TA 17' |  | -0.017 |
| 'HEALTH GOOD? 05' |  | -0.017 |
| 'ES6 WHETHER DAD LIVED IN US IN 1968 97' |  | -0.017 |
| 'ES7 WTR DAD US CITIZEN OUT OF US IN 6897' |  | -0.017 |
| 'MAIN FAM ID FOR S/O 15' |  | -0.017 |
| 'RESPONDENT? 84' |  | -0.017 |
| 'R3/R13 WTR EARNINGS JAN 2003 05' |  | -0.017 |
| 'RELATIONSHIP TO HEAD 75' |  | -0.017 |
| 'SN 1ST PERSON WHO HELPED WITH IW 13' |  | -0.017 |
| '1976 INTERVIEW NUMBER' |  | -0.017 |
| 'R15 WTR OFUM UNEMP JAN 2003 05' |  | -0.017 |
| 'AGE OF INDIVIDUAL 17' |  | -0.017 |
| 'MARITAL PAIRS INDICATOR 03' |  | -0.017 |
| 'MONTH S/O FAM FORMED 93' |  | -0.017 |
| 'YEAR MOVED IN/OUT 88' |  | -0.017 |
| 'ACC ANN WRK HRS 85' |  | -0.017 |
| 'H61N MONTHS UNINSURED IN 16 19' |  | -0.017 |
| 'H6G USE/GET TO TOILET 96' |  | -0.017 |
| 'H15 PROB USE PHONE 96' |  | -0.017 |
| 'H13 PROB MANAGE MONEY 96' |  | -0.017 |
| 'H11 PROB SHOP PERS ITEM 96' |  | -0.017 |
| 'UP: WTR REC HS DIPLOMA/GED/NEITHER 15' |  | -0.017 |
| 'G34 ACC SOC SEC AMT 17' |  | -0.017 |
| 'TYPE OF HIGHEST DEGREE 15' |  | -0.017 |
| 'MO S/O FAM FORMED 72' |  | -0.017 |
| 'TYPE TRANSFER Y 87' |  | -0.017 |
| 'TYPE TRANSFER Y 84' |  | -0.017 |
| 'ACC WORK HRS 77' |  | -0.017 |
| 'YEAR MOVED IN 68' |  | -0.017 |
| 'G33 TYPE SOC SEC RCD 92' |  | -0.017 |
| 'R56 WTR RECEIVED CHILD SUPPORT IN 03 05' |  | -0.017 |
| 'SUM SS+TRANSFER Y 84' |  | -0.017 |
| 'TOT ASSET INCOME 92' |  | -0.017 |
| 'WTR ATTENDED COLLEGE 19' |  | -0.018 |
| 'EMPLOYMENT STAT 84' |  | -0.018 |
| 'SELECTION STATUS FOR CDS 2014 13' |  | -0.018 |
| 'G34 AMT SOC SEC RCD 86' |  | -0.018 |
| 'YR S/O FAM FORMED 72' |  | -0.018 |
| 'EMPLOYMENT STATUS 09' |  | -0.018 |
| 'RELATIONSHIP TO HEAD 80' |  | -0.018 |
| 'TYPE TRANSFER Y 82 83' |  | -0.018 |
| 'EMPLOYMENT STATUS 97' |  | -0.018 |
| 'YEARS COMPLETED EDUCATION 96' |  | -0.018 |
| 'F33 TYPE SOC SEC RCD 84' |  | -0.018 |
| 'G84H IMPUTED UNEMP COMP 07' |  | -0.018 |
| 'WHETHER MOVED IN/OUT 96' |  | -0.018 |
| 'H1/37/69 HLTH STATUS 86' |  | -0.018 |
| 'ACC ANN WRK HRS 82 83' |  | -0.018 |
| 'FOLLOW STATUS 03' |  | -0.018 |
| 'EMPLOYMENT STAT-IND 88' |  | -0.018 |
| '1991 INTERVIEW NUMBER' |  | -0.018 |
| '1986 INTERVIEW NUMBER' |  | -0.018 |
| 'time_education1_17' |  | -0.018 |
| 'RESPONDENT? 75' |  | -0.018 |
| 'ACC ANN WRK HRS 84' |  | -0.018 |
| 'RELATION TO HEAD 03' |  | -0.018 |
| 'realcost_trips_11' |  | -0.018 |
| 'cost_trips_11' |  | -0.018 |
| 'R3/R13 WTR EARNINGS JUN 2003 05' |  | -0.018 |
| 'H18 B/C OF HEALTH? 94' |  | -0.018 |
| 'H61G SN 2ND PERSON POLICY HOLDER 19' |  | -0.018 |
| 'R3/R13 WTR EARNINGS AUG 2003 05' |  | -0.018 |
| 'MONTH LAST IN SCHOOL IF NEITHER 17' |  | -0.018 |
| 'HEALTH GOOD? 96' |  | -0.018 |
| 'H61E TYPE CURRENT HEALTH INS MEN 3 17' |  | -0.018 |
| 'UP: WTR ATTENDED SCHOOL SINCE LAST IW 15' |  | -0.018 |
| 'R3/R13 WTR EARNINGS JUL 2003 05' |  | -0.018 |
| 'G33 TYPE SOC SEC RCD 05' |  | -0.018 |
| 'SEQUENCE NUMBER 79' |  | -0.018 |
| 'R3/R13 WTR EARNINGS APR 2003 05' |  | -0.018 |
| 'G84H IMPUTED UNEMP COMP 09' |  | -0.018 |
| 'R2/R11 EARNINGS PER UNIT IN 2003 05' |  | -0.018 |
| 'SEQUENCE NUMBER 76' |  | -0.019 |
| 'HEALTH GOOD? 03' |  | -0.019 |
| 'RELATIONSHIP TO HEAD 81' |  | -0.019 |
| 'G34 AMT SOC SEC RCD 91' |  | -0.019 |
| 'R3/R13 WTR EARNINGS MAY 2003 05' |  | -0.019 |
| 'PERSON # OF FATHER' |  | -0.019 |
| 'H61E TYPE CURRENT HEALTH INS MEN 1 11' |  | -0.019 |
| 'MONTH MOVED IN/OUT 94' |  | -0.019 |
| 'COMPLETED EDUC-IND 90' |  | -0.019 |
| 'H61C MOS COVERED BY INSURANCE IN 06 07' |  | -0.019 |
| 'K33 AMT SOC SEC RCD 85' |  | -0.019 |
| 'WTR COVERED BY TANF PAYMENTS IN 2014 15' |  | -0.019 |
| '1983 INTERVIEW NUMBER' |  | -0.019 |
| 'TOTAL TRANSFER Y 76' |  | -0.019 |
| 'MONEY INCOME 70' |  | -0.019 |
| 'RESPONDENT? 81' |  | -0.019 |
| 'R16 WTR RECEIVED HELP FROM RELS IN 99 01' |  | -0.019 |
| 'YR S/O FAM FORMED 78' |  | -0.019 |
| 'WTR RECEIVED COLLEGE DEGREE 19' |  | -0.019 |
| 'SEQUENCE NUMBER 89' |  | -0.019 |
| 'SEQUENCE NUMBER 74' |  | -0.019 |
| 'G76 NUMBER OF JOBS IN PY 13' |  | -0.019 |
| 'WHETHER MOVED IN 68' |  | -0.019 |
| 'YEAR MOVED IN/OUT 72' |  | -0.019 |
| 'G33 TYPE SOC SEC RCD 09' |  | -0.019 |
| 'MO S/O FAM FORMED 69' |  | -0.019 |
| 'M34 PARTICIPATE EXTRACURRICULAR ACT 95' |  | -0.019 |
| 'MONTH LAST IN SCHOOL 09' |  | -0.019 |
| 'RELATION TO HEAD 13' |  | -0.019 |
| '2001 INTERVIEW NUMBER' |  | -0.019 |
| 'WEEKLY HOUSEWORK 86' |  | -0.019 |
| 'YEAR MOVED IN/OUT 97' |  | -0.019 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 11' |  | -0.02 |
| 'WTR CURRENTLY ENROLLED IN SCHOOL 17' |  | -0.02 |
| 'G31 TYPE SOC SEC RCD 86' |  | -0.02 |
| 'MONTH INDIVIDUAL BORN 11' |  | -0.02 |
| 'TOT TRANSFR EXC SS 87' |  | -0.02 |
| 'RELATIONSHIP TO HEAD 84' |  | -0.02 |
| 'WTR CURRENTLY ENROLLED IN SCHOOL 15' |  | -0.02 |
| 'G34 AMT SOC SEC RCD 88' |  | -0.02 |
| 'M18 REPEAT GRADE/SCHOOL RECOMMENDED 95' |  | -0.02 |
| 'YEAR LAST IN SCHOOL IF NEITHER 15' |  | -0.02 |
| 'G34 AMT SOC SEC RCD 05' |  | -0.02 |
| 'weight_15' |  | -0.02 |
| 'WEEKLY HOUSEWORK 85' |  | -0.02 |
| 'R27/R34/R42 WEEKS WORKED IN 1997 99' |  | -0.02 |
| 'H61G SN 1ST PERSON POLICY HOLDER 19' |  | -0.02 |
| 'TOT TRANSFER INC 79' |  | -0.02 |
| 'RESPONDENT? 73' |  | -0.02 |
| 'MONEY INCOME 69' |  | -0.02 |
| 'G34 AMT SOC SEC RCD 89' |  | -0.02 |
| 'R43 STATE WHERE RECD PUB ASSTNCE 2005 07' |  | -0.02 |
| 'ACC ANN UNEMP HR 80 81' |  | -0.02 |
| 'R4 WTR RECD GENERAL ASSISTANCE 1999 01' |  | -0.02 |
| 'YR S/O FAM FORMED 74' |  | -0.02 |
| 'M34A HOW OFTEN PARTIC EXTRACUR ACT 95' |  | -0.02 |
| 'R4 ASSET TYPE DIVIDEND 2003 05' |  | -0.02 |
| 'RESULT OF WELL-BEING IW ATTEMPT 16 15' |  | -0.02 |
| 'TRANSFER Y SOURCE 76' |  | -0.02 |
| 'RELATION TO HEAD 09' |  | -0.02 |
| 'RELATION TO HEAD 91' |  | -0.021 |
| 'H61G SN 2ND PERSON POLICY HOLDER 11' |  | -0.021 |
| 'RELATIONSHIP TO HEAD 71' |  | -0.021 |
| 'MONTH INDIVIDUAL BORN 07' |  | -0.021 |
| 'H61D3 WTR COVERED BY INSURANCE NOW 19' |  | -0.021 |
| 'EMPLOYMENT STATUS 95' |  | -0.021 |
| 'MONTH INDIVIDUAL BORN 93' |  | -0.021 |
| 'M12 HIGH SCHOOL GRAD, GED, OR NEITHER 95' |  | -0.021 |
| 'MONTH FIRST/ONLY MARRIAGE BEGAN' |  | -0.021 |
| 'H61C MOS COVERED BY INSURANCE IN 08 09' |  | -0.021 |
| 'M26 SUSPENDED OR EXPELLED FROM SCHOOL 95' |  | -0.021 |
| 'WTR CURRENTLY ENROLLED IN SCHOOL 13' |  | -0.021 |
| 'MONTH IND BORN 84' |  | -0.021 |
| 'H61E TYPE CURRENT HEALTH INS MEN 3 11' |  | -0.021 |
| 'R16 WTR RECEIVED HELP FROM RELS IN 97 99' |  | -0.021 |
| 'MONTH INDIVIDUAL BORN 88' |  | -0.021 |
| 'RESULT OF CDS TRANS-ADULT IW ATTEMPT 05' |  | -0.022 |
| 'M22 EVER ENROLLED IN HEAD START 95' |  | -0.022 |
| 'RELATION TO HEAD 90' |  | -0.022 |
| 'MONTH MOVED IN/OUT 97' |  | -0.022 |
| 'M17 ATTENDED SPEC CLASS/SCHL GIFTED 95' |  | -0.022 |
| 'YRS COMPLETED EDUCATION 93' |  | -0.022 |
| 'R26/R41 REPORTED ERNINGS TIME UNIT 01 03' |  | -0.022 |
| 'H61E TYPE CURRENT HEALTH INS MEN 2 19' |  | -0.022 |
| 'RELATIONSHIP TO HEAD 86' |  | -0.022 |
| 'R44 HOURS PER WEEK WORKED IN 2001 03' |  | -0.022 |
| 'EMPLOYMENT STATUS 07' |  | -0.022 |
| 'G34 AMT SOC SEC RCD 92' |  | -0.022 |
| 'TOTAL TRNSFR INCOME 86' |  | -0.022 |
| 'RELATIONSHIP TO HEAD 83' |  | -0.022 |
| 'RESPONDENT? 83' |  | -0.022 |
| 'ACC TOT TXBL Y 80 81' |  | -0.022 |
| 'RELATIONSHIP TO HEAD 85' |  | -0.022 |
| 'RELATION TO HEAD 93' |  | -0.022 |
| 'HEALTH GOOD? 15' |  | -0.022 |
| 'AGE OF INDIVIDUAL 93' |  | -0.022 |
| 'RELATIONSHIP TO HEAD 73' |  | -0.022 |
| 'RELATIONSHIP TO RESPONDENT 95' |  | -0.022 |
| 'IN SCHOOL 68' |  | -0.022 |
| 'MONEY INCOME 71' |  | -0.022 |
| 'MONTH INDIVIDUAL BORN 89' |  | -0.022 |
| 'YR S/O FAM FORMED 69' |  | -0.022 |
| 'RELATIONSHIP TO HEAD 72' |  | -0.022 |
| 'TOTAL TRNSFR INCOME 87' |  | -0.022 |
| 'UP: WTR CURRENTLY ENROLLED IN SCHOOL 19' |  | -0.022 |
| 'sex1_15' |  | -0.022 |
| 'TOTAL TRNSFR Y-IND 91' |  | -0.023 |
| 'G31 TYPE SOC SEC RCD 91' |  | -0.023 |
| 'TOT TRNSFR EXC SS-IND 88' |  | -0.023 |
| 'G84D_G94D IMPUTED WELFARE 07' |  | -0.023 |
| 'HR/WK HOUSEWORK 73' |  | -0.023 |
| 'COMPLETED EDUC-IND 88' |  | -0.023 |
| 'TYPE TRANSFER Y 81 82' |  | -0.023 |
| 'RESPONDENT? 71' |  | -0.023 |
| 'EMPLOYMENT STATUS 94' |  | -0.023 |
| 'weight_19' |  | -0.023 |
| 'YEAR LAST IN SCHOOL 01' |  | -0.023 |
| 'NEEDS EXTRA CARE? 77' |  | -0.023 |
| 'TRANSFER TYPE INC 75' |  | -0.023 |
| 'HEALTH GOOD? 94' |  | -0.023 |
| 'TOT ASSET INCOME-IND 91' |  | -0.023 |
| 'MAIN FAM ID FOR S/O 74' |  | -0.023 |
| '1975 INTERVIEW NUMBER' |  | -0.023 |
| 'H61E TYPE CURRENT HEALTH INS MEN 3 15' |  | -0.023 |
| 'R60 WTR RECD HELP FRM RELS/OTRS IN 03 05' |  | -0.024 |
| 'EMPLOYMENT STAT 85' |  | -0.024 |
| 'realcost_home_19' |  | -0.024 |
| 'cost_home_19' |  | -0.024 |
| 'MARITAL PAIRS INDICATOR 99' |  | -0.024 |
| 'MONEY INCOME 72' |  | -0.024 |
| 'YEAR LAST IN SCHOOL IF NEITHER 17' |  | -0.024 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 09' |  | -0.024 |
| 'HEALTH GOOD? 97' |  | -0.024 |
| 'WTR REC HS DIPLOMA/GED/NEITHER 13' |  | -0.024 |
| 'RELATIONSHIP TO HEAD 68' |  | -0.024 |
| 'YR S/O FAM FORMED 71' |  | -0.024 |
| 'TRANSFER INCOME 75' |  | -0.024 |
| 'WHETHER MOVED IN/OUT 70' |  | -0.024 |
| 'M7 MONTH LAST ATTENDED SCHOOL 95' |  | -0.024 |
| 'YEAR S/O FAM FORMED 03' |  | -0.024 |
| 'G34 ACC SOC SEC AMT 15' |  | -0.024 |
| 'MONTH INDIVIDUAL BORN 09' |  | -0.024 |
| 'M14 EVER ATTEND PRIVATE SCHOOL K-12 95' |  | -0.024 |
| 'time_shopping1_19' |  | -0.024 |
| 'R64 WTR RECD AMT ANYTHING ELSE IN 05 07' |  | -0.024 |
| 'WEEKLY HOUSEWORK 84' |  | -0.024 |
| 'EMPLOYMENT STATUS 96' |  | -0.024 |
| 'time_leisure1_17' |  | -0.025 |
| 'spouse2011' |  | -0.025 |
| 'UP: WTR ATTENDED SCHOOL SINCE LAST IW 19' |  | -0.025 |
| 'HRS/WK HOUSEWK 70' |  | -0.025 |
| 'RELATIONSHIP TO HEAD 70' |  | -0.025 |
| 'TOTAL TRNSFR INCOME 92' |  | -0.025 |
| 'SEQUENCE NUMBER 96' |  | -0.025 |
| 'RESPONDENT? 72' |  | -0.025 |
| 'STOP SCHOOL? 78' |  | -0.025 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 07' |  | -0.025 |
| 'RELATION TO HEAD 94' |  | -0.025 |
| 'YEAR FIRST/ONLY MARRIAGE BEGAN' |  | -0.025 |
| 'TYPE TRANSFER INC 79' |  | -0.025 |
| 'R16 WTR RECEIVED HELP FROM RELS IN 01 03' |  | -0.025 |
| 'RELATIONSHIP TO HEAD 69' |  | -0.025 |
| 'MO S/O FAM FORMED 71' |  | -0.025 |
| 'WTR RECEIVED COLLEGE DEGREE 15' |  | -0.025 |
| 'EMPLOYMENT STATUS 01' |  | -0.025 |
| 'WTR ELIG FOR WELL-BEING 2016 15' |  | -0.025 |
| 'WHETHER HEALTH LIMIT 78' |  | -0.025 |
| 'GRADE OF SCHOOL FINISHED IF NEITHER 19' |  | -0.025 |
| 'RESPONDENT? 03' |  | -0.026 |
| 'H61M MONTHS UNINSURED IN 13 15' |  | -0.026 |
| 'RELATION TO HEAD 05' |  | -0.026 |
| 'COMPLETED EDUCATION 72' |  | -0.026 |
| 'spouse2017' |  | -0.026 |
| 'spouse2015' |  | -0.026 |
| 'COMPLETED EDUC 84' |  | -0.026 |
| 'RESPONDENT? 70' |  | -0.026 |
| 'TOT TRANSFER Y 80 81' |  | -0.026 |
| 'H61B MOS COVERED BY INSURANCE IN 05 07' |  | -0.026 |
| 'M10 HIGHEST GRADE OR YEAR COMPLETED 95' |  | -0.026 |
| 'WHETHER SAMPLE OR NONSAMPLE' |  | -0.026 |
| 'UP: WTR ATTENDED SCHOOL SINCE LAST IW 17' |  | -0.026 |
| 'HR/WEEK HOUSEWORK 80' |  | -0.026 |
| 'ACC TOT TXBL Y 82 83' |  | -0.026 |
| 'COMPLETED EDUCATION 85' |  | -0.026 |
| 'H61 TYPE HEALTH INSURANCE MENTION 1 01' |  | -0.026 |
| 'WHETHER MEDICARE NUMBER GIVEN 05' |  | -0.026 |
| 'TYPE TRANSFER Y 80 81' |  | -0.027 |
| '1996 INTERVIEW NUMBER' |  | -0.027 |
| 'H61N MONTHS UNINSURED IN 14 15' |  | -0.027 |
| 'R21 WTR RECEIVED SOCL SECURITY IN 03 05' |  | -0.027 |
| 'RELATION TO HEAD 92' |  | -0.027 |
| 'time_housework1_19' |  | -0.027 |
| 'SEQUENCE NUMBER 77' |  | -0.027 |
| 'H1 HEALTH STATUS 95' |  | -0.027 |
| 'RESPONDENT? 69' |  | -0.027 |
| 'TOT TRANSFER Y 81 82' |  | -0.027 |
| 'HEALTH GOOD? 99' |  | -0.027 |
| 'WHETHER MOVED IN/OUT 77' |  | -0.027 |
| 'HEALTH GOOD? 95' |  | -0.028 |
| 'WHY FOLLOWABLE 93' |  | -0.028 |
| 'WHETHER MOVED IN/OUT 74' |  | -0.028 |
| 'COMPLETED EDUCATION 86' |  | -0.028 |
| 'WEEKLY HOUSEWORK 83' |  | -0.028 |
| 'SEQUENCE NUMBER 71' |  | -0.028 |
| 'WHETHER MEDICARE NUMBER GIVEN 07' |  | -0.028 |
| 'G34 AMT SOC SEC RCD 09' |  | -0.028 |
| 'H62 MOS COVERED BY INSURANCE IN 01 03' |  | -0.028 |
| 'MONTH INDIVIDUAL BORN 91' |  | -0.028 |
| 'R81A WTR REC SCHOOL BREAKFAST IN 2002 03' |  | -0.028 |
| 'WTR RECEIVED COLLEGE DEGREE 17' |  | -0.028 |
| 'time_leisure1_19' |  | -0.028 |
| 'EXTRA CARE? 76' |  | -0.028 |
| 'MONTH IND BORN 86' |  | -0.028 |
| 'TOTAL TRANSFER INCOME 93' |  | -0.028 |
| 'M33 TIMES FAM ASKED TALK SCHOOL BEHAV 95' |  | -0.028 |
| 'FOLLOW STATUS 01' |  | -0.028 |
| 'MONTH INDIVIDUAL BORN 94' |  | -0.028 |
| 'EMPLOYMENT STATUS 11' |  | -0.028 |
| 'MARITAL PAIRS INDICATOR 95' |  | -0.028 |
| 'HRS HOUSEWORK/WK 76' |  | -0.028 |
| 'TOTAL TRNSFR Y-IND 88' |  | -0.028 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 19' |  | -0.028 |
| 'H61D3 WTR COVERED BY INSURANCE NOW 15' |  | -0.028 |
| 'H61B MOS COVERED BY INSURANCE IN 07 09' |  | -0.028 |
| 'M27 EVER BOOKED/CHARGED BREAKING LAW 95' |  | -0.028 |
| 'R26 WTR RECEIVED NON-VA PENSION IN 05 07' |  | -0.028 |
| 'G33A WTR SOC SEC TYPE RETIREMENT 11' |  | -0.028 |
| 'LOOKING FOR WORK? 78' |  | -0.028 |
| 'HRS HOUSEWORK/WK 78' |  | -0.029 |
| 'WTR ATTENDED COLLEGE 15' |  | -0.029 |
| 'FOLLOW STATUS 90' |  | -0.029 |
| 'WTR ELIGIBLE FOR TA 19' |  | -0.029 |
| 'RELATION TO HEAD 89' |  | -0.029 |
| 'YEAR INDIVIDUAL BORN 13' |  | -0.029 |
| 'FOLLOW STATUS 92' |  | -0.029 |
| 'MONTH IND BORN 85' |  | -0.029 |
| 'H61E TYPE CURRENT HEALTH INS MEN 2 15' |  | -0.029 |
| 'MONTH INDIVIDUAL BORN 95' |  | -0.029 |
| 'INDIVIDUAL WEIGHT 82' |  | -0.029 |
| 'RELATIONSHIP TO HEAD 87' |  | -0.03 |
| 'ACC TOT TXBL Y 81 82' |  | -0.03 |
| 'H1 HEALTH STATUS 94' |  | -0.03 |
| 'WHY FOLLOWABLE 03' |  | -0.03 |
| 'YEAR IND BORN 83' |  | -0.03 |
| 'AGE OF INDIVIDUAL 15' |  | -0.03 |
| 'HRS HOUSEWORK/WK 77' |  | -0.03 |
| 'MONTH IND BORN 92' |  | -0.03 |
| 'AGE OF INDIVIDUAL 13' |  | -0.03 |
| 'G34 AMT SOC SEC RCD 07' |  | -0.03 |
| 'spouse2013' |  | -0.03 |
| 'STOPPED SCHOOL 73' |  | -0.03 |
| 'FOLLOW STATUS 91' |  | -0.03 |
| 'HOURS WORKED IND 68' |  | -0.03 |
| 'H32/35 WTR MEDICAID 86' |  | -0.03 |
| 'TYPE TRANSFER Y-IND 88' |  | -0.03 |
| 'COMPLETED EDUC 81' |  | -0.031 |
| 'STOP SCHOOL? 77' |  | -0.031 |
| 'YEAR INDIVIDUAL BORN 90' |  | -0.031 |
| 'MONTH INDIVIDUAL BORN 97' |  | -0.031 |
| 'WHO DID WORK? 72' |  | -0.031 |
| 'WTR ATTENDED COLLEGE 17' |  | -0.031 |
| 'STOP SCHOOL? 76' |  | -0.031 |
| 'RELATION TO HEAD 99' |  | -0.031 |
| 'COMPLETED EDUCATION 82' |  | -0.031 |
| 'HRS/WK HOUSEWRK 69' |  | -0.031 |
| 'INDIVIDUAL WEIGHT 79' |  | -0.032 |
| 'TOT TXBL INCOME 86' |  | -0.032 |
| 'MONEY INCOME 73' |  | -0.032 |
| 'G33A WTR SOC SEC TYPE RETIREMENT 13' |  | -0.032 |
| 'HOURS WORKED 72' |  | -0.032 |
| 'INDIVIDUAL WEIGHT 78' |  | -0.032 |
| 'EXTRA EARNER NR. 68' |  | -0.032 |
| 'RELATION TO HEAD 88' |  | -0.032 |
| 'INDIVIDUAL WEIGHT 80' |  | -0.032 |
| 'MONTH INDIVIDUAL BORN 05' |  | -0.032 |
| 'HRS/WK HSWK 71' |  | -0.032 |
| 'SEQUENCE NUMBER 70' |  | -0.032 |
| 'YEAR INDIVIDUAL BORN 15' |  | -0.032 |
| 'YEAR IND BORN 87' |  | -0.032 |
| 'MONTH LAST IN SCHOOL IF NEITHER 19' |  | -0.032 |
| 'SEQUENCE NUMBER 69' |  | -0.032 |
| 'weight_17' |  | -0.032 |
| 'UP: WTR CURRENTLY ENROLLED IN SCHOOL 17' |  | -0.032 |
| 'INDIVIDUAL WEIGHT 83' |  | -0.032 |
| 'STOPPED SCHOOL 71' |  | -0.032 |
| 'AGE OF INDIVIDUAL 11' |  | -0.033 |
| 'STOP SCHOOL? 74' |  | -0.033 |
| 'WHY FOLLOWABLE 19' |  | -0.033 |
| 'DISABLED OR REQ CR 71' |  | -0.033 |
| 'AGE OF INDIVIDUAL 07' |  | -0.033 |
| 'EMPLOYMENT STATUS 13' |  | -0.033 |
| 'YEAR INDIVIDUAL BORN 07' |  | -0.033 |
| 'MONTH INDIVIDUAL BORN 99' |  | -0.033 |
| 'INDIVIDUAL WEIGHT 77' |  | -0.033 |
| 'MAIN FAM ID FOR S/O 93' |  | -0.033 |
| 'YEAR INDIVIDUAL BORN 11' |  | -0.033 |
| 'STOPPED SCHOOL? 75' |  | -0.033 |
| 'time_volunteering1_19' |  | -0.033 |
| 'M7 YEAR LAST ATTENDED SCHOOL 95' |  | -0.034 |
| 'TOT TXBL INCOME-IND 88' |  | -0.034 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 99' |  | -0.034 |
| 'MONTH INDIVIDUAL BORN 03' |  | -0.034 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 97' |  | -0.034 |
| 'WHETHER HEALTH SUPP RECD 91' |  | -0.034 |
| 'MARITAL PAIRS INDICAT 94' |  | -0.034 |
| 'MARITAL PAIRS INDICATOR 97' |  | -0.034 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 05' |  | -0.034 |
| 'YEAR IND BORN 84' |  | -0.034 |
| 'HR/WEEK ON HOUSEWRK 81' |  | -0.034 |
| 'FOLLOW STATUS 93' |  | -0.034 |
| 'MONTH INDIVIDUAL BORN 96' |  | -0.034 |
| 'INDIVIDUAL WEIGHT 73' |  | -0.034 |
| 'time_adultcare1_19' |  | -0.034 |
| 'WTR ELIGIBLE FOR DUST 09' |  | -0.034 |
| 'INDIVIDUAL WEIGHT 81' |  | -0.034 |
| 'COMPLETED EDUCATION 83' |  | -0.034 |
| 'ANN WORK HRS-IND 89' |  | -0.034 |
| 'TOTAL TAXABLE Y 76' |  | -0.034 |
| 'YEAR INDIVIDUAL BORN 89' |  | -0.034 |
| 'TOT ANN HRS 74' |  | -0.034 |
| 'STOPPED SCHOOL 70' |  | -0.035 |
| 'H62A MOS COVERED BY INSURANCE IN 02 03' |  | -0.035 |
| 'AGE OF INDIVIDUAL 09' |  | -0.035 |
| 'MONTH INDIVIDUAL BORN 01' |  | -0.035 |
| 'ANN WORK HRS 86' |  | -0.035 |
| 'STOPPED SCHOOL 69' |  | -0.035 |
| 'M3 CURRENTLY ATTENDING SCHOOL 95' |  | -0.035 |
| 'RELATION TO HEAD 96' |  | -0.035 |
| 'YEAR INDIVIDUAL BORN 88' |  | -0.035 |
| 'YEAR LAST IN SCHOOL IF NEITHER 19' |  | -0.035 |
| 'WTR HCB RECORD FOR DAD 93' |  | -0.035 |
| 'ANN WORK HRS 87' |  | -0.035 |
| 'STATUS OF FIRST/ONLY MARRIAGE' |  | -0.036 |
| 'EDUCATION ATTAINED 80' |  | -0.036 |
| 'STOPPED SCHOOL 72' |  | -0.036 |
| 'RELATION TO HEAD 95' |  | -0.036 |
| 'RELATION TO HEAD 97' |  | -0.036 |
| 'TYPE TXBL INCOME 84' |  | -0.036 |
| 'RESPONDENT? 99' |  | -0.036 |
| 'INDIVIDUAL WEIGHT 84' |  | -0.036 |
| 'HEALTH GOOD? 01' |  | -0.036 |
| 'AGE OF INDIVIDUAL 05' |  | -0.036 |
| 'WHY FOLLOWABLE 99' |  | -0.036 |
| 'INDIVIDUAL WEIGHT 76' |  | -0.036 |
| 'TOT TXBL INCOME 87' |  | -0.036 |
| 'TOT TXBL INCOME-IND 89' |  | -0.036 |
| 'YEAR IND BORN 86' |  | -0.036 |
| 'INDIVIDUAL WEIGHT 74' |  | -0.036 |
| 'ANN WORK HRS 92' |  | -0.037 |
| 'LAST KNOWN MARITAL STATUS' |  | -0.037 |
| 'TYPE OF INCOME 69' |  | -0.037 |
| 'YRS SCHL COMPL 68' |  | -0.037 |
| 'MARITAL PAIRS INDICATOR 96' |  | -0.037 |
| 'TOT LABOR INCOME 92' |  | -0.037 |
| 'MARITAL INDICATOR-IND 88' |  | -0.037 |
| 'H11 HD MED COVERAGE? 87' |  | -0.037 |
| 'YEAR IND BORN 85' |  | -0.037 |
| 'INDIVIDUAL WEIGHT 75' |  | -0.037 |
| 'EMPLOYMENT STATUS 17' |  | -0.037 |
| 'MARITAL INDICATOR-IND 91' |  | -0.037 |
| 'MONEY INCOME IND 68' |  | -0.037 |
| 'FOLLOW STATUS 94' |  | -0.037 |
| 'FOLLOW STATUS 95' |  | -0.037 |
| 'HOURS WORKED 73' |  | -0.037 |
| 'TYPE OF INCOME 71' |  | -0.037 |
| 'H5 OFUM MED COVERAGE? 90' |  | -0.037 |
| 'HIGHEST GRADE FINISH 77' |  | -0.037 |
| 'MARITAL INDICATOR-IND 89' |  | -0.037 |
| 'TOT LABOR INCOME-IND 91' |  | -0.037 |
| 'DISABLED OR RQ CARE 69' |  | -0.037 |
| 'FOLLOW STATUS 99' |  | -0.038 |
| 'ANN WORK HRS-IND 88' |  | -0.038 |
| 'H5 OFUM MED COVERAGE? 89' |  | -0.038 |
| 'WHY FOLLOWABLE 01' |  | -0.038 |
| 'YEAR INDIVIDUAL BORN 09' |  | -0.038 |
| 'INDIVIDUAL WEIGHT 71' |  | -0.038 |
| 'MARITAL PAIRS INDICATOR 93' |  | -0.038 |
| 'COMBINED IND WEIGHT 95' |  | -0.038 |
| 'LIKELY TO MOVE 68' |  | -0.038 |
| 'DISABLED OR RQ CARE 70' |  | -0.038 |
| 'ANN WORK HRS-IND 90' |  | -0.038 |
| 'TYPE TXBL INCOME 88' |  | -0.038 |
| 'H62 MOS COVERED BY INSURANCE IN 99 01' |  | -0.038 |
| 'DISABLED OR REQ CR 72' |  | -0.038 |
| 'MARR PAIRS INDICATOR 83' |  | -0.039 |
| 'WHETHER SELECTED FOR DUST 09' |  | -0.039 |
| 'MARITAL INDICATOR-IND 90' |  | -0.039 |
| 'TOTAL ANNUAL WORK HRS 93' |  | -0.039 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 03' |  | -0.039 |
| 'WTR REC HS DIPLOMA/GED/NEITHER 19' |  | -0.039 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 13' |  | -0.039 |
| 'MARR PAIRS INDICATOR 87' |  | -0.039 |
| 'HRS HSWRK 79' |  | -0.04 |
| 'TYPE TXBL INCOME 82 83' |  | -0.04 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 07' |  | -0.04 |
| 'WHY FOLLOWABLE 96' |  | -0.04 |
| 'H25 IND MED COVERAGE? 92' |  | -0.04 |
| 'TOT TXBL INCOME 82 83' |  | -0.04 |
| 'RESPONDENT? 01' |  | -0.04 |
| 'INDIVIDUAL WEIGHT 85' |  | -0.04 |
| 'MARR PAIRS INDICATOR 86' |  | -0.04 |
| 'TOTAL LABOR INCOME 93' |  | -0.04 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 17' |  | -0.04 |
| 'H5 IND MED COVERAGE? 91' |  | -0.04 |
| 'SEX OF INDIVIDUAL' |  | -0.04 |
| 'sex1_19' |  | -0.04 |
| 'H1 HEALTH STATUS 96' |  | -0.04 |
| 'WHY FOLLOWABLE 94' |  | -0.04 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 11' |  | -0.041 |
| 'TYPE TXBL INCOME 89' |  | -0.041 |
| 'INDIVIDUAL WEIGHT 86' |  | -0.041 |
| 'INDIVIDUAL WEIGHT 70' |  | -0.041 |
| 'RETND SELF ADMIN QNAIRE 90' |  | -0.041 |
| 'YEAR INDIVIDUAL BORN 93' |  | -0.041 |
| 'MARR PAIRS INDICATOR 92' |  | -0.041 |
| 'INDIVIDUAL WEIGHT 72' |  | -0.041 |
| 'G34 AMT SOC SEC RCD 11' |  | -0.041 |
| 'AGE OF INDIVIDUAL 03' |  | -0.041 |
| 'INDIVIDUAL WEIGHT 68' |  | -0.041 |
| 'YEAR INDIVIDUAL BORN 91' |  | -0.041 |
| 'SHARE EXPENSES 68' |  | -0.042 |
| 'HAS MEDICAL COVERAGE? 94' |  | -0.042 |
| 'COMBO IND WEIGHT 94' |  | -0.042 |
| 'HRS WORKED IN 68 69' |  | -0.042 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 09' |  | -0.042 |
| 'HAS MEDICAL COVERAGE? 96' |  | -0.042 |
| 'AGE FROM BIRTH DATE 88' |  | -0.042 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 15' |  | -0.042 |
| 'FOLLOW STATUS 96' |  | -0.042 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 99' |  | -0.042 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 97' |  | -0.042 |
| 'MARR PAIRS INDICATOR 68' |  | -0.042 |
| 'H5 OFUM MED COVERAGE? 88' |  | -0.042 |
| 'TOT TXBL INCOME 84' |  | -0.042 |
| 'AGE FROM BIRTH DATE 83' |  | -0.042 |
| 'WHY FOLLOWABLE 17' |  | -0.042 |
| 'TOT TXBL INCOME 85' |  | -0.042 |
| 'ANN WORK HRS 85' |  | -0.043 |
| 'EMPLOYMENT STATUS 15' |  | -0.043 |
| 'WTR REC HS DIPLOMA/GED/NEITHER 15' |  | -0.043 |
| 'ANN WORK HRS-IND 91' |  | -0.043 |
| 'RELATION TO HEAD 01' |  | -0.043 |
| 'FOLLOW STATUS 97' |  | -0.043 |
| 'AGE FROM BIRTH DATE 90' |  | -0.044 |
| 'INDIVIDUAL WEIGHT 69' |  | -0.044 |
| 'TYPE TXBL INCOME 86' |  | -0.044 |
| 'H62A MOS COVERED BY INSURANCE IN 00 01' |  | -0.044 |
| 'COMBINED IND WEIGHT 93' |  | -0.044 |
| 'AGE FROM BIRTH DATE 87' |  | -0.044 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 05' |  | -0.044 |
| 'TYPE TXBL INC BUILT 92' |  | -0.044 |
| 'WHETHER MEDICARE NUMBER GIVEN 09' |  | -0.044 |
| 'AGE OF INDIVIDUAL 99' |  | -0.044 |
| 'WHETHER ELIG PARENT 91' |  | -0.044 |
| 'TOT TXBL INCOME 81 82' |  | -0.044 |
| 'TYPE TXBL INCOME 81 82' |  | -0.044 |
| 'WHY FOLLOWABLE 97' |  | -0.044 |
| 'TOTAL TAXABLE INCOM 78' |  | -0.044 |
| 'ANN WORK HRS 82 83' |  | -0.045 |
| 'YEAR IND BORN 92' |  | -0.045 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 03' |  | -0.045 |
| 'YEAR INDIVIDUAL BORN 05' |  | -0.045 |
| 'TYPE TXBL INCOME 1980 81' |  | -0.045 |
| 'HAS MEDICAL COVERAGE? 93' |  | -0.045 |
| 'WHY FOLLOWABLE 95' |  | -0.045 |
| 'WHY FOLLOWABLE 13' |  | -0.045 |
| 'ETHNICITY ELIGIBILITY FOR LNPS' |  | -0.045 |
| 'G33A WTR SOC SEC TYPE SURVIVOR 11' |  | -0.045 |
| 'MARR PAIRS INDICATOR 70' |  | -0.045 |
| 'G33A WTR SOC SEC TYPE DEP OF DISABLED 11' |  | -0.045 |
| 'TOT TXBL INCOME-IND 90' |  | -0.045 |
| 'CORE INDIVIDUAL LONGITUDINAL WEIGHT 93' |  | -0.045 |
| 'EMPLOYMENT STATUS 19' |  | -0.045 |
| 'INDIVIDUAL WEIGHT 87' |  | -0.045 |
| 'H62A MOS COVERED BY INSURANCE IN 98 99' |  | -0.045 |
| 'K49 EDUCATION 79' |  | -0.045 |
| 'MARR PAIRS INDICATOR 84' |  | -0.045 |
| 'CORE IND WEIGHT 91' |  | -0.045 |
| 'YEAR INDIVIDUAL BORN 94' |  | -0.046 |
| 'MARR PAIRS INDICATOR 69' |  | -0.046 |
| 'CORE/IMM INDIVIDUAL CROSS-SECTION WT 01' |  | -0.046 |
| 'G33A WTR SOC SEC TYPE DEP OF RETIRED 11' |  | -0.046 |
| 'WHY FOLLOWABLE 07' |  | -0.046 |
| 'WHY FOLLOWABLE 15' |  | -0.046 |
| 'MARR PAIRS INDICATOR 85' |  | -0.046 |
| 'TYPE TXBL INCOME 87' |  | -0.046 |
| 'CORE INDIVIDUAL LONGITUDINAL WEIGHT 94' |  | -0.046 |
| 'COMBINED IND WEIGHT 91' |  | -0.046 |
| 'TYPE OF INCOME 70' |  | -0.046 |
| 'G33A WTR SOC SEC TYPE OTHER 11' |  | -0.046 |
| 'WHY FOLLOWABLE 09' |  | -0.046 |
| 'AGE FROM BIRTH DATE 89' |  | -0.047 |
| 'INDIVIDUAL WEIGHT 89' |  | -0.047 |
| 'TAXABLE INCOME 75' |  | -0.047 |
| 'CORE IND WEIGHT 92' |  | -0.047 |
| 'TYPE TXBL INCOME 85' |  | -0.047 |
| 'WHY FOLLOWABLE 11' |  | -0.047 |
| 'INDIVIDUAL WEIGHT 88' |  | -0.047 |
| 'YEAR INDIVIDUAL BORN 03' |  | -0.047 |
| 'TOT TXBL INCOME 80 81' |  | -0.047 |
| 'AGE FROM BIRTH DATE 84' |  | -0.047 |
| 'AGE FROM BIRTH DATE 86' |  | -0.047 |
| 'AGE OF INDIVIDUAL 01' |  | -0.047 |
| 'G33A WTR SOC SEC TYPE DISABILITY 11' |  | -0.047 |
| 'COMBINED IND WEIGHT 92' |  | -0.047 |
| 'CORE IND WEIGHT 90' |  | -0.048 |
| 'HAS MEDICAL COVERAGE? 97' |  | -0.048 |
| 'HAS MEDICAL COVERAGE? 95' |  | -0.048 |
| 'CORE INDIVIDUAL LONGITUDINAL WEIGHT 95' |  | -0.048 |
| 'G33A WTR SOC SEC TYPE DISABILITY 13' |  | -0.048 |
| 'G33A WTR SOC SEC TYPE RETIREMENT 15' |  | -0.048 |
| 'AGE OF INDIVIDUAL 82' |  | -0.048 |
| 'CORE/IMM INDIVIDUAL LONGITUDINAL WT 01' |  | -0.048 |
| 'AGE OF INDIVIDUAL 83' |  | -0.048 |
| 'AGE OF INDIVIDUAL 86' |  | -0.048 |
| 'WTR HCB RECORD FOR MOM 93' |  | -0.048 |
| 'TYPE TAXABLE Y 1979 80' |  | -0.048 |
| 'G34 AMT SOC SEC RCD 13' |  | -0.048 |
| 'COMBINED IND WEIGHT 90' |  | -0.048 |
| 'AGE OF INDIVIDUAL 84' |  | -0.049 |
| 'AGE OF INDIVIDUAL 89' |  | -0.049 |
| 'TYPE TXBL INCOME 91' |  | -0.049 |
| 'WHY FOLLOWABLE 05' |  | -0.049 |
| 'TYPE OF INCOME 68' |  | -0.049 |
| 'TYPE OF INCOME 72' |  | -0.049 |
| 'G33A WTR SOC SEC TYPE DEP OF DISABLED 13' |  | -0.049 |
| 'WHETHER MEDICARE NUMBER GIVEN 13' |  | -0.049 |
| 'LABOR/ASSET TYPE INC 75' |  | -0.049 |
| 'CORE INDIVIDUAL LONGITUDINAL WEIGHT 96' |  | -0.049 |
| 'TOT TAXABLE INCOME 79' |  | -0.049 |
| 'ANN WORK HRS 84' |  | -0.049 |
| 'G33A WTR SOC SEC TYPE RETIREMENT 19' |  | -0.049 |
| 'ANN WORK HRS 80 81' |  | -0.049 |
| 'WTR REC HS DIPLOMA/GED/NEITHER 17' |  | -0.049 |
| 'AGE OF INDIVIDUAL 85' |  | -0.049 |
| 'AGE FROM BIRTH DATE 85' |  | -0.05 |
| 'AGE OF INDIVIDUAL 81' |  | -0.05 |
| 'ANN WORK HRS 81 82' |  | -0.05 |
| 'AGE OF INDIVIDUAL 87' |  | -0.05 |
| 'G33A WTR SOC SEC TYPE RETIREMENT 17' |  | -0.05 |
| 'AGE OF INDIVIDUAL 90' |  | -0.05 |
| 'AGE OF INDIVIDUAL 79' |  | -0.05 |
| 'MARR PAIRS INDICATOR 71' |  | -0.05 |
| 'YEAR INDIVIDUAL BORN 97' |  | -0.05 |
| 'AGE OF INDIVIDUAL 80' |  | -0.05 |
| 'AGE OF INDIVIDUAL 97' |  | -0.05 |
| 'YEAR INDIVIDUAL BORN 95' |  | -0.05 |
| 'WHETHER MEDICARE NUMBER GIVEN 11' |  | -0.05 |
| 'AGE OF INDIVIDUAL 88' |  | -0.05 |
| 'G33A WTR SOC SEC TYPE DEP OF RETIRED 13' |  | -0.051 |
| 'H62 MOS COVERED BY INSURANCE IN 97 99' |  | -0.051 |
| 'YEAR INDIVIDUAL BORN 99' |  | -0.051 |
| 'AGE OF INDIVIDUAL 78' |  | -0.051 |
| 'TYPE OF INCOME 73' |  | -0.052 |
| 'TYPE OF INCOME 74' |  | -0.052 |
| 'G33A WTR SOC SEC TYPE OTHER 13' |  | -0.052 |
| 'AGE OF INDIVIDUAL 77' |  | -0.053 |
| 'TYPE TXBL INCOME 90' |  | -0.053 |
| 'TYPE TAXABLE INCOME 79' |  | -0.053 |
| 'MARR PAIRS INDICATOR 81' |  | -0.053 |
| 'TAXABLE Y SOURCE 76' |  | -0.053 |
| 'AGE FROM BIRTH DATE 91' |  | -0.053 |
| 'AGE OF INDIVIDUAL 92' |  | -0.054 |
| 'AGE OF INDIVIDUAL 74' |  | -0.054 |
| 'YEAR INDIVIDUAL BORN 96' |  | -0.054 |
| 'AGE OF INDIVIDUAL 75' |  | -0.054 |
| 'HOURS WORKED 70' |  | -0.054 |
| 'AGE OF INDIVIDUAL 91' |  | -0.054 |
| 'AGE OF INDIVIDUAL 94' |  | -0.054 |
| 'AGE OF INDIVIDUAL 76' |  | -0.054 |
| 'AGE OF INDIVIDUAL 73' |  | -0.054 |
| 'HIGHEST GRAD FINISHED 75' |  | -0.054 |
| 'AGE FROM BIRTH DATE 92' |  | -0.054 |
| 'LIKELY TO MOVE OUT 69' |  | -0.054 |
| 'H5N3/H50C WTR CHNGE INTEREST ACTVTIES 19' |  | -0.055 |
| 'WHETHER MEDICARE NUMBER GIVEN 17' |  | -0.055 |
| 'TOTAL TAXABLE Y 77' |  | -0.055 |
| '1979 TOT TAXABLE Y 80' |  | -0.055 |
| 'HOURS WORKED 71' |  | -0.055 |
| 'MARR PAIRS INDICATOR 82' |  | -0.055 |
| 'AGE OF INDIVIDUAL 95' |  | -0.055 |
| 'HOURS WORKED IN 1979 80' |  | -0.055 |
| 'AGE OF INDIVIDUAL 72' |  | -0.055 |
| 'HOURS WORKED IN 77 78' |  | -0.056 |
| 'TYPE TAXABLE INCOM 78' |  | -0.056 |
| 'MARR PAIRS INDICATOR 72' |  | -0.056 |
| 'YEAR INDIVIDUAL BORN 01' |  | -0.056 |
| 'MARR PAIRS INDICATOR 75' |  | -0.057 |
| 'AGE OF INDIVIDUAL 68' |  | -0.057 |
| 'H5N4/H50D WTR CHNGE REPEATNG STORIES 19' |  | -0.057 |
| 'AGE OF INDIVIDUAL 96' |  | -0.057 |
| 'WTR ENDORSED 2+ MEMORY PROBLEMS 19' |  | -0.057 |
| 'WHETHER MEDICARE NUMBER GIVEN 19' |  | -0.057 |
| 'MARR PAIRS INDICATOR 76' |  | -0.057 |
| 'H5N5/H50E WTR CHNGE LEARNING/USE TOOLS19' |  | -0.057 |
| 'AGE OF INDIVIDUAL 69' |  | -0.057 |
| 'AGE OF INDIVIDUAL 70' |  | -0.057 |
| 'AGE OF INDIVIDUAL 71' |  | -0.058 |
| 'HRS WORKED IN 74 75' |  | -0.058 |
| 'H5N9/H50I WTR CHNGE IN THINKING/MEMORY19' |  | -0.058 |
| 'G33A WTR SOC SEC TYPE SURVIVOR 13' |  | -0.058 |
| 'G33A WTR SOC SEC TYPE DISABILITY 15' |  | -0.058 |
| 'H5N8/H50H WTR CHNGE REMEMBERING APPTS 19' |  | -0.058 |
| 'SHARE EXPENSES 69' |  | -0.058 |
| 'TAXABLE Y SOURCE 77' |  | -0.059 |
| 'MARR PAIRS INDICATOR 77' |  | -0.059 |
| 'H5N6/H50F WTR CHNGE REMEMBERING DATES 19' |  | -0.059 |
| 'TOT HRS WRKD 78 79' |  | -0.059 |
| 'MARR PAIRS INDICATOR 73' |  | -0.059 |
| 'H5N2/H50B WTR CHNGE MAKING DECISIONS 19' |  | -0.059 |
| 'H5N3/H50C WTR CHNGE INTEREST ACTVTIES 17' |  | -0.059 |
| 'H5N7/H50G WTR CHNGE HNDLNG MONEY ISSUE19' |  | -0.059 |
| 'MARR PAIRS INDICATOR 78' |  | -0.06 |
| 'H5N4/H50D WTR CHNGE REPEATNG STORIES 17' |  | -0.06 |
| 'MARR PAIRS INDICATOR 74' |  | -0.06 |
| 'MARR PAIRS INDICATOR 79' |  | -0.06 |
| 'H5N9/H50I WTR CHNGE IN THINKING/MEMORY17' |  | -0.06 |
| 'G34 AMT SOC SEC RCD 15' |  | -0.061 |
| 'WHETHER MEDICARE NUMBER GIVEN 15' |  | -0.061 |
| 'LIKELY TO MOVE OUT 71' |  | -0.061 |
| 'MARR PAIRS INDICATOR 80' |  | -0.061 |
| 'HRS WORKED LAST YR 77' |  | -0.061 |
| 'H5N8/H50H WTR CHNGE REMEMBERING APPTS 17' |  | -0.062 |
| 'LIKELY TO MOVE OUT 70' |  | -0.062 |
| 'G33A WTR SOC SEC TYPE SURVIVOR 15' |  | -0.062 |
| 'WTR ENDORSED 2+ MEMORY PROBLEMS 17' |  | -0.063 |
| 'H5N5/H50E WTR CHNGE LEARNING/USE TOOLS17' |  | -0.063 |
| 'HIGHEST GRADE FINISH 76' |  | -0.063 |
| 'WTR WELFARE INCOME 74' |  | -0.063 |
| 'G33A WTR SOC SEC TYPE DEP OF DISABLED 15' |  | -0.063 |
| 'HRS WRKED LAST YR 76' |  | -0.063 |
| 'H5N7/H50G WTR CHNGE HNDLNG MONEY ISSUE17' |  | -0.063 |
| 'G33A WTR SOC SEC TYPE DEP OF RETIRED 15' |  | -0.064 |
| 'HIGHEST GRADE FINISH 78' |  | -0.064 |
| 'H5N2/H50B WTR CHNGE MAKING DECISIONS 17' |  | -0.064 |
| 'G33A WTR SOC SEC TYPE OTHER 15' |  | -0.064 |
| 'H5N6/H50F WTR CHNGE REMEMBERING DATES 17' |  | -0.065 |
| 'LIKELY TO MOVE OUT 72' |  | -0.065 |
| 'G33A WTR SOC SEC TYPE SURVIVOR 19' |  | -0.065 |
| 'SHARE EXPENSES 71' |  | -0.065 |
| 'G33A WTR SOC SEC TYPE OTHER 19' |  | -0.067 |
| 'G33A WTR SOC SEC TYPE SURVIVOR 17' |  | -0.068 |
| 'SHARE EXPENSES? 72' |  | -0.068 |
| 'SHARE EXPENSES 70' |  | -0.068 |
| 'G33A WTR SOC SEC TYPE DISABILITY 19' |  | -0.068 |
| 'G33A WTR SOC SEC TYPE DEP OF DISABLED 19' |  | -0.069 |
| 'G33A WTR SOC SEC TYPE DEP OF RETIRED 19' |  | -0.069 |
| 'G33A WTR SOC SEC TYPE DISABILITY 17' |  | -0.071 |
| 'G33A WTR SOC SEC TYPE DEP OF DISABLED 17' |  | -0.072 |
| 'G33A WTR SOC SEC TYPE DEP OF RETIRED 17' |  | -0.072 |
| 'G33A WTR SOC SEC TYPE OTHER 17' |  | -0.073 |
| 'G34 AMT SOC SEC RCD 19' |  | -0.074 |
| 'G34 AMT SOC SEC RCD 17' |  | -0.076 |

</details>





<!--

I was going to include a section where I look at correlations among those who have non-zero commute time.
But the lists look very similar.
Seems not worth the effort until after expanding the family file processing.

<details markdown="block"><summary>Click for full list of correlations.</summary>

Note as of 2023 April 14: Minimal processing has been done. So some of these, especially near the bottom are "correlations" on categorical data which is just coded with numbers. These have no actually meaning.

| Variable Name | Description (TODO) | Correlation |
|:--|:--|:-:|


</details>-->






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






















### LASSO on time spent commuting.

Commuting here is defined using the [anchor method with a dwell time of 30](https://www.bls.gov/opub/mlr/2018/article/what-is-the-impact-of-recoding-travel-activities-in-the-american-time-use-survey.htm).

<!--Sample was those in the leave module.-->


Biggest positive predictors of having days where you work from home:
- Being employed and working.
- working in construction/extraction
- having high weekly earnings
- Having at least one child under the age of 13
- not working for a family business?
- having a cleaning/maintainance occupation

Biggest negative predictors
- diary day on the weekend
- diary day on a holiday
- having a job but being absent from that job
- working in the "membership associations and organizations" industry
- working in the agriculture industry

<details markdown="block"><summary>Click for full list of coeficients.</summary>

| Variable Name | coef |
|:-:|:-:|| day_sunday | -0.519 |
| day_saturday | -0.49 |
| holiday_yes | -0.266 |
| empstat_employed - absent | -0.15 |
| ind2_membership associations and organizations | -0.082 |
| ind2_agriculture | -0.069 |
| clwkr_government, local | -0.06 |
| occ2_protective service occupations | -0.059 |
| fullpart_part time | -0.057 |
| occ2_education, training, and library occupations | -0.052 |
| fambus_family business | -0.048 |
| occ2_personal care and service occupations | -0.035 |
| ind2_educational services | -0.032 |
| day_friday | -0.032 |
| citizen_native, born in united states | -0.032 |
| occ2_healthcare practitioner and technical occupations | -0.03 |
| educyrs_bachelor's degree | -0.027 |
| occ2_transportation and material moving occupations | -0.024 |
| housetype_house, apartment, flat | -0.023 |
| kid6to12_yes | -0.022 |
| ind2_transportation and warehousing | -0.021 |
| occ2_computer and mathematical science occupations | -0.021 |
| month_november | -0.02 |
| month_june | -0.019 |
| statefip_texas | -0.019 |
| paidhour_paid hourly | -0.017 |
| clwkr_private, nonprofit | -0.017 |
| hhtenure_occupied without payment of cash rent | -0.016 |
| occ2_community and social service occupations | -0.015 |
| ind2_primary metals and fabricated metal products | -0.014 |
| race_white only | -0.012 |
| ind2_real estate | -0.012 |
| metro_nonmetropolitan | -0.012 |
| ind2_social assistance | -0.012 |
| region_midwest | -0.011 |
| kidund1_yes | -0.011 |
| statefip_new mexico | -0.011 |
| famincome_$150,000 and over | -0.01 |
| month_december | -0.009 |
| educyrs_college--four years | -0.009 |
| famincome_refused | -0.009 |
| msasize_not identified or non-metropolitan | -0.008 |
| speduc_bachelor's degree (ba, ab, bs, etc.) | -0.007 |
| month_july | -0.006 |
| schlcoll_college/university part time | -0.006 |
| schlcoll_college/university full time | -0.005 |
| msasize_250,000 - 499,999 | -0.005 |
| spusualhrs | -0.005 |
| marst_divorced | -0.005 |
| metro_metropolitan, not identified | -0.005 |
| educyrs_twelfth grade | -0.004 |
| speduc_7th or 8th grade | -0.004 |
| statefip_utah | -0.003 |
| statefip_rhode island | -0.003 |
| ind2_paper manufacturing and printing | -0.003 |
| vetstat_non-veteran | -0.003 |
| occ2_management occupations | -0.003 |
| month_may | -0.002 |
| educyrs_doctoral degree | -0.002 |
| otpay | -0.002 |
| ind2_professional, scientific, and technical services | -0.001 |
| statefip_oregon | -0.001 |
| sprace_white only | -0.001 |
| statefip_arkansas | -0.0 |
| multjobs_no | -0.0 |
| statefip_ohio | -0.0 |
| speduc_master's degree (ma, ms, meng, med, msw, etc.) | -0.0 |
| citizen_native, born abroad of american parent or parents | -0.0 |
| citizen_native, born in puerto rico or u.s. outlying area | -0.0 |
| clwkr_government, state | 0.0 |
| clwkr_niu (not in universe) | 0.0 |
| clwkr_private, for profit | -0.0 |
| clwkr_self-employed, unincorporated | 0.0 |
| day_monday | 0.0 |
| earnweek | 0.0 |
| educyrs_college--one year | -0.0 |
| educyrs_college--three years | -0.0 |
| educyrs_college--two years | -0.0 |
| educyrs_first through fourth grade | 0.0 |
| educyrs_less than first grade | 0.0 |
| educyrs_master's degree | 0.0 |
| educyrs_master's degree--one year program | 0.0 |
| educyrs_master's degree--two year program | -0.0 |
| educyrs_professional degree | -0.0 |
| educyrs_seventh through eighth grade | -0.0 |
| empstat_not in labor force | -0.0 |
| empstat_unemployed - looking | -0.0 |
| empstat_unemployed - on layoff | 0.0 |
| fambus_no family business | 0.0 |
| fambus_pay_no | -0.0 |
| famincome_$10,000 to $12,499 | 0.0 |
| famincome_$100,000 to $149,999 | 0.0 |
| famincome_$15,000 to $19,999 | -0.0 |
| famincome_$20,000 to $24,999 | -0.0 |
| famincome_$25,000 to $29,999 | 0.0 |
| famincome_$35,000 to $39,999 | -0.0 |
| famincome_$40,000 to $49,999 | -0.0 |
| famincome_$5,000 to $7,499 | 0.0 |
| famincome_$50,000 to $59,999 | -0.0 |
| famincome_$60,000 to $74,999 | -0.0 |
| famincome_don't know | 0.0 |
| fullpart_niu (not in universe) | -0.0 |
| hh_numkids | 0.0 |
| hh_numownkids | 0.0 |
| hhtenure_owned or being bought by a household member | 0.0 |
| housetype_mobile home or trailer with 1 or more rooms added | 0.0 |
| housetype_mobile home or trailer with no permanent room added | -0.0 |
| ind2_arts, entertainment, and recreation | 0.0 |
| ind2_beverage and tobacco product mfg | 0.0 |
| ind2_broadcasting (except internet) | -0.0 |
| ind2_chemical manufacturing | -0.0 |
| ind2_computer and electronic product mfg | -0.0 |
| ind2_electrical equipment, appliance mfg | 0.0 |
| ind2_finance | 0.0 |
| ind2_food manufacturing | 0.0 |
| ind2_furniture and fixtures manufacturing | -0.0 |
| ind2_health care services, except hospitals | 0.0 |
| ind2_hospitals | 0.0 |
| ind2_machinery manufacturing | -0.0 |
| ind2_mining | 0.0 |
| ind2_miscellaneous and not specified mfg | -0.0 |
| ind2_motion picture and sound recording industries | 0.0 |
| ind2_niu (not in universe) | 0.0 |
| ind2_nonmetallic mineral product manufacturing | 0.0 |
| ind2_other information services | 0.0 |
| ind2_plastics and rubber products manufacturing | -0.0 |
| ind2_private households | 0.0 |
| ind2_publishing industries (except internet) | -0.0 |
| ind2_repair and maintenance | 0.0 |
| ind2_telecommunications | 0.0 |
| ind2_textile, apparel, and leather manufacturing | -0.0 |
| ind2_utilities | -0.0 |
| ind2_waste management and remediation services | 0.0 |
| ind2_wholesale trade | -0.0 |
| ind2_wood product manufacturing | -0.0 |
| looking_niu (not in universe) | 0.0 |
| looking_no | -0.0 |
| looking_refused | 0.0 |
| looking_retired | -0.0 |
| looking_yes | 0.0 |
| marst_married - spouse absent | 0.0 |
| marst_married - spouse present | 0.0 |
| marst_never married | -0.0 |
| marst_separated | -0.0 |
| metro_metropolitan, central city | 0.0 |
| metro_not identified | 0.0 |
| month_august | 0.0 |
| month_october | -0.0 |
| month_september | 0.0 |
| msasize_100,000 - 249,999 | -0.0 |
| msasize_500,000 - 999,999 | -0.0 |
| multjobs_niu (not in universe) | 0.0 |
| occ2_arts, design, entertainment, sports, and media occupations | 0.0 |
| occ2_farming, fishing, and forestry occupations | 0.0 |
| occ2_food preparation and serving related occupations | 0.0 |
| occ2_healthcare support occupations | -0.0 |
| occ2_legal occupations | 0.0 |
| occ2_niu (not in universe) | 0.0 |
| occ2_production occupations | -0.0 |
| occ2_sales and related occupations | -0.0 |
| paidhour_not paid hourly | 0.0 |
| race_american indian, alaskan native | 0.0 |
| race_asian only | 0.0 |
| race_black only | -0.0 |
| race_hawaiian pacific islander only | -0.0 |
| race_white-american indian | 0.0 |
| race_white-asian | 0.0 |
| race_white-black | -0.0 |
| region_south | 0.0 |
| region_west | -0.0 |
| retired_no | -0.0 |
| retired_yes | -0.0 |
| schlcoll_high school full time | 0.0 |
| schlcoll_high school part time | -0.0 |
| spearnweek | 0.0 |
| speduc_10th grade | -0.0 |
| speduc_11th grade | -0.0 |
| speduc_12th grade - no diploma | 0.0 |
| speduc_1st, 2nd, 3rd, or 4th grade | -0.0 |
| speduc_5th or 6th grade | -0.0 |
| speduc_9th grade | -0.0 |
| speduc_associate degree - occupational vocational | -0.0 |
| speduc_high school graduate - diploma | 0.0 |
| speduc_high school graduate - ged | -0.0 |
| speduc_niu (not in universe) | -0.0 |
| speduc_not available (see description) | 0.0 |
| speduc_professional school degree (md, dds, dvm, etc.) | -0.0 |
| spempnot_employed | -0.0 |
| spempnot_niu (not in universe) | -0.0 |
| spempnot_not employed | 0.0 |
| spempstat_disabled | 0.0 |
| spempstat_employed - at work | 0.0 |
| spempstat_employed - not at work | -0.0 |
| spempstat_niu (not in universe) | -0.0 |
| spempstat_retired | -0.0 |
| spousepres_no spouse or unmarried partner present | -0.0 |
| spousepres_spouse present | -0.0 |
| spousepres_unmarried partner present | 0.0 |
| sprace_american indian, alaskan native | 0.0 |
| sprace_black only | -0.0 |
| sprace_hawaiian pacific islander only | -0.0 |
| sprace_niu (not in universe) | -0.0 |
| sprace_not available (see description) | 0.0 |
| sprace_white-american indian | -0.0 |
| spsex_male | -0.0 |
| spsex_niu (not in universe) | -0.0 |
| statefip_alabama | 0.0 |
| statefip_alaska | -0.0 |
| statefip_arizona | -0.0 |
| statefip_connecticut | -0.0 |
| statefip_delaware | -0.0 |
| statefip_district of columbia | 0.0 |
| statefip_georgia | -0.0 |
| statefip_hawaii | 0.0 |
| statefip_idaho | -0.0 |
| statefip_indiana | 0.0 |
| statefip_iowa | -0.0 |
| statefip_kansas | -0.0 |
| statefip_kentucky | -0.0 |
| statefip_louisiana | 0.0 |
| statefip_maine | 0.0 |
| statefip_massachusetts | 0.0 |
| statefip_minnesota | -0.0 |
| statefip_mississippi | -0.0 |
| statefip_missouri | 0.0 |
| statefip_montana | -0.0 |
| statefip_nebraska | -0.0 |
| statefip_nevada | 0.0 |
| statefip_new hampshire | 0.0 |
| statefip_new jersey | 0.0 |
| statefip_north carolina | -0.0 |
| statefip_north dakota | -0.0 |
| statefip_oklahoma | -0.0 |
| statefip_pennsylvania | -0.0 |
| statefip_south carolina | 0.0 |
| statefip_south dakota | -0.0 |
| statefip_vermont | -0.0 |
| statefip_west virginia | 0.0 |
| statefip_wisconsin | -0.0 |
| statefip_wyoming | 0.0 |
| vetstat_veteran | 0.0 |
| statefip_michigan | 0.0 |
| hhtenure_rented for cash | 0.001 |
| statefip_virginia | 0.001 |
| educyrs_eleventh grade | 0.001 |
| ind2_food services and drinking places | 0.001 |
| statefip_california | 0.002 |
| hh_size | 0.002 |
| wrkdaysavg | 0.002 |
| speduc_some college but no degree | 0.002 |
| educyrs_master's degree--three+ year program | 0.002 |
| famincome_$7,500 to $9,999 | 0.002 |
| educyrs_tenth grade | 0.002 |
| ind2_transportation equipment manufacturing | 0.003 |
| msasize_1,000,000 - 2,499,999 | 0.005 |
| spempstat_not employed | 0.005 |
| kid3to5_yes | 0.005 |
| marst_widowed | 0.006 |
| month_april | 0.006 |
| educyrs_ninth grade | 0.007 |
| occ2_office and administrative support occupations | 0.007 |
| statefip_colorado | 0.007 |
| vetstat_niu (not in universe) | 0.008 |
| month_january | 0.008 |
| hh_numadults | 0.009 |
| sex_male | 0.009 |
| statefip_florida | 0.009 |
| statefip_illinois | 0.01 |
| statefip_washington | 0.011 |
| retired_niu (not in universe) | 0.011 |
| famincome_$75,000 to $99,999 | 0.012 |
| famincome_$12,500 to $14,999 | 0.012 |
| educyrs_fifth through sixth grade | 0.012 |
| occ2_business and financial operations occupations | 0.013 |
| ind2_insurance | 0.014 |
| hourwage | 0.014 |
| sprace_asian only | 0.014 |
| day_thursday | 0.014 |
| ind2_rental and leasing services | 0.015 |
| famincome_less than $5,000 | 0.015 |
| month_march | 0.016 |
| age | 0.017 |
| speduc_doctoral degree (phd, edd, etc.) | 0.017 |
| famincome_$30,000 to $34,999 | 0.017 |
| statefip_tennessee | 0.017 |
| kid1to2_yes | 0.018 |
| citizen_foreign born, u.s. citizen by naturalization | 0.019 |
| month_february | 0.019 |
| metro_metropolitan, balance of msa | 0.019 |
| schlcoll_not enrolled | 0.02 |
| speduc_associate degree - academic program | 0.02 |
| day_wednesday | 0.02 |
| ind2_administrative and support services | 0.022 |
| occ2_architecture and engineering occupations | 0.025 |
| ind2_public administration | 0.026 |
| citizen_foreign born, not a u.s. citizen | 0.029 |
| kid13to17_yes | 0.03 |
| spsex_female | 0.032 |
| ind2_retail trade | 0.033 |
| region_northeast | 0.033 |
| uhrsworkt | 0.034 |
| day_tuesday | 0.036 |
| schlcoll_niu (not in universe) | 0.039 |
| occ2_life, physical, and social science occupations | 0.04 |
| paidhour_niu (not in universe) | 0.04 |
| statefip_new york | 0.042 |
| occ2_installation, maintenance, and repair occupations | 0.043 |
| fullpart_full time | 0.046 |
| clwkr_self-employed, incorporated | 0.049 |
| msasize_2,500,000 - 4,999,999 | 0.05 |
| multjobs_yes | 0.053 |
| msasize_5,000,000+ | 0.063 |
| ind2_personal and laundry services | 0.066 |
| statefip_maryland | 0.067 |
| clwkr_government, federal | 0.074 |
| ind2_traveler accommodation | 0.077 |
| ind2_construction | 0.083 |
| occ2_building and grounds cleaning and maintenance occupations | 0.084 |
| fambus_pay_niu (not in universe) | 0.098 |
| kidund13_yes | 0.105 |
| logearnweek | 0.123 |
| occ2_construction and extraction occupations | 0.166 |
| empstat_employed - at work | 0.331 |

</details>


But this is largely just modelling the question of whether someone had a commute on that diary day.
If we instead restrict the sample to only those who had at least some commute time, then:

Biggest positive predictors of time spent commuting today (conditional on commuting a non-zero amount):
- working in the private households industry (maids, cooks, etc.)
- Living in a very big metro area, with 5+ million people.
- working in a construction/extraction occupation
- working in a mining occupation
- living in New York
- Having at least one child under the age of 13

Biggest negative predictors
- diary day on the weekend
- being a local government worker
- living in New Mexico
- Working in the food services industry
- being a full-time highschool student


<details markdown="block"><summary>Click for full list of coeficients.</summary>

| Variable Name | coef |
|:-:|:-:|
| day_sunday | -0.259 |
| day_saturday | -0.254 |
| clwkr_government, local | -0.214 |
| statefip_new mexico | -0.163 |
| ind2_food services and drinking places | -0.159 |
| schlcoll_high school full time | -0.159 |
| ind2_membership associations and organizations | -0.141 |
| housetype_house, apartment, flat | -0.136 |
| statefip_utah | -0.135 |
| paidhour_paid hourly | -0.125 |
| occ2_healthcare practitioner and technical occupations | -0.12 |
| occ2_education, training, and library occupations | -0.112 |
| occ2_protective service occupations | -0.109 |
| statefip_texas | -0.1 |
| hhtenure_occupied without payment of cash rent | -0.098 |
| ind2_retail trade | -0.098 |
| educyrs_professional degree | -0.085 |
| ind2_real estate | -0.085 |
| region_midwest | -0.074 |
| occ2_personal care and service occupations | -0.071 |
| fambus_family business | -0.071 |
| clwkr_private, nonprofit | -0.069 |
| ind2_educational services | -0.068 |
| citizen_native, born in united states | -0.063 |
| educyrs_seventh through eighth grade | -0.06 |
| metro_nonmetropolitan | -0.059 |
| spempnot_employed | -0.058 |
| metro_metropolitan, not identified | -0.057 |
| uhrsworkt | -0.052 |
| msasize_not identified or non-metropolitan | -0.049 |
| educyrs_twelfth grade | -0.047 |
| statefip_idaho | -0.047 |
| month_june | -0.045 |
| educyrs_doctoral degree | -0.043 |
| statefip_oregon | -0.042 |
| educyrs_college--one year | -0.042 |
| kid6to12_yes | -0.04 |
| famincome_refused | -0.04 |
| speduc_9th grade | -0.039 |
| ind2_health care services, except hospitals | -0.039 |
| msasize_250,000 - 499,999 | -0.034 |
| race_white only | -0.033 |
| statefip_arkansas | -0.03 |
| race_asian only | -0.026 |
| occ2_food preparation and serving related occupations | -0.023 |
| occ2_production occupations | -0.022 |
| famincome_$20,000 to $24,999 | -0.022 |
| famincome_$40,000 to $49,999 | -0.021 |
| month_july | -0.02 |
| speduc_bachelor's degree (ba, ab, bs, etc.) | -0.018 |
| speduc_7th or 8th grade | -0.018 |
| sex_male | -0.016 |
| occ2_community and social service occupations | -0.016 |
| citizen_native, born abroad of american parent or parents | -0.015 |
| ind2_primary metals and fabricated metal products | -0.014 |
| occ2_sales and related occupations | -0.013 |
| famincome_$15,000 to $19,999 | -0.013 |
| msasize_100,000 - 249,999 | -0.012 |
| occ2_transportation and material moving occupations | -0.01 |
| statefip_iowa | -0.009 |
| wrkdaysavg | -0.007 |
| otpay | -0.007 |
| famincome_$35,000 to $39,999 | -0.006 |
| spsex_male | -0.006 |
| famincome_$25,000 to $29,999 | -0.005 |
| famincome_$50,000 to $59,999 | -0.005 |
| marst_divorced | -0.004 |
| statefip_pennsylvania | -0.004 |
| region_west | -0.004 |
| sprace_white only | -0.004 |
| spempstat_not employed | -0.004 |
| spousepres_spouse present | -0.003 |
| statefip_minnesota | -0.002 |
| educyrs_college--three years | -0.001 |
| month_may | -0.001 |
| citizen_foreign born, u.s. citizen by naturalization | 0.0 |
| citizen_native, born in puerto rico or u.s. outlying area | 0.0 |
| clwkr_government, state | -0.0 |
| clwkr_niu (not in universe) | -0.0 |
| clwkr_self-employed, incorporated | 0.0 |
| day_friday | -0.0 |
| day_thursday | -0.0 |
| educyrs_bachelor's degree | -0.0 |
| educyrs_college--two years | 0.0 |
| educyrs_eleventh grade | 0.0 |
| educyrs_first through fourth grade | 0.0 |
| educyrs_less than first grade | 0.0 |
| educyrs_master's degree--one year program | -0.0 |
| educyrs_ninth grade | -0.0 |
| educyrs_tenth grade | 0.0 |
| empstat_employed - absent | -0.0 |
| empstat_not in labor force | -0.0 |
| empstat_unemployed - looking | 0.0 |
| empstat_unemployed - on layoff | 0.0 |
| fambus_no family business | 0.0 |
| fambus_pay_niu (not in universe) | -0.0 |
| famincome_$10,000 to $12,499 | -0.0 |
| famincome_$150,000 and over | 0.0 |
| famincome_$5,000 to $7,499 | -0.0 |
| famincome_$60,000 to $74,999 | 0.0 |
| famincome_don't know | 0.0 |
| fullpart_niu (not in universe) | -0.0 |
| fullpart_part time | -0.0 |
| hh_numkids | -0.0 |
| hh_size | 0.0 |
| hhtenure_rented for cash | 0.0 |
| holiday_yes | -0.0 |
| housetype_mobile home or trailer with 1 or more rooms added | 0.0 |
| housetype_mobile home or trailer with no permanent room added | 0.0 |
| ind2_agriculture | -0.0 |
| ind2_arts, entertainment, and recreation | -0.0 |
| ind2_beverage and tobacco product mfg | 0.0 |
| ind2_broadcasting (except internet) | -0.0 |
| ind2_chemical manufacturing | 0.0 |
| ind2_computer and electronic product mfg | -0.0 |
| ind2_electrical equipment, appliance mfg | 0.0 |
| ind2_food manufacturing | -0.0 |
| ind2_furniture and fixtures manufacturing | -0.0 |
| ind2_machinery manufacturing | -0.0 |
| ind2_miscellaneous and not specified mfg | -0.0 |
| ind2_motion picture and sound recording industries | 0.0 |
| ind2_niu (not in universe) | -0.0 |
| ind2_nonmetallic mineral product manufacturing | -0.0 |
| ind2_other information services | 0.0 |
| ind2_paper manufacturing and printing | -0.0 |
| ind2_personal and laundry services | -0.0 |
| ind2_plastics and rubber products manufacturing | -0.0 |
| ind2_publishing industries (except internet) | -0.0 |
| ind2_repair and maintenance | -0.0 |
| ind2_social assistance | 0.0 |
| ind2_telecommunications | 0.0 |
| ind2_textile, apparel, and leather manufacturing | -0.0 |
| ind2_transportation and warehousing | -0.0 |
| ind2_transportation equipment manufacturing | 0.0 |
| ind2_utilities | -0.0 |
| ind2_waste management and remediation services | 0.0 |
| ind2_wholesale trade | 0.0 |
| ind2_wood product manufacturing | -0.0 |
| kidund1_yes | -0.0 |
| looking_niu (not in universe) | 0.0 |
| looking_no | -0.0 |
| looking_refused | 0.0 |
| looking_retired | -0.0 |
| looking_yes | 0.0 |
| marst_married - spouse absent | 0.0 |
| marst_married - spouse present | -0.0 |
| marst_never married | 0.0 |
| marst_separated | -0.0 |
| metro_metropolitan, central city | 0.0 |
| metro_not identified | 0.0 |
| month_april | -0.0 |
| month_january | 0.0 |
| month_november | -0.0 |
| month_october | -0.0 |
| msasize_500,000 - 999,999 | 0.0 |
| multjobs_niu (not in universe) | -0.0 |
| multjobs_no | -0.0 |
| occ2_architecture and engineering occupations | 0.0 |
| occ2_farming, fishing, and forestry occupations | -0.0 |
| occ2_healthcare support occupations | 0.0 |
| occ2_legal occupations | 0.0 |
| occ2_life, physical, and social science occupations | 0.0 |
| occ2_management occupations | 0.0 |
| occ2_niu (not in universe) | -0.0 |
| paidhour_niu (not in universe) | 0.0 |
| paidhour_not paid hourly | 0.0 |
| race_american indian, alaskan native | -0.0 |
| race_hawaiian pacific islander only | 0.0 |
| race_white-american indian | 0.0 |
| race_white-asian | 0.0 |
| race_white-black | -0.0 |
| retired_niu (not in universe) | 0.0 |
| retired_no | 0.0 |
| retired_yes | -0.0 |
| schlcoll_college/university full time | -0.0 |
| schlcoll_college/university part time | 0.0 |
| schlcoll_high school part time | -0.0 |
| speduc_10th grade | -0.0 |
| speduc_11th grade | -0.0 |
| speduc_12th grade - no diploma | 0.0 |
| speduc_1st, 2nd, 3rd, or 4th grade | -0.0 |
| speduc_5th or 6th grade | -0.0 |
| speduc_high school graduate - diploma | -0.0 |
| speduc_high school graduate - ged | 0.0 |
| speduc_master's degree (ma, ms, meng, med, msw, etc.) | -0.0 |
| speduc_niu (not in universe) | 0.0 |
| speduc_not available (see description) | 0.0 |
| speduc_professional school degree (md, dds, dvm, etc.) | -0.0 |
| spempnot_niu (not in universe) | 0.0 |
| spempnot_not employed | 0.0 |
| spempstat_disabled | 0.0 |
| spempstat_employed - at work | -0.0 |
| spempstat_employed - not at work | -0.0 |
| spempstat_niu (not in universe) | 0.0 |
| spempstat_retired | 0.0 |
| spousepres_no spouse or unmarried partner present | 0.0 |
| spousepres_unmarried partner present | 0.0 |
| sprace_american indian, alaskan native | 0.0 |
| sprace_asian only | -0.0 |
| sprace_black only | 0.0 |
| sprace_hawaiian pacific islander only | -0.0 |
| sprace_niu (not in universe) | 0.0 |
| sprace_not available (see description) | 0.0 |
| sprace_white-american indian | -0.0 |
| spsex_female | 0.0 |
| spsex_niu (not in universe) | 0.0 |
| statefip_alabama | 0.0 |
| statefip_alaska | -0.0 |
| statefip_arizona | -0.0 |
| statefip_connecticut | -0.0 |
| statefip_delaware | -0.0 |
| statefip_district of columbia | 0.0 |
| statefip_georgia | 0.0 |
| statefip_hawaii | 0.0 |
| statefip_indiana | 0.0 |
| statefip_kansas | -0.0 |
| statefip_kentucky | -0.0 |
| statefip_louisiana | 0.0 |
| statefip_maine | 0.0 |
| statefip_massachusetts | 0.0 |
| statefip_mississippi | -0.0 |
| statefip_missouri | 0.0 |
| statefip_montana | -0.0 |
| statefip_nebraska | -0.0 |
| statefip_nevada | 0.0 |
| statefip_new hampshire | 0.0 |
| statefip_new jersey | 0.0 |
| statefip_north carolina | 0.0 |
| statefip_north dakota | -0.0 |
| statefip_ohio | -0.0 |
| statefip_oklahoma | -0.0 |
| statefip_rhode island | -0.0 |
| statefip_south carolina | 0.0 |
| statefip_south dakota | -0.0 |
| statefip_vermont | -0.0 |
| statefip_virginia | -0.0 |
| statefip_wisconsin | 0.0 |
| statefip_wyoming | 0.0 |
| vetstat_niu (not in universe) | -0.0 |
| vetstat_non-veteran | -0.0 |
| month_december | 0.001 |
| hhtenure_owned or being bought by a household member | 0.001 |
| occ2_computer and mathematical science occupations | 0.001 |
| day_monday | 0.003 |
| speduc_associate degree - occupational vocational | 0.006 |
| marst_widowed | 0.006 |
| clwkr_private, for profit | 0.006 |
| region_south | 0.009 |
| hh_numownkids | 0.01 |
| educyrs_college--four years | 0.011 |
| citizen_foreign born, not a u.s. citizen | 0.013 |
| spusualhrs | 0.013 |
| day_wednesday | 0.014 |
| ind2_finance | 0.015 |
| spearnweek | 0.016 |
| statefip_michigan | 0.017 |
| famincome_$100,000 to $149,999 | 0.018 |
| statefip_tennessee | 0.018 |
| famincome_$75,000 to $99,999 | 0.019 |
| fullpart_full time | 0.019 |
| ind2_hospitals | 0.022 |
| msasize_1,000,000 - 2,499,999 | 0.022 |
| occ2_office and administrative support occupations | 0.022 |
| multjobs_yes | 0.023 |
| month_september | 0.024 |
| famincome_$12,500 to $14,999 | 0.025 |
| occ2_business and financial operations occupations | 0.025 |
| speduc_associate degree - academic program | 0.026 |
| educyrs_master's degree--three+ year program | 0.027 |
| logearnweek | 0.027 |
| statefip_california | 0.028 |
| statefip_florida | 0.03 |
| educyrs_master's degree | 0.031 |
| statefip_west virginia | 0.031 |
| occ2_arts, design, entertainment, sports, and media occupations | 0.032 |
| day_tuesday | 0.033 |
| hh_numadults | 0.036 |
| month_august | 0.036 |
| statefip_colorado | 0.038 |
| occ2_installation, maintenance, and repair occupations | 0.039 |
| kid3to5_yes | 0.04 |
| speduc_some college but no degree | 0.042 |
| month_march | 0.044 |
| schlcoll_niu (not in universe) | 0.044 |
| famincome_$7,500 to $9,999 | 0.046 |
| hourwage | 0.052 |
| schlcoll_not enrolled | 0.053 |
| ind2_rental and leasing services | 0.054 |
| clwkr_self-employed, unincorporated | 0.054 |
| ind2_traveler accommodation | 0.056 |
| statefip_illinois | 0.057 |
| race_black only | 0.059 |
| fambus_pay_no | 0.06 |
| occ2_building and grounds cleaning and maintenance occupations | 0.061 |
| empstat_employed - at work | 0.062 |
| educyrs_fifth through sixth grade | 0.062 |
| educyrs_master's degree--two year program | 0.063 |
| kid13to17_yes | 0.063 |
| famincome_$30,000 to $34,999 | 0.065 |
| metro_metropolitan, balance of msa | 0.071 |
| ind2_insurance | 0.072 |
| region_northeast | 0.075 |
| age | 0.076 |
| statefip_washington | 0.079 |
| vetstat_veteran | 0.08 |
| month_february | 0.082 |
| kid1to2_yes | 0.086 |
| speduc_doctoral degree (phd, edd, etc.) | 0.089 |
| famincome_less than $5,000 | 0.115 |
| ind2_professional, scientific, and technical services | 0.117 |
| earnweek | 0.125 |
| clwkr_government, federal | 0.134 |
| statefip_maryland | 0.154 |
| ind2_administrative and support services | 0.157 |
| ind2_public administration | 0.165 |
| ind2_construction | 0.22 |
| msasize_2,500,000 - 4,999,999 | 0.243 |
| kidund13_yes | 0.252 |
| statefip_new york | 0.268 |
| ind2_mining | 0.279 |
| occ2_construction and extraction occupations | 0.353 |
| msasize_5,000,000+ | 0.356 |
| ind2_private households | 0.383 |


</details>







