---
title: "Experity"
linkTitle: "Experity"
quote:
    text: "Airflow can be an enterprise scheduling tool if used properly. Its ability to run \"any command, on any node\" is amazing. Handling complex, mixed-mode tasks was easy and scaling out with celery workers is huge. The open source community is great and we can help diagnose and debug our own problems as well as contribute those back to the greater good."
    author: "Luke Bodeen"
logo: "experity-logo.jpg"
---

##### What was the problem?
We had to deploy our complex, flagship app to multiple nodes in multiple ways. This required tasks to communicate across Windows nodes and coordinate timing perfectly. We did not want to buy an expensive enterprise scheduling tool and needed ultimate flexibility.

##### How did Apache Airflow help to solve this problem?
Ultimately we decided flexible, multi-node, DAG capable tooling was key and airflow was one of the few tools that fit that bill. Having it based on open source and python were large factors that upheld our core principles. At the time, Airflow was missing a windows hook and operator so we contributed the WinRM hook and operator back to the community. Given its flexibilty we also use DAG generators to have our metadata drive our DAGs and keep maintenance costs down.

##### What are the results?
We have a very flexible deployment framework that allows us to be as nimble as possible. The reliability is something we have grown to trust as long as we use the tool correctly. The scalability has also allowed us to decrease the time it takes to operate on our fleet of servers.
