# Getting Started with GitHub Copilot for Azure

Unlock a more efficient workflow and boost your productivity with GitHub Copilot for Azure Preview. This quick-start guide takes you through everything you need to know, from preparing the prerequisites to installing the GitHub Copilot for Azure extension in Visual Studio Code. By the end, you’ll be equipped to craft your first prompt and fully leverage the Azure platform’s potential.


![GitHub Copilot for Azure](./images/intro.gif "GitHub Copilot for Azure")
 
 
</header>

- **Who is this for**: Developers, Operations (ITPRO), and AI Engineers.
- **What you'll learn**: Setup steps in getting started with GitHub Copilot for Azure.
- **What you'll build**: You’ll confidently setup your AI enabled workspace.
 
 
## Prerequisite reading:
- [What is GitHub Copilot for Azure Preview?](https://learn.microsoft.com/azure/developer/github-copilot-azure/introduction)
 
 
## 👉 Prerequisites

To complete the steps in this lab, make sure that you have:

1. An Azure account and access to an Azure subscription. For details on how to set them up, see the [pricing page for Azure accounts.](https://azure.microsoft.com/pricing/purchase-options/azure-account)

1. A GitHub account. Steps on setting one up can be found here: [Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
  
1. GitHub Copilot subscription. Details on how to enable GitHub Copilot can be found here: [Quickstart for GitHub Copilot](https://docs.github.com/en/copilot/quickstart)

1. Visual Studio Code. For details on how to download and install it, see [Setting up Visual Studio Code.](https://code.visualstudio.com/docs/setup/setup-overview)

1. The GitHub Copilot extension and the GitHub Copilot Chat extension. For instructions on how to install this extension, see [Set up GitHub Copilot in VS Code.](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
 
 
## 💪🏽 Exercise
 
 
### 🛠 Step 1: Authenticate to GitHub and login to GitHub Copilot chat to enable the Copilot for Azure Preview

**Right click the following Codespaces button to open your Codespace in a new tab**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)

1. Upon opening  VS Code, in the right hans side, click **"Sign in with a GitHub.com account"**.

    1. Visual Studio Code will pop up a message asking **"The extension 'GitHub Copilot Chat' wants to sign in using GitHub."** Click **Allow**.

    1. You will need to authorize Visual Studio Code to continue with the user signed in. Click the **Continue** button.

    1. And complete the authorization by clicking the **Authorize Visual-Studio-Code** button.

    1. A popup message will ask to open VS Code.  Click **Open**. you will be returned to VS Code, you will be authenticated to GitHub and will have access to **GitHub Copilot**.


1. In Visual Studio Code, select the **Extensions** icon.
   
1. Verify that you have the following Extensions installed.
    1. **Azure Tools**
    1. **GitHub Copilot**
    1. **GitHub Copilot Chat**
    1. **GitHub Copilot for Azure**
    1. **.NET Install**
    1. **Python**
   
1. If one is missing install it from the marketplace.

### ✍️ Step 2: Write your first prompt

1. Now that the extensions are installed, that you're properly authenticated, and that the extension is working correctly.

1. On the Activity Bar, select the **Chat** icon if the **Ask Copilot** pane is closed.

1. In the chat text area at the bottom of the chat pane, enter the following prompt:

```prompt
@azure Do I have any resources currently running?
```
> In the next section you will be asked to authorize applications and services multiple times.  This is for your protection and will only be done once.  We are authorizing **GitHub**, **VS Code** and **Azure** to trust the prompts with the credentials supplied.

1. You might get a message in the GitHub Copilot Chat pane that states "you need to sign in your Microsoftaccount to use GitHub Copilot for Azure (@Azure)".

    1. If you do, click the link in the **"Already have an account? Sign in"** line.
    1. Visual Studio Code will pop up a message asking **"The extension 'GitHub Copilot for Azure' wants to sign in using Microsoft."** Click **Allow**.
    1. login using the credentials in the existing session, or the credentials found in the Resource Tab of the lab instructions. The same credential as the Azure subscriptions.
    1. Close the tab.  Not the browser.
    1. Return to VS Code. Visual Studio Code will pop up a message asking **"The extension 'GitHub Copilot for Azure' wants to access the language models provided by GitHub Copilot Chat."** Click **Allow**.
    1. Visual Studio Code will pop up another message asking **"The extension 'GitHub Copilot for Azure' wants to sign in using GitHub."** Click **Allow** again.
        1. You will need to authorize Visual Studio Code to continue with the user signed in. Click the **Continue** button
        1. Complete the authorization by clicking the **Authorize Visual-Studio-Code** button.
        1. A popup message will ask to open VS Code.  Click **Open**. you will be returned to VS Code, you will be authenticated to GitHub and will have access to **GitHub Copilot**.

1. The Copilot for Azure extension will query the Azure Resource graph, provide you with the resource query and provide the answer.  Which at this point should be **You currently do not have any running resources across all your subscriptions.**

### Conclusion

Congratulations, through the exercise, you have setup VS Code to use GitHub Copilot for Azure and have inquired it to let you know of any resources running in your Azure subscription.
