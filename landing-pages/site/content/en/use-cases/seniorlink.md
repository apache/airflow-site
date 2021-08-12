---
title: "Seniorlink"
linkTitle: "Seniorlink"
quote:
    text: "Airflow helped us increase the visibility of our batch processes, decouple our batch jobs, and improve our development cycle, all while building confidence in our ability to scale and grow."
    author: "Christopher Petrino"
logo: "seniorlink-logo.svg"
---

##### What was the problem?
Here at Seniorlink, we provide services, support, and technology that engages family caregivers. One of our focuses is using data to bolster our knowledge and improve the experience of our users. Like many looking to build an effective data stack, we adopted a Python, Spark, Redshift, and Tableau core toolset.

We had built a robust stack of batch processes to deliver value to the business, deploying these data services in AWS using a mixture of EMR, ECS, Lambda, and EC2. Moving fast, as many new endeavors do, we ultimately ended up with one monolithic batch process with many smaller satellite jobs. Given the scale and quantity of jobs, we began to lose transparency as to what was happening. Additionally, many jobs were launched in a single EMR cluster and so tightly coupled that a failure in one job required the recompute of all the jobs run on that cluster. These behaviors are highly inefficient, difficult to debug and result in long iteration periods given the duration of these batch jobs.

We were beginning to lose precious time manually managing the schedules via AWS Datapiplines, AWS Lambdas, and ECS Tasks. Much of our development effort was spent waiting for the monolith to complete running to examine a smaller job within. Our best chance at keeping system transparency was active documentation in our internal wiki.

##### How did Apache Airflow help to solve this problem?
Airflow gave us a way to orchestrate our disparate tools into a single place. Instead of dealing with multiple schedules, we have a straightforward UI to consider. We gained a great deal of transparency, being able to monitor the status of tasks, re-run or restart tasks from any given point in a workflow, and manage the dependencies between jobs using DAGs. We were able to decouple our monolith and schedule the resulting smaller tasks confidently.

##### What are the results?
Airflow increased the visibility of our batch processes through the use of the DAGs and the UI. Our end-to-end run time decreased by 20%, given our ability to decouple our monolithic batch jobs into several smaller ones. Our development and debugging time reduced with our ability to manage and isolate all our tasks. We were able to merge our diverse toolset into a more central location. Lastly, with its broad adoption, we were able to quickly push this new framework up to our production environment.
