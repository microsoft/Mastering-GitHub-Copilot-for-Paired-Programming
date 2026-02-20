<header>

# Using the GitHub Copilot CLI with Python

Welcome to a hands-on, multi-module course that takes GitHub Copilot beyond the editor and directly into your terminal as a fully autonomous coding agent. The GitHub Copilot CLI is a standalone AI-powered tool — separate from the `gh` extension — that opens an interactive chat session in your terminal, understands your local codebase, and can plan and execute complex multi-step coding tasks on your behalf.

Prepare for a practical, end-to-end experience! You will install the `copilot` CLI, master its interactive and programmatic interfaces (including plan mode and auto model selection), control tool permissions, manage conversation context, integrate with GitHub.com, select models, configure custom agents, and combine everything into a real-world Python development workflow.

</header>


- **Who this is for**: Python Developers, DevOps Engineers, Platform Engineers, Software Development Managers, Testers.
- **What you'll learn**: How to install and use the standalone GitHub Copilot CLI, leverage its interactive and plan modes, use Auto model selection, control tool approval, manage context, interact with GitHub.com, select AI models, configure custom agents, and use `gh agent-task` for remote agent tasks.
- **What you'll build**: A real-world CLI-driven workflow for Python projects covering project analysis, debugging, refactoring, test generation, and agent-assisted automation using MCP integrations.
- **Prerequisites**: GitHub Copilot is available to use for free, sign up for [GitHub Copilot](https://gh.io/copilot). Basic familiarity with a terminal, Git, and Python is recommended.
- **Timing**: This module can be completed in under 90 minutes.

By the end of this module, you'll acquire the skills to be able to:

- Install, authenticate, and launch the standalone GitHub Copilot CLI.
- Use interactive mode and plan mode; let Auto model selection choose the optimal model.
- Control tool approval with `--allow-tool`, `--deny-tool`, and `--allow-all-tools`.
- Manage conversation context with `/compact`, `/context`, and auto-compaction.
- Interact with GitHub.com natively — list PRs, work on issues, and create pull requests from the terminal.
- Select and switch AI models using `/model`.
- Configure custom agents and use `gh agent-task` to kick off and monitor remote agent tasks.
- Leverage MCP servers to extend CLI capabilities for Python projects.

## Prerequisite reading:
- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot/?WT.mc_id=academic-113596-abartolo)
- [Using GitHub Copilot with Python](https://learn.microsoft.com/en-us/training/modules/introduction-copilot-python/?WT.mc_id=academic-113596-abartolo)
- [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Installing GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli)

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)

2. Install the standalone **GitHub Copilot CLI** (see Section 1 — the old `gh copilot` extension has been replaced by this new tool)

3. Clone [this repository with locally](https://github.com/MicrosoftDocs/mslearn-copilot-codespaces-python)

## 💪🏽 Exercise

**Right click the following Codespaces button to open your Codespace in a new tab**


This workshop uses a Python FastAPI sample project. Throughout the exercises you will use the GitHub Copilot CLI and Coding Agent to understand, improve, and extend this project — entirely from the terminal and through agent-driven automation.

---

### 🗒️ Section 1: Install and Verify the GitHub Copilot CLI

🎯 **Learning Goals**
- Install the standalone GitHub Copilot CLI
- Authenticate and launch your first session
- Understand the difference between the new `copilot` CLI and the deprecated `gh copilot` extension

The **GitHub Copilot CLI** (`copilot`) is a standalone terminal application — distinct from the old `gh copilot` extension — that opens a full interactive AI chat session in your terminal. It ships with the GitHub MCP server built in, supports plan mode and auto model selection, and can autonomously read files, run commands, and interact with GitHub.com on your behalf.

> **Note**: The `gh extension install github/gh-copilot` extension was deprecated in September 2025 and archived at v1.2.0. This workshop uses the new standalone `copilot` CLI.

#### Prerequisites

This workshop uses two separate CLI tools:

- **`copilot`** — the standalone GitHub Copilot CLI (installed below)
- **`gh`** — the GitHub CLI, required for `gh agent-task` commands in Sections 4 and 6

Install `gh` first if you don't already have it:

**Windows:**
```powershell
winget install GitHub.CLI
```
**macOS / Linux:**
```bash
brew install gh
```
Then authenticate: `gh auth login`

---

#### Installing the Copilot CLI

1. Choose the installation method for your platform:

   **Windows** (WinGet):
   ```powershell
   winget install GitHub.Copilot
   ```

   **macOS / Linux** (Homebrew):
   ```bash
   brew install copilot-cli
   ```

   **Any platform** (pip):
   ```bash
   pip install github-copilot-cli
   ```

   **macOS / Linux** (install script):
   ```bash
   curl -fsSL https://gh.io/copilot-install | bash
   ```

2. Verify the installation:

   ```bash
   copilot --version
   ```

3. Launch the CLI from the root of the sample project. On first launch you will see an animated welcome banner and be prompted to log in if you are not already authenticated:

   ```bash
   copilot
   ```

   If prompted, use the `/login` slash command and follow the on-screen instructions to authenticate with your GitHub account.

   Alternatively, authenticate headlessly using a fine-grained Personal Access Token (PAT) with the **Copilot Requests** permission set in the `GH_TOKEN` or `GITHUB_TOKEN` environment variable:

   ```bash
   export GH_TOKEN=<your-pat>
   copilot
   ```

4. Keep the CLI up to date using the same package manager you used to install it. For example:

   ```bash
   brew upgrade copilot-cli       # macOS/Linux via Homebrew
   winget upgrade GitHub.Copilot  # Windows via WinGet
   pip install --upgrade github-copilot-cli  # pip
   ```

In the above exercises we achieved the following:
- ✅ Installed the standalone GitHub Copilot CLI
- ✅ Authenticated and launched an interactive session
- ✅ Understood the distinction from the deprecated `gh copilot` extension

---

### 🗒️ Section 2: Interactive Modes — Default, Plan, and Autopilot

🎯 **Learning Goals**
- Use the default ask/execute mode for general coding tasks
- Switch to plan mode to build a structured implementation plan before writing code
- Enable Auto model selection to reduce rate limiting and simplify model management
- Navigate the interactive interface using slash commands

The GitHub Copilot CLI interactive session (launched with `copilot`) offers three modes. You cycle between them with `Shift+Tab`.

#### Default (Ask/Execute) Mode

In default mode Copilot responds to each prompt, asks clarifying questions when needed, and requests your approval before modifying files or running commands.

1. Launch the CLI from the sample project root:

   ```bash
   copilot
   ```

2. Ask Copilot a question about the project to confirm it has context:

   ```
   Explain the overall structure of this Python project and what each file contains.
   ```

   Copilot reads the files in the current directory and responds with a summary.

<div align="left">
<img src="./images/003-default-mode.jpg" alt="Copilot interactive session responding to a project overview prompt">
</div>

3. Ask it to make a small change — for example, add a `/ping` endpoint. Copilot will propose the change and ask for your approval before writing to disk:

   ```
   Add a GET /ping endpoint to the FastAPI app that returns {"status": "ok"} with HTTP 200.
   ```

   When Copilot requests permission to edit `main.py`, choose **Yes** to allow the change for this action only, or **Yes, and approve for the rest of this session** to skip future prompts for this file tool.

#### Plan Mode

Plan mode is ideal for larger or less well-defined tasks. Instead of immediately writing code, Copilot analyses your request, asks clarifying questions, and produces a structured step-by-step implementation plan. No code is written until you approve the plan.

4. Press `Shift+Tab` to cycle to **Plan** mode. You will see the mode indicator change in the prompt.

5. Give Copilot a multi-step task:

   ```
   Refactor the token generation endpoint to use a service class with dependency injection, add CRUD operations for a User entity with Pydantic models, and write pytest tests for both.
   ```

   Copilot will ask clarifying questions — for example, which test framework to use, whether to use in-memory or mocked repositories — before producing a numbered plan.

<div align="left">
<img src="./images/004-plan-mode.jpg" alt="Copilot CLI plan mode showing a structured implementation plan with numbered steps">
</div>

6. Review the plan. You can ask Copilot to revise a specific step before it begins:

   ```
   Change step 3 to use pytest-mock instead of unittest.mock for mocking.
   ```

   Once you are satisfied, confirm the plan and Copilot will execute each step sequentially, requesting tool approval as needed.

#### Auto Model Selection

Instead of manually picking a model every session, you can let Copilot automatically choose the best available model on your behalf. This reduces rate limiting and removes the mental overhead of model selection. Auto model selection is available on all Copilot plans.

7. Open the model picker and choose **Auto**:

   ```
   /model
   ```

   Select **Auto** from the list. With Auto enabled, Copilot picks from a pool of 1× multiplier models — currently GPT-4.1, GPT-5 mini, GPT-5.2-Codex, GPT-5.3-Codex, Claude Haiku 4.5, and Claude Sonnet 4.5 — subject to your organisation's policies and your subscription. The pool changes over time as new models become available.

   > **Note**: Auto will never select models excluded by administrator policy, models with a premium multiplier greater than 1×, or models unavailable on your plan.

<div align="left">
<img src="./images/005-auto-model.jpg" alt="/model picker with Auto selected in the Copilot CLI">
</div>

8. To see which model handled a response, check the CLI output — the model used is reported alongside each reply.

9. Override Auto at any time by picking a specific model from `/model`, or set one at launch:

   ```bash
   copilot --model claude-sonnet-4.6
   ```

   > **Paid plan tip**: When using Auto on a paid plan (Pro, Pro+, Business, Enterprise), qualifying models receive a **10% multiplier discount** compared to selecting the same model manually.

   > **Coding agent note**: Auto model selection for `gh agent-task` (Copilot coding agent) is generally available for **Pro and Pro+ plans only** and currently selects from Claude Sonnet 4.5.

In the above exercises we achieved the following:
- ✅ Used default mode for interactive ask/execute tasks
- ✅ Used plan mode to design a multi-step implementation before writing code
- ✅ Enabled Auto model selection for automatic model choice

---

### 🗒️ Section 3: Tool Approval and Context Management

🎯 **Learning Goals**
- Understand how tool approval protects you from unintended changes
- Use `--allow-tool`, `--deny-tool`, and `--allow-all-tools` to configure automatic approval
- Use programmatic mode with `-p` for scripted and headless workflows
- Manage conversation context with `/compact`, `/context`, and auto-compaction

#### Tool Approval

Every time Copilot wants to modify a file or execute a shell command it asks for your approval. This keeps you in control — but for trusted, repetitive tasks you can pre-approve specific tools.

1. Launch a new session and ask Copilot to run the project's tests:

   ```bash
   copilot
   ```

   ```
   Run all the tests in the project and show me a summary of the results.
   ```

   When Copilot asks permission to run `pytest`, notice the three options presented:

   ```
   1. Yes
   2. Yes, and approve pytest for the rest of this session
   3. No, and tell Copilot what to do differently (Esc)
   ```

   Choose **2** to approve `pytest` for the rest of the session.

<div align="left">
<img src="./images/006-tool-approval.jpg" alt="Copilot CLI tool approval prompt with three options">
</div>

2. Use the `--allow-tool` flag to pre-approve specific commands at launch. This is useful for CI scripts or trusted tasks:

   ```bash
   copilot --allow-tool 'shell(pytest)' --allow-tool 'write'
   ```

   - `shell(COMMAND)` — approves a specific shell command. Omit the command name to allow all shell commands.
   - `write` — approves all file modifications without individual prompts.
   - `MCP_SERVER_NAME` — approves all tools from a named MCP server.

3. Use `--deny-tool` to block specific commands even when `--allow-all-tools` is set. For example, to allow everything except `rm` and `git push`:

   ```bash
   copilot --allow-all-tools --deny-tool 'shell(rm)' --deny-tool 'shell(git push)'
   ```

   `--deny-tool` always takes precedence over `--allow-tool` and `--allow-all-tools`.

<div align="left">
<img src="./images/007-deny-tool.jpg" alt="Copilot CLI launched with allow-all-tools and specific deny-tool overrides">
</div>

#### Programmatic Mode

For headless use in scripts and CI pipelines, pass a prompt directly with `-p` instead of opening an interactive session:

4. Run a single task non-interactively:

   ```bash
   copilot -p "Show me this week's commits and summarize them" --allow-tool 'shell(git)'
   ```

   Copilot completes the task and exits. You can also pipe options from a script:

   ```bash
   echo "Run pytest and report any failures" | copilot --allow-tool 'shell(pytest)'
   ```

<div align="left">
<img src="./images/008-programmatic.jpg" alt="Copilot CLI programmatic mode completing a task and exiting">
</div>

#### Context Management

For long sessions working on large codebases, the conversation history can approach the model's token limit. The CLI manages this automatically and gives you manual control.

5. Check how much of your context window is in use at any time:

   ```
   /context
   ```

   This shows a token usage breakdown split by system prompt, conversation history, and available remaining tokens.

6. When you want to free up context without ending the session, run:

   ```
   /compact
   ```

   Copilot compresses the conversation history while retaining key facts about the tasks completed so far. Press `Escape` to cancel if you change your mind.

<div align="left">
<img src="./images/009-compact.jpg" alt="/compact command output showing context compressed from 80% to 12% usage">
</div>

7. Auto-compaction kicks in automatically when the session approaches **95%** of the token limit, compressing history in the background without interrupting your workflow. This enables virtually unlimited session length — you can work on a feature from start to finish without restarting.

In the above exercises we achieved the following:
- ✅ Understood per-action tool approval prompts
- ✅ Pre-approved tools with `--allow-tool` and blocked tools with `--deny-tool`
- ✅ Used programmatic mode for headless CLI invocations
- ✅ Monitored and managed conversation context with `/context` and `/compact`

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

<div align="left">
<img src="./images/010-list-prs.jpg" alt="Copilot CLI listing open pull requests from GitHub.com">
</div>

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

<div align="left">
<img src="./images/011-create-pr.jpg" alt="Copilot CLI creating a pull request on GitHub.com">
</div>

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

7. The default model is **Claude Sonnet 4.6**. To see all available models and switch, use the `/model` slash command:

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

### 🗒️ Section 5: Custom Agents, Custom Instructions, and MCP Integrations

🎯 **Learning Goals**
- Understand custom agents and how to configure them for specialised tasks
- Create custom instructions files for Python projects
- Use Copilot Memory for persistent context across sessions
- Add additional MCP servers to extend CLI capabilities beyond GitHub

#### Custom Instructions for Python

GitHub Copilot instructions files are markdown documents that provide essential context to guide Copilot's behavior within a specific codebase. These files help tailor AI-generated suggestions to match your team's coding standards, architectural patterns, naming conventions, testing strategies, and deployment practices.

1. Create a `copilot-instructions.md` file in the `.github` directory of your project:

   ```markdown
   # Project Guidelines

   ## Project Overview

   This repository contains a FastAPI application that provides various endpoints for token generation, text echo, and checksum calculation.

   ## Technology Stack
   - **Framework**: FastAPI
   - **Testing**: pytest with pytest-mock
   - **Validation**: Pydantic models

   ### ✨ Coding Style
   - Follow **PEP 8** standards for formatting and naming.
   - Use **type hints** consistently across all functions.
   - Prefer **f-strings** for string interpolation.
   - Include **Google-style docstrings** for all public functions and classes.

   ### 🧪 Testing Guidance
   - Use **pytest** for writing unit tests.
   - Mock external dependencies using `pytest-mock`.
   - Name tests descriptively, e.g., `test_generate_token_valid_input`.

   ### 🏗️ Architecture Preferences
   - Use **FastAPI** conventions for routing and dependency injection.
   - Define **Pydantic models** for request and response schemas.
   - Keep logic modular—separate API routes, models, and utility functions.

   ### 📚 Documentation & Comments
   - Generate concise inline comments for non-obvious logic.
   - Include endpoint descriptions in FastAPI route docstrings.
   - Avoid redundant comments that restate code behavior.
   ```

2. Create scoped instructions for specific directories. In `.github/instructions/`, create `api.instructions.md`:

   ```markdown
   ---
   applyTo: "webapp/**/*.py"
   ---

   ## API Coding Conventions

   - Follow PEP 8 for variables and functions
   - PascalCase for class names
   - Use type hints for clarity and tooling support
   - Add detailed docstrings to endpoint functions
   - Include examples in Pydantic model Config
   - Use descriptive parameter names and Field descriptions
   - Consider async handlers for I/O bound operations
   - Configure CORS with specific origins in production
   - Use middleware for rate limiting

   ## Error Handling

   - Return appropriate HTTP status codes
   - Provide human-readable error messages with actionable information
   - Use FastAPI's HTTPException for error responses
   ```

#### Custom Agents

Custom agents are specialised versions of Copilot configured for specific tasks or roles — for example, a data science agent that follows your team's pandas conventions, or a security agent that checks for common vulnerabilities.

3. Create a custom agent configuration file at `.github/agents/fastapi-expert.md` in the sample project:

   ```markdown
   ---
   name: fastapi-expert
   description: A FastAPI specialist that follows best practices for async Python web development.
   ---

   ## Role
   You are a Python backend engineer specialising in FastAPI and async Python.

   ## Conventions
   - Use async/await for all I/O operations
   - Define Pydantic models for all request/response bodies
   - Use dependency injection for shared resources (database, config)
   - Follow RESTful naming conventions for endpoints
   - Include OpenAPI documentation via docstrings
   - Use proper HTTP status codes (201 for creation, 204 for delete, etc.)
   - Implement proper error handling with HTTPException
   ```

4. Invoke the custom agent in a session by mentioning it in your prompt:

   ```
   @fastapi-expert Add rate limiting middleware to the API and implement proper error handling for all endpoints.
   ```

   The `@fastapi-expert` agent uses your conventions file as additional system context, producing output that matches your team's standards without you having to explain them each time.

#### Copilot Memory

Copilot Memory allows the CLI to build a persistent understanding of your repository across sessions. It stores "memories" — coding conventions, patterns, and preferences deduced from your work — so you don't need to re-explain context in every new session.

5. After completing a significant task in a session, ask Copilot to summarise what it learned:

   ```
   /memory
   ```

   Review the stored memories. You can add, edit, or delete entries to correct any misunderstandings.

6. Start a new session and observe that Copilot already knows project-specific context — for example, that you prefer pytest over unittest or that you use Pydantic v2 syntax — without you having to repeat it.

#### Adding MCP Servers

The CLI ships with the GitHub MCP server pre-configured and authenticated. You can add additional MCP servers (for databases, monitoring tools, cloud providers, etc.) via a config file.

7. Open or create `~/.copilot/mcp-config.json` (user-level, applies to all projects) or `.github/mcp.json` (repository-level):

   ```json
   {
     "servers": {
       "postgres": {
         "command": "docker",
         "args": [
           "run", "-i", "--rm",
           "-e", "DATABASE_URL",
           "mcp/postgres"
         ],
         "env": {
           "DATABASE_URL": "postgresql://localhost:5432/mydb"
         }
       }
     }
   }
   ```

8. List configured MCP servers from within an active session:

   ```
   /mcp
   ```

   Select a server from the list to see which tools it exposes. You can then use those tools in natural language:

   ```
   Use the postgres MCP server to show me the schema of the users table.
   ```

9. When pre-approving MCP server tools at launch, use the server name as the `--allow-tool` argument:

   ```bash
   copilot --allow-tool 'postgres'
   ```

   To allow only a specific tool from the server:

   ```bash
   copilot --allow-tool 'postgres(query)' --deny-tool 'postgres(execute)'
   ```

#### Hooks

Hooks let you execute custom shell commands at key points during agent execution — for example, running a linter after every file write, or logging actions for an audit trail.

10. Create a hook file at `.github/hooks/post-write.sh`:

    ```bash
    #!/bin/bash
    # Run the linter and formatter on any Python file that was just written
    if [[ "$COPILOT_HOOK_FILE" == *.py ]]; then
      ruff check --fix "$COPILOT_HOOK_FILE"
      ruff format "$COPILOT_HOOK_FILE"
    fi
    ```

    Register the hook in `.github/hooks/config.json`:

    ```json
    {
      "hooks": [
        { "event": "post-write", "command": ".github/hooks/post-write.sh" }
      ]
    }
    ```

    Now every time Copilot writes a `.py` file, it will be automatically linted and formatted before the next step runs.

In the above exercises we achieved the following:
- ✅ Created custom instructions for Python projects
- ✅ Created a custom agent with project-specific conventions
- ✅ Used Copilot Memory for persistent cross-session context
- ✅ Added and queried additional MCP servers
- ✅ Configured hooks to automate linting after file writes

---

### 🗒️ Section 6: A Real-World End-to-End Python Workflow

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

<div align="left">
<img src="./images/018-plan-pagination.jpg" alt="Plan mode showing numbered steps for the pagination feature">
</div>

4. Once you approve the plan, press `Shift+Tab` to switch back to default mode (or keep plan mode — Copilot will execute each step and check in after each one).

#### Step 3 — Build and test

5. Copilot creates `models/pagination.py`, updates the route handler in `main.py`, and scaffolds tests in `tests/`. When it requests permission to run `pytest`, approve it:

   ```
   1. Yes, and approve pytest for the rest of this session
   ```

   Copilot runs the tests, observes any failures, and self-corrects until all tests pass.

<div align="left">
<img src="./images/019-self-correct.jpg" alt="Copilot CLI running tests, observing a failure, and self-correcting">
</div>

6. Check context usage mid-session if the conversation has been running for a while:

   ```
   /context
   ```

   If usage is above 70%, run `/compact` to free up space before the final steps.

#### Step 4 — Commit and create a PR via GitHub.com integration

7. Ask Copilot to commit the changes and open a pull request:

   ```
   Commit these changes with a conventional commit message and create a pull request against main with a description that summarises the pagination feature.
   ```

   Copilot uses the built-in GitHub MCP server to create the PR on GitHub.com, with you listed as the author.

<div align="left">
<img src="./images/020-create-pr.jpg" alt="Copilot CLI creating a pull request via GitHub.com integration">
</div>

8. Kick off a remote agent task to add docstrings to the new code, so it runs asynchronously in the cloud while you move on to other work:

   ```bash
   gh agent-task create --repo <owner>/<repo> --issue <number> \
     --body "Add Google-style docstrings to PaginatedResponse and the updated token route handler."
   ```

9. Monitor and merge:

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

### Useful Links and Further Learning

- [About GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- [Installing GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli)
- [Using GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Responsible use of GitHub Copilot CLI](https://docs.github.com/copilot/responsible-use/copilot-cli)
- [GitHub Copilot CLI changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)
- [Copilot CLI ACP server](https://docs.github.com/copilot/reference/acp-server)
- [Integrate MCP with GitHub Copilot — GitHub Skills](https://github.com/skills/integrate-mcp-with-copilot)


## Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
