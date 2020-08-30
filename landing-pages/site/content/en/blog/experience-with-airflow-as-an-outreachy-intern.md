---
title: "Journey with Airflow as an Outreachy Intern"
linkTitle: "Journey with Airflow as an Outreachy Intern"
author: "Omair Khan"
github: "OmairK"
linkedin: "omairkhan64"
description: ""
tags: [Community]
date: "2020-08-30"
---

[Outreachy](https://www.outreachy.org/) is a program which organises three months paid internships with FOSS
projects for people who are typically underrepresented in those projects.

### Contribution Period
The first thing I had to do was choose a project under an organisation. After going through all the projects
I chose “Extending the REST API of Apache Airflow”, because I had a good idea of what  REST API(s) are, so I
thought it would be easier to get started with the contributions. The next step was to set up Airflow’s dev
environment which thanks to [Breeze](https://github.com/apache/airflow/blob/master/BREEZE.rst), was a breeze.
Since I had never contributed to FOSS before so this part was overwhelming but there were plenty of issues
labelled “good first issues” with detailed descriptions and some even had code snippets so luckily that nudged
me in the right direction. These things about Airflow and the positive vibes from the community were the reasons
why I chose to stick with Airflow as my Outreachy project.

### Internship Period
My first PR was followed by many new experiences one of them being that I introduced a
[bug](https://github.com/apache/airflow/pull/7680#issuecomment-619763051) in it;).
But nonetheless it made me familiar with the feedback loop and the feedback on my subsequent
[PRs](https://github.com/apache/airflow/pulls?q=is%3Apr+author%3AOmairK+) was the focal point of the overall
learning experience I went through, which boosted my confidence to contribute more and move out of my comfort zone.
I wanted to learn more about the things that happen under the Airflow’s hood so I started filtering out recent PRs
dealing with different components and I would go through the code changes along with discussion that would help me
get a better understanding of the whole workflow. [Airflow’s mailing list](https://lists.apache.org/list.html?dev@airflow.apache.org)
was also a great source of knowledge.

The API related PRs that I worked on helped me with some of the important concepts like:

  1) [Pool CRUD endpoints](https://github.com/apache/airflow/pull/9329) where pools limit the execution parallelism.

  2) [Tasks](https://github.com/apache/airflow/pull/9597) determine the actual work that has to be carried out.

  3) [DAG](https://github.com/apache/airflow/pull/9473) which represents the structure for a collection
  of tasks. It keeps track of tasks, their dependencies and the sequence in which they have to run.

  4) [Dag Runs](https://github.com/apache/airflow/pull/9473) that are the instantiation of DAG(s) in time.

Through actively and passively participating in discussions I learnt that even if there is a difference of opinion
one could always learn from the different approaches, and [this PR](https://github.com/apache/airflow/pull/8721) with
more than 300+ comments is the proof of it. I also started reviewing small PRs which gave me the amazing opportunity
to interact with new people. Throughout my internship I learnt a lot about different frameworks and technologies
but the biggest takeaway for me was that a code is read more often than it's written, and I started writing code with
that in mind.

### Wrapping Up
So with my project of extending Airflow’s REST API as well as the Outreachy internship coming to an end I would like
to thank my mentors [Jarek Potiuk](https://github.com/potiuk), [Kaxil Naik](https://github.com/kaxil) and
[Kamil Breguła](https://github.com/mik-laj) for the patience and the time they invested in mentoring me and
the Airflow community for making me feel so welcomed. I plan to stick around and contribute to give back to the
community that has been made my summer, one to remember.
