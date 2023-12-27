<header>

# GitHub 代码空间(Codespaces)简介

欢迎来到充满刺激的GitHub 代码空间世界，这是您的云端编程资源。在本模块中，我们将深入探讨即时的云端开发环境，这将彻底改变您的编程方式。GitHub 代码空间为您提供了一个无缝整合的体验，带有用于开发的基础语言、工具和实用程序的容器。

在这个学习之旅中，我们将研究代码空间的生命周期和过程。揭示定制您的代码空间设置以适应您独特的喜好和需求的能力。参与对GitHub 代码空间和GitHub.dev的比较分析，深入了解这两个创新平台之间的区别。为了巩固您的理解，我们将在最后进行一个动手练习，让您在GitHub 代码空间环境中展示您的编程实力。

想象一下，一个已经完全配置好的开发环境就在您的指尖，只要有互联网连接的任何电脑都可以访问。GitHub Codespaces为协作和灵活编程的新时代敞开了大门。让我们一起深入挖掘，解锁云端开发的全部潜力吧！

</header>


- **适合对象**: 开发者、DevOps工程师、工程经理、产品经理。
- **您将学习**: 如何创建一个代码空间，从代码空间推送代码，选择自定义图像以及如何定制代码空间。
- **您将要构建**: 含有devcontainer.json文件、定制和个性化的代码空间。
- **预置知识要求**: 您需要了解以下内容：
  - Visual Studio代码的使用， [Visual Studio Code 文档](https://code.visualstudio.com/docs)。
  - 对GitHub使用的理解或完成【GitHub入门】(https://github.com/WirelessLife/Mastering-GitHub-Copilot-for-Paired-Programming/blob/main/01-Introduction-to-GitHub/README.md?WT.mc_id=academic-113596-abartolo)这个模块。
- **所需时间**: 这门课程可以在1小时内完成。

在本模块结束后，您将能够：

1. 描述GitHub 代码空间。
2. 解释GitHub 代码空间的生命周期以及如何执行每个步骤。
3. 定义您可以使用GitHub 代码空间个性化的不同定制项。
4. 分清GitHub.dev和GitHub 代码空间之间的差异。


## 预备阅读: 

- [通过GitHub 代码空间编程](https://learn.microsoft.com/training/modules/code-with-github-codespaces/?WT.mc_id=academic-113596-abartolo)
- 什么是GitHub Codespaces? (以下视频播放列表)
- [![什么是代码空间](https://img.youtube.com/vi/ozuDPmcC1io/0.jpg)](https://www.youtube.com/watch?v=ozuDPmcC1io&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-)



### 如何开始这门课程

<!-- 开始课程，运行 JavaScript:
'https://github.com/new?' + new URLSearchParams({
  template_owner: 'skills',
  template_name: 'code-with-codespaces',
  owner: '@me',
  name: 'skills-code-with-codespaces',
  description: 'My clone repository',
  visibility: 'public',
}).toString()
-->

[![开始课程](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=skills&template_name=code-with-codespaces&owner=%40me&name=skills-code-with-codespaces&description=My+clone+repository&visibility=public)

1. 右键点击**开始课程**并在新标签页中打开链接。
2. 在新打开的标签页中，大部分提示将会自动为您填充。
   - 对于所有者，选择您的个人帐户或一个组织来托管仓库。
   - 我们推荐创建一个公共仓库，因为私人仓库会[使用Action分钟](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions?WT.mc_id=academic-113596-abartolo)。
   - 向下滚动并点击表格底部的**创建仓库**按钮。
3. 创建好新仓库后，等待大约20秒，然后刷新页面。按照新仓库的README中的分步说明进行操作。

<footer>

<!--
  <<< 作者注: Footer >>>
  添加获取支持的链接、GitHub状态页面、行为准则、许可证链接。
-->

---

获取帮助：[在我们的讨论板发布](https://github.com/orgs/skills/discussions/categories/introduction-to-github) &bull; [查看Github状态页面](https://www.githubstatus.com/)