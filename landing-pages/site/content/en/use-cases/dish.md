---
title: "Dish"
linkTitle: "Dish"
quote:
    text: "Airflow is Batteries-Included. A great ecosystem and community that comes together to address about any (batch) data pipeline needs."
    author: "Austin Benett"
logo: "dish-logo.svg"
---

##### What was the problem?
We faced increasing complexity managing lengthy crontabs with scheduling being an issue, this required carefully planning timing due to resource constraints, usage patterns, and especially custom code needed for retry logic.  In the last case, having to verify success of previous jobs and/or steps prior to running the next.  Furthermore, time to results is important, but we were increasingly relying on buffers for processing, where things were effectively sitting idle and not processing, waiting for the next stage, in an effort to not rely as much on custom code/logic.

##### How did Apache Airflow help to solve this problem?
Relying on community built and existing hooks and operators to the majority of cloud services we use has allowed us to focus on business outcomes rather than operations.

##### What are the results?
Airflow helps us manage many of our pain-points, letting us benefit from the overall ecosystem and community.  We are able to reduce time-to-end delivery of data products by being event-driven in our processing flows (in our first usage, for example, we were able to take out over 2 hours - on average - of various waiting between stages).  Furthermore, we are able to arrive at and iterate on products quicker as a result of not needing as much custom or roll-our-own solutions.  For Our code base is smaller and simpler, it is easier to follow, and to a large extent our DAGs serve as sufficient documentation for new contributors to understand what is going on.
