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
- time spent by spouse commuting
- family expenditures on buses and trains
- family expenditures on gas
- own labor income
- working in the construction industry
- time spent working
- total family expenditures

Some things that are negatively correlated:
- "other" hourly status
- living in the north central region (the midwest)
- being female
- self or spouse grew up in north central region
- being a house spouse in a previous year
- having a sales occupation



<details markdown="block"><summary>Click for full list of correlations.</summary>

<!--Note as of 2023 April 14: Minimal processing has been done. So some of these, especially near the bottom are "correlations" on categorical data which is just coded with numbers. These have no actually meaning.-->

Means and correlations are both weighted, 
and conditional on the individual being in the subsample
(which here is people who typically work).

The weights are the 2019 individual cross-sectional weights from PSID (ER34864)

Units vary from variable to variable.

| Variable Name | Mean | Correlation |
|:--|:--|:-:|
| time_commute_self_19 | 40.0 | 1.0 |
| time_commute_self_17 | 39.9 | 0.504 |
| time_commute_self_15 | 38.8 | 0.451 |
| time_commute_self_13 | 37.9 | 0.404 |
| time_commute_self_11 | 39.0 | 0.401 |
| cost_transport_bustrain_17 | 105.2 | 0.174 |
| time_commute_spouse_19 | 22.9 | 0.164 |
| cost_transport_bustrain_13 | 106.0 | 0.162 |
| cost_transport_bustrain_19 | 128.1 | 0.154 |
| cost_transport_bustrain_11 | 109.8 | 0.127 |
| cost_transport_gas_19 | 2381.0 | 0.124 |
| cost_transport_bustrain_15 | 113.4 | 0.121 |
| cost_transport_gas_17 | 2259.0 | 0.11 |
| time_commute_spouse_17 | 23.5 | 0.107 |
| time_commute_spouse_13 | 23.0 | 0.1 |
| income_labor_self_15 | 51957.8 | 0.094 |
| time_commute_spouse_11 | 25.0 | 0.093 |
| income_labor_self_19 | 59138.6 | 0.09 |
| income_labor_self_17 | 54391.4 | 0.086 |
| income_labor_self_11 | 45872.3 | 0.085 |
| time_commute_spouse_15 | 23.5 | 0.08 |
| ind_self_19_construction | 0.07 | 0.078 |
| time_work_annual_self_19 | 2010.0 | 0.078 |
| time_work_self_19 | 40.6 | 0.078 |
| cost_total_19 | 60410.2 | 0.077 |
| income_wagerate_self_15 | 26.2 | 0.076 |
| cost_transport_gas_15 | 2512.6 | 0.073 |
| income_wagerate_self_19 | 29.5 | 0.072 |
| ind_self_17_construction | 0.06 | 0.071 |
| time_work_annual_self_17 | 1932.2 | 0.07 |
| cost_childcare_17 | 714.0 | 0.069 |
| cost_total_with_rent_value_19 | 64069.9 | 0.067 |
| cost_housing_19 | 24174.1 | 0.067 |
| time_work_annual_self_15 | 1908.2 | 0.066 |
| income_wagerate_self_13 | 25.5 | 0.065 |
| time_work_self_17 | 38.2 | 0.065 |
| time_work_prevyear_self_19 | 42.7 | 0.065 |
| ind_self_15_construction | 0.049 | 0.065 |
| income_wagerate_self_17 | 27.6 | 0.064 |
| cost_transport_19 | 11677.3 | 0.064 |
| hourlystatus_self_19_salaried | 0.359 | 0.064 |
| grewup_state_spouse_19_ny | 0.041 | 0.064 |
| grewup_region_spouse_19_foreign | 0.122 | 0.063 |
| cost_housing_tax_19 | 2380.4 | 0.063 |
| cost_transport_17 | 10949.6 | 0.063 |
| cost_housing_mortgage_19 | 6923.4 | 0.063 |
| cost_housing_tax_17 | 2096.5 | 0.061 |
| income_wagerate_self_11 | 23.9 | 0.06 |
| grewup_region_spouse_17_foreign | 0.107 | 0.058 |
| cost_transport_gas_13 | 3164.8 | 0.058 |
| ind_self_13_construction | 0.042 | 0.057 |
| cost_housing_17 | 22567.4 | 0.056 |
| grewup_region_spouse_19_northeast | 0.128 | 0.056 |
| income_labor_self_13 | 50503.7 | 0.055 |
| workweeks_self_15 | 44.5 | 0.055 |
| cost_transport_insurance_17 | 2024.2 | 0.055 |
| grewup_state_spouse_15_ny | 0.033 | 0.055 |
| grewup_size_spouse_19_bigcity | 0.225 | 0.053 |
| hourlystatus_self_17_salaried | 0.304 | 0.053 |
| grewup_state_spouse_17_ny | 0.037 | 0.052 |
| cost_transport_insurance_19 | 2091.8 | 0.052 |
| cost_transport_parking_15 | 78.1 | 0.051 |
| time_work_prevyear_self_17 | 42.0 | 0.051 |
| cost_housing_13 | 21753.1 | 0.051 |
| time_housework_spouse_17 | 9.5 | 0.051 |
| cost_transport_11 | 11445.7 | 0.051 |
| cost_transport_repair_19 | 928.2 | 0.05 |
| grewup_size_self_bigcity | 0.333 | 0.05 |
| grewup_size_spouse_17_bigcity | 0.2 | 0.05 |
| cost_food_away_19 | 3365.7 | 0.05 |
| ind_self_11_construction | 0.04 | 0.049 |
| cost_trips_19 | 2571.0 | 0.049 |
| hourlystatus_self_19_hourlypluscomm | 0.004 | 0.049 |
| grewup_state_self_ny | 0.058 | 0.048 |
| cost_transport_insurance_15 | 1805.8 | 0.048 |
| time_housework_spouse_19 | 9.2 | 0.048 |
| cost_food_19 | 11064.9 | 0.048 |
| sizeworkplace_self_13 | 764.9 | 0.048 |
| cost_transport_gas_11 | 3257.9 | 0.048 |
| time_work_annual_self_13 | 1878.0 | 0.048 |
| cost_transport_parking_17 | 82.6 | 0.047 |
| cost_housing_rent_11 | 2966.6 | 0.047 |
| time_shopping_spouse_17 | 2.8 | 0.046 |
| cost_transport_13 | 11390.5 | 0.046 |
| cost_transport_15 | 11116.9 | 0.046 |
| grewup_region_spouse_17_northeast | 0.115 | 0.046 |
| cost_transport_parking_19 | 108.2 | 0.045 |
| time_housework_spouse_11 | 9.9 | 0.045 |
| cost_transport_insurance_11 | 1669.6 | 0.045 |
| grewup_state_spouse_11_ny | 0.03 | 0.045 |
| time_work_annual_self_11 | 1828.5 | 0.045 |
| cost_transport_parking_13 | 69.4 | 0.044 |
| grewup_state_spouse_13_ny | 0.031 | 0.044 |
| cost_housing_rent_13 | 3268.3 | 0.044 |
| workweeks_self_17 | 45.3 | 0.043 |
| grewup_region_spouse_15_northeast | 0.106 | 0.043 |
| income_familytotal_19 | 111723.9 | 0.043 |
| cost_housing_telecom_17 | 2873.0 | 0.042 |
| cost_housing_tax_13 | 2135.8 | 0.041 |
| cost_transport_repair_17 | 957.9 | 0.041 |
| cost_transport_parking_11 | 55.1 | 0.04 |
| cost_housing_insurance_19 | 826.6 | 0.04 |
| cost_housing_telecom_19 | 2972.8 | 0.039 |
| cost_housing_utility_17 | 2938.7 | 0.039 |
| cost_housing_tax_11 | 2111.1 | 0.039 |
| time_childcare_spouse_19 | 8.5 | 0.039 |
| workweeks_self_13 | 43.8 | 0.039 |
| ind_self_13_utilities | 0.007 | 0.039 |
| home_rent_value_17 | 11992.4 | 0.037 |
| home_rent_value_19 | 12963.4 | 0.037 |
| cost_transport_additionalvehicle_11 | 1605.7 | 0.037 |
| cost_housing_tax_15 | 2132.9 | 0.037 |
| cost_food_deliver_19 | 209.5 | 0.037 |
| daycare_19_yes | 0.075 | 0.037 |
| time_housework_spouse_15 | 8.9 | 0.037 |
| ishd_19 | 0.688 | 0.036 |
| empstat_17_other | 0.001 | 0.036 |
| id68 | 2257028.4 | 0.036 |
| grewup_size_spouse_15_bigcity | 0.164 | 0.036 |
| time_work_prevyear_self_15 | 42.1 | 0.036 |
| cost_housing_mortgage_17 | 6262.1 | 0.036 |
| cost_childcare_19 | 775.0 | 0.036 |
| cost_housing_insurance_11 | 674.0 | 0.036 |
| cost_housing_rent_15 | 3548.7 | 0.035 |
| cost_housing_rent_17 | 4228.5 | 0.035 |
| cost_childcare_15 | 656.2 | 0.035 |
| Unnamed: 0 | 13341.2 | 0.035 |
| cost_transport_additionalvehicle_15 | 1286.8 | 0.034 |
| daycare_17_yes | 0.076 | 0.034 |
| ind_spouse_13_education | 0.049 | 0.034 |
| time_housework_spouse_13 | 9.4 | 0.034 |
| time_childcare_spouse_17 | 9.1 | 0.034 |
| hh_size_17 | 2.9 | 0.033 |
| vacationdays_self_13 | 1.7 | 0.033 |
| cost_housing_15 | 21813.8 | 0.033 |
| cost_transport_repair_13 | 1876.8 | 0.033 |
| hourlystatus_self_13_salaried | 0.247 | 0.033 |
| cost_transport_loans_19 | 1852.8 | 0.033 |
| cost_transport_other_19 | 53.9 | 0.033 |
| ind_self_15_utilities | 0.008 | 0.033 |
| cost_housing_utility_15 | 3062.6 | 0.033 |
| time_work_prevyear_sp_19 | 22.8 | 0.033 |
| cost_food_deliver_15 | 129.4 | 0.032 |
| grewup_state_spouse_15_ut | 0.008 | 0.032 |
| time_pcare_spouse_19 | 5.4 | 0.032 |
| workweeks_self_11 | 42.6 | 0.032 |
| grewup_state_spouse_17_ut | 0.008 | 0.032 |
| cost_housing_mortgage_11 | 7587.0 | 0.032 |
| cost_transport_additionalvehicle_17 | 1461.2 | 0.032 |
| hh_size_19 | 2.8 | 0.032 |
| cost_housing_mortgage_13 | 6865.5 | 0.031 |
| grewup_state_spouse_19_ut | 0.009 | 0.031 |
| grewup_state_spouse_11_vt | 0.0 | 0.031 |
| grewup_state_spouse_13_vt | 0.0 | 0.031 |
| grewup_state_spouse_13_dc | 0.001 | 0.03 |
| cost_food_17 | 10354.6 | 0.03 |
| weight_indiv_cs_17 | 19965.2 | 0.03 |
| grewup_state_self_ut | 0.01 | 0.03 |
| ind_self_19_financeinsurance | 0.054 | 0.03 |
| cost_housing_11 | 22415.7 | 0.029 |
| cost_childcare_13 | 703.3 | 0.029 |
| grewup_state_self_ma | 0.028 | 0.029 |
| income_familytotal_17 | 103431.3 | 0.029 |
| ind_self_11_utilities | 0.006 | 0.029 |
| hourlystatus_self_15_salaried | 0.27 | 0.029 |
| cost_housing_rent_19 | 4547.4 | 0.029 |
| grewup_state_spouse_17_dc | 0.001 | 0.029 |
| grewup_state_spouse_19_ga | 0.009 | 0.028 |
| cost_education_17 | 2456.1 | 0.028 |
| kids_youngest_11 | 7.9 | 0.028 |
| ind_self_19_transportwarehouse | 0.05 | 0.028 |
| grewup_state_spouse_13_ut | 0.007 | 0.028 |
| grewup_state_spouse_11_ut | 0.008 | 0.028 |
| cost_food_deliver_17 | 151.3 | 0.028 |
| grewup_state_spouse_15_dc | 0.001 | 0.028 |
| cost_housing_telecom_15 | 2836.8 | 0.028 |
| kids_youngest_19 | 7.7 | 0.027 |
| cost_housing_utility_19 | 3088.3 | 0.027 |
| ind_self_19_utilities | 0.01 | 0.027 |
| ind_self_17_utilities | 0.009 | 0.027 |
| grewup_state_spouse_19_dc | 0.001 | 0.027 |
| cost_food_athome_17 | 7120.8 | 0.027 |
| cost_transport_insurance_13 | 1814.5 | 0.027 |
| income_familytotal_15 | 100763.5 | 0.027 |
| ishd_11 | 0.447 | 0.027 |
| grewup_state_spouse_13_nh | 0.001 | 0.027 |
| grewup_state_spouse_11_ok | 0.005 | 0.026 |
| cost_housing_furnishing_17 | 1174.6 | 0.026 |
| grewup_state_spouse_11_dc | 0.001 | 0.026 |
| cost_clothing_17 | 1550.2 | 0.026 |
| hourlystatus_self_19_salpluscomm | 0.012 | 0.026 |
| cost_housing_utility_11 | 3064.7 | 0.026 |
| ind_spouse_11_financeinsurance | 0.025 | 0.026 |
| ind_self_17_financeinsurance | 0.048 | 0.026 |
| ind_self_11_mining | 0.003 | 0.025 |
| cost_transport_taxi_19 | 133.1 | 0.025 |
| hourlystatus_self_11_hourlypluscomm | 0.004 | 0.025 |
| cost_education_13 | 3067.0 | 0.025 |
| cost_health_insurance_19 | 2922.0 | 0.025 |
| cost_food_athome_19 | 7489.7 | 0.025 |
| grewup_state_spouse_11_ga | 0.007 | 0.025 |
| grewup_state_spouse_15_vt | 0.0 | 0.025 |
| cost_food_away_13 | 2585.0 | 0.025 |
| ind_self_13_manufacturing | 0.082 | 0.024 |
| cost_food_deliver_13 | 127.1 | 0.024 |
| ind_self_11_financeinsurance | 0.036 | 0.024 |
| grewup_size_spouse_11_bigcity | 0.154 | 0.023 |
| grewup_size_spouse_13_bigcity | 0.158 | 0.023 |
| grewup_state_spouse_13_ma | 0.015 | 0.023 |
| ishd_17 | 0.611 | 0.023 |
| ind_self_17_transportwarehouse | 0.038 | 0.023 |
| grewup_state_spouse_13_ok | 0.004 | 0.023 |
| workweeks_self_19 | 47.4 | 0.023 |
| time_education_spouse_17 | 1.0 | 0.023 |
| grewup_state_spouse_17_ma | 0.018 | 0.023 |
| educyrs_19 | 13.9 | 0.023 |
| time_work_prevyear_sp_17 | 21.7 | 0.022 |
| grewup_state_spouse_19_ma | 0.021 | 0.022 |
| income_familytotal_13 | 96452.6 | 0.022 |
| cost_housing_utility_13 | 3073.3 | 0.022 |
| weight_indiv_cs_19 | 23855.6 | 0.022 |
| cost_education_19 | 2049.8 | 0.022 |
| ind_spouse_11_arts | 0.007 | 0.022 |
| time_work_prevyear_sp_13 | 21.2 | 0.022 |
| ind_self_19_mining | 0.005 | 0.022 |
| sizeworkplace_spouse_19 | 1036.5 | 0.021 |
| income_familytotal_11 | 89106.7 | 0.021 |
| cost_food_13 | 8907.4 | 0.021 |
| kids_num_19 | 0.792 | 0.021 |
| cost_clothing_19 | 1580.5 | 0.021 |
| ind_self_17_mining | 0.004 | 0.021 |
| ind_self_15_mining | 0.004 | 0.021 |
| grewup_state_self_ga | 0.011 | 0.021 |
| cost_transport_additionalvehicle_19 | 1727.2 | 0.021 |
| cost_education_15 | 3082.5 | 0.02 |
| cost_transport_taxi_17 | 90.3 | 0.02 |
| cost_recreation_17 | 1088.9 | 0.02 |
| ind_self_19_information | 0.02 | 0.02 |
| ishd_13 | 0.479 | 0.02 |
| grewup_state_spouse_11_ma | 0.014 | 0.02 |
| ind_self_19_management | 0.042 | 0.02 |
| grewup_state_self_dc | 0.002 | 0.02 |
| cost_education_11 | 2819.8 | 0.02 |
| grewup_state_spouse_19_ok | 0.006 | 0.02 |
| hourlystatus_self_11_salpluscomm | 0.008 | 0.019 |
| hourlystatus_spouse_19_salaried | 0.223 | 0.019 |
| cost_housing_telecom_11 | 2542.6 | 0.019 |
| time_shopping_spouse_19 | 2.8 | 0.019 |
| ind_self_15_financeinsurance | 0.043 | 0.019 |
| cost_transport_repair_11 | 1840.1 | 0.019 |
| ind_spouse_11_DKNARefused | 0.001 | 0.019 |
| grewup_state_spouse_15_ma | 0.016 | 0.019 |
| ind_self_13_financeinsurance | 0.039 | 0.019 |
| empstat_19_laid off | 0.006 | 0.019 |
| grewup_state_spouse_13_ga | 0.007 | 0.019 |
| grewup_state_spouse_17_vt | 0.0 | 0.019 |
| grewup_state_spouse_19_vt | 0.0 | 0.019 |
| sizeworkplace_self_15 | 707.6 | 0.019 |
| grewup_state_spouse_13_al | 0.006 | 0.019 |
| grewup_state_spouse_17_ga | 0.008 | 0.019 |
| time_pcare_spouse_17 | 5.5 | 0.018 |
| cost_health_19 | 4888.9 | 0.018 |
| time_work_prevyear_sp_15 | 21.1 | 0.018 |
| sizeworkplace_self_17 | 723.6 | 0.018 |
| cost_transport_loans_15 | 1762.9 | 0.018 |
| hourlystatus_self_11_salaried | 0.232 | 0.018 |
| kids_youngest_17 | 7.5 | 0.018 |
| ind_self_13_mining | 0.005 | 0.018 |
| ind_self_11_manufacturing | 0.078 | 0.018 |
| cost_housing_telecom_13 | 2735.6 | 0.018 |
| grewup_state_self_tx | 0.042 | 0.018 |
| grewup_state_spouse_11_nh | 0.001 | 0.017 |
| grewup_state_spouse_15_al | 0.006 | 0.017 |
| grewup_state_spouse_19_nj | 0.022 | 0.017 |
| ind_self_15_management | 0.026 | 0.017 |
| grewup_state_spouse_11_mn | 0.007 | 0.017 |
| ind_spouse_13_financeinsurance | 0.026 | 0.017 |
| workweeks_spouse_19 | 27.1 | 0.016 |
| time_education_spouse_19 | 0.963 | 0.016 |
| ind_self_15_manufacturing | 0.09 | 0.016 |
| grewup_state_self_ca | 0.082 | 0.016 |
| empstat_17_working | 0.839 | 0.016 |
| cost_food_away_17 | 3082.5 | 0.016 |
| cost_transport_loans_11 | 1339.5 | 0.016 |
| cost_childcare_11 | 671.0 | 0.016 |
| empstat_17_laid off | 0.005 | 0.016 |
| grewup_state_spouse_11_al | 0.005 | 0.016 |
| ind_self_13_information | 0.015 | 0.016 |
| grewup_state_spouse_17_ok | 0.006 | 0.016 |
| cost_trips_13 | 2055.2 | 0.016 |
| grewup_state_spouse_19_fl | 0.015 | 0.016 |
| cost_transport_other_13 | 98.2 | 0.015 |
| sequence_number_15 | 2.3 | 0.015 |
| cost_housing_insurance_15 | 688.5 | 0.015 |
| empstat_15_searching | 0.032 | 0.015 |
| cost_transport_loans_13 | 1510.7 | 0.014 |
| time_volunteering_spouse_17 | 0.898 | 0.014 |
| grewup_state_spouse_17_nh | 0.001 | 0.014 |
| grewup_state_spouse_15_ga | 0.007 | 0.014 |
| empstat_19_working | 0.98 | 0.014 |
| ind_spouse_11_education | 0.046 | 0.014 |
| empstat_13_other | 0.001 | 0.014 |
| grewup_state_self_al | 0.008 | 0.014 |
| ind_self_11_transportwarehouse | 0.027 | 0.014 |
| cost_health_bills_19 | 987.9 | 0.014 |
| ishd_15 | 0.521 | 0.014 |
| grewup_state_self_il | 0.029 | 0.013 |
| ind_spouse_11_realestate | 0.007 | 0.013 |
| relation_to_head_17 | 14.0 | 0.013 |
| time_work_prevyear_self_13 | 42.2 | 0.013 |
| ind_self_15_adminmilitary | 0.05 | 0.013 |
| grewup_state_spouse_19_nh | 0.001 | 0.013 |
| ind_self_19_adminmilitary | 0.058 | 0.013 |
| cost_housing_mortgage_15 | 6402.9 | 0.013 |
| empstat_11_other | 0.002 | 0.013 |
| kids_num_17 | 0.83 | 0.013 |
| ind_self_15_transportwarehouse | 0.033 | 0.012 |
| cost_transport_leases_15 | 463.5 | 0.012 |
| grewup_state_spouse_19_tx | 0.029 | 0.012 |
| grewup_size_self_other | 0.028 | 0.012 |
| cost_computing_17 | 570.0 | 0.012 |
| hourlystatus_spouse_19_hourly | 0.25 | 0.012 |
| ind_self_19_manufacturing | 0.109 | 0.012 |
| grewup_state_self_vt | 0.0 | 0.011 |
| cost_recreation_19 | 1022.5 | 0.011 |
| wealth_homeequity_17 | 97487.0 | 0.011 |
| grewup_state_self_id | 0.002 | 0.011 |
| grewup_state_spouse_17_tx | 0.025 | 0.011 |
| hourlystatus_self_15_salpluscomm | 0.01 | 0.011 |
| hh_size_13 | 3.0 | 0.011 |
| ind_spouse_11_otherservices | 0.02 | 0.01 |
| grewup_state_self_ky | 0.012 | 0.01 |
| grewup_state_spouse_13_mn | 0.007 | 0.01 |
| empstat_current_self_17_laid off | 0.003 | 0.01 |
| cost_food_away_15 | 2818.1 | 0.01 |
| ind_spouse_13_otherservices | 0.02 | 0.01 |
| time_adultcare_spouse_17 | 0.451 | 0.01 |
| grewup_state_spouse_17_fl | 0.014 | 0.01 |
| grewup_state_spouse_17_al | 0.006 | 0.01 |
| cost_transport_leases_17 | 490.6 | 0.01 |
| cost_transport_other_17 | 54.2 | 0.01 |
| vacationdays_self_19 | 1.9 | 0.01 |
| hourlystatus_spouse_11_hourlypluscomm | 0.002 | 0.01 |
| grewup_state_self_hi | 0.001 | 0.009 |
| daycare_11_yes | 0.075 | 0.009 |
| sizeworkplace_self_11 | 9891.2 | 0.009 |
| hourlystatus_spouse_17_other | 0.05 | 0.009 |
| cost_transport_repair_15 | 1374.2 | 0.009 |
| empstat_17_searching | 0.033 | 0.009 |
| cost_transport_taxi_11 | 33.7 | 0.009 |
| time_work_prevyear_self_11 | 41.8 | 0.009 |
| ind_self_17_adminmilitary | 0.052 | 0.009 |
| cost_food_athome_11 | 6053.3 | 0.008 |
| daycare_13_yes | 0.07 | 0.008 |
| cost_health_rx_19 | 395.7 | 0.008 |
| cost_health_bills_17 | 868.3 | 0.008 |
| grewup_state_spouse_15_nj | 0.019 | 0.008 |
| cost_trips_17 | 2278.4 | 0.008 |
| grewup_state_spouse_15_mn | 0.007 | 0.008 |
| ind_self_13_management | 0.024 | 0.008 |
| grewup_state_spouse_17_nj | 0.019 | 0.008 |
| cost_food_15 | 9409.4 | 0.008 |
| grewup_state_self_mn | 0.012 | 0.008 |
| cost_housing_repairs_17 | 2259.3 | 0.008 |
| ind_self_17_management | 0.033 | 0.008 |
| workweeks_spouse_15 | 27.4 | 0.008 |
| ind_self_17_information | 0.018 | 0.008 |
| grewup_state_spouse_13_wv | 0.002 | 0.008 |
| grewup_state_spouse_13_ca | 0.039 | 0.008 |
| grewup_state_spouse_19_de | 0.0 | 0.007 |
| grewup_state_spouse_17_wv | 0.002 | 0.007 |
| wealth_homeequity_15 | 90047.2 | 0.007 |
| hourlystatus_spouse_17_hourly | 0.232 | 0.007 |
| cost_recreation_15 | 1039.7 | 0.007 |
| hh_size_15 | 2.9 | 0.007 |
| daycare_17_no | 0.294 | 0.007 |
| grewup_state_spouse_15_ok | 0.005 | 0.007 |
| income_wagerate_spouse_15 | 16.5 | 0.007 |
| cost_housing_repairs_13 | 1917.5 | 0.007 |
| ind_spouse_13_realestate | 0.007 | 0.007 |
| daycare_19_no | 0.303 | 0.007 |
| hourlystatus_spouse_19_hourlypluscomm | 0.001 | 0.007 |
| ind_self_11_adminmilitary | 0.047 | 0.007 |
| cost_housing_insurance_17 | 734.7 | 0.007 |
| time_work_prevyear_spouse_15 | 40.1 | 0.007 |
| grewup_state_self_tn | 0.016 | 0.007 |
| grewup_state_spouse_11_nj | 0.017 | 0.007 |
| cost_transport_additionalvehicle_13 | 1208.3 | 0.007 |
| cost_food_athome_13 | 6195.3 | 0.006 |
| grewup_state_spouse_15_wv | 0.002 | 0.006 |
| empstat_current_self_15_student | 0.009 | 0.006 |
| workweeks_spouse_17 | 27.0 | 0.006 |
| cost_housing_furnishing_11 | 1219.5 | 0.006 |
| grewup_state_spouse_11_wy | 0.0 | 0.006 |
| grewup_state_spouse_13_wy | 0.0 | 0.006 |
| vacationdays_self_15 | 2.0 | 0.006 |
| cost_health_doctor_13 | 936.2 | 0.006 |
| ind_self_13_transportwarehouse | 0.03 | 0.006 |
| grewup_state_self_wv | 0.003 | 0.005 |
| grewup_state_spouse_11_fl | 0.009 | 0.005 |
| grewup_state_spouse_15_wy | 0.0 | 0.005 |
| cost_transport_taxi_13 | 38.3 | 0.005 |
| cost_food_11 | 8623.4 | 0.005 |
| cost_health_doctor_15 | 968.5 | 0.005 |
| ind_self_17_accomodationsfood | 0.046 | 0.005 |
| grewup_state_spouse_17_wy | 0.0 | 0.005 |
| ind_self_17_manufacturing | 0.1 | 0.005 |
| cost_transport_loans_17 | 1924.9 | 0.005 |
| income_wagerate_spouse_19 | 17.7 | 0.005 |
| time_work_spouse_19 | 21.9 | 0.005 |
| ind_self_13_adminmilitary | 0.049 | 0.005 |
| grewup_state_spouse_19_al | 0.006 | 0.004 |
| interview_number_13 | 4001.9 | 0.004 |
| empstat_13_student | 0.03 | 0.004 |
| cost_housing_repairs_19 | 2276.1 | 0.004 |
| grewup_state_spouse_17_il | 0.018 | 0.004 |
| kids_youngest_13 | 7.8 | 0.004 |
| grewup_state_spouse_19_wy | 0.001 | 0.004 |
| income_labor_spouse_19 | 34158.7 | 0.004 |
| hourlystatus_spouse_13_other | 0.042 | 0.004 |
| time_work_annual_spouse_19 | 1129.4 | 0.004 |
| ind_spouse_13_arts | 0.008 | 0.004 |
| cost_health_hospital_19 | 572.4 | 0.004 |
| grewup_state_spouse_17_pa | 0.032 | 0.004 |
| grewup_state_spouse_15_tx | 0.023 | 0.004 |
| grewup_state_spouse_19_pa | 0.035 | 0.004 |
| hourlystatus_spouse_13_salaried | 0.166 | 0.004 |
| grewup_state_spouse_15_nm | 0.001 | 0.004 |
| daycare_15_yes | 0.065 | 0.003 |
| cost_housing_furnishing_15 | 1228.9 | 0.003 |
| cost_housing_furnishing_19 | 1159.0 | 0.003 |
| hourlystatus_self_17_salpluscomm | 0.011 | 0.003 |
| grewup_state_self_me | 0.003 | 0.003 |
| grewup_state_spouse_15_fl | 0.011 | 0.003 |
| educyrs_17 | 12.8 | 0.003 |
| grewup_state_spouse_11_wv | 0.001 | 0.003 |
| grewup_state_spouse_15_pa | 0.03 | 0.003 |
| grewup_state_spouse_11_tx | 0.02 | 0.002 |
| grewup_state_spouse_19_tn | 0.011 | 0.002 |
| ind_self_15_information | 0.016 | 0.002 |
| grewup_region_spouse_19_south | 0.167 | 0.002 |
| cost_housing_furnishing_13 | 1074.5 | 0.002 |
| vacationdays_spouse_11 | 0.922 | 0.002 |
| cost_transport_taxi_15 | 49.7 | 0.002 |
| cost_transport_leases_19 | 511.1 | 0.002 |
| grewup_state_spouse_19_il | 0.019 | 0.002 |
| ind_spouse_13_health | 0.061 | 0.002 |
| grewup_state_spouse_11_me | 0.003 | 0.002 |
| vacationdays_self_17 | 1.7 | 0.001 |
| cost_clothing_15 | 1723.9 | 0.001 |
| grewup_state_self_nj | 0.033 | 0.001 |
| hourlystatus_spouse_13_hourlyplustips | 0.001 | 0.001 |
| grewup_state_spouse_19_mt | 0.0 | 0.001 |
| grewup_state_self_mt | 0.001 | 0.001 |
| cost_health_doctor_19 | 998.7 | 0.001 |
| grewup_state_spouse_15_me | 0.003 | 0.001 |
| grewup_state_spouse_11_hi | 0.001 | 0.001 |
| grewup_state_spouse_15_hi | 0.001 | 0.001 |
| grewup_state_spouse_13_hi | 0.001 | 0.001 |
| grewup_state_spouse_17_ca | 0.046 | 0.001 |
| cost_transport_leases_11 | 255.9 | 0.001 |
| interview_number_11 | 3874.8 | 0.001 |
| grewup_state_spouse_15_ca | 0.042 | 0.001 |
| vacationdays_self_11 | 1.5 | 0.0 |
| grewup_state_spouse_19_mn | 0.009 | 0.0 |
| grewup_state_spouse_13_ms | 0.006 | 0.0 |
| cost_trips_15 | 2266.5 | 0.0 |
| grewup_state_spouse_17_de | 0.0 | -0.0 |
| grewup_state_spouse_11_de | 0.0 | -0.0 |
| grewup_state_spouse_13_de | 0.0 | -0.0 |
| grewup_state_spouse_15_de | 0.0 | -0.0 |
| empstat_11_student | 0.031 | -0.0 |
| ind_self_19_arts | 0.021 | -0.0 |
| sequence_number_13 | 2.4 | -0.0 |
| ind_spouse_11_information | 0.011 | -0.0 |
| cost_food_athome_15 | 6461.9 | -0.0 |
| ind_spouse_11_mining | 0.002 | -0.0 |
| hourlystatus_spouse_15_hourlypluscomm | 0.001 | -0.001 |
| grewup_state_spouse_19_nv | 0.001 | -0.001 |
| ind_self_11_information | 0.018 | -0.001 |
| grewup_size_spouse_19_suburban | 0.39 | -0.001 |
| sizeworkplace_spouse_17 | 798.6 | -0.001 |
| grewup_state_spouse_19_ms | 0.007 | -0.001 |
| time_leisure_spouse_19 | 10.4 | -0.001 |
| cost_transport_downpayment_11 | 1142.4 | -0.001 |
| grewup_state_spouse_17_me | 0.003 | -0.001 |
| grewup_state_spouse_13_tx | 0.022 | -0.001 |
| kids_youngest_15 | 7.8 | -0.001 |
| cost_food_away_11 | 2443.9 | -0.001 |
| grewup_state_spouse_11_ca | 0.037 | -0.001 |
| grewup_state_spouse_19_ca | 0.054 | -0.001 |
| grewup_state_self_la | 0.008 | -0.001 |
| vacationdays_spouse_13 | 1.0 | -0.001 |
| grewup_state_spouse_13_fl | 0.01 | -0.001 |
| hourlystatus_spouse_17_salaried | 0.194 | -0.002 |
| interview_number_19 | 4514.9 | -0.002 |
| cost_health_insurance_17 | 2755.0 | -0.002 |
| hourlystatus_spouse_11_hourlyplustips | 0.002 | -0.002 |
| time_work_annual_spouse_17 | 1123.4 | -0.002 |
| empstat_11_searching | 0.051 | -0.002 |
| grewup_state_spouse_17_ms | 0.007 | -0.002 |
| sizeworkplace_self_19 | 855.9 | -0.002 |
| cost_housing_insurance_13 | 682.6 | -0.002 |
| hourlystatus_spouse_15_salaried | 0.179 | -0.002 |
| ind_spouse_13_information | 0.01 | -0.002 |
| hourlystatus_self_13_hourlypluscomm | 0.003 | -0.002 |
| hourlystatus_self_13_salpluscomm | 0.011 | -0.002 |
| ind_spouse_13_mining | 0.002 | -0.002 |
| empstat_current_self_15_laid off | 0.002 | -0.002 |
| empstat_13_laid off | 0.003 | -0.002 |
| empstat_current_self_11_student | 0.01 | -0.002 |
| grewup_state_spouse_17_tn | 0.009 | -0.003 |
| grewup_state_spouse_15_ms | 0.006 | -0.003 |
| cost_transport_downpayment_15 | 1474.0 | -0.003 |
| time_work_spouse_17 | 21.9 | -0.003 |
| empstat_current_self_15_searching | 0.025 | -0.003 |
| grewup_state_spouse_13_nm | 0.001 | -0.003 |
| time_work_prevyear_sp_11 | 21.5 | -0.003 |
| grewup_state_spouse_19_mi | 0.025 | -0.003 |
| grewup_state_spouse_19_wv | 0.002 | -0.003 |
| ind_self_17_arts | 0.015 | -0.003 |
| cost_clothing_13 | 1628.9 | -0.003 |
| ind_self_11_management | 0.024 | -0.003 |
| time_work_annual_spouse_15 | 1136.5 | -0.003 |
| ind_spouse_13_utilities | 0.005 | -0.003 |
| grewup_state_self_az | 0.011 | -0.003 |
| grewup_state_spouse_17_mi | 0.022 | -0.003 |
| grewup_state_spouse_13_tn | 0.007 | -0.003 |
| grewup_state_spouse_17_mn | 0.008 | -0.004 |
| cost_clothing_11 | 1613.6 | -0.004 |
| cost_health_hospital_17 | 451.9 | -0.004 |
| grewup_state_spouse_19_hi | 0.001 | -0.004 |
| income_labor_spouse_15 | 31454.3 | -0.004 |
| hourlystatus_spouse_19_hourlyplustips | 0.002 | -0.004 |
| weight_indiv_cs_15 | 18488.0 | -0.004 |
| grewup_state_self_ms | 0.011 | -0.004 |
| grewup_state_spouse_15_mi | 0.019 | -0.004 |
| grewup_state_spouse_15_tn | 0.009 | -0.004 |
| grewup_state_self_md | 0.013 | -0.004 |
| weight_indiv_long_19 | 39.0 | -0.004 |
| empstat_current_self_15_working | 0.679 | -0.004 |
| hourlystatus_self_17_hourlyplustips | 0.006 | -0.004 |
| grewup_state_spouse_11_nm | 0.001 | -0.004 |
| ind_self_19_profsciencetech | 0.071 | -0.004 |
| grewup_state_spouse_19_me | 0.003 | -0.004 |
| wealth_homeequity_19 | 113197.8 | -0.004 |
| grewup_state_self_wy | 0.001 | -0.004 |
| ind_spouse_11_accomodationsfood | 0.019 | -0.004 |
| ind_self_17_health | 0.125 | -0.004 |
| sequence_number_17 | 2.1 | -0.004 |
| grewup_region_spouse_17_south | 0.149 | -0.005 |
| cost_computing_19 | 606.2 | -0.005 |
| empstat_11_working | 0.63 | -0.005 |
| empstat_current_self_11_searching | 0.036 | -0.005 |
| grewup_state_spouse_13_ky | 0.008 | -0.005 |
| grewup_state_spouse_15_nh | 0.001 | -0.005 |
| hh_size_11 | 3.1 | -0.005 |
| empstat_current_self_13_laid off | 0.003 | -0.005 |
| grewup_state_spouse_13_me | 0.003 | -0.005 |
| ind_self_19_health | 0.145 | -0.005 |
| grewup_state_spouse_15_la | 0.004 | -0.005 |
| daycare_11_no | 0.331 | -0.005 |
| grewup_state_spouse_11_ms | 0.005 | -0.005 |
| time_work_prevyear_spouse_17 | 39.7 | -0.005 |
| ind_self_13_otherservices | 0.031 | -0.005 |
| ind_self_19_wholesale | 0.031 | -0.005 |
| hourlystatus_spouse_19_other | 0.059 | -0.005 |
| weight_indiv_cs_11 | 15877.2 | -0.005 |
| cost_food_deliver_11 | 126.2 | -0.005 |
| cost_health_rx_13 | 437.7 | -0.005 |
| empstat_current_self_11_working | 0.579 | -0.006 |
| ind_self_11_otherservices | 0.03 | -0.006 |
| grewup_state_spouse_19_nm | 0.001 | -0.006 |
| ind_self_17_DKNARefused | 0.003 | -0.006 |
| grewup_state_spouse_15_ky | 0.008 | -0.006 |
| grewup_state_spouse_19_ky | 0.009 | -0.006 |
| time_education_self_17 | 1.4 | -0.006 |
| kids_num_15 | 0.828 | -0.006 |
| grewup_state_spouse_17_mt | 0.0 | -0.006 |
| ind_spouse_11_health | 0.059 | -0.006 |
| grewup_state_spouse_13_nj | 0.018 | -0.006 |
| grewup_state_spouse_19_sc | 0.009 | -0.006 |
| income_wagerate_spouse_13 | 16.0 | -0.006 |
| grewup_state_self_ct | 0.01 | -0.006 |
| time_work_prevyear_spouse_11 | 40.3 | -0.007 |
| hourlystatus_spouse_15_hourlyplustips | 0.001 | -0.007 |
| grewup_state_spouse_13_il | 0.015 | -0.007 |
| empstat_19_retired | 0.005 | -0.007 |
| grewup_state_spouse_11_ky | 0.008 | -0.007 |
| cost_housing_repairs_11 | 2250.2 | -0.007 |
| grewup_state_spouse_17_hi | 0.001 | -0.007 |
| cost_transport_downpayment_17 | 1499.3 | -0.007 |
| grewup_state_spouse_17_nm | 0.001 | -0.007 |
| ind_spouse_13_DKNARefused | 0.003 | -0.007 |
| cost_transport_other_11 | 136.0 | -0.007 |
| hourlystatus_self_17_hourly | 0.416 | -0.007 |
| grewup_state_spouse_11_il | 0.015 | -0.007 |
| vacationdays_spouse_19 | 1.1 | -0.007 |
| grewup_state_self_de | 0.0 | -0.007 |
| ind_spouse_11_utilities | 0.005 | -0.007 |
| cost_recreation_11 | 915.4 | -0.007 |
| grewup_state_spouse_15_ct | 0.004 | -0.007 |
| grewup_state_spouse_13_sd | 0.003 | -0.007 |
| empstat_15_laid off | 0.003 | -0.008 |
| time_work_prevyear_spouse_19 | 39.4 | -0.008 |
| hourlystatus_self_11_hourly | 0.283 | -0.008 |
| workweeks_spouse_13 | 27.5 | -0.008 |
| empstat_19_disabled | 0.001 | -0.008 |
| hourlystatus_self_15_hourly | 0.341 | -0.008 |
| hourlystatus_spouse_17_hourlypluscomm | 0.002 | -0.008 |
| grewup_state_spouse_17_la | 0.004 | -0.008 |
| hourlystatus_spouse_11_salaried | 0.16 | -0.008 |
| grewup_state_self_ri | 0.001 | -0.008 |
| grewup_state_spouse_11_mt | 0.0 | -0.008 |
| grewup_state_spouse_13_mt | 0.0 | -0.008 |
| grewup_state_spouse_15_mt | 0.0 | -0.008 |
| ind_spouse_11_retail | 0.036 | -0.008 |
| grewup_state_self_ne | 0.01 | -0.008 |
| time_childcare_self_19 | 8.9 | -0.008 |
| grewup_state_spouse_19_la | 0.004 | -0.008 |
| weight_indiv_cs_13 | 16678.1 | -0.009 |
| cost_health_17 | 4553.9 | -0.009 |
| grewup_state_spouse_17_ky | 0.008 | -0.009 |
| daycare_15_no | 0.283 | -0.009 |
| grewup_state_spouse_17_ct | 0.005 | -0.009 |
| empstat_13_working | 0.671 | -0.009 |
| grewup_state_spouse_17_md | 0.007 | -0.009 |
| grewup_state_spouse_11_sd | 0.003 | -0.009 |
| ind_spouse_13_profsciencetech | 0.031 | -0.009 |
| grewup_state_spouse_19_md | 0.008 | -0.009 |
| grewup_state_self_nm | 0.001 | -0.009 |
| grewup_state_spouse_13_ct | 0.004 | -0.009 |
| grewup_state_spouse_15_sd | 0.003 | -0.009 |
| cost_health_rx_17 | 400.9 | -0.009 |
| cost_health_bills_15 | 1806.8 | -0.009 |
| empstat_17_student | 0.007 | -0.009 |
| ind_self_15_profsciencetech | 0.055 | -0.01 |
| vacationdays_spouse_15 | 1.2 | -0.01 |
| ind_self_17_profsciencetech | 0.065 | -0.01 |
| grewup_state_spouse_17_nv | 0.001 | -0.01 |
| grewup_state_spouse_19_ar | 0.016 | -0.01 |
| ind_self_19_DKNARefused | 0.002 | -0.01 |
| empstat_15_student | 0.018 | -0.01 |
| grewup_state_spouse_11_pa | 0.029 | -0.01 |
| income_labor_spouse_17 | 32010.8 | -0.01 |
| wealth_homeequity_13 | 76027.1 | -0.01 |
| ind_self_11_accomodationsfood | 0.033 | -0.01 |
| grewup_state_spouse_13_pa | 0.031 | -0.01 |
| income_wagerate_spouse_11 | 15.5 | -0.01 |
| empstat_current_self_13_working | 0.624 | -0.01 |
| hourlystatus_spouse_17_hourlyplustips | 0.002 | -0.01 |
| grewup_size_spouse_11_other | 0.012 | -0.011 |
| ind_spouse_13_transportwarehouse | 0.017 | -0.011 |
| grewup_state_spouse_11_tn | 0.007 | -0.011 |
| ind_self_11_wholesale | 0.021 | -0.011 |
| grewup_state_spouse_19_ct | 0.005 | -0.011 |
| empstat_current_self_13_student | 0.012 | -0.011 |
| empstat_15_working | 0.724 | -0.011 |
| grewup_state_spouse_11_mi | 0.018 | -0.011 |
| grewup_state_spouse_19_wi | 0.009 | -0.011 |
| grewup_state_spouse_13_mi | 0.017 | -0.011 |
| cost_transport_downpayment_19 | 1762.0 | -0.011 |
| empstat_13_searching | 0.043 | -0.012 |
| cost_health_rx_11 | 407.4 | -0.012 |
| kids_num_13 | 0.921 | -0.012 |
| grewup_state_spouse_15_nv | 0.001 | -0.012 |
| grewup_state_spouse_11_la | 0.003 | -0.012 |
| ind_spouse_13_accomodationsfood | 0.018 | -0.012 |
| grewup_state_self_ak | 0.001 | -0.012 |
| ind_self_17_wholesale | 0.027 | -0.012 |
| ind_spouse_11_management | 0.014 | -0.012 |
| ind_self_17_otherservices | 0.043 | -0.012 |
| ind_spouse_11_adminmilitary | 0.03 | -0.012 |
| grewup_region_spouse_19_akhi | 0.001 | -0.012 |
| grewup_state_spouse_17_ne | 0.006 | -0.012 |
| grewup_state_spouse_15_ak | 0.001 | -0.012 |
| grewup_state_spouse_13_ar | 0.013 | -0.012 |
| grewup_state_spouse_17_wi | 0.009 | -0.012 |
| kids_num_11 | 0.99 | -0.012 |
| grewup_state_spouse_13_ak | 0.001 | -0.012 |
| grewup_state_spouse_11_ri | 0.0 | -0.013 |
| cost_health_bills_11 | 776.7 | -0.013 |
| grewup_state_spouse_11_ct | 0.003 | -0.013 |
| ind_self_11_profsciencetech | 0.046 | -0.013 |
| ind_self_15_DKNARefused | 0.002 | -0.013 |
| ind_spouse_13_adminmilitary | 0.031 | -0.013 |
| ind_spouse_13_management | 0.013 | -0.013 |
| cost_transport_leases_13 | 279.0 | -0.013 |
| hourlystatus_spouse_15_hourly | 0.196 | -0.013 |
| empstat_11_disabled | 0.004 | -0.013 |
| hourlystatus_self_19_hourly | 0.502 | -0.013 |
| hourlystatus_self_13_hourly | 0.308 | -0.013 |
| grewup_state_spouse_17_sc | 0.007 | -0.013 |
| grewup_state_self_ok | 0.008 | -0.013 |
| grewup_state_spouse_17_nc | 0.013 | -0.013 |
| grewup_state_spouse_17_ar | 0.014 | -0.013 |
| cost_health_bills_13 | 840.5 | -0.013 |
| grewup_state_self_mi | 0.038 | -0.013 |
| time_leisure_spouse_17 | 10.4 | -0.013 |
| cost_health_15 | 4521.2 | -0.013 |
| cost_health_doctor_11 | 715.0 | -0.013 |
| grewup_state_spouse_15_ar | 0.014 | -0.013 |
| grewup_state_spouse_19_nc | 0.015 | -0.013 |
| grewup_state_spouse_15_sc | 0.007 | -0.014 |
| grewup_state_spouse_17_ak | 0.001 | -0.014 |
| empstat_current_self_11_other | 0.001 | -0.014 |
| grewup_state_spouse_15_il | 0.015 | -0.014 |
| cost_health_doctor_17 | 946.1 | -0.014 |
| grewup_state_self_pa | 0.047 | -0.014 |
| grewup_state_spouse_13_wi | 0.007 | -0.014 |
| grewup_state_self_nc | 0.023 | -0.014 |
| grewup_region_spouse_17_akhi | 0.001 | -0.014 |
| sizeworkplace_spouse_11 | 15028.9 | -0.014 |
| empstat_11_laid off | 0.003 | -0.014 |
| grewup_state_spouse_13_ri | 0.0 | -0.014 |
| grewup_state_spouse_15_ri | 0.0 | -0.014 |
| ind_self_15_otherservices | 0.035 | -0.014 |
| grewup_state_spouse_13_id | 0.002 | -0.014 |
| time_volunteering_spouse_19 | 0.827 | -0.014 |
| grewup_state_spouse_19_ak | 0.001 | -0.014 |
| grewup_state_spouse_17_ri | 0.0 | -0.014 |
| grewup_state_spouse_19_ri | 0.0 | -0.014 |
| grewup_state_spouse_15_az | 0.005 | -0.014 |
| hourlystatus_self_15_hourlypluscomm | 0.003 | -0.014 |
| grewup_state_spouse_13_la | 0.003 | -0.014 |
| cost_health_insurance_15 | 2681.4 | -0.014 |
| grewup_state_self_nd | 0.002 | -0.014 |
| grewup_state_spouse_13_md | 0.005 | -0.014 |
| grewup_state_self_sc | 0.017 | -0.015 |
| ind_self_15_accomodationsfood | 0.038 | -0.015 |
| cost_health_hospital_15 | 455.0 | -0.015 |
| income_wagerate_spouse_17 | 16.8 | -0.015 |
| hourlystatus_spouse_13_hourlypluscomm | 0.002 | -0.015 |
| empstat_current_self_13_searching | 0.03 | -0.015 |
| ind_spouse_13_retail | 0.037 | -0.015 |
| grewup_state_spouse_17_sd | 0.003 | -0.015 |
| grewup_state_spouse_11_ar | 0.013 | -0.015 |
| grewup_state_self_nv | 0.001 | -0.015 |
| grewup_state_spouse_11_sc | 0.006 | -0.015 |
| grewup_state_spouse_19_sd | 0.003 | -0.015 |
| grewup_state_spouse_17_az | 0.006 | -0.015 |
| sequence_number_11 | 2.4 | -0.015 |
| hourlystatus_self_13_hourlyplustips | 0.003 | -0.015 |
| grewup_state_spouse_11_id | 0.002 | -0.015 |
| time_childcare_self_17 | 9.8 | -0.015 |
| grewup_state_spouse_19_az | 0.008 | -0.015 |
| grewup_state_spouse_19_or | 0.012 | -0.015 |
| sizeworkplace_spouse_15 | 732.7 | -0.016 |
| sizeworkplace_spouse_13 | 731.3 | -0.016 |
| grewup_state_spouse_15_wi | 0.008 | -0.016 |
| grewup_state_spouse_13_sc | 0.007 | -0.016 |
| ind_spouse_11_profsciencetech | 0.025 | -0.016 |
| grewup_size_spouse_17_other | 0.014 | -0.016 |
| income_labor_spouse_13 | 29476.7 | -0.016 |
| grewup_state_spouse_19_mo | 0.018 | -0.016 |
| grewup_size_spouse_19_other | 0.016 | -0.016 |
| grewup_state_spouse_13_nv | 0.001 | -0.016 |
| grewup_state_spouse_11_ak | 0.001 | -0.016 |
| ind_self_11_DKNARefused | 0.002 | -0.016 |
| cost_housing_repairs_15 | 1912.5 | -0.016 |
| ind_self_13_DKNARefused | 0.003 | -0.016 |
| grewup_region_spouse_15_south | 0.137 | -0.017 |
| time_volunteering_self_17 | 1.1 | -0.017 |
| time_pcare_self_17 | 7.5 | -0.017 |
| grewup_state_spouse_11_wi | 0.007 | -0.017 |
| grewup_state_self_wi | 0.011 | -0.017 |
| wealth_15 | 322932.2 | -0.017 |
| ind_self_13_accomodationsfood | 0.036 | -0.017 |
| grewup_state_spouse_11_ne | 0.006 | -0.017 |
| grewup_size_spouse_13_other | 0.013 | -0.017 |
| hourlystatus_self_17_hourlypluscomm | 0.003 | -0.017 |
| cost_recreation_13 | 999.7 | -0.017 |
| grewup_state_spouse_11_md | 0.005 | -0.017 |
| cost_transport_downpayment_13 | 1224.7 | -0.017 |
| time_pcare_self_19 | 7.5 | -0.017 |
| ind_spouse_13_construction | 0.025 | -0.018 |
| grewup_state_self_sd | 0.005 | -0.018 |
| hourlystatus_spouse_11_salpluscomm | 0.005 | -0.018 |
| ind_spouse_11_transportwarehouse | 0.018 | -0.018 |
| grewup_state_spouse_11_va | 0.014 | -0.018 |
| cost_trips_11 | 1954.0 | -0.018 |
| grewup_state_spouse_11_az | 0.005 | -0.018 |
| empstat_15_disabled | 0.006 | -0.018 |
| grewup_state_spouse_15_ne | 0.006 | -0.018 |
| grewup_state_self_nh | 0.001 | -0.018 |
| grewup_state_self_wa | 0.021 | -0.018 |
| ind_self_13_realestate | 0.014 | -0.018 |
| grewup_state_spouse_15_md | 0.006 | -0.018 |
| hourlystatus_spouse_11_hourly | 0.175 | -0.018 |
| grewup_state_self_fl | 0.027 | -0.018 |
| time_work_prevyear_spouse_13 | 40.6 | -0.018 |
| ind_self_19_accomodationsfood | 0.055 | -0.019 |
| grewup_size_spouse_15_other | 0.014 | -0.019 |
| hourlystatus_self_15_hourlyplustips | 0.004 | -0.019 |
| cost_transport_other_15 | 195.9 | -0.019 |
| cost_health_hospital_11 | 364.8 | -0.019 |
| grewup_state_spouse_17_va | 0.017 | -0.019 |
| empstat_15_other | 0.001 | -0.019 |
| cost_health_insurance_13 | 2595.9 | -0.019 |
| wealth_other_15 | 232885.0 | -0.019 |
| grewup_state_spouse_17_oh | 0.028 | -0.02 |
| empstat_current_self_11_laid off | 0.002 | -0.02 |
| ind_self_11_realestate | 0.012 | -0.02 |
| grewup_size_spouse_17_suburban | 0.348 | -0.02 |
| grewup_state_spouse_15_nc | 0.013 | -0.02 |
| ind_self_13_wholesale | 0.021 | -0.02 |
| grewup_state_spouse_19_in | 0.017 | -0.02 |
| vacationdays_spouse_17 | 1.0 | -0.02 |
| grewup_state_spouse_19_oh | 0.03 | -0.02 |
| grewup_state_spouse_17_or | 0.012 | -0.02 |
| grewup_state_spouse_13_az | 0.005 | -0.02 |
| hourlystatus_spouse_17_salpluscomm | 0.006 | -0.02 |
| grewup_state_spouse_17_in | 0.017 | -0.02 |
| grewup_state_spouse_13_nd | 0.001 | -0.02 |
| grewup_state_spouse_11_nd | 0.001 | -0.02 |
| grewup_state_spouse_15_nd | 0.001 | -0.02 |
| grewup_state_spouse_17_nd | 0.001 | -0.02 |
| ind_self_11_health | 0.088 | -0.02 |
| grewup_state_spouse_13_nc | 0.012 | -0.021 |
| grewup_state_spouse_13_va | 0.015 | -0.021 |
| grewup_state_spouse_17_id | 0.002 | -0.021 |
| grewup_state_spouse_19_ne | 0.007 | -0.021 |
| ind_self_15_arts | 0.012 | -0.021 |
| grewup_state_spouse_15_va | 0.017 | -0.021 |
| grewup_state_spouse_11_in | 0.012 | -0.021 |
| interview_number_17 | 4427.9 | -0.021 |
| ind_spouse_11_wholesale | 0.013 | -0.021 |
| time_work_annual_spouse_13 | 1145.6 | -0.021 |
| daycare_13_no | 0.3 | -0.021 |
| grewup_state_spouse_11_nv | 0.001 | -0.021 |
| ind_self_13_profsciencetech | 0.048 | -0.021 |
| grewup_state_spouse_11_oh | 0.023 | -0.021 |
| time_adultcare_spouse_19 | 0.468 | -0.021 |
| cost_health_rx_15 | 416.3 | -0.021 |
| cost_health_13 | 4342.9 | -0.021 |
| grewup_state_spouse_15_oh | 0.026 | -0.022 |
| grewup_state_spouse_13_or | 0.011 | -0.022 |
| grewup_state_spouse_19_nd | 0.001 | -0.022 |
| grewup_state_spouse_15_or | 0.011 | -0.022 |
| time_adultcare_self_17 | 0.76 | -0.022 |
| hourlystatus_self_11_hourlyplustips | 0.004 | -0.022 |
| ind_self_11_arts | 0.011 | -0.022 |
| ind_self_15_realestate | 0.015 | -0.022 |
| grewup_state_spouse_15_in | 0.014 | -0.022 |
| grewup_state_spouse_11_or | 0.01 | -0.023 |
| ind_self_15_wholesale | 0.021 | -0.023 |
| grewup_state_spouse_11_nc | 0.011 | -0.023 |
| grewup_size_self_suburban | 0.534 | -0.023 |
| income_labor_spouse_11 | 28803.1 | -0.023 |
| grewup_state_spouse_17_ks | 0.003 | -0.023 |
| empstat_17_disabled | 0.004 | -0.023 |
| age_self_17 | 44.4 | -0.023 |
| grewup_state_spouse_19_va | 0.02 | -0.023 |
| hourlystatus_spouse_15_other | 0.04 | -0.023 |
| workweeks_spouse_11 | 27.7 | -0.023 |
| time_education_self_19 | 1.3 | -0.024 |
| ind_self_13_health | 0.095 | -0.024 |
| empstat_19_housespouse | 0.003 | -0.024 |
| grewup_state_spouse_13_in | 0.012 | -0.024 |
| ind_spouse_13_manufacturing | 0.049 | -0.024 |
| grewup_state_spouse_15_ks | 0.003 | -0.024 |
| hourlystatus_spouse_19_salpluscomm | 0.007 | -0.024 |
| grewup_state_self_co | 0.015 | -0.024 |
| empstat_13_disabled | 0.005 | -0.024 |
| grewup_state_self_oh | 0.045 | -0.024 |
| grewup_state_spouse_13_oh | 0.025 | -0.024 |
| weight_indiv_long_17 | 27.7 | -0.025 |
| grewup_state_spouse_15_co | 0.009 | -0.025 |
| grewup_state_spouse_13_co | 0.009 | -0.025 |
| ind_self_17_realestate | 0.019 | -0.025 |
| hourlystatus_spouse_11_other | 0.038 | -0.025 |
| grewup_state_self_or | 0.019 | -0.026 |
| relation_to_head_15 | 13.3 | -0.026 |
| grewup_region_spouse_19_west | 0.114 | -0.026 |
| hourlystatus_spouse_13_salpluscomm | 0.007 | -0.026 |
| wealth_homeequity_11 | 71754.9 | -0.026 |
| grewup_state_spouse_19_ks | 0.003 | -0.026 |
| relation_to_head_13 | 13.3 | -0.026 |
| weight_indiv_long_11 | 25.1 | -0.026 |
| age_self_19 | 45.2 | -0.027 |
| hourlystatus_spouse_15_salpluscomm | 0.007 | -0.027 |
| grewup_state_spouse_13_ne | 0.005 | -0.027 |
| flag_allyears | 0.831 | -0.027 |
| grewup_state_self_mo | 0.025 | -0.027 |
| age_self_13 | 43.0 | -0.027 |
| weight_indiv_long_13 | 24.9 | -0.027 |
| grewup_state_spouse_11_co | 0.008 | -0.027 |
| educyrs_11 | 10.3 | -0.027 |
| age_spouse_17 | 45.7 | -0.027 |
| grewup_state_spouse_19_wa | 0.014 | -0.028 |
| hourlystatus_spouse_13_hourly | 0.184 | -0.028 |
| grewup_state_spouse_15_id | 0.001 | -0.028 |
| grewup_state_spouse_19_id | 0.002 | -0.028 |
| ind_spouse_11_construction | 0.026 | -0.028 |
| ind_self_13_arts | 0.012 | -0.028 |
| grewup_state_self_va | 0.025 | -0.028 |
| grewup_state_self_ar | 0.02 | -0.028 |
| grewup_region_spouse_17_west | 0.099 | -0.028 |
| grewup_region_spouse_15_west | 0.092 | -0.029 |
| cost_health_hospital_13 | 373.1 | -0.029 |
| ind_spouse_11_manufacturing | 0.051 | -0.029 |
| interview_number_15 | 4031.3 | -0.029 |
| ind_self_15_retail | 0.059 | -0.029 |
| grewup_state_spouse_17_co | 0.009 | -0.029 |
| grewup_state_spouse_13_mo | 0.015 | -0.029 |
| weight_indiv_long_15 | 28.1 | -0.03 |
| ind_self_11_retail | 0.051 | -0.03 |
| grewup_state_spouse_13_ks | 0.002 | -0.03 |
| ind_self_15_health | 0.105 | -0.031 |
| grewup_state_spouse_11_ks | 0.002 | -0.031 |
| age_self_15 | 44.1 | -0.031 |
| grewup_state_self_ks | 0.004 | -0.031 |
| grewup_state_spouse_19_co | 0.011 | -0.031 |
| ind_self_15_education | 0.06 | -0.031 |
| empstat_13_retired | 0.008 | -0.031 |
| empstat_17_housespouse | 0.019 | -0.032 |
| grewup_size_spouse_17_country | 0.058 | -0.032 |
| age_self_11 | 42.1 | -0.032 |
| time_shopping_self_17 | 3.5 | -0.032 |
| wealth_other_11 | 179290.9 | -0.033 |
| ind_self_13_education | 0.058 | -0.034 |
| ind_self_11_education | 0.052 | -0.034 |
| grewup_size_spouse_15_suburban | 0.303 | -0.034 |
| ind_self_17_education | 0.073 | -0.034 |
| grewup_size_spouse_11_country | 0.054 | -0.034 |
| ind_self_13_retail | 0.054 | -0.034 |
| time_leisure_self_17 | 14.3 | -0.034 |
| grewup_size_spouse_19_country | 0.063 | -0.034 |
| ind_self_19_farmfishforest | 0.019 | -0.035 |
| ind_self_19_education | 0.082 | -0.035 |
| wealth_11 | 251045.9 | -0.035 |
| grewup_state_spouse_17_wa | 0.013 | -0.035 |
| grewup_state_spouse_17_mo | 0.015 | -0.036 |
| time_work_annual_spouse_11 | 1156.4 | -0.036 |
| wealth_17 | 323752.8 | -0.036 |
| relation_to_head_19 | 13.2 | -0.036 |
| grewup_state_spouse_11_mo | 0.015 | -0.036 |
| age_spouse_19 | 46.5 | -0.036 |
| grewup_state_spouse_15_mo | 0.016 | -0.036 |
| age_spouse_15 | 45.4 | -0.036 |
| ind_self_19_otherservices | 0.054 | -0.036 |
| grewup_state_spouse_11_wa | 0.011 | -0.036 |
| hourlystatus_self_19_hourlyplustips | 0.007 | -0.036 |
| iswf_19 | 0.312 | -0.036 |
| sequence_number_19 | 1.3 | -0.036 |
| ind_self_19_realestate | 0.021 | -0.037 |
| grewup_state_self_in | 0.029 | -0.037 |
| time_volunteering_self_19 | 0.957 | -0.037 |
| grewup_size_spouse_13_suburban | 0.281 | -0.037 |
| grewup_state_spouse_13_wa | 0.012 | -0.037 |
| cost_health_11 | 3321.4 | -0.037 |
| educyrs_13 | 10.7 | -0.037 |
| educyrs_15 | 11.4 | -0.037 |
| relation_to_head_11 | 13.4 | -0.038 |
| grewup_state_spouse_15_wa | 0.013 | -0.038 |
| grewup_size_spouse_13_country | 0.053 | -0.038 |
| ind_spouse_13_farmfishforest | 0.009 | -0.038 |
| empstat_11_housespouse | 0.027 | -0.039 |
| grewup_size_spouse_11_suburban | 0.268 | -0.039 |
| ind_spouse_11_farmfishforest | 0.008 | -0.04 |
| wealth_19 | 358002.2 | -0.04 |
| ind_self_13_farmfishforest | 0.015 | -0.04 |
| ind_self_17_farmfishforest | 0.018 | -0.04 |
| empstat_11_retired | 0.007 | -0.04 |
| wealth_13 | 255084.8 | -0.04 |
| wealth_other_17 | 226265.8 | -0.041 |
| grewup_state_spouse_19_ia | 0.018 | -0.041 |
| grewup_state_spouse_15_ia | 0.016 | -0.041 |
| time_housework_self_19 | 9.7 | -0.041 |
| grewup_size_spouse_15_country | 0.054 | -0.042 |
| empstat_15_retired | 0.013 | -0.042 |
| cost_health_insurance_11 | 1834.2 | -0.042 |
| ind_self_11_farmfishforest | 0.013 | -0.042 |
| wealth_other_13 | 179057.6 | -0.042 |
| time_leisure_self_19 | 13.9 | -0.042 |
| grewup_state_spouse_17_ia | 0.017 | -0.042 |
| wealth_other_19 | 244804.4 | -0.043 |
| time_adultcare_self_19 | 0.756 | -0.043 |
| iswf_17 | 0.279 | -0.044 |
| grewup_state_spouse_13_ia | 0.016 | -0.044 |
| grewup_state_self_ia | 0.026 | -0.045 |
| grewup_state_spouse_11_ia | 0.015 | -0.047 |
| ind_self_17_retail | 0.068 | -0.047 |
| empstat_13_housespouse | 0.024 | -0.048 |
| ind_self_15_farmfishforest | 0.016 | -0.048 |
| time_housework_self_17 | 10.2 | -0.048 |
| age_spouse_11 | 43.4 | -0.049 |
| age_spouse_13 | 44.3 | -0.049 |
| time_housework_self_13 | 10.4 | -0.049 |
| empstat_15_housespouse | 0.024 | -0.049 |
| grewup_size_self_country | 0.092 | -0.05 |
| time_shopping_self_19 | 3.5 | -0.052 |
| ind_self_19_retail | 0.079 | -0.053 |
| time_housework_self_11 | 10.6 | -0.054 |
| grewup_region_spouse_19_northcentral | 0.161 | -0.054 |
| grewup_region_spouse_17_northcentral | 0.147 | -0.059 |
| hourlystatus_self_13_other | 0.07 | -0.059 |
| iswf_15 | 0.245 | -0.063 |
| hourlystatus_self_15_other | 0.071 | -0.064 |
| hourlystatus_self_17_other | 0.086 | -0.067 |
| hourlystatus_self_11_other | 0.063 | -0.069 |
| iswf_13 | 0.233 | -0.078 |
| empstat_19_other | 0.0 | nan |
| logcost_transport_bustrain_19 | 0.656 | 0.177 |
| logcost_transport_bustrain_17 | 0.627 | 0.157 |
| logcost_transport_bustrain_13 | 0.637 | 0.135 |
| logcost_transport_bustrain_11 | 0.61 | 0.132 |
| logincome_wagerate_self_19 | 3.0 | 0.132 |
| logincome_labor_self_19 | 10.2 | 0.124 |
| logincome_wagerate_self_17 | 2.9 | 0.118 |
| logcost_transport_bustrain_15 | 0.612 | 0.115 |
| logincome_wagerate_self_13 | 2.8 | 0.111 |
| logincome_wagerate_self_15 | 2.9 | 0.109 |
| logincome_labor_self_17 | 9.8 | 0.108 |
| logincome_wagerate_self_11 | 2.8 | 0.099 |
| logcost_housing_19 | 9.9 | 0.094 |
| logincome_labor_self_15 | 9.7 | 0.091 |
| logcost_total_19 | 10.8 | 0.09 |
| logincome_labor_self_11 | 9.4 | 0.084 |
| occ_self_19_constructionextraction | 0.055 | 0.082 |
| logcost_transport_19 | 8.9 | 0.081 |
| logincome_labor_self_13 | 9.6 | 0.08 |
| logcost_total_with_rent_value_19 | 10.9 | 0.08 |
| region_19_northeast | 0.177 | 0.078 |
| region_17_northeast | 0.172 | 0.075 |
| state_19_ny | 0.053 | 0.074 |
| logcost_transport_parking_17 | 0.732 | 0.072 |
| grewup_region_self_foreign | 0.156 | 0.072 |
| logcost_housing_17 | 9.8 | 0.07 |
| logcost_transport_parking_15 | 0.657 | 0.07 |
| state_17_ny | 0.052 | 0.068 |
| logcost_childcare_17 | 1.1 | 0.065 |
| logcost_transport_17 | 8.8 | 0.065 |
| state_17_nj | 0.031 | 0.065 |
| logincome_familytotal_19 | 11.3 | 0.064 |
| sex_spouse_19_female | 0.396 | 0.064 |
| state_19_nj | 0.033 | 0.063 |
| occ_self_17_constructionextraction | 0.048 | 0.062 |
| state_11_nj | 0.035 | 0.061 |
| state_15_nj | 0.033 | 0.056 |
| logcost_transport_parking_19 | 0.78 | 0.056 |
| occ_self_13_constructionextraction | 0.034 | 0.055 |
| occ_self_15_constructionextraction | 0.038 | 0.055 |
| logcost_transport_parking_13 | 0.562 | 0.055 |
| region_11_northeast | 0.167 | 0.054 |
| empstat_current_self_19_working | 0.951 | 0.054 |
| religion_spouse_17_catholic | 0.172 | 0.051 |
| region_15_northeast | 0.163 | 0.051 |
| state_13_nj | 0.034 | 0.05 |
| sex_male | 0.524 | 0.05 |
| sex_self_19_male | 0.524 | 0.05 |
| state_19_ma | 0.029 | 0.05 |
| logcost_transport_parking_11 | 0.488 | 0.049 |
| logcost_transport_other_19 | 0.251 | 0.049 |
| region_13_northeast | 0.165 | 0.048 |
| union_self_19_no | 0.736 | 0.048 |
| sex_spouse_17_female | 0.355 | 0.048 |
| logcost_transport_gas_19 | 7.0 | 0.046 |
| logcost_housing_telecom_19 | 7.7 | 0.046 |
| logcost_housing_13 | 9.7 | 0.046 |
| occ_self_11_constructionextraction | 0.03 | 0.045 |
| state_13_ny | 0.05 | 0.045 |
| race_spouse_17_other | 0.037 | 0.044 |
| religion_spouse_15_catholic | 0.148 | 0.044 |
| grewup_region_spouse_15_foreign | 0.063 | 0.044 |
| state_17_ma | 0.028 | 0.043 |
| race_spouse_19_other | 0.043 | 0.042 |
| logcost_transport_additionalvehicle_11 | 2.5 | 0.042 |
| state_11_ny | 0.049 | 0.042 |
| religion_self_17_jewish | 0.019 | 0.042 |
| occ_self_17_architectengineering | 0.017 | 0.042 |
| logcost_transport_15 | 8.8 | 0.042 |
| logcost_housing_11 | 9.7 | 0.041 |
| state_11_fl | 0.044 | 0.041 |
| state_15_ny | 0.049 | 0.041 |
| union_self_17_no | 0.613 | 0.041 |
| state_19_ca | 0.116 | 0.041 |
| occ_spouse_19_healthcaresupport | 0.015 | 0.041 |
| religion_spouse_13_catholic | 0.14 | 0.04 |
| religion_spouse_11_catholic | 0.138 | 0.04 |
| logcost_food_19 | 9.1 | 0.039 |
| empstat_current_spouse_19_housespouse | 0.092 | 0.039 |
| logcost_health_19 | 7.1 | 0.039 |
| state_17_ca | 0.11 | 0.039 |
| logcost_childcare_19 | 1.1 | 0.039 |
| religion_self_19_none | 0.0 | 0.038 |
| logcost_health_insurance_19 | 5.6 | 0.038 |
| logcost_transport_13 | 8.8 | 0.038 |
| logincome_familytotal_17 | 11.2 | 0.037 |
| logcost_education_13 | 2.7 | 0.037 |
| union_self_19_yes | 0.124 | 0.037 |
| grewup_region_spouse_13_foreign | 0.061 | 0.036 |
| logcost_housing_mortgage_19 | 4.6 | 0.036 |
| logcost_housing_rent_13 | 2.9 | 0.036 |
| grewup_region_spouse_11_foreign | 0.059 | 0.036 |
| logcost_transport_11 | 8.8 | 0.036 |
| state_11_ma | 0.026 | 0.035 |
| religion_self_17_catholic | 0.226 | 0.035 |
| state_17_md | 0.017 | 0.035 |
| logcost_transport_gas_17 | 7.0 | 0.035 |
| state_15_ma | 0.025 | 0.035 |
| logcost_education_11 | 2.9 | 0.035 |
| occ_self_19_architectengineering | 0.019 | 0.034 |
| occ_spouse_19_janitors | 0.023 | 0.034 |
| logcost_transport_taxi_17 | 0.718 | 0.034 |
| sex_self_17_male | 0.467 | 0.034 |
| ind_spouse_19_financeinsurance | 0.034 | 0.034 |
| religion_self_15_jewish | 0.018 | 0.034 |
| logcost_transport_repair_19 | 5.2 | 0.034 |
| union_self_17_yes | 0.1 | 0.033 |
| sex_self_15_male | 0.394 | 0.033 |
| occ_self_13_architectengineering | 0.015 | 0.033 |
| occ_self_15_architectengineering | 0.014 | 0.033 |
| grewup_region_self_northeast | 0.18 | 0.032 |
| state_13_ma | 0.025 | 0.032 |
| union_spouse_19_yes | 0.069 | 0.032 |
| logcost_housing_telecom_17 | 7.7 | 0.032 |
| logcost_food_athome_17 | 8.6 | 0.032 |
| logcost_transport_additionalvehicle_19 | 2.5 | 0.032 |
| ind_spouse_17_health | 0.082 | 0.032 |
| moved_17_yes | 0.307 | 0.031 |
| race_self_17_other | 0.049 | 0.031 |
| logcost_health_hospital_17 | 1.6 | 0.031 |
| sex_spouse_15_female | 0.301 | 0.031 |
| grewup_region_spouse_11_northeast | 0.097 | 0.031 |
| empstat_current_spouse_17_housespouse | 0.081 | 0.031 |
| logcost_transport_additionalvehicle_15 | 2.1 | 0.031 |
| logcost_clothing_19 | 6.5 | 0.03 |
| state_17_ga | 0.027 | 0.03 |
| moved_why_17_consmore | 0.052 | 0.03 |
| logcost_transport_downpayment_15 | 1.8 | 0.03 |
| state_13_fl | 0.047 | 0.03 |
| state_11_md | 0.017 | 0.03 |
| ind_spouse_19_education | 0.065 | 0.03 |
| logcost_housing_15 | 9.7 | 0.029 |
| logcost_transport_taxi_19 | 0.829 | 0.029 |
| logcost_housing_telecom_13 | 7.6 | 0.029 |
| occ_spouse_15_education | 0.038 | 0.029 |
| race_spouse_11_other | 0.021 | 0.029 |
| state_13_ca | 0.094 | 0.028 |
| logcost_food_17 | 9.0 | 0.028 |
| state_19_ga | 0.028 | 0.028 |
| state_13_ga | 0.02 | 0.028 |
| logcost_housing_rent_11 | 2.8 | 0.028 |
| religion_spouse_17_jewish | 0.015 | 0.027 |
| race_self_19_other | 0.059 | 0.027 |
| occ_self_19_businessfinance | 0.053 | 0.027 |
| empstat_current_spouse_11_housespouse | 0.064 | 0.027 |
| ind_spouse_17_education | 0.058 | 0.027 |
| logincome_familytotal_15 | 11.2 | 0.027 |
| state_15_fl | 0.048 | 0.027 |
| state_11_ga | 0.02 | 0.026 |
| logcost_childcare_15 | 1.0 | 0.026 |
| grewup_region_spouse_13_northeast | 0.102 | 0.026 |
| state_15_md | 0.016 | 0.026 |
| logcost_childcare_11 | 1.1 | 0.026 |
| religion_self_11_jewish | 0.017 | 0.026 |
| union_self_13_yes | 0.08 | 0.026 |
| state_19_md | 0.019 | 0.026 |
| occ_spouse_13_education | 0.036 | 0.026 |
| logcost_food_deliver_15 | 0.681 | 0.026 |
| religion_spouse_15_jewish | 0.014 | 0.026 |
| logincome_wagerate_spouse_19 | 1.8 | 0.026 |
| occ_self_19_janitors | 0.042 | 0.026 |
| logcost_food_deliver_19 | 0.774 | 0.026 |
| occ_spouse_17_healthcaresupport | 0.016 | 0.026 |
| state_15_ca | 0.098 | 0.026 |
| race_spouse_13_other | 0.022 | 0.025 |
| religion_self_13_jewish | 0.017 | 0.025 |
| logincome_labor_spouse_19 | 5.9 | 0.025 |
| state_13_md | 0.016 | 0.025 |
| occ_spouse_11_DKNARefused | 0.002 | 0.025 |
| empstat_current_spouse_13_student | 0.007 | 0.024 |
| union_spouse_11_yes | 0.051 | 0.024 |
| occ_spouse_17_education | 0.041 | 0.024 |
| logcost_education_17 | 2.3 | 0.023 |
| union_self_11_yes | 0.08 | 0.023 |
| logcost_transport_loans_19 | 2.7 | 0.023 |
| logcost_transport_loans_15 | 2.8 | 0.023 |
| occ_self_19_protective | 0.023 | 0.023 |
| logcost_transport_leases_15 | 0.684 | 0.023 |
| occ_self_17_protective | 0.02 | 0.023 |
| religion_spouse_11_jewish | 0.013 | 0.023 |
| logcost_food_athome_19 | 8.6 | 0.023 |
| logcost_transport_repair_13 | 3.5 | 0.023 |
| union_spouse_13_yes | 0.049 | 0.023 |
| logcost_education_15 | 2.5 | 0.023 |
| race_spouse_15_other | 0.024 | 0.022 |
| logcost_transport_taxi_15 | 0.39 | 0.022 |
| logcost_transport_leases_17 | 0.717 | 0.022 |
| logcost_housing_mortgage_17 | 4.6 | 0.022 |
| ind_spouse_15_education | 0.052 | 0.022 |
| state_11_ca | 0.097 | 0.022 |
| union_self_15_yes | 0.089 | 0.022 |
| occ_spouse_19_education | 0.045 | 0.022 |
| occ_self_19_repair | 0.034 | 0.022 |
| occ_self_13_production | 0.041 | 0.022 |
| state_15_ga | 0.022 | 0.021 |
| logcost_transport_additionalvehicle_17 | 2.2 | 0.021 |
| logincome_familytotal_13 | 11.1 | 0.021 |
| race_self_13_pacis | 0.002 | 0.021 |
| religion_self_11_catholic | 0.178 | 0.021 |
| empstat_current_spouse_19_working | 0.522 | 0.021 |
| occ_self_11_businessfinance | 0.031 | 0.021 |
| own_or_rent_13_rent | 0.286 | 0.021 |
| moved_why_19_productive | 0.019 | 0.021 |
| occ_spouse_19_pcareservice | 0.019 | 0.021 |
| race_self_11_pacis | 0.002 | 0.02 |
| occ_spouse_19_arts | 0.018 | 0.02 |
| empstat_current_self_19_laid off | 0.005 | 0.02 |
| race_self_15_other | 0.031 | 0.02 |
| union_spouse_17_yes | 0.06 | 0.02 |
| ind_spouse_17_realestate | 0.011 | 0.02 |
| moved_why_17_consother | 0.092 | 0.02 |
| ind_spouse_19_health | 0.092 | 0.02 |
| race_self_19_black | 0.111 | 0.02 |
| race_spouse_11_pacis | 0.001 | 0.02 |
| religion_self_15_catholic | 0.195 | 0.02 |
| logcost_food_deliver_17 | 0.681 | 0.02 |
| empstat_current_spouse_15_housespouse | 0.068 | 0.02 |
| occ_spouse_19_softscience | 0.015 | 0.02 |
| race_spouse_13_pacis | 0.001 | 0.02 |
| ind_spouse_17_financeinsurance | 0.029 | 0.02 |
| occ_spouse_17_arts | 0.016 | 0.02 |
| religion_self_19_catholic | 0.173 | 0.019 |
| mightmove_19_yes | 0.316 | 0.019 |
| religion_self_13_catholic | 0.182 | 0.019 |
| ind_spouse_15_financeinsurance | 0.028 | 0.019 |
| occ_self_13_compscimath | 0.02 | 0.019 |
| state_11_ut | 0.01 | 0.019 |
| occ_spouse_19_sales | 0.05 | 0.019 |
| religion_spouse_13_jewish | 0.013 | 0.019 |
| logcost_health_insurance_17 | 5.6 | 0.019 |
| ind_spouse_15_otherservices | 0.023 | 0.019 |
| logincome_labor_spouse_15 | 6.1 | 0.019 |
| own_or_rent_17_rent | 0.333 | 0.019 |
| race_spouse_19_asian | 0.051 | 0.019 |
| union_spouse_15_yes | 0.054 | 0.019 |
| state_17_il | 0.022 | 0.018 |
| ind_spouse_19_management | 0.02 | 0.018 |
| occ_self_11_architectengineering | 0.011 | 0.018 |
| race_self_13_other | 0.028 | 0.018 |
| logcost_trips_19 | 5.7 | 0.018 |
| occ_self_15_production | 0.043 | 0.018 |
| race_self_13_black | 0.078 | 0.018 |
| occ_spouse_17_softscience | 0.012 | 0.018 |
| race_self_15_black | 0.085 | 0.018 |
| logcost_clothing_17 | 6.5 | 0.018 |
| race_self_17_black | 0.099 | 0.017 |
| race_self_11_black | 0.071 | 0.017 |
| occ_spouse_11_janitors | 0.013 | 0.017 |
| empstat_current_self_17_working | 0.8 | 0.017 |
| occ_self_15_legal | 0.01 | 0.017 |
| occ_self_15_compscimath | 0.021 | 0.017 |
| race_spouse_19_black | 0.054 | 0.016 |
| occ_self_11_legal | 0.009 | 0.016 |
| occ_self_17_hardscience | 0.013 | 0.016 |
| state_15_ut | 0.009 | 0.016 |
| race_self_11_other | 0.026 | 0.016 |
| logcost_housing_telecom_15 | 7.6 | 0.016 |
| ind_spouse_19_information | 0.011 | 0.016 |
| ind_spouse_17_arts | 0.01 | 0.016 |
| occ_self_11_production | 0.038 | 0.016 |
| logcost_childcare_13 | 1.1 | 0.016 |
| occ_spouse_13_janitors | 0.012 | 0.016 |
| logincome_wagerate_spouse_15 | 1.8 | 0.016 |
| empstat_current_spouse_11_student | 0.008 | 0.016 |
| religion_spouse_19_other | 0.001 | 0.015 |
| occ_spouse_17_pcareservice | 0.017 | 0.015 |
| logcost_housing_mortgage_15 | 4.8 | 0.015 |
| occ_self_15_janitors | 0.026 | 0.015 |
| logcost_transport_other_11 | 0.257 | 0.015 |
| own_or_rent_11_rent | 0.277 | 0.015 |
| logcost_education_19 | 2.0 | 0.015 |
| region_11_south | 0.307 | 0.015 |
| logcost_housing_tax_19 | 4.9 | 0.015 |
| logcost_housing_telecom_11 | 7.5 | 0.015 |
| occ_spouse_15_compscimath | 0.013 | 0.015 |
| logcost_health_rx_19 | 3.9 | 0.015 |
| occ_spouse_17_healthcareprac | 0.028 | 0.015 |
| occ_spouse_17_hardscience | 0.008 | 0.015 |
| race_self_17_asian | 0.058 | 0.015 |
| logcost_housing_mortgage_11 | 5.1 | 0.015 |
| occ_spouse_17_sales | 0.048 | 0.015 |
| state_17_fl | 0.06 | 0.014 |
| ind_spouse_15_health | 0.067 | 0.014 |
| occ_self_11_protective | 0.016 | 0.014 |
| union_self_15_no | 0.518 | 0.014 |
| state_13_ut | 0.009 | 0.014 |
| logcost_transport_other_17 | 0.297 | 0.014 |
| occ_self_17_softscience | 0.016 | 0.014 |
| logcost_transport_taxi_13 | 0.311 | 0.014 |
| logcost_health_insurance_15 | 5.6 | 0.014 |
| logcost_transport_other_13 | 0.279 | 0.014 |
| occ_spouse_19_hardscience | 0.008 | 0.014 |
| logcost_transport_taxi_11 | 0.261 | 0.014 |
| moved_why_11_closertowork | 0.016 | 0.014 |
| logcost_housing_rent_15 | 3.0 | 0.014 |
| state_19_il | 0.023 | 0.014 |
| race_spouse_13_black | 0.036 | 0.014 |
| moved_why_15_consother | 0.082 | 0.014 |
| moved_why_17_involuntary | 0.04 | 0.014 |
| logcost_housing_repairs_19 | 4.1 | 0.014 |
| logcost_transport_loans_13 | 2.5 | 0.014 |
| occ_spouse_13_arts | 0.012 | 0.014 |
| logcost_transport_loans_17 | 3.0 | 0.013 |
| logcost_computing_17 | 3.9 | 0.013 |
| region_17_south | 0.352 | 0.013 |
| region_13_south | 0.311 | 0.013 |
| state_15_mn | 0.011 | 0.013 |
| occ_self_17_businessfinance | 0.045 | 0.013 |
| occ_self_19_legal | 0.011 | 0.013 |
| occ_self_19_hardscience | 0.014 | 0.013 |
| logcost_health_rx_17 | 3.9 | 0.013 |
| occ_spouse_15_arts | 0.011 | 0.013 |
| occ_spouse_13_compscimath | 0.012 | 0.013 |
| occ_spouse_19_architectengineering | 0.011 | 0.013 |
| religion_spouse_17_orthodox | 0.004 | 0.013 |
| logcost_housing_utility_11 | 7.4 | 0.012 |
| region_19_south | 0.37 | 0.012 |
| moved_why_11_involuntary | 0.044 | 0.012 |
| ind_spouse_19_realestate | 0.011 | 0.012 |
| ind_spouse_19_arts | 0.012 | 0.012 |
| occ_spouse_19_healthcareprac | 0.034 | 0.012 |
| occ_spouse_13_food | 0.011 | 0.012 |
| empstat_current_spouse_19_searching | 0.015 | 0.012 |
| state_15_il | 0.021 | 0.012 |
| logcost_housing_rent_17 | 3.5 | 0.012 |
| occ_self_13_legal | 0.01 | 0.012 |
| race_spouse_15_black | 0.038 | 0.012 |
| ind_spouse_19_adminmilitary | 0.034 | 0.012 |
| religion_self_19_protestant | 0.006 | 0.012 |
| occ_self_15_protective | 0.017 | 0.012 |
| occ_self_11_compscimath | 0.019 | 0.011 |
| state_13_mn | 0.011 | 0.011 |
| race_self_19_asian | 0.067 | 0.011 |
| religion_spouse_15_orthodox | 0.002 | 0.011 |
| union_spouse_19_no | 0.403 | 0.011 |
| race_self_11_asian | 0.025 | 0.011 |
| moved_why_17_homeless | 0.003 | 0.011 |
| logcost_transport_insurance_19 | 7.0 | 0.011 |
| occ_self_19_softscience | 0.02 | 0.011 |
| state_15_ms | 0.011 | 0.011 |
| moved_why_15_productive | 0.023 | 0.011 |
| occ_spouse_15_healthcaresupport | 0.011 | 0.011 |
| logcost_housing_insurance_19 | 4.2 | 0.011 |
| race_spouse_17_asian | 0.046 | 0.011 |
| state_19_fl | 0.065 | 0.011 |
| empstat_current_spouse_13_housespouse | 0.063 | 0.01 |
| occ_self_19_healthcareprac | 0.053 | 0.01 |
| logcost_trips_17 | 5.6 | 0.01 |
| empstat_current_spouse_17_laid off | 0.002 | 0.01 |
| union_self_11_no | 0.43 | 0.01 |
| ind_spouse_15_realestate | 0.007 | 0.01 |
| occ_spouse_17_architectengineering | 0.01 | 0.01 |
| mightmove_15_yes | 0.296 | 0.01 |
| state_13_il | 0.023 | 0.01 |
| logcost_transport_gas_13 | 7.3 | 0.01 |
| empstat_current_spouse_15_laid off | 0.001 | 0.01 |
| logcost_food_deliver_11 | 0.747 | 0.01 |
| region_15_south | 0.315 | 0.01 |
| occ_self_13_janitors | 0.022 | 0.01 |
| occ_spouse_19_compscimath | 0.018 | 0.01 |
| moved_why_19_consmore | 0.046 | 0.01 |
| logincome_wagerate_spouse_17 | 1.8 | 0.01 |
| state_19_ut | 0.01 | 0.009 |
| logcost_transport_repair_11 | 3.6 | 0.009 |
| occ_self_13_hardscience | 0.01 | 0.009 |
| moved_why_13_closertowork | 0.015 | 0.009 |
| race_self_19_amind | 0.005 | 0.009 |
| state_13_tn | 0.02 | 0.009 |
| logcost_transport_repair_17 | 5.4 | 0.009 |
| state_19_mn | 0.014 | 0.009 |
| occ_self_11_hardscience | 0.009 | 0.009 |
| logincome_labor_spouse_17 | 5.9 | 0.009 |
| logcost_housing_utility_15 | 7.5 | 0.009 |
| state_13_ms | 0.011 | 0.009 |
| state_11_ms | 0.011 | 0.009 |
| occ_spouse_13_healthcaresupport | 0.01 | 0.009 |
| race_spouse_11_asian | 0.02 | 0.009 |
| logcost_transport_gas_15 | 7.0 | 0.009 |
| ind_spouse_15_arts | 0.008 | 0.009 |
| logincome_familytotal_11 | 11.0 | 0.009 |
| occ_self_11_healthcareprac | 0.033 | 0.009 |
| state_17_mn | 0.013 | 0.009 |
| logincome_labor_spouse_13 | 6.1 | 0.009 |
| occ_self_15_hardscience | 0.013 | 0.009 |
| occ_self_17_compscimath | 0.028 | 0.008 |
| race_spouse_17_black | 0.047 | 0.008 |
| occ_self_13_protective | 0.017 | 0.008 |
| occ_self_15_repair | 0.028 | 0.008 |
| state_15_tn | 0.022 | 0.008 |
| race_spouse_11_black | 0.033 | 0.008 |
| race_spouse_15_pacis | 0.001 | 0.008 |
| religion_self_15_orthodox | 0.002 | 0.008 |
| occ_self_17_janitors | 0.034 | 0.008 |
| state_15_vt | 0.001 | 0.008 |
| race_self_13_asian | 0.027 | 0.008 |
| ind_spouse_17_information | 0.01 | 0.008 |
| state_19_al | 0.009 | 0.008 |
| race_self_13_amind | 0.004 | 0.008 |
| occ_spouse_15_officeadmin | 0.067 | 0.008 |
| occ_self_13_healthcareprac | 0.033 | 0.008 |
| logcost_transport_downpayment_11 | 1.7 | 0.008 |
| mightmove_17_yes | 0.312 | 0.008 |
| occ_self_11_repair | 0.027 | 0.008 |
| moved_why_17_productive | 0.029 | 0.008 |
| logcost_housing_mortgage_13 | 4.9 | 0.008 |
| occ_spouse_19_officeadmin | 0.077 | 0.008 |
| state_19_tn | 0.023 | 0.007 |
| logcost_food_away_19 | 7.4 | 0.007 |
| logcost_transport_downpayment_17 | 1.8 | 0.007 |
| logcost_health_17 | 7.1 | 0.007 |
| logcost_transport_leases_11 | 0.348 | 0.007 |
| occ_self_15_healthcareprac | 0.037 | 0.007 |
| logcost_trips_13 | 5.3 | 0.007 |
| logcost_transport_leases_19 | 0.73 | 0.007 |
| occ_spouse_11_sales | 0.055 | 0.007 |
| logcost_health_insurance_13 | 5.2 | 0.007 |
| moved_why_19_closertowork | 0.023 | 0.007 |
| occ_spouse_13_sales | 0.056 | 0.007 |
| empstat_current_self_17_student | 0.01 | 0.007 |
| occ_self_19_healthcaresupport | 0.027 | 0.007 |
| occ_spouse_11_healthcareprac | 0.024 | 0.007 |
| state_17_tn | 0.021 | 0.007 |
| race_self_15_asian | 0.033 | 0.007 |
| state_17_ut | 0.009 | 0.007 |
| logcost_housing_repairs_13 | 4.1 | 0.007 |
| occ_self_15_businessfinance | 0.037 | 0.007 |
| state_11_il | 0.024 | 0.007 |
| occ_spouse_17_janitors | 0.02 | 0.007 |
| state_11_de | 0.001 | 0.007 |
| logcost_transport_other_15 | 0.373 | 0.006 |
| own_or_rent_19_own | 0.629 | 0.006 |
| logcost_health_doctor_11 | 4.6 | 0.006 |
| ind_spouse_19_mining | 0.002 | 0.006 |
| logcost_transport_downpayment_19 | 1.8 | 0.006 |
| logcost_computing_19 | 3.7 | 0.006 |
| state_15_wv | 0.002 | 0.006 |
| state_15_wy | 0.002 | 0.006 |
| union_self_13_no | 0.478 | 0.006 |
| occ_self_17_production | 0.051 | 0.006 |
| logcost_transport_additionalvehicle_13 | 2.0 | 0.006 |
| logcost_health_rx_11 | 4.2 | 0.006 |
| state_13_ok | 0.009 | 0.006 |
| occ_self_17_legal | 0.011 | 0.006 |
| state_13_de | 0.001 | 0.006 |
| state_15_de | 0.001 | 0.006 |
| state_17_de | 0.001 | 0.006 |
| religion_spouse_13_orthodox | 0.001 | 0.006 |
| moved_why_11_consneighbor | 0.021 | 0.006 |
| logcost_housing_tax_17 | 4.8 | 0.006 |
| state_11_vt | 0.001 | 0.006 |
| state_13_vt | 0.001 | 0.006 |
| moved_why_15_consmore | 0.04 | 0.006 |
| state_11_ok | 0.009 | 0.006 |
| logincome_wagerate_spouse_13 | 1.8 | 0.006 |
| state_19_de | 0.001 | 0.006 |
| occ_spouse_11_businessfinance | 0.022 | 0.006 |
| race_self_17_amind | 0.004 | 0.006 |
| race_self_11_amind | 0.004 | 0.006 |
| state_17_vt | 0.001 | 0.006 |
| moved_why_13_consneighbor | 0.024 | 0.006 |
| occ_self_17_healthcareprac | 0.044 | 0.006 |
| state_19_ok | 0.01 | 0.006 |
| religion_spouse_19_catholic | 0.11 | 0.005 |
| race_spouse_15_asian | 0.026 | 0.005 |
| ind_spouse_19_transportwarehouse | 0.023 | 0.005 |
| moved_why_17_mixed | 0.018 | 0.005 |
| state_11_mn | 0.011 | 0.005 |
| state_17_al | 0.008 | 0.005 |
| occ_spouse_11_education | 0.033 | 0.005 |
| state_17_wv | 0.001 | 0.005 |
| state_11_tn | 0.02 | 0.005 |
| religion_self_17_none | 0.152 | 0.005 |
| logwealth_homeequity_19 | 7.2 | 0.005 |
| state_19_wv | 0.001 | 0.005 |
| occ_self_17_repair | 0.034 | 0.005 |
| logcost_housing_furnishing_15 | 4.6 | 0.005 |
| own_or_rent_19_rent | 0.341 | 0.005 |
| occ_spouse_15_janitors | 0.016 | 0.005 |
| state_17_la | 0.007 | 0.005 |
| logcost_transport_insurance_15 | 6.8 | 0.004 |
| logcost_health_bills_19 | 0.628 | 0.004 |
| occ_self_11_management | 0.062 | 0.004 |
| occ_spouse_11_arts | 0.011 | 0.004 |
| state_17_dc | 0.002 | 0.004 |
| state_19_nh | 0.003 | 0.004 |
| empstat_current_spouse_19_student | 0.007 | 0.004 |
| state_17_ok | 0.009 | 0.004 |
| empstat_current_spouse_17_working | 0.467 | 0.004 |
| religion_spouse_19_orthodox | 0.016 | 0.004 |
| occ_spouse_15_sales | 0.057 | 0.004 |
| ind_spouse_15_information | 0.01 | 0.004 |
| logcost_health_bills_15 | 0.763 | 0.004 |
| moved_15_yes | 0.274 | 0.004 |
| occ_spouse_17_officeadmin | 0.073 | 0.004 |
| ind_spouse_17_transportwarehouse | 0.019 | 0.003 |
| state_19_ms | 0.01 | 0.003 |
| state_17_wy | 0.002 | 0.003 |
| union_spouse_17_no | 0.36 | 0.003 |
| logcost_food_away_17 | 7.2 | 0.003 |
| state_11_tx | 0.059 | 0.003 |
| state_17_ms | 0.01 | 0.003 |
| region_19_west | 0.229 | 0.003 |
| state_19_tx | 0.069 | 0.003 |
| logcost_health_15 | 7.1 | 0.003 |
| occ_spouse_15_healthcareprac | 0.026 | 0.003 |
| state_15_ct | 0.004 | 0.003 |
| region_17_west | 0.217 | 0.003 |
| occ_self_15_softscience | 0.014 | 0.003 |
| occ_spouse_15_architectengineering | 0.009 | 0.003 |
| state_17_nh | 0.004 | 0.002 |
| occ_self_11_transport | 0.039 | 0.002 |
| empstat_current_self_17_searching | 0.028 | 0.002 |
| occ_self_19_officeadmin | 0.128 | 0.002 |
| occ_self_13_military | 0.007 | 0.002 |
| moved_why_19_consother | 0.089 | 0.002 |
| state_13_nm | 0.002 | 0.002 |
| occ_spouse_11_food | 0.013 | 0.002 |
| state_13_wv | 0.002 | 0.002 |
| state_19_dc | 0.003 | 0.002 |
| state_19_ct | 0.008 | 0.002 |
| moved_why_13_consother | 0.075 | 0.002 |
| state_15_me | 0.003 | 0.002 |
| race_self_19_pacis | 0.001 | 0.002 |
| religion_self_13_orthodox | 0.001 | 0.002 |
| logcost_health_doctor_17 | 4.4 | 0.002 |
| moved_19_yes | 0.289 | 0.001 |
| state_17_nc | 0.035 | 0.001 |
| empstat_current_spouse_17_searching | 0.016 | 0.001 |
| logcost_health_11 | 6.7 | 0.001 |
| race_spouse_17_pacis | 0.0 | 0.001 |
| region_19_foreign | 0.007 | 0.001 |
| state_11_wy | 0.001 | 0.001 |
| logcost_health_doctor_13 | 4.7 | 0.001 |
| occ_self_13_softscience | 0.013 | 0.001 |
| own_or_rent_15_rent | 0.295 | 0.001 |
| race_spouse_19_pacis | 0.001 | 0.001 |
| ind_spouse_19_otherservices | 0.03 | 0.0 |
| state_17_me | 0.003 | 0.0 |
| logcost_housing_utility_13 | 7.4 | 0.0 |
| occ_self_13_healthcaresupport | 0.016 | 0.0 |
| moved_why_15_involuntary | 0.036 | 0.0 |
| ind_spouse_15_adminmilitary | 0.03 | 0.0 |
| occ_spouse_11_officeadmin | 0.062 | 0.0 |
| occ_self_19_compscimath | 0.033 | 0.0 |
| logcost_transport_insurance_11 | 6.7 | 0.0 |
| state_13_dc | 0.002 | 0.0 |
| state_15_dc | 0.002 | 0.0 |
| moved_why_13_mixed | 0.02 | 0.0 |
| occ_spouse_13_healthcareprac | 0.025 | 0.0 |
| state_15_hi | 0.0 | -0.0 |
| state_11_hi | 0.0 | -0.0 |
| state_19_vt | 0.001 | -0.0 |
| moved_why_11_mixed | 0.028 | -0.0 |
| logcost_transport_leases_13 | 0.445 | -0.0 |
| moved_why_17_consless | 0.019 | -0.0 |
| religion_self_19_orthodox | 0.023 | -0.0 |
| logcost_housing_furnishing_19 | 4.5 | -0.0 |
| empstat_current_spouse_11_laid off | 0.002 | -0.0 |
| state_13_tx | 0.058 | -0.0 |
| state_19_va | 0.034 | -0.0 |
| ind_spouse_15_management | 0.015 | -0.0 |
| ind_spouse_15_mining | 0.002 | -0.0 |
| logcost_housing_tax_11 | 5.0 | -0.0 |
| empstat_current_spouse_15_student | 0.007 | -0.0 |
| occ_self_15_transport | 0.045 | -0.0 |
| empstat_current_spouse_17_student | 0.007 | -0.0 |
| race_spouse_13_asian | 0.023 | -0.0 |
| occ_spouse_19_legal | 0.007 | -0.001 |
| state_19_la | 0.006 | -0.001 |
| state_17_ct | 0.006 | -0.001 |
| logcost_housing_insurance_17 | 4.2 | -0.001 |
| occ_self_13_transport | 0.04 | -0.001 |
| ind_spouse_15_utilities | 0.005 | -0.001 |
| state_17_tx | 0.065 | -0.001 |
| logcost_housing_rent_19 | 3.4 | -0.001 |
| empstat_current_spouse_15_searching | 0.013 | -0.001 |
| logcost_food_athome_11 | 8.3 | -0.001 |
| state_13_wy | 0.002 | -0.001 |
| religion_self_17_orthodox | 0.004 | -0.001 |
| moved_19_no | 0.711 | -0.001 |
| race_self_17_pacis | 0.001 | -0.001 |
| occ_spouse_11_softscience | 0.009 | -0.001 |
| state_13_al | 0.007 | -0.002 |
| logcost_food_athome_15 | 8.5 | -0.002 |
| religion_spouse_19_protestant | 0.004 | -0.002 |
| moved_why_15_closertowork | 0.017 | -0.002 |
| logcost_health_hospital_19 | 1.7 | -0.002 |
| moved_why_19_homeless | 0.001 | -0.002 |
| logcost_housing_tax_15 | 4.8 | -0.002 |
| state_19_me | 0.003 | -0.002 |
| religion_self_11_orthodox | 0.001 | -0.002 |
| ind_spouse_17_DKNARefused | 0.002 | -0.002 |
| logcost_recreation_19 | 5.3 | -0.002 |
| ind_spouse_19_profsciencetech | 0.043 | -0.002 |
| occ_spouse_15_protective | 0.011 | -0.002 |
| state_15_tx | 0.061 | -0.002 |
| state_15_ky | 0.013 | -0.002 |
| logwealth_homeequity_15 | 7.0 | -0.002 |
| logcost_transport_insurance_17 | 6.9 | -0.002 |
| ind_spouse_17_mining | 0.002 | -0.002 |
| ind_spouse_15_DKNARefused | 0.002 | -0.003 |
| grewup_region_self_akhi | 0.002 | -0.003 |
| state_11_wv | 0.001 | -0.003 |
| ind_spouse_19_construction | 0.037 | -0.003 |
| occ_spouse_19_businessfinance | 0.032 | -0.003 |
| occ_spouse_13_DKNARefused | 0.002 | -0.003 |
| moved_why_13_consless | 0.021 | -0.003 |
| moved_why_13_homeless | 0.001 | -0.003 |
| ind_spouse_19_DKNARefused | 0.002 | -0.003 |
| state_13_ky | 0.013 | -0.003 |
| occ_spouse_13_architectengineering | 0.008 | -0.003 |
| state_15_nm | 0.002 | -0.003 |
| state_15_ok | 0.009 | -0.003 |
| ind_spouse_17_adminmilitary | 0.031 | -0.003 |
| religion_self_19_jewish | 0.024 | -0.003 |
| religion_self_15_none | 0.123 | -0.003 |
| logcost_food_13 | 8.8 | -0.003 |
| ind_spouse_17_retail | 0.043 | -0.003 |
| state_19_wy | 0.001 | -0.004 |
| region_11_akhi | 0.002 | -0.004 |
| state_11_nc | 0.031 | -0.004 |
| ind_spouse_17_otherservices | 0.026 | -0.004 |
| region_15_foreign | 0.005 | -0.004 |
| state_11_ak | 0.001 | -0.004 |
| state_13_nc | 0.031 | -0.004 |
| state_19_nc | 0.036 | -0.004 |
| logcost_health_doctor_19 | 4.5 | -0.004 |
| occ_self_17_officeadmin | 0.112 | -0.004 |
| logcost_transport_insurance_13 | 6.7 | -0.004 |
| logcost_transport_gas_11 | 7.3 | -0.004 |
| occ_self_11_softscience | 0.011 | -0.004 |
| logcost_health_insurance_11 | 5.0 | -0.004 |
| occ_spouse_15_hardscience | 0.008 | -0.004 |
| state_15_wi | 0.014 | -0.004 |
| occ_self_15_farmfishforest | 0.008 | -0.004 |
| occ_self_11_military | 0.007 | -0.004 |
| moved_why_19_consneighbor | 0.028 | -0.004 |
| occ_spouse_17_production | 0.028 | -0.004 |
| logcost_food_deliver_13 | 0.718 | -0.005 |
| empstat_current_spouse_13_laid off | 0.001 | -0.005 |
| occ_self_13_businessfinance | 0.034 | -0.005 |
| occ_self_15_military | 0.007 | -0.005 |
| state_15_al | 0.007 | -0.005 |
| state_15_la | 0.004 | -0.005 |
| state_13_hi | 0.0 | -0.005 |
| religion_self_11_none | 0.094 | -0.005 |
| occ_spouse_15_legal | 0.006 | -0.005 |
| logcost_housing_utility_17 | 7.4 | -0.005 |
| moved_why_13_involuntary | 0.04 | -0.005 |
| occ_self_13_farmfishforest | 0.008 | -0.005 |
| logcost_transport_loans_11 | 2.3 | -0.005 |
| logcost_food_athome_13 | 8.4 | -0.005 |
| state_15_nc | 0.031 | -0.005 |
| ind_spouse_17_utilities | 0.005 | -0.005 |
| empstat_current_spouse_11_other | 0.001 | -0.005 |
| state_17_ak | 0.002 | -0.005 |
| empstat_current_spouse_19_laid off | 0.002 | -0.005 |
| ind_spouse_19_retail | 0.043 | -0.005 |
| occ_spouse_11_architectengineering | 0.007 | -0.005 |
| moved_why_11_homeless | 0.002 | -0.005 |
| occ_self_19_production | 0.059 | -0.005 |
| state_11_la | 0.005 | -0.005 |
| religion_self_13_none | 0.106 | -0.005 |
| logcost_food_15 | 8.9 | -0.005 |
| state_11_ct | 0.004 | -0.005 |
| logcost_health_bills_17 | 0.715 | -0.005 |
| state_11_dc | 0.002 | -0.005 |
| moved_why_15_consless | 0.02 | -0.005 |
| logcost_food_away_15 | 7.2 | -0.005 |
| state_13_ct | 0.004 | -0.005 |
| ind_spouse_17_management | 0.018 | -0.005 |
| occ_spouse_19_food | 0.022 | -0.005 |
| occ_spouse_11_protective | 0.01 | -0.006 |
| occ_spouse_15_food | 0.013 | -0.006 |
| state_11_az | 0.012 | -0.006 |
| occ_spouse_11_healthcaresupport | 0.007 | -0.006 |
| ind_spouse_17_wholesale | 0.018 | -0.006 |
| occ_self_19_DKNARefused | 0.002 | -0.006 |
| region_13_foreign | 0.004 | -0.006 |
| occ_spouse_11_farmfishforest | 0.004 | -0.006 |
| occ_spouse_13_officeadmin | 0.063 | -0.006 |
| occ_spouse_13_protective | 0.011 | -0.006 |
| occ_self_17_transport | 0.053 | -0.006 |
| race_self_15_amind | 0.004 | -0.006 |
| occ_spouse_15_softscience | 0.01 | -0.006 |
| occ_spouse_13_softscience | 0.009 | -0.006 |
| race_spouse_19_white | 0.546 | -0.006 |
| moved_11_no | 0.607 | -0.006 |
| moved_why_11_productive | 0.017 | -0.006 |
| logwealth_homeequity_17 | 7.0 | -0.007 |
| religion_self_15_nonchristian | 0.015 | -0.007 |
| grewup_region_self_west | 0.164 | -0.007 |
| state_11_ky | 0.014 | -0.007 |
| occ_self_17_farmfishforest | 0.009 | -0.007 |
| state_13_me | 0.003 | -0.007 |
| religion_self_17_other | 0.004 | -0.007 |
| religion_self_15_other | 0.004 | -0.007 |
| occ_self_17_healthcaresupport | 0.025 | -0.007 |
| race_self_15_pacis | 0.001 | -0.007 |
| ind_spouse_19_wholesale | 0.019 | -0.007 |
| logcost_housing_utility_19 | 7.5 | -0.007 |
| state_13_nv | 0.009 | -0.007 |
| grewup_region_spouse_13_akhi | 0.002 | -0.007 |
| mightmove_13_yes | 0.274 | -0.007 |
| grewup_region_spouse_15_akhi | 0.002 | -0.007 |
| region_13_west | 0.194 | -0.007 |
| region_15_akhi | 0.002 | -0.007 |
| state_13_ak | 0.002 | -0.007 |
| state_15_ak | 0.002 | -0.007 |
| mightmove_11_yes | 0.287 | -0.007 |
| state_11_al | 0.007 | -0.007 |
| ind_spouse_15_transportwarehouse | 0.018 | -0.008 |
| occ_self_13_repair | 0.027 | -0.008 |
| moved_why_19_consless | 0.015 | -0.008 |
| occ_self_13_food | 0.025 | -0.008 |
| logcost_housing_furnishing_11 | 4.6 | -0.008 |
| religion_spouse_11_orthodox | 0.001 | -0.008 |
| logcost_health_13 | 7.0 | -0.008 |
| occ_self_19_military | 0.007 | -0.008 |
| occ_self_17_food | 0.034 | -0.008 |
| occ_self_15_healthcaresupport | 0.019 | -0.008 |
| occ_self_11_janitors | 0.022 | -0.008 |
| state_11_me | 0.003 | -0.008 |
| occ_spouse_11_military | 0.004 | -0.008 |
| moved_why_19_mixed | 0.026 | -0.008 |
| region_13_akhi | 0.002 | -0.008 |
| occ_self_11_healthcaresupport | 0.015 | -0.008 |
| moved_why_11_consother | 0.068 | -0.008 |
| logcost_housing_insurance_15 | 4.2 | -0.008 |
| occ_spouse_17_compscimath | 0.016 | -0.008 |
| occ_spouse_15_military | 0.004 | -0.008 |
| own_or_rent_17_own | 0.598 | -0.008 |
| state_15_va | 0.032 | -0.009 |
| logcost_health_doctor_15 | 4.5 | -0.009 |
| occ_self_13_management | 0.071 | -0.009 |
| religion_spouse_19_nonchristian | 0.023 | -0.009 |
| region_17_akhi | 0.002 | -0.009 |
| occ_spouse_17_protective | 0.01 | -0.009 |
| empstat_current_self_19_housespouse | 0.007 | -0.009 |
| logincome_wagerate_spouse_11 | 1.8 | -0.009 |
| occ_spouse_17_food | 0.017 | -0.009 |
| occ_self_17_military | 0.006 | -0.009 |
| occ_self_15_management | 0.074 | -0.009 |
| occ_self_17_DKNARefused | 0.002 | -0.009 |
| occ_spouse_11_hardscience | 0.005 | -0.009 |
| religion_self_11_nonchristian | 0.014 | -0.009 |
| state_13_nh | 0.002 | -0.009 |
| state_17_ky | 0.017 | -0.009 |
| occ_spouse_11_legal | 0.005 | -0.009 |
| moved_why_13_productive | 0.022 | -0.009 |
| occ_spouse_15_DKNARefused | 0.002 | -0.01 |
| logwealth_15 | 11.1 | -0.01 |
| occ_spouse_13_constructionextraction | 0.02 | -0.01 |
| empstat_current_spouse_17_disabled | 0.015 | -0.01 |
| ind_spouse_15_retail | 0.038 | -0.01 |
| grewup_region_spouse_11_akhi | 0.002 | -0.01 |
| state_17_nv | 0.01 | -0.01 |
| occ_spouse_13_production | 0.023 | -0.01 |
| region_11_west | 0.197 | -0.01 |
| occ_spouse_17_transport | 0.024 | -0.01 |
| logcost_health_hospital_15 | 1.5 | -0.01 |
| state_17_hi | 0.0 | -0.01 |
| occ_spouse_13_hardscience | 0.007 | -0.01 |
| moved_why_15_homeless | 0.002 | -0.01 |
| state_11_wa | 0.022 | -0.01 |
| moved_why_15_consneighbor | 0.025 | -0.01 |
| state_17_va | 0.033 | -0.01 |
| ind_spouse_19_accomodationsfood | 0.028 | -0.01 |
| occ_spouse_19_DKNARefused | 0.001 | -0.01 |
| state_17_wa | 0.024 | -0.01 |
| ind_spouse_17_farmfishforest | 0.011 | -0.01 |
| ind_spouse_19_utilities | 0.007 | -0.01 |
| logincome_labor_spouse_11 | 6.2 | -0.011 |
| moved_why_17_closertowork | 0.016 | -0.011 |
| region_15_west | 0.2 | -0.011 |
| logcost_trips_15 | 5.5 | -0.011 |
| occ_self_13_DKNARefused | 0.002 | -0.011 |
| logcost_transport_repair_15 | 6.6 | -0.011 |
| occ_self_19_transport | 0.067 | -0.011 |
| occ_spouse_13_businessfinance | 0.021 | -0.011 |
| logcost_health_rx_15 | 4.1 | -0.011 |
| state_19_nm | 0.002 | -0.011 |
| region_11_foreign | 0.006 | -0.011 |
| religion_spouse_19_jewish | 0.014 | -0.011 |
| state_19_nv | 0.01 | -0.011 |
| moved_13_yes | 0.27 | -0.011 |
| occ_self_15_DKNARefused | 0.002 | -0.012 |
| occ_self_11_DKNARefused | 0.001 | -0.012 |
| occ_spouse_19_protective | 0.011 | -0.012 |
| region_17_foreign | 0.006 | -0.012 |
| occ_spouse_13_military | 0.004 | -0.012 |
| occ_self_11_farmfishforest | 0.007 | -0.012 |
| occ_spouse_11_production | 0.024 | -0.012 |
| moved_why_17_consneighbor | 0.024 | -0.012 |
| occ_spouse_19_constructionextraction | 0.029 | -0.012 |
| state_13_va | 0.032 | -0.012 |
| occ_spouse_17_legal | 0.007 | -0.012 |
| state_11_nm | 0.002 | -0.012 |
| occ_spouse_19_transport | 0.028 | -0.012 |
| state_11_nv | 0.009 | -0.012 |
| state_11_nh | 0.003 | -0.012 |
| empstat_current_spouse_11_searching | 0.022 | -0.012 |
| logcost_housing_insurance_11 | 4.3 | -0.013 |
| moved_why_15_mixed | 0.018 | -0.013 |
| occ_self_19_farmfishforest | 0.01 | -0.013 |
| occ_spouse_15_businessfinance | 0.023 | -0.013 |
| state_19_ky | 0.017 | -0.013 |
| logwealth_other_11 | 10.2 | -0.013 |
| religion_spouse_15_nonchristian | 0.011 | -0.013 |
| state_19_wa | 0.025 | -0.013 |
| state_13_sc | 0.017 | -0.013 |
| occ_spouse_13_farmfishforest | 0.004 | -0.013 |
| occ_spouse_17_constructionextraction | 0.026 | -0.014 |
| state_15_sd | 0.003 | -0.014 |
| grewup_region_spouse_11_south | 0.12 | -0.014 |
| ind_spouse_15_construction | 0.027 | -0.014 |
| occ_spouse_11_compscimath | 0.011 | -0.014 |
| state_11_sc | 0.018 | -0.014 |
| logcost_transport_downpayment_13 | 1.6 | -0.014 |
| moved_why_19_involuntary | 0.033 | -0.014 |
| occ_spouse_15_constructionextraction | 0.023 | -0.014 |
| occ_self_17_pcareservice | 0.028 | -0.014 |
| state_17_mt | 0.001 | -0.014 |
| occ_spouse_19_farmfishforest | 0.005 | -0.014 |
| state_13_sd | 0.003 | -0.014 |
| logcost_housing_repairs_15 | 4.2 | -0.014 |
| state_15_nv | 0.009 | -0.014 |
| religion_self_13_nonchristian | 0.013 | -0.014 |
| state_13_la | 0.005 | -0.014 |
| occ_self_11_food | 0.025 | -0.014 |
| ind_spouse_17_accomodationsfood | 0.023 | -0.014 |
| empstat_current_self_11_disabled | 0.004 | -0.014 |
| empstat_current_spouse_15_disabled | 0.011 | -0.014 |
| state_19_sc | 0.02 | -0.014 |
| grewup_region_spouse_13_south | 0.127 | -0.014 |
| state_19_ri | 0.001 | -0.014 |
| logcost_housing_furnishing_13 | 4.5 | -0.015 |
| logcost_housing_tax_13 | 4.8 | -0.015 |
| empstat_19_searching | 0.005 | -0.015 |
| religion_spouse_11_nonchristian | 0.011 | -0.015 |
| state_13_wi | 0.014 | -0.015 |
| state_17_or | 0.02 | -0.015 |
| state_17_ri | 0.001 | -0.015 |
| logcost_recreation_17 | 5.4 | -0.015 |
| logcost_housing_repairs_17 | 4.1 | -0.015 |
| state_19_mt | 0.001 | -0.015 |
| empstat_current_self_19_searching | 0.005 | -0.015 |
| ind_spouse_15_accomodationsfood | 0.018 | -0.015 |
| state_11_va | 0.031 | -0.015 |
| ind_spouse_17_construction | 0.033 | -0.015 |
| state_17_wi | 0.014 | -0.015 |
| state_11_wi | 0.014 | -0.015 |
| religion_self_19_other | 0.002 | -0.015 |
| religion_spouse_17_nonchristian | 0.025 | -0.015 |
| empstat_current_self_17_disabled | 0.005 | -0.015 |
| occ_spouse_17_military | 0.002 | -0.015 |
| occ_self_15_arts | 0.017 | -0.016 |
| race_spouse_15_amind | 0.003 | -0.016 |
| logcost_recreation_11 | 5.4 | -0.016 |
| own_or_rent_15_neither | 0.029 | -0.016 |
| occ_spouse_15_repair | 0.015 | -0.016 |
| logcost_health_rx_13 | 4.3 | -0.016 |
| state_19_ak | 0.002 | -0.016 |
| occ_spouse_15_production | 0.023 | -0.016 |
| state_13_mt | 0.001 | -0.016 |
| union_spouse_13_no | 0.294 | -0.016 |
| religion_spouse_15_other | 0.003 | -0.016 |
| logcost_recreation_15 | 5.5 | -0.016 |
| empstat_current_spouse_11_disabled | 0.01 | -0.016 |
| state_13_or | 0.019 | -0.016 |
| logcost_food_away_13 | 7.0 | -0.016 |
| religion_spouse_13_nonchristian | 0.01 | -0.016 |
| state_15_or | 0.02 | -0.016 |
| state_17_az | 0.017 | -0.016 |
| state_19_co | 0.025 | -0.016 |
| state_17_nm | 0.001 | -0.016 |
| state_19_id | 0.001 | -0.016 |
| moved_why_13_consmore | 0.04 | -0.016 |
| logcost_housing_furnishing_17 | 4.5 | -0.016 |
| occ_spouse_17_businessfinance | 0.026 | -0.017 |
| state_13_id | 0.002 | -0.017 |
| state_15_id | 0.002 | -0.017 |
| state_17_id | 0.002 | -0.017 |
| empstat_current_spouse_13_searching | 0.016 | -0.017 |
| occ_spouse_17_DKNARefused | 0.002 | -0.017 |
| mightmove_17_no | 0.622 | -0.017 |
| state_17_sd | 0.003 | -0.017 |
| state_19_sd | 0.003 | -0.017 |
| moved_13_no | 0.61 | -0.017 |
| moved_11_yes | 0.278 | -0.017 |
| state_17_sc | 0.019 | -0.017 |
| state_13_ri | 0.001 | -0.017 |
| state_15_ri | 0.001 | -0.017 |
| occ_spouse_17_repair | 0.019 | -0.017 |
| state_13_wa | 0.023 | -0.017 |
| grewup_region_self_south | 0.246 | -0.018 |
| religion_self_11_other | 0.009 | -0.018 |
| state_19_wi | 0.015 | -0.018 |
| mightmove_11_no | 0.581 | -0.018 |
| state_11_pa | 0.045 | -0.018 |
| occ_spouse_13_legal | 0.006 | -0.018 |
| race_spouse_17_white | 0.489 | -0.018 |
| state_15_az | 0.013 | -0.018 |
| race_spouse_13_amind | 0.003 | -0.018 |
| race_spouse_19_amind | 0.004 | -0.018 |
| race_spouse_17_amind | 0.004 | -0.018 |
| occ_spouse_15_farmfishforest | 0.005 | -0.019 |
| state_13_mo | 0.024 | -0.019 |
| state_15_mt | 0.001 | -0.019 |
| religion_spouse_17_other | 0.003 | -0.019 |
| state_15_mi | 0.032 | -0.019 |
| occ_spouse_19_production | 0.032 | -0.019 |
| occ_self_19_management | 0.101 | -0.019 |
| ind_spouse_17_profsciencetech | 0.038 | -0.019 |
| state_15_sc | 0.017 | -0.019 |
| state_19_or | 0.021 | -0.019 |
| logcost_trips_11 | 5.3 | -0.019 |
| empstat_current_spouse_15_working | 0.41 | -0.019 |
| state_11_ri | 0.001 | -0.019 |
| state_19_az | 0.017 | -0.019 |
| state_15_wa | 0.023 | -0.02 |
| occ_spouse_19_military | 0.003 | -0.02 |
| religion_self_13_other | 0.009 | -0.02 |
| state_11_id | 0.002 | -0.02 |
| logcost_food_11 | 8.8 | -0.02 |
| state_15_mo | 0.022 | -0.02 |
| state_13_az | 0.013 | -0.02 |
| state_11_mt | 0.002 | -0.02 |
| own_or_rent_15_own | 0.561 | -0.02 |
| state_17_nd | 0.002 | -0.02 |
| state_19_nd | 0.002 | -0.02 |
| state_17_mo | 0.023 | -0.02 |
| logcost_health_hospital_13 | 1.6 | -0.02 |
| occ_spouse_13_repair | 0.015 | -0.02 |
| logwealth_11 | 10.9 | -0.021 |
| moved_why_11_consmore | 0.048 | -0.021 |
| occ_spouse_15_transport | 0.023 | -0.021 |
| state_11_nd | 0.002 | -0.021 |
| state_13_nd | 0.002 | -0.021 |
| logwealth_other_15 | 10.3 | -0.021 |
| ind_spouse_15_profsciencetech | 0.033 | -0.021 |
| empstat_19_student | 0.001 | -0.021 |
| state_13_pa | 0.044 | -0.021 |
| empstat_current_self_13_disabled | 0.004 | -0.021 |
| own_or_rent_11_neither | 0.027 | -0.021 |
| own_or_rent_13_neither | 0.032 | -0.021 |
| logwealth_17 | 11.1 | -0.021 |
| state_19_mo | 0.025 | -0.021 |
| state_11_ks | 0.006 | -0.021 |
| state_19_hi | 0.001 | -0.021 |
| occ_spouse_11_transport | 0.023 | -0.021 |
| occ_spouse_17_management | 0.056 | -0.021 |
| race_spouse_11_amind | 0.003 | -0.021 |
| state_17_co | 0.022 | -0.022 |
| occ_self_17_management | 0.088 | -0.022 |
| occ_self_13_arts | 0.015 | -0.022 |
| ind_spouse_15_wholesale | 0.014 | -0.022 |
| occ_self_15_food | 0.029 | -0.022 |
| occ_spouse_17_farmfishforest | 0.005 | -0.022 |
| logwealth_19 | 11.2 | -0.022 |
| logcost_clothing_11 | 6.6 | -0.022 |
| logcost_clothing_15 | 6.6 | -0.022 |
| state_15_pa | 0.044 | -0.022 |
| state_15_nh | 0.002 | -0.022 |
| empstat_current_spouse_13_working | 0.389 | -0.022 |
| ind_spouse_13_wholesale | 0.013 | -0.022 |
| occ_spouse_11_constructionextraction | 0.019 | -0.023 |
| empstat_current_spouse_19_disabled | 0.01 | -0.023 |
| occ_self_11_officeadmin | 0.093 | -0.023 |
| religion_spouse_11_none | 0.235 | -0.023 |
| mightmove_19_no | 0.653 | -0.023 |
| occ_spouse_19_repair | 0.017 | -0.023 |
| state_11_mi | 0.033 | -0.023 |
| union_spouse_15_no | 0.316 | -0.023 |
| empstat_current_self_19_disabled | 0.003 | -0.023 |
| state_11_co | 0.022 | -0.023 |
| state_11_mo | 0.024 | -0.023 |
| state_13_co | 0.022 | -0.024 |
| logcost_clothing_13 | 6.5 | -0.024 |
| state_17_pa | 0.045 | -0.024 |
| state_15_nd | 0.002 | -0.024 |
| state_13_mi | 0.032 | -0.025 |
| state_15_co | 0.021 | -0.025 |
| logcost_health_bills_13 | 0.788 | -0.025 |
| occ_self_17_arts | 0.024 | -0.025 |
| occ_self_15_officeadmin | 0.104 | -0.025 |
| religion_spouse_13_other | 0.007 | -0.025 |
| region_19_akhi | 0.003 | -0.025 |
| logcost_health_hospital_11 | 1.8 | -0.026 |
| union_spouse_11_no | 0.274 | -0.026 |
| grewup_region_spouse_13_west | 0.086 | -0.026 |
| logcost_housing_insurance_13 | 4.2 | -0.026 |
| religion_spouse_17_none | 0.349 | -0.026 |
| occ_self_19_food | 0.043 | -0.026 |
| state_11_or | 0.019 | -0.027 |
| religion_spouse_11_other | 0.007 | -0.027 |
| logcost_health_bills_11 | 0.716 | -0.027 |
| logwealth_other_17 | 10.4 | -0.027 |
| occ_spouse_13_transport | 0.02 | -0.027 |
| religion_self_17_nonchristian | 0.031 | -0.027 |
| ind_spouse_19_farmfishforest | 0.01 | -0.027 |
| moved_why_11_consless | 0.019 | -0.027 |
| state_11_sd | 0.003 | -0.027 |
| state_15_ar | 0.018 | -0.028 |
| state_15_ne | 0.008 | -0.028 |
| mightmove_13_no | 0.588 | -0.028 |
| moved_15_no | 0.611 | -0.029 |
| state_11_ne | 0.008 | -0.029 |
| empstat_current_spouse_11_working | 0.37 | -0.029 |
| religion_spouse_13_none | 0.262 | -0.029 |
| own_or_rent_11_own | 0.581 | -0.029 |
| religion_spouse_19_none | 0.294 | -0.029 |
| state_19_pa | 0.045 | -0.029 |
| occ_self_11_arts | 0.014 | -0.03 |
| state_19_ks | 0.005 | -0.03 |
| state_17_ar | 0.019 | -0.03 |
| state_19_ar | 0.019 | -0.03 |
| empstat_current_self_19_student | 0.006 | -0.03 |
| ind_spouse_17_manufacturing | 0.058 | -0.031 |
| logcost_recreation_13 | 5.4 | -0.031 |
| empstat_current_self_15_disabled | 0.008 | -0.031 |
| state_13_ar | 0.019 | -0.031 |
| state_15_oh | 0.034 | -0.031 |
| religion_self_19_nonchristian | 0.033 | -0.031 |
| occ_self_19_arts | 0.027 | -0.031 |
| state_17_oh | 0.034 | -0.031 |
| occ_self_13_officeadmin | 0.095 | -0.031 |
| own_or_rent_19_neither | 0.03 | -0.032 |
| state_17_mi | 0.036 | -0.032 |
| religion_spouse_15_none | 0.292 | -0.032 |
| grewup_region_spouse_11_west | 0.084 | -0.032 |
| empstat_current_spouse_13_disabled | 0.01 | -0.032 |
| occ_spouse_19_management | 0.063 | -0.032 |
| mightmove_15_no | 0.572 | -0.032 |
| occ_self_17_sales | 0.073 | -0.032 |
| moved_17_no | 0.654 | -0.032 |
| state_13_ne | 0.008 | -0.032 |
| state_13_ks | 0.006 | -0.033 |
| empstat_current_spouse_13_retired | 0.028 | -0.033 |
| own_or_rent_17_neither | 0.03 | -0.033 |
| occ_spouse_11_repair | 0.017 | -0.033 |
| state_19_mi | 0.036 | -0.033 |
| logcost_housing_repairs_11 | 4.2 | -0.033 |
| state_13_oh | 0.035 | -0.033 |
| state_11_oh | 0.036 | -0.034 |
| occ_spouse_15_management | 0.044 | -0.034 |
| state_19_oh | 0.032 | -0.034 |
| religion_spouse_17_protestant | 0.295 | -0.034 |
| occ_self_13_education | 0.041 | -0.034 |
| empstat_current_spouse_19_retired | 0.058 | -0.034 |
| logwealth_homeequity_11 | 6.9 | -0.034 |
| occ_self_19_education | 0.056 | -0.035 |
| logwealth_other_19 | 10.4 | -0.035 |
| state_17_ks | 0.006 | -0.035 |
| state_11_in | 0.026 | -0.035 |
| logwealth_homeequity_13 | 6.8 | -0.035 |
| ind_spouse_15_farmfishforest | 0.01 | -0.036 |
| state_19_in | 0.027 | -0.036 |
| state_11_ar | 0.018 | -0.036 |
| race_spouse_15_white | 0.446 | -0.036 |
| race_self_19_white | 0.747 | -0.036 |
| state_15_ks | 0.007 | -0.037 |
| empstat_current_spouse_15_retired | 0.036 | -0.037 |
| state_17_ne | 0.012 | -0.037 |
| occ_spouse_11_management | 0.044 | -0.038 |
| ind_spouse_15_manufacturing | 0.052 | -0.038 |
| occ_self_11_education | 0.036 | -0.038 |
| state_19_ne | 0.012 | -0.038 |
| occ_self_17_education | 0.05 | -0.038 |
| own_or_rent_13_own | 0.562 | -0.038 |
| occ_self_19_sales | 0.083 | -0.038 |
| sex_spouse_19_male | 0.31 | -0.039 |
| occ_self_15_education | 0.043 | -0.039 |
| ind_spouse_19_manufacturing | 0.061 | -0.039 |
| empstat_current_spouse_17_retired | 0.043 | -0.039 |
| empstat_current_self_17_housespouse | 0.021 | -0.04 |
| state_15_in | 0.027 | -0.04 |
| occ_spouse_13_management | 0.046 | -0.041 |
| empstat_current_self_11_retired | 0.012 | -0.042 |
| logwealth_other_13 | 10.3 | -0.042 |
| logcost_food_away_11 | 7.0 | -0.043 |
| state_17_in | 0.027 | -0.043 |
| state_13_in | 0.027 | -0.045 |
| logwealth_13 | 10.9 | -0.046 |
| race_spouse_13_white | 0.423 | -0.047 |
| empstat_current_self_13_housespouse | 0.026 | -0.047 |
| sex_spouse_17_male | 0.278 | -0.047 |
| race_spouse_11_white | 0.414 | -0.048 |
| empstat_current_spouse_11_retired | 0.022 | -0.048 |
| empstat_current_self_13_retired | 0.012 | -0.05 |
| occ_self_11_sales | 0.082 | -0.05 |
| state_17_ia | 0.019 | -0.05 |
| sex_female | 0.476 | -0.05 |
| sex_self_19_female | 0.476 | -0.05 |
| race_self_17_white | 0.668 | -0.05 |
| state_11_ia | 0.018 | -0.05 |
| religion_self_17_protestant | 0.418 | -0.05 |
| empstat_current_self_15_retired | 0.019 | -0.051 |
| religion_spouse_15_protestant | 0.27 | -0.051 |
| religion_spouse_11_protestant | 0.246 | -0.051 |
| sex_self_17_female | 0.424 | -0.051 |
| religion_spouse_13_protestant | 0.253 | -0.052 |
| empstat_current_self_19_retired | 0.024 | -0.052 |
| state_19_ia | 0.019 | -0.052 |
| empstat_17_retired | 0.014 | -0.052 |
| state_13_ia | 0.019 | -0.054 |
| occ_self_19_pcareservice | 0.033 | -0.055 |
| state_15_ia | 0.019 | -0.055 |
| empstat_current_self_11_housespouse | 0.03 | -0.056 |
| religion_self_11_protestant | 0.334 | -0.057 |
| occ_self_13_sales | 0.084 | -0.057 |
| empstat_current_self_15_housespouse | 0.025 | -0.057 |
| occ_self_15_sales | 0.09 | -0.058 |
| race_self_15_white | 0.604 | -0.059 |
| race_self_11_white | 0.54 | -0.06 |
| religion_self_13_protestant | 0.353 | -0.06 |
| religion_self_15_protestant | 0.378 | -0.062 |
| sex_spouse_15_male | 0.245 | -0.063 |
| grewup_region_spouse_11_northcentral | 0.124 | -0.066 |
| grewup_region_spouse_15_northcentral | 0.133 | -0.066 |
| empstat_current_self_17_retired | 0.024 | -0.066 |
| race_self_13_white | 0.565 | -0.067 |
| grewup_region_self_northcentral | 0.236 | -0.067 |
| grewup_region_spouse_13_northcentral | 0.125 | -0.068 |
| time_housework_self_15 | 9.9 | -0.07 |
| sex_self_15_female | 0.371 | -0.076 |
| region_15_northcentral | 0.2 | -0.077 |
| iswf_11 | 0.227 | -0.08 |
| region_11_northcentral | 0.206 | -0.082 |
| region_13_northcentral | 0.203 | -0.085 |
| region_17_northcentral | 0.213 | -0.086 |
| hourlystatus_self_19_other | 0.114 | -0.087 |
| region_19_northcentral | 0.214 | -0.087 |

</details>


And here's something similar when the selection criteria is a positive response to the question about typical round trip commute time:

Results look qualitatively similar for the most positively correlated variables.
On the negative correlation side of things, the effect of living in the midwest is more obvious, 
and the retail industry and food service occupations are now more negatively correlated.
(Speculation: teenagers?)

<details markdown="block"><summary>Click for full list of correlations.</summary>

| Variable Name | Mean | Correlation |
|:--|:--|:-:|
| time_commute_self_19 | 42.8 | 1.0 |
| time_commute_self_17 | 41.0 | 0.524 |
| time_commute_self_15 | 39.7 | 0.459 |
| time_commute_self_11 | 39.2 | 0.426 |
| time_commute_self_13 | 38.5 | 0.412 |
| time_commute_spouse_19 | 22.7 | 0.166 |
| cost_transport_bustrain_17 | 109.3 | 0.165 |
| cost_transport_bustrain_19 | 129.5 | 0.158 |
| cost_transport_bustrain_13 | 111.4 | 0.155 |
| cost_transport_bustrain_11 | 108.5 | 0.139 |
| cost_transport_bustrain_15 | 110.9 | 0.128 |
| cost_transport_gas_19 | 2324.9 | 0.123 |
| income_labor_self_15 | 49639.1 | 0.12 |
| cost_total_19 | 58089.7 | 0.119 |
| income_labor_self_19 | 55912.3 | 0.117 |
| income_labor_self_17 | 51791.9 | 0.116 |
| cost_transport_gas_17 | 2215.3 | 0.11 |
| cost_total_with_rent_value_19 | 61736.9 | 0.11 |
| income_labor_self_11 | 44150.3 | 0.11 |
| time_commute_spouse_17 | 23.6 | 0.107 |
| cost_housing_19 | 23210.2 | 0.107 |
| income_wagerate_self_15 | 25.1 | 0.106 |
| income_wagerate_self_17 | 26.4 | 0.105 |
| time_commute_spouse_13 | 23.1 | 0.101 |
| cost_housing_tax_19 | 2244.3 | 0.1 |
| income_wagerate_self_19 | 28.5 | 0.1 |
| income_wagerate_self_13 | 24.4 | 0.096 |
| time_commute_spouse_11 | 25.1 | 0.095 |
| cost_housing_mortgage_19 | 6426.8 | 0.09 |
| cost_housing_tax_17 | 1980.5 | 0.09 |
| income_labor_self_13 | 47343.6 | 0.088 |
| time_work_annual_self_15 | 1868.7 | 0.087 |
| income_wagerate_self_11 | 23.0 | 0.086 |
| cost_transport_gas_15 | 2469.9 | 0.084 |
| cost_housing_17 | 21769.6 | 0.082 |
| time_commute_spouse_15 | 23.5 | 0.082 |
| cost_housing_13 | 21092.6 | 0.082 |
| income_familytotal_19 | 106220.6 | 0.08 |
| cost_transport_19 | 11358.2 | 0.079 |
| cost_transport_17 | 10753.6 | 0.077 |
| cost_transport_gas_13 | 3114.7 | 0.076 |
| home_rent_value_17 | 11480.7 | 0.076 |
| hourlystatus_self_17_salaried | 0.291 | 0.076 |
| cost_transport_repair_19 | 881.0 | 0.076 |
| cost_transport_11 | 11115.7 | 0.075 |
| cost_food_19 | 10747.8 | 0.075 |
| time_work_annual_self_19 | 1952.0 | 0.074 |
| cost_trips_19 | 2439.8 | 0.074 |
| home_rent_value_19 | 12318.3 | 0.073 |
| time_work_annual_self_17 | 1887.2 | 0.073 |
| time_work_prevyear_self_15 | 41.5 | 0.072 |
| hourlystatus_self_19_salaried | 0.332 | 0.071 |
| ind_self_19_construction | 0.063 | 0.07 |
| cost_housing_insurance_19 | 786.4 | 0.069 |
| cost_childcare_17 | 699.5 | 0.068 |
| cost_transport_repair_17 | 910.9 | 0.068 |
| cost_food_away_19 | 3229.3 | 0.068 |
| workweeks_self_15 | 43.9 | 0.068 |
| income_familytotal_17 | 98868.4 | 0.067 |
| time_work_self_17 | 37.3 | 0.067 |
| time_work_prevyear_self_19 | 42.2 | 0.067 |
| time_work_annual_self_11 | 1792.7 | 0.066 |
| grewup_state_spouse_19_ny | 0.04 | 0.063 |
| hourlystatus_self_15_salaried | 0.26 | 0.061 |
| ind_self_15_construction | 0.045 | 0.059 |
| time_work_prevyear_self_17 | 41.3 | 0.059 |
| grewup_region_spouse_19_northeast | 0.123 | 0.058 |
| ind_self_17_construction | 0.054 | 0.057 |
| time_housework_spouse_17 | 9.2 | 0.056 |
| grewup_size_spouse_19_bigcity | 0.222 | 0.056 |
| time_shopping_spouse_17 | 2.7 | 0.056 |
| grewup_size_spouse_17_bigcity | 0.197 | 0.054 |
| time_work_annual_self_13 | 1842.6 | 0.054 |
| time_work_self_19 | 37.2 | 0.052 |
| grewup_state_spouse_15_ny | 0.033 | 0.052 |
| grewup_state_spouse_17_ny | 0.036 | 0.052 |
| time_housework_spouse_19 | 9.0 | 0.051 |
| ind_self_13_construction | 0.037 | 0.051 |
| hourlystatus_self_13_salaried | 0.239 | 0.051 |
| workweeks_self_11 | 42.2 | 0.05 |
| workweeks_self_17 | 44.5 | 0.048 |
| ind_self_19_profsciencetech | 0.062 | 0.048 |
| hourlystatus_self_11_salaried | 0.225 | 0.048 |
| ind_self_19_financeinsurance | 0.05 | 0.048 |
| grewup_region_spouse_19_foreign | 0.127 | 0.048 |
| time_housework_spouse_11 | 9.6 | 0.048 |
| hourlystatus_self_19_hourlypluscomm | 0.003 | 0.048 |
| workweeks_self_13 | 43.3 | 0.047 |
| time_work_prevyear_self_11 | 41.0 | 0.046 |
| grewup_region_spouse_17_northeast | 0.111 | 0.046 |
| ind_self_17_financeinsurance | 0.044 | 0.045 |
| time_pcare_spouse_19 | 5.4 | 0.045 |
| grewup_region_spouse_17_foreign | 0.111 | 0.044 |
| grewup_state_spouse_13_ny | 0.031 | 0.044 |
| ind_self_15_financeinsurance | 0.04 | 0.044 |
| ind_self_11_construction | 0.035 | 0.044 |
| grewup_size_self_bigcity | 0.336 | 0.044 |
| grewup_state_spouse_11_ny | 0.03 | 0.042 |
| grewup_region_spouse_15_northeast | 0.104 | 0.042 |
| time_childcare_spouse_19 | 8.2 | 0.041 |
| workweeks_self_19 | 45.9 | 0.041 |
| grewup_size_spouse_15_bigcity | 0.163 | 0.04 |
| ind_self_13_financeinsurance | 0.036 | 0.038 |
| time_childcare_spouse_17 | 8.5 | 0.038 |
| grewup_state_self_ny | 0.059 | 0.038 |
| hourlystatus_spouse_19_salaried | 0.214 | 0.035 |
| time_housework_spouse_15 | 8.7 | 0.035 |
| grewup_state_self_ma | 0.028 | 0.034 |
| ind_spouse_11_financeinsurance | 0.022 | 0.034 |
| income_wagerate_spouse_15 | 15.7 | 0.033 |
| time_work_prevyear_self_13 | 41.5 | 0.033 |
| ind_self_19_transportwarehouse | 0.045 | 0.033 |
| ind_self_11_financeinsurance | 0.035 | 0.033 |
| vacationdays_self_13 | 1.7 | 0.033 |
| empstat_17_other | 0.001 | 0.033 |
| ind_spouse_13_education | 0.048 | 0.032 |
| time_pcare_spouse_17 | 5.4 | 0.032 |
| ind_self_19_management | 0.036 | 0.032 |
| time_shopping_spouse_19 | 2.7 | 0.03 |
| daycare_17_yes | 0.075 | 0.03 |
| grewup_size_spouse_11_bigcity | 0.151 | 0.03 |
| ind_self_15_profsciencetech | 0.049 | 0.029 |
| hourlystatus_self_19_salpluscomm | 0.009 | 0.029 |
| grewup_state_spouse_19_ga | 0.008 | 0.029 |
| grewup_state_spouse_15_ut | 0.008 | 0.029 |
| grewup_size_spouse_13_bigcity | 0.156 | 0.029 |
| sizeworkplace_self_13 | 984.1 | 0.029 |
| ind_self_17_profsciencetech | 0.058 | 0.028 |
| grewup_state_spouse_11_vt | 0.0 | 0.028 |
| grewup_state_spouse_13_vt | 0.0 | 0.028 |
| ind_self_11_manufacturing | 0.076 | 0.028 |
| grewup_state_spouse_19_ma | 0.02 | 0.027 |
| empstat_17_working | 0.823 | 0.027 |
| ind_self_13_management | 0.021 | 0.027 |
| grewup_state_spouse_17_ut | 0.009 | 0.027 |
| grewup_state_spouse_11_dc | 0.001 | 0.027 |
| ind_self_13_manufacturing | 0.081 | 0.027 |
| grewup_state_spouse_17_ma | 0.017 | 0.027 |
| time_housework_spouse_13 | 9.2 | 0.026 |
| grewup_state_self_ut | 0.01 | 0.026 |
| grewup_state_spouse_13_dc | 0.001 | 0.026 |
| grewup_state_spouse_19_ut | 0.01 | 0.026 |
| daycare_19_yes | 0.075 | 0.026 |
| hourlystatus_spouse_17_other | 0.045 | 0.026 |
| ind_spouse_13_financeinsurance | 0.023 | 0.025 |
| hourlystatus_spouse_13_other | 0.038 | 0.025 |
| hourlystatus_self_11_salpluscomm | 0.007 | 0.025 |
| time_volunteering_spouse_17 | 0.835 | 0.025 |
| ind_self_15_utilities | 0.008 | 0.025 |
| grewup_state_spouse_17_dc | 0.001 | 0.024 |
| grewup_state_spouse_13_ut | 0.008 | 0.024 |
| ind_self_17_transportwarehouse | 0.035 | 0.024 |
| grewup_state_spouse_13_ma | 0.016 | 0.024 |
| grewup_state_spouse_13_nh | 0.001 | 0.024 |
| grewup_state_spouse_11_ut | 0.009 | 0.024 |
| grewup_state_spouse_15_dc | 0.001 | 0.023 |
| ind_self_19_information | 0.019 | 0.023 |
| workweeks_spouse_19 | 26.5 | 0.023 |
| grewup_state_spouse_19_nj | 0.02 | 0.023 |
| grewup_state_spouse_19_dc | 0.001 | 0.023 |
| grewup_state_spouse_15_vt | 0.0 | 0.023 |
| hourlystatus_spouse_19_other | 0.052 | 0.023 |
| grewup_state_spouse_11_ga | 0.006 | 0.023 |
| ind_self_13_utilities | 0.007 | 0.023 |
| income_wagerate_spouse_17 | 15.9 | 0.022 |
| income_labor_spouse_19 | 32778.4 | 0.021 |
| ind_spouse_11_realestate | 0.006 | 0.021 |
| grewup_state_spouse_11_ma | 0.015 | 0.021 |
| grewup_state_spouse_19_fl | 0.015 | 0.021 |
| ind_self_11_mining | 0.003 | 0.021 |
| grewup_state_spouse_15_ma | 0.016 | 0.02 |
| sizeworkplace_spouse_19 | 1070.0 | 0.02 |
| time_work_prevyear_spouse_15 | 39.7 | 0.02 |
| ind_self_15_manufacturing | 0.089 | 0.02 |
| ind_self_19_utilities | 0.011 | 0.02 |
| grewup_state_self_ga | 0.011 | 0.02 |
| hourlystatus_self_15_salpluscomm | 0.009 | 0.02 |
| grewup_state_self_ca | 0.083 | 0.02 |
| ind_self_17_mining | 0.004 | 0.019 |
| vacationdays_self_19 | 1.8 | 0.019 |
| income_labor_spouse_15 | 30169.4 | 0.019 |
| income_wagerate_spouse_19 | 17.0 | 0.019 |
| ind_self_17_utilities | 0.009 | 0.018 |
| income_labor_spouse_17 | 30616.5 | 0.018 |
| time_education_spouse_17 | 1.0 | 0.018 |
| grewup_state_spouse_17_il | 0.018 | 0.018 |
| grewup_state_spouse_13_ga | 0.006 | 0.018 |
| ind_self_19_arts | 0.018 | 0.018 |
| empstat_19_working | 0.896 | 0.018 |
| grewup_state_self_dc | 0.002 | 0.017 |
| grewup_state_self_il | 0.029 | 0.017 |
| hourlystatus_spouse_17_salaried | 0.185 | 0.017 |
| ind_self_11_utilities | 0.007 | 0.017 |
| grewup_state_spouse_17_fl | 0.013 | 0.017 |
| empstat_current_self_11_laid off | 0.002 | 0.017 |
| ind_self_11_adminmilitary | 0.047 | 0.017 |
| ind_self_15_mining | 0.004 | 0.017 |
| hourlystatus_spouse_15_salaried | 0.171 | 0.017 |
| grewup_state_spouse_17_ak | 0.001 | 0.017 |
| ind_self_19_mining | 0.005 | 0.017 |
| grewup_state_spouse_19_il | 0.019 | 0.017 |
| grewup_state_spouse_17_vt | 0.0 | 0.017 |
| grewup_state_spouse_19_vt | 0.0 | 0.017 |
| ind_self_11_profsciencetech | 0.041 | 0.017 |
| grewup_state_spouse_13_ak | 0.001 | 0.016 |
| ind_spouse_13_profsciencetech | 0.027 | 0.016 |
| hourlystatus_self_11_hourlypluscomm | 0.004 | 0.016 |
| ind_self_13_mining | 0.004 | 0.016 |
| grewup_state_spouse_15_al | 0.006 | 0.016 |
| grewup_state_spouse_17_ga | 0.007 | 0.016 |
| sizeworkplace_self_19 | 775.8 | 0.015 |
| workweeks_spouse_15 | 26.9 | 0.015 |
| ind_self_13_profsciencetech | 0.042 | 0.015 |
| grewup_state_spouse_11_ok | 0.005 | 0.015 |
| grewup_state_spouse_19_ak | 0.001 | 0.015 |
| grewup_state_spouse_15_ak | 0.001 | 0.015 |
| grewup_state_spouse_11_nh | 0.001 | 0.014 |
| grewup_state_spouse_13_al | 0.006 | 0.014 |
| hourlystatus_spouse_13_salaried | 0.158 | 0.014 |
| ind_self_15_transportwarehouse | 0.032 | 0.014 |
| ind_spouse_13_realestate | 0.006 | 0.014 |
| ind_self_11_transportwarehouse | 0.026 | 0.014 |
| time_work_spouse_19 | 21.3 | 0.014 |
| empstat_11_laid off | 0.004 | 0.014 |
| ind_self_17_information | 0.017 | 0.014 |
| workweeks_spouse_17 | 26.6 | 0.014 |
| sizeworkplace_self_17 | 791.6 | 0.014 |
| ind_self_15_information | 0.015 | 0.013 |
| ind_self_13_information | 0.015 | 0.013 |
| grewup_state_spouse_19_ok | 0.006 | 0.013 |
| ind_spouse_11_information | 0.01 | 0.013 |
| ind_self_15_adminmilitary | 0.051 | 0.013 |
| ind_spouse_11_otherservices | 0.021 | 0.013 |
| empstat_11_working | 0.617 | 0.013 |
| ind_self_15_management | 0.025 | 0.013 |
| grewup_state_spouse_17_tx | 0.024 | 0.012 |
| ind_spouse_11_arts | 0.007 | 0.012 |
| ind_spouse_11_education | 0.044 | 0.012 |
| grewup_state_spouse_17_nh | 0.001 | 0.012 |
| grewup_state_spouse_11_nj | 0.016 | 0.012 |
| grewup_state_spouse_15_ga | 0.006 | 0.012 |
| grewup_state_spouse_19_tx | 0.027 | 0.012 |
| empstat_19_laid off | 0.006 | 0.012 |
| grewup_state_spouse_15_fl | 0.01 | 0.012 |
| grewup_state_self_id | 0.002 | 0.012 |
| grewup_state_self_al | 0.008 | 0.012 |
| grewup_state_spouse_11_fl | 0.008 | 0.012 |
| grewup_state_spouse_11_al | 0.005 | 0.012 |
| empstat_15_searching | 0.036 | 0.012 |
| empstat_current_self_15_working | 0.667 | 0.012 |
| grewup_state_spouse_17_nj | 0.018 | 0.012 |
| ind_self_17_management | 0.03 | 0.012 |
| empstat_current_self_11_working | 0.566 | 0.012 |
| grewup_state_spouse_15_nj | 0.018 | 0.012 |
| hourlystatus_self_13_salpluscomm | 0.008 | 0.012 |
| grewup_state_spouse_13_ok | 0.004 | 0.012 |
| hourlystatus_self_17_salpluscomm | 0.009 | 0.011 |
| time_education_spouse_19 | 0.979 | 0.011 |
| daycare_13_yes | 0.067 | 0.011 |
| time_leisure_spouse_19 | 10.2 | 0.011 |
| grewup_state_spouse_19_nh | 0.001 | 0.011 |
| time_work_annual_spouse_19 | 1111.0 | 0.011 |
| grewup_state_spouse_13_id | 0.001 | 0.011 |
| empstat_13_working | 0.656 | 0.01 |
| grewup_state_spouse_17_wv | 0.002 | 0.01 |
| empstat_current_self_11_disabled | 0.004 | 0.01 |
| empstat_11_disabled | 0.004 | 0.01 |
| grewup_state_spouse_11_id | 0.001 | 0.01 |
| empstat_11_other | 0.002 | 0.01 |
| grewup_state_spouse_17_al | 0.006 | 0.01 |
| empstat_19_disabled | 0.006 | 0.01 |
| ind_self_13_adminmilitary | 0.05 | 0.01 |
| grewup_state_spouse_11_ak | 0.001 | 0.01 |
| grewup_state_self_vt | 0.0 | 0.01 |
| grewup_size_self_other | 0.028 | 0.01 |
| empstat_17_laid off | 0.004 | 0.009 |
| ind_spouse_13_health | 0.059 | 0.009 |
| grewup_state_spouse_17_wy | 0.0 | 0.009 |
| grewup_state_self_md | 0.013 | 0.009 |
| grewup_state_self_mt | 0.001 | 0.009 |
| ind_self_13_transportwarehouse | 0.028 | 0.009 |
| grewup_state_spouse_13_wv | 0.002 | 0.008 |
| hourlystatus_spouse_11_hourlypluscomm | 0.002 | 0.008 |
| empstat_current_self_13_working | 0.609 | 0.008 |
| ind_spouse_11_DKNARefused | 0.002 | 0.008 |
| hourlystatus_spouse_11_salaried | 0.153 | 0.008 |
| sizeworkplace_self_11 | 10661.1 | 0.008 |
| sizeworkplace_self_15 | 911.3 | 0.008 |
| grewup_state_spouse_15_wv | 0.001 | 0.008 |
| grewup_state_spouse_19_wy | 0.0 | 0.008 |
| grewup_state_spouse_19_wv | 0.002 | 0.008 |
| grewup_state_spouse_11_mn | 0.007 | 0.007 |
| ind_self_17_arts | 0.014 | 0.007 |
| grewup_state_spouse_13_tx | 0.021 | 0.007 |
| income_wagerate_spouse_13 | 15.5 | 0.007 |
| grewup_state_spouse_17_ok | 0.006 | 0.007 |
| grewup_state_self_tx | 0.04 | 0.007 |
| grewup_state_spouse_13_fl | 0.009 | 0.007 |
| grewup_state_self_hi | 0.001 | 0.007 |
| daycare_11_yes | 0.072 | 0.007 |
| grewup_state_spouse_13_ca | 0.038 | 0.007 |
| grewup_state_spouse_11_tx | 0.019 | 0.007 |
| grewup_state_self_nj | 0.03 | 0.006 |
| grewup_state_spouse_19_de | 0.0 | 0.006 |
| empstat_15_laid off | 0.003 | 0.006 |
| empstat_13_other | 0.001 | 0.006 |
| grewup_state_self_az | 0.011 | 0.006 |
| empstat_current_self_17_laid off | 0.003 | 0.006 |
| ind_self_17_manufacturing | 0.102 | 0.005 |
| ind_spouse_11_health | 0.057 | 0.005 |
| grewup_state_spouse_15_ca | 0.041 | 0.005 |
| vacationdays_self_15 | 2.0 | 0.005 |
| grewup_region_spouse_19_akhi | 0.001 | 0.005 |
| grewup_state_spouse_15_tx | 0.022 | 0.005 |
| grewup_state_spouse_17_ca | 0.046 | 0.005 |
| empstat_current_self_15_student | 0.01 | 0.005 |
| ind_spouse_13_otherservices | 0.019 | 0.005 |
| grewup_state_spouse_11_ca | 0.035 | 0.005 |
| ind_self_11_information | 0.017 | 0.005 |
| ind_spouse_13_arts | 0.007 | 0.005 |
| grewup_state_spouse_19_al | 0.006 | 0.005 |
| grewup_state_spouse_11_wy | 0.0 | 0.004 |
| grewup_state_spouse_13_wy | 0.0 | 0.004 |
| grewup_state_spouse_15_wy | 0.0 | 0.004 |
| grewup_state_self_mn | 0.011 | 0.004 |
| grewup_state_spouse_19_ca | 0.054 | 0.004 |
| vacationdays_spouse_13 | 0.954 | 0.004 |
| ind_self_11_management | 0.022 | 0.004 |
| ind_self_11_realestate | 0.011 | 0.004 |
| time_work_annual_spouse_15 | 1118.7 | 0.004 |
| empstat_19_student | 0.006 | 0.003 |
| grewup_state_self_wv | 0.002 | 0.003 |
| grewup_region_spouse_17_akhi | 0.001 | 0.003 |
| empstat_current_self_11_student | 0.01 | 0.003 |
| hourlystatus_spouse_13_hourlypluscomm | 0.001 | 0.003 |
| age_self_19 | 45.1 | 0.003 |
| time_adultcare_spouse_17 | 0.444 | 0.003 |
| ind_self_17_realestate | 0.017 | 0.003 |
| age_self_17 | 44.5 | 0.003 |
| grewup_region_spouse_19_south | 0.161 | 0.003 |
| ind_self_19_manufacturing | 0.115 | 0.003 |
| vacationdays_self_17 | 1.6 | 0.002 |
| empstat_15_working | 0.714 | 0.002 |
| ind_spouse_13_information | 0.01 | 0.002 |
| grewup_state_spouse_15_ok | 0.005 | 0.002 |
| grewup_state_self_ky | 0.014 | 0.002 |
| grewup_state_spouse_13_ms | 0.005 | 0.002 |
| grewup_state_spouse_19_md | 0.008 | 0.002 |
| ind_spouse_13_transportwarehouse | 0.016 | 0.002 |
| ind_spouse_11_profsciencetech | 0.023 | 0.002 |
| hourlystatus_spouse_19_hourlypluscomm | 0.001 | 0.002 |
| grewup_state_spouse_17_md | 0.007 | 0.002 |
| grewup_state_spouse_19_mt | 0.001 | 0.001 |
| daycare_19_no | 0.297 | 0.001 |
| workweeks_spouse_13 | 27.0 | 0.001 |
| grewup_state_spouse_19_pa | 0.033 | 0.001 |
| grewup_state_spouse_15_nm | 0.001 | 0.001 |
| grewup_state_spouse_11_wv | 0.001 | 0.001 |
| grewup_state_spouse_13_mn | 0.007 | 0.001 |
| grewup_state_spouse_19_tn | 0.01 | 0.001 |
| vacationdays_spouse_11 | 0.909 | 0.001 |
| time_work_annual_spouse_17 | 1110.8 | 0.001 |
| grewup_state_spouse_15_mn | 0.006 | 0.0 |
| grewup_state_spouse_19_nv | 0.001 | 0.0 |
| daycare_17_no | 0.287 | 0.0 |
| grewup_state_spouse_15_pa | 0.029 | 0.0 |
| empstat_17_searching | 0.038 | 0.0 |
| grewup_state_spouse_17_pa | 0.03 | 0.0 |
| ind_self_19_adminmilitary | 0.063 | -0.0 |
| ind_self_13_realestate | 0.013 | -0.0 |
| income_labor_spouse_13 | 28749.2 | -0.0 |
| daycare_15_yes | 0.064 | -0.001 |
| grewup_state_spouse_11_de | 0.0 | -0.001 |
| grewup_state_spouse_13_de | 0.0 | -0.001 |
| grewup_state_spouse_15_de | 0.0 | -0.001 |
| grewup_state_spouse_17_de | 0.0 | -0.001 |
| grewup_state_spouse_13_nj | 0.017 | -0.001 |
| ind_spouse_11_accomodationsfood | 0.019 | -0.001 |
| vacationdays_spouse_19 | 1.1 | -0.001 |
| grewup_state_self_tn | 0.017 | -0.001 |
| age_spouse_17 | 45.7 | -0.001 |
| hourlystatus_spouse_15_hourlypluscomm | 0.001 | -0.001 |
| time_education_self_17 | 1.5 | -0.001 |
| grewup_state_spouse_19_ms | 0.007 | -0.001 |
| sizeworkplace_spouse_17 | 814.1 | -0.001 |
| grewup_state_spouse_17_ms | 0.006 | -0.001 |
| grewup_state_spouse_11_hi | 0.001 | -0.002 |
| grewup_state_spouse_15_hi | 0.001 | -0.002 |
| empstat_13_student | 0.032 | -0.002 |
| grewup_state_self_ct | 0.009 | -0.002 |
| grewup_state_spouse_13_hi | 0.001 | -0.002 |
| vacationdays_spouse_15 | 1.2 | -0.002 |
| time_work_spouse_17 | 21.8 | -0.002 |
| hourlystatus_spouse_11_other | 0.033 | -0.002 |
| hourlystatus_spouse_11_hourlyplustips | 0.001 | -0.002 |
| grewup_state_spouse_15_ms | 0.006 | -0.002 |
| grewup_state_spouse_19_id | 0.001 | -0.002 |
| grewup_state_spouse_15_ct | 0.004 | -0.002 |
| grewup_state_spouse_15_il | 0.015 | -0.002 |
| ind_self_17_adminmilitary | 0.054 | -0.002 |
| time_leisure_spouse_17 | 10.4 | -0.002 |
| grewup_size_spouse_19_suburban | 0.38 | -0.003 |
| vacationdays_self_11 | 1.5 | -0.003 |
| hourlystatus_spouse_13_hourlyplustips | 0.001 | -0.003 |
| grewup_state_spouse_13_tn | 0.007 | -0.003 |
| empstat_11_student | 0.033 | -0.003 |
| grewup_size_spouse_11_other | 0.011 | -0.003 |
| grewup_state_spouse_11_ms | 0.005 | -0.003 |
| empstat_current_self_15_laid off | 0.002 | -0.003 |
| grewup_state_spouse_19_mi | 0.024 | -0.003 |
| grewup_state_self_ne | 0.009 | -0.004 |
| time_volunteering_spouse_19 | 0.752 | -0.004 |
| grewup_state_self_wy | 0.001 | -0.004 |
| grewup_state_spouse_15_tn | 0.008 | -0.004 |
| grewup_state_self_ms | 0.011 | -0.004 |
| empstat_current_self_15_searching | 0.026 | -0.004 |
| grewup_state_spouse_17_id | 0.001 | -0.004 |
| ind_self_11_otherservices | 0.03 | -0.004 |
| grewup_region_spouse_17_south | 0.144 | -0.004 |
| grewup_state_spouse_11_md | 0.004 | -0.004 |
| grewup_state_spouse_19_sc | 0.009 | -0.004 |
| empstat_15_disabled | 0.006 | -0.004 |
| grewup_state_spouse_17_mi | 0.021 | -0.004 |
| grewup_state_spouse_17_tn | 0.009 | -0.005 |
| grewup_state_spouse_17_ct | 0.004 | -0.005 |
| grewup_state_spouse_13_nm | 0.001 | -0.005 |
| grewup_state_spouse_13_ct | 0.003 | -0.005 |
| grewup_state_self_me | 0.003 | -0.005 |
| hourlystatus_self_13_hourlypluscomm | 0.003 | -0.005 |
| grewup_state_spouse_11_nm | 0.001 | -0.005 |
| grewup_state_self_wa | 0.02 | -0.005 |
| grewup_state_spouse_13_il | 0.014 | -0.005 |
| empstat_19_searching | 0.037 | -0.006 |
| time_childcare_self_19 | 9.0 | -0.006 |
| grewup_state_spouse_19_hi | 0.001 | -0.006 |
| grewup_state_spouse_15_md | 0.006 | -0.006 |
| grewup_state_spouse_15_nh | 0.001 | -0.006 |
| ind_self_19_wholesale | 0.029 | -0.006 |
| grewup_state_spouse_15_mi | 0.019 | -0.006 |
| income_wagerate_spouse_11 | 15.3 | -0.006 |
| time_work_prevyear_spouse_19 | 39.1 | -0.006 |
| hourlystatus_spouse_15_hourlyplustips | 0.001 | -0.007 |
| grewup_state_spouse_13_md | 0.005 | -0.007 |
| grewup_state_spouse_17_ne | 0.005 | -0.007 |
| grewup_state_spouse_11_il | 0.014 | -0.007 |
| ind_self_19_realestate | 0.018 | -0.007 |
| grewup_state_spouse_17_mt | 0.0 | -0.007 |
| hourlystatus_spouse_17_hourlypluscomm | 0.002 | -0.007 |
| grewup_state_spouse_19_ct | 0.005 | -0.008 |
| ind_self_15_realestate | 0.013 | -0.008 |
| grewup_state_spouse_17_nv | 0.001 | -0.008 |
| grewup_state_spouse_11_tn | 0.007 | -0.008 |
| grewup_state_spouse_19_nm | 0.001 | -0.008 |
| ind_self_11_wholesale | 0.019 | -0.008 |
| hourlystatus_spouse_11_salpluscomm | 0.004 | -0.008 |
| grewup_state_spouse_11_ct | 0.003 | -0.008 |
| grewup_state_spouse_11_pa | 0.027 | -0.008 |
| grewup_state_spouse_11_ne | 0.005 | -0.008 |
| time_childcare_self_17 | 9.7 | -0.008 |
| grewup_state_self_de | 0.0 | -0.008 |
| age_spouse_19 | 46.3 | -0.008 |
| ind_spouse_11_transportwarehouse | 0.017 | -0.008 |
| grewup_state_spouse_15_me | 0.003 | -0.008 |
| grewup_state_spouse_13_pa | 0.029 | -0.008 |
| ind_self_13_wholesale | 0.019 | -0.008 |
| grewup_size_spouse_13_other | 0.012 | -0.008 |
| grewup_state_spouse_11_va | 0.012 | -0.008 |
| empstat_current_self_17_disabled | 0.006 | -0.009 |
| ind_self_17_wholesale | 0.025 | -0.009 |
| grewup_state_spouse_11_me | 0.003 | -0.009 |
| grewup_state_spouse_19_ky | 0.009 | -0.009 |
| grewup_state_spouse_17_hi | 0.001 | -0.009 |
| grewup_state_self_fl | 0.025 | -0.009 |
| ind_spouse_11_adminmilitary | 0.031 | -0.009 |
| grewup_state_spouse_11_mt | 0.0 | -0.009 |
| grewup_state_spouse_13_mt | 0.0 | -0.009 |
| grewup_state_spouse_15_mt | 0.0 | -0.009 |
| grewup_state_spouse_17_nm | 0.001 | -0.009 |
| grewup_state_spouse_19_mn | 0.009 | -0.009 |
| grewup_state_spouse_13_sd | 0.003 | -0.009 |
| grewup_state_spouse_15_id | 0.001 | -0.009 |
| grewup_state_self_nc | 0.023 | -0.009 |
| hourlystatus_spouse_15_other | 0.036 | -0.009 |
| empstat_current_self_13_student | 0.012 | -0.01 |
| grewup_state_spouse_15_ky | 0.008 | -0.01 |
| ind_spouse_13_mining | 0.003 | -0.01 |
| grewup_state_self_nm | 0.001 | -0.01 |
| ind_self_17_DKNARefused | 0.003 | -0.01 |
| grewup_state_spouse_19_me | 0.003 | -0.01 |
| grewup_state_self_ri | 0.001 | -0.01 |
| grewup_state_spouse_17_me | 0.003 | -0.01 |
| ind_spouse_13_management | 0.013 | -0.01 |
| ind_spouse_11_retail | 0.034 | -0.01 |
| grewup_state_spouse_15_sc | 0.008 | -0.01 |
| hourlystatus_spouse_19_hourly | 0.254 | -0.01 |
| grewup_state_spouse_17_sc | 0.008 | -0.01 |
| ind_spouse_11_mining | 0.002 | -0.01 |
| grewup_state_spouse_13_ky | 0.008 | -0.01 |
| hourlystatus_self_17_hourlypluscomm | 0.002 | -0.01 |
| grewup_size_spouse_19_other | 0.015 | -0.01 |
| hourlystatus_spouse_19_salpluscomm | 0.005 | -0.01 |
| grewup_state_spouse_11_sd | 0.003 | -0.01 |
| hourlystatus_spouse_17_hourly | 0.238 | -0.011 |
| hourlystatus_self_17_hourlyplustips | 0.007 | -0.011 |
| ind_self_17_otherservices | 0.043 | -0.011 |
| income_labor_spouse_11 | 27998.9 | -0.011 |
| ind_spouse_13_utilities | 0.005 | -0.011 |
| grewup_state_spouse_15_nv | 0.001 | -0.011 |
| hourlystatus_spouse_19_hourlyplustips | 0.003 | -0.011 |
| grewup_state_spouse_15_sd | 0.003 | -0.011 |
| grewup_state_spouse_17_az | 0.006 | -0.011 |
| grewup_state_spouse_11_mi | 0.017 | -0.011 |
| ind_spouse_13_adminmilitary | 0.032 | -0.011 |
| grewup_state_spouse_17_ky | 0.009 | -0.011 |
| grewup_state_spouse_15_az | 0.005 | -0.011 |
| grewup_size_spouse_17_other | 0.014 | -0.011 |
| workweeks_spouse_11 | 27.1 | -0.011 |
| grewup_state_spouse_11_ky | 0.008 | -0.012 |
| ind_spouse_13_DKNARefused | 0.003 | -0.012 |
| grewup_size_spouse_15_other | 0.012 | -0.012 |
| grewup_state_spouse_13_sc | 0.007 | -0.012 |
| grewup_state_self_la | 0.008 | -0.012 |
| grewup_state_spouse_13_mi | 0.017 | -0.012 |
| grewup_state_spouse_11_ar | 0.012 | -0.012 |
| hourlystatus_self_19_other | 0.07 | -0.012 |
| time_volunteering_self_17 | 1.0 | -0.012 |
| grewup_state_spouse_17_mn | 0.008 | -0.012 |
| empstat_current_self_15_disabled | 0.007 | -0.013 |
| grewup_state_spouse_13_va | 0.013 | -0.013 |
| age_spouse_15 | 45.4 | -0.013 |
| grewup_region_spouse_19_west | 0.109 | -0.013 |
| ind_spouse_13_accomodationsfood | 0.018 | -0.013 |
| time_work_annual_spouse_13 | 1125.6 | -0.013 |
| grewup_state_spouse_11_sc | 0.007 | -0.013 |
| grewup_state_spouse_19_az | 0.007 | -0.013 |
| grewup_state_self_pa | 0.046 | -0.013 |
| grewup_state_self_sc | 0.018 | -0.013 |
| time_work_prevyear_spouse_13 | 40.0 | -0.013 |
| grewup_state_spouse_17_va | 0.015 | -0.013 |
| daycare_15_no | 0.278 | -0.013 |
| grewup_state_spouse_19_ne | 0.006 | -0.013 |
| grewup_state_spouse_13_ar | 0.012 | -0.013 |
| grewup_state_spouse_11_ri | 0.0 | -0.013 |
| grewup_state_spouse_15_ne | 0.005 | -0.013 |
| grewup_state_spouse_19_ar | 0.015 | -0.013 |
| grewup_state_spouse_15_va | 0.015 | -0.014 |
| grewup_state_spouse_19_mo | 0.018 | -0.014 |
| grewup_state_spouse_13_me | 0.003 | -0.014 |
| grewup_region_spouse_15_south | 0.131 | -0.014 |
| ind_self_13_DKNARefused | 0.003 | -0.014 |
| ind_self_11_DKNARefused | 0.001 | -0.014 |
| grewup_state_spouse_15_la | 0.004 | -0.014 |
| ind_spouse_11_management | 0.013 | -0.014 |
| ind_spouse_13_construction | 0.024 | -0.014 |
| ind_self_13_otherservices | 0.033 | -0.015 |
| grewup_state_spouse_13_ri | 0.0 | -0.015 |
| grewup_state_spouse_15_ri | 0.0 | -0.015 |
| ind_spouse_11_utilities | 0.005 | -0.015 |
| ind_self_15_wholesale | 0.019 | -0.015 |
| grewup_state_self_ak | 0.001 | -0.015 |
| ind_self_19_DKNARefused | 0.002 | -0.015 |
| grewup_state_spouse_13_nv | 0.001 | -0.015 |
| grewup_state_spouse_17_ri | 0.0 | -0.015 |
| grewup_state_spouse_19_ri | 0.0 | -0.015 |
| time_work_prevyear_spouse_17 | 39.5 | -0.015 |
| daycare_11_no | 0.33 | -0.015 |
| grewup_state_spouse_19_wi | 0.01 | -0.015 |
| grewup_state_spouse_11_az | 0.005 | -0.015 |
| grewup_state_self_nv | 0.001 | -0.016 |
| time_education_self_19 | 1.4 | -0.016 |
| grewup_state_spouse_17_wi | 0.009 | -0.016 |
| age_spouse_11 | 43.5 | -0.016 |
| grewup_state_spouse_17_la | 0.004 | -0.016 |
| hourlystatus_spouse_17_hourlyplustips | 0.002 | -0.016 |
| time_leisure_self_19 | 14.4 | -0.016 |
| grewup_state_spouse_13_co | 0.007 | -0.016 |
| time_pcare_self_19 | 7.7 | -0.016 |
| empstat_current_self_13_searching | 0.032 | -0.016 |
| grewup_state_spouse_19_sd | 0.004 | -0.016 |
| grewup_state_spouse_13_wi | 0.008 | -0.016 |
| grewup_state_self_ar | 0.02 | -0.016 |
| ind_self_17_health | 0.129 | -0.017 |
| grewup_state_spouse_19_la | 0.004 | -0.017 |
| grewup_state_spouse_17_sd | 0.004 | -0.017 |
| hourlystatus_spouse_17_salpluscomm | 0.006 | -0.017 |
| grewup_state_spouse_13_az | 0.005 | -0.017 |
| grewup_state_spouse_15_co | 0.007 | -0.017 |
| grewup_state_spouse_15_ar | 0.013 | -0.017 |
| grewup_state_spouse_19_nc | 0.015 | -0.017 |
| grewup_state_spouse_17_nc | 0.014 | -0.017 |
| grewup_state_spouse_17_ar | 0.014 | -0.017 |
| time_adultcare_spouse_19 | 0.456 | -0.017 |
| hourlystatus_self_15_hourlypluscomm | 0.003 | -0.017 |
| grewup_state_self_mi | 0.038 | -0.018 |
| grewup_region_spouse_17_west | 0.094 | -0.018 |
| grewup_state_spouse_11_oh | 0.022 | -0.018 |
| grewup_state_spouse_15_oh | 0.025 | -0.018 |
| grewup_state_spouse_11_co | 0.007 | -0.018 |
| grewup_state_self_wi | 0.012 | -0.018 |
| grewup_region_spouse_15_west | 0.087 | -0.018 |
| hourlystatus_spouse_15_salpluscomm | 0.006 | -0.018 |
| grewup_state_spouse_15_wi | 0.008 | -0.018 |
| grewup_state_spouse_19_or | 0.012 | -0.019 |
| sizeworkplace_spouse_11 | 702.9 | -0.019 |
| ind_spouse_13_retail | 0.035 | -0.019 |
| grewup_state_self_nh | 0.001 | -0.019 |
| grewup_state_spouse_13_ne | 0.004 | -0.019 |
| grewup_state_spouse_19_va | 0.018 | -0.019 |
| grewup_state_spouse_19_wa | 0.013 | -0.019 |
| hourlystatus_self_13_hourlyplustips | 0.004 | -0.019 |
| grewup_state_spouse_17_oh | 0.028 | -0.019 |
| grewup_state_spouse_17_in | 0.017 | -0.02 |
| ind_self_19_health | 0.151 | -0.02 |
| grewup_state_self_nd | 0.003 | -0.02 |
| grewup_state_spouse_11_nv | 0.001 | -0.02 |
| sizeworkplace_spouse_15 | 796.2 | -0.02 |
| time_adultcare_self_17 | 0.764 | -0.02 |
| grewup_state_spouse_19_in | 0.017 | -0.02 |
| ind_self_19_farmfishforest | 0.018 | -0.021 |
| grewup_state_spouse_15_in | 0.014 | -0.021 |
| grewup_state_spouse_11_wi | 0.007 | -0.021 |
| ind_self_11_arts | 0.011 | -0.021 |
| grewup_state_spouse_17_or | 0.011 | -0.021 |
| grewup_state_spouse_11_in | 0.012 | -0.021 |
| ind_self_17_accomodationsfood | 0.052 | -0.021 |
| sizeworkplace_spouse_13 | 822.6 | -0.021 |
| hourlystatus_spouse_15_hourly | 0.2 | -0.021 |
| time_pcare_self_17 | 7.7 | -0.021 |
| grewup_state_spouse_13_in | 0.012 | -0.021 |
| grewup_state_spouse_13_oh | 0.024 | -0.021 |
| grewup_size_self_suburban | 0.529 | -0.021 |
| grewup_state_spouse_17_ks | 0.003 | -0.022 |
| ind_self_17_farmfishforest | 0.017 | -0.022 |
| grewup_state_spouse_13_la | 0.004 | -0.022 |
| grewup_state_spouse_19_oh | 0.031 | -0.022 |
| grewup_state_spouse_19_co | 0.009 | -0.022 |
| time_work_prevyear_spouse_11 | 39.7 | -0.022 |
| age_spouse_13 | 44.4 | -0.022 |
| grewup_state_spouse_11_la | 0.004 | -0.022 |
| hourlystatus_spouse_13_salpluscomm | 0.005 | -0.022 |
| grewup_state_spouse_17_co | 0.008 | -0.022 |
| ind_self_15_otherservices | 0.036 | -0.022 |
| ind_spouse_11_construction | 0.024 | -0.022 |
| hourlystatus_self_13_other | 0.054 | -0.023 |
| ind_self_11_farmfishforest | 0.012 | -0.023 |
| ind_self_15_DKNARefused | 0.002 | -0.023 |
| grewup_size_spouse_17_suburban | 0.34 | -0.023 |
| vacationdays_spouse_17 | 0.971 | -0.023 |
| hourlystatus_self_11_hourlyplustips | 0.003 | -0.023 |
| time_shopping_self_17 | 3.5 | -0.023 |
| grewup_state_self_sd | 0.006 | -0.023 |
| grewup_state_spouse_15_nc | 0.013 | -0.024 |
| grewup_state_spouse_11_or | 0.01 | -0.024 |
| grewup_state_spouse_13_or | 0.01 | -0.024 |
| grewup_state_spouse_19_ks | 0.003 | -0.024 |
| ind_spouse_13_farmfishforest | 0.008 | -0.024 |
| ind_self_15_arts | 0.012 | -0.024 |
| ind_self_13_arts | 0.012 | -0.024 |
| hourlystatus_self_15_hourlyplustips | 0.004 | -0.024 |
| grewup_state_self_co | 0.015 | -0.024 |
| grewup_state_spouse_13_nc | 0.013 | -0.024 |
| grewup_state_spouse_15_or | 0.01 | -0.024 |
| ind_self_11_accomodationsfood | 0.036 | -0.025 |
| grewup_state_self_or | 0.018 | -0.025 |
| grewup_state_spouse_13_nd | 0.001 | -0.025 |
| ind_spouse_11_farmfishforest | 0.008 | -0.025 |
| grewup_state_spouse_11_nd | 0.001 | -0.025 |
| grewup_state_spouse_15_nd | 0.001 | -0.025 |
| grewup_state_spouse_17_nd | 0.001 | -0.025 |
| grewup_state_spouse_13_mo | 0.014 | -0.025 |
| hourlystatus_self_11_other | 0.048 | -0.025 |
| ind_self_13_farmfishforest | 0.013 | -0.025 |
| grewup_state_self_ok | 0.009 | -0.025 |
| time_work_annual_spouse_11 | 1130.6 | -0.025 |
| grewup_state_self_ks | 0.003 | -0.026 |
| hourlystatus_spouse_11_hourly | 0.178 | -0.026 |
| grewup_state_spouse_13_ks | 0.002 | -0.026 |
| ind_spouse_11_wholesale | 0.012 | -0.026 |
| grewup_state_spouse_11_nc | 0.012 | -0.026 |
| grewup_state_spouse_19_nd | 0.002 | -0.026 |
| ind_self_11_retail | 0.052 | -0.026 |
| grewup_state_self_mo | 0.025 | -0.027 |
| grewup_state_self_va | 0.025 | -0.027 |
| hourlystatus_self_17_other | 0.063 | -0.028 |
| grewup_state_self_oh | 0.046 | -0.028 |
| time_leisure_self_17 | 14.5 | -0.028 |
| grewup_size_spouse_11_country | 0.052 | -0.028 |
| ind_self_11_health | 0.092 | -0.028 |
| grewup_size_spouse_17_country | 0.058 | -0.028 |
| grewup_state_spouse_15_ks | 0.003 | -0.029 |
| ind_self_19_otherservices | 0.055 | -0.029 |
| grewup_state_spouse_11_ks | 0.002 | -0.029 |
| grewup_size_spouse_19_country | 0.063 | -0.03 |
| grewup_state_spouse_11_mo | 0.014 | -0.03 |
| ind_self_15_accomodationsfood | 0.041 | -0.03 |
| grewup_state_spouse_17_wa | 0.012 | -0.03 |
| grewup_state_spouse_17_mo | 0.015 | -0.03 |
| ind_self_13_accomodationsfood | 0.039 | -0.03 |
| grewup_size_spouse_15_suburban | 0.296 | -0.031 |
| daycare_13_no | 0.298 | -0.031 |
| ind_self_15_retail | 0.063 | -0.031 |
| ind_spouse_13_manufacturing | 0.051 | -0.031 |
| grewup_state_spouse_13_wa | 0.01 | -0.032 |
| hourlystatus_self_13_hourly | 0.318 | -0.032 |
| grewup_state_spouse_15_mo | 0.015 | -0.032 |
| grewup_state_spouse_15_wa | 0.012 | -0.033 |
| hourlystatus_spouse_13_hourly | 0.186 | -0.033 |
| grewup_size_spouse_11_suburban | 0.26 | -0.033 |
| grewup_size_spouse_13_country | 0.051 | -0.033 |
| grewup_state_spouse_11_wa | 0.009 | -0.033 |
| grewup_size_spouse_13_suburban | 0.273 | -0.033 |
| time_volunteering_self_19 | 0.932 | -0.033 |
| ind_self_13_health | 0.098 | -0.033 |
| hourlystatus_self_15_other | 0.056 | -0.034 |
| hourlystatus_self_11_hourly | 0.293 | -0.034 |
| ind_self_13_education | 0.061 | -0.035 |
| grewup_size_spouse_15_country | 0.053 | -0.036 |
| ind_spouse_11_manufacturing | 0.052 | -0.036 |
| time_adultcare_self_19 | 0.831 | -0.037 |
| ind_self_15_education | 0.064 | -0.037 |
| ind_self_15_health | 0.106 | -0.037 |
| time_housework_self_19 | 10.2 | -0.037 |
| empstat_19_housespouse | 0.021 | -0.037 |
| ind_self_17_education | 0.076 | -0.038 |
| hourlystatus_self_15_hourly | 0.355 | -0.038 |
| ind_self_11_education | 0.055 | -0.038 |
| hourlystatus_self_19_hourlyplustips | 0.008 | -0.039 |
| ind_self_15_farmfishforest | 0.015 | -0.04 |
| grewup_state_self_in | 0.03 | -0.04 |
| grewup_state_spouse_15_ia | 0.015 | -0.041 |
| grewup_state_spouse_19_ia | 0.017 | -0.042 |
| ind_self_19_accomodationsfood | 0.066 | -0.042 |
| hourlystatus_self_17_hourly | 0.436 | -0.043 |
| grewup_state_spouse_13_ia | 0.015 | -0.044 |
| grewup_state_spouse_17_ia | 0.016 | -0.044 |
| grewup_state_self_ia | 0.024 | -0.044 |
| ind_self_13_retail | 0.056 | -0.044 |
| time_housework_self_13 | 10.7 | -0.046 |
| grewup_size_self_country | 0.093 | -0.046 |
| time_shopping_self_19 | 3.6 | -0.046 |
| ind_self_19_education | 0.087 | -0.046 |
| time_housework_self_17 | 10.5 | -0.047 |
| grewup_state_spouse_11_ia | 0.014 | -0.047 |
| grewup_region_spouse_19_northcentral | 0.159 | -0.051 |
| time_housework_self_11 | 10.9 | -0.052 |
| empstat_19_other | 0.0 | nan |
| logcost_transport_bustrain_19 | 0.671 | 0.189 |
| logincome_wagerate_self_19 | 3.0 | 0.156 |
| logcost_transport_bustrain_17 | 0.64 | 0.154 |
| logcost_transport_bustrain_13 | 0.657 | 0.137 |
| logincome_wagerate_self_17 | 2.9 | 0.135 |
| logincome_wagerate_self_15 | 2.8 | 0.132 |
| logcost_transport_bustrain_11 | 0.627 | 0.131 |
| logincome_wagerate_self_13 | 2.8 | 0.13 |
| logincome_wagerate_self_11 | 2.7 | 0.125 |
| logcost_total_19 | 10.8 | 0.125 |
| logcost_housing_19 | 9.9 | 0.124 |
| logcost_total_with_rent_value_19 | 10.9 | 0.119 |
| logcost_transport_bustrain_15 | 0.616 | 0.118 |
| logincome_labor_self_19 | 10.2 | 0.113 |
| logcost_housing_17 | 9.8 | 0.105 |
| logincome_familytotal_19 | 11.2 | 0.099 |
| logincome_labor_self_15 | 9.7 | 0.094 |
| logincome_labor_self_17 | 9.8 | 0.093 |
| logcost_transport_19 | 8.8 | 0.088 |
| logcost_transport_parking_17 | 0.707 | 0.085 |
| logincome_labor_self_11 | 9.4 | 0.083 |
| logcost_transport_parking_15 | 0.649 | 0.08 |
| logincome_labor_self_13 | 9.6 | 0.076 |
| occ_self_19_constructionextraction | 0.049 | 0.075 |
| region_19_northeast | 0.178 | 0.075 |
| logcost_transport_parking_13 | 0.545 | 0.074 |
| logincome_familytotal_17 | 11.2 | 0.074 |
| region_17_northeast | 0.171 | 0.073 |
| sex_spouse_19_female | 0.377 | 0.072 |
| logcost_transport_17 | 8.8 | 0.07 |
| logcost_health_19 | 7.0 | 0.07 |
| state_19_ny | 0.055 | 0.069 |
| logcost_transport_parking_19 | 0.722 | 0.069 |
| grewup_region_self_foreign | 0.161 | 0.067 |
| logincome_familytotal_15 | 11.1 | 0.067 |
| logcost_housing_13 | 9.7 | 0.066 |
| cost_housing_tax_13 | 2055.9 | 0.066 |
| logcost_food_19 | 9.1 | 0.066 |
| logcost_transport_parking_11 | 0.458 | 0.065 |
| cost_housing_mortgage_17 | 5800.9 | 0.065 |
| cost_housing_tax_15 | 2044.8 | 0.065 |
| logcost_childcare_17 | 1.1 | 0.065 |
| occ_self_19_businessfinance | 0.051 | 0.065 |
| cost_housing_15 | 21155.9 | 0.064 |
| state_11_nj | 0.034 | 0.064 |
| cost_housing_telecom_19 | 2883.0 | 0.063 |
| state_17_ny | 0.053 | 0.062 |
| state_17_nj | 0.03 | 0.062 |
| logcost_housing_11 | 9.7 | 0.061 |
| cost_transport_13 | 11152.1 | 0.061 |
| cost_transport_gas_11 | 3185.1 | 0.06 |
| cost_transport_insurance_11 | 1646.9 | 0.06 |
| state_19_nj | 0.032 | 0.06 |
| cost_food_17 | 10066.7 | 0.06 |
| income_familytotal_15 | 96364.1 | 0.06 |
| cost_transport_insurance_19 | 2035.1 | 0.06 |
| cost_transport_parking_15 | 76.7 | 0.059 |
| cost_housing_tax_11 | 2047.2 | 0.059 |
| logcost_housing_telecom_19 | 7.7 | 0.058 |
| occ_self_17_constructionextraction | 0.042 | 0.058 |
| state_15_nj | 0.032 | 0.057 |
| sex_spouse_17_female | 0.339 | 0.056 |
| cost_housing_insurance_11 | 659.7 | 0.056 |
| logincome_familytotal_13 | 11.1 | 0.056 |
| occ_self_15_constructionextraction | 0.035 | 0.056 |
| cost_housing_telecom_17 | 2824.6 | 0.056 |
| logcost_transport_taxi_17 | 0.688 | 0.056 |
| cost_transport_parking_11 | 48.4 | 0.055 |
| cost_transport_parking_13 | 66.9 | 0.055 |
| state_11_fl | 0.042 | 0.054 |
| logcost_transport_11 | 8.8 | 0.054 |
| cost_transport_insurance_17 | 1987.2 | 0.053 |
| income_familytotal_13 | 92452.5 | 0.053 |
| cost_transport_insurance_15 | 1780.6 | 0.053 |
| region_11_northeast | 0.165 | 0.053 |
| educyrs_19 | 13.9 | 0.052 |
| occ_self_11_businessfinance | 0.029 | 0.052 |
| state_13_nj | 0.033 | 0.052 |
| cost_transport_15 | 10836.7 | 0.052 |
| logcost_transport_repair_19 | 5.1 | 0.052 |
| religion_self_17_jewish | 0.017 | 0.051 |
| cost_housing_mortgage_13 | 6558.7 | 0.051 |
| state_19_ca | 0.119 | 0.051 |
| state_17_ca | 0.112 | 0.051 |
| state_19_ma | 0.029 | 0.051 |
| logcost_health_insurance_19 | 5.4 | 0.051 |
| logcost_education_13 | 2.7 | 0.051 |
| cost_trips_17 | 2173.4 | 0.05 |
| logcost_housing_mortgage_19 | 4.4 | 0.05 |
| income_familytotal_11 | 86075.0 | 0.05 |
| cost_food_athome_17 | 6940.8 | 0.05 |
| occ_self_13_constructionextraction | 0.031 | 0.05 |
| cost_food_athome_19 | 7318.7 | 0.05 |
| logcost_transport_taxi_19 | 0.805 | 0.05 |
| logcost_transport_other_19 | 0.246 | 0.049 |
| cost_housing_mortgage_11 | 7280.8 | 0.049 |
| region_15_northeast | 0.161 | 0.049 |
| region_13_northeast | 0.163 | 0.049 |
| logcost_housing_15 | 9.7 | 0.049 |
| cost_housing_utility_17 | 2899.7 | 0.049 |
| state_17_ma | 0.027 | 0.048 |
| cost_transport_parking_17 | 81.6 | 0.047 |
| logcost_transport_13 | 8.7 | 0.047 |
| cost_transport_parking_19 | 99.9 | 0.047 |
| cost_housing_telecom_15 | 2789.5 | 0.047 |
| sex_male | 0.507 | 0.047 |
| sex_self_19_male | 0.507 | 0.047 |
| cost_housing_rent_11 | 2963.8 | 0.047 |
| cost_housing_insurance_15 | 666.7 | 0.046 |
| cost_health_insurance_19 | 2786.1 | 0.046 |
| logcost_transport_15 | 8.8 | 0.046 |
| occ_self_13_architectengineering | 0.014 | 0.046 |
| logcost_clothing_19 | 6.4 | 0.046 |
| occ_self_17_architectengineering | 0.017 | 0.046 |
| cost_childcare_19 | 738.5 | 0.045 |
| occ_self_15_businessfinance | 0.033 | 0.045 |
| state_17_md | 0.015 | 0.045 |
| state_19_md | 0.017 | 0.044 |
| cost_food_deliver_15 | 124.9 | 0.044 |
| religion_self_15_jewish | 0.017 | 0.043 |
| logcost_food_athome_17 | 8.5 | 0.043 |
| cost_housing_rent_13 | 3230.0 | 0.043 |
| cost_food_deliver_19 | 199.8 | 0.043 |
| logcost_food_athome_19 | 8.6 | 0.043 |
| cost_housing_11 | 21858.0 | 0.042 |
| cost_trips_13 | 1961.5 | 0.042 |
| cost_food_15 | 9179.2 | 0.042 |
| occ_self_15_compscimath | 0.019 | 0.042 |
| logcost_food_17 | 9.0 | 0.042 |
| ind_spouse_19_financeinsurance | 0.03 | 0.042 |
| wealth_homeequity_17 | 93875.5 | 0.042 |
| state_15_hi | 0.0 | 0.041 |
| logcost_housing_tax_19 | 4.7 | 0.041 |
| logcost_education_11 | 2.8 | 0.041 |
| cost_food_away_15 | 2717.0 | 0.041 |
| sex_spouse_15_female | 0.289 | 0.041 |
| cost_computing_17 | 542.0 | 0.041 |
| cost_education_17 | 2341.3 | 0.041 |
| occ_spouse_19_healthcaresupport | 0.014 | 0.041 |
| ishd_11 | 0.438 | 0.04 |
| cost_food_away_17 | 2982.0 | 0.04 |
| cost_food_deliver_17 | 144.0 | 0.04 |
| ishd_19 | 0.683 | 0.04 |
| religion_spouse_17_catholic | 0.171 | 0.04 |
| occ_self_17_businessfinance | 0.042 | 0.04 |
| cost_housing_utility_19 | 3026.0 | 0.04 |
| cost_clothing_19 | 1496.5 | 0.04 |
| state_15_ma | 0.025 | 0.04 |
| logcost_transport_gas_19 | 6.9 | 0.04 |
| cost_recreation_17 | 1027.8 | 0.039 |
| logcost_clothing_17 | 6.4 | 0.039 |
| logincome_familytotal_11 | 11.0 | 0.039 |
| cost_housing_furnishing_17 | 1140.8 | 0.039 |
| cost_transport_taxi_19 | 129.7 | 0.039 |
| occ_self_13_compscimath | 0.018 | 0.039 |
| state_13_fl | 0.046 | 0.039 |
| cost_transport_repair_13 | 1843.8 | 0.039 |
| cost_clothing_17 | 1496.7 | 0.039 |
| state_19_ga | 0.025 | 0.039 |
| sex_self_15_male | 0.38 | 0.039 |
| logcost_housing_mortgage_17 | 4.4 | 0.039 |
| cost_childcare_13 | 648.1 | 0.039 |
| state_11_ma | 0.026 | 0.038 |
| cost_education_19 | 1895.3 | 0.038 |
| occ_self_11_constructionextraction | 0.026 | 0.038 |
| occ_self_15_architectengineering | 0.015 | 0.038 |
| logcost_housing_telecom_17 | 7.7 | 0.038 |
| logcost_housing_repairs_19 | 4.0 | 0.038 |
| cost_transport_loans_19 | 1803.5 | 0.038 |
| state_15_md | 0.015 | 0.038 |
| state_15_ca | 0.101 | 0.037 |
| logcost_trips_17 | 5.5 | 0.037 |
| state_11_md | 0.016 | 0.037 |
| state_13_ny | 0.05 | 0.037 |
| logincome_wagerate_spouse_19 | 1.8 | 0.037 |
| cost_health_19 | 4660.4 | 0.037 |
| race_spouse_11_pacis | 0.002 | 0.037 |
| state_17_ga | 0.025 | 0.037 |
| cost_housing_rent_17 | 4227.3 | 0.037 |
| empstat_current_self_19_working | 0.872 | 0.037 |
| logcost_transport_taxi_15 | 0.36 | 0.037 |
| race_spouse_13_pacis | 0.002 | 0.037 |
| religion_spouse_17_jewish | 0.013 | 0.036 |
| cost_housing_telecom_13 | 2693.7 | 0.036 |
| cost_housing_mortgage_15 | 6049.0 | 0.036 |
| logcost_housing_telecom_13 | 7.6 | 0.036 |
| cost_housing_telecom_11 | 2506.8 | 0.036 |
| cost_housing_utility_15 | 3016.4 | 0.036 |
| religion_self_11_jewish | 0.015 | 0.036 |
| cost_education_13 | 2970.8 | 0.036 |
| race_self_13_pacis | 0.002 | 0.036 |
| occ_self_19_architectengineering | 0.02 | 0.036 |
| logcost_education_17 | 2.2 | 0.036 |
| occ_self_11_compscimath | 0.017 | 0.036 |
| time_work_prevyear_sp_19 | 22.5 | 0.036 |
| logcost_transport_gas_17 | 6.9 | 0.036 |
| race_self_11_pacis | 0.002 | 0.036 |
| state_13_ca | 0.097 | 0.036 |
| cost_childcare_15 | 617.1 | 0.036 |
| wealth_homeequity_15 | 85890.2 | 0.035 |
| logcost_health_hospital_17 | 1.6 | 0.035 |
| sex_self_17_male | 0.451 | 0.035 |
| logcost_health_rx_19 | 3.8 | 0.035 |
| state_13_ma | 0.025 | 0.035 |
| state_13_ga | 0.019 | 0.035 |
| grewup_region_spouse_15_foreign | 0.069 | 0.035 |
| occ_self_13_businessfinance | 0.031 | 0.035 |
| grewup_region_spouse_11_foreign | 0.065 | 0.034 |
| occ_self_19_compscimath | 0.027 | 0.034 |
| state_15_fl | 0.047 | 0.034 |
| ind_spouse_19_education | 0.062 | 0.034 |
| logcost_health_rx_17 | 3.8 | 0.034 |
| logcost_education_15 | 2.4 | 0.034 |
| wealth_homeequity_19 | 106430.2 | 0.034 |
| logcost_food_deliver_17 | 0.644 | 0.034 |
| religion_self_13_jewish | 0.016 | 0.033 |
| cost_housing_rent_15 | 3514.2 | 0.033 |
| logcost_trips_19 | 5.5 | 0.033 |
| weight_indiv_cs_17 | 19997.4 | 0.033 |
| logcost_trips_13 | 5.2 | 0.033 |
| grewup_region_spouse_11_northeast | 0.096 | 0.033 |
| state_13_md | 0.015 | 0.033 |
| state_11_ca | 0.1 | 0.033 |
| state_15_ny | 0.05 | 0.033 |
| race_self_17_asian | 0.059 | 0.033 |
| occ_self_11_management | 0.056 | 0.033 |
| cost_food_13 | 8721.9 | 0.032 |
| logcost_health_doctor_19 | 4.4 | 0.032 |
| logincome_labor_spouse_19 | 5.8 | 0.032 |
| cost_transport_insurance_13 | 1784.6 | 0.032 |
| logcost_childcare_19 | 1.0 | 0.032 |
| logcost_food_deliver_15 | 0.658 | 0.032 |
| religion_spouse_15_catholic | 0.15 | 0.032 |
| cost_transport_taxi_17 | 87.6 | 0.032 |
| cost_housing_insurance_17 | 706.6 | 0.032 |
| logcost_health_insurance_17 | 5.5 | 0.032 |
| ind_spouse_17_health | 0.08 | 0.031 |
| logcost_food_deliver_19 | 0.735 | 0.031 |
| grewup_region_spouse_13_foreign | 0.066 | 0.031 |
| logcost_transport_loans_19 | 2.6 | 0.031 |
| occ_self_11_architectengineering | 0.011 | 0.031 |
| ishd_17 | 0.604 | 0.031 |
| logcost_housing_insurance_19 | 4.1 | 0.031 |
| state_11_ny | 0.05 | 0.031 |
| cost_childcare_11 | 608.3 | 0.031 |
| logwealth_15 | 11.0 | 0.031 |
| ishd_13 | 0.471 | 0.031 |
| occ_spouse_19_sales | 0.048 | 0.031 |
| cost_food_away_13 | 2510.0 | 0.031 |
| grewup_region_self_northeast | 0.177 | 0.031 |
| logwealth_homeequity_19 | 7.0 | 0.03 |
| logcost_transport_additionalvehicle_19 | 2.5 | 0.03 |
| logcost_transport_repair_17 | 5.3 | 0.03 |
| empstat_current_spouse_17_housespouse | 0.076 | 0.03 |
| state_15_ga | 0.02 | 0.03 |
| kids_youngest_19 | 7.6 | 0.03 |
| logcost_health_doctor_11 | 4.5 | 0.03 |
| logcost_transport_additionalvehicle_11 | 2.5 | 0.03 |
| logcost_transport_repair_11 | 3.6 | 0.03 |
| cost_housing_utility_11 | 3049.7 | 0.029 |
| cost_food_11 | 8452.0 | 0.029 |
| logcost_computing_17 | 3.9 | 0.029 |
| grewup_region_spouse_13_northeast | 0.099 | 0.029 |
| religion_spouse_15_jewish | 0.013 | 0.029 |
| logincome_wagerate_spouse_15 | 1.8 | 0.029 |
| race_self_15_asian | 0.033 | 0.029 |
| logcost_childcare_11 | 1.0 | 0.029 |
| cost_education_11 | 2720.6 | 0.029 |
| cost_transport_additionalvehicle_11 | 1601.7 | 0.029 |
| hh_size_17 | 2.9 | 0.029 |
| empstat_current_spouse_19_working | 0.508 | 0.028 |
| occ_spouse_15_education | 0.037 | 0.028 |
| religion_spouse_13_catholic | 0.142 | 0.028 |
| race_self_19_asian | 0.067 | 0.028 |
| logcost_health_insurance_11 | 4.9 | 0.028 |
| ind_spouse_15_financeinsurance | 0.025 | 0.028 |
| ind_spouse_15_education | 0.05 | 0.028 |
| logcost_transport_repair_13 | 3.5 | 0.028 |
| religion_spouse_11_catholic | 0.14 | 0.028 |
| occ_self_17_compscimath | 0.024 | 0.028 |
| cost_transport_additionalvehicle_17 | 1454.3 | 0.028 |
| occ_spouse_19_arts | 0.015 | 0.027 |
| logcost_health_17 | 7.0 | 0.027 |
| logcost_food_15 | 8.9 | 0.027 |
| state_11_ga | 0.02 | 0.027 |
| logcost_housing_mortgage_15 | 4.6 | 0.027 |
| cost_food_athome_11 | 5953.9 | 0.027 |
| logcost_housing_tax_17 | 4.6 | 0.027 |
| race_spouse_19_asian | 0.051 | 0.027 |
| occ_self_17_hardscience | 0.012 | 0.027 |
| logcost_housing_rent_13 | 3.0 | 0.027 |
| logcost_childcare_15 | 0.975 | 0.027 |
| ishd_15 | 0.513 | 0.027 |
| cost_health_bills_17 | 890.2 | 0.027 |
| hh_size_19 | 2.8 | 0.027 |
| ind_spouse_17_education | 0.056 | 0.027 |
| religion_self_17_catholic | 0.231 | 0.027 |
| ind_spouse_17_financeinsurance | 0.027 | 0.026 |
| moved_why_11_consneighbor | 0.02 | 0.026 |
| logcost_transport_leases_17 | 0.721 | 0.026 |
| logwealth_other_15 | 10.2 | 0.026 |
| logcost_health_11 | 6.7 | 0.026 |
| occ_spouse_17_arts | 0.014 | 0.026 |
| union_spouse_19_yes | 0.069 | 0.026 |
| logcost_housing_furnishing_15 | 4.5 | 0.026 |
| cost_housing_rent_19 | 4625.1 | 0.026 |
| cost_education_15 | 3016.8 | 0.026 |
| cost_trips_15 | 2155.1 | 0.026 |
| logcost_food_deliver_11 | 0.711 | 0.026 |
| cost_food_deliver_13 | 126.3 | 0.026 |
| weight_indiv_cs_19 | 24037.8 | 0.026 |
| cost_housing_repairs_13 | 1845.9 | 0.026 |
| occ_spouse_13_arts | 0.01 | 0.025 |
| ind_spouse_17_realestate | 0.01 | 0.025 |
| logcost_health_rx_11 | 4.1 | 0.025 |
| cost_transport_other_19 | 56.0 | 0.025 |
| religion_self_19_none | 0.0 | 0.025 |
| logcost_health_15 | 7.0 | 0.025 |
| empstat_current_spouse_19_housespouse | 0.087 | 0.025 |
| race_spouse_17_other | 0.039 | 0.025 |
| logincome_labor_spouse_15 | 5.9 | 0.025 |
| time_work_prevyear_sp_17 | 21.3 | 0.025 |
| logwealth_other_11 | 10.1 | 0.025 |
| cost_food_athome_15 | 6337.3 | 0.025 |
| cost_transport_repair_11 | 1823.3 | 0.025 |
| own_or_rent_19_own | 0.615 | 0.025 |
| logcost_education_19 | 1.9 | 0.025 |
| empstat_current_self_17_working | 0.785 | 0.025 |
| logcost_health_insurance_15 | 5.5 | 0.024 |
| cost_transport_additionalvehicle_15 | 1284.2 | 0.024 |
| occ_spouse_17_sales | 0.047 | 0.024 |
| occ_spouse_13_education | 0.034 | 0.024 |
| educyrs_17 | 12.8 | 0.024 |
| logcost_computing_19 | 3.6 | 0.024 |
| ind_spouse_19_realestate | 0.01 | 0.024 |
| logcost_housing_telecom_11 | 7.5 | 0.024 |
| occ_spouse_17_healthcareprac | 0.026 | 0.024 |
| id68 | 2281088.1 | 0.024 |
| occ_spouse_15_compscimath | 0.011 | 0.024 |
| race_spouse_17_asian | 0.046 | 0.024 |
| logwealth_19 | 11.1 | 0.024 |
| logcost_health_doctor_13 | 4.6 | 0.024 |
| kids_youngest_17 | 7.4 | 0.024 |
| race_spouse_19_other | 0.045 | 0.024 |
| moved_17_yes | 0.312 | 0.023 |
| Unnamed: 0 | 13479.8 | 0.023 |
| state_17_il | 0.024 | 0.023 |
| logincome_wagerate_spouse_17 | 1.8 | 0.023 |
| religion_spouse_13_jewish | 0.012 | 0.023 |
| religion_spouse_11_jewish | 0.013 | 0.023 |
| logcost_food_athome_15 | 8.4 | 0.023 |
| cost_recreation_19 | 979.1 | 0.023 |
| logcost_transport_other_15 | 0.352 | 0.023 |
| cost_transport_additionalvehicle_19 | 1696.2 | 0.023 |
| logcost_recreation_19 | 5.2 | 0.023 |
| cost_housing_utility_13 | 3023.6 | 0.023 |
| occ_spouse_17_healthcaresupport | 0.016 | 0.023 |
| logcost_housing_mortgage_11 | 5.0 | 0.023 |
| logcost_housing_rent_11 | 2.8 | 0.023 |
| race_spouse_15_asian | 0.027 | 0.023 |
| logcost_transport_taxi_11 | 0.251 | 0.023 |
| logcost_childcare_13 | 1.1 | 0.023 |
| occ_spouse_19_pcareservice | 0.018 | 0.023 |
| cost_transport_downpayment_11 | 1034.3 | 0.023 |
| cost_transport_other_11 | 88.9 | 0.023 |
| logcost_transport_gas_13 | 7.2 | 0.022 |
| state_17_fl | 0.058 | 0.022 |
| cost_housing_insurance_13 | 654.1 | 0.022 |
| state_15_ut | 0.009 | 0.022 |
| occ_spouse_17_hardscience | 0.007 | 0.022 |
| occ_spouse_13_compscimath | 0.01 | 0.022 |
| empstat_current_spouse_11_housespouse | 0.06 | 0.022 |
| cost_recreation_15 | 1000.5 | 0.022 |
| state_19_il | 0.024 | 0.022 |
| state_13_ut | 0.008 | 0.022 |
| cost_transport_loans_11 | 1310.7 | 0.021 |
| logcost_transport_downpayment_15 | 1.8 | 0.021 |
| logcost_transport_leases_15 | 0.656 | 0.021 |
| logcost_food_away_19 | 7.3 | 0.021 |
| logcost_transport_other_11 | 0.256 | 0.021 |
| logcost_health_insurance_13 | 5.1 | 0.021 |
| empstat_current_spouse_13_student | 0.007 | 0.021 |
| religion_spouse_15_orthodox | 0.001 | 0.021 |
| logcost_transport_insurance_11 | 6.6 | 0.021 |
| cost_health_17 | 4345.1 | 0.021 |
| time_work_prevyear_sp_13 | 20.9 | 0.021 |
| interview_number_11 | 3831.9 | 0.021 |
| union_self_17_no | 0.616 | 0.021 |
| religion_spouse_13_orthodox | 0.001 | 0.02 |
| occ_self_15_hardscience | 0.012 | 0.02 |
| occ_spouse_19_janitors | 0.025 | 0.02 |
| occ_spouse_11_businessfinance | 0.02 | 0.02 |
| cost_health_doctor_13 | 919.2 | 0.02 |
| religion_self_11_catholic | 0.183 | 0.02 |
| logcost_housing_utility_11 | 7.4 | 0.02 |
| logcost_food_away_15 | 7.1 | 0.02 |
| occ_spouse_19_compscimath | 0.017 | 0.02 |
| state_11_ut | 0.01 | 0.02 |
| logcost_transport_additionalvehicle_15 | 2.1 | 0.02 |
| state_15_il | 0.023 | 0.02 |
| ind_spouse_15_otherservices | 0.023 | 0.02 |
| occ_spouse_19_education | 0.043 | 0.02 |
| race_self_11_asian | 0.026 | 0.019 |
| state_19_fl | 0.062 | 0.019 |
| occ_spouse_13_healthcaresupport | 0.01 | 0.019 |
| moved_why_17_involuntary | 0.042 | 0.019 |
| logcost_health_doctor_15 | 4.4 | 0.019 |
| cost_housing_repairs_19 | 2107.5 | 0.019 |
| moved_why_17_consmore | 0.052 | 0.019 |
| logcost_transport_other_13 | 0.29 | 0.019 |
| kids_youngest_11 | 8.0 | 0.019 |
| race_self_17_other | 0.051 | 0.019 |
| occ_spouse_17_pcareservice | 0.017 | 0.019 |
| cost_transport_taxi_15 | 44.6 | 0.019 |
| union_self_13_yes | 0.084 | 0.019 |
| empstat_current_spouse_11_student | 0.008 | 0.019 |
| logcost_transport_gas_15 | 7.0 | 0.019 |
| occ_self_19_janitors | 0.047 | 0.019 |
| occ_self_19_repair | 0.033 | 0.019 |
| race_spouse_11_other | 0.023 | 0.019 |
| logcost_housing_telecom_15 | 7.6 | 0.018 |
| logwealth_11 | 10.8 | 0.018 |
| state_13_il | 0.023 | 0.018 |
| occ_spouse_17_education | 0.04 | 0.018 |
| state_11_il | 0.025 | 0.018 |
| cost_health_doctor_19 | 952.4 | 0.018 |
| cost_computing_19 | 563.8 | 0.018 |
| ind_spouse_15_health | 0.065 | 0.018 |
| logcost_health_doctor_17 | 4.3 | 0.018 |
| race_self_13_asian | 0.027 | 0.017 |
| cost_housing_furnishing_15 | 1198.1 | 0.017 |
| ind_spouse_17_arts | 0.009 | 0.017 |
| time_work_prevyear_sp_15 | 20.8 | 0.017 |
| union_self_17_yes | 0.106 | 0.017 |
| region_17_west | 0.217 | 0.017 |
| cost_food_athome_13 | 6085.5 | 0.017 |
| logcost_transport_other_17 | 0.297 | 0.017 |
| logcost_housing_mortgage_13 | 4.8 | 0.017 |
| moved_19_no | 0.698 | 0.017 |
| cost_health_rx_19 | 385.9 | 0.017 |
| race_spouse_11_asian | 0.021 | 0.017 |
| logcost_housing_tax_15 | 4.8 | 0.017 |
| logcost_transport_loans_15 | 2.7 | 0.017 |
| religion_spouse_19_orthodox | 0.015 | 0.017 |
| religion_self_13_catholic | 0.187 | 0.017 |
| cost_food_away_11 | 2379.2 | 0.017 |
| logcost_housing_repairs_13 | 4.1 | 0.017 |
| logincome_labor_spouse_17 | 5.9 | 0.017 |
| cost_transport_loans_13 | 1499.9 | 0.017 |
| logcost_transport_downpayment_11 | 1.7 | 0.016 |
| occ_self_11_legal | 0.009 | 0.016 |
| occ_spouse_11_healthcareprac | 0.022 | 0.016 |
| religion_self_15_catholic | 0.201 | 0.016 |
| cost_health_insurance_17 | 2659.7 | 0.016 |
| cost_transport_other_13 | 100.7 | 0.016 |
| logcost_housing_repairs_17 | 4.0 | 0.016 |
| logcost_trips_15 | 5.4 | 0.016 |
| logcost_housing_insurance_17 | 4.1 | 0.016 |
| religion_spouse_17_orthodox | 0.003 | 0.016 |
| logwealth_other_17 | 10.3 | 0.016 |
| logcost_recreation_15 | 5.4 | 0.016 |
| moved_why_17_consother | 0.091 | 0.015 |
| logwealth_17 | 11.0 | 0.015 |
| union_self_19_yes | 0.125 | 0.015 |
| occ_spouse_19_softscience | 0.015 | 0.015 |
| occ_spouse_19_hardscience | 0.008 | 0.015 |
| logcost_housing_furnishing_19 | 4.4 | 0.015 |
| region_19_west | 0.229 | 0.015 |
| logcost_housing_utility_15 | 7.4 | 0.015 |
| logcost_transport_additionalvehicle_17 | 2.2 | 0.015 |
| cost_transport_leases_17 | 478.8 | 0.015 |
| occ_spouse_19_healthcareprac | 0.032 | 0.015 |
| mightmove_19_yes | 0.324 | 0.015 |
| cost_health_hospital_17 | 422.3 | 0.015 |
| moved_why_15_productive | 0.022 | 0.015 |
| logcost_transport_insurance_15 | 6.7 | 0.015 |
| occ_self_19_legal | 0.011 | 0.015 |
| logcost_transport_leases_11 | 0.319 | 0.015 |
| race_spouse_13_other | 0.024 | 0.015 |
| cost_transport_loans_15 | 1729.7 | 0.014 |
| religion_self_19_catholic | 0.176 | 0.014 |
| race_spouse_19_black | 0.055 | 0.014 |
| occ_spouse_13_janitors | 0.013 | 0.014 |
| empstat_current_self_19_laid off | 0.005 | 0.014 |
| state_17_hi | 0.0 | 0.014 |
| union_self_15_yes | 0.092 | 0.014 |
| logwealth_homeequity_15 | 6.9 | 0.014 |
| race_self_13_black | 0.08 | 0.014 |
| logincome_wagerate_spouse_13 | 1.8 | 0.014 |
| race_self_11_black | 0.072 | 0.014 |
| occ_self_15_legal | 0.011 | 0.014 |
| cost_transport_other_17 | 53.9 | 0.014 |
| ind_spouse_19_health | 0.091 | 0.014 |
| ind_spouse_19_profsciencetech | 0.039 | 0.014 |
| occ_self_19_hardscience | 0.014 | 0.014 |
| logcost_transport_insurance_19 | 6.9 | 0.014 |
| logcost_transport_taxi_13 | 0.312 | 0.014 |
| logwealth_other_19 | 10.3 | 0.014 |
| logcost_recreation_17 | 5.3 | 0.014 |
| cost_food_deliver_11 | 118.9 | 0.013 |
| occ_spouse_15_arts | 0.011 | 0.013 |
| own_or_rent_11_rent | 0.278 | 0.013 |
| logwealth_homeequity_17 | 6.9 | 0.013 |
| ind_spouse_19_information | 0.011 | 0.013 |
| occ_spouse_15_healthcareprac | 0.023 | 0.013 |
| occ_spouse_11_janitors | 0.014 | 0.013 |
| cost_housing_repairs_17 | 2189.2 | 0.013 |
| logcost_food_away_17 | 7.2 | 0.013 |
| occ_spouse_11_DKNARefused | 0.002 | 0.013 |
| race_self_15_black | 0.086 | 0.013 |
| union_spouse_13_yes | 0.051 | 0.013 |
| ind_spouse_15_realestate | 0.007 | 0.013 |
| own_or_rent_13_rent | 0.29 | 0.013 |
| ind_spouse_19_adminmilitary | 0.034 | 0.013 |
| mightmove_15_yes | 0.3 | 0.013 |
| cost_health_rx_17 | 376.8 | 0.013 |
| occ_self_17_softscience | 0.015 | 0.013 |
| race_self_19_other | 0.061 | 0.013 |
| region_11_south | 0.307 | 0.013 |
| logcost_housing_tax_11 | 4.9 | 0.013 |
| logcost_food_athome_13 | 8.3 | 0.013 |
| cost_transport_taxi_13 | 37.7 | 0.012 |
| occ_self_19_arts | 0.021 | 0.012 |
| union_spouse_17_yes | 0.06 | 0.012 |
| state_19_ut | 0.009 | 0.012 |
| moved_why_17_mixed | 0.02 | 0.012 |
| logcost_transport_loans_17 | 3.0 | 0.012 |
| logcost_health_rx_15 | 4.0 | 0.012 |
| moved_why_13_closertowork | 0.015 | 0.012 |
| occ_self_13_legal | 0.01 | 0.012 |
| cost_recreation_11 | 870.1 | 0.012 |
| union_spouse_11_yes | 0.052 | 0.012 |
| logcost_food_athome_11 | 8.3 | 0.012 |
| occ_spouse_17_softscience | 0.012 | 0.012 |
| region_19_south | 0.366 | 0.012 |
| occ_spouse_15_sales | 0.055 | 0.012 |
| union_spouse_19_no | 0.397 | 0.012 |
| religion_spouse_19_other | 0.001 | 0.012 |
| cost_health_doctor_15 | 922.0 | 0.012 |
| moved_why_19_productive | 0.02 | 0.011 |
| cost_transport_leases_19 | 490.6 | 0.011 |
| logcost_health_13 | 7.0 | 0.011 |
| logcost_housing_utility_19 | 7.4 | 0.011 |
| state_15_mn | 0.01 | 0.011 |
| wealth_homeequity_13 | 72989.6 | 0.011 |
| logincome_labor_spouse_13 | 6.0 | 0.011 |
| union_spouse_15_yes | 0.055 | 0.011 |
| cost_housing_furnishing_19 | 1111.2 | 0.011 |
| kids_num_19 | 0.78 | 0.011 |
| occ_self_19_protective | 0.023 | 0.011 |
| moved_why_19_consmore | 0.047 | 0.011 |
| occ_self_13_hardscience | 0.01 | 0.011 |
| occ_self_17_protective | 0.021 | 0.011 |
| cost_transport_taxi_11 | 32.7 | 0.011 |
| union_self_11_yes | 0.084 | 0.011 |
| occ_spouse_15_healthcaresupport | 0.011 | 0.01 |
| union_self_19_no | 0.695 | 0.01 |
| logcost_housing_utility_13 | 7.4 | 0.01 |
| cost_housing_furnishing_13 | 1030.8 | 0.01 |
| occ_self_13_production | 0.044 | 0.01 |
| occ_spouse_13_food | 0.012 | 0.01 |
| logcost_transport_loans_13 | 2.5 | 0.01 |
| logcost_food_13 | 8.8 | 0.01 |
| race_spouse_15_pacis | 0.001 | 0.01 |
| occ_self_13_management | 0.064 | 0.01 |
| religion_spouse_11_orthodox | 0.001 | 0.01 |
| cost_health_doctor_17 | 886.3 | 0.01 |
| logcost_transport_leases_19 | 0.716 | 0.01 |
| race_spouse_15_black | 0.038 | 0.01 |
| ind_spouse_19_arts | 0.011 | 0.01 |
| region_13_west | 0.194 | 0.01 |
| empstat_current_spouse_15_housespouse | 0.066 | 0.01 |
| region_11_west | 0.196 | 0.01 |
| race_self_19_black | 0.115 | 0.01 |
| occ_self_11_hardscience | 0.009 | 0.01 |
| region_13_south | 0.311 | 0.01 |
| race_self_13_other | 0.031 | 0.01 |
| cost_transport_downpayment_17 | 1487.6 | 0.01 |
| cost_transport_loans_17 | 1887.1 | 0.01 |
| region_17_south | 0.35 | 0.009 |
| cost_transport_leases_15 | 440.9 | 0.009 |
| occ_spouse_19_businessfinance | 0.029 | 0.009 |
| race_spouse_13_asian | 0.022 | 0.009 |
| occ_self_15_management | 0.066 | 0.009 |
| moved_why_13_consneighbor | 0.024 | 0.009 |
| occ_spouse_13_healthcareprac | 0.022 | 0.009 |
| state_17_ut | 0.009 | 0.009 |
| religion_spouse_19_catholic | 0.109 | 0.009 |
| cost_transport_repair_15 | 1366.5 | 0.009 |
| race_self_11_other | 0.028 | 0.009 |
| occ_spouse_11_arts | 0.01 | 0.009 |
| race_spouse_15_other | 0.027 | 0.009 |
| state_15_ms | 0.01 | 0.009 |
| moved_why_11_closertowork | 0.016 | 0.009 |
| region_15_south | 0.314 | 0.009 |
| grewup_region_spouse_13_akhi | 0.002 | 0.009 |
| empstat_current_spouse_17_working | 0.461 | 0.009 |
| occ_self_11_healthcareprac | 0.033 | 0.009 |
| race_self_15_other | 0.033 | 0.009 |
| religion_self_13_orthodox | 0.001 | 0.009 |
| state_15_wy | 0.002 | 0.009 |
| occ_spouse_11_healthcaresupport | 0.008 | 0.008 |
| state_13_mn | 0.01 | 0.008 |
| logcost_transport_downpayment_19 | 1.7 | 0.008 |
| union_self_11_no | 0.431 | 0.008 |
| cost_health_bills_19 | 1049.0 | 0.008 |
| relation_to_head_17 | 14.1 | 0.008 |
| logcost_transport_gas_11 | 7.3 | 0.008 |
| kids_num_17 | 0.813 | 0.008 |
| race_self_17_black | 0.102 | 0.008 |
| grewup_region_spouse_15_akhi | 0.002 | 0.008 |
| religion_self_15_nonchristian | 0.015 | 0.008 |
| occ_self_17_arts | 0.018 | 0.008 |
| mightmove_17_yes | 0.321 | 0.008 |
| state_19_hi | 0.001 | 0.008 |
| logcost_transport_insurance_13 | 6.7 | 0.008 |
| ind_spouse_17_information | 0.01 | 0.008 |
| occ_spouse_15_hardscience | 0.008 | 0.008 |
| union_self_15_no | 0.523 | 0.008 |
| ind_spouse_15_information | 0.01 | 0.008 |
| empstat_current_spouse_15_laid off | 0.002 | 0.007 |
| occ_self_15_healthcareprac | 0.036 | 0.007 |
| ind_spouse_19_management | 0.022 | 0.007 |
| logcost_health_hospital_19 | 1.6 | 0.007 |
| religion_self_15_orthodox | 0.002 | 0.007 |
| occ_spouse_19_legal | 0.006 | 0.007 |
| race_spouse_13_black | 0.038 | 0.007 |
| empstat_current_spouse_13_housespouse | 0.059 | 0.007 |
| logwealth_other_13 | 10.1 | 0.007 |
| state_11_ms | 0.01 | 0.007 |
| moved_why_13_mixed | 0.019 | 0.007 |
| logcost_recreation_11 | 5.3 | 0.007 |
| ind_spouse_17_profsciencetech | 0.034 | 0.007 |
| religion_self_19_jewish | 0.023 | 0.007 |
| moved_why_19_closertowork | 0.024 | 0.007 |
| state_11_tn | 0.02 | 0.007 |
| ind_spouse_15_arts | 0.008 | 0.007 |
| state_11_de | 0.0 | 0.007 |
| state_15_vt | 0.001 | 0.007 |
| state_13_ms | 0.011 | 0.007 |
| state_11_wa | 0.02 | 0.007 |
| union_spouse_17_no | 0.358 | 0.007 |
| occ_spouse_11_sales | 0.054 | 0.007 |
| ind_spouse_19_wholesale | 0.018 | 0.007 |
| state_13_tn | 0.02 | 0.006 |
| occ_self_15_repair | 0.027 | 0.006 |
| cost_health_doctor_11 | 686.1 | 0.006 |
| occ_spouse_13_businessfinance | 0.019 | 0.006 |
| occ_self_19_softscience | 0.019 | 0.006 |
| occ_self_15_production | 0.046 | 0.006 |
| region_15_west | 0.201 | 0.006 |
| logcost_housing_insurance_15 | 4.1 | 0.006 |
| race_spouse_17_black | 0.048 | 0.006 |
| moved_why_19_homeless | 0.002 | 0.006 |
| logcost_housing_repairs_15 | 4.2 | 0.006 |
| own_or_rent_17_rent | 0.342 | 0.006 |
| state_15_wv | 0.002 | 0.006 |
| interview_number_13 | 4013.7 | 0.006 |
| state_17_wv | 0.001 | 0.006 |
| empstat_current_spouse_17_laid off | 0.002 | 0.006 |
| state_15_tn | 0.022 | 0.006 |
| occ_self_11_production | 0.04 | 0.006 |
| occ_spouse_11_education | 0.031 | 0.005 |
| weight_indiv_cs_11 | 16001.1 | 0.005 |
| cost_clothing_15 | 1692.8 | 0.005 |
| state_13_de | 0.001 | 0.005 |
| state_15_de | 0.001 | 0.005 |
| state_17_de | 0.001 | 0.005 |
| occ_self_17_legal | 0.011 | 0.005 |
| state_17_wy | 0.002 | 0.005 |
| grewup_region_spouse_11_akhi | 0.002 | 0.005 |
| state_19_al | 0.009 | 0.005 |
| logcost_transport_insurance_17 | 6.9 | 0.005 |
| state_19_wv | 0.002 | 0.005 |
| cost_health_rx_11 | 383.4 | 0.005 |
| occ_spouse_17_businessfinance | 0.023 | 0.005 |
| wealth_homeequity_11 | 68568.3 | 0.005 |
| occ_self_13_healthcareprac | 0.033 | 0.005 |
| ind_spouse_19_otherservices | 0.029 | 0.005 |
| own_or_rent_17_own | 0.588 | 0.005 |
| moved_11_no | 0.609 | 0.005 |
| race_spouse_17_pacis | 0.0 | 0.004 |
| cost_transport_leases_11 | 235.2 | 0.004 |
| occ_self_19_healthcareprac | 0.053 | 0.004 |
| religion_self_11_orthodox | 0.001 | 0.004 |
| time_work_prevyear_sp_11 | 21.2 | 0.004 |
| occ_spouse_19_architectengineering | 0.012 | 0.004 |
| race_spouse_19_white | 0.528 | 0.004 |
| religion_self_11_nonchristian | 0.013 | 0.004 |
| grewup_region_self_west | 0.164 | 0.004 |
| cost_housing_furnishing_11 | 1180.4 | 0.004 |
| occ_spouse_15_businessfinance | 0.021 | 0.004 |
| occ_spouse_17_architectengineering | 0.01 | 0.004 |
| occ_self_11_transport | 0.039 | 0.004 |
| occ_self_13_arts | 0.013 | 0.004 |
| state_11_vt | 0.001 | 0.004 |
| state_13_vt | 0.001 | 0.004 |
| wealth_15 | 293484.4 | 0.004 |
| state_19_tn | 0.024 | 0.004 |
| occ_spouse_15_janitors | 0.016 | 0.004 |
| empstat_current_spouse_17_student | 0.006 | 0.004 |
| race_self_13_amind | 0.004 | 0.003 |
| occ_self_15_arts | 0.014 | 0.003 |
| occ_self_11_repair | 0.026 | 0.003 |
| cost_transport_additionalvehicle_13 | 1191.8 | 0.003 |
| religion_self_19_protestant | 0.006 | 0.003 |
| logcost_health_bills_19 | 0.663 | 0.003 |
| logcost_transport_downpayment_17 | 1.8 | 0.003 |
| moved_why_15_mixed | 0.017 | 0.003 |
| logcost_housing_furnishing_17 | 4.4 | 0.003 |
| logcost_housing_utility_17 | 7.4 | 0.003 |
| state_19_va | 0.033 | 0.003 |
| region_15_akhi | 0.001 | 0.003 |
| weight_indiv_cs_15 | 18566.8 | 0.003 |
| occ_spouse_15_officeadmin | 0.066 | 0.003 |
| empstat_current_spouse_15_student | 0.006 | 0.003 |
| occ_self_15_softscience | 0.013 | 0.003 |
| state_17_tn | 0.022 | 0.003 |
| cost_health_hospital_19 | 535.9 | 0.003 |
| race_spouse_19_pacis | 0.001 | 0.003 |
| occ_spouse_17_compscimath | 0.015 | 0.003 |
| occ_self_19_management | 0.09 | 0.002 |
| interview_number_19 | 4532.6 | 0.002 |
| state_11_mn | 0.01 | 0.002 |
| state_17_nc | 0.034 | 0.002 |
| union_self_13_no | 0.478 | 0.002 |
| state_19_mn | 0.013 | 0.002 |
| moved_why_15_consother | 0.086 | 0.002 |
| logcost_housing_rent_15 | 3.1 | 0.002 |
| occ_self_13_softscience | 0.011 | 0.002 |
| state_13_wy | 0.002 | 0.002 |
| occ_spouse_13_sales | 0.052 | 0.002 |
| state_17_mn | 0.013 | 0.002 |
| weight_indiv_cs_13 | 16793.2 | 0.002 |
| empstat_current_self_19_searching | 0.034 | 0.002 |
| occ_spouse_11_food | 0.013 | 0.002 |
| occ_self_17_management | 0.078 | 0.002 |
| religion_self_17_none | 0.154 | 0.002 |
| race_spouse_11_black | 0.034 | 0.002 |
| logcost_food_deliver_13 | 0.698 | 0.002 |
| state_17_ms | 0.01 | 0.002 |
| occ_self_15_protective | 0.018 | 0.002 |
| state_17_mt | 0.001 | 0.001 |
| occ_self_11_protective | 0.017 | 0.001 |
| ind_spouse_15_profsciencetech | 0.03 | 0.001 |
| kids_youngest_15 | 7.8 | 0.001 |
| ind_spouse_19_construction | 0.037 | 0.001 |
| state_19_ms | 0.01 | 0.001 |
| occ_spouse_19_officeadmin | 0.077 | 0.001 |
| state_11_wy | 0.001 | 0.001 |
| occ_spouse_11_legal | 0.004 | 0.001 |
| moved_why_17_consneighbor | 0.023 | 0.001 |
| sequence_number_15 | 2.5 | 0.001 |
| occ_spouse_11_officeadmin | 0.059 | 0.001 |
| race_self_11_amind | 0.004 | 0.001 |
| logcost_transport_additionalvehicle_13 | 1.9 | 0.001 |
| ind_spouse_17_otherservices | 0.025 | 0.001 |
| region_19_foreign | 0.006 | 0.001 |
| occ_spouse_15_legal | 0.006 | 0.001 |
| state_19_nh | 0.004 | 0.001 |
| empstat_current_self_17_student | 0.011 | 0.001 |
| moved_why_17_productive | 0.029 | 0.001 |
| state_19_wa | 0.023 | 0.001 |
| logcost_housing_rent_17 | 3.5 | 0.0 |
| state_15_ct | 0.004 | 0.0 |
| religion_self_17_orthodox | 0.005 | 0.0 |
| logcost_clothing_15 | 6.5 | 0.0 |
| moved_why_11_involuntary | 0.045 | 0.0 |
| ind_spouse_17_transportwarehouse | 0.019 | 0.0 |
| state_17_dc | 0.002 | 0.0 |
| empstat_current_spouse_11_laid off | 0.001 | 0.0 |
| religion_spouse_19_jewish | 0.013 | 0.0 |
| state_19_wy | 0.001 | 0.0 |
| state_17_al | 0.008 | 0.0 |
| occ_self_17_repair | 0.033 | -0.0 |
| occ_spouse_11_compscimath | 0.009 | -0.0 |
| religion_spouse_11_nonchristian | 0.01 | -0.0 |
| occ_self_13_military | 0.007 | -0.0 |
| state_17_ct | 0.006 | -0.0 |
| state_13_wv | 0.002 | -0.0 |
| region_17_akhi | 0.002 | -0.0 |
| state_13_al | 0.007 | -0.0 |
| state_17_wa | 0.022 | -0.0 |
| religion_spouse_15_nonchristian | 0.011 | -0.0 |
| moved_why_13_consother | 0.074 | -0.0 |
| cost_trips_11 | 1904.7 | -0.0 |
| cost_health_rx_13 | 435.8 | -0.001 |
| occ_self_11_softscience | 0.01 | -0.001 |
| cost_health_15 | 4357.5 | -0.001 |
| state_11_hi | 0.0 | -0.001 |
| state_11_nc | 0.03 | -0.001 |
| logcost_housing_tax_13 | 4.8 | -0.001 |
| sequence_number_13 | 2.5 | -0.001 |
| cost_clothing_13 | 1556.5 | -0.001 |
| cost_clothing_11 | 1566.7 | -0.001 |
| educyrs_11 | 10.2 | -0.001 |
| state_19_de | 0.001 | -0.001 |
| moved_why_13_homeless | 0.001 | -0.001 |
| occ_spouse_11_farmfishforest | 0.004 | -0.001 |
| race_self_19_amind | 0.005 | -0.001 |
| logcost_health_bills_15 | 0.795 | -0.001 |
| state_19_nc | 0.036 | -0.001 |
| race_self_19_pacis | 0.001 | -0.001 |
| occ_spouse_11_softscience | 0.009 | -0.001 |
| state_19_mt | 0.001 | -0.001 |
| occ_self_17_janitors | 0.036 | -0.001 |
| state_19_ct | 0.008 | -0.001 |
| occ_spouse_13_architectengineering | 0.008 | -0.001 |
| kids_youngest_13 | 7.9 | -0.001 |
| empstat_current_spouse_19_searching | 0.017 | -0.002 |
| logincome_wagerate_spouse_11 | 1.8 | -0.002 |
| occ_self_13_farmfishforest | 0.007 | -0.002 |
| occ_spouse_11_hardscience | 0.004 | -0.002 |
| wealth_other_15 | 207594.1 | -0.002 |
| state_15_nc | 0.03 | -0.002 |
| ind_spouse_15_adminmilitary | 0.031 | -0.002 |
| logcost_food_11 | 8.8 | -0.002 |
| occ_spouse_17_management | 0.052 | -0.002 |
| state_17_vt | 0.002 | -0.002 |
| occ_spouse_15_architectengineering | 0.009 | -0.002 |
| occ_spouse_13_officeadmin | 0.061 | -0.002 |
| religion_self_15_other | 0.003 | -0.002 |
| religion_self_17_other | 0.003 | -0.002 |
| cost_transport_downpayment_15 | 1368.4 | -0.002 |
| occ_self_13_janitors | 0.026 | -0.002 |
| occ_spouse_13_hardscience | 0.006 | -0.002 |
| moved_why_15_consmore | 0.042 | -0.002 |
| logcost_housing_insurance_11 | 4.2 | -0.002 |
| occ_self_13_protective | 0.018 | -0.002 |
| hh_size_15 | 2.9 | -0.002 |
| cost_health_insurance_11 | 1735.7 | -0.002 |
| moved_why_11_mixed | 0.027 | -0.002 |
| state_13_wa | 0.021 | -0.002 |
| moved_why_13_involuntary | 0.043 | -0.003 |
| age_self_13 | 43.2 | -0.003 |
| empstat_current_spouse_17_searching | 0.016 | -0.003 |
| state_15_mt | 0.001 | -0.003 |
| empstat_current_spouse_19_student | 0.008 | -0.003 |
| state_19_dc | 0.003 | -0.003 |
| moved_why_15_closertowork | 0.017 | -0.003 |
| logcost_health_hospital_15 | 1.5 | -0.003 |
| empstat_current_spouse_15_searching | 0.013 | -0.003 |
| occ_spouse_17_officeadmin | 0.072 | -0.003 |
| occ_self_11_military | 0.007 | -0.003 |
| occ_self_17_healthcareprac | 0.044 | -0.003 |
| state_13_dc | 0.002 | -0.003 |
| occ_spouse_15_softscience | 0.01 | -0.003 |
| logcost_health_rx_13 | 4.2 | -0.003 |
| ind_spouse_19_mining | 0.002 | -0.003 |
| state_13_nc | 0.031 | -0.003 |
| cost_transport_downpayment_19 | 1711.9 | -0.003 |
| ind_spouse_19_transportwarehouse | 0.023 | -0.003 |
| age_self_11 | 42.3 | -0.003 |
| moved_why_15_involuntary | 0.038 | -0.003 |
| occ_spouse_17_legal | 0.006 | -0.003 |
| cost_housing_repairs_11 | 2169.7 | -0.003 |
| region_15_foreign | 0.005 | -0.003 |
| empstat_current_self_17_searching | 0.031 | -0.004 |
| cost_transport_downpayment_13 | 1133.1 | -0.004 |
| moved_why_13_consless | 0.02 | -0.004 |
| state_11_az | 0.013 | -0.004 |
| race_self_17_pacis | 0.001 | -0.004 |
| race_self_17_amind | 0.005 | -0.004 |
| region_13_foreign | 0.005 | -0.004 |
| moved_why_19_consneighbor | 0.028 | -0.004 |
| logcost_transport_leases_13 | 0.425 | -0.004 |
| cost_health_insurance_15 | 2599.5 | -0.004 |
| mightmove_11_yes | 0.283 | -0.004 |
| ind_spouse_15_transportwarehouse | 0.019 | -0.004 |
| state_13_mt | 0.002 | -0.004 |
| cost_transport_other_15 | 164.3 | -0.004 |
| logcost_transport_loans_11 | 2.3 | -0.004 |
| occ_self_15_janitors | 0.03 | -0.004 |
| state_11_wv | 0.001 | -0.005 |
| state_11_mt | 0.002 | -0.005 |
| occ_spouse_17_janitors | 0.021 | -0.005 |
| age_self_15 | 44.2 | -0.005 |
| ind_spouse_15_management | 0.015 | -0.005 |
| ind_spouse_17_retail | 0.043 | -0.005 |
| religion_self_13_nonchristian | 0.013 | -0.005 |
| ind_spouse_17_wholesale | 0.017 | -0.005 |
| religion_spouse_19_nonchristian | 0.021 | -0.005 |
| logcost_housing_furnishing_11 | 4.5 | -0.005 |
| ind_spouse_17_farmfishforest | 0.011 | -0.005 |
| state_13_nm | 0.002 | -0.005 |
| occ_self_17_officeadmin | 0.121 | -0.005 |
| state_15_va | 0.03 | -0.005 |
| ind_spouse_15_mining | 0.002 | -0.005 |
| hh_size_13 | 3.0 | -0.005 |
| logcost_trips_11 | 5.2 | -0.005 |
| moved_why_11_productive | 0.016 | -0.005 |
| state_15_wa | 0.021 | -0.005 |
| state_13_hi | 0.0 | -0.005 |
| logwealth_13 | 10.8 | -0.005 |
| occ_self_13_transport | 0.041 | -0.006 |
| religion_spouse_19_protestant | 0.004 | -0.006 |
| state_15_dc | 0.002 | -0.006 |
| occ_self_11_farmfishforest | 0.007 | -0.006 |
| occ_spouse_15_DKNARefused | 0.002 | -0.006 |
| state_17_va | 0.031 | -0.006 |
| religion_self_15_none | 0.124 | -0.006 |
| ind_spouse_17_DKNARefused | 0.002 | -0.006 |
| ind_spouse_17_adminmilitary | 0.032 | -0.006 |
| occ_self_17_farmfishforest | 0.01 | -0.006 |
| ind_spouse_19_DKNARefused | 0.002 | -0.006 |
| state_13_ok | 0.009 | -0.006 |
| religion_spouse_17_nonchristian | 0.024 | -0.006 |
| state_13_ct | 0.004 | -0.006 |
| state_11_al | 0.007 | -0.006 |
| grewup_region_self_akhi | 0.002 | -0.006 |
| moved_15_yes | 0.281 | -0.006 |
| ind_spouse_15_DKNARefused | 0.002 | -0.006 |
| state_19_vt | 0.002 | -0.006 |
| empstat_current_spouse_11_other | 0.001 | -0.006 |
| moved_why_17_homeless | 0.004 | -0.006 |
| own_or_rent_15_own | 0.558 | -0.006 |
| religion_self_13_none | 0.105 | -0.007 |
| region_11_akhi | 0.001 | -0.007 |
| cost_health_11 | 3166.8 | -0.007 |
| state_11_ak | 0.001 | -0.007 |
| logcost_housing_furnishing_13 | 4.5 | -0.007 |
| empstat_19_retired | 0.029 | -0.007 |
| religion_spouse_15_other | 0.002 | -0.007 |
| moved_why_11_homeless | 0.002 | -0.007 |
| empstat_current_spouse_11_disabled | 0.01 | -0.007 |
| occ_self_11_DKNARefused | 0.002 | -0.007 |
| moved_why_17_consless | 0.021 | -0.007 |
| ind_spouse_19_retail | 0.043 | -0.007 |
| occ_spouse_13_DKNARefused | 0.003 | -0.007 |
| logcost_transport_repair_15 | 6.6 | -0.007 |
| state_15_me | 0.004 | -0.007 |
| occ_self_15_transport | 0.046 | -0.007 |
| occ_self_19_healthcaresupport | 0.029 | -0.007 |
| state_17_la | 0.007 | -0.008 |
| occ_self_17_pcareservice | 0.029 | -0.008 |
| weight_indiv_long_19 | 39.3 | -0.008 |
| moved_why_13_productive | 0.022 | -0.008 |
| empstat_current_spouse_15_working | 0.402 | -0.008 |
| state_11_ct | 0.004 | -0.008 |
| occ_self_13_repair | 0.025 | -0.008 |
| occ_self_17_production | 0.055 | -0.008 |
| state_19_tx | 0.07 | -0.008 |
| state_15_ky | 0.014 | -0.008 |
| logincome_labor_spouse_11 | 6.1 | -0.008 |
| empstat_current_spouse_13_working | 0.377 | -0.008 |
| cost_housing_repairs_15 | 1877.1 | -0.008 |
| state_17_ak | 0.001 | -0.008 |
| moved_why_15_consneighbor | 0.025 | -0.009 |
| race_self_15_pacis | 0.001 | -0.009 |
| state_13_ky | 0.015 | -0.009 |
| religion_self_11_none | 0.095 | -0.009 |
| logcost_health_bills_17 | 0.718 | -0.009 |
| state_17_me | 0.004 | -0.009 |
| religion_self_19_orthodox | 0.023 | -0.009 |
| cost_health_hospital_15 | 432.9 | -0.009 |
| state_15_al | 0.007 | -0.009 |
| occ_spouse_19_farmfishforest | 0.006 | -0.009 |
| state_11_dc | 0.002 | -0.009 |
| union_spouse_13_no | 0.289 | -0.009 |
| occ_spouse_15_protective | 0.011 | -0.009 |
| state_17_tx | 0.065 | -0.009 |
| state_15_nm | 0.002 | -0.009 |
| moved_13_yes | 0.269 | -0.009 |
| state_11_tx | 0.059 | -0.009 |
| occ_spouse_13_softscience | 0.009 | -0.009 |
| logcost_recreation_13 | 5.3 | -0.009 |
| ind_spouse_15_utilities | 0.005 | -0.009 |
| moved_why_15_homeless | 0.002 | -0.009 |
| state_13_nh | 0.002 | -0.009 |
| logcost_clothing_11 | 6.5 | -0.009 |
| occ_spouse_19_food | 0.022 | -0.009 |
| empstat_current_spouse_19_laid off | 0.002 | -0.009 |
| cost_health_bills_13 | 878.4 | -0.009 |
| own_or_rent_15_rent | 0.299 | -0.009 |
| empstat_current_spouse_13_laid off | 0.002 | -0.009 |
| logcost_clothing_13 | 6.5 | -0.01 |
| state_17_ok | 0.01 | -0.01 |
| logcost_transport_downpayment_13 | 1.6 | -0.01 |
| occ_self_15_farmfishforest | 0.008 | -0.01 |
| occ_spouse_15_management | 0.041 | -0.01 |
| occ_spouse_17_production | 0.028 | -0.01 |
| religion_spouse_13_nonchristian | 0.009 | -0.01 |
| grewup_region_spouse_11_south | 0.116 | -0.01 |
| occ_self_19_DKNARefused | 0.002 | -0.01 |
| ind_spouse_17_mining | 0.002 | -0.01 |
| occ_self_13_healthcaresupport | 0.018 | -0.01 |
| state_17_nh | 0.005 | -0.01 |
| occ_spouse_13_legal | 0.005 | -0.01 |
| empstat_13_laid off | 0.003 | -0.01 |
| state_11_pa | 0.044 | -0.01 |
| race_spouse_17_white | 0.473 | -0.01 |
| occ_self_11_janitors | 0.024 | -0.01 |
| mightmove_13_yes | 0.276 | -0.01 |
| ind_spouse_15_retail | 0.037 | -0.01 |
| religion_spouse_17_other | 0.002 | -0.011 |
| state_11_ok | 0.01 | -0.011 |
| occ_spouse_13_constructionextraction | 0.021 | -0.011 |
| cost_health_13 | 4224.0 | -0.011 |
| state_15_wi | 0.015 | -0.011 |
| occ_spouse_13_farmfishforest | 0.005 | -0.011 |
| grewup_region_spouse_13_south | 0.123 | -0.011 |
| ind_spouse_17_utilities | 0.006 | -0.011 |
| cost_recreation_13 | 960.8 | -0.011 |
| state_13_tx | 0.059 | -0.011 |
| state_13_va | 0.031 | -0.011 |
| state_15_tx | 0.061 | -0.011 |
| occ_self_17_transport | 0.053 | -0.011 |
| state_19_me | 0.004 | -0.011 |
| race_self_15_amind | 0.004 | -0.011 |
| empstat_current_self_13_laid off | 0.003 | -0.011 |
| occ_self_11_arts | 0.012 | -0.011 |
| union_spouse_15_no | 0.311 | -0.011 |
| occ_spouse_17_transport | 0.026 | -0.011 |
| state_13_ak | 0.001 | -0.011 |
| state_15_ak | 0.001 | -0.011 |
| region_11_foreign | 0.006 | -0.011 |
| occ_spouse_15_food | 0.014 | -0.011 |
| occ_self_15_military | 0.008 | -0.011 |
| moved_why_11_consother | 0.068 | -0.011 |
| kids_num_15 | 0.817 | -0.011 |
| ind_spouse_19_accomodationsfood | 0.029 | -0.012 |
| religion_spouse_11_none | 0.239 | -0.012 |
| occ_spouse_15_farmfishforest | 0.005 | -0.012 |
| state_19_la | 0.006 | -0.012 |
| region_19_akhi | 0.003 | -0.012 |
| state_19_ok | 0.011 | -0.012 |
| state_13_az | 0.014 | -0.012 |
| educyrs_15 | 11.3 | -0.012 |
| ind_spouse_15_construction | 0.028 | -0.012 |
| occ_spouse_11_protective | 0.01 | -0.012 |
| occ_spouse_11_military | 0.004 | -0.012 |
| empstat_current_spouse_19_retired | 0.058 | -0.012 |
| cost_health_insurance_13 | 2501.9 | -0.012 |
| state_11_ky | 0.016 | -0.012 |
| state_13_me | 0.003 | -0.012 |
| own_or_rent_15_neither | 0.028 | -0.012 |
| region_13_akhi | 0.001 | -0.012 |
| region_17_foreign | 0.005 | -0.012 |
| cost_health_rx_15 | 403.1 | -0.012 |
| occ_spouse_19_constructionextraction | 0.029 | -0.012 |
| state_11_nh | 0.002 | -0.012 |
| logcost_housing_insurance_13 | 4.1 | -0.012 |
| occ_spouse_11_architectengineering | 0.007 | -0.012 |
| state_11_va | 0.03 | -0.013 |
| empstat_current_self_11_searching | 0.039 | -0.013 |
| mightmove_11_no | 0.585 | -0.013 |
| empstat_current_spouse_11_working | 0.361 | -0.013 |
| state_13_nv | 0.008 | -0.013 |
| occ_self_17_DKNARefused | 0.002 | -0.013 |
| state_13_pa | 0.043 | -0.013 |
| wealth_17 | 298408.5 | -0.013 |
| occ_spouse_19_DKNARefused | 0.001 | -0.013 |
| state_11_nm | 0.002 | -0.013 |
| ind_spouse_17_management | 0.019 | -0.013 |
| empstat_current_self_11_other | 0.001 | -0.013 |
| occ_spouse_11_management | 0.039 | -0.013 |
| wealth_11 | 229454.8 | -0.013 |
| moved_why_17_closertowork | 0.016 | -0.013 |
| sequence_number_11 | 2.5 | -0.013 |
| occ_spouse_19_transport | 0.029 | -0.014 |
| cost_health_bills_15 | 1860.4 | -0.014 |
| empstat_17_student | 0.009 | -0.014 |
| moved_15_no | 0.605 | -0.014 |
| logcost_health_hospital_13 | 1.6 | -0.014 |
| state_17_pa | 0.043 | -0.014 |
| occ_spouse_15_military | 0.004 | -0.014 |
| occ_self_19_farmfishforest | 0.01 | -0.014 |
| state_11_co | 0.02 | -0.014 |
| occ_spouse_13_protective | 0.012 | -0.014 |
| sequence_number_17 | 2.1 | -0.014 |
| moved_why_19_consother | 0.093 | -0.014 |
| mightmove_17_no | 0.612 | -0.014 |
| occ_self_13_DKNARefused | 0.003 | -0.014 |
| occ_self_19_officeadmin | 0.14 | -0.014 |
| educyrs_13 | 10.6 | -0.014 |
| ind_spouse_19_utilities | 0.007 | -0.014 |
| occ_self_17_healthcaresupport | 0.026 | -0.014 |
| empstat_17_disabled | 0.005 | -0.015 |
| religion_self_17_nonchristian | 0.03 | -0.015 |
| empstat_current_self_19_disabled | 0.008 | -0.015 |
| empstat_current_self_19_student | 0.01 | -0.015 |
| moved_why_19_mixed | 0.028 | -0.015 |
| cost_health_bills_11 | 762.9 | -0.015 |
| occ_spouse_19_management | 0.059 | -0.015 |
| state_19_sc | 0.021 | -0.015 |
| moved_13_no | 0.611 | -0.015 |
| state_15_la | 0.005 | -0.015 |
| state_17_nv | 0.009 | -0.015 |
| state_13_co | 0.019 | -0.015 |
| state_11_me | 0.003 | -0.015 |
| own_or_rent_11_own | 0.576 | -0.015 |
| logcost_housing_repairs_11 | 4.2 | -0.015 |
| wealth_other_11 | 160886.5 | -0.015 |
| occ_self_17_military | 0.007 | -0.015 |
| state_15_pa | 0.042 | -0.016 |
| empstat_15_student | 0.018 | -0.016 |
| empstat_current_spouse_13_disabled | 0.012 | -0.016 |
| occ_self_19_transport | 0.066 | -0.016 |
| state_13_sc | 0.019 | -0.016 |
| state_17_az | 0.018 | -0.016 |
| occ_spouse_17_protective | 0.011 | -0.016 |
| logwealth_homeequity_11 | 6.8 | -0.016 |
| state_19_co | 0.024 | -0.016 |
| state_17_ky | 0.019 | -0.016 |
| state_11_ks | 0.005 | -0.016 |
| occ_self_19_military | 0.008 | -0.016 |
| occ_self_11_officeadmin | 0.097 | -0.016 |
| occ_spouse_13_military | 0.004 | -0.016 |
| state_15_az | 0.014 | -0.016 |
| union_spouse_11_no | 0.269 | -0.016 |
| religion_self_11_other | 0.009 | -0.017 |
| own_or_rent_19_rent | 0.353 | -0.017 |
| state_17_co | 0.02 | -0.017 |
| wealth_19 | 327531.4 | -0.017 |
| moved_19_yes | 0.302 | -0.017 |
| moved_why_15_consless | 0.023 | -0.017 |
| state_11_id | 0.002 | -0.017 |
| state_19_ri | 0.001 | -0.017 |
| state_11_la | 0.005 | -0.017 |
| state_13_id | 0.002 | -0.017 |
| state_15_id | 0.002 | -0.017 |
| state_17_id | 0.002 | -0.017 |
| logcost_food_away_13 | 7.0 | -0.017 |
| state_19_nv | 0.01 | -0.017 |
| empstat_current_spouse_11_searching | 0.022 | -0.017 |
| occ_spouse_17_military | 0.003 | -0.017 |
| occ_spouse_17_food | 0.017 | -0.017 |
| mightmove_13_no | 0.584 | -0.017 |
| state_17_ri | 0.001 | -0.017 |
| logcost_housing_rent_19 | 3.5 | -0.017 |
| state_11_sc | 0.02 | -0.018 |
| state_19_az | 0.017 | -0.018 |
| wealth_13 | 230335.6 | -0.018 |
| ind_spouse_17_accomodationsfood | 0.022 | -0.018 |
| state_19_id | 0.001 | -0.018 |
| state_17_nm | 0.001 | -0.018 |
| occ_spouse_17_DKNARefused | 0.001 | -0.018 |
| mightmove_19_no | 0.644 | -0.018 |
| occ_spouse_15_constructionextraction | 0.024 | -0.018 |
| flag_allyears | 0.831 | -0.018 |
| ind_spouse_17_construction | 0.033 | -0.018 |
| occ_spouse_19_protective | 0.012 | -0.018 |
| state_11_nv | 0.008 | -0.018 |
| moved_why_19_consless | 0.017 | -0.018 |
| empstat_11_searching | 0.056 | -0.018 |
| state_15_ok | 0.01 | -0.018 |
| moved_why_19_involuntary | 0.034 | -0.018 |
| occ_spouse_17_farmfishforest | 0.007 | -0.019 |
| state_15_co | 0.02 | -0.019 |
| religion_self_13_other | 0.009 | -0.019 |
| occ_spouse_13_transport | 0.02 | -0.019 |
| empstat_current_self_13_disabled | 0.004 | -0.019 |
| grewup_region_spouse_13_west | 0.081 | -0.019 |
| state_15_sc | 0.019 | -0.019 |
| cost_transport_leases_13 | 267.5 | -0.019 |
| occ_self_15_healthcaresupport | 0.02 | -0.019 |
| occ_self_13_food | 0.027 | -0.019 |
| state_19_nm | 0.002 | -0.019 |
| ind_spouse_15_accomodationsfood | 0.019 | -0.019 |
| state_17_wi | 0.015 | -0.019 |
| empstat_current_spouse_15_retired | 0.034 | -0.019 |
| state_13_or | 0.019 | -0.019 |
| religion_spouse_13_none | 0.266 | -0.02 |
| interview_number_15 | 4037.6 | -0.02 |
| moved_why_11_consless | 0.019 | -0.02 |
| religion_self_19_other | 0.002 | -0.02 |
| state_19_ak | 0.002 | -0.02 |
| grewup_region_self_south | 0.246 | -0.02 |
| occ_self_19_production | 0.065 | -0.02 |
| state_17_or | 0.021 | -0.02 |
| state_19_ky | 0.018 | -0.02 |
| state_15_or | 0.02 | -0.02 |
| interview_number_17 | 4424.8 | -0.02 |
| moved_11_yes | 0.275 | -0.02 |
| occ_spouse_15_repair | 0.018 | -0.02 |
| occ_spouse_13_management | 0.042 | -0.021 |
| grewup_region_spouse_11_west | 0.077 | -0.021 |
| moved_why_13_consmore | 0.039 | -0.021 |
| empstat_current_spouse_15_disabled | 0.012 | -0.021 |
| kids_num_13 | 0.914 | -0.021 |
| state_17_sc | 0.021 | -0.021 |
| occ_spouse_17_constructionextraction | 0.027 | -0.021 |
| state_15_nv | 0.009 | -0.021 |
| occ_spouse_11_constructionextraction | 0.019 | -0.021 |
| logcost_health_bills_13 | 0.789 | -0.021 |
| empstat_current_spouse_17_disabled | 0.017 | -0.021 |
| occ_self_15_DKNARefused | 0.002 | -0.021 |
| empstat_13_searching | 0.048 | -0.021 |
| occ_self_15_officeadmin | 0.11 | -0.021 |
| state_11_ri | 0.001 | -0.022 |
| own_or_rent_13_neither | 0.032 | -0.022 |
| moved_why_11_consmore | 0.046 | -0.022 |
| wealth_other_17 | 204533.1 | -0.022 |
| occ_spouse_15_transport | 0.025 | -0.022 |
| state_15_mi | 0.031 | -0.022 |
| logwealth_homeequity_13 | 6.7 | -0.022 |
| occ_self_17_sales | 0.07 | -0.022 |
| state_11_wi | 0.016 | -0.022 |
| wealth_other_13 | 157346.0 | -0.022 |
| occ_self_11_healthcaresupport | 0.017 | -0.022 |
| religion_spouse_15_none | 0.297 | -0.022 |
| state_15_ar | 0.018 | -0.022 |
| hh_size_11 | 3.1 | -0.022 |
| occ_spouse_11_production | 0.025 | -0.022 |
| state_13_sd | 0.004 | -0.022 |
| own_or_rent_19_neither | 0.032 | -0.023 |
| state_19_pa | 0.043 | -0.023 |
| logcost_health_hospital_11 | 1.8 | -0.023 |
| occ_self_13_officeadmin | 0.098 | -0.023 |
| state_13_ri | 0.001 | -0.023 |
| state_15_ri | 0.001 | -0.023 |
| empstat_13_disabled | 0.005 | -0.023 |
| state_15_sd | 0.004 | -0.023 |
| empstat_current_spouse_19_disabled | 0.011 | -0.024 |
| occ_spouse_11_transport | 0.023 | -0.024 |
| cost_health_hospital_11 | 361.6 | -0.024 |
| wealth_other_19 | 221101.2 | -0.024 |
| empstat_current_spouse_17_retired | 0.042 | -0.024 |
| state_11_mo | 0.023 | -0.024 |
| moved_17_no | 0.649 | -0.024 |
| ind_spouse_15_wholesale | 0.013 | -0.024 |
| state_19_wi | 0.016 | -0.024 |
| ind_spouse_19_farmfishforest | 0.011 | -0.024 |
| empstat_current_spouse_13_searching | 0.016 | -0.024 |
| religion_self_19_nonchristian | 0.031 | -0.024 |
| occ_spouse_19_military | 0.003 | -0.024 |
| state_19_ar | 0.019 | -0.024 |
| state_19_or | 0.021 | -0.025 |
| ind_spouse_13_wholesale | 0.012 | -0.025 |
| religion_spouse_17_none | 0.358 | -0.025 |
| state_17_ar | 0.019 | -0.025 |
| state_13_la | 0.006 | -0.025 |
| state_17_nd | 0.002 | -0.025 |
| state_19_nd | 0.002 | -0.025 |
| state_11_nd | 0.002 | -0.025 |
| state_13_nd | 0.002 | -0.025 |
| weight_indiv_long_11 | 25.3 | -0.025 |
| state_13_wi | 0.015 | -0.026 |
| ind_spouse_15_farmfishforest | 0.01 | -0.026 |
| state_13_mo | 0.024 | -0.026 |
| state_13_ar | 0.019 | -0.026 |
| religion_spouse_13_other | 0.007 | -0.026 |
| weight_indiv_long_17 | 28.1 | -0.026 |
| cost_health_hospital_13 | 367.1 | -0.026 |
| state_17_sd | 0.004 | -0.026 |
| state_19_sd | 0.004 | -0.026 |
| state_11_ne | 0.008 | -0.026 |
| state_15_nh | 0.002 | -0.026 |
| state_11_or | 0.019 | -0.026 |
| empstat_15_other | 0.002 | -0.027 |
| mightmove_15_no | 0.569 | -0.027 |
| race_spouse_15_white | 0.432 | -0.027 |
| occ_spouse_17_repair | 0.02 | -0.027 |
| race_spouse_15_amind | 0.004 | -0.027 |
| relation_to_head_13 | 13.4 | -0.027 |
| state_11_mi | 0.033 | -0.027 |
| race_spouse_13_amind | 0.004 | -0.027 |
| own_or_rent_13_own | 0.558 | -0.027 |
| state_15_ne | 0.007 | -0.027 |
| weight_indiv_long_13 | 25.1 | -0.027 |
| state_13_mi | 0.032 | -0.027 |
| occ_spouse_13_production | 0.025 | -0.027 |
| occ_spouse_19_repair | 0.019 | -0.027 |
| religion_spouse_17_protestant | 0.288 | -0.027 |
| state_13_ks | 0.005 | -0.027 |
| state_11_ar | 0.017 | -0.028 |
| empstat_current_spouse_13_retired | 0.029 | -0.028 |
| occ_spouse_19_production | 0.033 | -0.028 |
| relation_to_head_15 | 13.5 | -0.028 |
| state_17_mo | 0.023 | -0.028 |
| occ_self_19_sales | 0.079 | -0.028 |
| race_spouse_19_amind | 0.005 | -0.028 |
| occ_spouse_15_production | 0.023 | -0.028 |
| religion_spouse_11_other | 0.007 | -0.029 |
| kids_num_11 | 0.99 | -0.029 |
| state_15_mo | 0.023 | -0.029 |
| state_15_nd | 0.002 | -0.029 |
| race_spouse_11_amind | 0.004 | -0.029 |
| weight_indiv_long_15 | 28.3 | -0.029 |
| empstat_current_self_19_retired | 0.044 | -0.029 |
| state_19_mo | 0.025 | -0.03 |
| occ_spouse_13_repair | 0.018 | -0.03 |
| ind_spouse_17_manufacturing | 0.058 | -0.03 |
| empstat_current_self_19_housespouse | 0.026 | -0.03 |
| own_or_rent_11_neither | 0.031 | -0.031 |
| race_spouse_11_white | 0.397 | -0.031 |
| logcost_food_away_11 | 6.9 | -0.032 |
| race_spouse_17_amind | 0.005 | -0.032 |
| state_17_mi | 0.035 | -0.032 |
| state_13_ne | 0.007 | -0.032 |
| state_19_ks | 0.005 | -0.032 |
| occ_self_11_food | 0.026 | -0.033 |
| own_or_rent_17_neither | 0.031 | -0.033 |
| race_self_19_white | 0.739 | -0.033 |
| state_19_mi | 0.036 | -0.033 |
| logcost_health_bills_11 | 0.724 | -0.033 |
| religion_spouse_19_none | 0.308 | -0.033 |
| race_spouse_13_white | 0.408 | -0.033 |
| relation_to_head_11 | 13.6 | -0.034 |
| religion_spouse_11_protestant | 0.233 | -0.034 |
| occ_self_17_food | 0.039 | -0.035 |
| state_15_oh | 0.036 | -0.035 |
| empstat_17_housespouse | 0.022 | -0.036 |
| state_17_oh | 0.036 | -0.036 |
| state_15_ks | 0.006 | -0.036 |
| state_17_ks | 0.007 | -0.037 |
| empstat_13_retired | 0.011 | -0.037 |
| empstat_current_self_17_housespouse | 0.023 | -0.037 |
| religion_spouse_13_protestant | 0.242 | -0.037 |
| occ_self_15_food | 0.03 | -0.037 |
| ind_spouse_15_manufacturing | 0.052 | -0.037 |
| state_11_sd | 0.004 | -0.037 |
| state_13_oh | 0.037 | -0.038 |
| state_17_ne | 0.011 | -0.038 |
| state_11_in | 0.027 | -0.038 |
| occ_spouse_11_repair | 0.019 | -0.038 |
| state_19_in | 0.028 | -0.039 |
| state_19_ne | 0.011 | -0.039 |
| state_11_oh | 0.038 | -0.039 |
| empstat_11_housespouse | 0.029 | -0.04 |
| religion_self_11_protestant | 0.324 | -0.04 |
| race_self_11_white | 0.527 | -0.04 |
| empstat_current_spouse_11_retired | 0.023 | -0.04 |
| relation_to_head_19 | 13.3 | -0.04 |
| state_19_oh | 0.035 | -0.04 |
| religion_spouse_15_protestant | 0.259 | -0.04 |
| iswf_19 | 0.317 | -0.04 |
| sequence_number_19 | 1.3 | -0.04 |
| occ_self_11_sales | 0.079 | -0.04 |
| empstat_13_housespouse | 0.025 | -0.04 |
| race_self_17_white | 0.659 | -0.041 |
| empstat_11_retired | 0.008 | -0.041 |
| empstat_current_self_13_housespouse | 0.028 | -0.041 |
| religion_self_17_protestant | 0.412 | -0.042 |
| state_15_in | 0.027 | -0.042 |
| sex_spouse_19_male | 0.315 | -0.042 |
| empstat_current_self_11_retired | 0.014 | -0.042 |
| ind_spouse_19_manufacturing | 0.062 | -0.043 |
| race_self_15_white | 0.595 | -0.043 |
| empstat_17_retired | 0.019 | -0.044 |
| occ_self_13_education | 0.043 | -0.044 |
| religion_self_13_protestant | 0.345 | -0.044 |
| occ_self_15_sales | 0.086 | -0.045 |
| state_17_in | 0.027 | -0.045 |
| iswf_17 | 0.283 | -0.046 |
| occ_self_19_pcareservice | 0.034 | -0.046 |
| occ_self_11_education | 0.038 | -0.046 |
| sex_self_17_female | 0.437 | -0.046 |
| empstat_15_retired | 0.015 | -0.046 |
| state_13_in | 0.028 | -0.046 |
| religion_self_15_protestant | 0.369 | -0.047 |
| sex_female | 0.493 | -0.047 |
| sex_self_19_female | 0.493 | -0.047 |
| empstat_15_housespouse | 0.025 | -0.047 |
| state_11_ia | 0.018 | -0.048 |
| state_17_ia | 0.019 | -0.048 |
| sex_spouse_17_male | 0.282 | -0.049 |
| occ_self_15_education | 0.045 | -0.049 |
| race_self_13_white | 0.553 | -0.049 |
| empstat_current_self_13_retired | 0.016 | -0.049 |
| occ_self_19_education | 0.058 | -0.049 |
| occ_self_17_education | 0.052 | -0.05 |
| state_13_ia | 0.019 | -0.05 |
| state_19_ia | 0.019 | -0.051 |
| empstat_current_self_15_housespouse | 0.027 | -0.052 |
| state_15_ia | 0.019 | -0.053 |
| ind_self_17_retail | 0.073 | -0.053 |
| occ_self_19_food | 0.051 | -0.053 |
| occ_self_13_sales | 0.079 | -0.054 |
| empstat_current_self_11_housespouse | 0.031 | -0.055 |
| grewup_region_spouse_17_northcentral | 0.145 | -0.055 |
| empstat_current_self_17_retired | 0.028 | -0.056 |
| empstat_current_self_15_retired | 0.022 | -0.056 |
| hourlystatus_self_19_hourly | 0.488 | -0.057 |
| iswf_15 | 0.247 | -0.06 |
| sex_spouse_15_male | 0.247 | -0.06 |
| grewup_region_spouse_15_northcentral | 0.131 | -0.062 |
| grewup_region_spouse_11_northcentral | 0.119 | -0.064 |
| sex_self_15_female | 0.38 | -0.064 |
| time_housework_self_15 | 10.0 | -0.065 |
| grewup_region_spouse_13_northcentral | 0.121 | -0.065 |
| ind_self_19_retail | 0.088 | -0.067 |
| iswf_13 | 0.234 | -0.07 |
| iswf_11 | 0.227 | -0.071 |
| grewup_region_self_northcentral | 0.236 | -0.071 |
| region_15_northcentral | 0.203 | -0.084 |
| region_11_northcentral | 0.209 | -0.086 |
| region_13_northcentral | 0.206 | -0.092 |
| region_17_northcentral | 0.217 | -0.095 |
| region_19_northcentral | 0.218 | -0.097 |

</details>

### Sidenote: Commuting time by region

I was curious about that negative correlation between midwest residence and commute time in the PSID data.
To expand on that, I looked at the weighted average commute time by region.
Commute time is round trip, and conditional on having a positive commute time.

| region | chance commutes | commute time |
|:--|:--|:--|
| south | 57% | 43 min |
| midwest | 59% | 36 min |
| west | 58% | 44 min |
| northeast | 60% | 49 min |

(remember midwest is called northcentral in psid)

<!--TODO: Does this also show up in ATUS data?-->

To check whether this is a fluke, I look at the same question in the ATUS data (2004-2019).

| region | chance commutes | commute time |
|:--|:--|:--|
| south | 27% | 41 min |
| midwest | 29% | 38 min |
| west | 28% | 43 min |
| northeast | 28% | 47 min |

The "chance commutes" columns aren't directly comparable. 
The condition checked in the PSID is whether they were able to answer the question about their typical round trip commute time, 
while the condition in the ATUS is whether they commuted today (as defined using the dwell 30 anchor rule).

The conditional commute time columns do look qualitatively similar though.
So yeah, I guess midwesterners have shorter commute times.

(Midwesterners also seem to have a bit lower variance in commute time as well. (Not shown))

























































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







