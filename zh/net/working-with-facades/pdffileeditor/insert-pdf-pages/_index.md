---
title: 插入 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/insert-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 插入 PDF 页面。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "通过新功能优化您的 PDF 管理，允许用户使用 Aspose.PDF for .NET PdfFileEditor 类将一个 PDF 中的特定页面插入到另一个 PDF 中。此功能支持基于范围和基于数组的页面插入，通过文件路径或流无缝结合文档，从而提高工作流程效率。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 使用文件路径在两个数字之间插入 PDF 页面

可以使用 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类的 [Insert](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 方法将特定范围的页面从一个 PDF 插入到另一个 PDF 中。为此，您需要一个输入 PDF 文件，您希望在其中插入页面，一个源文件，从中提取要插入的页面，一个要插入页面的位置，以及要插入到输入 PDF 文件中的源文件的页面范围。此范围通过起始页面和结束页面参数指定。最后，输出 PDF 文件将保存指定范围的页面插入到输入文件中。以下代码片段演示了如何使用文件流在两个数字之间插入 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## 使用文件路径插入 PDF 页面数组

如果您想将一些特定页面插入到另一个 PDF 文件中，则可以使用 [Insert](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 方法的一个重载，该重载需要一个整数数组来指定页面。在此数组中，您可以指定希望插入到输入 PDF 文件中的特定页面。为此，您需要一个输入 PDF 文件，您希望在其中插入页面，一个源文件，从中提取要插入的页面，一个要插入页面的位置，以及要插入到输入 PDF 文件中的源文件的页面的整数数组。此数组包含您希望插入到输入 PDF 文件中的特定页面列表。最后，输出 PDF 文件将保存指定的页面数组插入到输入文件中。以下代码片段演示了如何使用文件路径插入 PDF 页面数组。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## 使用流在两个数字之间插入 PDF 页面

如果您想使用流插入页面范围，只需使用 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类的 [Insert](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) 方法的适当重载。为此，您需要一个输入 PDF 流，您希望在其中插入页面，一个源流，从中提取要插入的页面，一个要插入页面的位置，以及要插入到输入 PDF 流中的源流的页面范围。此范围通过起始页面和结束页面参数指定。最后，输出 PDF 流将保存指定范围的页面插入到输入流中。以下代码片段演示了如何使用流在两个数字之间插入 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## 使用流插入 PDF 页面数组

您还可以使用流将页面数组插入到另一个 PDF 文件中，方法是使用需要整数数组的 Insert 方法的适当重载。在此数组中，您可以指定希望插入到输入 PDF 流中的特定页面。为此，您需要一个输入 PDF 流，您希望在其中插入页面，一个源流，从中提取要插入的页面，一个要插入页面的位置，以及要插入到输入 PDF 文件中的源流的页面的整数数组。此数组包含您希望插入到输入 PDF 流中的特定页面列表。最后，输出 PDF 流将保存指定的页面数组插入到输入文件中。以下代码片段演示了如何使用流插入 PDF 页面数组。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```