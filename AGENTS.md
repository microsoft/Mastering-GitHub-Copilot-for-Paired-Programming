# AGENTS.md

## Project Overview

This is **Mastering GitHub Copilot for Paired Programming**, an open-source educational repository maintained by Microsoft. It is a multi-module, 10-hour course that teaches developers how to use GitHub Copilot as an AI coding partner — from beginner to advanced topics including Agent Mode.

The repository is **documentation-centric**: most content is Markdown-based lesson guides. A small number of code samples exist within specific lessons.

## Repository Layout

```
├── Getting-Started-with-GitHub-Copilot/       # Beginner lesson
├── Using-GitHub-Copilot-with-JavaScript/       # Intermediate – JS / Node
├── Using-GitHub-Copilot-with-Python/           # Intermediate – Python / FastAPI
├── Using-GitHub-Copilot-with-CSharp/           # Intermediate – C# / .NET Minimal APIs
├── Using-GitHub-Copilot-CLI/                   # Intermediate – CLI usage
├── Using-GitHub-Copilot-Coding-Agent/          # Intermediate – Coding Agent workflow
├── Integrate-MCP-with-Copilot/                 # Intermediate – MCP integration
├── Creating-Mini-Game-with-GitHub-Copilot/     # Intermediate – Python console game (has app.py)
├── Using-Advanced-GitHub-Copilot-Features/     # Advanced – inline chat, slash commands, agents
├── Using-GitHub-Copilot-for-Azure-to-Deploy-to-Cloud/  # Advanced – Azure deployment
├── Challenging-GitHub-Copilot-with-SQL/        # Advanced – complex SQL
├── Upgrading-Legacy-Projects/                  # Advanced – Python 2 → 3 migration
├── Migrating-Languages/                        # Advanced – Python → Rust migration
├── GitHub-Copilot-for-Data-Scientists/         # Advanced – Jupyter / data science
├── archive/                                    # Archived older lesson content
├── images/                                     # Shared images for the root README
├── .devcontainer/                              # Dev container configuration
├── .github/workflows/                          # CI (CodeQL)
└── Root files: README.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md
```

Each lesson module follows a consistent structure:

- A `README.md` (sometimes `README.MD`) with the written lesson
- An `images/` subdirectory for screenshots and diagrams
- Optionally, code files or additional markdown guides

Most exercises reference external Codespaces template repos (e.g., `github/dotnet-codespaces`) rather than containing code directly.

## Dev Environment

The repository ships a **dev container** (`.devcontainer/devcontainer.json`) for use with GitHub Codespaces or VS Code Dev Containers:

- **Base image**: `mcr.microsoft.com/vscode/devcontainers/python:dev-3.13-bookworm`
- **Forwarded ports**: 5000, 8000
- **VS Code extensions installed automatically**:
  - `github.copilot`
  - `ms-python.python`, `ms-python.vscode-pylance`
  - `ms-toolsai.jupyter`
  - `dbaeumer.vscode-eslint`, `esbenp.prettier-vscode`
  - `streetsidesoftware.code-spell-checker`
  - `ms-vscode.azure-account`, `ms-azuretools.vscode-azure-github-copilot`

To get started:

1. Open the repo in GitHub Codespaces or a local dev container.
2. The container automatically installs Python 3.13 and the listed VS Code extensions.
3. No additional dependency installation is required at the root level.

## Content Conventions

When editing or adding lesson content, follow these conventions:

- **Lesson README**: Each lesson folder must have a `README.md` describing the lesson, challenge, and extra resources.
- **Images**: Place images inside the lesson's `images/` subdirectory. Use relative paths in Markdown.
- **Lesson table**: If adding a new lesson, update the lesson table in the root `README.md` under the appropriate difficulty level (Beginner, Intermediate, or Advanced).
- **Language**: Write in clear, instructional English. The audience ranges from beginners to experienced developers.
- **No hardcoded secrets**: Never commit API keys, tokens, or credentials.

## Code Style

This repo has minimal code. When code is present, follow these guidelines:

- **Python**: Follow PEP 8. The dev container includes `pylance` for type checking. Example: `Creating-Mini-Game-with-GitHub-Copilot/app.py`.
- **JavaScript**: ESLint and Prettier are available via the dev container extensions.
- **C#**: Follow standard .NET conventions. C# lessons reference the external `github/dotnet-codespaces` repo.
- **Markdown**: Use standard GitHub-Flavored Markdown. Keep lines readable. Use fenced code blocks with language identifiers.

## CI/CD

- **CodeQL Advanced** (`.github/workflows/codeql.yml`): Runs on pushes and PRs to `main`, plus a weekly schedule. Currently analyzes Python only.
- There is no build or test pipeline at the repository level — the repo is primarily documentation.

## Pull Request Guidelines

- A **Contributor License Agreement (CLA)** is required. A bot will prompt you on your first PR.
- Follow the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
- Title format: use a clear, descriptive title summarizing the change.
- Ensure spelling and grammar are correct — the `code-spell-checker` extension helps with this.
- Do not modify files unrelated to your change.
- If adding a new lesson, include the README, images, and update the root lesson table.

## Troubleshooting

- **Codespace won't start**: Ensure your GitHub account has Codespaces access and that the dev container image can be pulled.
- **Copilot not working**: Verify you have an active [GitHub Copilot subscription](https://gh.io/copilot).
- **Port conflicts**: The dev container forwards ports 5000 and 8000. Ensure they are not in use locally if running outside Codespaces.
