<header>

# Getting Started with GitHub Copilot

Begin your journey with GitHub Copilot—an AI developer tool that helps you write, understand, test, and improve code faster.

In this foundational module, you will practice using Copilot as a collaborative coding partner through **Ask, Edit, and Agent modes**. You’ll use natural-language prompts to explore a codebase, make scoped updates, and produce a pull request summary and review.

By the end of this module, you’ll be able to explain where Copilot adds value in modern software development and confidently use it in VS Code.

Note: This module is designed around [GitHub Codespaces](https://github.com/codespaces), but you can also complete it locally in Visual Studio Code.
</header>

- **Who is this for**: Developers at any experience level looking to accelerate their coding workflow.
- **What you'll learn**: Setup and practical use of GitHub Copilot, including Copilot Chat and Ask/Edit/Agent workflows.
- **What you'll build**: Improvements to Mergington High School's extracurricular activities website.
- **Prerequisites**:
  - Sign up for a [GitHub account](https://github.com/) (or use an existing account).
  - Sign up for [GitHub Copilot](https://gh.io/copilot).
  - Skills exercise: [Introduction to GitHub](https://github.com/skills/introduction-to-github)
  - Familiarity with [VS Code](https://code.visualstudio.com/)
  - Basic coding principles
- **Timing**: This course can be completed in under an hour.

## Learning objectives

By the end of this module, you'll be able to:

1. Use a preconfigured Codespace to run VS Code securely in your browser.
2. Use multiple GitHub Copilot interaction modes (Ask, Edit, and Agent) to complete development tasks.
3. Use Copilot to summarize and review your pull request.

## Prerequisite reading

- [Accelerate app development by using GitHub Copilot](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/)
- Ask, Edit, and Agent modes: [Learn more](https://learn.microsoft.com/shows/visual-studio-code/ask-edit-and-agent-in-depth-overview-of-github-copilot-chat-modes)
- Video overview: [Ask, Edit, and Agent - In-depth Overview of GitHub Copilot Chat Modes](https://www.youtube.com/watch?v=s7Qzq0ejhjg)

---

## How to start this course

Create your own copy of the exercise repository:

- **Copy exercise repository**: https://github.com/new?template_owner=skills&template_name=getting-started-with-github-copilot&owner=%40me&name=skills-getting-started-with-github-copilot&description=Exercise:+Get+started+using+GitHub+Copilot&visibility=public

Then wait for setup automation to complete and refresh the page.

### Setup readiness checks

Before starting the lab tasks, confirm:

1. The repository copy is created under your account.
2. GitHub Actions setup has completed successfully (indicated by a checkmark on the workflow run).
3. Your Codespace opens with VS Code and Copilot Chat available.
4. The lesson instructions and starter files are visible in your copied repository.

If setup is still running, wait and refresh when the workflow finishes.

<details>
<summary>Having trouble? 🤷</summary><br/>

When copying the exercise, we recommend:

- Choose your personal account or an organization as the owner.
- Prefer a public repository (private repositories can consume Actions minutes).

If the exercise is not ready yet:

1. Open the [Actions](../../actions) tab.
2. Check whether a setup job is still in progress.
3. If a setup workflow failed, open an issue in this repository and include the failing run details.

</details>

---

## Exercise map (recommended flow)

### Milestone 1: Environment and context

Goal: Verify your environment and understand the project quickly.

- Open the project in Codespaces (or local VS Code).
- Confirm Copilot Chat is enabled.
- Use **Ask mode** to understand project structure.

Adapt these prompts to the repository you copied for this lab (the Mergington High School extracurricular activities project).

Prompt examples:

- "Summarize this repository structure and explain where I should start as a beginner."
- "Explain the current behavior of the extracurricular activities site and identify one low-risk improvement."

Checkpoint:

- You can identify where to make your first change and why.

### Milestone 2: Implement a scoped change with Copilot

Goal: Make one realistic, bounded improvement.

- Use **Edit mode** for a targeted update.
- Ask Copilot for two implementation options and choose one.
- Apply the change and review the diff before accepting.

When using these prompts, replace `[specific page/feature]` with a real target in your repository (for example: `clubs listing page`).

Prompt examples:

- "Propose two ways to improve [specific page/feature], with trade-offs and level of effort."
- "Implement option 1 with minimal changes and preserve existing behavior."

Checkpoint:

- You made one focused change and can explain why it is safe.

### Milestone 3: Use Agent mode for multi-step support

Goal: Practice delegating a multi-step task while keeping human review in control.

- Use **Agent mode** to request a small multi-step update.
- Review every proposed edit and keep only relevant changes.
- Ask for a short validation checklist.

Prompt examples:

- "Plan and apply a small UX/content improvement across related files, then summarize all edits and risks."
- "Generate manual validation steps for the changes you made."

Checkpoint:

- You can describe what Agent mode did, what you accepted, and what you rejected.

### Milestone 4: Pull request summary and self-review

Goal: Produce a quality PR summary and validate confidence before submission.

- Use Copilot to draft a pull request summary.
- Ask Copilot for a self-review checklist focused on regressions and clarity.

Prompt examples:

- "Draft a pull request summary with: purpose, changed files, risks, and validation steps."
- "Review this change set and list potential regressions, missing tests, or unclear decisions."

Checkpoint:

- Your PR summary clearly states what changed, why, and how it was validated.

---

## Reflection prompts (confidence building)

After completing the lab, answer:

1. Which mode (Ask, Edit, Agent) was most useful for each milestone, and why?
2. What Copilot output did you accept, and what did you reject?
3. What validation steps increased your confidence in the final change?
4. What would you improve in your prompts next time?

---

## Local VS Code alternative (if not using Codespaces)

If you complete this module locally:

1. Clone your copied exercise repository.
2. Open it in VS Code.
3. Sign in to GitHub and confirm Copilot + Copilot Chat are enabled.
4. Follow the same milestone flow above.

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)
