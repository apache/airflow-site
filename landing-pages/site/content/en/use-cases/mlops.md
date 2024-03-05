---
title: "MLOps"
linkTitle: "MLOps"
quote:
    text: "Airflow is the heart of the modern MLOps stack, orchestrating the entire machine learning lifecycle."
    author: "Tamara Fingerlin"
logo: "mlops.png"
blocktype: use-case
---

<div style="display: flex; justify-content: center; align-items: center;">

# Use Airflow for Machine Learning Operations (MLOps)

</div>

</br>

Machine Learning Operations (MLOps) is a broad term encompassing everything needed to run machine learning models in production. MLOps is a rapidly evolving field with many different best practices and behavioral patterns, with Apache Airflow providing tool agnostic orchestration capabilities for all steps. An emerging subset of MLOps is Large Language Model Operations (LLMOps), which focuses on developing pipelines around applications of large language models like GPT-4 or Command.

The following video shows an example of using Airflow and Weaviate to create an automatic RAG pipeline that ingests and embeds data from news articles and provides trading advice. You can find the code shown in this example [here](https://github.com/astronomer/use-case-airflow-llm-rag-finance).

<div style="display: flex; justify-content: center; align-items: center; border: 2px solid #ccc; width: 75%; margin: auto; padding: 20px;">
    <video controls style="width: 100%; display: block;">
        <source src="/usecase-videos/placeholder_video_mlops.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

</br>
</br>

## Why use Airflow for MLOps?

</br>

Airflow is a popular choice for orchestrating MLOps workflows because it is:

- **Python native**: You use Python code to define Airflow pipelines, which makes it easy to integrate the most popular machine learning tools and embed your ML operations in a best practice CI/CD workflow. By using the decorators of the TaskFlow API you can turn existing scripts into Airflow tasks.
- **Extensible**: Airflow itself is written in Python, which makes it extensible with [custom modules](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html) and [Airflow plugins](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/plugins.html).
- **Data agnostic**: Airflow is data agnostic, which means it can be used to orchestrate any data pipeline, regardless of the data format or storage solution. You can plug in any new data storage, such as the latest vector database or your favorite RDBMS, with minimal effort.

</br>
</br>

## Airflow features for MLOps

</br>

Airflow has several key features that make it a great option for orchestrating MLOps workflows:

- **Monitoring and alerting**: Airflow comes with production-ready monitoring and alerting modules like Airflow notifiers, extensive logging features, and Airflow listeners. They enable you to have fine-grained control over how you monitor your ML operations and how Airflow alerts you if something goes wrong.
- **Features for day 2 ops**: Simple features like automatic retries, complex dependencies and branching logic, as well as the option to make pipelines dynamic make a big difference when orchestrating MLOps pipelines. Airflow has all of these built-in.
- **[Airflow providers](https://airflow.apache.org/docs/apache-airflow-providers/index.html)**: Airflow providers extend core Airflow functionality with additional modules to simplify integration with popular data tools, including many popular MLOps tools. You can find a list of active providers [here](https://airflow.apache.org/docs/#active-providers).