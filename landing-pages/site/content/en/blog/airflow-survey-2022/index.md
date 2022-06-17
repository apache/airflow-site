---
title: "Airflow Survey 2022"
linkTitle: "Airflow Survey 2022"
author: "John Thomas, Ewa Tatarczak"
github: "Tohn Jhomas"
linkedin: "john-e-thomas"
description: "2021 saw rapid adoption of Airflow 2, and continued growth of the community. This annual survey helps us understand how people are using Airflow, and where we can best focus our efforts going forward."
tags: ["community", "survey", "users"]
date: "2022-06-17"
draft: true
---

# Airflow User Survey 2022

This year’s survey has come and gone, and with it we’ve got a new batch of data for everyone! We collected 210 responses over two weeks. We continue to see growth in both contributions and downloads over the last two years, and expect that trend will continue through 2022.

The raw response data is available here for anyone interested in doing additional analysis: [airflow_survey_2022.csv]()

## TL;DR

### Overview of the user

- Like previous years, more than half of the Airflow users are Data Engineers (54%). Solutions Architects (13%), Developers (12%), DevOps (6%) and Data Scientists (4%) are also active Airflow users! There was a slight increase in the representation of Solutions Architect roles compared to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/) .
- Airflow is used and popular in bigger companies, 64% of Airflow users work for companies with 200+ employees which is an 11 percent increase compared to [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user).
- 62% of the survey participants have more than 6 Airflow users in their company.
- More Airflow users (65.9%) are willing to recommend Apache Airflow compared to the survey results in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/). There is a general positive trend in a willingness to recommend Airflow, 93% of surveyed Airflow users are willing to recommend Airflow ( 85.7% in [2019](https://airflow.apache.org/blog/airflow-survey/) and 92% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) ), only 1% of users are not likely to recommend (3.6% in [2019](https://airflow.apache.org/blog/airflow-survey/) and 3.5% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)).
- Airflow documentation is a critical source of information, with more than 90% (15% increase compared to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)) of survey participants using the documentation. Airflow documentation is also one of the top areas to improve! What’s interesting, also Stack Overflow usage is critical, with about 60% users declaring to use it as a source of information (24% increase compared to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)).

### Deployments

- 85% of the Airflow users have between 1 to 7 active Airflow instances. 62.5% of the Airflow users have between 11 to 250 DAGs in their largest Airflow instance. 75% of the surveyed Airflow users have between 1 to 100 tasks per DAG.
- Close to 85% of users use one of the Airflow 2 versions, 9.2% users still use 1.10.15, while the remaining 6.3% are still using olderAirflow 1 versions. The good news is that the majority of users on Airflow 1 are planning migration to Airflow 2 quite soon, with resources and capacity being the main blockers.
- In comparison to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user), more users were interested in monitoring in general and specifically in using tools such as external monitoring services (40.7%, up from 29.6%) and information from metabase (35.7%, up from 25.1%).
- Celery (52.7%) and Kubernetes (39.4%) are the most common executors used.

### Usage

- 81.3% of Airflow users who responded to the survey don’t have any customisation of Airflow.
- Xcom (69.8%) is the most popular method to pass inputs and outputs between tasks, however Saving and Retrieving Inputs and Outputs from Storage still plays an important role (49%).
- Lineage itself is a quite new topic for Airflow users, most of them don’t use lineage solutions but might be interested if supported by Airflow (47.5%), are not familiar with data lineage (29%) or that data lineage is not their concern (13%).
- The Airflow web UI is used heavily for Monitoring Runs (95.9%), Accessing Task Logs (89.8%), Manually triggering DAGs (85.2%), Clearing Tasks (82.7%) and Marking Tasks as successful (60.7%). The top 3 views used are: List of DAGs, Task Logs and DAG Runs, which is very similar to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/).

### Community and contribution

- Most Airflow users (57.1%) are aware they could contribute but do not, and an additional 21.7% contribute very rarely. 14.8% of users were not aware they could contribute. There is much more to be done to engage our community to be more active contributors and raise the current 6.4% of users who actively contribute, especially considering that one important blocker for contribution is lack of knowledge on how to start (37.7%).

### The future of Airflow

- The top area for improvement is still the Airflow web UI (49.5%), closely followed by more telemetry for logging, monitoring and alerting purposes (48%). However all those efforts should go in line with improved documentation (36.6.%) and resources about using the Airflow, especially when we take into account the need of onboarding new users (36.6%).
- DAG Versioning(66.2%) is a winner for new features in Airflow, and it’s not a surprise as this feature may positively impact daily work of Airflow users. It is followed by three other ideas: Dependency management and Data-driven scheduling (42.6%), More dynamic task structure (42.1%) and Multi-Tenancy (37.9%).

## Overview of the user

### What best describes your current occupation? (single choice)

![alt_text](images/image1.png "user_occupations")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Data Engineer
   </td>
   <td><p style="text-align: right">
114</p>

   </td>
   <td><p style="text-align: right">
54%</p>

   </td>
  </tr>
  <tr>
   <td>Solutions Architect
   </td>
   <td><p style="text-align: right">
27</p>

   </td>
   <td><p style="text-align: right">
13%</p>

   </td>
  </tr>
  <tr>
   <td>Developer
   </td>
   <td><p style="text-align: right">
25</p>

   </td>
   <td><p style="text-align: right">
12%</p>

   </td>
  </tr>
  <tr>
   <td>DevOps
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
6%</p>

   </td>
  </tr>
  <tr>
   <td>Data Scientist
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
4%</p>

   </td>
  </tr>
  <tr>
   <td>Support Engineer
   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td><p style="text-align: right">
2%</p>

   </td>
  </tr>
  <tr>
   <td>Data Analyst
   </td>
   <td><p style="text-align: right">
3</p>

   </td>
   <td><p style="text-align: right">
1%</p>

   </td>
  </tr>
  <tr>
   <td>Business Analyst
   </td>
   <td><p style="text-align: right">
2</p>

   </td>
   <td><p style="text-align: right">
1%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td><p style="text-align: right">
7%</p>

   </td>
  </tr>
</table>

According to the survey, more than half of Airflow users are Data Engineers (54%). Roles of the remaining Airflow users might be broken down into Solutions Architects (13%), Developers (12%), DevOps (6%) and Data Scientists (4%). The 2022 results are similar to [those from 2019](https://airflow.apache.org/blog/airflow-survey/) and [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) with a slight increase in the representation of Solutions Architect roles.

### How often do you interact with Airflow? (single choice)

![alt_text](images/image2.png "interaction_frequency")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No. </p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Every day
   </td>
   <td><p style="text-align: right">
154</p>

   </td>
   <td><p style="text-align: right">
73%</p>

   </td>
  </tr>
  <tr>
   <td>At least once per week
   </td>
   <td><p style="text-align: right">
36</p>

   </td>
   <td><p style="text-align: right">
17%</p>

   </td>
  </tr>
  <tr>
   <td>At least once per month
   </td>
   <td><p style="text-align: right">
11</p>

   </td>
   <td><p style="text-align: right">
5%</p>

   </td>
  </tr>
  <tr>
   <td>Less than once per month
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4%</p>

   </td>
  </tr>
</table>

Users who took the survey are actively using Airflow as part of their current role. 73% of Airflow users who responded use it on a daily basis, 17% weekly.

### How many people work at your company? (single choice)

![alt_text](images/image3.png "company_size")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>201-5000
   </td>
   <td><p style="text-align: right">
85</p>

   </td>
   <td><p style="text-align: right">
41%</p>

   </td>
  </tr>
  <tr>
   <td>5000+
   </td>
   <td><p style="text-align: right">
49</p>

   </td>
   <td><p style="text-align: right">
23%</p>

   </td>
  </tr>
  <tr>
   <td>51-200
   </td>
   <td><p style="text-align: right">
46</p>

   </td>
   <td><p style="text-align: right">
22%</p>

   </td>
  </tr>
  <tr>
   <td>11-50
   </td>
   <td><p style="text-align: right">
20</p>

   </td>
   <td><p style="text-align: right">
10%</p>

   </td>
  </tr>
  <tr>
   <td>1-10
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4%</p>

   </td>
  </tr>
</table>

Airflow is a framework that is used and popular in bigger companies, 64% of Airflow users who responded (compared to 52.7% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)) work for companies bigger than 200 employees (41% in companies size 201-5000 and 23% in companies size 5000+).

### How many people at your company use Airflow? (single choice)

![alt_text](images/image4.png "airflow_usage")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>6-20
   </td>
   <td><p style="text-align: right">
80</p>

   </td>
   <td><p style="text-align: right">
38%</p>

   </td>
  </tr>
  <tr>
   <td>1-5
   </td>
   <td><p style="text-align: right">
61</p>

   </td>
   <td><p style="text-align: right">
29%</p>

   </td>
  </tr>
  <tr>
   <td>51-200
   </td>
   <td><p style="text-align: right">
49</p>

   </td>
   <td><p style="text-align: right">
24%</p>

   </td>
  </tr>
  <tr>
   <td>200+
   </td>
   <td><p style="text-align: right">
18</p>

   </td>
   <td><p style="text-align: right">
9%</p>

   </td>
  </tr>
</table>

Airflow is generally used by small to medium-sized teams. 62% of the survey participants have more than 6 Airflow users in their company (38% have between 6 and 200 users, 24% between 51-200 users).

### How likely are you to recommend Apache Airflow? (single choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
% 2019</p>

   </td>
   <td><p style="text-align: right">
% 2020</p>

   </td>
   <td><p style="text-align: right">
% 2022</p>

   </td>
  </tr>
  <tr>
   <td>Very Likely
   </td>
   <td><p style="text-align: right">
45.4%</p>

   </td>
   <td><p style="text-align: right">
61.6%</p>

   </td>
   <td><p style="text-align: right">
65.9%</p>

   </td>
  </tr>
  <tr>
   <td>Likely
   </td>
   <td><p style="text-align: right">
40.3%</p>

   </td>
   <td><p style="text-align: right">
30.4%</p>

   </td>
   <td><p style="text-align: right">
26.9%</p>

   </td>
  </tr>
  <tr>
   <td>Neutral
   </td>
   <td><p style="text-align: right">
10.7%</p>

   </td>
   <td><p style="text-align: right">
5.4%</p>

   </td>
   <td><p style="text-align: right">
6.3%</p>

   </td>
  </tr>
  <tr>
   <td>Unlikely
   </td>
   <td><p style="text-align: right">
2.6%</p>

   </td>
   <td><p style="text-align: right">
1.5%</p>

   </td>
   <td><p style="text-align: right">
0.5%</p>

   </td>
  </tr>
  <tr>
   <td>Very Unlikely
   </td>
   <td><p style="text-align: right">
1%</p>

   </td>
   <td><p style="text-align: right">
1%</p>

   </td>
   <td><p style="text-align: right">
0.5%</p>

   </td>
  </tr>
</table>

According to the survey, more Airflow users (65.9%) are willing to recommend Apache Airflow compared to the survey results in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/). There is a general positive trend in a willingness to recommend Airflow, 93% of surveyed Airflow users are willing to recommend Airflow (92% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and 85.7% in [2019](https://airflow.apache.org/blog/airflow-survey/)), only 1% of users are not likely to recommend (3.6% in [2019](https://airflow.apache.org/blog/airflow-survey/) and 3.5% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) ).

### What is your source of information about Airflow? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Documentation
   </td>
   <td><p style="text-align: right">
189</p>

   </td>
   <td><p style="text-align: right">
90.4%</p>

   </td>
  </tr>
  <tr>
   <td>Airflow website (Blog, etc.)
   </td>
   <td><p style="text-align: right">
142</p>

   </td>
   <td><p style="text-align: right">
67.9%</p>

   </td>
  </tr>
  <tr>
   <td>Stack Overflow
   </td>
   <td><p style="text-align: right">
126</p>

   </td>
   <td><p style="text-align: right">
60.3%</p>

   </td>
  </tr>
  <tr>
   <td>Github Issues
   </td>
   <td><p style="text-align: right">
104</p>

   </td>
   <td><p style="text-align: right">
49.8%</p>

   </td>
  </tr>
  <tr>
   <td>Slack
   </td>
   <td><p style="text-align: right">
96</p>

   </td>
   <td><p style="text-align: right">
45.9%</p>

   </td>
  </tr>
  <tr>
   <td>Airflow Summit Videos
   </td>
   <td><p style="text-align: right">
88</p>

   </td>
   <td><p style="text-align: right">
42.1%</p>

   </td>
  </tr>
  <tr>
   <td>GitHub Discussions
   </td>
   <td><p style="text-align: right">
76</p>

   </td>
   <td><p style="text-align: right">
36.4%</p>

   </td>
  </tr>
  <tr>
   <td>Airflow Community Webinars
   </td>
   <td><p style="text-align: right">
41</p>

   </td>
   <td><p style="text-align: right">
19.6%</p>

   </td>
  </tr>
  <tr>
   <td>Astronomer Registry
   </td>
   <td><p style="text-align: right">
51</p>

   </td>
   <td><p style="text-align: right">
24.4%</p>

   </td>
  </tr>
  <tr>
   <td>Airflow Mailing List
   </td>
   <td><p style="text-align: right">
34</p>

   </td>
   <td><p style="text-align: right">
16.3%</p>

   </td>
  </tr>
</table>

Airflow documentation is a critical source of information, with more than 90% of survey participants using the documentation. It is of increasing importance compared to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) where documentation was at about 75% level. Moreover, more than 60% of users are getting information from the Airflow website (67.9% ) and Stack Overflow (60.3%) which is also a big increase compared to 36% level in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user). What’s interesting is that Slack usage decreased from 63.05% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) to 45.9% in 2022.

## Deployments

### How many active DAGs do you have in your largest Airflow instance? (single choice)

![alt_text](images/image5.png "active_dags")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>51-250
   </td>
   <td><p style="text-align: right">
66</p>

   </td>
   <td><p style="text-align: right">
31.7%</p>

   </td>
  </tr>
  <tr>
   <td>11-50
   </td>
   <td><p style="text-align: right">
64</p>

   </td>
   <td><p style="text-align: right">
30.8%</p>

   </td>
  </tr>
  <tr>
   <td>5-10
   </td>
   <td><p style="text-align: right">
25</p>

   </td>
   <td><p style="text-align: right">
12.0%</p>

   </td>
  </tr>
  <tr>
   <td>251-500
   </td>
   <td><p style="text-align: right">
20</p>

   </td>
   <td><p style="text-align: right">
9.6%</p>

   </td>
  </tr>
  <tr>
   <td>&lt;5
   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td><p style="text-align: right">
6.7%</p>

   </td>
  </tr>
  <tr>
   <td>1000+
   </td>
   <td><p style="text-align: right">
10</p>

   </td>
   <td><p style="text-align: right">
4.8%</p>

   </td>
  </tr>
  <tr>
   <td>501-1000
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4.3%</p>

   </td>
  </tr>
</table>

62.5% of the Airflow users surveyed have between 11 to 250 DAGs in their largest Airflow instance.

### How many active Airflow instances do you have? (single choice)

![alt_text](images/image6.png "image_tooltip")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><p style="text-align: right">
52</p>

   </td>
   <td><p style="text-align: right">
25.2%</p>

   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td><p style="text-align: right">
46</p>

   </td>
   <td><p style="text-align: right">
22.3%</p>

   </td>
  </tr>
  <tr>
   <td>4-7
   </td>
   <td><p style="text-align: right">
40</p>

   </td>
   <td><p style="text-align: right">
19.4%</p>

   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><p style="text-align: right">
37</p>

   </td>
   <td><p style="text-align: right">
18.0%</p>

   </td>
  </tr>
  <tr>
   <td>20+
   </td>
   <td><p style="text-align: right">
19</p>

   </td>
   <td><p style="text-align: right">
9.2%</p>

   </td>
  </tr>
  <tr>
   <td>8-10
   </td>
   <td><p style="text-align: right">
7</p>

   </td>
   <td><p style="text-align: right">
3.4%</p>

   </td>
  </tr>
  <tr>
   <td>11-20
   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td><p style="text-align: right">
2.4%</p>

   </td>
  </tr>
</table>

85% of the Airflow users surveyed have between 1 and 7 active Airflow instances, and nearly 50% have only 1 or 2.

### What is the maximum number of tasks that you have used in a single DAG?(single choice)

![alt_text](images/image7.png "maximum tasks")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>11-25
   </td>
   <td><p style="text-align: right">
51</p>

   </td>
   <td><p style="text-align: right">
24.5%</p>

   </td>
  </tr>
  <tr>
   <td>26-50
   </td>
   <td><p style="text-align: right">
41</p>

   </td>
   <td><p style="text-align: right">
19.7%</p>

   </td>
  </tr>
  <tr>
   <td>51-100
   </td>
   <td><p style="text-align: right">
35</p>

   </td>
   <td><p style="text-align: right">
16.8%</p>

   </td>
  </tr>
  <tr>
   <td>&lt;10
   </td>
   <td><p style="text-align: right">
29</p>

   </td>
   <td><p style="text-align: right">
13.9%</p>

   </td>
  </tr>
  <tr>
   <td>101-250
   </td>
   <td><p style="text-align: right">
23</p>

   </td>
   <td><p style="text-align: right">
11.1%</p>

   </td>
  </tr>
  <tr>
   <td>501-1000
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4.3%</p>

   </td>
  </tr>
  <tr>
   <td>1000-2500
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
3.8%</p>

   </td>
  </tr>
  <tr>
   <td>251-500
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
3.8%</p>

   </td>
  </tr>
  <tr>
   <td>2500-5000
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
1.9%</p>

   </td>
  </tr>
</table>

75% of the surveyed Airflow users have between 1 and 100 tasks per DAG.

### How many schedulers do you have in your largest Airflow instance? (single choice)

![alt_text](images/image8.png "max_schedulers")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><p style="text-align: right">
113</p>

   </td>
   <td><p style="text-align: right">
55.1%</p>

   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td><p style="text-align: right">
61</p>

   </td>
   <td><p style="text-align: right">
29.8%</p>

   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td><p style="text-align: right">
18</p>

   </td>
   <td><p style="text-align: right">
8.8%</p>

   </td>
  </tr>
  <tr>
   <td>4+
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.3%</p>

   </td>
  </tr>
</table>

More than half of Airflow users who responded to the survey have 1 scheduler in their largest Airflow instance, however it’s important to notice that the second half of Airflow users decided to have 2 schedulers and more.

### What executor type do you use? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
% 2022</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Celery</p>

   </td>
   <td><p style="text-align: right">
52.7 %</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Kubernetes</p>

   </td>
   <td><p style="text-align: right">
39.4%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Local</p>

   </td>
   <td><p style="text-align: right">
24.1%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Sequential</p>

   </td>
   <td><p style="text-align: right">
10.3%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
CeleryKubernetes </p>

   </td>
   <td><p style="text-align: right">
6.9%</p>

   </td>
  </tr>
</table>

Celery (52.7%) and Kubernetes (39.4%) are the most common executors used. CeleryKubernetes (6.9%) executor also started to be noticed and used by Airflow users.

### If you use the Celery executor, how many workers do you have in your largest Airflow instance? (single choice)

![alt_text](images/image9.png "max_workers")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>2-5
   </td>
   <td><p style="text-align: right">
64</p>

   </td>
   <td><p style="text-align: right">
44.8%</p>

   </td>
  </tr>
  <tr>
   <td>10+
   </td>
   <td><p style="text-align: right">
28</p>

   </td>
   <td><p style="text-align: right">
19.6%</p>

   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td><p style="text-align: right">
26</p>

   </td>
   <td><p style="text-align: right">
18.2%</p>

   </td>
  </tr>
  <tr>
   <td>6-10
   </td>
   <td><p style="text-align: right">
25</p>

   </td>
   <td><p style="text-align: right">
17.5%</p>

   </td>
  </tr>
</table>

Amongst Celery executor users who responded to the survey, close to half the number (44.8%) have between 2 to 5 workers in their largest Airflow instance. It’s notable that nearly a fifth (19.6%) have more than 10 workers.

### Which version of Airflow do you currently use? (single choice)

![alt_text](images/image10.png "airflow_version")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>1.10.14 or older
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.3%</p>

   </td>
  </tr>
  <tr>
   <td>1.10.15
   </td>
   <td><p style="text-align: right">
19</p>

   </td>
   <td><p style="text-align: right">
9.2%</p>

   </td>
  </tr>
  <tr>
   <td>2.0.x
   </td>
   <td><p style="text-align: right">
23</p>

   </td>
   <td><p style="text-align: right">
11.1%</p>

   </td>
  </tr>
  <tr>
   <td>2.1.x
   </td>
   <td><p style="text-align: right">
24</p>

   </td>
   <td><p style="text-align: right">
11.6%</p>

   </td>
  </tr>
  <tr>
   <td>2.2.x
   </td>
   <td><p style="text-align: right">
79</p>

   </td>
   <td><p style="text-align: right">
38.2%</p>

   </td>
  </tr>
  <tr>
   <td>2.3.x
   </td>
   <td><p style="text-align: right">
49</p>

   </td>
   <td><p style="text-align: right">
23.7%</p>

   </td>
  </tr>
</table>

It's good to see that close to 85% of users who responded to the survey use one of the Airflow 2 versions, 9.2% users still use 1.10.15, while the remaining 6.3% are still using older Airflow 1.10 versions.

The good news is that the majority of users on Airflow 1 are planning migration to Airflow 2 quite soon, as for now they have capacity constraints to undertake such a significant effort in their opinion. However, it can also be noticed in the survey’s comments that some users are generally skeptical towards migration to Airflow 2, they have negative opinions about the new scheduler or compatibility with the helm chart.

As to plans about migration to the newest version of Airflow 2, users who responded to the survey are committed and waiting especially for the features related to dynamic DAGs. However, some users also reported that they are waiting to solve some dependencies they have or they prefer to wait a little bit more for the community to test the new version before they decide to move on.

### What metrics do you use to monitor Airflow? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>External monitoring service
   </td>
   <td><p style="text-align: right">
81</p>

   </td>
   <td><p style="text-align: right">
40.7%</p>

   </td>
  </tr>
  <tr>
   <td>Information from metadatabase
   </td>
   <td><p style="text-align: right">
71</p>

   </td>
   <td><p style="text-align: right">
35.7%</p>

   </td>
  </tr>
  <tr>
   <td>Statsd
   </td>
   <td><p style="text-align: right">
54</p>

   </td>
   <td><p style="text-align: right">
27.1%</p>

   </td>
  </tr>
  <tr>
   <td>I do not use monitoring
   </td>
   <td><p style="text-align: right">
47</p>

   </td>
   <td><p style="text-align: right">
23.6%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td><p style="text-align: right">
7%</p>

   </td>
  </tr>
</table>

In comparison to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user), more users are monitoring airflow in some way. External monitoring services (40.7%) and information from metabase (35.7%) started to play a more important role in Airflow monitoring.

How do you deploy Airflow? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>On virtual machines (for example using AWS EC2)
   </td>
   <td><p style="text-align: right">
63</p>

   </td>
   <td><p style="text-align: right">
30.6 %</p>

   </td>
  </tr>
  <tr>
   <td>Using a managed service like Astronomer, Google Composer or AWS MWAA
   </td>
   <td><p style="text-align: right">
54</p>

   </td>
   <td><p style="text-align: right">
26.2 %</p>

   </td>
  </tr>
  <tr>
   <td>On Kubernetes (using Apache Airflow’s helm chart)
   </td>
   <td><p style="text-align: right">
46</p>

   </td>
   <td><p style="text-align: right">
22.3%</p>

   </td>
  </tr>
  <tr>
   <td>On premises
   </td>
   <td><p style="text-align: right">
43</p>

   </td>
   <td><p style="text-align: right">
20.9%</p>

   </td>
  </tr>
  <tr>
   <td>On Kubernetes (using custom deployments)
   </td>
   <td><p style="text-align: right">
39</p>

   </td>
   <td><p style="text-align: right">
18.9%</p>

   </td>
  </tr>
  <tr>
   <td>On Kubernetes (using another helm chart)
   </td>
   <td><p style="text-align: right">
21</p>

   </td>
   <td><p style="text-align: right">
10.2%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.5%</p>

   </td>
  </tr>
</table>

More than half of Airflow users who responded (51.4%) deploy Airflow on Kubernetes. This is about 20 percent more than in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user). The remaining top deployment methods are on virtual machines (30.6%) and via managed services (26.2%).

### How do you distribute your DAGs from your developer environment to the cloud? (single choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Using a synchronizing process (Git sync, GCS fuse, etc)
   </td>
   <td><p style="text-align: right">
100</p>

   </td>
   <td><p style="text-align: right">
49%</p>

   </td>
  </tr>
  <tr>
   <td>Bake them into the docker image
   </td>
   <td><p style="text-align: right">
51</p>

   </td>
   <td><p style="text-align: right">
25%</p>

   </td>
  </tr>
  <tr>
   <td>Shared files system
   </td>
   <td><p style="text-align: right">
30</p>

   </td>
   <td><p style="text-align: right">
14.7%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
16</p>

   </td>
   <td><p style="text-align: right">
7.9%</p>

   </td>
  </tr>
  <tr>
   <td>I don’t know
   </td>
   <td><p style="text-align: right">
7</p>

   </td>
   <td><p style="text-align: right">
3.4%</p>

   </td>
  </tr>
</table>

According to the survey responses, the most popular way of distributing DAGs is a synchronizing process, about half of Airflow users (49%) use this process to distribute DAGs from developer environments to the cloud.

## Usage

### Do you have any customisation of Airflow? (single choice)

![alt_text](images/image11.png "customization")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>No, we use vanilla airflow
   </td>
   <td><p style="text-align: right">
165</p>

   </td>
   <td><p style="text-align: right">
81.3%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, we have a separate fork
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.4%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, we use a 3rd-party fork
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
5.9%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, we’ve backpropagated bug fixes to an older version
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.4%</p>

   </td>
  </tr>
</table>

More Airflow users (81.3%) don’t have any customisation of Airflow (compared to 75.9% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)). Those Airflow users who have customisations (18.7%) decided to introduce them mainly to separate development and production workflows, to backport bug fixes, due to security fixes or to run a backfill command on Kubernetes pod.

### Which Metadata Database do you use? (single choice)

![alt_text](images/image12.png "database")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%I </p>

   </td>
  </tr>
  <tr>
   <td>PostgreSQL 13
   </td>
   <td><p style="text-align: right">
86</p>

   </td>
   <td><p style="text-align: right">
43.9%</p>

   </td>
  </tr>
  <tr>
   <td>PostgreSQL 12
   </td>
   <td><p style="text-align: right">
74</p>

   </td>
   <td><p style="text-align: right">
37.8%</p>

   </td>
  </tr>
  <tr>
   <td>MySQL 8
   </td>
   <td><p style="text-align: right">
22</p>

   </td>
   <td><p style="text-align: right">
11.2%</p>

   </td>
  </tr>
  <tr>
   <td>MySQL 5
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4.6%</p>

   </td>
  </tr>
  <tr>
   <td>MariaDB
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
2.0%</p>

   </td>
  </tr>
  <tr>
   <td>MsSQL
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5%</p>

   </td>
  </tr>
</table>

According to the survey responses, the most popular metadata databases are PostgreSQL 13 (43.9%) and PostgreSQL 12 (37.8%). This represents a sharp increase from 2020, up from 68.9% to 81.7% total on PostgreSQL, with a corresponding decrease in MySQL, down from 23% to 15%. This is an interesting result taking into account community discussion about not adding support for more database backend or even deciding on single database support.

### What's the primary method by which you integrate with providers and external services in your Airflow DAGs? (single choice)

![alt_text](images/image13.png "providers_interface")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Using existing dedicated operators / hooks
   </td>
   <td><p style="text-align: right">
70</p>

   </td>
   <td><p style="text-align: right">
34.5%</p>

   </td>
  </tr>
  <tr>
   <td>Using Bash/Python operators
   </td>
   <td><p style="text-align: right">
58</p>

   </td>
   <td><p style="text-align: right">
28.6%</p>

   </td>
  </tr>
  <tr>
   <td>Using custom operators / hooks
   </td>
   <td><p style="text-align: right">
50</p>

   </td>
   <td><p style="text-align: right">
24.6%</p>

   </td>
  </tr>
  <tr>
   <td>Using KubernetesPodOperator
   </td>
   <td><p style="text-align: right">
25</p>

   </td>
   <td><p style="text-align: right">
12.3%</p>

   </td>
  </tr>
</table>

According to the survey responses, the following ways of using Airflow to connect to external services are the most popular: Using existing dedicated operators / hooks (34.5%), Using Bash/Python operators (28.6%), Using custom operators / hooks (24.6%). Using KubernetesPodOperator (12.3%) is less popular regarding the survey responses. The integration with providers and external services methods ranking is similar to the one from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user).

What providers do you use in your Airflow DAGs? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Amazon Web Services</p>

   </td>
   <td><p style="text-align: right">
112</p>

   </td>
   <td><p style="text-align: right">
55.4%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Google Cloud Platform / Google APIs</p>

   </td>
   <td><p style="text-align: right">
79</p>

   </td>
   <td><p style="text-align: right">
39.1%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Internal company systems</p>

   </td>
   <td><p style="text-align: right">
75</p>

   </td>
   <td><p style="text-align: right">
37.1%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Hadoop / Spark / Flink / Other Apache software</p>

   </td>
   <td><p style="text-align: right">
57</p>

   </td>
   <td><p style="text-align: right">
28.2%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Microsoft Azure</p>

   </td>
   <td><p style="text-align: right">
17</p>

   </td>
   <td><p style="text-align: right">
8.4%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
Other</p>

   </td>
   <td><p style="text-align: right">
21</p>

   </td>
   <td><p style="text-align: right">
10.5%</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: right">
I do not use external services in my Airflow DAGs</p>

   </td>
   <td><p style="text-align: right">
14</p>

   </td>
   <td><p style="text-align: right">
6.9%</p>

   </td>
  </tr>
</table>

It’s not surprising that Amazon Web Services (55.4% vs 59.6% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)), on the next three positions Google Cloud Platform (39.1% vs 47.7% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/) ), Internal company systems (37.1% vs 55.6% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)), and other Apache products (28.2% vs 35.47% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)) are leading Airflow providers.

<table>
  <tr>
   <td><strong>No.</strong>
   </td>
   <td><strong>%</strong>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>Amazon Web Services
   </td>
   <td>121
   </td>
   <td>59.61
   </td>
  </tr>
  <tr>
   <td>Internal company systems
   </td>
   <td>113
   </td>
   <td>55.67
   </td>
  </tr>
  <tr>
   <td>Google Cloud Platform / Google APIs
   </td>
   <td>97
   </td>
   <td>47.78
   </td>
  </tr>
  <tr>
   <td>Hadoop / Spark / Flink / Other Apache software
   </td>
   <td>72
   </td>
   <td>35.47
   </td>
  </tr>
  <tr>
   <td>Microsoft Azure
   </td>
   <td>21
   </td>
   <td>10.34
   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td>19
   </td>
   <td>9.36
   </td>
  </tr>
  <tr>
   <td>I do not use external services in my Airflow DAGs
   </td>
   <td>5
   </td>
   <td>2.46
   </td>
  </tr>
</table>

### How frequently do you upgrade Airflow environments? (single choice)

![alt_text](images/image14.png "upgrade_frequency")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>every 12 months
   </td>
   <td><p style="text-align: right">
46</p>

   </td>
   <td><p style="text-align: right">
22.9%</p>

   </td>
  </tr>
  <tr>
   <td>every 6 months
   </td>
   <td><p style="text-align: right">
49</p>

   </td>
   <td><p style="text-align: right">
24.4%</p>

   </td>
  </tr>
  <tr>
   <td>once a quarter
   </td>
   <td><p style="text-align: right">
47</p>

   </td>
   <td><p style="text-align: right">
23.4%</p>

   </td>
  </tr>
  <tr>
   <td>Whenever there is a newer version
   </td>
   <td><p style="text-align: right">
59</p>

   </td>
   <td><p style="text-align: right">
29.4%</p>

   </td>
  </tr>
</table>

Different frequencies of Airflow environments upgrades are almost equally popular amongst Airflow users who responded to the survey.

### Do you upgrade providers separately from the core? (single choice)

![alt_text](images/image15.png "providers_upgrade")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>When I need it
   </td>
   <td><p style="text-align: right">
83</p>

   </td>
   <td><p style="text-align: right">
42.8%</p>

   </td>
  </tr>
  <tr>
   <td>Never - always use the providers that come with Airflow
   </td>
   <td><p style="text-align: right">
68</p>

   </td>
   <td><p style="text-align: right">
35.1%</p>

   </td>
  </tr>
  <tr>
   <td>I did not know I can upgrade providers separately
   </td>
   <td><p style="text-align: right">
32</p>

   </td>
   <td><p style="text-align: right">
16.5%</p>

   </td>
  </tr>
  <tr>
   <td>I upgrade providers when they are released
   </td>
   <td><p style="text-align: right">
11</p>

   </td>
   <td><p style="text-align: right">
5.7%</p>

   </td>
  </tr>
</table>

According to the survey responses, Airflow users most often upgrade providers when they need it (42.8%) or prefer to stay with providers that come with Airflow (35.1%). It’s surprising that 16.5% of Airflow users who responded to the survey were not aware that they can upgrade their providers separately from the core Airflow.

### How do you pass inputs and outputs between tasks? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Xcom
   </td>
   <td><p style="text-align: right">
141</p>

   </td>
   <td><p style="text-align: right">
69.8%</p>

   </td>
  </tr>
  <tr>
   <td>Saving and retrieving from Storage 
   </td>
   <td><p style="text-align: right">
99</p>

   </td>
   <td><p style="text-align: right">
49%</p>

   </td>
  </tr>
  <tr>
   <td>TaskFlow
   </td>
   <td><p style="text-align: right">
37</p>

   </td>
   <td><p style="text-align: right">
18.3%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
5</p>

   </td>
   <td><p style="text-align: right">
2.5%</p>

   </td>
  </tr>
  <tr>
   <td>We don’t
   </td>
   <td><p style="text-align: right">
29</p>

   </td>
   <td><p style="text-align: right">
14.4%</p>

   </td>
  </tr>
</table>

According to the survey responses, Xcom (69.8%) is the most popular method to pass inputs and outputs between tasks, however Saving and Retrieving Inputs and Outputs from Storage still plays an important role (49%). It’s interesting that close to 15% of Airflow users who responded to the survey declare to not pass any outputs or inputs between tasks.

### Do you use a data lineage backend? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>No, but I will use such feature if fully supported in Airflow
   </td>
   <td><p style="text-align: right">
95</p>

   </td>
   <td><p style="text-align: right">
47.5%</p>

   </td>
  </tr>
  <tr>
   <td>I’m not familiar with data lineage
   </td>
   <td><p style="text-align: right">
58</p>

   </td>
   <td><p style="text-align: right">
29%</p>

   </td>
  </tr>
  <tr>
   <td>No, data lineage isn’t a concern for my usage
   </td>
   <td><p style="text-align: right">
26</p>

   </td>
   <td><p style="text-align: right">
13%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, I send lineage to an Open Source lineage repository
   </td>
   <td><p style="text-align: right">
15</p>

   </td>
   <td><p style="text-align: right">
7.5%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, I send lineage to an Enterprise lineage repository
   </td>
   <td><p style="text-align: right">
7</p>

   </td>
   <td><p style="text-align: right">
3.5%</p>

   </td>
  </tr>
  <tr>
   <td>Yes, I send lineage to a custom internal lineage repository
   </td>
   <td><p style="text-align: right">
9</p>

   </td>
   <td><p style="text-align: right">
4.5%</p>

   </td>
  </tr>
</table>

When asked what lineage backend Airflow users use, the answers indicated that, while lineage itself is a quite new topic, there is interest in the feature as a whole. Most Airflow users responded that they don’t use lineage solutions currently but might be interested in the future if supported by Airflow (47.5%), are not familiar with data lineage (29%) or that data lineage is not their concern (13%).

### Which interfaces of Airflow do you use as part of your current role? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Original Airflow Graphical User Interface
   </td>
   <td><p style="text-align: right">
189</p>

   </td>
   <td><p style="text-align: right">
94%</p>

   </td>
  </tr>
  <tr>
   <td>CLI
   </td>
   <td><p style="text-align: right">
98</p>

   </td>
   <td><p style="text-align: right">
48.8%</p>

   </td>
  </tr>
  <tr>
   <td>API
   </td>
   <td><p style="text-align: right">
80</p>

   </td>
   <td><p style="text-align: right">
39.8%</p>

   </td>
  </tr>
  <tr>
   <td>Custom (own created) Airflow Graphical User Interface
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
6%</p>

   </td>
  </tr>
  <tr>
   <td>GCP Composer 
   </td>
   <td><p style="text-align: right">
1</p>

   </td>
   <td><p style="text-align: right">
0.5%</p>

   </td>
  </tr>
</table>

It’s clear that usage of Airflow web UI is important as 94% of users who responded to the survey declare to use it as a part of their current role. Usage of CLI (48.8%) and API (39.8%) goes in pairs but are not so common compared to Airflow web UI usage.

### (If GUI Marked) What do you use the GUI for? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Monitoring Runs
   </td>
   <td><p style="text-align: right">
188</p>

   </td>
   <td><p style="text-align: right">
95.9%</p>

   </td>
  </tr>
  <tr>
   <td>Accessing Task Logs
   </td>
   <td><p style="text-align: right">
176</p>

   </td>
   <td><p style="text-align: right">
89.8%</p>

   </td>
  </tr>
  <tr>
   <td>Manually triggering DAGs
   </td>
   <td><p style="text-align: right">
167</p>

   </td>
   <td><p style="text-align: right">
85.2%</p>

   </td>
  </tr>
  <tr>
   <td>Clearing Tasks
   </td>
   <td><p style="text-align: right">
162</p>

   </td>
   <td><p style="text-align: right">
82.7%</p>

   </td>
  </tr>
  <tr>
   <td>Marking Tasks as successful
   </td>
   <td><p style="text-align: right">
119</p>

   </td>
   <td><p style="text-align: right">
60.7%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
6</p>

   </td>
   <td><p style="text-align: right">
3%</p>

   </td>
  </tr>
</table>

Airflow web UI is used heavily for monitoring: Monitoring Runs (95.9%) and troubleshooting: Accessing Task Logs (89.8%), Manually triggering DAGs (85.2%), Clearing Tasks (82.7%) and Marking Tasks as successful (60.7%).

### (if CLI Marked) What do you use the CLI For? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Backfilling
   </td>
   <td><p style="text-align: right">
63</p>

   </td>
   <td><p style="text-align: right">
56.8%</p>

   </td>
  </tr>
  <tr>
   <td>Manually triggering DAGs
   </td>
   <td><p style="text-align: right">
52</p>

   </td>
   <td><p style="text-align: right">
46.8%</p>

   </td>
  </tr>
  <tr>
   <td>Clearing Tasks
   </td>
   <td><p style="text-align: right">
26</p>

   </td>
   <td><p style="text-align: right">
23.4%</p>

   </td>
  </tr>
  <tr>
   <td>Monitoring Runs
   </td>
   <td><p style="text-align: right">
25</p>

   </td>
   <td><p style="text-align: right">
22.5%</p>

   </td>
  </tr>
  <tr>
   <td>Accessing Task Logs
   </td>
   <td><p style="text-align: right">
21</p>

   </td>
   <td><p style="text-align: right">
18.9%</p>

   </td>
  </tr>
  <tr>
   <td>Marking Tasks as successful
   </td>
   <td><p style="text-align: right">
11</p>

   </td>
   <td><p style="text-align: right">
9.9%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
17</p>

   </td>
   <td><p style="text-align: right">
15.3%</p>

   </td>
  </tr>
</table>

Compared to Airflow web UI, Airflow CLI is used mainly for Backfilling (56.8%) and Manually triggering DAGs (46.8%).

### In Airflow, which UI views are important for you? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>List of DAGs
   </td>
   <td><p style="text-align: right">
178</p>

   </td>
   <td><p style="text-align: right">
89.4%</p>

   </td>
  </tr>
  <tr>
   <td>Task Logs
   </td>
   <td><p style="text-align: right">
162</p>

   </td>
   <td><p style="text-align: right">
81.4%</p>

   </td>
  </tr>
  <tr>
   <td>DAG Runs
   </td>
   <td><p style="text-align: right">
160</p>

   </td>
   <td><p style="text-align: right">
80.4%</p>

   </td>
  </tr>
  <tr>
   <td>Graph view
   </td>
   <td><p style="text-align: right">
147</p>

   </td>
   <td><p style="text-align: right">
73.9%</p>

   </td>
  </tr>
  <tr>
   <td>Grid/Tree View
   </td>
   <td><p style="text-align: right">
138</p>

   </td>
   <td><p style="text-align: right">
69.3%</p>

   </td>
  </tr>
  <tr>
   <td>Run Details
   </td>
   <td><p style="text-align: right">
117</p>

   </td>
   <td><p style="text-align: right">
58.8%</p>

   </td>
  </tr>
  <tr>
   <td>DAG details
   </td>
   <td><p style="text-align: right">
111</p>

   </td>
   <td><p style="text-align: right">
55.8%</p>

   </td>
  </tr>
  <tr>
   <td>Task Instances
   </td>
   <td><p style="text-align: right">
102</p>

   </td>
   <td><p style="text-align: right">
51.3%</p>

   </td>
  </tr>
  <tr>
   <td>Task Duration
   </td>
   <td><p style="text-align: right">
91</p>

   </td>
   <td><p style="text-align: right">
45.7%</p>

   </td>
  </tr>
  <tr>
   <td>Code
   </td>
   <td><p style="text-align: right">
90</p>

   </td>
   <td><p style="text-align: right">
45.2%</p>

   </td>
  </tr>
  <tr>
   <td>Task Tries
   </td>
   <td><p style="text-align: right">
60</p>

   </td>
   <td><p style="text-align: right">
30.2%</p>

   </td>
  </tr>
  <tr>
   <td>Gantt
   </td>
   <td><p style="text-align: right">
48</p>

   </td>
   <td><p style="text-align: right">
21.4%</p>

   </td>
  </tr>
  <tr>
   <td>Landing Times
   </td>
   <td><p style="text-align: right">
27</p>

   </td>
   <td><p style="text-align: right">
13.6%</p>

   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
2%</p>

   </td>
  </tr>
</table>

UI views importance ranking shows that the majority Airflow users use Web UI mostly for monitoring and/or troubleshooting purposes, where the top 3 views are List of DAGs (89.4%), Task Logs (81.4%) and DAG Runs (80.4%). The results are very similar to those from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/).

## Community and contribution

### Are you participating in the Airflow community discussions? (single choice)

![alt_text](images/image16.png "discussions_engagement")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>I see them from time to time
   </td>
   <td><p style="text-align: right">
99</p>

   </td>
   <td><p style="text-align: right">
48.3%</p>

   </td>
  </tr>
  <tr>
   <td>I regularly follow what's being discussed but don't participate
   </td>
   <td><p style="text-align: right">
53</p>

   </td>
   <td><p style="text-align: right">
25.9%</p>

   </td>
  </tr>
  <tr>
   <td>I didn't know I could
   </td>
   <td><p style="text-align: right">
41</p>

   </td>
   <td><p style="text-align: right">
20.0%</p>

   </td>
  </tr>
  <tr>
   <td>I actively participate in the discussions
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
5.9%</p>

   </td>
  </tr>
</table>

Most of the Airflow users (48.3%) who responded to the survey participate in the Airflow community discussions only from time to time, 25.9% of users follow discussions but don’t participate and 20% of users were not aware they could actively participate. It clearly means there is much more to be done to engage our community to more active involvement and raise the current 5.9% of users who actively participate in the discussions.

### Do you contribute to Airflow?\*\* \*\*(single choice)

![alt_text](images/image17.png "airflow_contribution")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>I know I can but I do not contribute
   </td>
   <td><p style="text-align: right">
116</p>

   </td>
   <td><p style="text-align: right">
57.1%</p>

   </td>
  </tr>
  <tr>
   <td>Very rarely when it relates to what I need
   </td>
   <td><p style="text-align: right">
44</p>

   </td>
   <td><p style="text-align: right">
21.7%</p>

   </td>
  </tr>
  <tr>
   <td>I do not know I could
   </td>
   <td><p style="text-align: right">
30</p>

   </td>
   <td><p style="text-align: right">
14.8%</p>

   </td>
  </tr>
  <tr>
   <td>I regularly contribute by discussing, reviewing and submitting PR
   </td>
   <td><p style="text-align: right">
13</p>

   </td>
   <td><p style="text-align: right">
6.4%</p>

   </td>
  </tr>
</table>

Results related to the Airflow contribution are very similar to those about participating in the Airflow community discussions. Most of the Airflow users (57.1%) who responded to the survey are aware but do not contribute or contribute very rarely (21.7%). 14.8% of users were not aware they could contribute. Once again, it’s a clear indicator that there is much more to be done to engage our community to be more active contributors and raise the current 6.4% of users who actively contribute.

### If you do not contribute - why?

![alt_text](images/image18.png "contribution_reasons")

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>I have no time to contribute even if would like to
   </td>
   <td><p style="text-align: right">
65</p>

   </td>
   <td><p style="text-align: right">
38.9%</p>

   </td>
  </tr>
  <tr>
   <td>I don’t know how to start
   </td>
   <td><p style="text-align: right">
63</p>

   </td>
   <td><p style="text-align: right">
37.7%</p>

   </td>
  </tr>
  <tr>
   <td>I don’t have a need to contribute
   </td>
   <td><p style="text-align: right">
19</p>

   </td>
   <td><p style="text-align: right">
11.4%</p>

   </td>
  </tr>
  <tr>
   <td>I didn’t know I could
   </td>
   <td><p style="text-align: right">
12</p>

   </td>
   <td><p style="text-align: right">
7.2%</p>

   </td>
  </tr>
  <tr>
   <td>My employer has policy that makes it difficult to contribute
   </td>
   <td><p style="text-align: right">
8</p>

   </td>
   <td><p style="text-align: right">
4.8%</p>

   </td>
  </tr>
</table>

According to the survey results, the most important blocker for the Airflow contribution is limited time (38.9%), but surprisingly interesting and important blocker is also lack of knowledge on how to start (37.7%), followed by lack of knowledge that it’s possible to contribute (7.2%).

## The future of Airflow

### In your opinion, what could be improved in Airflow? (multiple choice)

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>Web UI
   </td>
   <td><p style="text-align: right">
100</p>

   </td>
   <td><p style="text-align: right">
49.5%</p>

   </td>
  </tr>
  <tr>
   <td>Logging, monitoring and alerting
   </td>
   <td><p style="text-align: right">
97</p>

   </td>
   <td><p style="text-align: right">
48.0%</p>

   </td>
  </tr>
  <tr>
   <td>Examples, how-to, onboarding documentation
   </td>
   <td><p style="text-align: right">
74</p>

   </td>
   <td><p style="text-align: right">
36.6%</p>

   </td>
  </tr>
  <tr>
   <td>Technical documentation
   </td>
   <td><p style="text-align: right">
74</p>

   </td>
   <td><p style="text-align: right">
36.6%</p>

   </td>
  </tr>
  <tr>
   <td>Scheduler performance
   </td>
   <td><p style="text-align: right">
56</p>

   </td>
   <td><p style="text-align: right">
27.7%</p>

   </td>
  </tr>
  <tr>
   <td>Reliability
   </td>
   <td><p style="text-align: right">
52</p>

   </td>
   <td><p style="text-align: right">
25.7%</p>

   </td>
  </tr>
  <tr>
   <td>DAG authoring
   </td>
   <td><p style="text-align: right">
48</p>

   </td>
   <td><p style="text-align: right">
23.8%</p>

   </td>
  </tr>
  <tr>
   <td>REST API
   </td>
   <td><p style="text-align: right">
43</p>

   </td>
   <td><p style="text-align: right">
21.3%</p>

   </td>
  </tr>
  <tr>
   <td>Authentication and authorization
   </td>
   <td><p style="text-align: right">
41</p>

   </td>
   <td><p style="text-align: right">
20.3%</p>

   </td>
  </tr>
  <tr>
   <td>External integration e.g. AWS, GCP, Apache products
   </td>
   <td><p style="text-align: right">
41</p>

   </td>
   <td><p style="text-align: right">
20.3%</p>

   </td>
  </tr>
  <tr>
   <td>Better support for various deployments (Docker-compose/Nomad/Others)
   </td>
   <td><p style="text-align: right">
39</p>

   </td>
   <td><p style="text-align: right">
19.3%</p>

   </td>
  </tr>
  <tr>
   <td>Everything works fine for me
   </td>
   <td><p style="text-align: right">
19</p>

   </td>
   <td><p style="text-align: right">
9.4%</p>

   </td>
  </tr>
  <tr>
   <td>I don’t know
   </td>
   <td><p style="text-align: right">
4</p>

   </td>
   <td><p style="text-align: right">
2.0%</p>

   </td>
  </tr>
</table>

The results are quite self-explanatory. According to the survey results, the top area for improvement is still the Airflow web UI (49.5%), closely followed by more telemetry for logging, monitoring and alerting purposes (48%). However all those efforts should go in line with improved documentation (36.6.%) and resources about using the Airflow, especially when we take into account the need of onboarding new users (36.6%).

### Which features would you like to see in Airflow?

<table>
  <tr>
   <td>
   </td>
   <td><p style="text-align: right">
No.</p>

   </td>
   <td><p style="text-align: right">
%</p>

   </td>
  </tr>
  <tr>
   <td>DAG Versioning
   </td>
   <td><p style="text-align: right">
129</p>

   </td>
   <td><p style="text-align: right">
66.2%</p>

   </td>
  </tr>
  <tr>
   <td>Dependency management and Data-driven scheduling
   </td>
   <td><p style="text-align: right">
83</p>

   </td>
   <td><p style="text-align: right">
42.6%</p>

   </td>
  </tr>
  <tr>
   <td>More dynamic task structure
   </td>
   <td><p style="text-align: right">
82</p>

   </td>
   <td><p style="text-align: right">
42.1%</p>

   </td>
  </tr>
  <tr>
   <td>Multi-Tenancy
   </td>
   <td><p style="text-align: right">
74</p>

   </td>
   <td><p style="text-align: right">
37.9%</p>

   </td>
  </tr>
  <tr>
   <td>Signal-based scheduling
   </td>
   <td><p style="text-align: right">
67</p>

   </td>
   <td><p style="text-align: right">
34.4%</p>

   </td>
  </tr>
  <tr>
   <td>Better Security (Isolation)
   </td>
   <td><p style="text-align: right">
65</p>

   </td>
   <td><p style="text-align: right">
33.3%</p>

   </td>
  </tr>
  <tr>
   <td>Submitting new DAGs externally via API
   </td>
   <td><p style="text-align: right">
53</p>

   </td>
   <td><p style="text-align: right">
27.2%</p>

   </td>
  </tr>
  <tr>
   <td>Composable Operators
   </td>
   <td><p style="text-align: right">
46</p>

   </td>
   <td><p style="text-align: right">
23.6%</p>

   </td>
  </tr>
  <tr>
   <td>Support for native cloud executors (AWS/GCP/Azure etc.)
   </td>
   <td><p style="text-align: right">
44</p>

   </td>
   <td><p style="text-align: right">
22.6%</p>

   </td>
  </tr>
  <tr>
   <td>Better support for Machine Learning
   </td>
   <td><p style="text-align: right">
38</p>

   </td>
   <td><p style="text-align: right">
19.5%</p>

   </td>
  </tr>
  <tr>
   <td>Remote CLI
   </td>
   <td><p style="text-align: right">
36</p>

   </td>
   <td><p style="text-align: right">
18.5%</p>

   </td>
  </tr>
  <tr>
   <td>Support for hybrid executors
   </td>
   <td><p style="text-align: right">
22</p>

   </td>
   <td><p style="text-align: right">
11.3%</p>

   </td>
  </tr>
</table>

According to the survey results, DAG Versioning is a winner for new features in Airflow, and it’s not a surprise as this feature may positively impact daily work of Airflow users. It is followed by three other ideas: Dependency management and Data-driven scheduling (42.6%), More dynamic task structure (42.1%) and Multi-Tenancy (37.9%). Another interesting point from that question is that only 11.3% think that support for hybrid executors is needed in Airflow.
