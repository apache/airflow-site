---
title: "Apache Airflow 2.5.0: Tick-Tock"
linkTitle: "Apache Airflow 2.5.0"
author: "Ash Berlin-Taylor"
github: "ashberlin"
twitter: "ashberlin"
linkedin: "ashberlin-taylor"
description: "We're proud to announce that Apache Airflow 2.5.0 has been released with many quality of life changes."
tags: [Release]
date: "2022-12-02"
---

Apache Airfow 2.5 has just been released, barely two and a half months after 2.4!


**Details**:

📦 PyPI: https://pypi.org/project/apache-airflow/2.5.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/2.5.0/ \
🛠️ Release Notes: https://airflow.apache.org/docs/apache-airflow/2.5.0/release_notes.html \
🐳 Docker Image: docker pull apache/airflow:2.5.0 \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-2.5.0

This quicker release cadence is a departure from our previous habit of releasing every five-to-seven months and was a deliberate effort to listen to you, our users, and get the changes and improvements into your workflows earlier.

## Usability improvements to the Datasets UI

When we released Dataset aware scheduling in September we knew that the tools we gave to manage the Datasets were very much a Minimum Viable Product, and in the last two months the committers and contributors have been hard at work at making the UI much more usable when it comes to Datasets.

But we we aren't done yet - keep an eye out for more improvements coming over the next couple of releases too.

## Greatly improved `airflow dags test` command

This airflow subcommand has been rethought and re-optimized to make it much easier to test your DAGs locally - the major changes are:

a. Task logs are visible right there in the console, instead of hidden away inside the task log files
b. It is about an order of magnitude quicker to run the tasks than before (i.e. it gets to running the task code so much quicker)
c. Everything runs in one process, so you can put a breakpoint in your IDE, and configure it to run `airflow dags test <mydag>` then debug code!

## Auto tailing task logs in the Grid view

Hopefully the headline says enough. It's lovely, go check it out.

## More improvments to Dynamic-Task mapping

In a similar vein to the improvements to the Dataset (UI), we have continued to iterate on and improve the feature we first added in Airflow 2.3, Dynamic Task Mapping, and 2.5 includes [dozens of improvements](https://github.com/apache/airflow/pulls?q=is%3Apr+author%3Auranusjr+is%3Aclosed+milestone%3A%22Airflow+2.5.0%22).


## Thanks to the contributors

Andrey Anshin, Ash Berlin-Taylor, blag, Bolke de Bruin, Brent Bovenzi, Chenglong Yan, Daniel Standish, Dov Benyomin Sohacheski, Elad Kalif, Ephraim Anierobi, Jarek Potiuk, Jed Cunningham, Jorrick Sleijster, Michael Petro, Niko, Pierre Jeambrun, Tzu-ping Chung and many more, over 75 of you. Thank you!

And a special thank you to Ephraim who tirelessly worked behind the scenes as release manager!

A much shorter change log than 2.4, but I think you'll agree, some great changes.
