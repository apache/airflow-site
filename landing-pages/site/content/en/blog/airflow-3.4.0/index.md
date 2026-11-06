---
title: "Apache Airflow 3.4.0: Task Loops, Dags in Any Language, and AI Agents"
linkTitle: "Apache Airflow 3.4.0: Task Loops, Dags in Any Language, and AI Agents"
author: "Rahul Vats"
github: "vatsrahul1001"
linkedin: "vats-rahul"
description: "Apache Airflow 3.4.0 introduces bounded Task Loops for iterative workflows, Dag authoring beyond Python (TypeScript, Go, Java, and YAML) on the new AIP-85 Dag Importer, and a maturing Common AI provider for running LLM and agent tasks with built-in human approval."
tags: [Release]
date: "2026-11-06"
images: ["/blog/airflow-3.4.0/images/3.4.0.jpg"]
---

We're proud to announce the release of **Apache Airflow 3.4.0**! Where 3.3 gave your *tasks* memory and task bodies in multiple languages, 3.4 is about **shape and reach**. It brings **Task Loops**, a native loop primitive for workflows that repeat until they are done; the ability to author an entire Dag in TypeScript, Go, Java, or YAML rather than only Python; and a steadily maturing `common.ai` provider that turns LLM calls and agents into ordinary Airflow tasks, complete with human approval.

**🎯 Release Highlights**

📦 PyPI: https://pypi.org/project/apache-airflow/3.4.0/ \
📚 Docs: https://airflow.apache.org/docs/apache-airflow/3.4.0/ \
🛠️ Release Notes: https://airflow.apache.org/docs/apache-airflow/3.4.0/release_notes.html \
🐳 Docker Image: `docker pull apache/airflow:3.4.0` \
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-3.4.0

# 🔁 Task Loops (AIP-111): Workflows That Repeat Until They Are Done

Some workflows do not have a fixed shape. You walk a tree of unknown depth, you refine an estimate until the error is small enough, or you run an agentic *generate → score → refine* loop until the output is good. Until now you reached for hard-coding a fixed depth or for Dags that trigger themselves. Airflow 3.4 makes **bounded, sequential iteration** a native concept.

{{< figure src="images/loops_running_graph.png" alt="The refine loop of refine_estimate in the Graph view, running its third of up to ten iterations" caption="The `refine_estimate` Dag below, part-way through a run. The `refine` task group is a loop on its third of up to ten iterations: `improve` is running, then `evaluate` and the `accurate_enough` gate run and decide whether to go round again. `finished` waits until the loop is done." >}}

Before we go any further, it is worth addressing one thing: “How can you have loops in a Dag, given DAG stands for Directed Acyclic Graph”. The answer to that is by being very careful. Essentially, there is no dependency loop introduced, the tasks in the Dag still do form a cycle-free graph. The looping nature is handled at runtime only.

Call `.loop()` on a decorated task group to repeat it a number of times decided at runtime, where each iteration can build on the result of the last. It behaves like a `do … while` loop with a hard cap:

```python
from airflow.sdk import dag, task, task_group


@dag(tags=["example"])
def refine_estimate():
    @task_group
    def refine():
        @task
        def improve(*, loop):
            # First pass starts from 1.0; later passes read the previous result.
            estimate = 1.0 if loop.index == 1 else loop.previous["estimate"]
            return (estimate + 2.0 / estimate) / 2.0

        @task
        def evaluate(estimate):
            return {"estimate": estimate, "error": abs(estimate * estimate - 2.0)}

        evaluate(improve())

    def accurate_enough(*, loop):
        return loop.result["error"] < 0.000001

    @task
    def finished():
        print("Refinement finished.")

    refinement = refine.loop(max_iterations=10, until=accurate_enough)
    refinement >> finished()


refine_estimate()
```

## Key Capabilities

- **`max_iterations`**: a required upper bound, so a loop can never run away.
- **`until`**: an optional predicate function that decides when to stop, or omit it entirely for a loop that runs a fixed number of times. Because the body runs before the check, it always runs at least once.
- **A `loop` context object** inside the body and the predicate: `loop.index` (the 1-based current pass), `loop.previous` (the last iteration's result), and `loop.result` (for the predicate).
- **Lazy materialization**: Airflow only creates the next iteration when the loop decides to continue, so you do not see a tail of skipped iterations.
- **Composable**: loops work with `.partial()` for body arguments, `.override()` for group config, and even `.expand()` to run mapped tasks *inside* a loop.

A loop with a fixed count (no `until`) always runs exactly `max_iterations` times and succeeds. If a loop reaches `max_iterations` while its `until` predicate is still `False`, meaning it never converged, the final iteration is marked failed, so a failure to converge surfaces as a real failure. The Airflow UI gains dedicated loop views so you can see each iteration's history at a glance.

{{< figure src="images/loops_running_iterations.png" alt="The Iterations tab of the running refine loop: iteration 3 in progress, with the reason the loop continued after iterations 1 and 2" caption="The loop's Iterations tab during the same run. Each finished iteration shows why its gate let the loop continue, here the error still being above the target, and iteration 3 is still running. To record a reason, the `until` function can return a `LoopDecision(stop=..., reason=...)` instead." >}}

> A few limits to know: loops cannot be nested, a loop cannot sit inside a mapped task group (though mapped tasks inside loops are okay), and a whole loop cannot itself be mapped.

For detailed usage, see the [loops authoring guide](https://airflow.apache.org/docs/apache-airflow/3.4.0/authoring-and-scheduling/loops.html).

{{< figure src="images/loops_review.png" alt="A Dag combining Common AI tasks, Loops, and HITL to provide human feedback to future rounds." caption="The third iteration of a `draft-and-review` loop, waiting for input. The graph shows the dag at iteration 3 of a max of 5. On the right, the reviewer reads the agent's draft and types feedback. *Request changes* runs the loop again with that feedback fed back to the next round, and *Approve* ends stops the loop early." >}}


# 🌐 Write Airflow Dags in TypeScript, Java and Go

Airflow 3.3 let you write individual *tasks* in Java or Go while Python still owned the Dag. Airflow 3.4 takes the next step: you can define the entire Dag, including its schedule, tasks and dependencies, in TypeScript, Java or Go, with no Python file involved. All three SDKs are generally available.

This is powered by **AIP-85, the Dag Importer**, a pluggable framework that teaches the Dag processor to read Dag sources beyond `.py`. Each format registers an importer. For a language SDK, the Dag processor runs the language's runtime to read the Dags an artifact declares, and Airflow then treats them exactly like Python Dags. The same framework also powers an opt-in YAML importer.

## What's supported

Each SDK works in two modes, and one artifact can serve both: a **Dag definition** declares the whole Dag in the SDK's language, which is what 3.4 adds, and a **Python Dag with stub TaskHandler** implements the `@task.stub` tasks of a Python Dag, including their TaskFlow arguments. A Dag definition supports Dag and task options under Airflow's own names, one queue for all of a Dag's tasks, TaskFlow inputs from task results and literals, order-only dependencies (`before` / `after`), nested task groups, edge labels, if / else and switch / case branching, and triggering another Dag's run. Task code can use Variables, Connections, XCom and the task state store. An artifact can hold several Dags, including Dags generated in a loop, and the Code view shows each Dag's own source file. All of this works the same in TypeScript, Java and Go, and the TypeScript SDK adds human-in-the-loop tasks (approval, `hitl`).

## The same Dag declared in three languages

Each example below declares the same Dag, `orders_daily`:

- the `extract` task group counts orders for two regions,
- `summarize` adds them up,
- `has_orders` runs `load` when there are orders, and `alert` when there are none,
- `pick_report` picks a full or a brief report,
- `trigger_finance` starts a run of the `finance_close` Dag after `load`, on a labeled edge.

The UI screenshot in each tab is of a separate real Dag authored with that SDK, not the `orders_daily` snippet itself.

<details name="sdk-dag" data-tab="typescript" data-sync-group="sdk" open>
<summary>TypeScript</summary>

A handler takes one object of named arguments, and calling a task names its inputs. The calls you write are the dependencies, and the compiler checks each one.

```typescript
import { Bundle, Dag, label, triggerDagRun } from "apache-airflow-ts-sdk";

const dag = new Dag("orders_daily", { schedule: "@daily", tags: ["orders"], queue: "typescript" });

// A task group: its task ids are "extract.eu" and "extract.us".
const extract = dag.taskGroup("extract");
const eu = extract.task("eu", async (): Promise<number> => 120)();
const us = extract.task("us", async (): Promise<number> => 80)();

// TaskFlow: passing a task's result draws the dependency and delivers the value.
const summarize = dag.task("summarize", async ({ eu, us }: { eu: number; us: number }) => eu + us);
const total = summarize({ eu, us });

const load = dag.task("load", async ({ total, table }: { total: number; table: string }) => {
  console.log(`Loading ${total} orders into ${table}`);
});
const loaded = load({ total, table: "warehouse.orders" });
const alerted = dag.task("alert", async () => console.log("No orders today"))();

// if / else: the side not taken is skipped.
const hasOrders = async ({ total }: { total: number }) => total > 0;
dag.if(hasOrders, { total }, { taskId: "has_orders" }).then(loaded).else(alerted);

// switch / case: the decider returns the task to run.
const full = dag.task("report_full", async () => console.log("Full report"))();
const brief = dag.task("report_brief", async () => console.log("Brief report"))();
const pickReport = async ({ total }: { total: number }) => (total > 1000 ? full : brief);
dag.switch(pickReport, { total }, { taskId: "pick_report" }).case(full).case(brief);

// Trigger another Dag after the load, on a labeled edge.
const triggered = dag.task("trigger_finance", triggerDagRun({ dagId: "finance_close" }))();
loaded.before(label(triggered, "hand off"));

await new Bundle(dag).serve();
```

![The TypeScript `storefront_daily_orders` Dag in the Airflow UI, with its packed `bundle.min.mjs` in the Code view](images/multilang-run-typescript.png)

</details>
<details name="sdk-dag" data-tab="java" data-sync-group="sdk">
<summary>Java</summary>

Annotations carry the configuration. A `@Airflow.Deps` class wires the graph through a view that the annotation processor generates, so `javac` type-checks every edge. An interface-based API (`DagDef`, `dag.task(...)`) is also available.

```java
package com.example;

import static java.lang.System.Logger.Level.INFO;

import org.apache.airflow.sdk.*;

@Airflow.Dag(id = "orders_daily", schedule = "@daily", tags = {"orders"}, queue = "java")
public class OrdersDaily {
  private static final System.Logger log = System.getLogger(OrdersDaily.class.getName());

  // A task group: its task ids are "extract.eu" and "extract.us".
  @Airflow.TaskGroup(id = "extract")
  static class Extract {
    @Airflow.Task
    public long eu() { return 120L; }

    @Airflow.Task
    public long us() { return 80L; }
  }

  @Airflow.Task
  public long summarize(long eu, long us) { return eu + us; }

  @Airflow.Task
  public void load(long total, String table) {
    log.log(INFO, "Loading {0} orders into {1}", total, table);
  }

  @Airflow.Task
  public void alert() { log.log(INFO, "No orders today"); }

  // if / else: the side not taken is skipped.
  @Airflow.If(id = "has_orders")
  public boolean hasOrders(long total) { return total > 0; }

  @Airflow.Task(id = "report_full")
  public void reportFull() { log.log(INFO, "Full report"); }

  @Airflow.Task(id = "report_brief")
  public void reportBrief() { log.log(INFO, "Brief report"); }

  // switch / case: the decider returns the class generated for the task to run.
  @Airflow.Switch(id = "pick_report")
  public Class<? extends Task> pickReport(long total) {
    return total > 1000 ? OrdersDailyBuilder.ReportFull.class : OrdersDailyBuilder.ReportBrief.class;
  }

  // Trigger another Dag. This method runs when the Dag is built, not when the task runs.
  @Airflow.Task(id = "trigger_finance")
  public TriggerDagRun triggerFinance() { return new TriggerDagRun("finance_close"); }

  // Each call is a task, and passing its result to another call draws the dependency.
  @Airflow.Deps
  static class Wiring implements OrdersDailyDeps {
    void depends() {
      var total = summarize(extract().eu(), extract().us());
      var loaded = load(total, lit("warehouse.orders"));
      hasOrders(total).Then(loaded).Else(alert());
      pickReport(total).Case(reportFull()).Case(reportBrief());
      loaded.before(Flow.label(triggerFinance(), "hand off"));
    }
  }

  public static void main(String[] args) {
    Server.create(args).serve(new Bundle().register(OrdersDaily.class));
  }
}
```

![The Java `risk_fraud_screening` Dag in the Airflow UI, with its `.jar` source in the Code view](images/multilang-run-java.png)

</details>
<details name="sdk-dag" data-tab="go" data-sync-group="sdk">
<summary>Go</summary>

`Inputs` passes task results and literals to a task function, in parameter order. A task's id is its function's name unless a `TaskSpec` sets one.

```go
package main

import (
    "log"

    "github.com/apache/airflow/go-sdk/airflow"
)

func main() {
    bundle := airflow.Bundle()
    bundle.Register(ordersDaily())
    if err := bundle.Serve(); err != nil {
        log.Fatal(err)
    }
}

func ordersDaily() *airflow.DagRef {
    dag := airflow.Dag("orders_daily", airflow.DagSpec{
        Schedule: "@daily",
        Tags:     []string{"orders"},
        Queue:    "golang",
    })

    // A task group: its task ids are "extract.eu" and "extract.us".
    extract := dag.TaskGroup("extract")
    eu := extract.Task(countOrders, airflow.TaskSpec{TaskID: "eu"}, airflow.Inputs(airflow.Literal("eu")))
    us := extract.Task(countOrders, airflow.TaskSpec{TaskID: "us"}, airflow.Inputs(airflow.Literal("us")))

    // TaskFlow: passing a task's result draws the dependency and delivers the value.
    total := dag.Task(summarize, airflow.Inputs(eu, us))
    loaded := dag.Task(load, airflow.Inputs(total, airflow.Literal("warehouse.orders")))

    // if / else: the side not taken is skipped.
    dag.If(hasOrders, airflow.TaskSpec{TaskID: "has_orders"}, airflow.Inputs(total)).
        Then(loaded).
        Else(dag.Task(alert))

    // switch / case: the decider returns the task to run.
    r := &reports{
        full:  dag.Task(reportFull, airflow.TaskSpec{TaskID: "report_full"}),
        brief: dag.Task(reportBrief, airflow.TaskSpec{TaskID: "report_brief"}),
    }
    dag.Switch(r.pick, airflow.TaskSpec{TaskID: "pick_report"}, airflow.Inputs(total)).
        Case(r.full).
        Case(r.brief)

    // Trigger another Dag after the load, on a labeled edge.
    triggered := dag.Task(
        airflow.TriggerDagRun(airflow.TriggerDagRunSpec{DagID: "finance_close"}),
        airflow.TaskSpec{TaskID: "trigger_finance"},
    )
    loaded.Before(airflow.Label(triggered, "hand off"))

    return dag
}

var ordersByRegion = map[string]int{"eu": 120, "us": 80}

func countOrders(_ airflow.Context, region string) (int, error) { return ordersByRegion[region], nil }

func summarize(_ airflow.Context, eu, us int) (int, error) { return eu + us, nil }

func load(actx airflow.Context, total int, table string) error {
    actx.Logger().Info("loading orders", "total", total, "table", table)
    return nil
}

func alert(actx airflow.Context) error {
    actx.Logger().Info("no orders today")
    return nil
}

func hasOrders(_ airflow.Context, total int) (bool, error) { return total > 0, nil }

func reportFull(actx airflow.Context) error {
    actx.Logger().Info("full report")
    return nil
}

func reportBrief(actx airflow.Context) error {
    actx.Logger().Info("brief report")
    return nil
}

// reports holds the switch's cases, because a decider returns a *TaskRef.
type reports struct{ full, brief *airflow.TaskRef }

func (r *reports) pick(_ airflow.Context, total int) (*airflow.TaskRef, error) {
    if total > 1000 {
        return r.full, nil
    }
    return r.brief, nil
}
```

![The Go `finance_revenue_close` Dag in the Airflow UI, with its source in the Code view](images/multilang-run-go.png)

</details>

## Building and deploying

Each SDK builds your code into one self-contained artifact, which goes into a Dag bundle like any `.py` file.

### Building

<details name="sdk-build" data-tab="typescript" data-sync-group="sdk" open>
<summary>TypeScript</summary>

`airflow-ts-pack` bundles the entry module and everything it imports into one file.

```bash
npm install apache-airflow-ts-sdk
npm install --save-dev esbuild
npx airflow-ts-pack src/orders_daily.ts --outdir dist   # writes dist/bundle.min.mjs
```

</details>
<details name="sdk-build" data-tab="java" data-sync-group="sdk">
<summary>Java</summary>

The Gradle plugin builds a fat JAR by default and packs the source of each Dag class into it. Maven is supported too.

```kotlin
plugins {
    id("org.apache.airflow.sdk") version "<version>"
}

dependencies {
    annotationProcessor("org.apache.airflow:airflow-sdk-processor:<version>")
    implementation("org.apache.airflow:airflow-sdk:<version>")
    implementation("org.apache.airflow:airflow-sdk-jpl:<version>")  // sends System.Logger output to the task log
}

airflowBundle {
    mainClass = "com.example.OrdersDaily"
}
```

```bash
./gradlew bundle   # writes the JAR to build/bundle/
```

</details>
<details name="sdk-build" data-tab="go" data-sync-group="sdk">
<summary>Go</summary>

`airflow-go-pack` compiles the program and embeds each Dag's source file and a manifest in the executable. It cross-compiles for the platform your Airflow components run on.

```bash
# go.mod
tool github.com/apache/airflow/go-sdk/cmd/airflow-go-pack

go tool airflow-go-pack --goos linux --goarch amd64 --output dist/orders_daily .
```

</details>

### Deploying

Put the artifact in a Dag bundle, such as the default dags-folder. The Dag processor and the workers need the language's runtime:

| **SDK** | **Artifact** | **Runtime on the Dag processor and workers** |
| --- | --- | --- |
| TypeScript | `*.min.mjs` file | Node.js 22+ |
| Java | `.jar` whose manifest sets `Main-Class` | Java runtime |
| Go | executable with no file extension | None |

Then register a coordinator for each language and route each Dag's queue to it, on the Dag processor and on the workers:

```ini
[sdk]
coordinators = {
    "ts": {"classpath": "airflow.sdk.coordinators.node.NodeCoordinator"},
    "java": {"classpath": "airflow.sdk.coordinators.java.JavaCoordinator"},
    "go": {"classpath": "airflow.sdk.coordinators.executable.ExecutableCoordinator"}
  }
queue_to_coordinator = {"typescript": "ts", "java": "java", "golang": "go"}
```

The Dag processor runs each artifact to read its Dags, and each task runs from the same Dag bundle. From there, Airflow treats the Dags like Python ones: the scheduler plans their runs, they show up in the UI, and the Code view shows each Dag's own source file. With more than one coordinator for the same language, map each Dag bundle to one of them with `[sdk] dag_bundle_to_coordinator`.

For a Python Dag with stub TaskHandler, put the artifact next to the Python Dag, or in the Dag bundle named by the coordinator's `task_handler_bundle_name`.

## Learn more

- [TypeScript SDK guide](https://airflow.apache.org/docs/apache-airflow/3.4.0/authoring-and-scheduling/language-sdks/typescript.html)
- [Java SDK guide](https://airflow.apache.org/docs/apache-airflow/3.4.0/authoring-and-scheduling/language-sdks/java.html)
- [Go SDK guide](https://airflow.apache.org/docs/apache-airflow/3.4.0/authoring-and-scheduling/language-sdks/go.html)

## YAML Dags

For teams that want Dags as declarative configuration, with no code and no build step, Airflow 3.4 adds a native YAML importer on top of AIP-85. A `.yaml` file carrying a `$schema` marker is discovered, validated against a schema, and built into a real Dag with real operators.

The format is intentionally small. A task either **`uses:`** a built-in operator or **`run:`** a code task, binds arguments with **`with:`**, and declares dependencies with **`needs:`**:

```yaml
# Illustrative of the YAML grammar. Confirm exact keys against the released schema.
$schema: airflow/dag
dag_id: daily_sales
schedule: "@daily"
tasks:
  - id: extract
    uses: airflow.providers.standard.operators.bash.BashOperator
    with:
      bash_command: "python extract.py"
  - id: load
    uses: airflow.providers.standard.operators.bash.BashOperator
    with:
      bash_command: "python load.py"
    needs: [extract]
```

Templating is explicit: a field only renders when the author marks it. The value grammar uses small markers, `$t` to render a template, `$x` to read an XCom, `$f` to read a file, and `$const` for a literal constant, and a marker on a field the operator does not template is a build error rather than something silently ignored. That makes YAML Dags predictable: what you see is what runs.

# 🤖 Common AI Goes GA: LLM and Agent Tasks, With a Human in the Loop

AI steps are becoming a normal part of data pipelines, and the `common.ai` provider reaches **GA** alongside this release — shipping **1.1.0** with Airflow 3.4.0 — stabilizing the API for running model calls and agents as ordinary Airflow tasks. Built on [pydantic-ai](https://ai.pydantic.dev/), it lets the API key come from a connection, a failed call retry like any task, the result land in XCom, and the whole thing run on a schedule.

The simplest form is a decorator:

```python
@task.llm(
    llm_conn_id="pydanticai_default",
    system_prompt="You write release announcements. Be concise.",
)
def summarize(notes: str):
    return f"Summarize these release notes in two sentences:\n{notes}"
```

For anything that needs tools, the `AgentOperator` runs a full agent that can use tools. Toolsets wire the model to real Airflow resources such as SQL, hooks, MCP servers, object storage, and sandboxes, so the agent can actually *do* work, not just talk:

```python
AgentOperator(
    task_id="analyst",
    prompt="What are the top 5 customers by order count?",
    llm_conn_id="pydanticai_default",
    system_prompt="You are a SQL analyst. Use the tools to explore the schema and answer with data.",
    toolsets=[SQLToolset(db_conn_id="postgres_default", allowed_tables=["customers", "orders"], max_rows=20)],
)
```

## Key Capabilities

- **A family of operators and decorators**: `@task.llm` and `LLMOperator`, `@task.agent` and `AgentOperator`, plus `LLMBranchOperator` (let the model pick the next task), `LLMSQLQueryOperator` (natural language to SQL), and operators for batch and file analysis.
- **Agents that use tools** via toolsets for SQL, hooks, MCP, object storage, and sandboxes, with LangChain and LlamaIndex integrations for pipelines in the RAG style.
- **Cost and usage limits**: cap tokens, requests, or spend per run, with usage (including prompt cache hits) pushed to XCom. Prompt caching is on by default.
- **Human in the loop, natively**: this is where the rest of the release pays off. An agent can pause partway through a run for a person to **approve a tool call** before it executes, or to **approve the final answer**, using the first-class `awaiting_input` state from Airflow 3.3. The task parks **without a triggerer and without holding a worker slot**, shows up on the **Required Actions** page, and resumes when a reviewer responds. Approve and it proceeds; reject and the agent is told and carries on.

Several of the more advanced pieces, such as durable replay at the step level on retry, sandbox toolsets, and code mode, are shipping as **experimental previews** and may change before they stabilize.

<!-- TODO image (from Kaxil): Loops + common.ai example, and/or the Required Actions / human-in-the-loop approval page -->

# 🖥️ UI, Observability, and Operations

- **Loop iteration views**: new UI for Task Loops shows each iteration's run and a per-task loop history chart, so an iterative workflow reads clearly instead of as an opaque group.
- **Dag Folders**: the Dags list gains a **Folders** panel that groups your Dags into a navigable tree mirroring each bundle's directory layout, so you can drill into `multilang/go` or `task_loops/experiments` and filter to a folder instead of scrolling one flat list. The tree nests to any depth.

  {{<figure src="images/dag-folders.png" alt="Airflow's Dags list page with a folder-like structure on the left hand side" caption="The Folders panel groups Dags by their directory layout within each bundle">}}

- **Language-aware Dags in the UI**: Dags not written in Python surface with their source language, so a Go or TypeScript Dag is treated like any other Dag in the grid and graph.
- Plus the usual round of stability, performance, and quality-of-life fixes across the scheduler, API server, and UI.

# ⬆️ Upgrading to 3.4.0

Before upgrading, review the [Significant Changes](https://airflow.apache.org/docs/apache-airflow/3.4.0/release_notes.html) in the release notes, and install against the [constraints file](https://github.com/apache/airflow/tree/constraints-3.4.0) for a reproducible upgrade. The language SDKs, the Dag Importer framework, and several `common.ai` previews are explicitly marked experimental, so pin to the exact versions you test with.

# 🙏 Community Appreciation

Apache Airflow 3.4.0 is the work of hundreds of contributors who authored AIPs, wrote and reviewed code, improved docs, triaged issues, and tested release candidates. Task Loops, the Dag Importer and its language SDKs, and the `common.ai` provider each represent months of design discussion and collaboration across the community. Thank you to everyone who helped shape and ship this release.

# 🔗 Get Involved

- 📥 **Upgrade**: `pip install apache-airflow==3.4.0` (use the [constraints files](https://github.com/apache/airflow/tree/constraints-3.4.0) for a reproducible install).
- 📚 **Read the docs**: https://airflow.apache.org/docs/apache-airflow/3.4.0/
- 💬 **Join the conversation** on the [Airflow Slack](https://s.apache.org/airflow-slack) and the [dev mailing list](https://airflow.apache.org/community/).
- 🐛 **Report issues** and open PRs on [GitHub](https://github.com/apache/airflow).

Happy orchestrating, whether you are iterating, writing in another language, or putting an agent to work with a human in the loop!

<!--
Notes for finalizing (delete before publishing):
- Hero image (OPTIONAL): images/3.4.0.jpg — 3.3.0 shipped without it, so not a blocker; add later if desired.
- Images still needed (replace the TODO-image comments above):
  * Loops + common.ai example and/or Required Actions approval page (from Kaxil).
  Lock all screenshots against the 3.4.0 GA build (the Loops UI may have changed since RC).
- Added: per-SDK Code-view screenshots (multilang-run-{typescript,java,go}.png) from the Google Doc.
- common.ai: confirmed shipping 1.1.0 (GA) with 3.4.0.
- Java build snippet: replace the three `<version>` placeholders with the released SDK versions.
- YAML: replace the illustrative snippet with a verbatim example once the schema is final.
- Verify the Learn-more SDK guide links resolve under /3.4.0/ (pinned from /stable/).
-->
