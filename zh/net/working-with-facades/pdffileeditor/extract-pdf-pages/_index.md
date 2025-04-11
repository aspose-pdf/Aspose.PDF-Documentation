---
title: 提取 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/extract-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类提取 PDF 页面。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "提取 PDF 页面功能在 Aspose.PDF for .NET Facades 中为用户提供了增强的能力，可以选择性地从 PDF 文档中提取页面。通过利用 PdfFileEditor 类，用户可以通过文件路径或流高效地提取指定范围或一组页面，使文档操作更加简化和灵活。此功能对于希望在不更改原始文件的情况下自定义 PDF 内容的用户特别有益。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 使用文件路径提取两个数字之间的 PDF 页面

[Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您从 PDF 文件中提取指定范围的页面。此重载允许您在操作磁盘上的 PDF 文件时提取页面。此重载需要以下参数：输入文件路径、起始页面、结束页面和输出文件路径。从起始页面到结束页面的页面将被提取，输出将保存在磁盘上。以下代码片段演示了如何使用文件路径提取两个数字之间的 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## 使用文件路径提取 PDF 页面数组

如果您不想提取一系列页面，而是特定页面的集合，[Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法也允许您这样做。您首先需要创建一个包含所有需要提取的页面编号的整数数组。此重载的 [Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法需要以下参数：输入 PDF 文件、要提取的页面的整数数组和输出 PDF 文件。以下代码片段演示了如何使用文件路径提取 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## 使用流提取两个数字之间的 PDF 页面

[Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您使用流提取一系列页面。您需要将以下参数传递给此重载：输入流、起始页面、结束页面和输出流。从输入流中提取的页面将根据起始页面和结束页面之间的范围进行提取，并保存到输出流中。以下代码片段演示了如何使用流提取两个数字之间的 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## 使用流提取 PDF 页面数组

可以从 PDF 流中提取页面数组，并使用适当的 [Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法重载将其保存到输出流中。如果您不想提取一系列页面，而是特定页面的集合，[Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法也允许您这样做。您首先需要创建一个包含所有需要提取的页面编号的整数数组。此重载的 [Extract](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) 方法需要以下参数：输入流、要提取的页面的整数数组和输出流。以下代码片段演示了如何使用流提取 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```