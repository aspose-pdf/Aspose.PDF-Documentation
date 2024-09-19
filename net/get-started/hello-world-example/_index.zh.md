---
title: 使用 C# 语言的 Hello World 示例
linktitle: Hello World 示例
type: docs
weight: 40
url: /net/hello-world-example/
description: 本示例演示如何使用 Aspose.PDF 创建一个简单的包含文本 Hello World 的 PDF 文档
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 C# 语言的 Hello World 示例",
    "alternativeHeadline": "Aspose.PDF C# 示例",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDF 文档生成",
    "keywords": "pdf, c#, 文档生成",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
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
                "contactType": "销售",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "销售",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "销售",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "本示例演示如何使用 Aspose.PDF 创建一个简单的包含文本 Hello World 的 PDF 文档",
    "articleBody": "“Hello World”示例传统上用于介绍编程语言或软件的特性，通过一个简单的用例。\nAspose.PDF for .NET 是一个功能丰富的 PDF API，允许开发者在他们的 .NET 应用程序中嵌入 PDF 文档创建、操作和转换功能。它支持处理多种流行的文件格式，包括 PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX 和图像文件格式。在本文中，我们将创建一个包含文本“Hello World!”的 PDF 文档。在您的环境中安装 Aspose.PDF for .NET 后，您可以执行以下代码示例来查看 Aspose.PDF API 的工作方式。\n以下代码片段遵循这些步骤：\n1. 实例化一个 Document 对象\n2. 向文档对象添加一个页面\n3. 创建一个 TextFragment\n4. 将 TextFragment 添加到页面的 Paragraph 集合中\n5. 保存结果 PDF 文档\n以下代码片段是一个展示 Aspose.PDF for .NET API 工作的 Hello World 程序。"
}
</script>
"Hello World" 示例通常用来介绍编程语言或软件的特性，以一个简单的用例。

Aspose.PDF for .NET 是一个功能丰富的 PDF API，允许开发者在他们的 .NET 应用程序中嵌入 PDF 文档创建、操作和转换功能。它支持处理许多流行的文件格式，包括 PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX 和图像文件格式。在本文中，我们将创建一个包含文本 "Hello World!" 的 PDF 文档。安装 Aspose.PDF for .NET 在您的环境后，您可以执行下面的代码示例来查看 Aspose.PDF API 的工作方式。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

以下代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. 将TextFragment添加到页面的[段落](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)集合中
1. [保存](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)生成的PDF文档

以下代码片段是一个Hello World程序，用于展示Aspose.PDF for .NET API的工作原理。

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // 初始化文档对象
            Document document = new Document();
            // 添加页面
            Page page = document.Pages.Add();
            // 向新页面添加文本
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // 保存更新后的PDF
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
