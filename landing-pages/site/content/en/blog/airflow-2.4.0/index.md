---
title: "Apache Airflow 2.4.0: That Data Aware Release"
linkTitle: "Apache Airflow 2.4.0"
author: "Ash Berlin-Taylor"
github: "ashberlin"
twitter: "ashberlin"
linkedin: "ashberlin-taylor"
description: "We're proud to announce that Apache Airflow 2.4.0 has been released with many exciting improvements."
tags: [Release]
date: "2022-09-19"
---

Apache Airflow 2.4.0 contains over 650 "user-facing" commits (excluding commits to providers or chart) and over 870 total. That includes 46 new features, 39 improvements, 52 bug fixes, and several documentation changes.

**Details**:

📦 PyPI: https://pypi.org/project/apache-airflow/2.4.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/2.4.0/ \
🛠️ Release Notes: https://airflow.apache.org/docs/apache-airflow/2.4.0/release_notes.html \
🐳 Docker Image: docker pull apache/airflow:2.4.0 \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-2.4.0

## Data-aware scheduling (AIP-48)

This one is big. Airflow now has the ability to schedule DAGs based on other tasks updating datasets.

What does this mean, exactly? This is a great new feature that lets DAG authors create smaller, more self-contained DAGs, which chain together into a larger data-based workflow. If you are currently using `ExternalTaskSensor` or `TriggerDagRunOperator` you should take a look at datasets -- in most cases you can replace them with something that will speed up the scheduling!

But enough talking, lets have a short example. First lets write a simple DAG with a task called `my_task` that produces a dataset called `my-dataset`:

```python
from airflow import Dataset


dataset = Dataset(uri='my-dataset')

with DAG(dag_id='producer', ...)
    @task(outlets=[dataset])
    def my_task():
        ...
```

Datasets are defined by a URI. Now, we can create a second DAG (`consumer`) that gets scheduled whenever this dataset changes:

```python

from airflow import Dataset


dataset = Dataset(uri='my-dataset')

with DAG(dag_id='dataset-consumer', schedule=[dataset]):
    ...
```

With these two DAGs, the instant `my_task` finishes, Airflow will create the DAG run for the `dataset-consumer` workflow.

We know that what exists right now won't fit all use cases that people might wish for datasets, and in the coming minor releases (2.5, 2.6, etc.) we will expand and improve upon this foundation.

Datasets represent the abstract concept of a dataset, and (for now) do not have any direct read or write capability - in this release we are adding the foundational feature that we will build upon in the future - and it's part of our goal to have smaller releases to get new features in your hands sooner!

For more information on datasets, see the [documentation on Data-aware scheduling][data-aware-scheduling]. That includes details on how datasets are identified (URIs), how you can depend on multiple datasets, and how to think about what a dataset is (hint: don't include "date partitions" in a dataset, it's higher level than that).

[data-aware-scheduling]: https://airflow.apache.org/docs/apache-airflow/2.4.0/concepts/datasets.html

## Easier management of conflicting python dependencies using the new ExternalPythonOperator

As much as we wish all python libraries could be used happily together that sadly isn't the world we live in, and sometimes there are conflicts when trying to install multiple python libraries in an Airflow install -- right now we hear this a lot with `dbt-core`.

To make this easier we have introduced `@task.external_python` (and the matching `ExternalPythonOperator`) that lets you run an python function as an Airflow task in a pre-configured virtual env, or even a whole different python version. For example:

```python
@task.external_python(python='/opt/venvs/task_deps/bin/python')
def my_task(data_interval_start, data_interval_env)
    print(f'Looking at data between {data_interval_start} and {data_interval_end}')
    ...
```

There are a few subtlties as to what you need installed in the virtual env depending on which context variables you access, so be sure to read the [how-to on using the ExternalPythonOperator][howto-externalpythonop]

[howto-externalpythonop]: http://airflow.apache.org/docs/apache-airflow/2.4.0/howto/operator/python.html#externalpythonoperator

## More improvements to Dynamic Task Mapping (AIP-42)

You asked, we listened. Dynamic task mapping now includes support for:

- `expand_kwargs`: To assign multiple parameters to a non-TaskFlow operator.
- `zip`: To combine multiple things without cross-product.
- `map`: To transform the parameters just before the task is run.

For more information on dynamic task mapping, see the new sections of the doc on [Transforming Mapped Data][transforming-mapped-data], [Combining upstream data (aka "zipping")][task-mapping-zip], and [Assigning multiple parameters to a non-TaskFlow operator][expand-kwargs].

[task-mapping-zip]: https://airflow.apache.org/docs/apache-airflow/2.4.0/concepts/dynamic-task-mapping.html#combining-upstream-data-aka-zipping
[transforming-mapped-data]: https://airflow.apache.org/docs/apache-airflow/2.4.0/concepts/dynamic-task-mapping.html#transforming-mapped-data
[expand-kwargs]: https://airflow.apache.org/docs/apache-airflow/2.4.0/concepts/dynamic-task-mapping.html#assigning-multiple-parameters-to-a-non-taskflow-operator

## Auto-register DAGs used in a context manager (no more `as dag:` needed)

This one is a small quality of life improvement, and I don't want to admit how many times I forgot the `as dag:`, or worse, had `as dag:` repeated.

```python

with DAG(dag_id="example") as dag:
  ...


@dag
def dag_maker():
    ...


dag2 = dag_maker()
```

can become

```python

with DAG(dag_id="example"):
    ...


@dag
def my_dag():
    ...


my_dag()
```

If you want to disable the behaviour for any reason, set `auto_register=False` on the DAG:

```python
# This dag will not be picked up by Airflow as it's not assigned to a variable
with DAG(dag_id="example", auto_register=False):
    ...
```

## Additional improvements

With over 650 commits the [full list of features, fixes and changes][release-notes-2.4.0] is too big to go in to here (check out the release notes for a full list), but some noteworthy or interesting small features include:

- Auto-refresh on the home page
- Add `@task.short_circuit` TaskFlow decorator
- Add roles delete command to cli
- Add support for `TaskGroup` in `ExternalTaskSensor`
- Add `@task.kubernetes` taskflow decorator
- Add experimental `parsing_context` to enable optimization of Dynamic DAG handling in workers
- Consolidate to one `schedule` param
- Allow showing non-sensitive config values in Admin -> Configuration (rather than all or nothing)
- Operator name separate from class (no more `_PythonDecoratedOperator` when using TaskFlow)

[release-notes-2.4.0]: https://airflow.apache.org/docs/apache-airflow/2.4.0/release_notes.html#airflow-2-4-0-2022-09-19

## Contributors

Thanks to everyone who contributed to this release, including Andrey Anshin, Ash Berlin-Taylor, Bartłomiej Hirsz, Brent Bovenzi, Chenglong Yan, D. Ferruzzi, Daniel Standish, Drew Hubl, Elad Kalif, Ephraim Anierobi, Jarek Potiuk, Jed Cunningham, Josh Fell, Mark Norman Francis, Niko, Tzu-ping Chung, Vincent, Wojciech Januszek, chethanuk-plutoflume, pierrejeambrun, and everyone else who committed, all 152 of you! You are what makes Airflow the successful project that it is!
