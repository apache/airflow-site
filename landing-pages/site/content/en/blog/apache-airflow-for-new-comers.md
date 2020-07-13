---
title: "Apache Airflow For New Comers"
linkTitle: "Apache Airflow For New Comers"
author: "Ephraim Anierobi"
twitter: "@ephraimbuddy"
github: "@ephraimbuddy"
description: "Description"
tags: []
date: "2020-07-12"
draft: true
---

Apache Airflow is a platform to programmatically author, schedule and monitor workflows.
A workflow is a sequence of tasks that processes a set of data. You can think of workflow
as the path that describes how tasks go from being undone to done.
Scheduling, on the other hand, is the process of planning, controlling and optimizing when
a particular task should be done.

### Authoring Workflow in Apache Airflow.
Apache Airflow makes it super easy to author workflows using python scripts in a DAG file. An
acronym for Directed Acyclic Graph. The DAG houses a collection of tasks in a way that
shows each task's relationships and dependencies. You can have as many DAGs as you want, and
Airflow will execute them respecting their relationships and dependencies.
If a task B depends on successful execution of another task A, it means airflow will run task
A and only run task B after task A. This dependency is very easy to express in Airflow.
For example, the above scenario is expressed in DAG as:

```task_A >> task_B```

Also equivalent to

```task_A.set_downstream(task_B)```

That helps airflow to know that it need to execute task A before task B.

There are many inbuilt operators that makes task creation very easy. Remember, a task could just
be to upload files/folders to Google Cloud Storage.

### Scheduling and monitoring Workflow
Just like you could schedule jobs in Crontabs, Airflow jobs are scheduled and more manageable.
You can have hundreds of tasks scheduled to be executed at different times in Airflow. The jobs
can be scheduled in a DAG with a schedule interval, Airflow then executes the DAG with respect to
the tasks relationships and dependencies.
Airflow has a web interface where you can monitor DAGs, view the tasks relationships and
dependencies in a graph or tree view.






