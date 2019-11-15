---
title: "Onefootball"
linkTitle: "Onefootball"
quote:
    text: "Airflow is extensible enough for any business to define the custom operators they need. Airflow can help you in your DataOps journey: viewing analytics as code, monitoring, reusing components, being a catalyst of team interactions."
    author: "Louis Guitton"
logo: "onefootball-logo.svg"
---

##### What was the problem?
With millions of daily active users, managing the complexity of data engineering at Onefootball is a constant challenge. Lengthy crontabs, multiplication of custom API clients, erosion of confidence in the analytics served, increasing heroism ("only one person can solve this issue"). Those are the challenges that most teams face unless they consciously invest in their tools and processes.

On top of that, new data tools appear each month: third party data sources, cloud providers solutions, different storage technologies... Managing all those integrations is costly and brittle, especially for small data engineering teams that are trying to do more with less.

##### How did Apache Airflow help to solve this problem?
Airflow had been on our radar for a while until one day we took the leap. We used the DAG paradigm to migrate the pipelines running on crontabs. We benefited from the community Hooks and Operators to remove parts of our code, or to refactor the API clients specific to our business. We use the alerts, SLAs and the web UI to regain confidence in our analytics. We use our airflow internal PRs as catalysts for team discussion and to challenge our technical designs.

We have DAGs orchestrating SQL transformations in our data warehouse, but also DAGs that are orchestrating functions ran against our Kubernetes cluster both for training Machine Learning models and sending daily analytics emails.

##### What are the results?
The learning curve was steep but in about 100 days we were able to efficiently use Airflow to manage the complexity of our data engineering. We currently have 17 DAGs (adding on average 1 per week), we have 2 contributions on apache/airflow, we have 7 internal hooks and operators and are planning to add more as our migration efforts continue.
