<h1 align="center">Upgrading a Python project with GitHub Copilot</h1>
<h5 align="center">Perform complex upgrades from legacy code to latest stable versions</h3>

<p align="center">
  <a href="#mega-prerequisites">Prerequisites</a> •
  <a href="#books-resources">Resources</a> •
  <a href="#learning-objectives">Learning Objectives</a>
</p>

- **Who is this for**: Any tecnologist that is looking to apply AI pair-programming techniques with GitHub Copilot to perform challenging upgrade scenarios for legacy code.
- **What you'll learn**: You'll use advanced GitHub Copilot techniques that are specifically useful when upgrading projects.  These techniques and patterns can be applied to upgrading and revamping projects as well as developing from scratch.
- **What you'll build**: A full revamped Python project that used Python 2.5 using legacy and deprecated constructs into the latest version of Python 3 available.

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
1. Open [this repository with Codespaces](https://codespaces.new/microsoft/github-copilot-upgrading)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/github-copilot-upgrading)

## Learning Objectives

In this workshop, you will:

  - Use advanced GitHub Copilot interaction techniques to deal with a legacy project
  - Iterate, validate, and refine answers to upgrade the legacy project and validate its correctness
  - Apply generic concpets that can improve suggestions and select from different strategies that can yield better results.
  - Build a thorough testing strategy to help you identify potential issues and
    validate the project in its final state after upgrading.

## :mega: Prerequisites

Before joining the workshop, there is only one prerequisite: you must have a public GitHub account. All resources, dependencies, and data are part of the repository itself. Make sure you have your GitHub Copilot license, trial, or the free version.

## Main takeaways

### 1. Define Clear Objectives and Requirements

*What needs to be achieved?*

Start by understanding the end goal clearly. What is the result you're after? For upgrading legacy projects, you must ensure a thorough testing strategy that can help you validate correctness and completion when making critical changes.

*What are the constraints?*

Identify limitations or exclusions. For example, large language models (LLMs) can have (or lack) enough context to provide the right suggestions. It is up to you, the driver, to make decisions that achieve your goal. Certain business logic might prevent you from adding other external libraries or functionality. For example, if you are upgrading a project that is used in a production environment, you might not be able to add new libraries or functionality that could break the existing code.

> [!TIP]
> Focus on being precise with the scope of the problem. If you're unsure, start broad and then progressively narrow down the details.

### 2. Break Down the Problem into Components

Decompose the problem into smaller, manageable pieces. For exampple, start with the core application components and then test a single API endpoint or library function. This makes it easier to understand and solve the problem step-by-step:

- Single Public, exposed functions, or API endpoints
- Tests, test setup and validation scripts
- Configuration and installation process

Ensure you're applying each condition step-by-step. In programming, breaking down a complex function into smaller helper functions can make it easier to write and debug.

> [!TIP]
> Decomposition is a great way to deal with complexity, as it allows you to focus on one small task at a time.

### 3. Create slices of work

A slice of work is a small, manageable piece of the overall problem. This is similar to breaking down the problem into components, but it focuses on the specific tasks that need to be completed. Think of this like a functional test that validates a specific feature or functionality. For example, if you're upgrading a legacy project, you might want to create a slice of work that focuses on upgrading a single library or function.
This allows you to focus on one small task at a time, and it makes it easier to test and validate the changes.

> [!TIP]
> When creating slices of work, thing about the functional testing so that you have an easy way to test the changes. This can be as simple as creating a test script that validates the changes or creating a test suite that runs all the tests in the project.

### 4. Iterate and Refine the Solution
Start simple, then refine. In complex problems, initial attempts are rarely perfect. Start by generating a basic solution and progressively build on it.


> [!TIP]
> With every iteration, test and verify against expected outcomes to ensure the result is moving in the right direction.

### 5. Use Examples to Clarify Requirements
When creating prompts for AI models or explaining problems, provide examples. An example can illustrate your expectations, making the task clearer for anyone or anything (including tools like GitHub Copilot) involved in solving the problem.

For instance, with legacy code, you could explain what the inputs and expected outputs can be while including the logic to accomplish the task

> [!TIP]
> Example-driven problem-solving helps align understanding. It's especially useful for ambiguous tasks.

### 6. Identify Patterns and Reuse Solutions
Recognize common patterns in your problem and reuse solutions where applicable. An obvious example of this in legacy Python projects is the use of exception handling in Python 2.5 would create a `SyntaxError` in Python 3+.

Sometimes in legacy projects it is common to create functions that handle either case, or even modules that can do imports depending on the Python version. This is a common pattern in legacy projects that can be reused in other projects.

> [!TIP]
> Recognizing patterns is a hallmark of experience. As you encounter similar problems repeatedly, you'll start to see similarities that can speed up your process.

### 7. Use Constraints and Edge Cases for Robustness
Think about edge cases and exceptions. Complex problems often involve handling not just the "ideal" data, but also the "edge" or "outlier" cases that might break a naive solution. Ensure that your prompt or solution accounts for these edge cases.

In legacy code, this might mean considering how the code behaves with unexpected inputs which would guide you to write new tests or modify existing ones.

> [!TIP]
> Thinking through edge cases helps you build more resilient, generalized solutions. Always put an added emphasis in testing and creating a robust test suite to validate your changes.

### 8. Use Tools Effectively
Whether you’re using GitHub Copilot, your editor auto-completion, or another form of automation, leverage the tools at your disposal but make sure you're guiding them with the right context. Tools are great for speeding up the generation, but they still need well-structured inputs and validation from you.

For GitHub Copilot, ensure that your prompts are detailed, but concise. Tools often work best when given structured input that leaves little ambiguity.

> [!TIP]
> Be specific with your tools, but also check results, as tools might not always fully understand context unless properly guided.


### 9. Test and Validate
Testing and validation are key to ensuring that your solution works as expected. In the case of legacy code, this is even more critical, as you want to ensure that the new code behaves similarly (or exactly the same) to the old code.

Testing ensures that both the expected and unexpected situations are handled correctly.

> [!TIP]
> Always have a validation step built into your process to catch mistakes early.

Generalization for Other Use Cases:
For writing code or algorithms: The same concepts apply when generating functions, classes, or workflows. Clearly define input, expected output, edge cases, and iterate to refine.

For AI model prompts: When asking for something complex (like generating code, text, or designs), give clear objectives, break down the problem, provide context, and iterate.

For design or content generation: Define the purpose, break down design elements, and provide examples or inspiration, then refine based on feedback.

Final Thoughts:
Complex generation problems often involve a balance of clarity, decomposition, iteration, and validation. Whether it's a SQL query or any other task, keeping these concepts in mind will allow you to generate more accurate, efficient, and reliable results.



## :books: Resources

Although not required, some of the features this workshop covers are in these Microsoft Learning modules:

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
Any use of third-party trademarks or logos are subject to those third-party's policies.
