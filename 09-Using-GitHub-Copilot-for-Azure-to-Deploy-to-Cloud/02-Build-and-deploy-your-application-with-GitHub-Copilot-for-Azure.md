# Build and deploy your application with GitHub Copilot for Azure

This module is a continuation of module 1 and provides a step-by-step guide on using GitHub Copilot for Azure Preview to create and deploy a new website in Azure.

It highlights an approach to seamlessly integrating GitHub Copilot for Azure into your development and deployment workflow.

## Prerequisites

Completion of [Module 1 - Getting Started to use GitHub Copilot for Azure](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/09-Using-GitHub-Copilot-for-Azure-to-Deploy-to-Cloud/01-Getting-Started-with-GitHub-Copilot-for-Azure.md)

## Create and deploy a website by using GitHub Copilot for Azure Preview

1. Create a new folder on your local computer where you can create a local clone of a GitHub repository.
    1. In VS Code click **File**, Then ""Open Folder"
    1. in the **Open Folder** dialogue box, click **New Folder**, Give the folder a name, select it, then click **Select Folder**

1. VS Code will ask you **Do you trust the Authors of the files in this folder?**
    1. click the **Yes, I trust the authors**

1. In Visual Studio Code, select **View** > **Terminal**. On the terminal pane, go to the new folder.

1. On the status Bar, select the **Chat** (GitHub) icon to open the chat pane.

1. Start a new chat session by selecting the plus icon (**+**) on the pane's title bar.

   ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat.png "Start a new chat session")

> If you closed the GitHub Copilot Chat after the last Module, click the GitHub icon in the status bar.  Bottom-right of your VS Code screen. And select **"GitHub Copilot Chat"** in the option menu.
>
> ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-2.png "Start a new chat session")

6. In the chat text box, type the following prompt. Then select **Send** (paper airplane icon) or select Enter on your keyboard.

   ```prompt
   @azure Could you help me create and deploy a simple Flask website by using Python?
   ```

    > **IMPORTANT**
The exact wording of the response is different each time GitHub Copilot for Azure answers, due to how large language models generate responses.

   After a moment, GitHub Copilot for Azure likely suggests an `azd` template to use.  Or in some cases will provide an answer like the following:

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-3.png "Screenshot that shows a response from GitHub Copilot for Azure with instructions for using a template to create a website in Azure.")

    Just Remember that the Large Language Model will understand what you tell it.  Therefore, just have the conversation with it.

1. If the answer provides a command that begins with `azd init` in a code fence, hover over the code fence to reveal a small pop-up action menu.

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-4.png "Screenshot that shows a pop-up menu with an option to insert a code-fenced command into the Visual Studio Code terminal.")

    Select **Insert into Terminal** to insert the command into the terminal.

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-5.png "Screenshot that shows the Visual Studio Code terminal after insertion of a code-fenced command.")

1. Before you run the `azd init` command, you might have questions about how it affects your local computer and your Azure subscription.

   Use the following prompt:

   ```prompt
   @azure Before I execute azd init, what does it do?
   ```

   You might see a response that resembles the following screenshot.

   ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-6.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of what the initialization command does.")

1. Use the following prompt to learn more about the `azd` template:

   ```prompt
   @azure What resources are created with this template?
   ```

   You might see a response that resembles the following screenshot.

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-7.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of the resources created by the suggested template.")

1. Ask questions about the services that the template uses with a prompt like:

   ```prompt
   @azure What is the purpose of a virtual network?
   ```

   You might see a response that resembles the following screenshot.

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-8.png "Screenshot that shows a response from GitHub Copilot for Azure with an explanation of what a virtual network is.")

1. When you're satisfied, run the `azd init` command in the terminal. Answer its prompts. If you're unsure what to answer for a prompt, ask GitHub Copilot for Azure for help.

1. Before you can continue, you must authenticate the `azd` tool by running in the terminal, the following command:

    ```cmd
    azd auth login
    ```

    1. This will open a browser that will require you to authenticate to Azure. select the same credentials as before.

1. Once the new project is initialized,and that you've authenticated to Azure, use **azd up** command to deploy the application to your subscription. In the terminal, run the command according to the instructions in the original prompt's reply.

    ```
    azd up
    ```

1. The `azd up` command asks for information about your subscription, where to deploy the resources, and more.

    If you're uncertain how to answer, you can ask GitHub Copilot for Azure for help. For example, you might ask:

    ```prompt
    @azure azd up is asking me what location I want to deploy the website into. How should I respond?
    ```

    You might see a response that resembles the following screenshot.

    ![Screenshot that shows the GitHub Copilot chat pane](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/images/mod2-CopilotChat-9.png "Screenshot that shows a response from GitHub Copilot for Azure with an answer that describes what the Azure locations are and how to choose one.")

5. Continue to answer prompts from `azd up`. Ask GitHub Copilot for Azure questions as needed.

    1. When asked the location select **Canada Central**.

    Depending on the `azd` template that you're deploying and the location that you selected, the template might take 20 to 40 minutes (or more) to deploy. But we can Move on to [Module 3](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/09-Using-GitHub-Copilot-for-Azure-to-Deploy-to-Cloud/03-Get-Answers-to-your-Questions-about-Azure-Services-and-Resources.md) while it completes

1. If `azd up` experiences an error, ask GitHub Copilot for Azure about the error and how you can resolve it.

    > **TIP**
    > For an easy way to attach the last terminal command results, use the paperclip icon at the bottom left of the chat pane. GitHub Copilot for Azure doesn't know the terminal command results unless they are copy/pasted or attached via the paperclip.
