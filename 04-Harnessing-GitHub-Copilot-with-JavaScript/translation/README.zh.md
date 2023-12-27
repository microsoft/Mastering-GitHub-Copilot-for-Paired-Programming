<header>

# 运用 JavaScript 轻松掌握 GitHub Copilot 

在这个模块中，我们将继续深入探索作为人工智能开发者工具的 GitHub Copilot，这个工具旨在提升您的编程体验。想象一下，您可以以更快的速度和更少的精力写代码——GitHub Copilot 将这个愿景变为现实，它可以根据您的注释和代码的上下文无缝生成建议。

作为一名寻求提高效率的开发者，您将开始一段旅程，掌握 GitHub Copilot 的各项功能，重点关注其在 JavaScript 应用中的运用。在模块结束时，您不仅会在 Visual Studio Code 中启用 GitHub Copilot 扩展，还会变得擅长构建能产生有价值建议的提示。在使用 GitHub Copilot 提升 JavaScript 项目时，提升您的编程技能，亲身体验这种人工智能配合程序员提供自动填充式建议，改变您的开发工作流程的方式。

通过掌握 GitHub Copilot，您不仅会在 Codespaces 中配置仓库，还会有效地利用这个人工智能工具来提升您的编程项目。准备在这次动态的学习之旅中革新您的编程体验，提高您的效率！

</header>

- **适合人群**：开发人员、DevOps 工程师、软件开发经理、测试员。
- **您将学会**：运用 GitHub Copilot 创建代码，为您的工作添加注释。
- **您将建立**：JavaScript 文件，这些文件将通过 Copilot AI 生成代码和注释建议。
- **先决条件**：要使用 GitHub Copilot，您必须拥有一个有效的 GitHub Copilot 订阅。在此处免费注册 30 天 [Copilot](https://github.com/settings/copilot) 。
- **时间**：您可以在一小时内完成这门课程。

这个模块结束后，您将获得以下技能：

- 在 代码空间 中配置 GitHub 仓库并且安装 GitHub Copilot 扩展。
- 制定提示以从 GitHub Copilot 产生建议。
- 应用 GitHub Copilot 提升您的项目。

## 预先阅读：
- [Introduction to prompt engineering with GitHub Copilot](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot//?WT.mc_id=academic-113596-abartolo)
- [Using GitHub Copilot with JavaScript](https://learn.microsoft.com/training/modules/introduction-copilot-javascript/?WT.mc_id=academic-113596-abartolo)


## 要求

1. 启用您的 [GitHub Copilot 服务](https://github.com/github-copilot/signup)
1. 在 Codespaces 中打开 [this repository](https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-javascript?quickstart=1)


## 💪🏽 练习

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=526682619)

在这个模板组合中，我们为您准备了一个 React 基础的网络应用，您可以在您的网络浏览器中方便地自定义和部署。

### 🛠 第一步：定制网络应用

使用您自己的链接定制组合。进入 `src/App.jsx`，更新其中的`siteProps`以添加您的信息。这是一个用于定制网站，富含键值对的 JavaScript 对象，它应该看起来像这样：

```javascript
const siteProps = {
  name: "Alexandrie Grenier",
  title: "Web Designer & Content Creator",
  email: "alex@example.com",
  gitHub: "microsoft",
  instagram: "microsoft",
  linkedIn: "satyanadella",
  medium: "",
  twitter: "microsoft",
  youTube: "Code",
};
```

### 🔎 第二步：使用提示为社交媒体图标添加动效

接下来，通过添加评论生成一个新的端点：

动画能让社交媒体部分更吸人眼球。请求 Copilot 的帮助为图标添加动效。在 `src/styles.css` 文件中，写下以下的提示：

```css
/* add an amazing animation to the social icons */
```

来自 Copilot 的建议应与以下内容类似：

```css
img.socialIcon:hover {
  animation: bounce 0.5s;
  animation-iteration-count: infinite;
}

@keyframes bounce {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
```

### 🚀 第三步：运用建议

接受这个建议，按 Tab 键即可。如果您并没有得到完全相同的建议，那么您可以尝试用提供的建议进行试验，或者继续编写 CSS 代码，直到结果匹配。

您的站点应该已经在您的 代码空间 中运行，改变会自动重载至页面。要查看效果，您可以将鼠标悬停在您的底部社交媒体图标上，看看效果如何！

恭喜您，通过这个练习，您不仅用 Copilot 生成了代码，而且还以一种互动和有趣的方式完成了这个过程！您可以使用 GitHub Copilot 不仅生成代码，还编写文档，测试您的应用等等。