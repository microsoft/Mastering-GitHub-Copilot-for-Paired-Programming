[← Previous: Instructions and Review](2-Instructions-and-Review.md) | [Next: Security and SDLC →](4-Security-and-SDLC.md)

# Advanced Customization

## 🎯 Learning Goals

- Create a custom agent profile for a specialized coding persona.
- Extend the agent with MCP servers for additional data sources and tools.
- Add hooks to execute custom shell commands during agent execution.
- Understand Copilot Memory (public preview).

---

## 🗒️ Part 1: Custom Agents

**Custom agents** are specialized versions of Copilot you define once using a Markdown file. Each profile encodes a specific persona, set of tools, and behavior. Custom agent profiles can also be defined at the [organization level](https://docs.github.com/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents) in a `.github-private` repository, making them available across all repositories in your organization.

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

---

## 🗒️ Part 2: Model Context Protocol (MCP) Servers

**MCP servers** give Copilot coding agent access to external data sources and tools — such as a project management system, internal documentation, or a database — that it wouldn't be able to reach otherwise. For organization-level or enterprise-level custom agents, the agent definition is managed centrally (not just in a repo under `.github/agents/`).

In those centrally managed agent profiles, you can define MCP servers directly in the YAML frontmatter of the agent profile. This allows administrators to centrally define which external tools the agent can access, eliminating the need for developers to configure MCP servers locally. This gives the agent access to those tools, allowing them to be policy-controlled and centralizing governance.

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

3. To add a third-party MCP server (for example: a Jira integration, an Azure DevOps integration, or other 3rd party service), follow the [MCP integration guide](https://docs.github.com/copilot/how-tos/use-copilot-agents/coding-agent/extend-coding-agent-with-mcp) and add the server configuration to `.github/mcp.json`.

---

## 🗒️ Part 3: Hooks — Lifecycle Automation

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

---

## 🗒️ Part 4: Copilot Memory (Public Preview)

**Copilot Memory** allows the coding agent to persist facts it learns about your repository across sessions — so it builds up knowledge over time without you having to repeat context.

To enable Copilot Memory:
1. Navigate to your [GitHub Copilot settings](https://github.com/settings/copilot).
2. Enable **Copilot Memory** (available for Pro and Pro+ plans).
3. After a session completes, Copilot will write memory entries such as: "This project uses better-sqlite3, not the default sqlite3 package."

---

In the above exercises we achieved the following:
- ✅ Built specialized custom agent profiles  
- ✅ Configured MCP server access
- ✅ Set up lifecycle hooks for post-run validation
- ✅ Understood Copilot Memory for persistent context

---

[← Previous: Instructions and Review](2-Instructions-and-Review.md) | [Next: Security and SDLC →](4-Security-and-SDLC.md)
