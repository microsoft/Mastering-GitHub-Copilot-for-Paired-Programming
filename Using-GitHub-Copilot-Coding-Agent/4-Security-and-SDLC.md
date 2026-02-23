[← Previous: Advanced Customization](3-Advanced-Customization.md) | [Back to Module Overview →](README.md)

# Security, SDLC Integration, and AI Model Selection

## 🗒️ Part 1: Security and Compliance with Copilot Coding Agent

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

> **Note:** These built-in checks require a GitHub Advanced Security (GHAS license)

### Exercise 1A: Assign a Security Alert to Copilot via a Security Campaign

[Security campaigns](https://docs.github.com/enterprise-cloud@latest/code-security/how-tos/manage-security-alerts/remediate-alerts-at-scale/creating-managing-security-campaigns) let you fix groups of security alerts at scale by assigning them to the coding agent.

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

## 🗒️ Part 2: Integrating the Coding Agent Across the Software Delivery Lifecycle

### 🎯 Learning Goals

- Trigger and track coding agent tasks from the GitHub CLI.
- Use Raycast to start and monitor tasks without leaving your desktop.
- Understand how the coding agent fits into the full SDLC — from backlog to merge.

> **Note:** You can also execute the coding agent into a full SDLC using Copilot Chat in VSCode

### Exercise 2A: Using the GitHub CLI

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

### Exercise 2B: Using Raycast (Windows and macOS)

1. Install [Raycast](https://www.raycast.com/).
2. Install the [GitHub Copilot extension for Raycast](https://www.raycast.com/github/github-copilot).
3. Open Raycast and search for **Copilot → View Tasks** to see all your sessions.
4. To view the session log for any task, open the log using the following command:
 **Windows:**
`Ctrl + L`
**macOS:**
`Command+L` 
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

## 📄 Part 3: Choosing the Right AI Model

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

For more details, see [Changing the AI model for GitHub Copilot coding agent](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/changing-the-ai-model).

---

[← Previous: Advanced Customization](3-Advanced-Customization.md) | [Back to Module Overview →](README.md)
