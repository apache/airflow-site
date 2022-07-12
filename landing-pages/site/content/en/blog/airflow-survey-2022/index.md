---
title: "Airflow Survey 2022"
linkTitle: "Airflow Survey 2022"
author: "John Thomas, Ewa Tatarczak"
github: "Tohn Jhomas"
linkedin: "john-e-thomas"
description: "2021 saw rapid adoption of Airflow 2, and continued growth of the community. This annual survey helps us understand how people are using Airflow, and where we can best focus our efforts going forward."
tags: ["community", "survey", "users"]
date: "2022-06-17"
---

# Airflow User Survey 2022

This year’s survey has come and gone, and with it we’ve got a new batch of data for everyone! We collected 210 responses over two weeks. We continue to see growth in both contributions and downloads over the last two years, and expect that trend will continue through 2022.

The raw response data will be made available here soon, in the meantime, feel free to email john.thomas@astronomer.io for a copy.

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

|                     |     |     |
| ------------------- | --- | --- |
|                     | No. | %   |
| Data Engineer       | 114 | 54% |
| Solutions Architect | 27  | 13% |
| Developer           | 25  | 12% |
| DevOps              | 12  | 6%  |
| Data Scientist      | 8   | 4%  |
| Support Engineer    | 5   | 2%  |
| Data Analyst        | 3   | 1%  |
| Business Analyst    | 2   | 1%  |
| Other               | 14  | 7%  |

According to the survey, more than half of Airflow users are Data Engineers (54%). Roles of the remaining Airflow users might be broken down into Solutions Architects (13%), Developers (12%), DevOps (6%) and Data Scientists (4%). The 2022 results are similar to [those from 2019](https://airflow.apache.org/blog/airflow-survey/) and [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) with a slight increase in the representation of Solutions Architect roles.

### How often do you interact with Airflow? (single choice)

![alt_text](images/image2.png "interaction_frequency")

|                          |     |     |
| ------------------------ | --- | --- |
|                          | No. | %   |
| Every day                | 154 | 73% |
| At least once per week   | 36  | 17% |
| At least once per month  | 11  | 5%  |
| Less than once per month | 9   | 4%  |

Users who took the survey are actively using Airflow as part of their current role. 73% of Airflow users who responded use it on a daily basis, 17% weekly.

### How many people work at your company? (single choice)

![alt_text](images/image3.png "company_size")

|          |     |     |
| -------- | --- | --- |
|          | No. | %   |
| 201-5000 | 85  | 41% |
| 5000+    | 49  | 23% |
| 51-200   | 46  | 22% |
| 11-50    | 20  | 10% |
| 1-10     | 9   | 4%  |

Airflow is a framework that is used and popular in bigger companies, 64% of Airflow users who responded (compared to 52.7% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)) work for companies bigger than 200 employees (41% in companies size 201-5000 and 23% in companies size 5000+).

### How many people at your company use Airflow? (single choice)

![alt_text](images/image4.png "airflow_usage")

|        |     |     |
| ------ | --- | --- |
|        | No. | %   |
| 6-20   | 80  | 38% |
| 1-5    | 61  | 29% |
| 51-200 | 49  | 24% |
| 200+   | 18  | 9%  |

Airflow is generally used by small to medium-sized teams. 62% of the survey participants have more than 6 Airflow users in their company (38% have between 6 and 200 users, 24% between 51-200 users).

### How likely are you to recommend Apache Airflow? (single choice)

|               |        |        |        |
| ------------- | ------ | ------ | ------ |
|               | % 2019 | % 2020 | % 2022 |
| Very Likely   | 45.4%  | 61.6%  | 65.9%  |
| Likely        | 40.3%  | 30.4%  | 26.9%  |
| Neutral       | 10.7%  | 5.4%   | 6.3%   |
| Unlikely      | 2.6%   | 1.5%   | 0.5%   |
| Very Unlikely | 1%     | 1%     | 0.5%   |

According to the survey, more Airflow users (65.9%) are willing to recommend Apache Airflow compared to the survey results in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/). There is a general positive trend in a willingness to recommend Airflow, 93% of surveyed Airflow users are willing to recommend Airflow (92% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and 85.7% in [2019](https://airflow.apache.org/blog/airflow-survey/)), only 1% of users are not likely to recommend (3.6% in [2019](https://airflow.apache.org/blog/airflow-survey/) and 3.5% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) ).

### What is your source of information about Airflow? (multiple choice)

|                              |     |       |
| ---------------------------- | --- | ----- |
|                              | No. | %     |
| Documentation                | 189 | 90.4% |
| Airflow website (Blog, etc.) | 142 | 67.9% |
| Stack Overflow               | 126 | 60.3% |
| Github Issues                | 104 | 49.8% |
| Slack                        | 96  | 45.9% |
| Airflow Summit Videos        | 88  | 42.1% |
| GitHub Discussions           | 76  | 36.4% |
| Airflow Community Webinars   | 41  | 19.6% |
| Astronomer Registry          | 51  | 24.4% |
| Airflow Mailing List         | 34  | 16.3% |

Airflow documentation is a critical source of information, with more than 90% of survey participants using the documentation. It is of increasing importance compared to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) where documentation was at about 75% level. Moreover, more than 60% of users are getting information from the Airflow website (67.9% ) and Stack Overflow (60.3%) which is also a big increase compared to 36% level in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user). What’s interesting is that Slack usage decreased from 63.05% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) to 45.9% in 2022.

## Deployments

### How many active DAGs do you have in your largest Airflow instance? (single choice)

![alt_text](images/image5.png "active_dags")

|          |     |       |
| -------- | --- | ----- |
|          | No. | %     |
| 51-250   | 66  | 31.7% |
| 11-50    | 64  | 30.8% |
| 5-10     | 25  | 12.0% |
| 251-500  | 20  | 9.6%  |
| <5       | 14  | 6.7%  |
| 1000+    | 10  | 4.8%  |
| 501-1000 | 9   | 4.3%  |

62.5% of the Airflow users surveyed have between 11 to 250 DAGs in their largest Airflow instance.

### How many active Airflow instances do you have? (single choice)

![alt_text](images/image6.png "image_tooltip")

|       |     |       |
| ----- | --- | ----- |
|       | No. | %     |
| 1     | 52  | 25.2% |
| 2     | 46  | 22.3% |
| 4-7   | 40  | 19.4% |
| 3     | 37  | 18.0% |
| 20+   | 19  | 9.2%  |
| 8-10  | 7   | 3.4%  |
| 11-20 | 5   | 2.4%  |

85% of the Airflow users surveyed have between 1 and 7 active Airflow instances, and nearly 50% have only 1 or 2.

### What is the maximum number of tasks that you have used in a single DAG?(single choice)

![alt_text](images/image7.png "maximum tasks")

|           |     |       |
| --------- | --- | ----- |
|           | No. | %     |
| 11-25     | 51  | 24.5% |
| 26-50     | 41  | 19.7% |
| 51-100    | 35  | 16.8% |
| <10       | 29  | 13.9% |
| 101-250   | 23  | 11.1% |
| 501-1000  | 9   | 4.3%  |
| 1000-2500 | 8   | 3.8%  |
| 251-500   | 8   | 3.8%  |
| 2500-5000 | 4   | 1.9%  |

75% of the surveyed Airflow users have between 1 and 100 tasks per DAG.

### How many schedulers do you have in your largest Airflow instance? (single choice)

![alt_text](images/image8.png "max_schedulers")

|     |     |       |
| --- | --- | ----- |
|     | No. | %     |
| 1   | 113 | 55.1% |
| 2   | 61  | 29.8% |
| 3   | 18  | 8.8%  |
| 4+  | 13  | 6.3%  |

More than half of Airflow users who responded to the survey have 1 scheduler in their largest Airflow instance, however it’s important to notice that the second half of Airflow users decided to have 2 schedulers and more.

### What executor type do you use? (multiple choice)

|                  |     |        |
| ---------------- | --- | ------ |
|                  | No. | %      |
| Celery           | 107 | 52.7 % |
| Kubernetes       | 80  | 39.4%  |
| Local            | 49  | 24.1%  |
| Sequential       | 21  | 10.3%  |
| CeleryKubernetes | 14  | 6.9%   |

Celery (52.7%) and Kubernetes (39.4%) are the most common executors used. CeleryKubernetes (6.9%) executor also started to be noticed and used by Airflow users.

### If you use the Celery executor, how many workers do you have in your largest Airflow instance? (single choice)

![alt_text](images/image9.png "max_workers")

|      |     |       |
| ---- | --- | ----- |
|      | No. | %     |
| 2-5  | 64  | 44.8% |
| 10+  | 28  | 19.6% |
| 1    | 26  | 18.2% |
| 6-10 | 25  | 17.5% |

Amongst Celery executor users who responded to the survey, close to half the number (44.8%) have between 2 to 5 workers in their largest Airflow instance. It’s notable that nearly a fifth (19.6%) have more than 10 workers.

### Which version of Airflow do you currently use? (single choice)

![alt_text](images/image10.png "airflow_version")

|                  |     |       |
| ---------------- | --- | ----- |
|                  | No. | %     |
| 1.10.14 or older | 13  | 6.3%  |
| 1.10.15          | 19  | 9.2%  |
| 2.0.x            | 23  | 11.1% |
| 2.1.x            | 24  | 11.6% |
| 2.2.x            | 79  | 38.2% |
| 2.3.x            | 49  | 23.7% |

It's good to see that close to 85% of users who responded to the survey use one of the Airflow 2 versions, 9.2% users still use 1.10.15, while the remaining 6.3% are still using older Airflow 1.10 versions.

The good news is that the majority of users on Airflow 1 are planning migration to Airflow 2 quite soon, as for now they have capacity constraints to undertake such a significant effort in their opinion. However, it can also be noticed in the survey’s comments that some users are generally skeptical towards migration to Airflow 2, they have negative opinions about the new scheduler or compatibility with the helm chart.

As to plans about migration to the newest version of Airflow 2, users who responded to the survey are committed and waiting especially for the features related to dynamic DAGs. However, some users also reported that they are waiting to solve some dependencies they have or they prefer to wait a little bit more for the community to test the new version before they decide to move on.

### What metrics do you use to monitor Airflow? (multiple choice)

|                               |     |       |
| ----------------------------- | --- | ----- |
|                               | No. | %     |
| External monitoring service   | 81  | 40.7% |
| Information from metadatabase | 71  | 35.7% |
| Statsd                        | 54  | 27.1% |
| I do not use monitoring       | 47  | 23.6% |
| Other                         | 14  | 7%    |

In comparison to results from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user), more users are monitoring airflow in some way. External monitoring services (40.7%) and information from metabase (35.7%) started to play a more important role in Airflow monitoring.

### How do you deploy Airflow? (multiple choice)

|                                                                      |     |        |
| -------------------------------------------------------------------- | --- | ------ |
|                                                                      | No. | %      |
| On virtual machines (for example using AWS EC2)                      | 63  | 30.6 % |
| Using a managed service like Astronomer, Google Composer or AWS MWAA | 54  | 26.2 % |
| On Kubernetes (using Apache Airflow’s helm chart)                    | 46  | 22.3%  |
| On premises                                                          | 43  | 20.9%  |
| On Kubernetes (using custom deployments)                             | 39  | 18.9%  |
| On Kubernetes (using another helm chart)                             | 21  | 10.2%  |
| Other                                                                | 13  | 6.5%   |

More than half of Airflow users who responded (51.4%) deploy Airflow on Kubernetes. This is about 20 percent more than in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user). The remaining top deployment methods are on virtual machines (30.6%) and via managed services (26.2%).

### How do you distribute your DAGs from your developer environment to the cloud? (single choice)

|                                                         |     |       |
| ------------------------------------------------------- | --- | ----- |
|                                                         | No. | %     |
| Using a synchronizing process (Git sync, GCS fuse, etc) | 100 | 49%   |
| Bake them into the docker image                         | 51  | 25%   |
| Shared files system                                     | 30  | 14.7% |
| Other                                                   | 16  | 7.9%  |
| I don’t know                                            | 7   | 3.4%  |

According to the survey responses, the most popular way of distributing DAGs is a synchronizing process, about half of Airflow users (49%) use this process to distribute DAGs from developer environments to the cloud.

## Usage

### Do you have any customisation of Airflow? (single choice)

![alt_text](images/image11.png "customization")

|                                                         |     |       |
| ------------------------------------------------------- | --- | ----- |
|                                                         | No. | %     |
| No, we use vanilla airflow                              | 165 | 81.3% |
| Yes, we have a separate fork                            | 13  | 6.4%  |
| Yes, we use a 3rd-party fork                            | 12  | 5.9%  |
| Yes, we’ve backpropagated bug fixes to an older version | 13  | 6.4%  |

More Airflow users (81.3%) don’t have any customisation of Airflow (compared to 75.9% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user)). Those Airflow users who have customisations (18.7%) decided to introduce them mainly to separate development and production workflows, to backport bug fixes, due to security fixes or to run a backfill command on Kubernetes pod.

### Which Metadata Database do you use? (single choice)

![alt_text](images/image12.png "database")

|               |     |       |
| ------------- | --- | ----- |
|               | No. | %I    |
| PostgreSQL 13 | 86  | 43.9% |
| PostgreSQL 12 | 74  | 37.8% |
| MySQL 8       | 22  | 11.2% |
| MySQL 5       | 9   | 4.6%  |
| MariaDB       | 4   | 2.0%  |
| MsSQL         | 1   | 0.5%  |

According to the survey responses, the most popular metadata databases are PostgreSQL 13 (43.9%) and PostgreSQL 12 (37.8%). This represents a sharp increase from 2020, up from 68.9% to 81.7% total on PostgreSQL, with a corresponding decrease in MySQL, down from 23% to 15%. This is an interesting result taking into account community discussion about not adding support for more database backend or even deciding on single database support.

### What's the primary method by which you integrate with providers and external services in your Airflow DAGs? (single choice)

![alt_text](images/image13.png "providers_interface")

|                                            |     |       |
| ------------------------------------------ | --- | ----- |
|                                            | No. | %     |
| Using existing dedicated operators / hooks | 70  | 34.5% |
| Using Bash/Python operators                | 58  | 28.6% |
| Using custom operators / hooks             | 50  | 24.6% |
| Using KubernetesPodOperator                | 25  | 12.3% |

According to the survey responses, the following ways of using Airflow to connect to external services are the most popular: Using existing dedicated operators / hooks (34.5%), Using Bash/Python operators (28.6%), Using custom operators / hooks (24.6%). Using KubernetesPodOperator (12.3%) is less popular regarding the survey responses. The integration with providers and external services methods ranking is similar to the one from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user).

### What providers do you use in your Airflow DAGs? (multiple choice)

|                                                   |     |       |
| ------------------------------------------------- | --- | ----- |
|                                                   | No. | %     |
| Amazon Web Services                               | 112 | 55.4% |
| Google Cloud Platform / Google APIs               | 79  | 39.1% |
| Internal company systems                          | 75  | 37.1% |
| Hadoop / Spark / Flink / Other Apache software    | 57  | 28.2% |
| Microsoft Azure                                   | 17  | 8.4%  |
| Other                                             | 21  | 10.5% |
| I do not use external services in my Airflow DAGs | 14  | 6.9%  |

It’s not surprising that Amazon Web Services (55.4% vs 59.6% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)), on the next three positions Google Cloud Platform (39.1% vs 47.7% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/) ), Internal company systems (37.1% vs 55.6% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)), and other Apache products (28.2% vs 35.47% in [2020](https://airflow.apache.org/blog/airflow-survey-2020/)) are leading Airflow providers.

### How frequently do you upgrade Airflow environments? (single choice)

![alt_text](images/image14.png "upgrade_frequency")

|                                   |     |       |
| --------------------------------- | --- | ----- |
|                                   | No. | %     |
| every 12 months                   | 46  | 22.9% |
| every 6 months                    | 49  | 24.4% |
| once a quarter                    | 47  | 23.4% |
| Whenever there is a newer version | 59  | 29.4% |

Different frequencies of Airflow environments upgrades are almost equally popular amongst Airflow users who responded to the survey.

### Do you upgrade providers separately from the core? (single choice)

![alt_text](images/image15.png "providers_upgrade")

|                                                         |     |       |
| ------------------------------------------------------- | --- | ----- |
|                                                         | No. | %     |
| When I need it                                          | 83  | 42.8% |
| Never - always use the providers that come with Airflow | 68  | 35.1% |
| I did not know I can upgrade providers separately       | 32  | 16.5% |
| I upgrade providers when they are released              | 11  | 5.7%  |

According to the survey responses, Airflow users most often upgrade providers when they need it (42.8%) or prefer to stay with providers that come with Airflow (35.1%). It’s surprising that 16.5% of Airflow users who responded to the survey were not aware that they can upgrade their providers separately from the core Airflow.

### How do you pass inputs and outputs between tasks? (multiple choice)

|                                    |     |       |
| ---------------------------------- | --- | ----- |
|                                    | No. | %     |
| Xcom                               | 141 | 69.8% |
| Saving and retrieving from Storage | 99  | 49%   |
| TaskFlow                           | 37  | 18.3% |
| Other                              | 5   | 2.5%  |
| We don’t                           | 29  | 14.4% |

According to the survey responses, Xcom (69.8%) is the most popular method to pass inputs and outputs between tasks, however Saving and Retrieving Inputs and Outputs from Storage still plays an important role (49%). It’s interesting that close to 15% of Airflow users who responded to the survey declare to not pass any outputs or inputs between tasks.

### Do you use a data lineage backend? (multiple choice)

|                                                               |     |       |
| ------------------------------------------------------------- | --- | ----- |
|                                                               | No. | %     |
| No, but I will use such feature if fully supported in Airflow | 95  | 47.5% |
| I’m not familiar with data lineage                            | 58  | 29%   |
| No, data lineage isn’t a concern for my usage                 | 26  | 13%   |
| Yes, I send lineage to an Open Source lineage repository      | 15  | 7.5%  |
| Yes, I send lineage to an Enterprise lineage repository       | 7   | 3.5%  |
| Yes, I send lineage to a custom internal lineage repository   | 9   | 4.5%  |

When asked what lineage backend Airflow users use, the answers indicated that, while lineage itself is a quite new topic, there is interest in the feature as a whole. Most Airflow users responded that they don’t use lineage solutions currently but might be interested in the future if supported by Airflow (47.5%), are not familiar with data lineage (29%) or that data lineage is not their concern (13%).

### Which interfaces of Airflow do you use as part of your current role? (multiple choice)

|                                                       |     |       |
| ----------------------------------------------------- | --- | ----- |
|                                                       | No. | %     |
| Original Airflow Graphical User Interface             | 189 | 94%   |
| CLI                                                   | 98  | 48.8% |
| API                                                   | 80  | 39.8% |
| Custom (own created) Airflow Graphical User Interface | 12  | 6%    |
| GCP Composer                                          | 1   | 0.5%  |

It’s clear that usage of Airflow web UI is important as 94% of users who responded to the survey declare to use it as a part of their current role. Usage of CLI (48.8%) and API (39.8%) goes in pairs but are not so common compared to Airflow web UI usage.

### (If GUI Marked) What do you use the GUI for? (multiple choice)

|                             |     |       |
| --------------------------- | --- | ----- |
|                             | No. | %     |
| Monitoring Runs             | 188 | 95.9% |
| Accessing Task Logs         | 176 | 89.8% |
| Manually triggering DAGs    | 167 | 85.2% |
| Clearing Tasks              | 162 | 82.7% |
| Marking Tasks as successful | 119 | 60.7% |
| Other                       | 6   | 3%    |

Airflow web UI is used heavily for monitoring: Monitoring Runs (95.9%) and troubleshooting: Accessing Task Logs (89.8%), Manually triggering DAGs (85.2%), Clearing Tasks (82.7%) and Marking Tasks as successful (60.7%).

### (if CLI Marked) What do you use the CLI For? (multiple choice)

|                             |     |       |
| --------------------------- | --- | ----- |
|                             | No. | %     |
| Backfilling                 | 63  | 56.8% |
| Manually triggering DAGs    | 52  | 46.8% |
| Clearing Tasks              | 26  | 23.4% |
| Monitoring Runs             | 25  | 22.5% |
| Accessing Task Logs         | 21  | 18.9% |
| Marking Tasks as successful | 11  | 9.9%  |
| Other                       | 17  | 15.3% |

Compared to Airflow web UI, Airflow CLI is used mainly for Backfilling (56.8%) and Manually triggering DAGs (46.8%).

### In Airflow, which UI views are important for you? (multiple choice)

|                |     |       |
| -------------- | --- | ----- |
|                | No. | %     |
| List of DAGs   | 178 | 89.4% |
| Task Logs      | 162 | 81.4% |
| DAG Runs       | 160 | 80.4% |
| Graph view     | 147 | 73.9% |
| Grid/Tree View | 138 | 69.3% |
| Run Details    | 117 | 58.8% |
| DAG details    | 111 | 55.8% |
| Task Instances | 102 | 51.3% |
| Task Duration  | 91  | 45.7% |
| Code           | 90  | 45.2% |
| Task Tries     | 60  | 30.2% |
| Gantt          | 48  | 21.4% |
| Landing Times  | 27  | 13.6% |
| Other          | 4   | 2%    |

UI views importance ranking shows that the majority Airflow users use Web UI mostly for monitoring and/or troubleshooting purposes, where the top 3 views are List of DAGs (89.4%), Task Logs (81.4%) and DAG Runs (80.4%). The results are very similar to those from [2020](https://airflow.apache.org/blog/airflow-survey-2020/#overview-of-the-user) and [2019](https://airflow.apache.org/blog/airflow-survey/).

## Community and contribution

### Are you participating in the Airflow community discussions? (single choice)

![alt_text](images/image16.png "discussions_engagement")

|                                                                   |     |       |
| ----------------------------------------------------------------- | --- | ----- |
|                                                                   | No. | %     |
| I see them from time to time                                      | 99  | 48.3% |
| I regularly follow what's being discussed but don't participate   | 53  | 25.9% |
| I didn't know I could                                             | 41  | 20.0% |
| I actively participate in the discussions                         | 12  | 5.9%  |
|                                                                   | No. | %     |
| I know I can but I do not contribute                              | 116 | 57.1% |
| Very rarely when it relates to what I need                        | 44  | 21.7% |
| I do not know I could                                             | 30  | 14.8% |
| I regularly contribute by discussing, reviewing and submitting PR | 13  | 6.4%  |

Results related to the Airflow contribution are very similar to those about participating in the Airflow community discussions. Most of the Airflow users (57.1%) who responded to the survey are aware but do not contribute or contribute very rarely (21.7%). 14.8% of users were not aware they could contribute. Once again, it’s a clear indicator that there is much more to be done to engage our community to be more active contributors and raise the current 6.4% of users who actively contribute.

### If you do not contribute - why?

![alt_text](images/image18.png "contribution_reasons")

|                                                              |     |       |
| ------------------------------------------------------------ | --- | ----- |
|                                                              | No. | %     |
| I have no time to contribute even if would like to           | 65  | 38.9% |
| I don’t know how to start                                    | 63  | 37.7% |
| I don’t have a need to contribute                            | 19  | 11.4% |
| I didn’t know I could                                        | 12  | 7.2%  |
| My employer has policy that makes it difficult to contribute | 8   | 4.8%  |

According to the survey results, the most important blocker for the Airflow contribution is limited time (38.9%), but surprisingly interesting and important blocker is also lack of knowledge on how to start (37.7%), followed by lack of knowledge that it’s possible to contribute (7.2%).

## The future of Airflow

### In your opinion, what could be improved in Airflow? (multiple choice)

|                                                                      |     |       |
| -------------------------------------------------------------------- | --- | ----- |
|                                                                      | No. | %     |
| Web UI                                                               | 100 | 49.5% |
| Logging, monitoring and alerting                                     | 97  | 48.0% |
| Examples, how-to, onboarding documentation                           | 74  | 36.6% |
| Technical documentation                                              | 74  | 36.6% |
| Scheduler performance                                                | 56  | 27.7% |
| Reliability                                                          | 52  | 25.7% |
| DAG authoring                                                        | 48  | 23.8% |
| REST API                                                             | 43  | 21.3% |
| Authentication and authorization                                     | 41  | 20.3% |
| External integration e.g. AWS, GCP, Apache products                  | 41  | 20.3% |
| Better support for various deployments (Docker-compose/Nomad/Others) | 39  | 19.3% |
| Everything works fine for me                                         | 19  | 9.4%  |
| I don’t know                                                         | 4   | 2.0%  |

The results are quite self-explanatory. According to the survey results, the top area for improvement is still the Airflow web UI (49.5%), closely followed by more telemetry for logging, monitoring and alerting purposes (48%). However all those efforts should go in line with improved documentation (36.6.%) and resources about using the Airflow, especially when we take into account the need of onboarding new users (36.6%).

### Which features would you like to see in Airflow?

|                                                         |     |       |
| ------------------------------------------------------- | --- | ----- |
|                                                         | No. | %     |
| DAG Versioning                                          | 129 | 66.2% |
| Dependency management and Data-driven scheduling        | 83  | 42.6% |
| More dynamic task structure                             | 82  | 42.1% |
| Multi-Tenancy                                           | 74  | 37.9% |
| Signal-based scheduling                                 | 67  | 34.4% |
| Better Security (Isolation)                             | 65  | 33.3% |
| Submitting new DAGs externally via API                  | 53  | 27.2% |
| Composable Operators                                    | 46  | 23.6% |
| Support for native cloud executors (AWS/GCP/Azure etc.) | 44  | 22.6% |
| Better support for Machine Learning                     | 38  | 19.5% |
| Remote CLI                                              | 36  | 18.5% |
| Support for hybrid executors                            | 22  | 11.3% |

According to the survey results, DAG Versioning is a winner for new features in Airflow, and it’s not a surprise as this feature may positively impact daily work of Airflow users. It is followed by three other ideas: Dependency management and Data-driven scheduling (42.6%), More dynamic task structure (42.1%) and Multi-Tenancy (37.9%). Another interesting point from that question is that only 11.3% think that support for hybrid executors is needed in Airflow.

## Data

If you're interested in taking a look at the raw data yourself, it's available here: (Airflow User Survey 2022.csv)[/data/survey-responses/airflow-user-survey-responses-2022.csv.zip]
