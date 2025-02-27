<h1 align="center">Challenging SQL with GitHub Copilot</h1>
<h5 align="center">Push the limits of GitHub Copilot in complex workflows</h3>

<p align="center">
  <a href="#mega-prerequisites">Prerequisites</a> •
  <a href="#books-resources">Resources</a> •
  <a href="#learning-objectives">Learning Objectives</a>
</p>

- **Who is this for**: Any tecnologist that is looking to advance basic techniques when working with GitHub Copilot. Software Engineers, Data Engineers, Data Scientists, and anyone working with challenging codebases or code projects.
- **What you'll learn**: You'll use advanced GItHub Copilot techniques that are specifically useful when working with challenging problems. These techniques and patterns can be applied to difficult problems and when GitHub Copilot isn't providing the best answer.
- **What you'll build**: A database with highly specific data with advanced queries that are unit tested for validation and correctness.

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
1. Open [this repository with Codespaces](https://codespaces.new/microsoft/challenging-github-copilot)


[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/challenging-github-copilot)

## Learning Objectives

In this workshop, you will:

  - Use advanced GitHub Copilot interaction techniques to deal with complex problems regarding SQL queries.
  - Iterate, validate, and refine answers to get better and more accurate suggestions
  - Apply generic concpets that can improve suggestions and select from different strategies that can yield better results.
  - Get a clear understanding on poor prompting techniques, and how these can
    affect drastically the output from GitHub Copilot.

## :mega: Prerequisites

Before joining the workshop, there is only one prerequisite: you must have a public GitHub account. All resources, dependencies, and data are part of the repository itself. Make sure you have your GitHub Copilot license, trial, or the free version.


## Main takeaways

### 1. Define Clear Objectives and Requirements

*What needs to be achieved?*

Start by understanding the end goal clearly. What is the result you're after? In the case of SQL queries, is it about data aggregation, filtering, joining, etc.? Always ask: What do I need this query to accomplish?

*What are the constraints?*

Identify limitations or exclusions. For example, in the SQL query, you want to exclude specific batch types or data. In a broader sense, constraints might also include things like time restrictions, performance limits, or rules you need to follow.

> [!TIP]
> Focus on being precise with the scope of the problem. If you're unsure, start broad and then progressively narrow down the details.

### 2. Break Down the Problem into Components

Decompose the problem into smaller, manageable pieces. For example, breaking down a complex SQL query:
- Data filtering (e.g., today's data).
- Data exclusions (e.g., "off-us" or "offset").
- Aggregation (e.g., summing amounts).

Ensure you're applying each condition step-by-step. In programming, breaking down a complex function into smaller helper functions can make it easier to write and debug.

> [!TIP]
> Decomposition is a great way to deal with complexity, as it allows you to focus on one small task at a time.

### 3. Leverage Domain-Specific Vocabulary and Context

Use the appropriate terminology for the problem domain. Whether you're writing SQL queries, working with code, or designing an algorithm, being familiar with the domain vocabulary helps you form more accurate instructions for tools like Copilot or while communicating with others.


> [!TIP]
> The more precise the vocabulary and context you use, the easier it is for both humans and tools to understand and generate solutions.

### 4. Iterate and Refine the Solution
Start simple, then refine. In complex problems, initial attempts are rarely perfect. Start by generating a basic solution and progressively build on it.

In a SQL query, you might first write a query that selects all data for today, then add filters, exclusions, and aggregation in phases.

> [!TIP]
> With every iteration, test and verify against expected outcomes to ensure the result is moving in the right direction.

### 5. Use Examples to Clarify Requirements
When creating prompts for AI models or explaining problems, provide examples. An example can illustrate your expectations, making the task clearer for anyone or anything (including tools like GitHub Copilot) involved in solving the problem.

For instance, in SQL queries, you can use sample data and explain how the output should look.

> [!TIP]
> Example-driven problem-solving helps align understanding. It's especially useful for ambiguous tasks.

### 6. Identify Patterns and Reuse Solutions
Recognize common patterns in your problem and reuse solutions where applicable. For example, SQL queries often have common patterns (such as aggregation, filtering, or grouping), so once you identify them, you can reuse and modify these building blocks.

In code or other technical tasks, identifying reusable functions or logic can save time and reduce errors.

> [!TIP]
> Recognizing patterns is a hallmark of experience. As you encounter similar problems repeatedly, you'll start to see similarities that can speed up your process.

### 7. Use Constraints and Edge Cases for Robustness
Think about edge cases and exceptions. Complex problems often involve handling not just the "ideal" data, but also the "edge" or "outlier" cases that might break a naive solution. Ensure that your prompt or solution accounts for these edge cases.

In SQL, this could involve ensuring that empty datasets, null values, or unexpected data types don’t cause errors.

> [!TIP]
> Thinking through edge cases helps you build more resilient, generalized solutions.

### 8. Use Tools Effectively
Whether you’re using GitHub Copilot, a query builder, or another form of automation, leverage the tools at your disposal but make sure you're guiding them with the right context. Tools are great for speeding up the generation, but they still need well-structured inputs and validation from you.

For Copilot, ensure that your prompts are detailed, but concise. Tools often work best when given structured input that leaves little ambiguity.

> [!TIP]
> Be specific with your tools, but also check results, as tools might not always fully understand context unless properly guided.

### 9. Seek Feedback and Collaboration
When tackling a complex task, especially one that involves code or queries, collaboration and feedback are crucial. Don’t hesitate to ask peers or communities for insights or review.

For example, when creating a complex SQL query, someone else might see potential issues or better optimization strategies that you might have missed.

> [!TIP]
> Collaboration often brings new perspectives, reducing blind spots.

### 10. Test and Validate
Testing and validation are key to ensuring that your solution works as expected. In the case of SQL queries, you might test the query with various edge cases and compare it against expected outputs.

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
