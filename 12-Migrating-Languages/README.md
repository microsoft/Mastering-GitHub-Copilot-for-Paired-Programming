<h1 align="center">Migrating a Python API to Rust with GitHub Copilot</h1>
<h5 align="center">Perform a challenging migration to a completely different language</h3>

<p align="center">
  <a href="#mega-prerequisites">Prerequisites</a> •
  <a href="#books-resources">Resources</a> •
  <a href="#learning-objectives">Learning Objectives</a>
</p>

- **Who is this for**: Any tecnologist that is looking to apply AI pair-programming techniques with GitHub Copilot to perform challenging work like migrating or translating from one programming language to another.
- **What you'll learn**: You'll use advanced GitHub Copilot techniques that are specifically useful when translating projects in different programming languages.
- **What you'll build**: An HTTP API that uses Rust with full compatibility from the original HTTP API written in Python.

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
1. Open [this repository with Codespaces](https://codespaces.new/microsoft/github-copilot-migrating-languages)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/github-copilot-migrating-languages)

## Learning Objectives

In this workshop, you will:

  - Understand the Differences Between Python and Rust for Web Development
  Learn the key differences in syntax, libraries, and frameworks when transitioning from Python's FastAPI to Rust's actix-web.
  - Implement JSON Serialization and Deserialization in Rust
  Gain hands-on experience using the serde library to handle JSON data, ensuring compatibility with the original Python API.
  - Develop and Validate Incremental Endpoints in Rust
  Practice creating and testing individual endpoints iteratively, ensuring correctness and alignment with the original Python API.
  - Optimize Performance and Identify Bottlenecks in Rust
  Learn to analyze and address potential performance issues, such as redundant file serialization, while building a production-ready Rust application.


## :mega: Prerequisites

Before joining the workshop, there is only one prerequisite: you must have a public GitHub account. All resources, dependencies, and data are part of the repository itself. Make sure you have your GitHub Copilot license, trial, or the free version.


## Main takeaways

### 1. Define Clear Objectives and Requirements

*What needs to be achieved?*

Start by understanding the end goal clearly. What is the result you're after? For migrating a project from one programming language to another, you must ensure a thorough testing strategy that can help you validate correctness and completion when making critical changes.

*What are the constraints?*

Identify limitations or exclusions. For example, large language models (LLMs) can have (or lack) enough context to provide the right suggestions. It is up to you, the driver, to make decisions that achieve your goal. Certain business logic might prevent you from adding other external libraries or functionality. For example, if you are migrating a project that is used in a production environment, you might not be able to add new libraries or functionality that could break the existing code.

> [!TIP]
> Focus on being precise with the scope of the problem. If you're unsure, start broad and then progressively narrow down the details.

### 2. Break Down the Problem into Components

Decompose the migration process into smaller, manageable pieces. For example, start with the core application components and then test a single API endpoint or library function. This makes it easier to understand and solve the problem step-by-step:

- Identify and migrate single public, exposed functions, or API endpoints from Python to Rust
- Develop and run tests, set up test environments, and create validation scripts to ensure correctness
- Handle configuration and installation processes for the new Rust environment

Ensure you're applying each condition step-by-step. In programming, breaking down a complex function into smaller helper functions can make it easier to write, debug, and migrate.

> [!TIP]
> Decomposition is a great way to deal with complexity, as it allows you to focus on one small task at a time.

### 3. Leverage Domain-Specific Vocabulary and Context

Use the appropriate terminology for the migration process. Whether you're translating Python code to Rust, working with APIs, or designing algorithms, being familiar with the domain vocabulary helps you form more accurate instructions for tools like GitHub Copilot or while communicating with others.

For example, understanding terms like "borrow checker" in Rust or "decorators" in Python can help you better navigate the migration process and communicate effectively with others involved.

> [!TIP]
> The more precise the vocabulary and context you use, the easier it is for both humans and tools to understand and generate solutions.

### 4. Iterate and Refine the Solution

Start simple, then refine. In complex problems, initial attempts are rarely perfect. Start by generating a basic solution and progressively build on it.

In this workshop for migrating an application from Python to Rust, you might want to start with a single function or piece of functionality and then isolate it, while subsequently adding complexity. For example, begin by translating a simple Python function to Rust, then incrementally add more complex features and integrations.

> [!TIP]
> With every iteration, test and verify against expected outcomes to ensure the result is moving in the right direction.

### 5. Use Examples to Clarify Requirements

When creating prompts for AI models or explaining problems, provide examples. An example can illustrate your expectations, making the task clearer for anyone or anything (including tools like GitHub Copilot) involved in solving the problem.

For instance, with migration code, you could explain what the inputs and expected outputs can be while including the logic to accomplish the task.

> [!TIP]
> Example-driven problem-solving helps align understanding. It's especially useful for ambiguous tasks.
### 6. Identify Patterns and Reuse Solutions

Recognize common patterns in your migration process and reuse solutions where applicable. For example, when migrating from Python to Rust, you might notice recurring patterns such as handling data structures, managing memory, or implementing similar algorithms. Once you identify these patterns, you can reuse and adapt these building blocks for different parts of your project.

In code migration, identifying reusable functions or logic can save time and reduce errors. For instance, if you have a common way of handling API requests in Python, you can create a similar reusable function in Rust.

> [!TIP]
> Recognizing patterns is a hallmark of experience. As you encounter similar migration challenges repeatedly, you'll start to see similarities that can speed up your process and improve consistency.

### 7. Use Constraints and Edge Cases for Robustness

Think about edge cases and exceptions. Complex problems often involve handling not just the "ideal" data, but also the "edge" or "outlier" cases that might break a naive solution. Ensure that your prompt or solution accounts for these edge cases.

In migration code, this might mean considering how the code behaves with unexpected inputs which would guide you to write new tests or modify existing ones.

> [!TIP]
> Thinking through edge cases helps you build more resilient, generalized solutions.

### 8. Use Tools Effectively

Whether you’re using GitHub Copilot, your editor auto-completion, or another form of automation, leverage the tools at your disposal but make sure you're guiding them with the right context. Tools are great for speeding up the generation, but they still need well-structured inputs and validation from you.

For GitHub Copilot, ensure that your prompts are detailed, but concise. Tools often work best when given structured input that leaves little ambiguity.

> [!TIP]
> Be specific with your tools, but also check results, as tools might not always fully understand context unless properly guided.

### 9. Seek Feedback and Collaboration

When tackling a complex task, especially one that involves code or queries, collaboration and feedback are crucial. Don’t hesitate to ask peers or communities for insights or review.

For example, when rewriting complex functions or code blocks, having a second pair of eyes can help catch mistakes or suggest improvements. This is especially true in migration projects where the original intent might not be clear.

> [!TIP]
> Collaboration often brings new perspectives, reducing blind spots.
### 10. Test and Validate

Testing and validation are key to ensuring that your solution works as expected. In the case of migrating code to another programming language, this is even more critical, as you want to ensure that the new code behaves similarly (or exactly the same) as the old code.

Testing ensures that both the expected and unexpected situations are handled correctly, and that the migration has not introduced any new issues.

> [!TIP]
> Always have a validation step built into your process to catch mistakes early and ensure the migrated code meets all requirements.

Generalization for Other Use Cases:
For writing code or algorithms: The same concepts apply when generating functions, classes, or workflows. Clearly define input, expected output, edge cases, and iterate to refine.

For AI model prompts: When asking for something complex (like generating code, text, or designs), give clear objectives, break down the problem, provide context, and iterate.

For design or content generation: Define the purpose, break down design elements, and provide examples or inspiration, then refine based on feedback.

Final Thoughts:
Complex generation problems often involve a balance of clarity, decomposition, iteration, and validation. Whether it's a migrating from one programming language to another or any other task, keeping these concepts in mind will allow you to generate more accurate, efficient, and reliable results.

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
