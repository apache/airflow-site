---
title: "Testing in Airflow Part 1 - DAG Validation Tests DAG, Definition Tests and Unit Tests"
linkTitle: "Testing in Airflow Part 1 - DAG Validation Tests, DAG Definition Tests and Unit Tests"
author: "Chandu Kavar"
twitter: "chandukavar"
github: "chandulal"
linkedin: "chandu-kavar-627a209b"
description: "To know how to test the validity of DAGs, typos, cyclicity, upstream and downstream dependencies and custom operator/sensors."
tags: ["Testing"]
date: "2020-01-03"
---
Testing is an integral part of any software system to build confidence and increase the reliability of the system. Recently, I joined Grab and here at Grab, we are using Airflow to create and manage pipelines. But, we were facing issues with Airflow. I had a conversation with my engineering manager and discussed on how we could make Airflow reliable and testable.
Before Grab, I worked with ThoughtWorks. They are using TDD (Test Driven Development) methodology in almost all the projects. As a matter of fact, everyone is very cognizant about testing. This motivated me to explore testing in Airflow.
I spent a weekend Googling. But, I didn’t find any good articles on airflow test covering all the aspects, there are only a handful of articles available. I felt it’s worth to write and share a blog on airflow testing.

You can find more details on how to write these tests with examples in [Testing in Airflow Part 1](https://blog.usejournal.com/testing-in-airflow-part-1-dag-validation-tests-dag-definition-tests-and-unit-tests-2aa94970570c).
