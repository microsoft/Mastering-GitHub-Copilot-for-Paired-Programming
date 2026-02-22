<header>

# Using the GitHub Copilot CLI with Python

Welcome to a hands-on, multi-module course that takes GitHub Copilot beyond the editor and directly into your terminal as a fully autonomous coding agent. The GitHub Copilot CLI is a standalone AI-powered tool — separate from the `gh` extension — that opens an interactive chat session in your terminal, understands your local codebase, and can plan and execute complex multi-step coding tasks on your behalf.

Prepare for a practical, end-to-end experience! You will install the `copilot` CLI, master its interactive and programmatic interfaces (including plan mode and auto model selection), control tool permissions, manage conversation context, integrate with GitHub.com, select models, configure custom agents, discover community extensions from [Awesome Copilot](https://github.com/github/awesome-copilot), and combine everything into a real-world Python development workflow.

</header>


- **Who this is for**: Python Developers, DevOps Engineers, Platform Engineers, Software Development Managers, Testers.
- **What you'll learn**: How to install and use the standalone GitHub Copilot CLI, leverage its interactive and plan modes, use Auto model selection, control tool approval, manage context, interact with GitHub.com, select AI models, configure custom agents, install community-contributed plugins and skills from [Awesome Copilot](https://github.com/github/awesome-copilot), and use `gh agent-task` for remote agent tasks.
- **What you'll build**: A real-world CLI-driven workflow for Python projects covering project analysis, debugging, refactoring, test generation, and agent-assisted automation using MCP integrations.
- **Prerequisites**: GitHub Copilot is available to use for free, sign up for [GitHub Copilot](https://gh.io/copilot). Basic familiarity with a terminal, Git, and Python is recommended.
- **Timing**: This module can be completed in under 90 minutes.

By the end of this module, you'll acquire the skills to be able to:

- Install, authenticate, and launch the standalone GitHub Copilot CLI.
- Use interactive mode and plan mode; let Auto model selection choose the optimal model.
- Control tool approval with `--allow-tool`, `--deny-tool`, and `--allow-all-tools`.
- Manage conversation context with `/compact`, `/context`, and auto-compaction.
- Interact with GitHub.com natively — list PRs, work on issues, and create pull requests from the terminal.
- Select and switch AI models using `/model`.
- Configure custom agents and use `gh agent-task` to kick off and monitor remote agent tasks.
- Leverage MCP servers to extend CLI capabilities for Python projects.
- Discover and install community-contributed plugins and skills from [Awesome Copilot](https://github.com/github/awesome-copilot).

## Prerequisite reading:
- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot/?WT.mc_id=academic-113596-abartolo)
- [Using GitHub Copilot with Python](https://learn.microsoft.com/en-us/training/modules/introduction-copilot-python/?WT.mc_id=academic-113596-abartolo)
- [About GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)
- [Installing GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-cli)

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)

2. Install the standalone **GitHub Copilot CLI** (see Section 1 — the old `gh copilot` extension has been replaced by this new tool)

3. Fork and then clone [this repository locally](https://github.com/MicrosoftDocs/mslearn-copilot-codespaces-python) for the following exercises. 

## 💪🏽 Exercise

This workshop uses a Python FastAPI sample project. Throughout the exercises you will use the GitHub Copilot CLI and Coding Agent to understand, improve, and extend this project — entirely from the terminal and through agent-driven automation.

> ### 👉 [Start here — Module 1: Install and Modes](1-Install-and-Modes.md)

The workshop is split across four modules. Work through them in order:

| Module | Sections | What you'll learn |
|---|---|---|
| [1 — Install and Modes](1-Install-and-Modes.md) | Sections 1–2 | Install the CLI, learn interactive and plan modes, Auto model selection |
| [2 — Tool Approval and Context](2-Tool-Approval-and-Context.md) | Section 3 | Tool approval, programmatic mode, context management |
| [3 — GitHub Integration and Workflows](3-GitHub-Integration-and-Workflows.md) | Sections 4–5 | GitHub.com integration, model selection, end-to-end Python workflow |
| [4 — Customization and Extensions](4-Customization-and-Extensions.md) | Section 6 | Custom instructions, agents, community extensions from Awesome Copilot, MCP servers, hooks |

---

### Useful Links and Further Learning

- [About GitHub Copilot CLI](https://docs.github.com/copilot/concepts/agents/about-copilot-cli)
- [Installing GitHub Copilot CLI](https://docs.github.com/copilot/how-tos/set-up/install-copilot-cli)
- [Using GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [Responsible use of GitHub Copilot CLI](https://docs.github.com/copilot/responsible-use/copilot-cli)
- [GitHub Copilot CLI changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)
- [Copilot CLI ACP server](https://docs.github.com/copilot/reference/acp-server)
- [Integrate MCP with GitHub Copilot — GitHub Skills](https://github.com/skills/integrate-mcp-with-copilot)
- [Awesome Copilot — Community plugins, skills, and agents](https://github.com/github/awesome-copilot)


## Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
