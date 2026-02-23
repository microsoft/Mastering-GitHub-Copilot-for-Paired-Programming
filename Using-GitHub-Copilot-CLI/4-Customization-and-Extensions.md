# Module 4: Customization and Extensions

[← Previous: GitHub Integration and Workflows](3-GitHub-Integration-and-Workflows.md) | [Back to overview](README.md)

---

### 🗒️ Section 6: Context Optimzation with Copilot: Custom Agents, Custom Instructions, and MCP Integrations

🎯 **Learning Goals**
- Understand custom agents and how to configure them for specialised tasks
- Create custom instructions files for Python projects
- Discover and install community-contributed plugins and skills from Awesome Copilot
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

Custom agents are specialized versions of Copilot configured for specific tasks or roles — for example, a data science agent that follows your team's pandas conventions, or a security agent that checks for common vulnerabilities.

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

#### Community Extensions with Awesome Copilot

So far you have created custom instructions and agents from scratch. The [Awesome Copilot](https://github.com/github/awesome-copilot) repository is a community-curated collection of ready-made agents, prompts, instructions, skills, and plugins that you can install directly into your workflow — saving you the effort of writing everything yourself.

The Awesome Copilot plugin system lets you browse and install curated bundles of related resources. Each plugin groups together agents, slash commands, and skills organised around a specific theme or workflow.

5. Add the Awesome Copilot plugin marketplace to your CLI:

   ```bash
   copilot plugin marketplace add github/awesome-copilot
   ```

6. Install the `awesome-copilot` plugin, which provides meta-commands for discovering and installing other community resources:

   ```bash
   copilot plugin install awesome-copilot@awesome-copilot
   ```

7. Launch a session and use the plugin's slash command to find skills relevant to your Python project:

   ```bash
   copilot
   ```

   ```
   /awesome-copilot:suggest-awesome-github-copilot-skills
   ```

   The plugin analyses your repository context and suggests matching skills from the community collection. You can also search for instructions and agents:

   ```
   /awesome-copilot:suggest-awesome-github-copilot-instructions
   ```

   ```
   /awesome-copilot:suggest-awesome-github-copilot-agents
   ```

8. Browse the full collection at [github.com/github/awesome-copilot](https://github.com/github/awesome-copilot) to explore available plugins, skills, and instructions. Notable resources for Python projects include plugins for Python MCP development, testing automation, and security best practices.

#### Copilot Memory

Copilot Memory allows the CLI to build a persistent understanding of your repository across sessions. It stores "memories" — coding conventions, patterns, and preferences deduced from your work — so you don't need to re-explain context in every new session.

9. After completing a significant task in a session, ask Copilot to summarise what it learned:

   ```
   /memory
   ```

   Review the stored memories. You can add, edit, or delete entries to correct any misunderstandings.

10. Start a new session and observe that Copilot already knows project-specific context — for example, that you prefer pytest over unittest or that you use Pydantic v2 syntax — without you having to repeat it.

#### Adding MCP Servers

The CLI ships with the GitHub MCP server pre-configured and authenticated. You can add additional MCP servers (for databases, monitoring tools, cloud providers, etc.) via a config file.

11. Open or create `~/.copilot/mcp-config.json` (user-level, applies to all projects) or `.github/mcp.json` (repository-level):

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

12. List configured MCP servers from within an active session:

   ```
   /mcp
   ```

   Select a server from the list to see which tools it exposes. You can then use those tools in natural language:

   ```
   Use the postgres MCP server to show me the schema of the users table.
   ```

13. When pre-approving MCP server tools at launch, use the server name as the `--allow-tool` argument:

   ```bash
   copilot --allow-tool 'postgres'
   ```

   To allow only a specific tool from the server:

   ```bash
   copilot --allow-tool 'postgres(query)' --deny-tool 'postgres(execute)'
   ```

#### Hooks

Hooks let you execute custom shell commands at key points during agent execution — for example, running a linter after every file write, or logging actions for an audit trail.

14. Create a hook file at `.github/hooks/post-write.sh`:

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
- ✅ Discovered and installed community plugins and skills from Awesome Copilot
- ✅ Used Copilot Memory for persistent cross-session context
- ✅ Added and queried additional MCP servers
- ✅ Configured hooks to automate linting after file writes

---

[← Previous: GitHub Integration and Workflows](3-GitHub-Integration-and-Workflows.md) | [Back to overview](README.md)
