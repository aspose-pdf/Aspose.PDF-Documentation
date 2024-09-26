---
title: 如何运行其他示例
linktitle: 如何运行其他示例
type: docs
weight: 50
url: /net/how-to-run-other-examples/    
description: 本页面提供的指南将帮助您在下载和运行示例之前满足以下要求。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 软件要求

请确保在下载和运行示例之前满足以下要求。

1. Visual Studio 2010 或更高版本
1. Visual Studio 中安装了 NuGet 包管理器。确保 Visual Studio 中安装了最新的 NuGet API 版本。有关如何安装 NuGet 包管理器的详细信息，请查看 <https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools>
1. 转到 `Tools->Options->NuGet Package Manager->Package Sources` 并确保选项 **nuget.org** 已勾选
1.
## 从 GitHub 下载

所有 Aspose.PDF for .NET 的示例都托管在 [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-.NET) 上。

- 您可以使用您喜欢的 GitHub 客户端克隆仓库，或者从[这里](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/archive/master.zip)下载 ZIP 文件。
- 将 ZIP 文件的内容解压到计算机上的任意文件夹。所有示例都位于 **Examples** 文件夹中。
- 有两个 Visual Studio 解决方案文件，一个用于控制台，另一个用于 Web 应用程序。
- 项目是在 Visual Studio 2013 中创建的，但解决方案文件与 Visual Studio 2010 SP1 及更高版本兼容。
- 在 Visual Studio 中打开解决方案文件并构建项目。
- 首次运行时，依赖项将通过 NuGet 自动下载。
- **Examples** 根文件夹中的 **Data** 文件夹包含 CSharp 示例使用的输入文件。下载示例项目时，必须下载 **Data** 文件夹。
- 打开 *RunExamples.cs* 文件，所有示例都从这里调用。
- 打开 *RunExamples.cs* 文件，所有示例都从这里调用。
- 从项目中取消注释您想要运行的示例。

如果在设置或运行示例时遇到任何问题，请随时通过我们的论坛联系我们。

## Contribute

如果您想添加或改进一个示例，我们鼓励您为项目做出贡献。此仓库中的所有示例和展示项目都是开源的，可以在您自己的应用程序中自由使用。

要贡献，您可以复制仓库，编辑源代码并创建一个拉取请求。我们将审查更改，并在发现有帮助的情况下将其包含在仓库中。
