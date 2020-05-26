---
title: "Sift"
linkTitle: "Sift"
quote:
    text: "Airflow helped us to define and organize our ML pipeline dependencies, and empowered us to introduce new, diverse batch processes at increasing scale."
    author: "Handong Park"
logo: "sift_logo.png"
---

##### What was the problem?

At Sift, we’re constantly training machine learning models that feed into the core of Sift’s Digital Trust & Safety platform. The platform gives our customers a way to discern suspicious online behavior from trustworthy behavior, allowing our customers to protect their online transactions, maintain the integrity of their content platforms, and keep their users’ accounts secure. To make this possible, we’ve built model training pipelines that consist of hundreds of steps in MapReduce and Spark, with complex requirements between them. 

When we built these workflows, we found that we needed a centralized way to organize the interactions between the many steps in each workflow. But before Airflow, we didn’t have an easy way to express those dependencies. And as we added steps to the workflows, it became increasingly difficult to coordinate their dependencies and keep ML experiments in sync.

It soon became clear that we needed a way to orchestrate both the scheduled execution of our jobs and the dependencies between steps of not only a single workflow, but of multiple workflows. We needed a way to dynamically create several experimental ML workflows at once that could each have their own code, dependencies, and tasks. Additionally, we needed a way to be able to monitor the status of tasks, and re-run or restart tasks from any given point in a workflow with ease.

##### How did Apache Airflow help to solve this problem?

Airflow makes it easy to clearly define the interactions between various jobs, expanding the scope of what we can do in our model training pipelines. We now have the ability to schedule and coordinate all jobs while managing the dependencies between them using DAGs. Each of our main workflows, including our model training pipeline and our ETL pipelines, has its own DAG code that manages its tasks’ dependencies and the execution schedule for the pipeline. We even define dependencies between separate DAGs by using Airflow’s ExternalTaskSensor. This allows our DAGs to actually depend on each other and allows us to keep each one focused and compact in its scope. 

As part of our custom Airflow setup, we’ve built out a separate Airflow ecosystem for short-lived experimental DAGs as well, so that we can test changes to our jobs or run separate model training pipelines in isolation. Using deployment scripts that edit our DAGs when we upload them to Airflow, the same code that powers an existing DAG can be deployed in a separate, isolated environment with experimental edits. This means that each experiment can have its own isolated code, running in parallel with other pipelines, without accidentally touching others’ jobs or dependencies.

Finally, Airflow has given us the ability to manage our tasks’ successes and failures through its user interface. Airflow allows us to track our tasks’ failures, duration, history, and logs in one central UI, and that same UI also allows us to easily retry single tasks, branches of a DAG, or entire DAGs.

##### What are the results?

Airflow initially gave us a way to solve our existing problems: we used Airflow to replace rigid crons with well-defined DAG dependencies, to build isolated ML experiments using short-lived DAGs, and to track our pipelines’ successes and failures. 

But even after that, Airflow helped us to grow beyond those initial challenges, and expanded the scope of what we could feasibly tackle. Airflow not only made it easier to manage our ever-expanding ML pipelines, but also allowed us to create entirely new pipelines, ranging from workflows that back up our production data to complex ETL pipelines that transform data into experimentation-ready formats. 

Airflow also allowed us to support a more diverse toolset. Shell scripts, Java, Python, Jupyter notebooks, and more - all of these can be managed from an Airflow DAG, allowing developers to utilize our data to test new ideas, generate insights, and improve our models with ease.
