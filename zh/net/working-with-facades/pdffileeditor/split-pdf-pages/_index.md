---
title: 拆分 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/split-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类拆分 PDF 页面。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "Aspose.PDF for .NET 中的新拆分 PDF 页面功能允许用户使用 PdfFileEditor 类高效地将 PDF 文档分割成多个部分。此功能支持从第一页拆分到指定页面、拆分成多个批次，甚至隔离单个页面，所有这些都可以通过文件路径或流提供多种 PDF 操作选项。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 从第一页开始使用文件路径拆分 PDF 页面

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您从第一页开始拆分 PDF 文件，并在指定页面号结束。如果您想从磁盘操作 PDF 文件，可以将输入和输出 PDF 文件的文件路径传递给此方法。以下代码片段演示了如何使用文件路径从第一页开始拆分 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## 从第一页开始使用文件流拆分 PDF 页面

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您从第一页开始拆分 PDF 文件，并在指定页面号结束。如果您想通过流操作 PDF 文件，可以将输入和输出 PDF 流传递给此方法。以下代码片段演示了如何使用文件流从第一页开始拆分 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## 使用文件路径拆分 PDF 页面到多个批次

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您将 PDF 文件拆分为多个页面集。在此示例中，我们需要两个页面集 (1, 2) 和 (5, 6)。如果您想从磁盘访问 PDF 文件，则需要将输入 PDF 作为文件路径传递。此方法返回一个 MemoryStream 数组。您可以遍历此数组并将每个页面集保存为单独的文件。以下代码片段演示了如何使用文件路径将 PDF 页面拆分为多个批次。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## 使用流拆分 PDF 页面到多个批次

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您将 PDF 文件拆分为多个页面集。在此示例中，我们需要两个页面集 (1, 2) 和 (5, 6)。您可以将流传递给此方法，而不是从磁盘访问文件。此方法返回一个 MemoryStream 数组。您可以遍历此数组并将每个页面集保存为单独的文件。以下代码片段演示了如何使用流将 PDF 页面拆分为多个批次。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## 使用文件路径拆分 PDF 页面到末尾

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您从指定页面号拆分 PDF 到 PDF 文件的末尾，并将其保存为新的 PDF。为此，使用文件路径，您需要传递输入和输出文件路径以及拆分开始的页面号。输出 PDF 将保存到磁盘。以下代码片段演示了如何使用文件路径将 PDF 页面拆分到末尾。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## 使用流拆分 PDF 页面到末尾

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) 类允许您从指定页面号拆分 PDF 到 PDF 文件的末尾，并将其保存为新的 PDF。为此，使用流，您需要传递输入和输出流以及拆分开始的页面号。输出 PDF 将保存到输出流。以下代码片段演示了如何使用流将 PDF 页面拆分到末尾。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## 使用文件路径拆分 PDF 到单独页面

{{% alert color="primary" %}}

您可以尝试拆分 PDF 文档并在线查看结果，链接如下：

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

为了将 PDF 文件拆分为单独的页面，您需要将 PDF 作为文件路径传递给 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittopages/index) 方法。此方法将返回一个包含 PDF 文件单独页面的 MemoryStream 数组。您可以遍历此 MemoryStream 数组并将单独的页面保存为单独的 PDF 文件到磁盘。以下代码片段演示了如何使用文件路径将 PDF 拆分为单独页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## 使用流拆分 PDF 到单独页面

为了将 PDF 文件拆分为单独的页面，您需要将 PDF 作为流传递给 [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittopages/index) 方法。此方法将返回一个包含 PDF 文件单独页面的 MemoryStream 数组。您可以遍历此 MemoryStream 数组并将单独的页面保存为单独的 PDF 文件到磁盘，或者您可以将这些单独的页面保存在内存流中以便在应用程序中稍后使用。以下代码片段演示了如何使用流将 PDF 拆分为单独页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```