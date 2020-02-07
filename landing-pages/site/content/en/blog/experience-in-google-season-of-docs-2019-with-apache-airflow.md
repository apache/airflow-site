---
title: "Experience in Google Season of Docs 2019 with Apache Airflow"
linkTitle: "Experience in Google Season of Docs 2019 with Apache Airflow"
author: "Kartik Khare"
twitter: "khare_khote"
github: "KKcorps"
linkedin: "kharekartik"
description: ""
tags: ["Documentation"]
date: 2019-12-20
---

I came across [Google Season of Docs][1] (GSoD) almost by accident, thanks to my extensive HackerNews and Twitter addiction.  I was familiar with the Google Summer of Code but not with this program.
It turns out it was the inaugural phase. I read the details, and the process felt a lot like GSoC except that this was about documentation.

## About Me
I have been writing tech articles on medium as well as my blog for the past 1.5 years.  Blogging helps me test my understanding of the concepts as untangling the toughest of ideas in simple sentences requires a considerable time investment.

Also, I have been working as a Software Developer for the past three years, which involves writing documentation for my projects as well. I completed my B.Tech from  IIT Roorkee. During my stay in college, I applied for GSoC once but didn’t make it through in the final list of selected candidates.

I saw GSoD as an excellent opportunity to improve my technical writing skills using feedback from the open-source community. I contributed some bug fixes and features to Apache Superset and Apache Druid, but this would be my first contribution as a technical writer.

## Searching for the organization
About 40+ organizations were participating in the GSoD. However, there were two which came as the right choice for me in the first instant. The first one was [Apache Airflow][2] because I had already used Airflow extensively and also contributed some custom operators inside the forked version of my previous company.

The second one was [Apache Cassandra][3], on which I also had worked extensively but hadn’t done any code or doc changes.

Considering the total experience, I decided to go with the Airflow.

## Project selection
After selecting the org, the next step was to choose the project. Again, my previous experience played a role here, and I ended up picking the **How to create a workflow** . The aim of the project was to write documentation which will help users in creating complex as well as custom DAGs.  
The final deliverables were a bit different, though. More on that later.

After submitting my application, I got involved in my job until one day, I saw a mail from google confirming my selection as a Technical Writer for the project.

## Community Bonding
Getting selected is just a beginning.  I got the invite to the Airflow slack channel where most of the discussions happened.
My mentor was [Ash-Berlin Taylor][4] from Apache Airflow. I started talking to my mentor to get a general sense of what deliverables were expected. The deliverables were documented in [confluence][5].

- A page for how to create a DAG that also includes:
    - Revamping the page related to scheduling a DAG
    - Adding tips for specific DAG conditions, such as rerunning a failed task
- A page for developing custom operators that includes:
    - Describing mechanisms that are important when creating an operator, such as template fields, UI color, hooks, connection, etc.
    - Describing the responsibility between the operator and the hook
    - Considerations for dealing with shared resources (such as connections and hooks)
- A page that describes how to define the relationships between tasks. The page should include information about:
    -  ** \>\> \<\< **
    - set upstream / set downstream
    - helpers method ex. chain
- A page that describes the communication between tasks that also includes:
    - Revamping the page related to macros and XCOM

My mentor set the expectation early on that the deliverables were sort of like guidelines and not strict rules.
If I wanted to, I could choose to work on something else related to the project also, which was not under deliverables.
After connecting with the mentor, I started engaging with the overall Airflow community. The people in the community were helpful, especially [Kamil Bregula][6]. Kamil helped me in getting started with the guidelines to follow while writing the documentation for Airflow.

## Doc Development
I picked DAG run as my first deliverable. I chose this topic as some parts of it were already documented but needed some additional text.
I splitter the existing Scheduling & Triggers page into two new pages.
1. Schedulers
2. DAG Runs

Most of the details unrelated to schedulers were moved to DAG runs page, and then missing points such as how to re-run a task or DAG were added.
Once I was satisfied with my version, I asked my mentor and Kamil to review it. For the first version, I shared the text in the Google docs file in which the reviewers added comments.
However, the document started getting messy, and it became difficult to track the changes. The time had come now to raise a proper Pull Request.

This was the time when I faced my first challenge. The documentation of Apache Airflow is written using RST(reStructuredText) syntax, with which I was entirely unfamiliar. I had mostly worked in Markdown.
I spent the next couple of days understanding the syntax. Fortunately, it was quite easy to get acquainted.
I raised the [Pull Request][7] and waited for the comments. Finally, after a few days when I saw the comments, they were mostly related to two things - grammar and formatting. There were also comments related to what I had missed or misinterpreted.

### Using correct grammar
After discussing with Kamil, I decided to follow [Google’s Developer Documentation Guidelines][8].  These guidelines contain almost everything you’ll need to consider while writing good documentation, such as always to use active voice.
Secondly, I installed the Grammarly app. After writing a doc, I used to put it in Grammarly to check for errors. Then I corrected the errors, made some more changes, and then again pushed it to Grammarly. This was an iterative process until I arrived with a version of the doc, which was grammatically correct but not seemed to have been written by an AI.

### Formatting
Formatting involves writing notes and tips, marking the airflow components correctly in the text, and making sure a user who is skimming through the docs doesn’t miss the critical text.
This required a bit of trial and error. I studied the current pattern in Airflow docs and made changes, pushed commits, incorporated new review comments, and then so on.

In the end, all the reviewers approved the PR, but it was not merged until two months later. This was because we doubted if some more pages, such as **Concepts**, should also be split up, resulting in a better-structured document. In the end, we decided to delay it until we discussed it with the broader community.

My [second PR][9] was a completely new document. It was related to How to create your custom operator. For this, since now I was familiar with most of the syntax, I directly raised the PR without going via Google docs. I received a lot of comments again, but this time they were more related to what I had written rather than how I had written it.
e.g., Describing in detail how to use **template fields** and clean up my code examples. The fewer grammatical & formatting error comments showed I had made progress.
The PR was accepted within two weeks and gave me a huge confidence boost.

After my second PR, I was in a bit of a deadlock. My last remaining deliverable was related to **Macros**, but the scope wasn’t clear. I talked to my mentor, and he told me he didn’t mind if I can go off-track to work on something else while the community figured out what changes were needed.
We discussed a lot of ideas. In the end, I decided to go with the Best Practices guide inspired by my mentors’ [talk on Apache Airflow ][10]in a meetup. Having faced challenges while running Airflow in production myself, I was highly motivated to write something like this so that other developers don’t suffer.
The first draft was ready within two weeks. I called it **Running Airflow in Production**. However, after adding a few more pieces to the document, I realized it was better to call it **Best Practices** guide, which most of the open-source projects contained.

People were enthusiastic about this [pull request][11] since a lot of them faced the challenges described in the doc. I had hit the nail on the head. After some deliberation over the next 1-2 weeks, my PR got accepted.

I then returned to my first PR and started making some changes related to the new review comments.  After this, I discussed with my mentor about specific elements that were bugging him, such as getting people to understand how the schedule interval works in as few words as possible.
After a lot of trial and error, we arrived at a version with which both of us could make peace.

## Final Evaluation
On 12th September, I received mail from Google about the successful completion of the project. This meant my mentor liked my work. The Airflow community also appreciated the contributions.

My documents were finally published on Airflow website -

- [DAG Runs][12]
- [Scheduler][13]
- [Creating a custom operator][14]
- [Best Practices][15]

I also started getting invited in the PR reviews of other developers. I am looking forward to more contributions to the project in the coming year.






[1]:    https://developers.google.com/season-of-docs
[2]:    https://airflow.apache.org/
[3]:    http://cassandra.apache.org/
[4]:    https://github.com/ashb
[5]:    https://cwiki.apache.org/confluence/display/AIRFLOW/Season+of+Docs+2019
[6]:    https://github.com/mik-laj
[7]:    https://github.com/apache/airflow/pull/6295
[8]:    https://developers.google.com/style/
[9]:    https://github.com/apache/airflow/pull/6348
[10]:   https://drive.google.com/file/d/1E4zle8-fv5S1rrlcNUzjiEV19OMYvwoY/view?usp=sharing
[11]:   https://github.com/apache/airflow/pull/6515
[12]:   https://airflow.readthedocs.io/en/latest/dag-run.html
[13]:   https://airflow.readthedocs.io/en/latest/scheduler.html
[14]:   https://airflow.readthedocs.io/en/latest/howto/custom-operator.html
[15]:   https://airflow.readthedocs.io/en/latest/best-practices.html
