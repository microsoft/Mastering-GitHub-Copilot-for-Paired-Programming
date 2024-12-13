# Get answers to your questions about Azure services and resources

If you're unfamiliar with Azure and how you can use it for your application, you can ask GitHub Copilot for Azure Preview to help you. Use this lab like a *Choose your own adventure* novel. Explore the many prompts below and try and craft your own prompts based on what you think you would need the @azure extension to do for you.

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

## Learn about Azure Services Using GitHub Copilot for Azure

In this exercise, we will use GitHub Copilot for Azure Preview to learn about how to use Azure for your application, We will start with open-ended question or request. Then, add details like specific services and technologies for better results. Try the following example prompts.

## Learn about system architecture on Azure

1. "@azure How can I create a highly available architecture in Azure?"
1. "@azure Explain the Azure Well-Architected Framework."
1. "@azure What types of app hosting solutions does Azure have?"
1. "@azure Help me orchestrate and automate my data processing workflows."
1. "@azure How can I integrate SignalR with Azure Application Gateway and Azure API Management?"
1. "@azure How many units do you recommend?"
1. "@azure What are the benefits and applications of using Terraform?"

## Learn about AI on Azure

8. "@azure I want to build an AI application. What services can I use?"

## Learn about web and application hosting on Azure

9. "@azure Which Azure service is best for hosting a scalable web application?"
1. "@azure Which service should I use to create a website?"
1. "@azure How can I use Azure to build a scalable web application?"
1. "@azure For what scenarios is Azure Functions better than Web Apps?"

## Learn about containers on Azure

- "@azure What types of containerized applications does Azure support?"
- "@azure What are the options for managing containers in Azure?"
- "@azure When should I use Azure Kubernetes Service instead of Azure Container Apps?"
- "@azure What's the difference between Azure Container Apps and AKS?"
- "@azure Why would I choose Azure Container Apps over AKS?"

### Learn how to use Azure services for your app

|Service or technology|Learn prompt examples|
|---|---|
|Azure AI Search|<ul><li>"@azure What is Azure AI Search and why should I use it?"</li><li>"@azure How does pricing work for Azure AI Search?"</li><li>"@azure How is Azure AI Search integrated with Azure OpenAI?"</li><li>"@azure How is Azure AI Search integrated with Azure Machine Learning?"</li><li>"@azure When should I use hybrid search or vector search versus semantic ranker in Azure AI Search?"</li><li>"@azure Is Azure AI Search a vector database? How does Azure AI Search ensure the accuracy and relevance of vector search results?"</li><li>"@azure What support do you have for high-scale multi-tenant applications in Azure AI Search?"</li><li>"@azure What is the integrated vectorization feature in Azure AI Search? From which data sources can I extract data and use integrated vectorization?"</li><li>"@azure What is AI enrichment in Azure AI Search? How does AI enrichment work? What are the benefits of using AI enrichment?"</li><li>"@azure What is the semantic ranker in Azure AI Search? How is it different from vector search?"</li><li>"@azure What are top recommended code samples or solution accelerators for Azure AI Search?"</li><li>"@azure What are some real-world examples of businesses using Azure AI Search?"</li></ul>|
|Azure API Management|<ul><li>"@azure What are the benefits and applications of Azure API Management?"</li></ul>|
|Azure App Service|<ul><li>"@azure How do I deploy a web app in Azure?"</li><li>"@azure How do I create an App Service app and deploy code to a staging environment by using the CLI?"</li><li>"@azure Create a script to deploy a web app that will run in Python."</li><li>"@azure What database options does Azure have for web apps?"</li><li>"@azure What serverless options does Azure have for web apps?"</li><li>"@azure Create a guide for maximizing Azure App Service."</li></ul>|
|Azure Cache for Redis|<ul><li>"@azure Demonstrate how to configure a Redis cache in Azure for high availability and disaster recovery."</li></ul>|
|Azure Container Apps|<ul><li>"@azure What is the Azure Container Apps service?"</li><li>"@azure Tell me the difference between a container app and a container app environment."</li></ul>|
|Azure Cosmos DB|<ul><li>"@azure Why would I use Azure Cosmos DB instead of Azure SQL?"</li><li>"@azure I want to use Azure Cosmos DB to store my data."</li><li>"@azure Why would I use an Azure Cosmos DB account over a SQL database?"</li></ul>|
|Azure Data Factory|<ul><li>"@azure How do I create data pipelines with Azure Data Factory?"</li></ul>|
|Azure Developer CLI (`azd`)|<ul><li>"@azure Do you have example deployment models for Azure? SaaS, PaaS, etc."</li><li>"@azure What is the best infrastructure for my application?"</li><li>"@azure How do I set up my Azure environment?"</li><li>"@azure What are Azure Resource Manager templates and how do I use them?"</li><li>"@azure How do I manage environments with the Azure Developer CLI?"</li><li>"@azure What is the Azure Developer CLI?"</li><li>"@azure What is the difference between Bicep and ARM templates?"</li><li>"@azure How do I make sure my environments have the best security patterns?"</li><li>"@azure How do I deploy by using my CI/CD pipeline?"</li></ul>|
|Azure Functions|<ul><li>"@azure How do I create a new Azure function?"</li><li>"@azure What is the difference between Azure Functions and Azure Logic Apps?"</li><li>"@azure Create a guide for integrating Azure Logic Apps with Azure Functions."</li><li>"@azure I want to create an Azure function in Node.js."</li></ul>|
|Azure Key Vault|<ul><li>"@azure Explain how and why I should use Azure key vaults."</li></ul>|
|Azure Kubernetes Service (AKS)|<ul><li>"@azure How do I get the status of all nodes in my AKS cluster?"</li><li>"@azure What's the command to set a context for my AKS cluster?"</li></ul>|
|Azure Machine Learning|<ul><li>"@azure Generate a PowerShell script to create a new Azure Machine Learning workspace."</li><li>"@azure What is the difference between Azure AI services and Azure Machine Learning?"</li></ul>|
|Azure Monitor|<ul><li>"@azure Create a guide for using Azure Logic Apps to automate responses to Azure Monitor alerts."</li></ul>|
|Azure Virtual Network|<ul><li>"@azure How do I balance inbound network traffic to my application?"</li></ul>|
|Azure OpenAI Service|<ul><li>"@azure What services does Azure OpenAI provide?"</li><li>"@azure Where is GPT-4o mini available?"</li><li>"@azure What are the prerequisites for integrating Azure OpenAI?"</li><li>"@azure Create a guide for creating and using Azure OpenAI resources."</li><li>"@azure What are the available types of Azure OpenAI models?"</li></ul>|
|Azure SDK|<ul><li>"@azure Can I use Azure SDKs in the browser?"</li><li>"@azure Does the C# storage SDK support chunked blob uploads and downloads?"</li></ul>|
|Azure SignalR Service|<ul><li>"@azure How do I host and scale SignalR on multiple servers?"</li><li>"@azure How do I do real-time communication in .NET?"</li><li>"@azure How do I push real-time updates to clients?"</li><li>"@azure How do I synchronize data across clients?"</li><li>"@azure How do I stream data to clients?"</li><li>"@azure How do I manage and scale WebSocket connections?"</li><li>"@azure How do I host and scale Socket.IO?"</li><li>"@azure What do I need to do to configure my SignalR code to work with Azure SignalR Service?"</li><li>"@azure Evaluate my use of SignalR. Is it following the best security practices?"</li><li>"@azure How do I stress test SignalR?"</li><li>"@azure How do I configure networking in Azure SignalR Service?"</li><li>"@azure How do I configure an Azure Web PubSub event handler?"</li>|
|Azure SQL|<ul><li>"@azure Create a Terraform configuration to deploy an Azure SQL database."</li><li>"@azure Design a strategy for migrating on-premises SQL Server databases to Azure SQL Managed Instance."</li></ul>|
|Azure Static Web Apps|<ul><li>"@azure Do static web apps support static IP addresses?"</li></ul>|
|Azure Storage|<ul><li>"@azure Why would I use a blob storage?"</li><li>"@azure How do I pull data from a storage blob in React?"</li><li>"@azure Outline steps to secure Azure Blob Storage with private endpoints and Azure Private Link."</li><li>"@azure Generate an Azure CLI script to create a new storage account."</li><li>"@azure Give me the code to create a new storage account with a CLI."</li><li>"@azure Can you help me choose the right Azure storage solution?"</li></ul>|
|Azure Web PubSub|<ul><li>"@azure How do I authenticate with Web PubSub?"</li><li>"@azure What do I need to do to host my Socket.IO app on Azure?"</li><li>"@azure How do I stress test Web PubSub?"</li></ul>|
