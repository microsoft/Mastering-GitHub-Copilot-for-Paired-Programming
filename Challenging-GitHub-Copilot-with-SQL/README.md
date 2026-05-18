<h1 align="center">Challenging SQL with GitHub Copilot</h1>
<h5 align="center">Use GitHub Copilot to solve complex SQL problems through iteration, validation, and critical review</h5>

<p align="center">
  <a href="#learning-objectives">Learning Objectives</a> •
  <a href="#scenario">Scenario</a> •
  <a href="#lab-flow">Lab Flow</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#success-criteria">Success Criteria</a>
</p>

- **Who is this for**: Software engineers, data engineers, data scientists, and technical professionals who want to move beyond basic GitHub Copilot usage and apply it effectively to difficult SQL tasks.
- **What you'll learn**: How to collaborate with GitHub Copilot on complex SQL by clarifying requirements, improving prompts, validating output, debugging issues, and refining queries based on evidence.
- **What you'll build**: SQL queries against a realistic transactional dataset that apply business rules, handle edge cases, and pass validation checks.

## Learning Objectives

In this workshop, you will:

- Use advanced GitHub Copilot interaction techniques to deal with complex SQL problems.
- Iterate, validate, and refine Copilot-generated answers to improve accuracy.
- Apply general problem-solving strategies that improve the quality of AI-assisted work.
- Recognize poor prompting techniques and explain how they affect GitHub Copilot output.

> [!IMPORTANT]
> This lab is not about getting the first query that runs. It is about learning how to collaborate with GitHub Copilot while still verifying, debugging, and reasoning about SQL yourself.

## Scenario

You are supporting a payment operations team that needs a reliable daily settlement report from transactional data.

The report must:

- include only valid settlement records,
- exclude transaction types that should not be counted,
- aggregate results correctly,
- hold up under validation and edge cases.

Your goal is to use GitHub Copilot to help you build the SQL, while reviewing every suggestion critically. A query that looks correct is not enough — it must also be explainable, testable, and validated.

> [!TIP]
> Treat GitHub Copilot as a collaborator, not a source of truth.

## Lab Flow

This lab is organized into six phases:

1. Understand the requirements
2. Explore the dataset
3. Generate a baseline query
4. Refine the query with better prompts
5. Validate and debug the output
6. Reflect on how GitHub Copilot helped — and where your judgment mattered

Each phase includes:
- a clear goal,
- suggested Copilot prompts,
- validation guidance,
- a checkpoint.

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
2. Open [this repository with Codespaces](https://codespaces.new/microsoft/challenging-github-copilot)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/challenging-github-copilot)

## Prerequisites

Before joining the workshop, make sure you have:

- a public GitHub account,
- access to GitHub Copilot,
- basic familiarity with SQL filtering, joins, and aggregation,
- comfort running scripts or tests from the command line.

All resources, dependencies, and data required for the workshop are included in the repository.

> [!NOTE]
> You do not need to know the final SQL solution in advance. You do need to be willing to inspect results, revise prompts, and validate output carefully.

## Success Criteria

By the end of the lab, you should have:

- a working SQL solution that satisfies the business rules,
- evidence that the result was validated,
- at least one example of a weak prompt and an improved version,
- notes on at least one defect, edge case, or incorrect Copilot assumption you found during the lab,
- a short reflection on what improved your results.

## How to Use GitHub Copilot in This Lab

Use GitHub Copilot to help with:

- translating requirements into SQL structure,
- exploring the schema,
- drafting initial queries,
- identifying edge cases,
- debugging failed validations,
- improving readability,
- suggesting alternative approaches.

Do **not** use GitHub Copilot as:

- a substitute for understanding the data,
- proof that a query is correct,
- a replacement for testing,
- a replacement for business-rule review.

A strong workflow for this lab looks like this:

1. Restate the requirement in plain English
2. Ask Copilot for a first pass
3. Inspect the SQL carefully
4. Run it and inspect the results
5. Compare against expected behavior
6. Revise the prompt or query
7. Validate again

## Prompting Patterns You Will Practice

You will use several prompting patterns throughout the lab.

### 1. Requirements-first prompting

Use this when the task is ambiguous.

**Example prompt**
```text
Before writing SQL, summarize the requirement as filters, exclusions, joins, aggregations, and expected output columns.
```

### 2. Decomposition prompting

Use this when the problem is too large for one step.

**Example prompt**
```text
Break this SQL problem into smaller steps using CTEs for filtering, normalization, and aggregation.
```

### 3. Verification prompting

Use this when a query seems plausible but needs review.

**Example prompt**
```text
List the edge cases or data anomalies that could cause this query to return incorrect totals.
```

### 4. Debug prompting

Use this when tests or outputs fail.

**Example prompt**
```text
This query returns more rows than expected. Identify likely causes such as duplicate joins, incorrect filters, or grouping issues, and suggest how to test each one.
```

### 5. Minimal-change prompting

Use this when most of the query is correct.

**Example prompt**
```text
Do not rewrite the whole query. Only revise the logic responsible for excluding invalid settlement records.
```

## Phase 1: Understand the Requirements

### Goal

Translate the reporting need into a precise SQL problem before generating code.

### Your task

Review the scenario and identify:

- what the query must return,
- what records must be excluded,
- how results should be grouped,
- what assumptions need clarification.

### Suggested Copilot prompt

```text
Summarize this reporting requirement as a SQL design checklist. Include filters, exclusions, joins, grouping, output columns, and possible ambiguities.
```

### Write down your answers

Document:

- required filters,
- required exclusions,
- aggregation rules,
- any assumptions about date handling, duplicate transactions, or null values.

> [!TIP]
> If you cannot explain the business rule in plain English, you are not ready to trust the SQL.

### Checkpoint

You are ready to move on if you can explain:

- which records count,
- which records do not count,
- how the final output should be shaped.

## Phase 2: Explore the Dataset

### Goal

Understand the schema and identify data characteristics before writing the final query.

### Your task

Inspect the available tables and answer:

- What tables are relevant?
- What columns appear necessary?
- What values exist in key filtering columns?
- Are there nulls, duplicates, or suspicious values?

### Suggested Copilot prompts

```text
Help me explore the transaction dataset. I want SQL to inspect row counts, date range, distinct status values, distinct batch types, and null counts for important columns.
```

```text
Based on this schema, which columns are most likely needed for a daily settlement report and why?
```

### Minimum exploration tasks

Write and run SQL to:

- count total rows,
- inspect the date range,
- list distinct statuses,
- list distinct batch types,
- inspect nulls in amount or key identifiers,
- identify possible duplicates.

### Checkpoint

You are ready to move on if you can answer:

- which columns drive filtering,
- which columns drive aggregation,
- which values are likely edge cases.

## Phase 3: Generate a Baseline Query

### Goal

Create a simple first-pass query that is correct in structure, even if incomplete.

### Your task

Write a baseline query that:

- filters to the target date,
- includes only valid record status values,
- returns raw rows before aggregation.

Do **not** optimize yet.

### Suggested Copilot prompt

```text
Write a simple SQL query for the daily settlement dataset that returns only valid records for the reporting date. Do not aggregate yet. Add comments explaining each WHERE clause.
```

### Review before running

Before executing the query, check:

- Did Copilot assume a date column without evidence?
- Did it invent a status value?
- Did it exclude records not mentioned in the requirements?
- Is the logic readable enough to debug?

> [!WARNING]
> A working query can still be wrong. Always verify assumptions against the actual schema and data.

### Checkpoint

You are ready to move on if:

- the baseline query runs,
- you understand each filter,
- the result set is smaller and more focused than the raw input.

## Phase 4: Refine the Query with Better Prompts

### Goal

Improve the SQL by strengthening the prompt and explicitly handling business constraints.

### Your task

Refine the baseline query to:

- exclude invalid settlement categories,
- group correctly,
- produce the expected report shape.

### Compare a weak prompt and a better prompt

**Weak prompt**
```text
Write a SQL query for today's transaction totals.
```

**Better prompt**
```text
Write a SQL query for a daily settlement report. Return one row per merchant and transaction type for the reporting date. Exclude rows with invalid batch types such as off-us and offset, include only settled records, and sum amount as total_amount. Add comments explaining each rule.
```

### Your assignment

Use both styles once and compare the results.

Document:

- what the weak prompt missed,
- what the improved prompt clarified,
- what Copilot still got wrong or assumed.

### Suggested Copilot prompts

```text
Refine this query to exclude invalid batch types and aggregate by merchant and transaction type. Keep the SQL readable and explain each business rule in comments.
```

```text
Rewrite this using CTEs so the filtering, exclusion logic, and final aggregation are easier to validate separately.
```

### Checkpoint

You are ready to move on if:

- your query reflects the stated business rules,
- you can explain why each exclusion exists,
- the query is organized clearly enough for targeted debugging.

## Phase 5: Validate and Debug

### Goal

Prove that the SQL is correct using evidence, not confidence.

### Your task

Validate the query by checking:

- row counts,
- totals,
- expected shape,
- automated tests if provided,
- edge-case behavior.

### Validation workflow

1. Run the query and inspect the output
2. Compare columns and row counts to expectations
3. Validate totals against sample or known cases
4. Run the provided tests
5. If a test fails, isolate the problem to one stage of the query
6. Revise only the failing logic

### Suggested Copilot prompts

```text
List the most likely reasons this settlement query could overcount totals.
```

```text
This query failed a validation case involving duplicate transactions. Suggest how to detect and fix the problem without rewriting the whole query.
```

```text
Explain how to test each CTE in this query separately so I can isolate the defect.
```

### Debugging guidance

If your query is wrong:

- inspect intermediate CTE outputs,
- test one filter at a time,
- compare pre-aggregation and post-aggregation row counts,
- look for duplicate joins,
- check whether nulls or reversals are handled correctly.

### Checkpoint

You are ready to move on if:

- your query passes validation,
- you can explain why it is correct,
- you identified at least one issue that required revision.

## Phase 6: Reflect on the Copilot Collaboration

### Goal

Capture what improved your results and where your own reasoning was essential.

### Reflection questions

Answer the following:

1. What did GitHub Copilot help with most?
2. What did it get wrong, assume, or oversimplify?
3. Which prompt improvement led to the biggest quality increase?
4. What validation step caught an issue you might otherwise have missed?
5. What would you do differently next time when using Copilot on a complex SQL task?

### Optional written artifact

Capture:

- one weak prompt,
- one improved prompt,
- one incorrect Copilot suggestion,
- one fix you made after validation,
- one lesson learned.

## Troubleshooting

### Problem: The query runs but totals are too high

Possible causes:

- duplicate joins,
- missing exclusions,
- duplicate transaction rows,
- grouping at the wrong level.

Try:

- checking row counts before and after joins,
- grouping by transaction identifier temporarily,
- validating one business rule at a time.

### Problem: The query returns no rows

Possible causes:

- overly restrictive date logic,
- incorrect status filter,
- wrong join type,
- mismatch between assumed and actual values.

Try:

- removing one filter at a time,
- checking distinct values in filter columns,
- validating the reporting date logic.

### Problem: Copilot keeps rewriting too much

Try:
```text
Do not rewrite the full query. Only revise the WHERE clause to fix the exclusion logic.
```

### Problem: The SQL is hard to understand

Try:
```text
Refactor this query into clearly named CTEs with one responsibility per CTE. Do not change the logic.
```

## Stretch Challenges

If you complete the core lab, try one or more of these:

### Stretch 1: Edge-case hardening

Revise the query to handle:

- null amounts,
- duplicate transaction IDs,
- reversal records,
- date-boundary ambiguity.

### Stretch 2: Readability refactor

Refactor the final query for readability without changing behavior.

### Stretch 3: Performance review

Ask Copilot to suggest possible performance improvements, then evaluate whether they preserve correctness.

### Stretch 4: Test generation

Ask Copilot to propose additional validation cases for the final query. Review whether those tests actually cover the business rules.

**Example prompt**
```text
Suggest five targeted test cases for this settlement query, including one for duplicates, one for null amounts, and one for excluded batch types.
```

## Main Takeaways

- Define the objective before generating SQL.
- Break hard problems into smaller, testable pieces.
- Use domain vocabulary to improve Copilot output.
- Iterate instead of expecting a perfect first answer.
- Use examples and constraints to reduce ambiguity.
- Think about edge cases early.
- Validate every meaningful output.
- Treat Copilot as a collaborator that must be reviewed.

## :books: Resources

Although not required, some of the features this workshop covers are in these Microsoft Learn modules:

- [Code with GitHub Codespaces](https://learn.microsoft.com/training/modules/code-with-github-codespaces/)
- [Using advanced GitHub Copilot features](https://learn.microsoft.com/training/modules/advanced-github-copilot/)

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (for example, status check or comment). Simply follow the
instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information, see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos is subject to those third-parties' policies.
