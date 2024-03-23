<header>

# 利用GitHub Copilot创建小游戏

本模块的焦点是运用GitHub Copilot的力量来创建一个经典的石头、剪刀、布小游戏。这种实践经验不仅能够提炼的编程技能，同时还能提高在Python平台下开发控制台应用程序的能力。最棒的是什么呢？我们将剥离所有烦琐的开发环境配置步骤，利用GitHub的代码库。有了GitHub Copilot作为的人工智能编程伙伴，可以专注于应用程序的开发，毫无阻碍地与的代码助理合作。

</header>

- **本课程适合的人群**：开发人员，DevOps工程师，软件开发经理，测试人员。
- **将学到**：运用GitHub Copilot创建代码和为的工作添加注释的方法。
- **将构建**：Python文件，该文件将包括由Copilot AI生成的代码和注释建议。
- **预备知识**：要使用GitHub Copilot，您必须持有一个有效的GitHub Copilot订阅。点击这里免费试用30天 [Copilot](https://github.com/settings/copilot)。
- **预计时长**：本课程预计一个小时内可以完成。

在本模块的结尾，将掌握以下能力：

- 体验GitHub的代码库作为开发环境。
- 在Python控制台应用程序中开发输入和输出例程。
- 使用GitHub Copilot作为助手。

## 预备阅读：
- [利用GitHub Copilot进行提示工程的介绍](https://learn.microsoft.com/training/modules/introduction-prompt-engineering-with-github-copilot//?WT.mc_id=academic-113596-abartolo)
- [挑战项目 - 利用GitHub Copilot和Python构建一个小游戏](https://learn.microsoft.com/training/modules/challenge-project-create-mini-game-with-copilot/?WT.mc_id=academic-113596-abartolo)
- 利用GitHub Copilot创建一个小游戏控制台应用程序的实时学习：视频如下
- [![利用GitHub Copilot创建小游戏控制台应用程序的实时学习](https://mediusimg.event.microsoft.com/video-53275/b508053c0b/thumbnail.jpg?sv=2018-03-28&sr=c&sig=k6NthrPwnvBfDPNAEBQaYaVzlJavZ8pnWuP6OcKm4Bs%3D&se=2028-11-18T05%3A23%3A52Z&sp=r)](https://ignite.microsoft.com/sessions/aeaf1e85-65e2-497d-aaf5-724d85213aa1?WT.mc_id=academic-113596-abartolo)
  

## 要求

- 启用的[GitHub Copilot服务](https://github.com/github-copilot/signup)

## 💪🏽 练习

[![开始课程](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=skills&template_name=copilot-codespaces-vscode&owner=%40me&name=skills-copilot-codespaces-vscode&description=My+clone+repository&visibility=public)

已经初步了解了GitHub代码库和GitHub Copilot以及它们是如何运作的。在本次挑战性练习中，的目标是利用GitHub Copilot开发一个Python小游戏。

#### 测试的GitHub代码库

1. 访问的代码库并在Visual Studio Code中创建一个名为*app.py*的新文件。

   **注意：**可能需要在Visual Studio Code中安装Python扩展，如果当前没有安装的话。

2. 输入以下注释：

   ```python
   # 将 'hello world' 写到控制台
   ```
      
3. GitHub Copilot应为完善码，并提供以下结果：

   ```python
   # 将 'hello world' 写到控制台
   print('hello world')
   ```

4. 在终端中输入*python app.py*命令运行应用，检查结果是否类似于以下控制台消息：

   ```bash
   hello world
   ```
   
### 创建游戏逻辑

既然已经验证了代码库和GitHub Copilot的联合工作能力，接下来需要利用GitHub Copilot帮助开发符合以下规范的Python小游戏逻辑：

游戏的赢家由三个简单规则决定：

- **石头** 击败剪刀。
- **剪刀** 击败布。
- **布** 击败石头。

#### 游戏交互考虑

计算机将作为的对手，随机选择一种元素（**石头**，**剪刀**或者**布**）。的游戏交互将通过控制台（终端）进行。

- 玩家可以选择三个选项之一：石头，剪刀或者布，如果输入了无效选项，应该得到提示。
- 每一轮中，玩家必须输入列表中的一个选项，并被告知他们是赢了、输了还是平手。
- 每轮结束后，玩家可以选择是否再玩一次。
- 游戏结束后，显示玩家的得分。
- 小游戏需要处理用户输入，将其转化为小写，并在选项无效时告知用户。

在的GitHub代码库中，按照给定的指示设置提示，让GitHub Copilot能够理解并帮助建立小游戏。请记住，GitHub Copilot依赖于注释来把握上下文，并在进行项目时为提供有用的建议。

#### 验证的工作

1. 在控制台上运行小游戏并输入*python app.py*命令。
2. 在提示时，输入游戏选项之一：*石头*，*布*或者*剪刀*。
3. 小游戏应该告诉玩家他的输赢情况，或者和对手平手。
4. 选择继续游戏。
5. 在提示时，输入*screen*。
6. 如果玩家输入的选项无效，小游戏应该告诉玩家。
7. 重复步骤2和4，玩几个回合并选择不继续游戏。
8. 检查是否结束了小游戏，是否显示了的得分，包括胜场数和轮数。

恭喜完成了这个挑战性练习!已经利用GitHub Copilot创建了一个Python控制台小游戏。