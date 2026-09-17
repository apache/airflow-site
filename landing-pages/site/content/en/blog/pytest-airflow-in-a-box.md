---
title: "Testing Apache Airflow Dags entirely inside pytest"
linkTitle: "Testing Apache Airflow Dags entirely inside pytest"
author: "nredd"
github: "nredd"
description: "pytest-airflow-in-a-box is a community-maintained pytest plugin for testing Apache Airflow Dags without a live Airflow deployment."
tags: [Community, Testing]
date: "2026-09-01"
---

> **Community project:** [`pytest-airflow-in-a-box`](https://github.com/nredd/pytest-airflow-in-a-box) is independently maintained. It is not part of, maintained by, or endorsed by the Apache Airflow project.

Airflow provides `dag.test()` for running a Dag in a local debugging environment. When a project needs to test many Dags as part of a pytest suite, it may also need reusable fixtures, isolated metadata, parallel execution, and test-friendly result objects.

[`pytest-airflow-in-a-box`](https://github.com/nredd/pytest-airflow-in-a-box) packages those capabilities as a pytest plugin for Dag authors. It auto-registers with pytest, creates an isolated metadata database when a test needs one, and supplies typed fixtures for Dags, Dag runs, task instances, sessions, and Dag bags.

## Install the plugin

For an Airflow 3 project, add the plugin to the development dependencies:

```bash
uv add --dev "pytest-airflow-in-a-box[airflow3]"
```

Or install it with pip:

```bash
pip install "pytest-airflow-in-a-box[airflow3]"
```

The plugin registers through pytest's entry-point mechanism, so projects do not need to declare it in `pytest_plugins`.

## Run a Dag in a test

The `dag_maker` fixture builds a Dag and can execute its tasks in dependency order:

```python
from airflow.sdk import task


def test_dag(dag_maker):
    with dag_maker():

        @task
        def produce():
            return 21

        @task
        def consume(value):
            return value * 2

        consume(produce())

    result = dag_maker.run()

    assert result.success
    assert result.xcoms == {"produce": 21, "consume": 42}
    assert result.order == ["produce", "consume"]
```

`dag_maker.run()` returns an inert result snapshot containing task states, XCom values, errors, and execution order. Tests can also execute a single task with `dag_maker.run_ti()`, exercise deferrable operators, use a live REST API fixture, or run DB-free task tests.

The plugin supports pytest-xdist as part of its execution model, allowing Airflow-facing tests to participate in a parallel test suite while keeping their state isolated. Consult the project's [requirements and compatibility information](https://github.com/nredd/pytest-airflow-in-a-box#requirements) before choosing an Airflow extra or interpreter version.

## Choosing the right testing surface

The plugin complements Airflow's built-in tools:

- Use `dag.test()` for local, interactive execution and debugging of an individual Dag.
- Use `pytest-airflow-in-a-box` when a Dag-authoring project benefits from pytest fixtures, isolated test state, parallel collection, or structured result assertions.
- Airflow's internal `tests_common` package remains the harness for testing Airflow itself; it is not published as an end-user Dag-testing package.

## Try it and contribute

- Read the [source and quickstart](https://github.com/nredd/pytest-airflow-in-a-box).
- Browse the [full documentation](https://nredd.github.io/pytest-airflow-in-a-box/).
- Install a release from [PyPI](https://pypi.org/project/pytest-airflow-in-a-box/).
- Report a problem or propose an improvement in the [issue tracker](https://github.com/nredd/pytest-airflow-in-a-box/issues).
