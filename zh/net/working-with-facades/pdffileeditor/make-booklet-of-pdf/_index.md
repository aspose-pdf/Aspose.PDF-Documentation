---
title: 制作 PDF 小册子
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /zh/net/make-booklet-of-pdf/
description: 本节解释如何使用 PdfFileEditor 类通过 Aspose.PDF 制作 PDF 小册子。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make Booklet of PDF",
    "alternativeHeadline": "Create Booklets from PDFs with Enhanced Flexibility",
    "abstract": "Aspose.PDF 中的制作 PDF 小册子功能允许用户使用 PdfFileEditor 类轻松地从 PDF 文件创建小册子。此功能支持文件路径和流，能够自定义页面大小并指定左右页面，以增强输出控制。这个强大的工具简化了小册子的制作过程，使其成为 PDF 操作的重要资源。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "946",
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
    "url": "/net/make-booklet-of-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-booklet-of-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还能应对更复杂的目标。请查看下一节以获取高级用户和开发者的信息。"
}
</script>

## 使用文件路径制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的小册子并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作小册子。以下代码片段演示了如何使用文件路径制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
}
```

## 使用页面大小和文件路径制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的小册子并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作小册子。您还可以使用此重载设置输出 PDF 文件的页面大小。以下代码片段演示了如何使用页面大小和文件路径制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPageSizeAndPaths_out.pdf", PageSize.A5);
}
```

## 使用页面大小、指定的左右页面和文件路径制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的小册子并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作小册子。您还可以使用此重载设置输出 PDF 文件的页面大小，并为输出 PDF 文件的左右两侧指定特定页面。以下代码片段演示了如何使用页面大小、指定的左右页面和文件路径制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", PageSize.A5, leftPages, rightPages);
}
```

## 使用指定的左右页面和文件路径制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 文件的小册子并将其保存到输出 PDF 文件中。此重载允许您使用文件路径制作小册子。您还可以使用此重载为输出 PDF 文件的左右两侧指定特定页面。以下代码片段演示了如何使用指定的左右页面和文件路径制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Set left and right pages
    var leftPages = new int[] { 1, 5 };
    var rightPages = new int[] { 2, 3 };
    // Make booklet
    pdfEditor.MakeBooklet(dataDir + "MakeBookletMultiplePagesInput.pdf", dataDir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf", leftPages, rightPages);
}
```

## 使用流制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的小册子并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作小册子。以下代码片段演示了如何使用流制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream);
        }
    }
}
```

## 使用页面大小和流制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的小册子并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作小册子。您还可以使用此重载设置输出 PDF 流的页面大小。以下代码片段演示了如何使用页面大小和流制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5);
        }
    }
}
```

## 使用页面大小、指定的左右页面和流制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的小册子并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作小册子。您还可以使用此重载设置输出 PDF 文件的页面大小，并为输出 PDF 流的左右两侧指定特定页面。以下代码片段演示了如何使用页面大小、指定的左右页面和流制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, PageSize.A5, leftPages, rightPages);
        }
    }
}
```

## 使用指定的左右页面和流制作 PDF 小册子

[MakeBooklet](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makebooklet/index) 方法的 [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类允许您制作输入 PDF 流的小册子并将其保存到输出 PDF 流中。此重载允许您使用流而不是文件路径制作小册子。您还可以使用此重载为输出 PDF 流的左右两侧指定特定页面。以下代码片段演示了如何使用指定的左右页面和流制作小册子。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeBookletMultiplePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", FileMode.Create))
        {
            // Set left and right pages
            var leftPages = new int[] { 1, 5 };
            var rightPages = new int[] { 2, 3 };
            // Make booklet
            pdfEditor.MakeBooklet(inputStream, outputStream, leftPages, rightPages);
        }
    }
}
```