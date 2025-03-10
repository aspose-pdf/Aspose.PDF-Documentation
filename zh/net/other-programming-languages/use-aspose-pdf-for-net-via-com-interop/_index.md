---
title: Aspose.PDF for .NET 通过 COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/use-aspose-pdf-for-net-via-com-interop/
description: 了解如何通过 COM Interop 使用 Aspose.PDF for .NET，以便与非 .NET 应用程序无缝集成。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET 现在支持通过 COM Interop 与各种编程语言的无缝集成，使开发人员能够在 .NET 框架之外利用其强大的 PDF 操作能力。此功能通过将 Aspose.PDF 对象转换为 COM 对象来增强灵活性，简化与非托管代码的交互，同时通过早期和晚期绑定技术保持高性能。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

本主题中的信息适用于您希望在以下任何编程语言中通过 COM Interop 使用 [Aspose.PDF for .NET](/pdf/zh/net/) 的场景：

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## 使用 COM Interop

Aspose.PDF for .NET 在 .NET 框架的控制下执行，这称为托管代码。用上述所有语言编写的代码在 .NET 框架之外运行，这称为非托管代码。非托管代码与 Aspose.PDF 之间的交互通过称为 COM Interop 的 .NET 功能进行。

Aspose.PDF 对象是 .NET 对象，但在通过 COM Interop 使用时，它们在您的编程语言中表现为 COM 对象。因此，在开始使用 [Aspose.PDF for .NET](/pdf/zh/net/) 之前，最好确保您知道如何在您的编程语言中创建和使用 COM 对象。

{{% alert color="primary" %}}

- 在 COM 世界中，我们区分 COM 服务器和 COM 客户端。COM 服务器存储 COM 类，而 COM 客户端请求 COM 服务器的类实例，即 COM 对象。
- COM 客户端或简单的客户端应用程序可以对 COM 类的内容有所了解，或者对其方法和属性完全不了解。因此，客户端应用程序可以在编译/构建时或仅在执行期间发现 COM 类结构。“发现”过程称为绑定，因此我们有 **早期绑定** 和 **晚期绑定**。
- 简而言之，COM 类就像黑匣子，要与其工作需要类型库，这个二进制文件描述了 COM 类的方法、属性，任何支持与 COM 对象一起工作的高级语言通常都有添加类型库的语法表达，例如在 C++ 中这是 [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx)。
- 类型库用于早期绑定。
- COM 对象可以通过两种方式公开其方法和属性：通过 **调度接口**（dispinterface）和在其 **vtable**（虚函数表）中。
- 在 **dispinterface** 中，每个方法和属性由唯一成员标识；该成员是函数的调度标识符（或 **DispID**）。
- **vtable** 只是指向 COM 类接口支持的函数的指针集合。
- 通过这两种接口公开其方法的对象支持 **双接口**。
- 两种绑定类型都有其优点。早期绑定为您提供了更高的性能和编译时语法检查。晚期绑定在您编写打算与未来版本的 COM 类 ***兼容*** 的客户端时最为有利。使用晚期绑定，类型库中的信息不会“硬编码”到您的客户端中，因此您可以更有信心地认为您的客户端可以在没有代码更改的情况下与未来版本的 COM 类一起工作。
- 晚期绑定机制有一个很大的优势：如果 COM DLL 的创建者决定发布新版本，具有不同的函数接口布局，任何调用这些方法的代码都不会崩溃，除非这些方法不再可用；即使 **vtable** 不同，晚期绑定也能发现新的 DISPIDs 并调用适当的方法。
{{% /alert %}}

以下是您最终需要掌握的主题：
{{% alert color="primary" %}}

- 在您的编程语言中使用 COM 对象。请参阅您的编程语言文档以及本文档中后面的语言特定主题。

- 使用 .NET COM Interop 暴露的 COM 对象。请参阅 [与非托管代码互操作](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) 和 [将 .NET Framework 组件暴露给 COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) 在 MSDN 中。

- Aspose.PDF 文档对象模型。请参阅 [Aspose.PDF 程序员指南](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) 和 [API 参考](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference)。

{{% /alert %}}

## 使用 COM Interop 注册 Aspose.PDF for .NET

您需要安装 Aspose.PDF for .NET 并确保它已通过 COM Interop 注册（确保可以从非托管代码调用它）。

{{% alert color="primary" %}}

要手动注册 Aspose.PDF for .NET 以进行 COM Interop：

1. 从 **开始** 菜单中，选择 **所有程序**，然后选择 **Microsoft Visual Studio**、**Visual Studio 工具**，最后选择 **Visual Studio 命令提示符**。
1. 输入注册程序集的命令：
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

请注意，/codebase 仅在 Aspose.PDF.dll 不在 GAC 中时才是必要的，使用此选项会使 regasm 将程序集的路径放入注册表中。

{{% alert color="primary" %}}

regasm.exe 是 .NET Framework SDK 中包含的工具。所有 .NET Framework SDK 工具位于 *\Microsoft .NET\Framevork\<FrameworkVersion>* 目录中，例如 *C:\Windows\Microsoft .NET\Framework\v4.0.30319*。如果您使用 Visual Studio .NET：
从 **开始** 菜单中，选择 **程序**，然后选择 **Visual Studio 2022**，最后选择 **VS 2022 的开发者命令提示符**。
它会运行一个命令提示符，并设置所有必要的环境变量。

{{% /alert %}}

### ProgIDs

ProgID 代表“程序标识符”。它是用于创建对象的 COM 类的名称。ProgID 由库名称 "Aspose.PDF" 和类名称组成。

### 类型库

{{% alert color="primary" %}}

如果您的编程语言（例如 Visual Basic 或 Delphi）允许您引用 COM 类型库，则添加对 Aspose.PDF.tlb 的引用，以查看您对象浏览器中的所有 Aspose.PDF for .NET 类、方法、属性和枚举。

要生成 TLB 文件：

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## 创建 COM 对象

创建 COM 对象类似于创建普通 .NET 对象：

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

创建后，您可以访问对象的方法和属性，就像它是一个 COM 对象一样：

```vb
'Add page to the document
document.Pages.Add()
```

某些方法具有重载，它们将通过 COM Interop 暴露，并添加数字后缀，除了第一个方法保持不变。例如，Document.Save 方法的重载变为 Document.Save、Document.Save_2 等。

有关更多信息，请参阅本文件中后面的语言特定文章。

## 创建包装程序集

如果您需要使用许多 Aspose.PDF for .NET 类、方法和属性，请考虑创建一个包装程序集（使用 C# 或任何其他 .NET 编程语言）。包装程序集有助于避免直接从非托管代码使用 Aspose.PDF for .NET。

一个好的方法是开发一个引用 Aspose.PDF for .NET 的 .NET 程序集，并与之进行所有工作，仅向非托管代码公开一组最小的类和方法。然后，您的应用程序应仅与您的包装库一起工作。

减少通过 COM Interop 调用的类和方法的数量简化了项目。通过 COM Interop 使用 .NET 类通常需要高级技能。