---
title: 使用 C# 语言的 Hello World 示例
linktitle: Hello World 示例
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/hello-world-example/
description: 此示例演示如何使用 Aspose.PDF 创建一个简单的包含文本 Hello World 的 PDF 文档
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Example of Hello World using C# language",
    "alternativeHeadline": "Aspose.PDF C# example",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2024-11-26",
    "description": "此示例演示如何使用 Aspose.PDF 创建一个简单的包含文本 Hello World 的 PDF 文档",
    "articleBody": "A \"Hello World\" example is traditionally used to introduce features of a programming language or software with a simple use case.\nAspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text \"Hello World!\". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.\nBelow code snippet follows these steps:\n1. // Create PDF document\n2. Add a Page to document object\n3. Create a TextFragment\n4. Add TextFragment to Paragraph collection of the page\n5. Save resultant PDF document\nFollowing code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API."
}
</script>

一个 "Hello World" 示例通常用于通过一个简单的用例介绍编程语言或软件的特性。

Aspose.PDF for .NET 是一个功能丰富的 PDF API，允许开发人员在其 .NET 应用程序中嵌入 PDF 文档创建、操作和转换功能。它支持处理许多流行的文件格式，包括 PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX 和图像文件格式。在本文中，我们将创建一个包含文本 "Hello World!" 的 PDF 文档。在您的环境中安装 Aspose.PDF for .NET 后，您可以执行以下代码示例以查看 Aspose.PDF API 的工作原理。

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

以下代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象。
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page)。
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/textfragment) 对象。
1. 将 TextFragment 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page/properties/paragraphs) 集合中。
1. [保存](https://reference.aspose.com/pdf/zh/net/aspose.pdf.document/save/methods/4) 生成的 PDF 文档。

以下代码片段是一个 Hello World 程序，用于展示 Aspose.PDF for .NET API 的工作。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```