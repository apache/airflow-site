---
title: "Adobe"
linkTitle: "Adobe"
quote:
    text: "Apache Airflow is highly extensible and its plugin interface can be used to meet a variety of use cases. It supports variety of deployment models and has a very active community to scale innovation."
    author: "Raman Gupta"
logo: "adobe-logo.svg"
---

##### What was the problem?
Modern big data platforms need sophisticated data pipelines connecting to many backend services enabling complex workflows. These workflows need to be deployed, monitored, and run either on regular schedules or triggered by external events. Adobe Experience Platform component services architected and built an orchestration service to enable their users to author, schedule, and monitor complex hierarchical (including sequential and parallel) workflows for Apache Spark (TM) and non-Spark jobs.

##### How did Apache Airflow help to solve this problem?
Adobe Experience Platform built an orchestration service to meet our user and customer requirements. It is architected based on guiding principles to leverage an off-the-shelf, open-source orchestration engine that is abstracted to other services through an API and extendible to any application through a pluggable framework. Adobe Experience Platform orchestration service leverages Apache Airflow execution engine for scheduling and executing various workflows. Apache Airflow is highly extensible and with support of K8s Executor it can scale to meet our requirements. It has a very rich Airflow Web UI to provide various workflow-related insights. Airflow’s active community that addresses issues and different feature requests also made it additionally attractive for us.

##### What are the results?
Adobe Experience Platform is using Apache Airflow's plugin interface to write custom operators to meet our use cases. With K8s Executor, we could scale it to run 1000(s) of concurrent workflows. Adobe and Adobe Experience Platform teams can focus on business use cases because all scheduling, dependency management, and retrying logic is offloaded to Apache Airflow.
