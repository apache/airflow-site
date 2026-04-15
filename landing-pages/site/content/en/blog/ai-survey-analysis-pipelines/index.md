---
title: "Ask Your Survey Anything: Building AI Analysis Pipelines with Airflow 3"
linkTitle: "AI Survey Analysis Pipelines with Airflow 3"
authors:
  - name: "Vikram Koka"
    github: "vikramkoka"
    linkedin: "vikramkoka"
description: "A walkthrough of two natural language analysis pipelines over the 2025 Airflow Community Survey, covering an interactive human-in-the-loop version and a fully automated scheduled version, using operators from the common.ai and common.sql providers."
tags: [Community, Tutorial]
date: "2026-04-15"
---

The [2025 Airflow Community Survey](https://airflow.apache.org/survey/) collected responses
from nearly 6,000 practitioners across 168 questions. You can open a spreadsheet and filter,
or write SQL by hand. But what if you could just ask a question and have Airflow figure out
the query, run it, and bring the result back for your approval?

This post builds two pipelines that do exactly that, using the
[`apache-airflow-providers-common-ai`](https://pypi.org/project/apache-airflow-providers-common-ai/)
provider released with Airflow 3.

The first pipeline is **interactive**: a human reviews the question before it reaches the LLM
and approves the result before the DAG finishes. The second is **scheduled**: it downloads
fresh survey data, validates the schema, runs the query unattended, and emails the result.

If you haven't seen the [common.ai provider overview](https://airflow.apache.org/blog/common-ai-provider/) yet, start there for a tour of all the
operators. This post goes deep on a concrete end-to-end example.


## Two Pipelines, One Example File

Both DAGs live in
[`example_llm_survey_analysis.py`](https://github.com/apache/airflow/tree/main/providers/common/ai/src/airflow/providers/common/ai/example_dags/example_llm_survey_analysis.py)
and share the same schema context and datasource configuration.

**`example_llm_survey_interactive`**: trigger manually, review at both ends:

```
prompt_confirmation  →  generate_sql  →  run_query  →  extract_data  →  result_confirmation
(HITLEntryOperator)     (LLMSQLQuery)    (Analytics)    (@task)          (ApprovalOperator)
```

**`example_llm_survey_scheduled`**: runs `@monthly`, no human in the loop:

```
download_survey  →  prepare_csv  →  check_schema  →  generate_sql  →  run_query  →  extract_data  →  send_result
(HttpOperator)      (@task)         (LLMSchema       (LLMSQLQuery)    (Analytics)    (@task)          (@task / Email)
                                     Compare)
```


## The Data

The [Airflow Community Survey 2025](https://airflow.apache.org/survey/) CSV has 5,856 rows
and 168 columns covering everything from Airflow version and executor type to cloud provider,
company size, and AI tool usage. A few highlights from the data:

- **3,320** respondents identify as Data Engineers
- **2,032** use AWS as their primary cloud provider for Airflow
- **1,445** are already running Airflow 3
- **1,351** say they *often* use AI tools to write Airflow code

Those last two numbers together are part of why this example exists: the people most likely
to use this pipeline are already using Airflow 3 and already using AI in their workflow.

> **Data prep note:** Apache DataFusion is strict about CSV schemas. The raw survey export
> has 22 duplicate `"Other"` column names and some free-text cells with embedded newlines.
> Both need cleaning before DataFusion will parse the file. The interactive DAG assumes a
> cleaned copy at the path set by the `SURVEY_CSV_PATH` environment variable. The scheduled
> DAG downloads the file at runtime and the `prepare_csv` step handles writing it to disk.


## The Interactive Pipeline

Five tasks. No external services beyond your LLM provider and a local copy of the CSV.

| Step | Operator | What happens |
|---|---|---|
| 1 | `HITLEntryOperator` | DAG pauses. Human reviews and optionally edits the question. |
| 2 | `LLMSQLQueryOperator` | LLM translates the confirmed question into SQL, validated by sqlglot. |
| 3 | `AnalyticsOperator` | Apache DataFusion executes the SQL against the local CSV. |
| 4 | `@task extract_data` | Strips the query from the JSON result so the reviewer sees only data rows. |
| 5 | `ApprovalOperator` | DAG pauses again. Human approves or rejects the result. |

The LLM and DataFusion steps run unattended. The human shows up at step 1 to confirm the
question and at step 5 to sign off on the answer. Everything in between is automated.

```python
@dag
def example_llm_survey_interactive():

    prompt_confirmation = HITLEntryOperator(
        task_id="prompt_confirmation",
        subject="Review the survey analysis question",
        params={
            "prompt": Param(
                "How does AI tool usage for writing Airflow code compare "
                "between Airflow 3 users and Airflow 2 users?",
                type="string",
                description="The natural language question to answer via SQL",
            )
        },
        response_timeout=datetime.timedelta(hours=1),
    )

    generate_sql = LLMSQLQueryOperator(
        task_id="generate_sql",
        prompt="{{ ti.xcom_pull(task_ids='prompt_confirmation')['params_input']['prompt'] }}",
        llm_conn_id=LLM_CONN_ID,
        datasource_config=survey_datasource,
        schema_context=SURVEY_SCHEMA,
    )

    run_query = AnalyticsOperator(
        task_id="run_query",
        datasource_configs=[survey_datasource],
        queries=["{{ ti.xcom_pull(task_ids='generate_sql') }}"],
        result_output_format="json",
    )

    @task
    def extract_data(raw: str) -> str:
        results = json.loads(raw)
        data = [row for item in results for row in item["data"]]
        return json.dumps(data, indent=2)

    result_data = extract_data(run_query.output)

    result_confirmation = ApprovalOperator(
        task_id="result_confirmation",
        subject="Review the survey query result",
        body=result_data,
        response_timeout=datetime.timedelta(hours=1),
    )

    prompt_confirmation >> generate_sql >> run_query
```


## Walking Through a Run

**Step 1: Prompt confirmation.** Trigger the DAG and navigate to the HITL review tab.
The default question appears in an editable field. Change it to anything the schema supports,
or leave it as-is and confirm.

> *"How does AI tool usage for writing Airflow code compare between Airflow 3 users and Airflow 2 users?"*

**Step 2: SQL generation.** `LLMSQLQueryOperator` receives the confirmed question, constructs
a system prompt from `SURVEY_SCHEMA`, and calls the LLM. It returns validated SQL. sqlglot
parses the output and rejects anything that isn't a `SELECT`. The generated query goes to XCom.

```sql
SELECT
    "Which version of Airflow do you currently use?"                                AS airflow_version,
    "Are you using AI/LLM (ChatGPT/Cursor/Claude etc) to assist you in writing Airflow code?" AS ai_usage,
    COUNT(*) AS respondents
FROM survey
WHERE "Which version of Airflow do you currently use?" IS NOT NULL
  AND "Are you using AI/LLM (ChatGPT/Cursor/Claude etc) to assist you in writing Airflow code?" IS NOT NULL
GROUP BY airflow_version, ai_usage
ORDER BY airflow_version, respondents DESC
```

**Step 3: DataFusion execution.** `AnalyticsOperator` loads the CSV into a DataFusion
`SessionContext`, registers it as the `survey` table, and executes the SQL in-process.
No database server, no network call. The 5,856-row CSV runs in under a second.

**Step 4: Extract data.** The raw JSON from `AnalyticsOperator` includes the original
query string alongside the result rows. This `@task` strips the query so the reviewer
isn't looking at SQL when they should be looking at data.

**Step 5: Result confirmation.** The data rows appear in the Airflow UI approval dialog.
The analyst reads the result, clicks Approve (or Reject if something looks off), and the
DAG completes.


## The Scheduled Pipeline

The scheduled variant adds three capabilities the interactive version intentionally omits:
data acquisition, schema validation, and result delivery. It runs `@monthly` (configurable)
with no human steps.

| Step | Operator | What happens |
|---|---|---|
| 1 | `HttpOperator` | Downloads the survey CSV from `airflow.apache.org`. |
| 2 | `@task prepare_csv` | Writes the CSV to disk and generates a reference schema file from `SURVEY_SCHEMA`. |
| 3 | `LLMSchemaCompareOperator` | LLM compares the downloaded CSV schema against the reference. Raises if critical columns are missing or renamed. |
| 4 | `LLMSQLQueryOperator` | Translates the fixed question into validated SQL. |
| 5 | `AnalyticsOperator` | Executes the SQL via DataFusion. |
| 6 | `@task extract_data` | Extracts data rows from the JSON result. |
| 7 | `@task send_result` | Sends the result via `SmtpHook` if `SMTP_CONN_ID` and `NOTIFY_EMAIL` are set, otherwise logs to the task log. |

The schema check at step 3 is worth calling out. `LLMSchemaCompareOperator` compares the
live download against a reference file derived from `SURVEY_SCHEMA`. If the survey format
changes between runs (a renamed column, a dropped field), the operator catches it before
any SQL runs, rather than failing silently mid-pipeline with a cryptic DataFusion error.

```python
@dag
def example_llm_survey_scheduled():

    download_survey = HttpOperator(
        task_id="download_survey",
        http_conn_id=AIRFLOW_WEBSITE_CONN_ID,
        endpoint=SURVEY_CSV_ENDPOINT,
        method="GET",
        response_filter=lambda r: r.text,
        log_response=False,
    )

    @task
    def prepare_csv(csv_text: str) -> None:
        os.makedirs(os.path.dirname(SURVEY_CSV_PATH), exist_ok=True)
        with open(SURVEY_CSV_PATH, "w", encoding="utf-8") as f:
            f.write(csv_text)
        columns = [line.split('"')[1] for line in SURVEY_SCHEMA.strip().splitlines() if '"' in line]
        with open(REFERENCE_CSV_PATH, "w", newline="", encoding="utf-8") as ref:
            csv_mod.writer(ref).writerow(columns)

    csv_ready = prepare_csv(download_survey.output)

    check_schema = LLMSchemaCompareOperator(
        task_id="check_schema",
        prompt="Compare the survey CSV schema against the reference. Flag missing or renamed columns.",
        llm_conn_id=LLM_CONN_ID,
        data_sources=[survey_datasource, reference_datasource],
        context_strategy="basic",
    )
    csv_ready >> check_schema

    generate_sql = LLMSQLQueryOperator(
        task_id="generate_sql",
        prompt=SCHEDULED_PROMPT,
        llm_conn_id=LLM_CONN_ID,
        datasource_config=survey_datasource,
        schema_context=SURVEY_SCHEMA,
    )
    check_schema >> generate_sql

    run_query = AnalyticsOperator(
        task_id="run_query",
        datasource_configs=[survey_datasource],
        queries=["{{ ti.xcom_pull(task_ids='generate_sql') }}"],
        result_output_format="json",
    )

    @task
    def extract_data(raw: str) -> str:
        results = json.loads(raw)
        data = [row for item in results for row in item["data"]]
        return json.dumps(data, indent=2)

    result_data = extract_data(run_query.output)

    @task
    def send_result(data: str) -> None:
        if SMTP_CONN_ID and NOTIFY_EMAIL:
            from airflow.providers.smtp.hooks.smtp import SmtpHook
            with SmtpHook(smtp_conn_id=SMTP_CONN_ID) as hook:
                hook.send_email_smtp(
                    to=NOTIFY_EMAIL,
                    subject=f"Airflow Survey Analysis: {SCHEDULED_PROMPT}",
                    html_content=f"<pre>{data}</pre>",
                )
        else:
            print(f"Survey analysis result:\n{data}")

    generate_sql >> run_query >> result_data >> send_result(result_data)
```


## Connecting Your LLM

Both DAGs use `llm_conn_id="pydanticai_default"`. Create a connection in the Airflow UI:

| Provider | Connection type | Required fields |
|---|---|---|
| OpenAI | `pydanticai` | Password: API key. Extra: `{"model": "openai:gpt-4o"}` |
| Anthropic | `pydanticai` | Password: API key. Extra: `{"model": "anthropic:claude-haiku-4-5-20251001"}` |
| Google Vertex | `pydanticai-vertex` | Extra: `{"model": "google-vertex:gemini-2.0-flash", "project": "...", "vertexai": true}` |
| AWS Bedrock | `pydanticai-bedrock` | Extra: `{"model": "bedrock:us.anthropic.claude-opus-4-5", "region_name": "us-east-1"}` |

Switch providers by changing the connection. Neither DAG requires any code changes.

For the scheduled DAG, also create an HTTP connection named `airflow_website` with host
`https://airflow.apache.org` (no auth required), and optionally set the `SMTP_CONN_ID`
and `NOTIFY_EMAIL` environment variables to enable email delivery.


## What This Shows

Four capabilities come together across these two pipelines that haven't been easy to combine before:

**Natural language as the interface.** Neither pipeline requires the analyst to write SQL.
`LLMSQLQueryOperator` handles schema awareness, column quoting, and query structure. The
`SURVEY_SCHEMA` context is the only thing it needs.

**In-process query execution.** `AnalyticsOperator` runs Apache DataFusion inside the Airflow
worker. There's no database to configure, no connection to manage for the data itself. Point
it at a file URI and it runs.

**Schema-aware data validation.** `LLMSchemaCompareOperator` uses an LLM to compare schemas
and surface structural changes in plain language, not a column count diff, but an explanation
of what changed and why it matters for downstream queries. It turns a silent mid-pipeline
failure into an early, actionable error.

**Human oversight without blocking automation.** The `HITLEntryOperator` and `ApprovalOperator`
are standard Airflow operators from `airflow.providers.standard.operators.hitl`. They have no
AI imports. They just pause the DAG and wait. The interactive pipeline uses them at both ends;
the scheduled pipeline skips them entirely. Adding or removing human review requires no changes
to the LLM or DataFusion steps.


## Try It

Both DAGs are in the `common.ai` provider example DAGs:
[`example_llm_survey_analysis.py`](https://github.com/apache/airflow/tree/main/providers/common/ai/src/airflow/providers/common/ai/example_dags/example_llm_survey_analysis.py).

```bash
pip install 'apache-airflow-providers-common-ai' \
            'apache-airflow-providers-common-sql[datafusion]' \
            'apache-airflow-providers-http' \
            'apache-airflow-providers-smtp'   # optional, for email delivery
```

Requires Apache Airflow 3.0+. `apache-airflow-providers-standard` (which provides
`HITLEntryOperator` and `ApprovalOperator`) ships with Airflow 3 and does not need
a separate install.

For the interactive DAG: set `SURVEY_CSV_PATH` to your local copy of the survey CSV, create
a `pydanticai_default` connection, and trigger `example_llm_survey_interactive`.

For the scheduled DAG: create the `airflow_website` HTTP connection, set `SMTP_CONN_ID` and
`NOTIFY_EMAIL` if you want email delivery, and trigger `example_llm_survey_scheduled`.

To go further, the follow-on post [Agentic Workloads on Airflow 3](https://airflow.apache.org/blog/agentic-workloads-airflow-3/)
extends this example into a multi-query synthesis pattern, answering questions that require
querying several dimensions in parallel and synthesizing the results with a second LLM call.

Questions, feedback, and survey queries that stumped the LLM are all welcome on
[Airflow Slack](https://s.apache.org/airflow-slack) in `#airflow-ai`.
