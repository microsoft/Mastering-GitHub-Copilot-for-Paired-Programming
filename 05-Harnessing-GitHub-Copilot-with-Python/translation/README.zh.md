<header>

# 利用GitHub Copilot与Python携手

GitHub Copilot是世界上首个大规模的AI开发者工具，它能显著加快编写代码的速度，为你的工作提供类似自动补全的建议。在这个模块，我们将重点放在如何利用GitHub Copilot来提升你的Python编码效率。

作为一个开发者，你的目标是提升生产力并加快编码流程。GitHub Copilot就像你的AI伙伴程序员，根据上下文和代码模式提供建议。在本模块结束时，你不仅会知道如何在Codespaces中配置GitHub Copilot，还会知道如何有效地生成和实施代码建议。

准备好深入到实际场景中去了吗！你将会修改一份Python仓库，使用GitHub Copilot创建一个交互式HTML表单和API终点。此项目将会给你在开发一个服务于HTTP API的Python网络应用、生成用于识别目的的伪随机标记方面的宝贵经验。

</header>

- **这是为谁准备的**：开发者、DevOps工程师、软件开发经理、测试员。
- **你将学到什么**：学习利用GitHub Copilot创建代码并为你的工作添加注释。
- **你将制作什么**：将会有Copilot AI生成的代码和注释建议的Python文件。
- **先决条件**：要使用GitHub Copilot，你必须拥有一个活动的GitHub Copilot订阅。在此处为[Copilot](https://github.com/settings/copilot)注册30天免费版。
- **时间**：这门课程可以在一个小时内完成。

在本模块结束时，你将具备以下技能：

- 配置GitHub仓库在Codespaces，并安装GitHub Copilot扩展程序。
- 编写提示以从GitHub Copilot生成建议。
- 应用GitHub Copilot提升你的项目。

## 需要预先阅读：
- [GitHub Copilot的提示工程引论](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot//?WT.mc_id=academic-113596-abartolo)
- [使用GitHub Copilot与Python](https://learn.microsoft.com/en-us/training/modules/introduction-copilot-python/?WT.mc_id=academic-113596-abartolo)

## 要求

1. 开启你的[GitHub Copilot服务](https://github.com/github-copilot/signup)
1. 打开[Codespaces中的这个仓库](https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-python)

## 💪🏽 练习

[![在GitHub Codespaces中打开](https://github.com/codespaces/badge.svg)](https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-python)

API已经有了一个生成标记的终点。我们现在更新API，添加一个新的端点，它接收文本并返回一串标记。

### 🛠 第一步：添加一个Pydantic模型

打开`main.py`文件，添加一个注释，让GitHub Copilot为你生成一个`Pydantic`模型。生成的模型应该如下所示：

```python
class Text(BaseModel): 

text: str
```

### 🔎 第二步：生成一个新的端点

接下来，通过添加注释使用GitHub Copilot生成一个新的端点：

```python
# 创建一个FastAPI端点，它接受一个带有JSON实体的POST请求，该实体包含一个名为“text”的字段，并返回文本的校验和
```

### 🐍 第三步：添加必要的引用

生成的代码导致应用程序崩溃。崩溃是因为`base64`和`os`模块没有被导入。在文件的顶部添加以下行：

```python
import base64 
import os
```

最后，通过试用新的端点并访问`/docs`端点进行验证，确保该端点显示出来。

🚀 恭喜你，通过练习，你不仅使用了copilot生成代码，而且还以一种互动和有趣的方式完成了这个任务！你可以使用GitHub Copilot生成代码，写文档，测试你的应用等等。

## 法律通知

微软及任何贡献者在此授予你一个许可，你可以使用本仓库中的微软文档和其他内容，许可遵循[创作共用Attribution 4.0国际公共许可](https://creativecommons.org/licenses/by/4.0/legalcode)，
请参见[LICENSE](LICENSE)文件，并授予你使用仓库中任何代码的许可，许可遵循[MIT许可](https://opensource.org/licenses/MIT)，请参见
[LICENSE-CODE](LICENSE-CODE)文件。

微软、Windows、微软Azure以及/或其他微软产品和服务在文档中引用可能是在美国和/或其他国家的微软的商标或注册商标。
这个项目的许可并未授予你使用任何微软名称、logo或商标的权利。微软的一般商标准则可以在 http://go.microsoft.com/fwlink/?LinkID=254653 找到。

个人信息隐私可以在 https://privacy.microsoft.com/en-us/ 找到。

微软和任何贡献者保留所有其他权利，无论是由于他们各自的版权、专利、商标，还是由于暗示、禁止或其他方式所留下的。