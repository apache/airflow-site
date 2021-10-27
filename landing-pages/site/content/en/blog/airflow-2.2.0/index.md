---
title: "What's new in Apache Airflow 2.2.0"
linkTitle: "What's new in Apache Airflow 2.2.0"
author: "Jed Cunningham"
github: "jedcunningham"
linkedin: "jedidiah-cunningham"
description: "We're proud to announce that Apache Airflow 2.2.0 has been released."
tags: [Release]
date: "2021-10-11"
---

I’m proud to announce that Apache Airflow 2.2.0 has been released. It contains over 600 commits since 2.1.4 and includes 30 new features, 84 improvements, 85 bug fixes, and many internal and doc changes.

**Details**:

📦 PyPI: https://pypi.org/project/apache-airflow/2.2.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/2.2.0/ \
🛠️ Changelog: https://airflow.apache.org/docs/apache-airflow/2.2.0/changelog.html \
🐳 Docker Image: docker pull apache/airflow:2.2.0 \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-2.2.0

As the changelog is quite large, the following are some notable new features that shipped in this release.

## Custom Timetables (AIP-39)

Airflow has historically used cron expressions and timedeltas to represent when a DAG should run. This worked for a lot of use cases, but not all. For example, running daily on Monday-Friday, but not on weekends wasn’t possible.

To provide more scheduling flexibility, determining when a DAG should run is now done with Timetables. Of course, backwards compatibility has been maintained - cron expressions and timedeltas are still fully supported, however, timetables are pluggable so you can add your own custom timetable to fit your needs! For example, you could write a timetable to schedule a DagRun

`execution_date` has long been confusing to new Airflowers, so as part of this change a new concept has been added to Airflow to replace it named `data_interval`, which is the period of data that a task should operate on. The following are now available:

- `logical_date` (aka `execution_date`)
- `data_interval_start` (same value as `execution_date` for cron)
- `data_interval_end` (aka `next_execution_date`)

If you write your own timetables, keep in mind they should be idempotent and fast as they are used in the scheduler to create DagRuns.

More information can be found at: [Customizing DAG Scheduling with Timetables](https://airflow.apache.org/docs/apache-airflow/stable/howto/timetable.html)

## Deferrable Tasks (AIP-40)

Deferrable tasks allows operators or sensors to defer themselves until a light-weight async check passes, at which point they can resume executing. Most importantly, this results in the worker slot, and most notably any resources used by it, to be returned to Airflow. This allows simple things like monitoring a job in an external system or watching for an event to be much cheaper.

To support this feature, a new component has been added to Airflow, the triggerer, which is the daemon process that runs the asyncio event loop.

Airflow 2.2.0 ships with 2 deferrable sensors, `DateTimeSensorAsync` and `TimeDeltaSensorAsync`, both of which are drop-in replacements for the existing corresponding sensor.

More information can be found at:

[Deferrable Operators & Triggers](https://airflow.apache.org/docs/apache-airflow/stable/concepts/deferring.html)

## Custom `@task` decorators and `@task.docker`

Airflow 2.2.0 allows providers to create custom `@task` decorators in the TaskFlow interface.

The `@task.docker` decorator is one such decorator that allows you to run a function in a docker container. Airflow handles getting the code into the container and returning xcom - you just worry about your function. This is particularly useful when you have conflicting dependencies between Airflow itself and tasks you need to run.

More information on creating custom `@task` decorators can be found at: [Creating Custom @task Decorators](https://airflow.apache.org/docs/apache-airflow/stable/howto/create-custom-decorator.html)

More information on the `@task.docker` decorator can be found at: [Using the Taskflow API with Docker or Virtual Environments](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html#using-the-taskflow-api-with-docker-or-virtual-environments)

## Validation of DAG params

You can now apply validation on DAG params by passing a `Param` object for each param. The `Param` object supports the full [json-schema validation specifications](https://json-schema.org/draft/2020-12/json-schema-validation.html).

Currently this only functions with manually triggered DAGs, but it does set the stage for future params related functionality.

More information can be found at: [Params](https://airflow.apache.org/docs/apache-airflow/stable/concepts/params.html)

## Other small features

This isn’t a comprehensive list, but some noteworthy or interesting small features include:

- Testing Connections from the UI - test the credentials for your Connection actually work
- Duplication Connections from the UI
- DAGs “Next run” info is shown in the UI, including when the run will actually start
- `airflow standalone` command runs all of the Airflow components directly without docker - great for local development

## Contributors

Thanks to everyone who contributed to this release: Andrew Godwin, Ash Berlin-Taylor, Brent Bovenzi, Elad Kalif, Ephraim Anierobi, James Timmins, Jarek Potiuk, Jed Cunningham, Josh Fell, Kamil Breguła, Kaxil Naik, Malthe Borch, Sam Wheating, Sumit Maheshwari, Tzu-ping Chung and many others
