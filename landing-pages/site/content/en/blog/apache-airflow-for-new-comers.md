---
title: "Apache Airflow For NewComers"
linkTitle: "Apache Airflow For NewComers"
author: "Ephraim Anierobi"
twitter: "@ephraimbuddy"
github: "@ephraimbuddy"
description: "Description"
tags: []
date: "2020-07-12"
draft: true
---

Apache Airflow is a platform to programmatically author, schedule, and monitor workflows.
A workflow is a sequence of tasks that processes a set of data. You can think of workflow as the
path that describes how tasks go from being undone to done. Scheduling, on the other hand, is the
process of planning, controlling, and optimizing when a particular task should be done.

### Authoring Workflow in Apache Airflow.
Airflow makes it easy to author workflows using python scripts. A DAG(Directed Acyclic Graph)
represents a workflow in Airflow. It is a collection of tasks in a way that shows each task's
relationships and dependencies. You can have as many DAGs as you want, and Airflow will execute
them in line with the task's relationships and dependencies. If task B depends on the successful
execution of another task A, it means airflow will run task A and only run task B after task A.
This dependency is very easy to express in Airflow. For example, the above scenario is expressed as
```python
task_A >> task_B
```
Also equivalent to
```python
task_A.set_downstream(task_B)
```

That helps airflow to know that it needs to execute task A before task B.
Let us now discuss the architecture of Airflow that makes scheduling, executing, and monitoring of
workflow an easy thing.

### Scheduler
The scheduler is the component that monitors DAGs and triggers those tasks whose dependencies have
been met. It watches over the DAG folder, checking the tasks in each DAG and triggers them once they
are ready. It accomplishes these by reading the metadata database to check the status of each task and
decides what needs to be done. The metadata database is where the status of all tasks are recorded.
The status can be one of running, success, failed, etc.

In the breeze environment, the scheduler is started by running the command airflow scheduler.

### Executor
Executors are responsible for running tasks. They work with the scheduler to get information about
what resources are needed to run a task as the task is queued.

By default, airflow uses the SequentialExecutor. However, this executor is limited and it is the only
executor that can be used with SQLite.

There are many other executors, the difference is on the resources they have and how they choose to
use the resources

### Webserver
The webserver is the web interface(UI) for Airflow. The UI is feature-rich. It makes it easy to
monitor and troubleshoot DAGs and Tasks.

There are many actions you can perform on the UI. You can trigger a task, monitor the execution
including the duration of the task. The UI makes it possible to view the task's dependencies in a
tree view and graph view. You can view task logs in the UI.

The web UI is started with the command "airflow webserver" in the breeze environment.

### Backend
By default, Airflow uses the SQLite backend for storing the configuration information, DAG states,
and much other useful information. This should not be used in production as SQLite can cause a data
loss.

You can use PostgreSQL or MySQL as a backend for airflow. It is easy to change to PostgreSQL or MySQL.

This command "./breeze --backend mysql" selects MySQL as the backend in the breeze environment.

### Operators
Operators determine what gets done by a task. Airflow has a lot of builtin Operators. Each operator
does a specific thing. There's a BashOperator that executes a bash command, the PythonOperator which
calls a python function, AwsBatchOperator which executes a job on AWS Batch and many more.

### Sensors
Sensors can be described as special operators that are used to monitor a long-running task.
Just like Operators, there are many predefined sensors in Airflow.
























