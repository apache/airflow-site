---
title: "Big Fish Games"
linkTitle: "Big Fish Games"
quote:
    text: "Apache Airflow is a great open-source workflow orchestration tool supported by an active community. It provides all the features needed for scheduling workflows out-of-the-box. Additionally, DAGs can be easily programmed in Python. Backfilling historical data and retrying failed jobs based on configuration helps mitigate any upstream issues and better handles the late arrival of data."
    author: "Suganya Varadarajan"
logo: "big-fish-games-logo.svg"
---

##### What was the problem?
The main challenge is the lack of standardized  ETL workflow orchestration tools. PowerShell and Python-based ETL frameworks built in-house are currently used for scheduling and running analytical workloads. However, there is no web UI through which we can monitor these workflows and it requires additional effort to maintain this framework. These scheduled jobs based on external dependencies are not well suited to modern Big Data platforms and their complex workflows. Although we experimented with Apache Oozie for certain workflows, it did not handle failed jobs properly. For late data arrival, these tools are not flexible enough to enforce retry attempts for the job failures.

##### How did Apache Airflow help to solve this problem?
Apache Airflow helps us programmatically control our workflows in Python by setting task dependencies and monitoring tasks within each DAG in a Web UI. Airflow allows us to view detailed logs for each task in these complex workflows. It has built-in connectors for Hive, MySQL, Google Cloud APIs and others. It also lends us flexibility to create our own custom connectors (i.e. for a Netezza database) using JDBCHook and JDBCOperator or extend the existing operator such as Hive Operator. For complex workflows, we can design ETLs using Airflow by running certain tasks only on weekdays. A powerful feature of Airflow is its support for backfilling of data: when we add a new task to a DAG, we can backfill for that task alone. Airflow also allows us to set external DAG dependencies alongside features such as SQLSensor on a database table to run a specific task.

##### What are the results?
We seek to run concurrent tasks with DAGs and concurrent DAGs using Apache Airflow, in hopes of running our entire ETL workload faster. Airflow helps our analysts and developers focus on the analyses, rather than labor over building an ETL framework to schedule and monitor our applications. Airflow facilitates a seamless ETL migration to the Google Cloud Platform (GCP), as GCP maintains Cloud Composer, an Apache Airflow managed service.
