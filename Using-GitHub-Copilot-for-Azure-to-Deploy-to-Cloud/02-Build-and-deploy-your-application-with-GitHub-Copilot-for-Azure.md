# Build and deploy your application with GitHub Copilot for Azure and Azure MCP

This module is a continuation of Module 1 and provides a step-by-step guide on using GitHub Copilot for Azure and Azure MCP to create and deploy a new website in Azure.

It highlights an approach to seamlessly integrating the extensions and their tools into your development and deployment workflow.

- **Who is this for**: Developers, DevOps Engineers, and Cloud Architects.
- **What you'll learn**: How to use GitHub Copilot for Azure to scaffold and deploy a Flask application.
- **What you'll build**: A Python Flask website deployed to Azure using the Azure Developer CLI (`azd`).
- **Estimated time**: 30-45 minutes (excluding deployment wait time)

## Prerequisites

- Completion of [Module 1 - Getting Started with GitHub Copilot for Azure](./01-Getting-Started-with-GitHub-Copilot-for-Azure.md)
- Your Codespace from Module 1 should still be running
- Azure authentication completed in Module 1

## 📚 Prerequisite Reading

- [What is the Azure Developer CLI?](https://learn.microsoft.com/azure/developer/azure-developer-cli/overview)
- [Azure App Service overview](https://learn.microsoft.com/azure/app-service/overview)

---

## 💪🏽 Exercise: Create and Deploy a Website Using GitHub Copilot for Azure

### 🛠 Step 1: Set Up Your Project Directory

> **Note:** These instructions assume you're continuing in the same GitHub Codespace from Module 1. If your Codespace has stopped, restart it using the button below.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)

1. In Visual Studio Code (within your Codespace), open the integrated terminal by selecting **View** > **Terminal** or pressing `` Ctrl+` ``.

2. Create a new directory for your Flask project and navigate into it:

    ```bash
    mkdir -p ~/flask-azure-app && cd ~/flask-azure-app
    ```

3. Verify you're in the correct directory:

    ```bash
    pwd
    ```

    You should see output similar to: `/home/codespace/flask-azure-app`

4. Open this new folder in VS Code using the Explorer:
    1. In the **Activity Bar** (left side), select the **Explorer** icon (top icon, looks like two files).
    2. Click **Open Folder**.
    3. Navigate to `/home/codespace/flask-azure-app` and select it.
    4. VS Code will ask if you trust the authors of this folder—select **Yes, I trust the authors**.

    > **Tip:** Alternatively, you can use **File** > **Open Folder** from the menu bar.

---

### ✍️ Step 2: Start a Conversation with GitHub Copilot

1. Select the **Chat** icon in the **title bar** (top of the VS Code window, near the search field) to open the GitHub Copilot Chat pane.

2. Start a new chat session by selecting the plus icon (**+**) on the pane's title bar.

   ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat.png "Start a new chat session")

3. Ensure you're in **Agent** mode and the model is set to **Claude Sonnet 4** or **GPT-5**.

4. In the chat text box, enter the following prompt and press **Enter**:

    ```prompt
    Help me create a simple Flask website using Python and deploy it to Azure
    ```

    > **Important:** The exact wording of responses varies each time due to how large language models generate text. Your conversation may differ slightly from the examples shown.

5. After a moment, Copilot will suggest an approach—typically starting with an `azd` template or building the application from scratch. Both approaches are valid.

    **Remember:** GitHub Copilot understands natural language. If something isn't clear, just ask follow-up questions conversationally.

---

### 🔍 Step 3: Understand the Azure Developer CLI Commands

Before running any commands, it's best practice to understand what they do.

1. If Copilot suggests a command starting with `azd init`, ask about it first:

    ```prompt
    Before I execute azd init, what does it do?
    ```

    ![Screenshot showing explanation of azd init](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-6.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of what the initialization command does.")

2. Learn about the resources that will be created:

    ```prompt
    What resources are created with this template?
    ```

    ![Screenshot showing resources explanation](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-7.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of the resources created by the suggested template.")

3. Ask any clarifying questions about Azure services:

    ```prompt
    What is the purpose of a virtual network?
    ```

    ![Screenshot showing virtual network explanation](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-8.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of what a virtual network is.")

---

### 🚀 Step 4: Initialize and Deploy Your Application

1. **Run the `azd init` command** when you're ready. If the command appears in a code fence in the chat, hover over it to reveal the action menu and select **Insert into Terminal**, then run it.

    ![Screenshot showing insert into terminal option](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-4.png "Screenshot that shows a pop-up menu with an option to insert a code-fenced command into the Visual Studio Code terminal.")

    ![Screenshot showing command in terminal](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-5.png "Screenshot that shows the Visual Studio Code terminal after insertion of a code-fenced command.")

2. **Authenticate with Azure** (if not already authenticated from Module 1):

    ```bash
    azd auth login
    ```

    - A browser window will open for authentication.
    - Use the same credentials from Module 1.
    - Return to VS Code after successful authentication.

3. **Deploy your application** using the `azd up` command:

    ```bash
    azd up
    ```

4. The `azd up` command will prompt you for:
   - **Subscription**: Select your Azure subscription
   - **Location**: Choose a region (recommended: **Canada Central** or a region close to you)

    > **Need help choosing?** Ask Copilot:
    > ```prompt
    > azd up is asking me what location I want to deploy the website into. How should I respond?
    > ```

    ![Screenshot showing location guidance](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-9.png "Screenshot that shows a response from GitHub Copilot for Azure with an answer that describes what the Azure locations are and how to choose one.")

---

### ⏳ Step 5: Wait for Deployment (or Continue Learning)

Deployment typically takes **20-40 minutes** depending on the template and selected region.

While waiting, you have two options:

- **Option A**: Continue to [Module 3 - Get Answers to Your Questions about Azure Services and Resources](./03-Get-Answers-to-your-Questions-about-Azure-Services-and-Resources.md)
- **Option B**: Monitor the deployment progress in your terminal

---

### 🔧 Troubleshooting

If `azd up` encounters an error:

1. Copy the error message from the terminal.
2. Use the **paperclip icon** at the bottom left of the chat pane to attach the terminal output.
3. Ask Copilot for help:

    ```prompt
    I received this error during deployment. How can I resolve it?
    ```

> **Tip:** GitHub Copilot for Azure doesn't automatically see terminal output. Always attach or paste error messages for accurate troubleshooting assistance.

---

### ✅ Conclusion

Congratulations! 🎉 You've successfully used GitHub Copilot for Azure to:

- Create a new Flask application project
- Understand the Azure resources required for deployment  
- Deploy your application to Azure using the Azure Developer CLI

Your Flask website is now running in Azure! Once deployment completes, `azd up` will display the URL where your application is accessible.

---

## 📖 Additional Resources

- [Azure Developer CLI documentation](https://learn.microsoft.com/azure/developer/azure-developer-cli/)
- [Flask documentation](https://flask.palletsprojects.com/)
- [Azure App Service documentation](https://learn.microsoft.com/azure/app-service/)

---

## ➡️ Next Steps

Continue to [Module 3 - Get Answers to Your Questions about Azure Services and Resources](./03-Get-Answers-to-your-Questions-about-Azure-Services-and-Resources.md)