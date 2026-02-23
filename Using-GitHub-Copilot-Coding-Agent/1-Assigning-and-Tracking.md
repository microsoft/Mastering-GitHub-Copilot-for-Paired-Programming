[← Back to Module Overview](README.md) | [Next: Custom Instructions and Code Review →](2-Instructions-and-Review.md)

# Assigning Tasks and Tracking Agent Sessions

## 🗒️ Part 1: Assigning Tasks to GitHub Copilot Coding Agent

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
<img width="500" alt="Assigment panel for issue showing Copilot is selected and the name has an AI badge next to it." src="https://github.com/user-attachments/assets/dec2f4af-c606-4350-9911-ee109c64cf36" />

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

<img width="800" alt="Screenshot of GitHub.com header hovering over the Copilot Icon for the agents panel" src="https://github.com/user-attachments/assets/4040c625-2d6e-4195-bf16-21cc62f37460" />

1. Click the agent icon (looks like a robot) in the top navigation bar on any GitHub page.
2. Click the **New task** button below the input box (or select it in the bottom right corner of the input box).
3. Select your repository and describe the work you want done.
4. Submit the task. Copilot will open a new pull request with the changes.

In the above exercises we achieved the following:
- ✅ Assigned a GitHub issue to the coding agent
- ✅ Invoked the agent via a PR comment using `@copilot`
- ✅ Started a new coding agent task from the agents panel

---

## 🗒️ Part 2: Tracking and Steering Agent Sessions

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

<img width="800"  alt="Screenshot of a Copilot session log" src="https://github.com/user-attachments/assets/e6796f87-f326-462b-922f-918896b40f52" />


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

<img width="800" alt="Start of a Copilot log with stop button in blue header bar of the response." src="https://github.com/user-attachments/assets/3f36130c-568b-48fd-980e-baf2e247b483" />

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

[← Back to Module Overview](README.md) | [Next: Custom Instructions and Code Review →](2-Instructions-and-Review.md)
