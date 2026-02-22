# Module 1: Install and Modes

[← Back to overview](README.md) | [Next: Tool Approval and Context →](2-Tool-Approval-and-Context.md)

---

### 🗒️ Section 1: Install and Verify the GitHub Copilot CLI

🎯 **Learning Goals**
- Install the GitHub Copilot CLI

The **GitHub Copilot CLI** (`copilot`) is a standalone terminal application — distinct from the old `gh copilot` extension — that opens a full interactive AI chat session in your terminal. It ships with the GitHub MCP server built in, supports plan mode and auto model selection, and can autonomously read files, run commands, and interact with GitHub.com on your behalf.

> **Note**: The `gh extension install github/gh-copilot` extension was deprecated in September 2025 and archived at v1.2.0. This workshop uses the new standalone `copilot` CLI.

#### Prerequisites

This workshop uses two separate CLI tools:

- **`copilot`** — the standalone GitHub Copilot CLI (installed below)
- **`gh`** — the GitHub CLI, required for `gh agent-task` commands in Sections 4 and 6

**NOTE:** To complete 4 and 6, the Copilot Free tier will need to be upgraded to allow for Agent Mode

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

   Select **Auto** from the list. With Auto enabled, Copilot picks from a pool of 1× multiplier models — currently GPT-4.1, GPT-5 mini, GPT-5.2-Codex, GPT-5.3-Codex, Claude Haiku 4.5, and Claude Sonnet 4.5 — subject to your organization's policies and your subscription. The pool changes over time as new models become available.

   > **Note**: Auto will never select models excluded by administrator policy, models with a premium multiplier greater than 1×, or models unavailable on your plan.

   > **Paid plan tip**: When using Auto on a paid plan (Pro, Pro+, Business, Enterprise), qualifying models receive a **10% multiplier discount** compared to selecting the same model manually.

   > **Coding agent note**: Auto model selection for `gh agent-task` (Copilot coding agent) is generally available for **Pro and Pro+ plans only**.

8. To see which model handled a response, check the CLI output — the model used is reported alongside each reply.

9. Override Auto at any time by picking a specific model from `/model`, or set one at launch:

   ```bash
   copilot --model claude-sonnet-4.6
   ```

In the above exercises we achieved the following:
- ✅ Used default mode for interactive ask/execute tasks
- ✅ Used plan mode to design a multi-step implementation before writing code
- ✅ Enabled Auto model selection for automatic model choice

---

[← Back to overview](README.md) | [Next: Tool Approval and Context →](2-Tool-Approval-and-Context.md)
