# Using GitHub Copilot Coding Agent

Welcome to a hands-on, multi-section module focused on the **GitHub Copilot Coding Agent** — an autonomous AI developer that works independently in the background to complete tasks across the full software delivery lifecycle. Unlike IDE-based assistant features, the coding agent operates on GitHub itself, handling everything from branch creation and code changes to pull request authoring and iterative review cycles.

This module walks through every major capability of the coding agent available today, giving you practical experience with each feature in a real workflow.

---

- **Who this is for**: Developers, DevOps Engineers, Engineering Managers, Platform Engineers, and anyone who wants to scale their team's output with AI.
- **What you'll learn**: How to assign tasks, track sessions, steer Copilot's work, customize agent behavior, integrate MCP servers, and manage security — all within a GitHub-native workflow.
- **What you'll build**: A hands-on understanding of Copilot coding agent across the complete software delivery lifecycle: planning → coding → testing → review → merge.
- **Prerequisites**: GitHub Copilot Pro, Pro+, Business, or Enterprise plan. [Sign up for GitHub Copilot](https://gh.io/copilot).
- **Timing**: This module can be completed in approximately 60–90 minutes.

By the end of this module, you'll acquire the skills to:

- Assign GitHub issues and pull requests to Copilot as a coding resource.
- Track, steer, and stop Copilot agent sessions from multiple surfaces.
- Review and iterate on Copilot-generated pull requests.
- Customize agent behavior with instructions, agent profiles, MCP servers, hooks, and skills.
- Use Copilot to address security alerts at scale with security campaigns.
- Integrate the coding agent into IDEs, the GitHub CLI, Raycast, and mobile tools.

## 📖 Prerequisite reading

- [About GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot/?WT.mc_id=academic-113596-abartolo)
- [GitHub Copilot coding agent vs. agent mode](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent#copilot-coding-agent-versus-agent-mode)

## 📋 Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup) (Pro, Pro+, Business, or Enterprise plan required for coding agent)
2. Open [this repository with Codespaces](https://codespaces.new/github-samples/node-recipe-app?quickstart=1) — a Node.js recipe app with known missing features that serves as our working example throughout this module.

**Right click the following Codespaces button to open your Codespace in a new tab**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/github-samples/node-recipe-app?quickstart=1)

> **Note:** If you have an existing Codespace with this project, please create a new one for this module.

---

## 🗒️ Section 1: Assigning Tasks to GitHub Copilot Coding Agent

### 🎯 Learning Goals

- Understand how the coding agent differs from IDE agent mode.
- Assign a GitHub Issue to Copilot coding agent.
- Trigger Copilot coding agent from multiple surfaces: issues, pull request comments, and the agents panel.

### What is the Copilot Coding Agent?

The **GitHub Copilot coding agent** works autonomously in the background using a GitHub Actions-powered ephemeral development environment. When you give it a task, it:

1. Reads your codebase and issue context.
2. Creates a `copilot/` branch.
3. Writes code, runs your tests and linters, and iterates on errors.
4. Opens a pull request and requests your review.

This is distinct from **agent mode in your IDE**, which edits your local files interactively. The coding agent is fully asynchronous — you can close your laptop while it works.

### Exercise 1A: Assign an Issue to Copilot

1. Navigate to your repository's **Issues** tab on GitHub.com.
2. Create a new issue with a clear, well-scoped description. For example:

   ```
   Title: Add the ability to delete a recipe

   Description:
   Users should be able to delete a recipe from the recipe list. 
   - Add a DELETE /recipes/:id endpoint in src/routes.js
   - Remove the recipe row from the SQLite database
   - Add a "Delete" button to the recipe detail view
   - Write a test that confirms a deleted recipe returns 404
   ```

3. On the issue page, click **Assignees** and select **Copilot** from the assignee list.

   > Copilot will begin working immediately. You'll see the issue label update to indicate an agent session is in progress.

4. Observe that Copilot creates a new branch named `copilot/<issue-number>-<slug>` and begins opening commits.

### Exercise 1B: Trigger Copilot from a Pull Request Comment

You can also invoke the coding agent on an *existing pull request* by mentioning `@copilot` in a PR comment.

1. Open any open pull request in your repository.
2. In a comment, type a specific request, for example:

   ```
   @copilot Please add input validation to the recipe creation form 
   and return a 400 status code with an error message if the title field is empty.
   ```

3. Copilot will respond in the PR thread, then push additional commits to address your request.

### Exercise 1C: Trigger Copilot from the Agents Panel

The **agents panel** is available on every page on GitHub.com.

1. Click the agent icon (looks like a hexagon/robot) in the top navigation bar on any GitHub page.
2. Click **New task**.
3. Select your repository and describe the work you want done.
4. Submit the task. Copilot will open a new pull request with the changes.

In the above exercises we achieved the following:
- ✅ Assigned a GitHub issue to the coding agent
- ✅ Invoked the agent via a PR comment using `@copilot`
- ✅ Started a new coding agent task from the agents panel

---

## 🗒️ Section 2: Tracking and Steering Agent Sessions

### 🎯 Learning Goals

- Track the progress of Copilot's work across multiple surfaces.
- Read and interpret session logs.
- Steer Copilot mid-session when you want to redirect its approach.
- Stop a session that has gone off-track.

### The Agents Tab

1. Open the [agents tab](https://github.com/copilot/agents) by clicking the agent icon in the GitHub navigation bar, then selecting **View all**.
2. You'll see a list of all your running and past agent sessions.
3. Click on a session to open the **session log and overview**, which shows:
   - Session status (running, completed, stopped)
   - Token usage and session duration
   - A step-by-step internal log showing how Copilot approached your task

### Reading Session Logs

Session logs show Copilot's internal reasoning and tool usage. You can see:

- Which files Copilot read to understand the codebase.
- What commands it ran (e.g., test runners, linters).
- How it iterated to fix errors before pushing.
- Which security checks it performed (CodeQL, secret scanning, dependency vulnerability checks).

> **Tip:** Session logs are also accessible from Visual Studio Code via the GitHub Pull Requests extension. Click on a pull request in the Copilot sessions list, then click **View Session**.

### Exercise 2A: Steer a Running Session

While Copilot is working, you can give it additional guidance from the agents tab:

1. Open the [agents tab](https://github.com/copilot/agents) and select an **in-progress** session.
2. Type a steering message in the prompt box, for example:

   ```
   Use our existing ErrorHandler utility instead of writing custom 
   try-catch blocks for the new endpoints.
   ```

3. Submit the message. Copilot will incorporate your guidance after finishing its current tool call.

> **Note:** Steering consumes one premium request per message.

### Exercise 2B: Stop a Session

If Copilot is going in a wrong direction or you have changed your mind about a task:

1. Open the session log viewer from the agents tab.
2. Click **Stop session**.

The agent stops immediately. The branch and any commits made so far are preserved, so you can inspect them.

### Tracking Across Other Surfaces

| Surface | How to access |
|---|---|
| **GitHub CLI** | `gh agent-task list` / `gh agent-task view --repo owner/repo <pr-number>` (requires CLI v2.80.0+) |
| **VS Code** | GitHub Pull Requests extension → Copilot sessions list in the sidebar |
| **JetBrains IDEs** | GitHub Copilot Chat extension → **GitHub Coding Agent Jobs** button (public preview) |
| **Eclipse** | GitHub Copilot Chat extension → agent icon in chat window (public preview) |
| **GitHub Mobile** | Home page → Agents section → **Agent Tasks** |
| **Raycast** | GitHub Copilot extension for Raycast → **View Tasks** command |

In the above exercises we achieved the following:
- ✅ Navigated the agents tab to track sessions
- ✅ Read and interpreted a Copilot session log
- ✅ Steered a running session with additional guidance
- ✅ Stopped an off-track session

---

## 🗒️ Section 3: Reviewing and Iterating on Copilot Pull Requests

### 🎯 Learning Goals

- Review a pull request opened by Copilot coding agent.
- Leave iterative feedback to refine Copilot's solution.
- Request a Copilot automated code review on your own pull requests.
- Understand the governance model around Copilot PRs.

### Exercise 3A: Review a Copilot-Generated Pull Request

When Copilot finishes a task, it opens a pull request and requests your review.

1. Navigate to the **Pull Requests** tab in your repository.
2. Open the pull request created by Copilot (marked with the Copilot author badge).
3. Review the changes. The PR description will include:
   - A summary of what was changed and why.
   - References back to the original issue.
   - Any security scan results from the automated validation.

4. Leave a review comment requesting a change. For example:

   ```
   The delete confirmation modal is a good start, but please also add 
   an accessible aria-label to the confirmation button.
   ```

5. Submit your review. Copilot will pick up your feedback, push new commits to the same branch, and re-request your review.

> **Governance note:** The user who asked Copilot to create a pull request **cannot approve that same pull request**. This enforces independent review. Copilot also cannot mark its own PRs as "Ready for review" or merge them.

### Exercise 3B: Request a Copilot Code Review on Your Own PR

Copilot can also serve as a first-pass reviewer on *your* pull requests before a human review.

1. Open a pull request you've authored.
2. In the **Reviewers** panel on the right side of the PR, click the gear icon.
3. Select **Copilot** from the reviewer list.
4. Within seconds, Copilot will leave inline comments on the diff, pointing out bugs, inefficiencies, and improvements.
5. Apply or dismiss each suggestion using the inline comment controls.

In the above exercises we achieved the following:
- ✅ Reviewed and gave iterative feedback on a Copilot-authored PR
- ✅ Used Copilot as an automated code reviewer on a human-authored PR

---

## 🗒️ Section 4: Customizing Copilot Coding Agent

### 🎯 Learning Goals

- Write custom repository instructions to guide Copilot's behavior.
- Create a custom agent profile for a specialized coding persona.
- Extend the agent with MCP servers for additional data sources and tools.
- Add hooks to execute custom shell commands during agent execution.
- Understand Copilot Memory (public preview).

### Part 1: Custom Instructions

Custom instructions are Markdown files you store in your repository that tell Copilot about your preferences, conventions, and architecture — so you don't have to repeat yourself in every task.

1. Create the file `.github/copilot-instructions.md` in your repository.
2. Add content like the following:

   ```markdown
   # Project Guidelines

   ## Technology Stack
   - Node.js with Express
   - SQLite via better-sqlite3
   - EJS templates for server-rendered HTML
   - xUnit-style tests with Jest

   ## Code Style
   - Use async/await — never raw callbacks or `.then()` chains
   - Follow the existing error handling pattern in `src/errorHandler.js`
   - All new routes must be added to `src/routes.js` following the existing pattern
   - Use 2-space indentation

   ## Testing
   - Every new route must have a corresponding test in `tests/`
   - Use supertest for HTTP integration tests

   ## Security
   - Never log user-provided input directly
   - Validate all request parameters before database access
   ```

3. Commit the file. All subsequent Copilot coding agent sessions in this repository will now follow these instructions automatically.

> **Tip:** You can also define custom instructions at the organization level from your organization's settings.

### Part 2: Custom Agents — Agent Profiles

**Custom agents** are specialized versions of Copilot you define once using a Markdown file called an **agent profile**. Each profile encodes a specific persona, set of tools, and behavior.

1. Create the file `.github/agents/documentation-agent.md`:

   ```markdown
   ---
   name: documentation-agent
   description: Specialist for maintaining and improving project documentation
   ---

   You are a technical documentation specialist. Your scope is limited to 
   documentation files only — README.md, docs/, and inline code comments.
   Do not modify source code logic.

   Follow these guidelines:
   - Structure READMEs with: Overview, Installation, Usage, API Reference, Contributing
   - Use clear, concise language targeted at developers unfamiliar with the project
   - Add code examples for every API endpoint documented
   - Use relative links for internal files
   - Add alt text to all images
   - Ensure all headings are in sentence case
   ```

2. Create a second agent profile `.github/agents/test-agent.md`:

   ```markdown
   ---
   name: test-agent
   description: Specialist for writing comprehensive test coverage using Jest
   ---

   You are a testing specialist focused exclusively on writing and improving tests.
   Do not modify application source code — only test files.

   Guidelines:
   - Use Jest with supertest for HTTP route tests
   - Write both happy-path and error-path tests for every function
   - Aim for 80%+ line coverage on any file you touch
   - Use descriptive test names that explain the scenario being tested
   - Mock external dependencies using jest.mock()
   ```

3. Commit both files. When you assign a task from the agents panel or an issue, you can now select a specific custom agent to use.

> **Note:** Custom agent profiles can also be defined at the organization level in a `.github-private` repository, making them available across all repositories in your organization.

### Part 3: Model Context Protocol (MCP) Servers

**MCP servers** give Copilot coding agent access to external data sources and tools — such as a project management system, internal documentation, or a database — that it wouldn't be able to reach otherwise.

1. Create the file `.github/mcp.json` in your repository:

   ```json
   {
     "mcpServers": {
       "github": {
         "type": "github",
         "tools": ["list_issues", "search_code", "get_pull_request"]
       }
     }
   }
   ```

2. The default GitHub MCP server is pre-configured and gives the agent access to your repository's issues, historic pull requests, and code search — grounding its responses in real project context.

3. To add a third-party MCP server (for example, a Jira integration), follow the [MCP integration guide](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp) and add the server configuration to `.github/mcp.json`.

> **Note:** Organization and enterprise-level agent profiles can embed MCP server configuration directly within the agent profile YAML frontmatter.

### Part 4: Hooks — Lifecycle Automation

**Hooks** execute custom shell commands at specific points during an agent session. Use them to add validation, custom linting, security scanning, or notification workflows.

Available hook points:
- `pre-run` — before Copilot begins working
- `post-run` — after Copilot finishes working

Create `.github/copilot/hooks.yaml`:

```yaml
hooks:
  post-run:
    - name: Run custom linter
      run: npm run lint -- --max-warnings 0
    - name: Check for TODO comments
      run: |
        if grep -r "TODO" src/; then
          echo "Warning: TODO comments found in src/"
        fi
```

If a hook exits with a non-zero status, Copilot will see the output and attempt to address the issue before completing its session.

### Part 5: Copilot Memory (Public Preview)

**Copilot Memory** allows the coding agent to persist facts it learns about your repository across sessions — so it builds up knowledge over time without you having to repeat context.

To enable Copilot Memory:
1. Navigate to your [GitHub Copilot settings](https://github.com/settings/copilot).
2. Enable **Copilot Memory** (available for Pro and Pro+ plans).
3. After a session completes, Copilot will write memory entries such as: "This project uses better-sqlite3, not the default sqlite3 package."

In the above exercises we achieved the following:
- ✅ Created repository custom instructions
- ✅ Built specialized custom agent profiles  
- ✅ Configured MCP server access
- ✅ Set up lifecycle hooks for post-run validation
- ✅ Understood Copilot Memory for persistent context

---

## 🗒️ Section 5: Security and Compliance with Copilot Coding Agent

### 🎯 Learning Goals

- Understand the built-in security protections of the coding agent.
- Use security campaigns to assign vulnerability fixes to Copilot at scale.
- Understand the governance and compliance model for Copilot-authored code.

### Built-in Security Protections

Every session Copilot runs includes automatic security validation before the pull request is opened:

| Protection | What it does |
|---|---|
| **CodeQL analysis** | Scans generated code for security vulnerabilities |
| **Dependency vulnerability check** | Checks new dependencies against the GitHub Advisory Database for High/Critical CVEs |
| **Secret scanning** | Detects hardcoded API keys, tokens, and secrets |
| **Firewall-restricted environment** | Copilot's development environment has internet access limited to an allowlist |
| **Branch restrictions** | Copilot can only push to `copilot/` branches — never `main` or `master` |

Details of all security checks are visible in the session log.

> **Note:** These built-in checks do **not** require a GitHub Advanced Security, Secret Protection, or Code Security license.

### Exercise 5A: Assign a Security Alert to Copilot via a Security Campaign

**Security campaigns** let you fix groups of security alerts at scale by assigning them to the coding agent.

1. Navigate to your repository's **Security** tab → **Code scanning alerts**.
2. If there are open alerts, click **Campaigns** in the left nav (available for orgs with GitHub Advanced Security).
3. Create a new campaign, assign the relevant alerts, and set **Copilot** as the assignee.
4. Copilot will work through each alert, creating a pull request per fix.

> **Tip:** For repositories without active alerts, you can trigger this flow manually by navigating to a specific code scanning alert and selecting "Assign to Copilot."

### Governance Model Summary

| Governance rule | Effect |
|---|---|
| Only write-access users can trigger the agent | Prevents unauthorized code changes |
| Copilot cannot approve its own PRs | Enforces independent human review |
| Commits are co-authored by the requester | Provides full attribution and compliance trail |
| PR workflows require approval before running | Actions don't run until a write-access user clicks "Approve and run workflows" |
| Content exclusions apply | Configure files Copilot should not have access to |

In the above exercises we achieved the following:
- ✅ Reviewed the built-in security scan process
- ✅ Assigned security alerts to Copilot via a security campaign

---

## 🗒️ Section 6: Integrating the Coding Agent Across the Software Delivery Lifecycle

### 🎯 Learning Goals

- Trigger and track coding agent tasks from the GitHub CLI.
- Use Raycast to start and monitor tasks without leaving your desktop.
- Understand how the coding agent fits into the full SDLC — from backlog to merge.

### Exercise 6A: Using the GitHub CLI

> Requires GitHub CLI v2.80.0 or later. Run `gh --version` to check.

```bash
# List your recent agent sessions
gh agent-task list

# View the session associated with PR #45 in your repo
gh agent-task view --repo YOUR-ORG/YOUR-REPO 45

# View the full session log
gh agent-task view --repo YOUR-ORG/YOUR-REPO 45 --log

# Stream live logs as Copilot works
gh agent-task view --repo YOUR-ORG/YOUR-REPO 45 --log --follow
```

### Exercise 6B: Using Raycast (Windows and macOS)

1. Install [Raycast](https://www.raycast.com/).
2. Install the [GitHub Copilot extension for Raycast](https://www.raycast.com/github/github-copilot).
3. Open Raycast and search for **Copilot → View Tasks** to see all your sessions.
4. Press `Command+L` to view the session log for any task.
5. Start a new session directly from Raycast without opening a browser.

### The Coding Agent in the Full SDLC

The table below shows where the coding agent fits in each phase of software delivery:

| SDLC Phase | How the Coding Agent Helps |
|---|---|
| **Planning** | Assign backlog issues directly to Copilot as an assignee, freeing developers for complex work |
| **Development** | Copilot implements features, writes documentation, addresses tech debt in the background while you focus elsewhere |
| **Testing** | Copilot runs your existing test suite during its session and iterates until tests pass; can also improve test coverage on demand |
| **Code Review** | Request Copilot as a reviewer on your PRs for instant feedback; leave iterative comments on Copilot's PRs to steer its solution |
| **Security** | Security campaigns allow bulk assignment of vulnerability fixes to Copilot; built-in CodeQL, secret scanning, and dependency checks run automatically |
| **Documentation** | Assign a documentation-focused custom agent to update READMEs, API docs, and inline comments |
| **Merge & Deploy** | Human approval is always required before merge; Copilot cannot self-approve or merge its own changes |

In the above exercises we achieved the following:
- ✅ Used the GitHub CLI to list, view, and stream agent session logs
- ✅ Configured Raycast for desktop-level task management
- ✅ Mapped the coding agent's capabilities to every phase of the SDLC

---

## 📄 Section 7: Choosing the Right AI Model

### 🎯 Learning Goals

- Understand that the coding agent supports multiple AI models.
- Learn how to change the model for a session.

### AI Model Selection

Depending on where you start a coding agent task, you may be able to select which AI model powers the session. Some models may perform better for specific task types:

- Complex architectural tasks: Try Claude Sonnet or GPT-4o models.
- High-speed, routine tasks: Try models optimized for speed.

To change the model:
1. From the **agents panel** or when assigning an issue, look for the **model selector** dropdown.
2. Select your preferred model.
3. The model selection applies to that session only.

For more details, see [Changing the AI model for GitHub Copilot coding agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/changing-the-ai-model).

---

## ✅ Module Summary

Across this module, the key capabilities you exercised include:

```
Assigning Tasks
  ✅ Issue assignment via the Assignees dropdown
  ✅ @copilot mentions in PR comments
  ✅ New tasks from the agents panel
  ✅ Tasks from VS Code, JetBrains, Eclipse, GitHub CLI, and Raycast

Tracking & Steering
  ✅ Session logs and internal monologue
  ✅ Live log streaming with the GitHub CLI
  ✅ Steering an in-progress session
  ✅ Stopping a session

Review & Iteration  
  ✅ Reviewing and commenting on Copilot PR output
  ✅ Requesting Copilot as a code reviewer on your own PRs

Customization
  ✅ Custom instructions (.github/copilot-instructions.md)
  ✅ Custom agent profiles (.github/agents/*.md)
  ✅ MCP server integration (.github/mcp.json)
  ✅ Lifecycle hooks (.github/copilot/hooks.yaml)
  ✅ Copilot Memory (Pro/Pro+)

Security & Compliance
  ✅ Built-in CodeQL, secret scanning, and dependency checks
  ✅ Security campaign bulk assignment
  ✅ Governance model and audit trail

SDLC Integration
  ✅ Every phase of delivery — planning through merge
```

---

## 📖 Further Reading

- [GitHub Copilot coding agent — all how-to articles](https://docs.github.com/en/copilot/how-tos/use-copilot-agents)
- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- [Extending the coding agent with MCP](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp)
- [About hooks](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks)
- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Responsible use of GitHub Copilot coding agent](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-copilot-coding-agent-on-githubcom)
- [Piloting Copilot coding agent in your organization](https://docs.github.com/en/copilot/tutorials/pilot-copilot-coding-agent)
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/)
- [GitHub Changelog — Copilot](https://github.blog/changelog/?label=copilot)
- [Skills exercise: Expand your team with Copilot coding agent](https://github.com/skills/expand-your-team-with-copilot/)
