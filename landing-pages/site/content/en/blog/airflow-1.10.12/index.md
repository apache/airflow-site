---
title: "Apache Airflow 1.10.12"
linkTitle: "Apache Airflow 1.10.12"
author: "Kaxil Naik"
twitter: "kaxil"
github: "kaxil"
linkedin: "kaxil"
description: "We are happy to present Apache Airflow 1.10.12"
tags: ["release"]
date: 2020-08-25
---

Airflow 1.10.12 contains 113 commits since 1.10.11 and includes 5 new features, 23 improvements, 23 bug fixes,
and several doc changes.

**Details**:

* **PyPI**: [https://pypi.org/project/apache-airflow/1.10.12/](https://pypi.org/project/apache-airflow/1.10.12/)
* **Docs**: [https://airflow.apache.org/docs/1.10.12/](https://airflow.apache.org/docs/1.10.12/)
* **Changelog**: [http://airflow.apache.org/docs/1.10.12/changelog.html](http://airflow.apache.org/docs/1.10.12/changelog.html)


**Airflow 1.10.11 has breaking changes with respect to
KubernetesExecutor & KubernetesPodOperator so I recommend users to directly upgrade to Airflow 1.10.12 instead**.

Some of the noteworthy new features (user-facing) are:

- [Allow defining custom XCom class](https://github.com/apache/airflow/pull/8560)
- [Get Airflow configs with sensitive data from Secret Backends](https://github.com/apache/airflow/pull/9645)
- [Add AirflowClusterPolicyViolation support to Airflow local settings](https://github.com/apache/airflow/pull/10282)

### Allow defining Custom XCom class

Until Airflow 1.10.11, the XCom data was only stored in Airflow Metadatabase. From Airflow 1.10.12, users
would be able to define custom XCom classes. This will allow users to transfer larger data between tasks.
An example here would be to store XCom in S3 or GCS Bucket if the size of data that needs to be stored is larger
than `XCom.MAX_XCOM_SIZE` (48 KB).

**PR**: https://github.com/apache/airflow/pull/8560

### Get Airflow configs with sensitive data from Secret Backends

Users would be able to get the following Airflow configs from Secrets Backend like Hashicorp Vault:

   - `sql_alchemy_conn` in [core] section
   - `fernet_key` in [core] section
   - `broker_url` in [celery] section
   - `flower_basic_auth` in [celery] section
   - `result_backend` in [celery] section
   - `password` in [atlas] section
   - `smtp_password` in [smtp] section
   - `bind_password` in [ldap] section
   - `git_password` in [kubernetes] section

Further improving Airflow's Secret Management story, from Airflow 1.10.12, users don't need to hardcode
the **sensitive** config value in airflow.cfg nor then need to use an Environment variable to set this config.

For example, the metadata database connection string can either be set in airflow.cfg like this:

```ini
[core]
sql_alchemy_conn_secret = sql_alchemy_conn
```
This will retrieve config option from the set Secret Backends.

As you can see you just need to add a `_secret` suffix at the end of the actual config option
and the value needs to be the **key** which the Secrets backend will look for.

Similarly, `_secret` config options can also be set using a corresponding environment variable. For example:

```
export AIRFLOW__CORE__SQL_ALCHEMY_CONN_SECRET=sql_alchemy_conn
```

More details: http://airflow.apache.org/docs/1.10.12/howto/set-config.html

### Add AirflowClusterPolicyViolation support to airflow_local_settings.py

Users can use Cluster Policies to apply cluster-wide checks on Airflow
tasks. You can raise [AirflowClusterPolicyViolation](http://airflow.apache.org/docs/1.10.12/_api/airflow/exceptions/index.html#airflow.exceptions.AirflowClusterPolicyViolation)
in a policy or task mutation hook to prevent a DAG from being
imported or prevent a task from being executed if the task is not compliant with
your check.

These checks are intended to help teams using Airflow to protect against common
beginner errors that may get past a code reviewer, rather than as technical
security controls.

For example, don't run tasks without `airflow` owners:

```python
def task_must_have_owners(task):
    if not task.owner or task.owner.lower() == conf.get('operators', 'default_owner'):
        raise AirflowClusterPolicyViolation(
            'Task must have non-None non-default owner. Current value: {}'.format(task.owner))
```

More details: http://airflow.apache.org/docs/1.10.12/concepts.html#cluster-policies-for-custom-task-checks

### Launch Pods via YAML files when using KubernetesExecutor and KubernetesPodOperator

As of 1.10.12, users can launch pods via YAML files instead of passing various configurations.

To allow greater flexibility we have deprecated Airflow's Pod class and instead now use classes and
objects from the official Kubernetes API. The POD class will still work but raise a deprecation
warning. This feature involved a pretty extensive rewrite of all of our pod creation code.

Initially, we were going to hold off on these features until Airflow 2.0. However, we soon
realized that exposing these features in 1.10.x is crucial in preparing users for the 2.0 release to come.

Details: https://github.com/apache/airflow/pull/6230 ([Backport commit](https://github.com/apache/airflow/commit/7aa0f472b57985a952a3e3d0a38f1b2535d93413))


## Updating Guide

If you are updating Apache Airflow from a previous version to `1.10.12`, please take a note of the following:

-   Run `airflow upgradedb` after `pip install -U apache-airflow==1.10.12` as `1.10.12` contains 1 database migration.

-   As of airflow 1.10.12, using the `airflow.contrib.kubernetes.Pod` class in the `pod_mutation_hook` is now
    deprecated. Instead we recommend that users treat the pod parameter as a `kubernetes.client.models.V1Pod` object.
    This means that users now have access to the full Kubernetes API when modifying airflow pods for mutating POD.

-   Previously, when tasks skipped by SkipMixin (such as `BranchPythonOperator`, `BaseBranchOperator` and
    `ShortCircuitOperator`) are cleared, they execute. Since 1.10.12, when such skipped tasks are cleared,
    they will be skipped again by the newly introduced `NotPreviouslySkippedDep`.


## Special Note

### Python 2
Python 2 has reached end of its life on Jan 2020. Airflow Master no longer supports Python 2.
Airflow 1.10.* would be the last series to support Python 2.

We strongly recommend users to use Python >= 3.6

### Use Airflow RBAC UI
Airflow 1.10.12 ships with 2 UIs, the default is non-RBAC Flask-admin based UI and Flask-appbuilder based UI.

The Flask-AppBuilder (FAB) based UI allows Role-based Access Control and has more advanced features compared to
the legacy Flask-admin based UI. This UI can be enabled by setting `rbac=True` in `[webserver]` section in
your `airflow.cfg`.

Flask-admin based UI is deprecated and new features won't be ported to it. This UI will still be the default
for 1.10.* series but would no longer be available from Airflow 2.0

### We have moved to GitHub Issues

The Airflow Project has moved from [JIRA](https://issues.apache.org/jira/projects/AIRFLOW/issues) to
[GitHub](https://github.com/apache/airflow/issues) for tracking issues.

So if you find any bugs in Airflow 1.10.12 please create a GitHub Issue for it.

## List of Contributors

According to git shortlog, the following people contributed to the 1.10.12 release. Thank you to all contributors!

Alexander Sutcliffe, Andy, Aneesh Joseph, Ash Berlin-Taylor, Aviral Agrawal, BaoshanGu, Beni Ben zikry,
Daniel Imberman, Daniel Standish, Danylo Baibak, Ephraim Anierobi, Felix Uellendall, Greg Neiheisel,
Hartorn, Jacob Ferriero, Jannik F, Jarek Potiuk, Jinhui Zhang, Kamil Breguła, Kaxil Naik, Kurganov,
Luis Magana, Max Arrich, Pete DeJoy, Sumit Maheshwari, Tomek Urbaszek, Vicken Simonian, Vinnie Guimaraes,
William Tran, Xiaodong Deng, YI FU, Zikun Zhu, dewaldabrie, pulsar314, retornam, yuqian90
