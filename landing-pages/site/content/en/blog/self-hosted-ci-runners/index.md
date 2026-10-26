---
title: "Apache Airflow CI Now Runs Trusted Builds on Self-Hosted Runners"
linkTitle: "Apache Airflow CI Now Runs Trusted Builds on Self-Hosted Runners"
author: "Shahar Epstein"
github: "shahar1"
description: "Following AIP-118, the canary builds and other trusted Apache Airflow CI runs now use self-hosted runners in the project's AWS account, managed with RunsOn."
tags: [Development]
date: "2026-10-26"
---

Apache Airflow's CI shares GitHub-hosted runner capacity with the other Apache Software Foundation projects,
and our large scheduled test runs compete for it.
[AIP-118: Self-hosted runners for Apache Airflow CI](https://cwiki.apache.org/confluence/x/-JXwGg),
accepted by lazy consensus, moves part of that load to ephemeral Linux runners in the project's AWS account,
paid for with AWS credits granted to the project. GitHub Actions still orchestrates every run.

## What runs where

Since [apache/airflow#74889](https://github.com/apache/airflow/pull/74889) was merged on October 25, 2026:

- **Canary builds**, the scheduled full runs of `main` on AMD and ARM, use self-hosted runners.
- **Pull requests that committers open from branches of `apache/airflow`** use self-hosted runners.
- **Pull requests from forks** stay on GitHub-hosted runners. A committer can move one to self-hosted runners
  by adding the `use self-hosted runners` label, approving its latest commit, and then closing and reopening
  the pull request. A new push sends it back to GitHub-hosted runners until a committer approves again.

Pull requests opened by bots, or labeled `use public runners`, also stay on GitHub-hosted runners. The full
rules are in the
[selective checks documentation](https://github.com/apache/airflow/blob/main/dev/breeze/doc/ci/04_selective_checks.md#self-hosted-runson-vs-public-runners).

## Choosing an approach

The AIP compared three approaches: AWS CodeBuild, a self-managed EKS cluster and [RunsOn](https://runs-on.com).
It chose RunsOn because it ran the same CI with minimal setup, needs no Kubernetes cluster for the project
to maintain, and is already used by other Apache projects. The choice does not lock the project in: the AIP
keeps the EKS approach as a fallback.

## Thank you

RunsOn offers its software free of charge to open-source projects in exchange for a public link back, and
Apache Airflow's self-hosted CI runs under that open-source license. Thank you to the RunsOn team for this
contribution to the open-source community, and thank you to AWS for the credits that pay for the runners.

To learn how organizations support the ASF as a whole, see
[ASF sponsorship](https://www.apache.org/foundation/sponsorship.html).
