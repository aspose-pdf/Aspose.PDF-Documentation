---
title: 将页面添加到PDF文档
linktitle: 添加页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/add-pages/
description: 探索如何在.NET中使用Aspose.PDF向现有PDF添加页面，以增强和扩展您的文档。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "Aspose.PDF for .NET中的功能允许用户轻松地在指定位置将页面插入PDF文档，从而增强文档的灵活性和组织性。此功能不仅支持添加页面，还包括使用C#移动或删除现有页面的选项。通过这一直观的功能简化您的PDF管理，增强您的开发工具包",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "本文教您如何在所需位置插入（添加）页面到PDF文件。了解如何使用C#移动、删除（删除）PDF文件中的页面。"
}
</script>

Aspose.PDF for .NET API提供了使用C#或其他任何.NET语言处理PDF文档中页面的完全灵活性。它在[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)中维护PDF文档的所有页面，可以用于处理PDF页面。
Aspose.PDF for .NET允许您在文件的任何位置向PDF文档插入页面，以及将页面添加到PDF文件的末尾。
本节展示了如何使用C#向PDF添加页面。

## 在PDF文件中添加或插入页面

Aspose.PDF for .NET允许您在文件的任何位置向PDF文档插入页面，以及将页面添加到PDF文件的末尾。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

### 在所需位置的PDF文件中插入空白页面

要在PDF文件中插入空白页面：

1. 创建一个带有输入PDF文件的[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类对象。
1. 调用[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)集合的[Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert)方法，并指定索引。
1. 使用[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)方法保存输出PDF。

以下代码片段展示了如何在PDF文件中插入页面。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

在上面的示例中，我们使用默认参数添加了空白页面。如果您需要使页面大小与文档中的另一个页面相同，您应该添加几行代码：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### 在PDF文件末尾添加空白页面

有时，您希望确保文档以空白页面结束。此主题解释了如何在PDF文档末尾插入空白页面。

要在PDF文件末尾插入空白页面：

1. 创建一个带有输入PDF文件的[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)类对象。
1. 调用[PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)集合的[Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)方法，不带任何参数。
1. 使用[Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)方法保存输出PDF。

以下代码片段展示了如何在PDF文件末尾插入空白页面。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>