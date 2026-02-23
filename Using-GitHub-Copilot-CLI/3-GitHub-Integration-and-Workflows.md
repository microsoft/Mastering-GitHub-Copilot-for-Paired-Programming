# Module 3: GitHub Integration and Workflows

[← Previous: Tool Approval and Context](2-Tool-Approval-and-Context.md) | [Next: Customization and Extensions →](4-Customization-and-Extensions.md)

---

### 🗒️ Section 4: GitHub.com Integration and Model Selection

🎯 **Learning Goals**
- Use Copilot CLI to interact with GitHub.com natively — list issues, open PRs, and manage workflows
- Work on a GitHub Issue directly from the terminal
- Select and switch AI models using `/model`
- Use `gh agent-task` to kick off and monitor remote Copilot coding agent tasks

The standalone Copilot CLI ships with the GitHub MCP server built in and authenticates using your existing GitHub credentials, so GitHub.com interactions feel like a natural part of the conversation.

#### Interacting with GitHub.com

1. Launch a session in the sample project directory:

   ```bash
   copilot
   ```

2. List your open pull requests across all repositories:

   ```
   List my open PRs
   ```

   For repository-specific results:

   ```
   List all open issues assigned to me in <owner>/<repo>
   ```

3. Ask Copilot to start working on an issue. Replace the URL with one from your fork of the sample repo:

   ```
   I've been assigned this issue: https://github.com/<owner>/<repo>/issues/<number>. Start working on this for me in a suitably named branch.
   ```

   Copilot will read the issue, create a branch, implement the change, run tests, and report back.

4. Create a pull request directly from the CLI:

   ```
   In the root of this repo, add a Python script called health_check.py that pings the /health endpoint and prints the result. Create a pull request to add this file to the repo on GitHub.
   ```

   You are marked as the PR author even though Copilot did the work.

5. Ask Copilot to review a PR for problems:

   ```
   Check the changes made in PR https://github.com/<owner>/<repo>/pull/<number>. Report any serious errors you find.
   ```

6. Find good first issues for a new contributor using the built-in GitHub MCP server:

   ```
   Use the GitHub MCP server to find good first issues for a new team member in <owner>/<repo>
   ```

   Specifying the MCP server by name in your prompt helps Copilot route the request efficiently.

#### Model Selection

7. To see all available models and switch, use the `/model` slash command:

   ```
   /model
   ```

   A selection list appears. Available models include (as of February 2026):

   | Model | Request multiplier | Notes |
   |---|---|---|
   | Claude Sonnet 4.6 (default) | 1× (tentative) | GA Feb 17 2026; excels at agentic coding & search |
   | Claude Sonnet 4.5 | 1× | |
   | Claude Sonnet 4 | 1× | |
   | Claude Opus 4.6 | varies | GA Feb 5 2026; best for hard planning & tool-calling tasks |
   | Claude Opus 4.6 Fast | 30× | Preview, Pro+/Enterprise only; up to 2.5× faster output |
   | GPT-5.3-Codex | varies | GA Feb 9 2026; 25% faster than GPT-5.2-Codex on agentic tasks |

   > **Note**: Model availability depends on your Copilot plan (Pro, Pro+, Business, Enterprise). Enterprise/Business admins must enable each model in org Copilot settings. Check [supported models](https://docs.github.com/copilot/reference/ai-models/supported-models) for the latest multipliers.

   Each prompt reduces your monthly premium request quota by the multiplier shown.

8. You can also set the model at launch time:

   ```bash
   copilot --model claude-sonnet-4
   ```

#### Remote Agent Tasks with `gh agent-task`

The `gh agent-task` command set lets you kick off a Copilot coding agent task on GitHub (running in the cloud on a remote Codespace) and monitor its progress from your local terminal — without the agent using your local files.

9. Create a remote agent task linked to an issue:

   ```bash
   gh agent-task create --repo <owner>/<repo> --issue <number>
   ```

   The agent task is queued on GitHub. The Copilot coding agent will pick it up, implement the change, and open a pull request.

10. List all agent tasks for a repository:

    ```bash
    gh agent-task list --repo <owner>/<repo>
    ```

11. Check the status of a specific task:

    ```bash
    gh agent-task view <task-id> --repo <owner>/<repo>
    ```

    When the task is complete, a pull request URL is shown. Review it with:

    ```bash
    gh pr view <pr-number> --web
    ```

In the above exercises we achieved the following:
- ✅ Listed issues and PRs from GitHub.com natively in the CLI
- ✅ Asked Copilot to work on a GitHub Issue and create a PR
- ✅ Selected and switched AI models with `/model`
- ✅ Created and monitored remote agent tasks with `gh agent-task`

---

### 🗒️ Section 5: A Real-World End-to-End Python Workflow

🎯 **Learning Goals**
- Combine interactive mode, plan mode, tool approval, context management, and GitHub.com integration into a single repeatable workflow
- Apply the full toolkit to a realistic Python feature-development scenario
- Use `gh agent-task` for async work that does not block your local session
- Understand when to use default mode, plan mode, autopilot, or remote agent tasks

In this section you will bring everything together. You will use the GitHub Copilot CLI — including plan mode, tool approval, context management, GitHub.com integration, and `gh agent-task` — to take a feature from raw idea to merged pull request, touching every stage of a real development cycle.

#### Scenario

You have been asked to add **pagination support** to the `/token` endpoint. The endpoint currently returns all generated tokens at once; it needs to accept `page` and `page_size` query parameters, validate them, and return a paginated response with metadata.

#### Step 1 — Understand the current state

1. Launch a session in the project root and ask Copilot for an overview of the token feature:

   ```bash
   copilot
   ```

   ```
   Show me all files that are involved in the /token endpoint, including models, handlers, and tests.
   ```

   Copilot reads the codebase and produces a file map — no shell scripting required.

2. Ask Copilot to explain the current FastAPI route structure before modifying it:

   ```
   Explain how the token generation route is registered and what Pydantic models it uses.
   ```

#### Step 2 — Plan the change using Plan Mode

3. Press `Shift+Tab` to switch to **Plan** mode, then describe the full feature:

   ```
   Add pagination to the /token endpoint. It should accept page and page_size query parameters with validation using Pydantic, return a PaginatedResponse model with items and metadata (total, page, page_size, total_pages), update the OpenAPI spec, and include pytest tests for happy-path and edge cases.
   ```

   Review Copilot's structured plan. Confirm or revise individual steps before execution begins.

4. Once you approve the plan, press `Shift+Tab` to switch back to default mode (or keep plan mode — Copilot will execute each step and check in after each one).

#### Step 3 — Build and test

5. Copilot creates `models/pagination.py`, updates the route handler in `main.py`, and scaffolds tests in `tests/`. When it requests permission to run `pytest`, approve it:

   ```
   1. Yes, and approve pytest for the rest of this session
   ```

   Copilot runs the tests, observes any failures, and self-corrects until all tests pass.

6. Check context usage mid-session if the conversation has been running for a while:

   ```
   /context
   ```

   If usage is above 70%, run `/compact` to free up space before the final steps.

#### Step 4 — Commit and create a PR via GitHub.com integration

7. In this next task we will work asynchronously with Copilot using the local CLI. Ask Copilot to commit the changes and open a pull request:

   ```
   Commit these changes with a conventional commit message and create a pull request against main with a description that summarises the pagination feature.
   ```

   Copilot uses the built-in GitHub MCP server to create the PR on GitHub.com, with you listed as the author.

8. Every coding agent task runs on a fresh branch and opens a new pull request based on the current default branch. The agent does not reuse your local branch or modify existing pull requests. Instead, it starts from the latest state of the repository's default branch (for example, main), creates its own isolated branch in the cloud, applies the requested changes, and then opens a new PR for you to review and merge

While the agent is working locally and in the background, we are going to kick off a remote agent task to ask the remote agent to add docstrings to the new code, so it runs asynchronously in the cloud while you move on to other work:

   ```bash
   gh agent-task create --repo <owner>/<repo> --issue <number> \
     --body "Add Google-style docstrings to PaginatedResponse and the updated token route handler."
   ```

9.  Monitor Copilot's progress and after review merge:

   ```bash
   gh agent-task list --repo <owner>/<repo>
   gh pr view <pr-number> --web
   ```

#### Workflow Summary

The complete workflow you just executed maps to a repeatable pattern for any Python feature:

| Stage | Tool | Action |
|---|---|---|
| Explore | Copilot CLI (default mode) | Map affected files with natural language |
| Design | Copilot CLI (plan mode) | Build and review a structured implementation plan |
| Build & test | Copilot CLI (default/plan mode) | Implement, run pytest, self-correct |
| Context | `/context` + `/compact` | Monitor and manage token usage |
| Ship | GitHub.com integration | Commit and open PR from the terminal |
| Polish | `gh agent-task` | Async documentation via remote agent |
| Review | `gh pr view` | Inspect and merge |

🚀 Congratulations! You have completed the full GitHub Copilot CLI workshop. You now have a practical, end-to-end workflow that covers every stage of Python feature development — from interactive planning to autonomous agent-driven pull requests.

In the above exercises we achieved the following:
- ✅ Used plan mode to design a feature before writing a single line of code
- ✅ Built, tested, and self-corrected with the Copilot CLI
- ✅ Managed conversation context with `/context` and `/compact`
- ✅ Created a pull request via GitHub.com integration from the terminal
- ✅ Kicked off an async documentation task using `gh agent-task`

---

[← Previous: Tool Approval and Context](2-Tool-Approval-and-Context.md) | [Next: Customization and Extensions →](4-Customization-and-Extensions.md)
