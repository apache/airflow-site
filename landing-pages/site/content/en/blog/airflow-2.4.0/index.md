---
title: "Apache Airflow 2.4.0: Data
linkTitle: "Apache Airflow 2.4.0"
author: "Ash Berlin-Taylor"
github: "ashberlin"
linkedin: "ashberlin-taylor"
description: "We're proud to announce that Apache Airflow 2.4.0 has been released."
tags: [Release]
date: "2022-09-19"
---

Apache Airflow
Apache Airflow 2.4.0 contains over 650 "user-facing" commits in this release (excluding commits to providers or chart) and over 870 in total since 2.3.0 and includes 50 new features, 99 improvements, 85 bug fixes, and several doc changes.

**Details**:

📦 PyPI: https://pypi.org/project/apache-airflow/2.4.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/2.4.0/ \
🛠️ Release Notes: https://airflow.apache.org/docs/apache-airflow/2.4.0/release_notes.html \
🐳 Docker Image: docker pull apache/airflow:2.4.0 \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-2.4.0


## Data-aware scheduling (AIP-48)

This one is big. Airflow now has the ability to schedule DAGs based on other tasks updating datasets.

What does this mean, exactly? This is a great new feature and lets DAG authors create smaller, more self-contained DAGs, that can chain together into a larger data-based workflow. If you are currently using `ExternalTaskSensor` or `TriggerDagRunOperator` you should take a look at datasets -- in most cases you can replace them with something that will speed up the scheduling!

But enough talking, lets have a short example. First lets create the task that produces the dataset:

```python
from airflow import Dataset


dataset = Dataset(uri='my-dataset')

with DAG(dag_id='producer', ...)
    @task(outlets=[dataset])
    def my_task():
        ...
```

And then we can tell Airflow to schedule a DAG whenever this Dataset changes:

```python

from airflow import Dataset


dataset = Dataset(uri='my-dataset')

with DAG(dag_id='dataset-consumer', schedule=[dataset]):
    ...
```

With these two dags, the instant that the `my_task` finishes Airflow will create the DAG run for the `dataset-consumer` workflow.

(If you have the produce and consumer in different files you do not need to use the same Dataset object, two `Dataset()`s created with the same URI are equal.)

We know that what exists right now won't fit all use cases that people might wish for datasets, and in the coming minor releases (2.5, 2.6, etc.) we will expand and improve upon this foundation

Datasets represent the abstract concept of a dataset, and (for now) do not have any direct read or write capability - in this release we are adding the foundational feature that we will build upon in future - and it's part of our goal to have smaller releases to get new features in your hands sooner!

For more info on Datasets please see the [docs on Data-aware scheduling][data-aware-scheduling], including how datasets are identified (URIs), how you can depend on multiple datasets, and how to think about what is a Dataset (hint: don't include "date partitions" in a dataset, it's higher level than that.)

[data-aware-scheduling]: https://airflow.apache.org/docs/apache-airflow/stable/concepts/datasets.html

## More improvments to Dynamic Task Mapping (AIP-42)

You asked, we listened. Dynamic task mapping now includes support for `expand_kwargs` (to assign multiple parameters to a non-TaskFlow operator), `zip` (to combine multiple things without cross-product) and `map` (to transform the parameters on just before the task is run).

For more info on dynamic task mapping please the new sections of the doc on [Transforming Mapped Data][transforming-mapped-data], [Combining upstream data (aka "zipping")][task-mapping-zip], and [Assigning multiple parameters to a non-TaskFlow operator][expand-kwargs].

[task-mapping-zip]: https://airflow.apache.org/docs/apache-airflow/stable/concepts/dynamic-task-mapping.html#combining-upstream-data-aka-zipping
[transforming-mapped-data]: https://airflow.apache.org/docs/apache-airflow/stable/concepts/dynamic-task-mapping.html#transforming-mapped-data
[expand-kwargs]: https://airflow.apache.org/docs/apache-airflow/stable/concepts/dynamic-task-mapping.html#assigning-multiple-parameters-to-a-non-taskflow-operator

## Auto-register DAGS used in a context manager (no more `as dag:` needed)

This one is a small quality of life improvement, and I don't want to admit how many times I forgot the `as dag:`, or worse, had `as dag:` repeated (meaning only the last use showed up)

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

If you want to disable the behaviour for any reason then set `auto_register=False` on the dag:

```python
# This dag will not be picked up by Airflow as it's not assigned to a variable
with DAG(dag_id="example", auto_register=False):
    ...
```

## Removal of experimental Smart Sensors feature

Smart Sensors were added in 2.0 and deprecated in favor of Deferrable operators in 2.2, and have now been removed. If you were using smart sensors you will have to switch to using deferrable operators before you can upgrade.

We're sorry to remove this feature (and we didn't do it lightly) but to enable us to continue to grow and evolve Airflow we needed to remove this experimental code. We will only do this sort of change in a minor release for features marked as experimental, for anything that is fully supported it won't be removed or broken until the next major release.

## Other small features

With over 650 commits the full list of features, fixes and changes is too big to go in to here (check out the release notes for a full list), but some noteworthy or interesting small features include:

- Auto-refresh on the home page
- Add `@task.short_circuit` TaskFlow decorator
- Add roles delete command to cli (#25854)
- Add support for `TaskGroup` in `ExternalTaskSensor` (#24902)
- Add `@task.kubernetes` taskflow decorator (#25663)
- Consolidate to one `schedule` param (#25410)
- Allow showing non-sensitive config values in Admin -> Configuration (rather than all or nothing) (#25346)
- Operator name separate from class (no more `_PythonDecoratedOperator` when using TaskFlow) (#22834)

## Contributors

Thanks to everyone who contributed to this release, including Andrey Anshin, Ash Berlin-Taylor, Bartłomiej Hirsz, Brent Bovenzi, Chenglong Yan, D. Ferruzzi, Daniel Standish, Ephraim Anierobi, Jarek Potiuk, Jed Cunningham, Josh Fell, Mark Norman Francis, Niko, Tzu-ping Chung, Vincent, Wojciech Januszek, blag, chethanuk-plutoflume, eladkal, pierrejeambrun, and everyone else who commited, all 152 of you! You are what makes Airflow the successful project that is is!
