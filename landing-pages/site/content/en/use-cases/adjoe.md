---
title: "adjoe"
linkTitle: "adjoe"
quote:
    text: "Deploying Airflow allowed us to efficiently manage workloads with multiple DAGs, from generating reports and system analyses to training machine learning models and preparing datasets."
    author: "Tadeh Alexani"
logo: "adjoe-logo.svg"
blocktype: "testimonial"
---

##### What was the problem?
Before adopting Airflow at adjoe, we handled job scheduling in two main ways: by setting up Kubernetes cronjobs or building AWS Lambda functions. While both approaches had their benefits, they also came with limitations, especially when it came to managing more complex workloads. As our data science teams needs evolved, it became clear that we needed a more robust and flexible orchestration tool.

##### How did Apache Airflow help to solve this problem?
With the creation of a new AWS environment for the data science teams, we introduced Airflow on Kubernetes as our primary orchestration solution, addressing both stability and scalability requirements.

After deploying Airflow in our staging and production environments, we were able to create multiple DAGs to manage and schedule a variety of workloads efficiently. These range from generating and emailing daily reports to performing system analyses, training complex machine learning models using the Spark Operator or Kubeflow’s Training Operator for GPU models, and preparing datasets using Airflow’s ETL capabilities.

##### What are the results?
By implementing Airflow, our data scientists can now manage and schedule their jobs more efficiently. Monitoring job statuses has become simpler, thanks to an intuitive interface that also provides easy access to logs. The need for infrastructure management has significantly reduced, allowing data scientists to test and deploy their DAGs independently, which in turn has accelerated development for both teams. Currently, our Data Science teams manages over 20 DAGs and more than 50 tasks, with plans to double the number of DAGs by the end of the next quarter.
