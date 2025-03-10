---
title: 如何安装 Aspose.PDF for .NET
linktitle: 安装
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/installation/
description: 本节展示了产品描述和在您自己计算机上安装 Aspose.PDF for .NET 的说明，以及使用 NuGet 的方法。
lastmod: "2024-09-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Install Aspose.PDF for .NET",
    "alternativeHeadline": "Seamless PDF Creation with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET 是一个强大的组件，使开发人员能够以编程方式生成和操作 PDF 文档，而无需依赖 Adobe Acrobat。支持插入复杂元素，如表格、图像和自定义字体，以及强大的安全功能和通过 NuGet 的无缝集成，这个多功能工具提高了 .NET 应用程序的生产力和效率。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Aspose.PDF, PDF documents, .NET component, NuGet installation, C# API, Temporary License, multithread safe, eval version limitations, .NET Core support, font installation",
    "wordcount": "1214",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/installation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/installation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## Aspose.PDF C# 组件

{{% alert color="primary" %}}

**Aspose.PDF 是一个 .NET** 组件，旨在允许开发人员以编程方式动态创建 PDF 文档，无论是简单还是复杂。Aspose.PDF for .NET 允许开发人员将表格、图形、图像、超链接、自定义字体等插入 PDF 文档。此外，还可以压缩 PDF 文档。Aspose.PDF for .NET 提供出色的安全功能，以开发安全的 PDF 文档。而 Aspose.PDF for .NET 最显著的特点是它支持通过 API 和 XML 模板创建 PDF 文档。

{{% /alert %}}

## 产品描述

**Aspose.PDF for .NET** 是一个强大的 .NET 组件，使开发人员能够从头开始创建 PDF 文档，而无需使用 Adobe Acrobat。它提供了一个简单的应用程序编程接口（API），易于学习和使用。

**Aspose.PDF for .NET** 是使用托管 C# 实现的，可以与任何 .NET 语言一起使用，如 C#、VB.NET 和 J# 等。它可以与任何类型的应用程序集成，无论是 ASP.NET Web 应用程序还是 Windows 应用程序。

为了让开发人员能够快速上手，Aspose.PDF for .NET 提供了功能齐全的演示和用 C# 编写的工作示例。通过这些演示，开发人员可以快速了解 Aspose.PDF for .NET 提供的功能。

这个快速、轻量级的组件高效地创建 PDF 文档，并帮助您的应用程序表现得更好。Aspose.PDF for .NET 是我们客户创建 PDF 文档时的首选，因为它的价格、卓越的性能和良好的支持。

**Aspose.PDF for .NET** 是多线程安全的，只要每次只有一个线程在处理一个文档。通常情况下，一个线程处理一个文档是典型场景。不同线程可以安全地同时处理不同的文档。

## 声明

所有 Aspose .NET 组件都需要完全信任权限集。原因是，Aspose .NET 组件需要访问注册表设置、系统文件（除了虚拟目录）以执行某些操作，如解析字体等。此外，Aspose .NET 组件基于核心 .NET 系统类，这在许多情况下也需要完全信任权限集。

托管多个来自不同公司的应用程序的互联网服务提供商通常会强制执行中等信任安全级别。在 .NET 2.0 的情况下，这种安全级别适用以下限制：

- **OleDbPermission 不可用。** 这意味着您无法使用 ADO.NET 托管 OLE DB 数据提供程序访问数据库。
- **EventLogPermission 不可用。** 这意味着您无法访问 Windows 事件日志。
- **ReflectionPermission 不可用。** 这意味着您无法使用反射。
- **RegistryPermission 不可用。** 这意味着您无法访问注册表。
- **WebPermission 受到限制。** 这意味着您的应用程序只能与您在 `<trust>` 元素中定义的地址或地址范围进行通信。
- **FileIOPermission 受到限制。** 这意味着您只能访问应用程序的虚拟目录层次结构中的文件。
由于上述原因，Aspose .NET 组件无法在授予非完全信任权限集的服务器上使用。

## 安装

### 评估 Aspose.PDF for .NET

您可以轻松下载 Aspose.PDF for .NET 进行评估。评估下载与购买下载相同。评估版本只需在您添加几行代码以应用许可证后即可获得许可。

Aspose.PDF 的评估版本（未指定许可证）提供完整的产品功能。然而，它有两个限制：它插入评估水印，并且任何文档的前四页只能查看/编辑。

{{% alert color="primary" %}}

如果您想在没有评估版本限制的情况下测试 Aspose.PDF for .NET，您还可以申请 30 天的临时许可证。请参阅 [如何获取临时许可证？](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

### 通过 NuGet 安装 Aspose.PDF for .NET

NuGet 是一个免费的开源开发者专用包管理系统，旨在简化在开发过程中将第三方库纳入 .NET 应用程序的过程。它是一个 Visual Studio 扩展，使得在使用 .NET Framework 的 Visual Studio 项目中轻松添加、删除和更新库和工具。通过创建 NuGet 包并将其存储在 NuGet 存储库中，可以轻松与其他开发人员共享库或工具。当您安装包时，NuGet 会将文件复制到您的解决方案中，并自动进行必要的更改，例如添加引用和更改您的 app.config 或 web.config 文件。如果您决定删除库，NuGet 会删除文件并撤销对项目所做的任何更改，以确保没有留下杂乱。

### 引用 Aspose.PDF for .NET

#### 使用包管理器控制台安装包

- 在 Visual Studio 中打开您的 .NET 应用程序。
- 在工具菜单中，选择 **NuGet 包管理器**，然后选择 **包管理器控制台**。
- 输入命令 `Install-Package Aspose.PDF` 安装最新的完整版本，或输入命令 `Install-Package Aspose.PDF -prerelease` 安装包括热修复的最新版本。
- 按 `Enter`。

#### 使用包管理器控制台更新包

如果您已经通过 NuGet 引用了该组件，请按照以下步骤更新引用到最新版本：

- 在 Visual Studio 中打开您的 .NET 应用程序。
- 在工具菜单中，选择 **NuGet 包管理器**，然后选择 **包管理器控制台**。
- 输入命令 `Update-Package Aspose.PDF` 引用最新的完整版本，或输入命令 `Update-Package Aspose.PDF -prerelease` 安装包括热修复的最新版本。

#### 使用包管理器 GUI 安装包

按照以下步骤使用包管理器 GUI 引用该组件：

- 在 Visual Studio 中打开您的 .NET 应用程序。

- 从项目菜单中选择 **管理 NuGet 包**。

![Installation_step](../images/install_step.png)

- 选择 **浏览** 选项卡。

![Installation_step1](../images/install_step1.png)

- 在搜索框中输入 Aspose.PDF 以查找 Aspose.PDF for .NET。

- 点击最新版本的 Aspose.PDF for .NET 旁边的安装/更新。

![Installation_step2](../images/Install_step2.png)

- 然后在弹出窗口中点击接受。

![Installation_step3](../images/Install_step3.png)

![Installation](../images/install.gif)

### 在非 Windows 环境中使用 .NET Core DLL

由于 Aspose.PDF for .NET 提供 .NET Standard 2.0 (.NET Core 2.0) 支持，因此可以在运行 Linux 等操作系统的 Core 应用程序中使用。我们正在不断努力改善我们 API 中的 .NET Core 支持。然而，我们建议客户执行以下操作，以便在使用 Aspose.PDF for .NET 的功能时获得更好的结果：

请安装：

- libgdiplus 包
- 与 Microsoft 兼容的字体包：**ttf-mscorefonts-installer**。 (例如 `sudo apt-get install ttf-mscorefonts-installer`)
这些字体应放置在 "/usr/share/fonts/truetype/msttcorefonts" 目录中，因为 Aspose.PDF for .NET 会扫描该文件夹以在 Linux 等操作系统上使用。如果操作系统有其他默认的字体文件夹/目录，您应在使用 Aspose.PDF 执行任何操作之前使用以下代码行。

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<user's path to ms fonts>"));
```

#### 在 Visual Studio Code 中设置 Aspose.PDF for .NET
- 安装 .NET SDK

1. 访问官方 [Microsoft .NET 网站](https://dotnet.microsoft.com/download)。
2. 下载最新的 .NET SDK。
3. 运行安装程序。
4. 打开终端并通过运行以下命令验证安装：
```bash
dotnet --version
```

- 安装 Visual Studio Code

1. 转到 https://code.visualstudio.com/。
2. 下载适合您操作系统的版本。

- 安装所需的 VS Code 扩展

1. 打开 Visual Studio Code。
2. 点击扩展视图图标（左侧边栏上的方形图标）。
3. 搜索并安装以下扩展：
   - Microsoft 的 "C#"
   - Microsoft 的 "C# Dev Kit"
   - ".NET Core Test Explorer"（可选，但推荐）

- 创建一个新的 .NET 项目

1. 打开 Visual Studio Code
2. 转到终端 > 新终端
3. 导航到您希望的项目目录
```bash
# Create a new console application
dotnet new console -n AsposePDFNetDemo
# Navigate into the project directory
cd AsposePDFNetDemo
```

- 添加 NuGet 包

```bash
# Install Aspose.PDF package
dotnet add package Aspose.PDF
```

- 验证包安装

1. 打开 `.csproj` 文件
2. 确认已添加 Aspose.PDF 包引用：
```xml
<ItemGroup>
  <PackageReference Include="Aspose.PDF" Version="x.x.x" />
</ItemGroup>
```

- 创建调试配置

1. 按 Ctrl+Shift+P（Mac 上为 Cmd+Shift+P）。
2. 输入 ">.NET: 生成构建和调试的资产"。
3. 选择您的项目。
4. 创建或修改 `.vscode/launch.json`：
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net7.0/AsposePDFNetDemo.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "console": "internalConsole",
            "stopAtEntry": false
        }
    ]
}
```

- 编写示例代码 Program.cs

将 `Program.cs` 的内容替换为：
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
using System;
using Aspose.Pdf;
using Aspose.Pdf.Text;

class Program 
{
    static void Main(string[] args)
    {
        // Activate your license, you can comment out these codelines to use library in Evaluation mode
        var license = new Aspose.Pdf.License();
        license.SetLicense("Aspose.PDF.NET.lic");

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();
            
            // Create a text fragment
            var textFragment = new Aspose.Pdf.Text.TextFragment("Hello, Aspose.PDF for .NET!");
            textFragment.Position = new Aspose.Pdf.Text.Position(100, 600);
            
            // Add text to the page
            page.Paragraphs.Add(textFragment);
            
            // Save PDF document
            document.Save("sample.pdf");
        }
    }
}
```

- 构建并运行

```bash
dotnet restore
dotnet build
dotnet run
```