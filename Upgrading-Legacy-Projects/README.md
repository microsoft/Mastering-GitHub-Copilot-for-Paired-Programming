<h1 align="center">Upgrading a Python project with GitHub Copilot</h1>
<h5 align="center">Perform complex upgrades from legacy code to latest stable versions</h3>

<p align="center">
  <a href="#mega-prerequisites">Prerequisites</a> •
  <a href="#books-resources">Resources</a> •
  <a href="#learning-objectives">Learning Objectives</a>
</p>

- **Who is this for**: Technologists who want to apply AI pair-programming techniques with GitHub Copilot to tackle challenging legacy code upgrade scenarios.
- **What you'll learn**: Advanced Copilot prompting and interaction strategies specifically useful for upgrading and modernizing projects, with techniques that are also applicable to greenfield development.
- **What you'll build**: A fully modernized Python project originally written in Python 2.5, upgraded from legacy and deprecated constructs to the latest version of Python 3.

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
1. Open [this repository with Codespaces](https://codespaces.new/microsoft/github-copilot-upgrading)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/github-copilot-upgrading)

💡 You don’t need Python installed locally. Codespaces includes everything you’ll need.

## Learning Objectives

In this workshop, you will:

  - Use advanced GitHub Copilot interaction techniques to handle legacy projects.
  - Iterate, validate, and refine AI-generated solutions to upgrade code correctly.
  - Apply general prompting strategies to improve Copilot suggestions.
  - Build and apply a testing strategy to validate the upgraded project.

Estimated completion time: 60–90 minutes

## :mega: Prerequisites

You only need a public GitHub account. All dependencies and data are included in this repository.
Make sure you have access to [GitHub Copilot](https://github.com/github-copilot/signup) (via license, trial, or free version).

## Key Practices for Upgrading Legacy Projects

### 1. Define Clear Objectives and Requirements

*What needs to be achieved?*

Start by understanding the end goal clearly. What is the result you're after? For upgrading legacy projects, you must ensure a thorough testing strategy that can help you validate correctness and completion when making critical changes.

*What are the constraints?*

Identify limitations or exclusions. For example, large language models (LLMs) can have (or lack) enough context to provide the right suggestions. It is up to you, the driver, to make decisions that achieve your goal. Certain business logic might prevent you from adding other external libraries or functionality. For example, if you are upgrading a project that is used in a production environment, you might not be able to add new libraries or functionality that could break the existing code.

> [!TIP]
> Start broad, then progressively narrow scope. Be precise about what success looks like.

### 2. Break Down the Problem into Components

Decompose the problem into smaller, manageable pieces. For example, start with the core application components and then test a single API endpoint or library function. This makes it easier to understand and solve the problem step-by-step:

- Single Public, exposed functions, or API endpoints
- Tests, test setup and validation scripts
- Configuration and installation process

Breaking down complexity makes debugging and validation easier.

> [!TIP]
> Decomposition helps you focus on one small, solvable task at a time.

### 3. Create slices of work

A slice of work is a small, manageable piece of the overall problem. This is similar to breaking down the problem into components, but it focuses on the specific tasks that need to be completed. Think of this like a functional test that validates a specific feature or functionality. For example, if you're upgrading a legacy project, you might want to create a slice of work that focuses on upgrading a single library or function.
This allows you to focus on one small task at a time, and it makes it easier to test and validate the changes.

> [!TIP]
> When creating slices, think about functional testing so you can easily validate changes.

### 4. Iterate and Refine the Solution
Start simple, then refine. In complex problems, initial attempts are rarely perfect. Start by generating a basic solution and progressively build on it.


> [!TIP]
> With each iteration, run tests and compare outcomes against expectations.

### 5. Use Examples to Clarify Requirements
When creating prompts for AI models or explaining problems, provide examples. An example can illustrate your expectations, making the task clearer for anyone or anything (including tools like GitHub Copilot) involved in solving the problem.

For instance, with legacy code, you could explain what the inputs and expected outputs can be while including the logic to accomplish the task

> [!TIP]
> Example-driven problem-solving is especially effective for ambiguous tasks.

### 6. Identify Patterns and Reuse Solutions
Recognize common patterns in your problem and reuse solutions where applicable. An obvious example of this in legacy Python projects is the use of exception handling in Python 2.5 would create a `SyntaxError` in Python 3+.

Sometimes in legacy projects it is common to create functions that handle either case or even modules that can do imports depending on the Python version. This is a common pattern in legacy projects that can be reused in other projects.

> [!TIP]
> Recognizing patterns helps speed up future upgrades.

### 7. Use Constraints and Edge Cases for Robustness
Consider edge cases and exceptions. Complex problems rarely involve only 'ideal' inputs—outliers and unusual scenarios can break simple solutions. Make sure your prompt or implementation anticipates and handles these cases.

In legacy code, this might mean considering how the code behaves with unexpected inputs, which would guide you to write new tests or modify existing ones.

> [!TIP]
> Emphasize building a comprehensive test suite to validate changes.

### 8. Use Tools Effectively
Whether you’re using GitHub Copilot, your editor auto-completion, or another form of automation, leverage the tools at your disposal but make sure you're guiding them with the right context. Tools are great for speeding up the generation, but they still need well-structured inputs and validation from you.

For GitHub Copilot, ensure that your prompts are detailed, but concise. Tools often work best when given structured input that leaves little ambiguity.

> [!TIP]
> Guide your tools with context and always verify their output.


### 9. Test and Validate
Testing and validation are key to ensuring that your solution works as expected. In the case of legacy code, this is even more critical, as you want to ensure that the new code behaves similarly (or exactly the same) to the old code.

Testing ensures that both the expected and unexpected situations are handled correctly.

> [!TIP]
> Always include a validation step to catch mistakes early.

**Generalization for Other Use Cases:**
These principles apply to a wide range of scenarios:
- _Coding & algorithms:_ Define inputs, outputs, and edge cases, then iterate.
- _AI prompting:_ Break down tasks, provide context, and refine results.
- _Design & content:_ Define purpose, provide examples, refine based on feedback.

**Final Thoughts:**
Tackling complex generation tasks requires a balance of clarity, decomposition, iteration, and validation. Whether you're writing an SQL query or solving another challenge, applying these principles helps produce results that are more accurate, efficient, and reliable.

## :books: Resources

Although not required, some of the features this workshop covers are in these Microsoft Learn modules:

- [Code with GitHub Codespaces](https://learn.microsoft.com/training/modules/code-with-github-codespaces/)
- [Using advanced GitHub Copilot features](https://learn.microsoft.com/training/modules/advanced-github-copilot/)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
The use of third-party trademarks or logos is subject to their respective policies.
