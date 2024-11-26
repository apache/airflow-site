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

These resources and services are not maintained, nor endorsed by the Apache Airflow® Community and Apache Airflow project (maintained by the Committers and the Airflow PMC). Use them at your sole discretion. The community does not verify the licences nor validity of those tools, so it's your responsibility to verify them.

If you would you like to be included on this page, please reach out to the [Apache Airflow dev or user mailing list](https://airflow.apache.org/community/) and let us know or simply open a Pull Request to that page.

&nbsp;

## Learning resources

[Apache Airflow YouTube Channel](https://www.youtube.com/channel/UCSXwxpWZQ7XZ1WL3wqevChA) - Official YouTube Channel

[Airflow Summit](https://airflowsummit.org/) - Conference for Apache Airflow developers

[Awesome Apache Airflow](https://github.com/jghoman/awesome-apache-airflow) - Curated list of resources about Apache Airflow

[Astronomer Academy](https://academy.astronomer.io/) - Full courses and certifications available by the Education team at Astronomer

[The Complete Hands-On Introduction to Apache Airflow](https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow) by Marc Lamberti on Udemy

[Apache Airflow: Complete Hands-On Beginner to Advanced Class](https://www.udemy.com/course/apache-airflow-course) by Alexandra Abbas on Udemy

[Data Pipelines with Apache Airflow](https://www.manning.com/books/data-pipelines-with-apache-airflow) Apache Airflow Book on Amazon

&nbsp;

## Airflow as a Service

[Astro](https://www.astronomer.io/product) - Provided by Astronomer, Astro is the modern data orchestration platform, powered by Apache Airflow. Astro enables data engineers, data scientists, and data analysts to build, run, and observe pipelines-as-code.

[Google Cloud Composer](https://cloud.google.com/composer) - Managed Apache Airflow service on Google Cloud Platform

[Amazon Managed Workflows for Apache Airflow](https://aws.amazon.com/managed-workflows-for-apache-airflow) - Managed Apache Airflow on Amazon Web Services (AWS)

[Azure Data Factory Managed Airflow](https://learn.microsoft.com/azure/data-factory/concept-managed-airflow) - Managed Apache Airflow service on Azure

[Yandex Managed Service for Apache Airflow](https://cloud.yandex.com/en/services/managed-airflow) - Managed Apache Airflow on Yandex Cloud

[Airflow with Restack](https://www.restack.io/store/airflow) - Managed Apache Airflow on Restack Cloud or bring your own cloud: AWS EKS, GCP GKE, or Azure AKS. Allowing you to use the latest version of Airflow with your own DAGs. Connect your repo to the Restack GitHub app for built-in CI/CD.

[DoubleCloud Managed Service for Apache Airflow](https://double.cloud/services/managed-airflow/) - Managed Apache Airflow on DoubleCloud platform.

&nbsp;

## Other deployments methods

[Airflow Heroku Deployment](https://github.com/slyapustin/airflow-on-heroku) - Airflow Heroku Deployment allows creating a demo Airflow instance in just a couple of clicks.

[Self-Managed Airflow via CNDI](https://github.com/polyseam/cndi) - Toolkit for deploying Airflow Kubernetes clusters, with support for AWS, GCP, Azure, VMWare, Bare-Metal, and even multi/hybrid cloud support. See [docs](https://docs.cndi.run) for more details.

[Self-managed Airflow on Amazon EKS](https://github.com/awslabs/data-on-eks/tree/main/schedulers/terraform/self-managed-airflow) - Self-managed Airflow on Amazon EKS provides a guide for deploying self-managed Apache Airflow on [Amazon EKS](https://aws.amazon.com/eks/) with [Terraform](https://www.terraform.io/) using Data on EKS Blueprints with the [Terraform Data add-ons](https://registry.terraform.io/modules/aws-ia/eks-data-addons/aws/latest) module, check out the [Data on EKS Airflow blueprint](https://awslabs.github.io/data-on-eks/docs/blueprints/job-schedulers/self-managed-airflow).

[Amazon MWAA Terraform Module](https://github.com/aws-ia/terraform-aws-mwaa) allows you to deploy Amazon Managed Workflows for Apache Airflow using the official Terraform module. For a full example on how to use Amazon MWAA, check out the [Data on EKS MWAA blueprint](https://awslabs.github.io/data-on-eks/docs/blueprints/job-schedulers/aws-managed-airflow).

&nbsp;

## Third Party Airflow Plugins and Providers

[Astronomer Registry](https://registry.astronomer.io/) - The discovery and distribution hub for Apache Airflow integrations created to aggregate and curate the best bits of the ecosystem.

[Airflow Plugins](https://github.com/airflow-plugins/) - Central collection of repositories of various plugins for Airflow, including mailchimp, trello, sftp, GitHub, etc.

[Airflow ECR Plugin](https://github.com/asandeep/airflow-ecr-plugin) - Plugin to refresh AWS ECR login token at regular intervals. This is helpful where DockerOperator needs to pull images hosted on ECR.

[Airflow OpenMLDB Provider](https://github.com/4paradigm/OpenMLDB/tree/main/extensions/airflow-provider-openmldb) - Airflow OpenMLDB Provider containing Operators for Feature Extraction on OpenMLDB.

[Airflow Apache Mesos Provider](https://github.com/AVENTER-UG/airflow-provider-mesos/blob/master/README.md) - Airflow Apache Mesos Provider containing Scheduler to scale out with Apache Mesos.

[Airflow Netezza Provider](https://github.com/sanjay-rendu/apache-airflow-providers-nz) - Airflow Provider to connect with [Netezza](https://www.ibm.com/products/netezza) using [nzpy](https://github.com/IBM/nzpy)

[Airflow Grafana Loki Provider](https://github.com/snjypl/airflow-provider-grafana-loki) - Provides Hook and LogHandler that integrates with [Grafana Loki](https://grafana.com/oss/loki/). This provides a LogHandler for writing and reading Task Logs to and from Grafana Loki.

[Airflow SAS Provider](https://github.com/sassoftware/sas-airflow-provider) - Provides Hook and Operators for creating Airflow tasks to execute [SAS](https://sas.com) Studio Flows and Jobs.

[Airflow Cloudera Provider](https://github.com/cloudera/cloudera-airflow-plugins/tree/main/cloudera_airflow_provider) - Provides Hooks and Operators to interact and run your workloads onto Cloudera Data Platform Services

[Airflow Alembic Provider](https://github.com/astronomer/airflow-provider-alembic) - Provides Hooks and Operators to run Database Migrations with Alembic

[Airflow Pulumi Provider](https://github.com/astronomer/airflow-provider-pulumi) - Provides Hooks and Operators to manage Infrastructure-as-Code with Pulumi

[Airflow DolphinDB Provider](https://github.com/dolphindb/airflow-provider-dolphindb) - Provides Hooks and Operators to run scripts with [DolphinDB](https://www.dolphindb.com).

[Airflow TM1 Provider](https://github.com/airflow-provider-tm1/airflow-provider-tm1) - Provides Hook and Operators to simplify connecting to the IBM Cognos TM1 / Planning Analytics database over REST API.

[Astronomer Cosmos](https://github.com/astronomer/astronomer-cosmos) - Run your dbt Core projects as Apache Airflow DAGs and Task Groups with a few lines of code.

[Airflow OpenTelemetry Provider](https://github.com/howardyoo/airflow_otel_provider) - Provides Hook and EventListener which will generate traces, metrics, and logs in [OpenTelemetry](https://opentelemetry.io/) for your DAG runs.

[Airflow Couchbase Provider](https://github.com/Couchbase-Ecosystem/airflow-providers-couchbase) - Provides Hook to seamlessly interact with Couchbase databases, execute queries, manage documents, and more.

&nbsp;

## Async Providers

[Astronomer Providers](https://github.com/astronomer/astronomer-providers) - A collection of Async Operators and Sensors for Apache Airflow built and maintained by Astronomer.

[Airflow Kafka Provider](https://github.com/astronomer/airflow-provider-kafka) - Apache Airflow Kafka provider containing Deferrable Operators & Sensors.

&nbsp;

## Third Party Airflow Helm Charts

Apache Airflow releases the [Official Apache Airflow Community Chart](https://airflow.apache.org/docs/helm-chart/stable/index.html) as of early 2021 but historically there were few other popular charts

[User Community Chart](https://github.com/airflow-helm/charts) - the user community managed chart that has existed since 2018 and was previously called [stable/airflow](https://github.com/helm/charts/tree/master/stable/airflow) on the official (now deprecated) Helm Charts repo.

[Bitnami Chart](https://github.com/bitnami/charts/tree/master/bitnami/airflow) - Bitnami manages a number of charts and the Airflow chart is one of those

[Astronomer Chart](https://github.com/astronomer/airflow-chart) - The chart managed by Astronomer Chart. This was the original chart that the Official Airflow Community chart is based on (it was donated by Astronomer)

&nbsp;

## Tools integrating with Airflow

[ADA](https://github.com/IBM/ada) - A microservice created to retrieve analytics metrics from an Airflow database instance.

[as-scraper](https://github.com/Avila-Systems/as-scraper) - An integration with Selenium to build & mantain web scrapers inside Airflow.

[afctl](https://github.com/qubole/afctl) - A CLI tool that includes everything required to create, manage and deploy airflow projects faster and smoother.

[airflint](https://github.com/feluelle/airflint) - Enforce Best Practices for all your Airflow DAGs.

[airflow-aws-executors](https://github.com/aelzeiny/airflow-aws-executors) - Run Airflow Tasks directly on AWS Batch, AWS Fargate, or AWS ECS; provisioning less infra is more.

[airflow-code-editor](https://github.com/andreax79/airflow-code-editor) - A tool for Apache Airflow that allows you to edit DAGs in browser.

[airflow-diagrams](https://github.com/feluelle/airflow-diagrams) - Auto-generated Diagrams from Airflow DAGs

[airflow-maintenance-dags](https://github.com/teamclairvoyant/airflow-maintenance-dags) - [Clairvoyant](https://clairvoyantsoft.com/) has a repo of Airflow DAGs that operator on Airflow itself, clearing out various bits of the backing metadata store.

[AirflowK8sDebugger](https://github.com/Javier162380/AirflowKuberentesDebugger) - A library for generate k8s pod yaml templates from an Airflow dag using the KubernetesPodOperator.

[Airflow Ditto](https://github.com/angadsingh/airflow-ditto) - An extensible framework to do transformations to an Airflow DAG and convert it into another DAG which is flow-isomorphic with the original DAG, to be able to run it on different environments (e.g. on different clouds, or even different container frameworks - Apache Spark on YARN vs Kubernetes). Comes with out-of-the-box support for EMR-to-HDInsight-DAG transforms.

[Amundsen](https://github.com/amundsen-io/amundsen) - Amundsen is a data discovery and metadata platform for improving the productivity of data analysts, data scientists and engineers when interacting with data. It can surface which Airflow task generates a given table.

[Apache-Liminal-Incubating](https://github.com/apache/incubator-liminal) -  Liminal provides a domain-specific-language (DSL) to build ML/AI workflows on top of Apache Airflow. Its goal is to operationalise the machine learning process, allowing data scientists to quickly transition from a successful experiment to an automated pipeline of model training, validation, deployment and inference in production.

[Astro CLI](https://docs.astronomer.io/astro/cli/overview) - The Astro CLI is the easiest way to get a local Airflow server for prototyping and development.

[Astro SDK](https://github.com/astronomer/astro-sdk) - Astro SDK allows rapid and clean development of Extract, Load, Transform workflows using Python and SQL, powered by Apache Airflow and maintained by Astronomer.

[Chartis](https://github.com/trejas/chartis) - Python package to convert Common Workflow Language (CWL) into Airflow DAG.

[CWL-Airflow](https://github.com/Barski-lab/cwl-airflow) - Python package to extend Apache-Airflow 1.10.11 functionality with CWL v1.2 support.

[DAGify](https://github.com/GoogleCloudPlatform/dagify) - A Python tool which converts Control-M workflows to Airflow DAGs.

[dag-factory](https://github.com/ajbosco/dag-factory) - A library for dynamically generating Apache Airflow DAGs from YAML configuration files.

[Dag Dependencies viewer](https://github.com/ms32035/airflow-dag-dependencies) - A tool which creates a view to visualize dependencies between the Airflow DAGs

[data-dag](https://github.com/rearc-data/data-dag) - A library for building factories to dynamically generate DAGs from data (such as YAML files)

[Databand](https://databand.ai/) - Observability platform built on top of Airflow.

[DataHub](https://datahubproject.io/) - A metadata platform for the modern data stack. It can automatically [collect lineage and other metadata](https://datahubproject.io/docs/metadata-ingestion#lineage-with-airflow) from Airflow.

[dbt (data build tool)](https://docs.getdbt.com/) - Data transformation tool, [dbt jobs can be scheduled using Airflow](https://docs.getdbt.com/docs/running-a-dbt-project/running-dbt-in-production/#using-airflow).

[Domino](https://github.com/Tauffer-Consulting/domino) - Domino is an open source Graphical User Interface platform for creating data and Machine Learning workflows (DAGs) with no-code, visually intuitive drag-and-drop actions. It is also a standard for publishing and sharing your Python code so it can be automatically used by anyone, directly in the GUI.

[Elyra](https://github.com/elyra-ai/elyra) - Elyra provides a visual editor that enables data scientists to create AI pipelines in a low-code/no-code fashion.

[GeniumCloud](https://geniumcloud.com) - One-Stop-Shop Platform for rapid build, scheduling and control Airflow workflows via completely new UI. Out of the box comprehensive Airflow infrastructure monitoring, integration with alerting systems and service adoption from small to enterprise organizations. The easiest way to manage complex workflows.

[gusty](https://github.com/chriscardillo/gusty) - Create a DAG using any number of YAML, Python, Jupyter Notebook, or R Markdown files that represent individual tasks in the DAG. gusty also configures dependencies, DAGs, and TaskGroups, features support for your local operators, and more. A fully containerized demo is available [here](https://github.com/chriscardillo/gusty-demo).

[Marquez](https://marquezproject.ai) - Marquez is an open source metadata service that maintains data provenance, shows how datasets are consumed and produced and centralizes dataset lifecycle management. Marquez can be used with Apache Airflow as an OpenLineage backend.

[Meltano](https://www.meltano.com/) - Open source, self-hosted, CLI-first, debuggable, and extensible ELT tool that embraces [Singer](https://www.singer.io) for extraction and loading, leverages [dbt](https://www.getdbt.com) for transformation, and [integrates with Airflow for orchestration](https://meltano.com/#orchestration).

[Nexla](https://www.nexla.com/) - Build, transform, and manage data flows to and from databases, APIs, streams, SaaS services, events, and even emails. Use Nexla's Airflow Operator to trigger flows to start in other Operators when your Nexla flow finishes running.

[Oozie to Airflow](https://github.com/GoogleCloudPlatform/oozie-to-airflow) - A tool to easily convert between [Apache Oozie](http://oozie.apache.org/) workflows and Apache Airflow workflows.

[OpenLineage](https://openlineage.io) - An open standard for the collection of data lineage, which can be used to trace the path of datasets as they traverse multiple systems including Apache Airflow.

[Panda Patrol](https://github.com/aivanzhang/panda_patrol#-panda-patrol) - Test and profile your data right within your Airflow DAGs. With dashboards and alerts already pre-built.

[PowerBI-Airflow-Plugin](https://github.com/ambika-garg/PowerBI_Airflow_Plugin) - The Airflow plugin for Power BI includes a custom Airflow operator designed to refresh Power BI datasets.

[Pylint-Airflow](https://github.com/BasPH/pylint-airflow) - A Pylint plugin for static code analysis on Airflow code.

[Redactics](https://www.redactics.com) - A managed appliance (built on Airflow) installed next to your databases that powers a growing collection of data management workflows.

[simple-dag-editor](https://github.com/ohadmata/simple-dag-editor) - Zero configuration Airflow tool that let you manage your DAG files.

[Viewflow](https://github.com/datacamp/viewflow) - An Airflow-based framework that allows data scientists to create data models without writing Airflow code.

[whirl](https://github.com/godatadriven/whirl) - Fast iterative local development and testing of Apache Airflow workflows.

[ZenML](https://github.com/zenml-io/zenml) - Run your machine learning specific pipelines on Airflow, easily integrating with your existing data science tools and workflows.

[Airflow Vscode Extension](https://github.com/necatiarslan/airflow-vscode-extension) This is a VSCode extension for Apache Airflow 2+. You can trigger your DAGs, pause/unpause DAGs, view execution logs, explore source code and do much more.

[Airflow Provider Template](https://github.com/angreal/airflow-provider) - Template and commands for creating and testing airflow provider packages.

[Airflow Template](https://github.com/angreal/airflow) - Template and commands for creating minimal airflow environments for rapid testing and prototyping.

&nbsp;

## Airflow Provider System Test Dashboards

[Amazon provider package health dashboard](https://aws-mwaa.github.io/open-source/system-tests/dashboard.html) - Dashboard listing all system tests within the Amazon provider package and their current health status: last execution status (succeeded/failed, average duration, ...).

[Google provider package health dashboard](https://storage.googleapis.com/providers-dashboard-html/dashboard.html) - Dashboard listing all system tests within the Google provider package and their current health status

[LLM Providers health dashboard](https://astronomer.github.io/llm-dags-dashboard) - Dashboard listing all system tests within the LLM provider packages and their current health status: execution status for last 7 runs(succeeded/failed, Execution date).

[Teradata Provider health dashboard](https://teradata.github.io/airflow/) - Dashboard listing status of system tests for Teradata Provider and their current health status for last runs.
