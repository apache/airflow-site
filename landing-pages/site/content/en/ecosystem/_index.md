---
title: "Ecosystem"
linkTitle: "Ecosystem"
menu:
  main:
    weight: 30
---

&nbsp;
&nbsp;

# Ecosystem

Those resources and services are not maintained, nor endorsed by the Apache Airflow Community and Apache Airflow project (maintained by the Committers and the Airflow PMC). Use them at your sole discretion. The community does not verify the licences nor validity of those tools, so it's your responsibility to verify them.

If you would you like to be included on this page, please reach out to the [Apache Airflow dev or user mailing list](https://airflow.apache.org/community/) and let us know or simply open a Pull Request to that page.

&nbsp;

## Learning resources

[Apache Airflow YouTube Channel](https://www.youtube.com/channel/UCSXwxpWZQ7XZ1WL3wqevChA) - Official YouTube Channel

[Airflow Summit](https://airflowsummit.org/) - Online conference for Apache Airflow developers

[Awesome Apache Airflow](https://github.com/jghoman/awesome-apache-airflow) - Curated list of resources about Apache Airflow

[The Complete Hands-On Introduction to Apache Airflow](https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow) by Marc Lamberti on Udemy

[Apache Airflow: Complete Hands-On Beginner to Advanced Class](https://www.udemy.com/course/apache-airflow-course) by Alexandra Abbas on Udemy

&nbsp;

## Airflow-As-A-Service

[Astronomer](https://www.astronomer.io/) - Managed Apache Airflow in Astronomer Cloud, or self-hosted within your environment

[Google Cloud Composer](https://cloud.google.com/composer) - Managed Apache Airflow service on Google Cloud Platform

[Qubole](https://qubole.com) - Managed Apache Airflow Service on all major public clouds

[Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow) - Managed Apache Airflow on Amazon Web Services (AWS)

&nbsp;

## Tools integrating with Airflow

[afctl](https://github.com/qubole/afctl) - A CLI tool that includes everything required to create, manage and deploy airflow projects faster and smoother.

[airflow-aws-executors](https://github.com/aelzeiny/airflow-aws-executors) - Run Airflow Tasks directly on AWS Batch, AWS Fargate, or AWS ECS; provisioning less infra is more.

[airflow-code-editor](https://github.com/andreax79/airflow-code-editor) - A plugin for Apache Airflow that allows you to edit DAGs in browser.

[airflow-diagrams](https://github.com/feluelle/airflow-diagrams) - Auto-generated Diagrams from Airflow DAGs

[airflow-maintenance-dags](https://github.com/teamclairvoyant/airflow-maintenance-dags) - [Clairvoyant](https://clairvoyantsoft.com/) has a repo of Airflow DAGs that operator on Airflow itself, clearing out various bits of the backing metadata store.

[AirflowK8sDebugger](https://github.com/Javier162380/AirflowKuberentesDebugger) - A library for generate k8s pod yaml templates from an Airflow dag using the KubernetesPodOperator.

[Airflow Ditto](https://github.com/angadsingh/airflow-ditto) - An extensible framework to do transformations to an Airflow DAG and convert it into another DAG which is flow-isomorphic with the original DAG, to be able to run it on different environments (e.g. on different clouds, or even different container frameworks - Apache Spark on YARN vs Kubernetes). Comes with out-of-the-box support for EMR-to-HDInsight-DAG transforms.

[Airflow ECR Plugin](https://github.com/asandeep/airflow-ecr-plugin) - Plugin to refresh AWS ECR login token at regular intervals. This is helpful where DockerOperator needs to pull images hosted on ECR.

[Airflow Plugins](https://github.com/airflow-plugins/) - Central collection of repositories of various plugins for Airflow, including mailchimp, trello, sftp, GitHub, etc.

[Chartis](https://github.com/trejas/chartis) - Python package to convert Common Workflow Language (CWL) into Airflow DAG.

[CWL-Airflow](https://github.com/Barski-lab/cwl-airflow) - Python package to extend Apache-Airflow 1.10.11 functionality with CWL v1.2 support.

[dag-factory](https://github.com/ajbosco/dag-factory) - A library for dynamically generating Apache Airflow DAGs from YAML configuration files.

[Dag Dependencies viewer](https://github.com/ms32035/airflow-dag-dependencies) - A plugin which creates a view to visualize dependencies between the Airflow DAGs

[Databand](https://databand.ai/) - Observability platform built on top of Airflow.

[dbt (data build tool)](https://docs.getdbt.com/) - Data transformation tool, [dbt jobs can be scheduled using Airflow](https://docs.getdbt.com/docs/running-a-dbt-project/running-dbt-in-production/#using-airflow).

[GeniumCloud](https://geniumcloud.com) - One-Stop-Shop Platform for rapid build, scheduling and control Airflow workflows via completely new UI. Out of the box comprehensive Airflow infrastructure monitoring, integration with alerting systems and service adoption from small to enterprise organizations. The easiest way to manage complex workflows.

[gusty](https://github.com/chriscardillo/gusty) - Create a DAG using any number of YAML, Python, Jupyter Notebook, or R Markdown files that represent individual tasks in the DAG. gusty also configures dependencies, DAGs, and TaskGroups, features support for your local operators, and more. A fully containerized demo is available [here](https://github.com/chriscardillo/gusty-demo).

[Meltano](https://www.meltano.com/) - Open source, self-hosted, CLI-first, debuggable, and extensible ELT tool that embraces [Singer](https://www.singer.io) for extraction and loading, leverages [dbt](https://www.getdbt.com) for transformation, and [integrates with Airflow for orchestration](https://meltano.com/#orchestration).

[Oozie to Airflow](https://github.com/GoogleCloudPlatform/oozie-to-airflow) - A tool to easily convert between [Apache Oozie](http://oozie.apache.org/) workflows and Apache Airflow workflows.

[Pylint-Airflow](https://github.com/BasPH/pylint-airflow) - A Pylint plugin for static code analysis on Airflow code.

[whirl](https://github.com/godatadriven/whirl) - Fast iterative local development and testing of Apache Airflow workflows.
