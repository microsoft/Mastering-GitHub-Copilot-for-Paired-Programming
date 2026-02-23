[← Previous: Assigning and Tracking](1-Assigning-and-Tracking.md) | [Next: Advanced Customization →](3-Advanced-Customization.md)

# Custom Instructions and Code Review

## 🗒️ Part 1: Custom Instructions

### 🎯 Learning Goals

- Write custom repository instructions to guide Copilot's behavior.
- Understand how instructions improve both the coding agent and Copilot code review.

### Writing Custom Instructions

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

In the above exercise we achieved the following:
- ✅ Created repository custom instructions that guide both the coding agent and Copilot code review

---

## 🗒️ Part 2: Reviewing and Iterating on Copilot Pull Requests

### 🎯 Learning Goals

- Review a pull request opened by Copilot coding agent.
- Leave iterative feedback to refine Copilot's solution.
- Request a Copilot automated code review on your own pull requests.
- Understand the governance model around Copilot PRs.

### Exercise 2A: Review a Copilot-Generated Pull Request

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

### Exercise 2B: Request a Copilot Code Review on Your Own PR

Copilot can also serve as a first-pass reviewer on *your* pull requests before a human review. The custom instructions you created in Part 1 will guide Copilot's review — it will check your code against the conventions and patterns you defined.

1. Open a pull request you've authored.
2. In the **Reviewers** panel on the right side of the PR, click the gear icon.
3. Select **Copilot** from the reviewer list.
4. Within seconds, Copilot will leave inline comments on the diff, pointing out bugs, inefficiencies, and improvements.
5. Apply or dismiss each suggestion using the inline comment controls.

In the above exercises we achieved the following:
- ✅ Reviewed and gave iterative feedback on a Copilot-authored PR
- ✅ Used Copilot as an automated code reviewer on a human-authored PR

---

[← Previous: Assigning and Tracking](1-Assigning-and-Tracking.md) | [Next: Advanced Customization →](3-Advanced-Customization.md)
