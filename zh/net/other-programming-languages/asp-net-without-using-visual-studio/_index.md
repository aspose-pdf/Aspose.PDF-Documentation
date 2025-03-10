---
title: 不使用 Visual Studio 的 ASP.NET
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/asp-net-without-using-visual-studio/
description: 学习如何在 ASP.NET 项目中使用 Aspose.PDF for .NET，而无需依赖 Visual Studio。请遵循此实用指南。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "ASP.NET without using Visual Studio",
    "alternativeHeadline": "Create ASP.NET Applications Without Visual Studio",
    "abstract": "发现如何在不依赖 Visual Studio 的情况下使用 Aspose.PDF for .NET 创建 ASP.NET 应用程序。这种创新的方法允许开发人员在单个 .aspx 文件中编写 HTML 和 C# 或 VB.NET 代码，从而简化了直接在 ASP.NET 页面中生成 PDF 文档的过程。通过这种无缝集成最大化您的开发效率",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "263",
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
    "url": "/net/asp-net-without-using-visual-studio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/asp-net-without-using-visual-studio/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) 可用于开发不使用 Visual Studio 的 ASP.NET 页面或应用程序。在此示例中，我们将在单个 .aspx 文件中编写 HTML 和 C# 或 VB.NET 代码；这通常被称为即时 ASP.NET。

{{% /alert %}}

## 实施细节

{{% alert color="primary" %}}

创建一个示例 web 应用程序，并将 Aspose.PDF.dll 复制到您网站目录中名为 "Bin" 的目录中（*如果 bin 文件夹不存在，请创建一个*）。然后创建您的 .aspx 页面并将以下代码复制到其中。
此示例演示如何在 ASP.NET 页面中使用 [Aspose.PDF for .NET](/pdf/net/) 和内联代码，以创建一个包含一些示例文本的简单 PDF 文档。
{{% /alert %}}

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> using Aspose.PDF for .NET with Inline ASP.NET</title>
    </head>
    <body>
        <h3>creation of simple PDF document while using Aspose.PDF for .NET with Inline ASP.NET</h3>
<%
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Set license
    Aspose.Pdf.License lic = new Aspose.Pdf.License();
    lic.SetLicense("Aspose.Total.lic");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        Aspose.Pdf.Page page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
%>

    </body>
</html>
```