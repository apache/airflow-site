---
title: "Infrastructure Management"
linkTitle: "Infrastructure Management"
usecasedescription:
    text: "With Airflow you can spin up, manage and tear down your infrastructure at the exact time you need it."
logo: "infrastructure-management.png"
blocktype: use-case
---

<div style="display: flex; justify-content: center; align-items: center;">

# Use Airflow for Infrastructure Management

</div>

Airflow can interact with any API, which makes it a great tool to manage your infrastructure, such as Kubernetes or Spark clusters running in any cloud. As of Airflow 2.7, the setup/teardown feature is available, a special type of task with intelligent behavior to spin up and tear down infrastructure at the exact time you need it.

Infrastructure management is often needed within the context of other use cases, such as MLOps, or implementing data quality checks. This video shows an example of how it might be used for an MLOps pipeline. You can find the code shown in this example [here](https://github.com/astronomer/use-case-setup-teardown-data-quality).

<div id="videoContainer" style="display: flex; justify-content: center; align-items: center; border: 2px solid #ccc; width: 75%; margin: auto; padding: 20px;">
    <a href="https://www.youtube.com/embed/JkURWnl76GQ?autoplay=1">
        <img id="videoPlaceholder" src="/usecase-video-placeholders/placeholder_infra_video.png" style="cursor: pointer; width: 100%; max-width: 560px;" alt="Click to play a one minute video showing the use case" title="Click to play video"/>
    </a>
</div>

</br>

## Why use Airflow for Infrastructure Management

Airflow is a popular choice for pipelines that require managing infrastructure because it is:

- **Python native**: Pipelines as Python code make it easy to turn custom functions into tasks. Any logic you need to manage your infrastructure, you can implement in Airflow with Python.
- **Extensible**: Infrastructure management is needed for many use cases, including MLOps, data quality checks, and more. Airflow's flexibility and wide array of providers makes it suitable for any use case that you may need to implement.
- **Scalable**: Airflow can be scaled to handle infinite numbers of tasks and workflows, given enough computing power. If you choose Airflow, your business will be able to grow with it.


## Airflow features for Infrastructure Management

Airflow 2.7 implemented a new key feature that makes it an even greater option for managing infrastructure:

- [**Setup/teardown tasks**](https://airflow.apache.org/docs/apache-airflow/stable/howto/setup-and-teardown.html): Setup/teardown tasks are a special type of task that can be used to manage the infrastructure needed to run other tasks. They have special behavior to support the pattern of setting up resources and configuration (e.g. a Spark cluster or other compute resources) before a task runs, and then tearing down that infrastructure after the task has completed, even if the task fails.
