---
title: "Apache Airflow 2.10.0 is here"
linkTitle: "Apache Airflow 2.10.0 is here"
author: "Utkarsh Sharma"
github: "utkarsharma2"
linkedin: "utkarsh-sharma-5791ab8a"
description: "Apache Airflow 2.10.0 is a game-changer, with powerful Dataset improvements and the groundbreaking Hybrid Executor, set to redefine your workflow capabilities!"
tags: [Release]
date: "2024-08-08"
---

I'm happy to announce that Apache Airflow 2.10.0 is now available, bringing an array of noteworthy enhancements and new features that will greatly serve our community.

Apache Airflow 2.10.0 contains over 135 commits, which include 43 new features,  85 improvements, 43 bug fixes, and 26 documentation changes.

**Details**:

📦 PyPI: https://pypi.org/project/apache-airflow/2.10.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/2.10.0/ \
🛠 Release Notes: https://airflow.apache.org/docs/apache-airflow/2.10.0/release_notes.html \
🐳 Docker Image: "docker pull apache/airflow:2.10.0" \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-2.10.0


## Multiple Executor Configuration (formerly "Hybrid Execution")

Each executor comes with its unique set of strengths and weaknesses, typically balancing latency, isolation, and compute efficiency. Traditionally, an Airflow environment is limited to a single executor, requiring users to make trade-offs, as no single executor is perfectly suited for all types of tasks.

We are introducing a new feature that allows for the concurrent use of multiple executors within a single Airflow environment. This flexibility enables users to take advantage of the specific strengths of different executors for various tasks, improving overall efficiency and mitigating weaknesses. Users can set a default executor for the entire environment and, if necessary, assign particular executors to individual DAGs or tasks.

To configure multiple executors we can pass comma separated list in airflow configuration. The first executor in the list will be the default executor for the environment.

```
[core]
executor = 'LocalExecutor,CeleryExecutor'
```
To make it easier for dag authors, we can also specify aliases for executors that can be specified in the executor configuration
```commandline
[core]
executor = 'LocalExecutor,my.custom.module.ExecutorClass:ShortName'
```

DAG authors can specify executors to use at the task
```python
BashOperator(
    task_id="hello_world",
    executor="LocalExecutor",
    bash_command="echo 'hello world!'",
)

@task(executor="LocalExecutor")
def hello_world():
    print("hello world!")
```

We can also specify executors on the DAG level

```python
def hello_world():
	print("hello world!")

def hello_world_again():
	print("hello world again!")

with DAG(
    dag_id="hello_worlds",
    default_args={"executor": "LocalExecutor"},  # Applies to all tasks in the DAG
) as dag:
    # All tasks will use the executor from default args automatically
    hw = hello_world()
    hw_again = hello_world_again()
```

## Dynamic Dataset scheduling through DatasetAlias

Airflow 2.10 comes with `DatasetAlias` class which can be passed as a value in the `outlets`, `inlets` on a task, and `schedule` on a DAG. An instance of `DatasetAlias` is resolved dynamically to a real dataset. Downstream can depend on either the resolved dataset or on an alias itself.

`DatasetAlias` has one argument `name` that uniquely identifies the dataset. The task must first declare the alias as an outlet, and use `outlet_events` or `yield Metadata` to add events to it.

### Emit a dataset event during task execution through outlet_events
```python
from airflow.datasets import DatasetAlias

@task(outlets=[DatasetAlias("my-task-outputs")])
def my_task_with_outlet_events(*, outlet_events):
    outlet_events["my-task-outputs"].add(Dataset("s3://bucket/my-task"), extra={"k": "v"})
```
### Emit a dataset event during task execution by yielding Metadata
```python
from airflow.datasets.metadata import Metadata

@task(outlets=[DatasetAlias("my-task-outputs")])
def my_task_with_metadata():
    s3_dataset = Dataset("s3://bucket/my-task}")
    yield Metadata(s3_dataset, extra={"k": "v"}, alias="my-task-outputs")
```

There are two options for scheduling based on dataset aliases. Schedule based on `DatasetAlias` or real datasets.

```python
with DAG(dag_id="dataset-producer"):
    @task(outlets=[Dataset("example-alias")])
    def produce_dataset_events():
        pass

with DAG(dag_id="dataset-alias-producer"):
    @task(outlets=[DatasetAlias("example-alias")])
    def produce_dataset_events(*, outlet_events):
        outlet_events["example-alias"].add(Dataset("s3://bucket/my-task"))

with DAG(dag_id="dataset-consumer", schedule=Dataset("s3://bucket/my-task")):
    ...

with DAG(dag_id="dataset-alias-consumer", schedule=DatasetAlias("example-alias")):
    ...
```
### Dataset aliases UI Enhancements

Now users can see Dataset Aliases in legend of each cross-dag dependency graph with a corresponded icon/color.

![DAG Dependencies graph](dag_dependencies_1.png)

## Dark mode for Airflow UI

Airflow 2.10 comes with new Dark Mode feature which is designed to enhance user experience by offering an alternative visual theme that is easier on the eyes, especially in low-light conditions. You can toggle the crescent icon on the right side of the navigation bar to switch between light and dark mode.

![Airflow Dark mode](airflow_dark_mode.png)

![Airflow Light mode](airflow_light_mode.png)



## Task Instance History

In Apache Airflow 2.10.0, when a task instance is retried or cleared, its execution history is maintained. You can view this history by clicking on the task instance in the Grid view, allowing you to access information about each attempt, such as logs, execution durations, and any failures. This feature improves transparency into the task's execution process, making it easier to troubleshoot and analyze your DAGs.

![Task instance history](task_instance_history.png)

The history displays the final values of the task instance attributes for each specific run. On the log page, you can also access the logs for each attempt of the task instance. This information is valuable for debugging purposes.

![Task instance history](task_instance_history_log.png)

## Dataset UI Enhancements

### Dataset Events list
We now have Dataset Events list to show all dataset events across all datasets.
![Dataset list](dataset_list.png)

### Dataset Detail
Users can now look at more details of a dataset like extra, consuming dags and producing tasks.
![Dataset list](dataset_details.png)


### Toggle datasets in Graph

We can now toggle the datasets in the DAG graph

![Dataset toggle button on](dataset_toggle_on.png)
![Dataset toggle button off](dataset_toggle_off.png)

### Dataset Conditions in DAG Graph view
We now display the graph view with logical gates. Datasets with actual events are highlighted with a different border, making it easier to see what triggered the selected run.

![Render dataset conditions in graph view](render_dataset_conditions.png)

### Dataset event info in DAG Graph
For a DAG run, users can now view the dataset events connected to it directly in the graph view.

![Dataset event info](dataset_info.png)

## Contributors
Thanks to everyone who contributed to this release, including Amogh Desai, Andrey Anshin, Brent Bovenzi, Daniel Standish, Ephraim Anierobi, Hussein Awala, Jarek Potiuk, Jed Cunningham, Jens Scheffler, Tzu-ping Chung, Vincent Beck, Wei Lee, and over 120 others!

I hope you enjoy using Apache Airflow 2.10.0!
