# Get answers to your questions about Azure services and resources

If you're unfamiliar with Azure and how you can use it for your application, you can ask GitHub Copilot for Azure and Azure MCP to help you. Use this lab like a *Choose your own adventure* novel. Explore the many prompts below and try and craft your own prompts based on what you think you would like to learn about Azure.

## Best practices

Using copilots can increase developer productivity by answering questions, executing tasks, and generating code. However, remember these vital rules:

- Review all AI-generated responses. Validate their correctness, applicability, potential outcomes (such as costs and security) before taking action based on those responses.
- Never save application secrets or credentials in source code.
- Never submit application secrets or credentials in questions or in code when you ask questions.

When you're working with any tool that's based on large language models, use good prompt engineering techniques for the best results. The following tips come from the article [Write effective prompts for Microsoft Copilot in Azure](https://learn.microsoft.com/azure/copilot/write-effective-prompts), which provides advice for prompt engineering in the context of Azure.

- Be clear and specific
- Set expectations
- Add context about your scenario
- Break down your requests
- Customize your code
- Use Azure terminology
- Use the feedback loop

## Learn about Azure Services Using GitHub Copilot for Azure & Azure MCP

In this exercise, we will use GitHub Copilot for Azure and Azure MCP to learn about how to use Azure for your application. We will start with an open-ended question or request. Then add details like specific services and technologies for better results. Try the following example prompts.

## Learn about system architecture on Azure

1. "How can I create a highly available architecture in Azure?"
1. "Explain the Azure Well-Architected Framework."
1. "What types of app hosting solutions does Azure have?"
1. "Help me orchestrate and automate my data processing workflows on Azure."
1. "How can I integrate SignalR with Azure Application Gateway and Azure API Management?"
1. "How many Azure units do you recommend?"
1. "What are the benefits and applications of using Terraform with Azure?"

## Learn about AI on Azure

8. "I want to build an AI application using Azure. What services can I use?"

## Learn about web and application hosting on Azure

9. "Which Azure service is best for hosting a scalable web application?"
1. "Which Azure service should I use to create a website?"
1. "How can I use Azure to build a scalable web application?"
1. "For what scenarios is Azure Functions better than Azure Web Apps?"

## Learn about containers on Azure

- "What types of containerized applications does Azure support?"
- "What are the options for managing containers in Azure?"
- "When should I use Azure Kubernetes Service instead of Azure Container Apps?"
- "What's the difference between Azure Container Apps and AKS?"
- "Why would I choose Azure Container Apps over AKS?"

### Learn how to use Azure services for your app

|Service or technology|Learn prompt examples|
|---|---|
|Azure AI Search|<ul><li>"What is Azure AI Search and why should I use it?"</li><li>"How does pricing work for Azure AI Search?"</li><li>"How is Azure AI Search integrated with Azure OpenAI?"</li><li>"How is Azure AI Search integrated with Azure Machine Learning?"</li><li>"When should I use hybrid search or vector search versus semantic ranker in Azure AI Search?"</li><li>"Is Azure AI Search a vector database? How does Azure AI Search ensure the accuracy and relevance of vector search results?"</li><li>"What support do you have for high-scale multi-tenant applications in Azure AI Search?"</li><li>"What is the integrated vectorization feature in Azure AI Search? From which data sources can I extract data and use integrated vectorization?"</li><li>"What is AI enrichment in Azure AI Search? How does AI enrichment work? What are the benefits of using AI enrichment?"</li><li>"What is the semantic ranker in Azure AI Search? How is it different from vector search?"</li><li>"What are top recommended code samples or solution accelerators for Azure AI Search?"</li><li>"What are some real-world examples of businesses using Azure AI Search?"</li></ul>|
|Azure API Management|<ul><li>"What are the benefits and applications of Azure API Management?"</li></ul>|
|Azure App Service|<ul><li>"How do I deploy a web app in Azure?"</li><li>"How do I create an Azure App Service app and deploy code to a staging environment by using the CLI?"</li><li>"Create a script to deploy a web app that will run in Python on Azure."</li><li>"What database options does Azure have for web apps?"</li><li>"What serverless options does Azure have for web apps?"</li><li>"Create a guide for maximizing Azure App Service."</li></ul>|
|Azure Cache for Redis|<ul><li>"Demonstrate how to configure a Redis cache in Azure for high availability and disaster recovery."</li></ul>|
|Azure Container Apps|<ul><li>"What is the Azure Container Apps service?"</li><li>"Tell me the difference between a container app and a container app environment in Azure."</li></ul>|
|Azure Cosmos DB|<ul><li>"Why would I use Azure Cosmos DB instead of Azure SQL?"</li><li>"I want to use Azure Cosmos DB to store my data."</li><li>"Why would I use an Azure Cosmos DB account over a SQL database?"</li></ul>|
|Azure Data Factory|<ul><li>"How do I create data pipelines with Azure Data Factory?"</li></ul>|
|Azure Developer CLI (`azd`)|<ul><li>"Do you have example Azure deployment models? SaaS, PaaS, etc."</li><li>"What is the best Azure infrastructure for my application?"</li><li>"How do I set up my Azure environment?"</li><li>"What are Azure Resource Manager templates and how do I use them?"</li><li>"How do I manage Azure environments with the Azure Developer CLI?"</li><li>"What is the Azure Developer CLI?"</li><li>"What is the difference between Azure Bicep and ARM templates?"</li><li>"How do I make sure my Azure environments have the best security patterns?"</li><li>"How do I deploy to Azure using my CI/CD pipeline?"</li></ul>|
|Azure Functions|<ul><li>"How do I create a new Azure function?"</li><li>"What is the difference between Azure Functions and Azure Logic Apps?"</li><li>"Create a guide for integrating Azure Logic Apps with Azure Functions."</li><li>"I want to create an Azure function in Node.js."</li></ul>|
|Azure Key Vault|<ul><li>"Explain how and why I should use Azure Key Vaults."</li></ul>|
|Azure Kubernetes Service (AKS)|<ul><li>"How do I get the status of all nodes in my Azure AKS cluster?"</li><li>"What's the command to set a context for my Azure AKS cluster?"</li></ul>|
|Azure Machine Learning|<ul><li>"Generate a PowerShell script to create a new Azure Machine Learning workspace."</li><li>"What is the difference between Azure AI services and Azure Machine Learning?"</li></ul>|
|Azure Monitor|<ul><li>"Create a guide for using Azure Logic Apps to automate responses to Azure Monitor alerts."</li></ul>|
|Azure Virtual Network|<ul><li>"How do I balance inbound network traffic to my application in Azure?"</li></ul>|
|Azure OpenAI Service|<ul><li>"What services does Azure OpenAI provide?"</li><li>"Where is GPT-4o mini available in Azure OpenAI?"</li><li>"What are the prerequisites for integrating Azure OpenAI?"</li><li>"Create a guide for creating and using Azure OpenAI resources."</li><li>"What are the available types of Azure OpenAI models?"</li></ul>|
|Azure SDK|<ul><li>"Can I use Azure SDKs in the browser?"</li><li>"Does the C# Azure storage SDK support chunked blob uploads and downloads?"</li></ul>|
|Azure SignalR Service|<ul><li>"How do I host and scale SignalR on multiple Azure servers?"</li><li>"How do I do real-time communication in .NET using Azure?"</li><li>"How do I push real-time updates to clients using Azure SignalR?"</li><li>"How do I synchronize data across clients using Azure SignalR?"</li><li>"How do I stream data to clients using Azure SignalR?"</li><li>"How do I manage and scale WebSocket connections in Azure?"</li><li>"How do I host and scale Socket.IO on Azure?"</li><li>"What do I need to do to configure my SignalR code to work with Azure SignalR Service?"</li><li>"Evaluate my use of SignalR on Azure. Is it following the best security practices?"</li><li>"How do I stress test Azure SignalR?"</li><li>"How do I configure networking in Azure SignalR Service?"</li><li>"How do I configure an Azure Web PubSub event handler?"</li>|
|Azure SQL|<ul><li>"Create a Terraform configuration to deploy an Azure SQL database."</li><li>"Design a strategy for migrating on-premises SQL Server databases to Azure SQL Managed Instance."</li></ul>|
|Azure Static Web Apps|<ul><li>"Do Azure static web apps support static IP addresses?"</li></ul>|
|Azure Storage|<ul><li>"Why would I use Azure blob storage?"</li><li>"How do I pull data from an Azure storage blob in React?"</li><li>"Outline steps to secure Azure Blob Storage with private endpoints and Azure Private Link."</li><li>"Generate an Azure CLI script to create a new Azure storage account."</li><li>"Give me the code to create a new Azure storage account with a CLI."</li><li>"Can you help me choose the right Azure storage solution?"</li></ul>|
|Azure Web PubSub|<ul><li>"How do I authenticate with Azure Web PubSub?"</li><li>"What do I need to do to host my Socket.IO app on Azure?"</li><li>"How do I stress test Azure Web PubSub?"</li></ul>|