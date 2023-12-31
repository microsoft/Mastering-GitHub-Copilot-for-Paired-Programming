<header>

# Harnessing GitHub Copilot with Python

GitHub Copilot is the world's first at-scale AI developer tool that significantly accelerates code writing by providing autocomplete-style suggestions as you work. In this module, we will focus on harnessing the power of GitHub Copilot to enhance your Python coding efficiency.

As a developer, your goal is to boost productivity and speed up coding processes. GitHub Copilot acts as your AI pair programmer, offering suggestions based on context and code patterns. By the end of this module, you'll not only know how to configure GitHub Copilot in Codespaces but also how to generate and implement code suggestions effectively.

Get ready to dive into a real-world scenario! You'll be modifying a Python repository using GitHub Copilot to create an interactive HTML form and an API endpoint. This project will give you valuable experience in developing a Python web app that serves an HTTP API, generating pseudo-random tokens for identification purposes.

</header>


- **Who this is for**: Developers, DevOps Engineers, Software development managers, Testers.
- **What you'll learn**: Harnessing GitHub Copilot to create code and add comments to your work.
- **What you'll build**: Python files that will have code generated by Copilot AI for code and comment suggestions.
- **Prerequisites**: To use GitHub Copilot you must have an active GitHub Copilot subscription. Sign up for 30 days free [Copilot](https://github.com/settings/copilot).
- **Timing**: This course can be completed in under an hour.

By the end of this module, you'll aquire the skills to be able to:

- Configure a GitHub repository in Codespaces and install GitHub Copilot extension.
- Crafted prompts to generate suggestions from GitHub Copilot
- Applied GitHub Copilot to improve your projects.

## Prerequisite reading:
- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot//?WT.mc_id=academic-113596-abartolo)
- [Using GitHub Copilot with Python](https://learn.microsoft.com/en-us/training/modules/introduction-copilot-python/?WT.mc_id=academic-113596-abartolo)

## Requirements

1. Enable your [GitHub Copilot service](https://github.com/github-copilot/signup)
1. Open [this repository with Codespaces](https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-python)

## 💪🏽 Exercise

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-python)

The API already has a single endpoint to generate a token. Let's update the API by adding a new endpoint that accepts text and returns a list of tokens.

### 🛠 Step 1: Add a Pydantic model

Go to the `main.py` file, and add a comment so that GitHub Copilot can generate a `Pydantic` model for you. The generated model should look like this:

```python
class Text(BaseModel): 

text: str
```

### 🔎 Step 2: Generate a new endpoint

Next, generate a new endpoint with GitHub Copilot by adding the comment: 

```python
# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text 
```

### 🐍 Step 3: Add necessary imports

The generated code causes the application to crash. The crash happens because the `base64` and `os` modules aren't imported. Add the following lines to the top of the file:

```python
import base64 
import os
```

Finally, verify the new endpoint is working by trying it out by going to the `/docs` endpoint and confirming that the endpoint shows up.


🚀 Congratulations, through the exercise, you haven't only used copilot to generate code but also done it in an interactive and fun way! You can use GitHub Copilot to not only generate code, but write documentation, test your applications and more.


## Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
