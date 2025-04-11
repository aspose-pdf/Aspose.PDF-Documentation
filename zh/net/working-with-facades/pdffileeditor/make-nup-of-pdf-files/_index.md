---
title: 制作 PDF 文件的 NUp
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /zh/net/make-nup-of-pdf-files/
description: 本文展示了如何使用 PdfFileEditor 类与 Aspose.PDF Facades 一起制作 PDF 文件的 NUp。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "Aspose.PDF for .NET 中的 NUp 功能允许用户高效地将多个 PDF 文件合并为一个输出文档，定制页面大小和布局配置。此功能支持文件路径和流，能够灵活集成到各种工作流程中，同时增强文档展示",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发者的信息。"
}
</script>

## 使用文件路径制作 PDF 的 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的 NUp 并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作 NUp。以下代码片段展示了如何使用文件路径制作 NUP。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## 使用页面大小和文件路径制作 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的 NUp 并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作 NUp。您还可以使用此重载设置输出 PDF 文件的页面大小。以下代码片段展示了如何使用页面大小和文件路径制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## 使用页面大小、水平和垂直值以及文件路径制作 PDF 的 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的 NUp 并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作 NUp。您还可以使用此重载设置输出 PDF 文件的页面大小以及每个输出页面上的水平和垂直页面数量。以下代码片段展示了如何使用页面大小、水平和垂直值以及文件路径制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## 使用 PDF 文件数组和文件路径制作 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件数组的 NUp 并将其保存到单个输出 PDF 文件中。此重载允许您使用文件路径制作 NUp。以下代码片段展示了如何使用 PDF 文件数组和文件路径制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## 使用流制作 PDF 的 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的 NUp 并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作 NUp。以下代码片段展示了如何使用流制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## 使用页面大小和流制作 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的 NUp 并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作 NUp。您还可以使用此重载设置输出 PDF 流的页面大小。以下代码片段展示了如何使用页面大小和流制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## 使用页面大小、水平和垂直值以及流制作 PDF 的 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的 NUp 并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作 NUp。您还可以使用此重载设置输出 PDF 流的页面大小以及每个输出页面上的水平和垂直页面数量。以下代码片段展示了如何使用页面大小、水平和垂直值以及流制作 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## 使用 PDF 文件数组和流制作 NUp

[MakeNUp](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流数组的 NUp 并将其保存到单个输出 PDF 流中。此重载允许您使用流而不是文件路径制作 NUp。以下代码片段展示了如何使用流制作 PDF 文件数组的 NUp。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```