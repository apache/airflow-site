---
title: "RancherBySUSE"
linkTitle: "RancherBySUSE"
quote:
    text: "Apache Airflow helps us orchestrate the construction and release of our curated collection of containers"
    author: "Ruben Pardo"
logo: "rancher-suse.svg"
---
#### What was the problem?

Our aim was to build, package, test and distribute curated and trusted containers at scale in an automated way. Those containers can be of any nature, meaning that we need a solution that allows us to build any kind of software with any kind of building tools like Maven, Rust, Java, Ant, or Go.

The construction of these containers requires the installation of several libraries (which may even conflict) and the orchestration of complex workflows with several integrations, executed either on a scheduled basis or triggered by events from external systems.

Finally, our building pipeline will be triggered by the release of sources upstream. This means that we need to trigger our pipeline whenever a new version is released by the owner of the software.

##### How did Apache Airflow help to solve this problem?

Apache Airflow has proven to be the perfect solution for implementing and controlling our pipelines. Its capability to orchestrate complex workflows programmatically and monitor their execution is complemented by a comprehensive graphical interface and detailed logs view.

Being extendable with a high-level language like Python has allowed us to customize our workflows as code with incredible flexibility and quality. Apache Airflow has enabled us to dynamically create and execute tasks derived from external sources, scheduling them to run in batches, thus reliably executing large-scale processes.

Apache Airflow also allows the execution of dependent tasks across nodes of different natures. This helped us to orchestrate the steps to build each container on the appropriate worker node. It offers multiple pre-built functionalities to facilitate integrations with external APIs, notifying events via Slack or e-mail as they occur. Its ability to isolate task execution allows us to scale, sparing us the need to worry about low-level details. Its complete REST API has allowed us to trigger workflows through events produced by external sources.

#### What are the results?

Thanks to Apache Airflow, we have been able to automate the lifecycle for the creation of our collections of containers in record time. We can execute concurrent processes much faster and more reliably, controlling aspects such as upstream failure handling or task-level concurrency, through configuration in a straightforward manner.

---
