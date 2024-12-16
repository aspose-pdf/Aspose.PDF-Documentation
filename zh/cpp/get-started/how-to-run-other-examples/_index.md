---
title: 如何运行其他 Aspose.PDF for C++ 示例
linktitle: 如何运行其他示例
type: docs
weight: 50
url: /zh/cpp/how-to-run-other-examples/
description: 本页展示了在下载和运行示例之前会有帮助的指南。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 软件要求

请确保在下载和运行示例之前满足以下要求。

1. Microsoft Visual Studio 2017 或更高版本。
1. 在 Visual Studio 中安装了 NuGet 包管理器。确保在 Visual Studio 中安装了最新的 NuGet API 版本。有关如何安装 NuGet 包管理器的详细信息，请查看 <http://docs.nuget.org/ndocs/guides/install-nuget>
1. 转到 `工具->选项->NuGet 包管理器->包源` 并确保选中选项 **nuget.org** 示例项目使用NuGet自动包还原功能，因此您应该有一个活动的互联网连接。如果您在要执行示例的计算机上没有活动的互联网连接，请检查[安装](/pdf/zh/cpp/installation/)并在示例项目中手动添加对Aspose.PDF.dll的引用。

## 从GitHub下载

Aspose.PDF for C++的所有示例都托管在[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-C)上。

- 您可以使用您喜欢的GitHub客户端克隆存储库，或者从[这里](https://codeload.github.com/aspose-pdf/Aspose.PDF-for-C/zip/master)下载ZIP文件。
- 将ZIP文件的内容解压到计算机上的任意文件夹。所有示例都位于**Examples**文件夹中。
- 有两个Visual Studio解决方案文件，一个用于控制台应用程序，另一个用于Web应用程序。
- 项目是在Visual Studio 2013中创建的，但解决方案文件与Visual Studio 2010 SP1及更高版本兼容。

- 在Visual Studio中打开解决方案文件并构建项目。- 在第一次运行时，依赖项将通过 NuGet 自动下载。
- **Examples** 根文件夹中的 **Data** 文件夹包含 CSharp 示例使用的输入文件。务必下载 **Data** 文件夹以及示例项目。
- 打开 *RunExamples.cs* 文件，所有示例都是从这里调用的。
- 取消注释您希望在项目中运行的示例。

如果您在设置或运行示例时遇到任何问题，请随时使用我们的论坛联系我们。

## 贡献

如果您想添加或改进示例，我们鼓励您为项目做出贡献。此存储库中的所有示例和展示项目都是开源的，可以在您自己的应用程序中自由使用。

要贡献，您可以 fork 此存储库，编辑源代码并创建一个 pull request。如果发现有帮助，我们将审核更改并将其包含在存储库中。