# 📺 Copilot Edits with Azure API Management 👩‍💻

Making code changes is often an iterative process that consists of multiple steps before achieving the desired result. When working on large projects, developers often need to make consistent updates across multiple files. In this lesson we will explore how to use Copilot Edits in Visual Studio Code to more efficiently author Azure API Management policies.

## Introduction

The focus in this lesson is on Azure API Management policies and Copilot Edits. Copilot Edits is currently in preview and available to all GitHub Copilot users.

Select the link below to watch the full demo and check out Copilot Edits and APIM policies! 👇

🌐 [![Watch the video](https://img.youtube.com/vi/lpTso8pAPwc/0.jpg)](https://www.youtube.com/watch?v=lpTso8pAPwc)

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand the Basics of Azure API Management: Gain a fundamental understanding of what APIM and APIM policies are and its key components.
- Author Azure API Management Policies: Learn how to create and configure policies to manage API behaviour effectively.
- Leverage Copilot edits to accelerate the journey authoring Azure API Management policies.

## Prerequisites

TODO

## Copilot Edits

Copilot Edits is a feature in preview that allows developers to start an AI-powered code editing session where they can quickly iterate on code changes using natural language. It proposes code changes across multiple files in the workspace and applies these edits directly in the editor, allowing for quick review and iteration. Copilot Edits combines the conversational flow of Copilot Chat with fast feedback from Inline Chat, making it ideal for iterating on large changes across multiple files.

**Features and Benefits:**
- **AI-Powered Code Editing**: Quickly iterate on code changes using natural language, enhancing productivity.
- **Multi-File Edits**: Propose and apply changes across multiple files, streamlining the development process.
- **Conversational Flow**: Combine Copilot Chat with Inline Chat for a seamless editing experience.
- **Quick Review and Iteration**: Apply edits directly in the editor for fast feedback and refinement.

**Example Scenario:**
Imagine working on a large project with multiple files that need consistent updates. With Copilot Edits, you can describe the changes you want to make in natural language, and the AI will propose edits across all relevant files. For instance, if you need to update the API endpoints in several files, Copilot Edits will identify and modify all instances, allowing you to review and apply the changes quickly.

## Azure API Management (APIM)
Azure API Management (APIM) is a comprehensive solution for managing and securing APIs. It provides a set of tools and services that enable developers to create, publish, secure, and monitor APIs. APIM helps organisations to expose their services to external and internal consumers in a controlled and scalable manner.

### What Problems Does APIM Address?

- Security: APIM provides robust security features such as authentication, authorisation, and IP filtering to protect APIs from unauthorised access and threats.
- Scalability: It allows APIs to scale efficiently to handle varying loads and ensures high availability and performance.
- Monitoring and Analytics: APIM offers detailed analytics and monitoring capabilities to track API usage, performance, and health, enabling proactive management and optimisation.

### APIM Policies

Azure API Management (APIM) policies allow developers to change the behaviour of their APIs through configuration. These policies are a collection of statements, described in an XML document, that are run sequentially and can apply to API requests and responses. APIM policies can include C# statements and can become quite complex based on the use case. By using APIM policies, developers can manage and secure their APIs, enforce usage quotas, transform requests and responses, and much more.

**Features and Benefits:**
- **Behaviour Configuration**: Change API behaviour through configuration, providing flexibility.
- **Sequential Statements**: Run policies sequentially to apply to API requests and responses.
- **Complex Policies**: Include C# statements for complex use cases, enhancing functionality.
- **API Management**: Manage and secure APIs, enforce usage quotas, and transform requests and responses.

**Example Scenario:**
Consider a scenario where you need to enforce rate limiting on an API to prevent abuse. With APIM policies, you can configure a policy to limit the number of requests a user can make within a specific time frame. This helps protect your API from being overwhelmed by too many requests and ensures fair usage among all users.

## Exercise

Explore how to use Copilot Edits in Visual Studio Code to accelerate the journey with Azure API Management policies.

### -1- Getting started

- Create an APIM resource in Azure Portal.
- Open Visual Studio Code.
- Install the Azure API Management extension.
- Open the APIM resource within the IDE.

### -2- Starting the Demo

Begin the demo in the Azure Portal to find the deployed Echo-API and see all operations, such as a POST operation to create resources.

- Navigate to the Azure Portal.
- Locate the deployed Echo-API.
- Review the available operations.

### -3- Scenario

Create a container called "logs-jukasper" in an Azure Storage Account to securely upload blob files using an API call through Azure API Management.

- Access the Azure Storage Account.
- Create a container named "logs-jukasper".
- Prepare to upload blob files securely.

### -4- Using GitHub Copilot Edits

As a newcomer to Azure Policies, use GitHub Copilot to write the API policy and Copilot Edits to modify the policy in the current working file.

- Open the working file in Visual Studio Code.
- Use GitHub Copilot to write the API policy.
- Apply Copilot Edits to modify the policy.

### -5- Testing and Iterating

Test and experiment with Copilot Edits, as outcomes may vary based on the prompts provided.

- Test the changes made by Copilot.
- Accept or discard the suggested edits.
- Continue refining the policy using Copilot's input.

### -6- Modifying the Policy

Provide the URL to the endpoint, which in this case is the Azure Storage Account and container.

- Identify the endpoint URL.
- Modify the policy to include the endpoint URL.
- Ensure the policy meets the requirements.

### -7- Handling Errors

If the prompt does not provide the authentication via managed identity as requested, provide new instructions.

- Review the prompt and identify missing elements.
- Provide new instructions to Copilot.
- Accept the suggested changes if satisfactory.

### -8- Deploying and Testing

Save the changes and upload them to the APIM service in the cloud.

- Save the modified policy.
- Upload the changes to the APIM service.
- Check the output window for errors and insights.

### -9- Adding Header Parameters

Request Copilot to include a header parameter in the policy.

- Ask Copilot to add a header parameter.
- Accept the suggested changes.
- Upload the updated policy.

### -10- Testing the API Call

Use the VS Code extension to select the operation to test, which will open an HTTP file for testing the API call.

- Select the operation to test.
- Open the HTTP file for testing.
- Provide the APIM subscription key.
- Send the request and verify the response.

### -11- Verifying the Results

Check the storage account to confirm the creation of a blob file.

- Access the storage account.
- Verify the creation of the blob file.
- Modify the policy if the naming convention is not as expected.

### -12- Final Testing

Provide the subscription key and send the request again.

- Provide the subscription key.
- Send the request.
- Verify the successful response.
- Check the storage account for new files with relevant information about the API calls.

## Conclusion

This demo showcases a great way to leverage the power of AI with GitHub Copilot Edits to get started with writing Azure API Management policies.

