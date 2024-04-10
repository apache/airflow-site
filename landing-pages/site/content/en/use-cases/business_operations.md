---
title: "Business Operations"
linkTitle: "Business Operations"
usecasedescription:
    text: "Many companies build their core business, data powered applications, on top of Apache Airflow."
logo: "business-ops.png"
blocktype: use-case
---

<div style="display: flex; justify-content: center; align-items: center;">

# Use Airflow for Business operations pipelines

</div>


Airflow can be the starting point for your business idea! For many companies, Airflow delivers the data that powers their core business applications. Whether you need to aggregate user data to power personalized recommendations, display analytics in a user-facing dashboard, or prepare the input data for an LLM, Airflow is the perfect orchestrator.

This video shows an example of using Airflow to run the pipelines that power a customer-facing analytics dashboard. You can find the code shown in this example [here](https://github.com/astronomer/business-operations-structure-example).


<div id="videoContainer" style="display: flex; justify-content: center; align-items: center; border: 2px solid #ccc; width: 75%; margin: auto; padding: 20px;">
    <a href="https://www.youtube.com/embed/2CEApKN0z1U?autoplay=1">
        <img id="videoPlaceholder" src="/usecase-video-placeholders/placeholder_business_ops_video.png" style="cursor: pointer; width: 100%; max-width: 560px;" alt="Click to play a one minute video showing the use case" title="Click to play video"/>
    </a>
</div>

</br>

## Why use Airflow for Business Operations?

Airflow is trusted and tested by many companies to deliver their data on time. Airflow is a popular choice to build your business upon, because it is:

- **Tool agnostic**: Using Airflow future-proofs your business, as it can be used to orchestrate actions in nearly any external tool or service. This means you can always switch to the newest and best tools, without needing to change your whole orchestration layer.
- **Extensible**: There are many Airflow modules available to connect to popular data tools, and you can write your own custom operators and hooks for specific use cases.
- **Dynamic**: In Airflow you can define [dynamic tasks](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html), which serve as placeholders to adapt at runtime based on changing input.
- **Scalable**: Airflow can be scaled to handle infinite numbers of tasks and workflows, given enough computing power. If you choose Airflow, your business will be able to grow with it.

</br>

## Airflow features for Business Operations

Airflow has several key features that make it a great option for orchestrating business operations:

- [**Dynamic task mapping**](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html): Oftentimes business operations are not static. You may design your pipelines to have one task per customer or report, and those lists will always be changing. Dynamic task mapping allows you to build flexibility into your pipelines, so they can adjust at runtime based on changing input.
- [**Datasets**](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/datasets.html): It is unlikely that you will have one team, much less one pipeline, responsible for all of the data that powers your business. Datasets allow you to make your pipelines event-based, scheduling them for when all data prerequisites are available rather than a specific time. With this type of scheduling, you can create smaller, more modular pipelines, that can be managed by the team responsible for that data, making your operations more efficient and easier to manage.
- [**Notifications**](https://airflow.apache.org/docs/apache-airflow-providers/core-extensions/notifications.html): When relying on an orchestrator to power your business applications, it's critical that you know promptly when something goes wrong. Airflow has a suite of notifications available so you can send alerts to your system of preference.
