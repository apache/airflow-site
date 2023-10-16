---
title: "Snapp"
linkTitle: "Snapp"
quote:
    text: "Airflow implementation resulted in significant time savings, increased productivity, and improved operational efficiency for our Map team at Snapp."
    author: "Tadeh Alexani"
logo: "snapp-logo.svg"
---

##### What was the problem?
As the Map team at Snapp, one of the largest and fastest-growing internet companies in the Middle East, we have experienced significant growth over the past couple of years, expanding from a team of 7 to a team of 60. However, with this growth came the realization that some of our crucial tasks were being performed manually. This manual approach consumed valuable time and hindered our ability to execute these tasks efficiently.

To address this challenge and streamline our operations, we recognized the need for an orchestration tool that could automate these tasks, saving time, and energy, and increasing reliability and monitoring for our runs. After conducting thorough research and evaluating various options, we ultimately decided to implement Airflow. Airflow is widely regarded as the leading open-source platform for task orchestration, making it an ideal choice for the diverse use cases of our Map team.

By leveraging Airflow, we aim to automate our critical tasks, enabling us to execute them more efficiently and effectively. This automation will not only enhance our productivity but also provide us with greater control and visibility over our workflows. With Airflow's robust features and flexibility, we are confident that it will significantly improve our team's performance and contribute to the continued success of Snapp.

##### How did Apache Airflow help to solve this problem?
After implementing Apache Airflow on our cloud platform, specifically utilizing the KubernetesExecutor, we experienced a significant improvement in our task management capabilities. With Airflow, each sub-team within the Map team was able to create and manage their own DAGs, automating various tasks seamlessly. This included essential procedures such as data updates, model training pipelines, and project deployments, leveraging the SparkKubernetesOperator and other relevant tools.

One notable example of Airflow's impact was the creation of a DAG specifically designed to update the traffic congestion colorization for our streets. This DAG runs every 10 minutes, ensuring that our congestion data remains up-to-date and accurate. The intuitive Airflow UI also proved to be invaluable, as it enabled our non-technical teammates to easily work with DAGs and monitor their progress.

By utilizing Airflow, we have not only automated our tasks but also improved collaboration and efficiency within our team. The ability to manage and monitor workflows through Airflow has significantly reduced manual effort and increased reliability. We are now able to focus more on analyzing and utilizing the data rather than spending time on repetitive and time-consuming manual tasks. Overall, Apache Airflow has proven to be an indispensable tool for our Map team, enabling us to streamline our operations and achieve greater productivity.

##### What are the results?
The implementation of Airflow has yielded significant results for our team. By automating and scheduling various tasks, ranging from data-related operations to deployments and data updates for the Map, we have successfully saved approximately 40 hours of manual work per week. This substantial time savings has allowed our team members to focus on more strategic and value-added activities, ultimately enhancing our overall productivity.

Furthermore, Airflow's intuitive UI has enhanced visibility into our workflows. We can easily check DAG and task logs through the Airflow UI, enabling us to monitor the progress and performance of our tasks effectively. This improved visibility has not only increased our confidence in the reliability of our processes but has also facilitated troubleshooting and issue resolution, leading to smoother operations and reduced downtime.

Overall, the results of implementing Airflow have been highly beneficial for our team. The significant reduction in manual work hours has freed up valuable time and resources, allowing us to allocate them towards more critical tasks. Additionally, the improved visibility and monitoring capabilities offered by Airflow have enhanced our operational efficiency and reliability. We are extremely pleased with the positive impact Airflow has had on our team's productivity and look forward to leveraging its capabilities further in the future.
