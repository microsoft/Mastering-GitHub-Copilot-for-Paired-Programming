# Module 2: Tool Approval and Context Management

[← Previous: Install and Modes](1-Install-and-Modes.md) | [Next: GitHub Integration and Workflows →](3-GitHub-Integration-and-Workflows.md)

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

2. Use the `--allow-tool` flag to pre-approve specific commands at launch. This is useful for CI scripts or trusted tasks:

   ```bash
   copilot --allow-tool 'shell(pytest)' --allow-tool 'write'
   ```

   - `shell(COMMAND)` — approves a specific shell command. Omit the command name to allow all shell commands.
   - `write` — approves all file modifications without individual prompts.
 
3. Use `--deny-tool` to block specific commands even when `--allow-all-tools` is set. For example, to allow everything except `rm` and `git push`:

   ```bash
   copilot --allow-all-tools --deny-tool 'shell(rm)' --deny-tool 'shell(git push)'
   ```

   `--deny-tool` always takes precedence over `--allow-tool` and `--allow-all-tools`.

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

7. Auto-compaction kicks in automatically when the session approaches **95%** of the token limit, compressing history in the background without interrupting your workflow. This enables virtually unlimited session length — you can work on a feature from start to finish without restarting.

In the above exercises we achieved the following:
- ✅ Understood per-action tool approval prompts
- ✅ Pre-approved tools with `--allow-tool` and blocked tools with `--deny-tool`
- ✅ Used programmatic mode for headless CLI invocations
- ✅ Monitored and managed conversation context with `/context` and `/compact`

---

[← Previous: Install and Modes](1-Install-and-Modes.md) | [Next: GitHub Integration and Workflows →](3-GitHub-Integration-and-Workflows.md)
