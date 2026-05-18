# AGENTS.md

## Project overview

This repository is a lesson-based training course for **Mastering GitHub Copilot for Paired Programming**.  
Most content is Markdown documentation and images organized by module folder.

## Repository layout

- Root-level docs and policy files: `README.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`
- Lesson modules: top-level folders such as `Getting-Started-with-GitHub-Copilot`, `Using-GitHub-Copilot-with-Python`, etc.
- Each lesson generally contains:
  - `README.md` (lesson instructions)
  - `images/` (screenshots and assets)
- CI workflows: `.github/workflows/`

## Setup commands

This repo has no single root package manager project.

- Verify repository state:
  - `git status --short`
- Inspect lesson folders:
  - `find . -maxdepth 2 -name README.md | sort`
- Search text across lessons:
  - `grep -RIn "search-term" .`

## Development workflow

1. Read the target lesson `README.md` before editing.
2. Keep edits scoped to the requested module/files.
3. Prefer small, reviewable commits.
4. Keep image references relative (for example, `./images/example.png`).
5. If a module introduces its own runnable sample code, follow commands documented in that module’s README.

## Testing instructions

There is currently no repository-wide automated lint/test/build command at the root.

Before submitting:

- Check Markdown and links manually in changed files.
- Validate changed file paths and references:
  - `git diff --name-only`
  - `git diff --check`
- If you modify runnable sample code inside a module, run that module’s documented tests/build commands before submitting.

## Code style guidelines

- Follow existing Markdown style in neighboring files.
- Use clear section headings and concise instructional language.
- Preserve existing casing for file names (`README.md` or `README.MD`) as already used in each module.
- Avoid unnecessary reformatting of unrelated content.

## Build and deployment

- No root build artifact is produced by this repository.
- GitHub Actions currently includes CodeQL scanning (`.github/workflows/codeql.yml`).
- Treat this repository as documentation/course content unless a module explicitly defines its own app build workflow.

## Pull request guidelines

- Keep PRs focused on one change/theme.
- Run applicable checks for files you touched (module-specific if relevant).
- Follow `CONTRIBUTING.md` requirements (including CLA process).

## Security considerations

- Do not commit credentials, tokens, or secrets.
- Follow `SECURITY.md` for vulnerability reporting (MSRC process).
- Do not report security issues in public GitHub issues.
