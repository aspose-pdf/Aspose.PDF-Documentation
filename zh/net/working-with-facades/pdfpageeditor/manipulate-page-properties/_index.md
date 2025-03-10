---
title: 操作页面属性
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /zh/net/manipulate-page-properties/
description: 本节解释如何使用 PdfPageEditor 类操作 Aspose.PDF Facades 的页面属性。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Page Properties",
    "alternativeHeadline": "Enhance PDF Page Control with PdfPageEditor Features",
    "abstract": "介绍 PdfPageEdito 类，这是一个强大的工具，用于管理 PDF 页面属性与 2651603203208 Facades。此功能使开发人员能够检索和修改基本页面属性，如旋转、缩放级别和页面尺寸，从而提供对 PDF 内容呈现的精细控制。通过简单的方法获取和设置属性，包括调整特定页面内容的大小，增强 PDF 文档从未如此简单。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "483",
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
    "url": "/net/manipulate-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 从现有 PDF 文件获取 PDF 页面属性

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 允许您处理 PDF 文件的单个页面。它帮助您获取单个页面的属性，如不同的页面框大小、页面旋转、页面缩放等。为了获取这些属性，您需要创建 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 对象并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，您可以使用不同的方法获取页面属性，如 [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation)、[GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages)、[GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) 等。

以下代码片段演示了如何从现有 PDF 文件获取 PDF 页面属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Get page properties and print them to the console
        Console.WriteLine($"Page 1 Rotation: {pageEditor.GetPageRotation(1)}");
        Console.WriteLine($"Total Pages: {pageEditor.GetPages()}");
        Console.WriteLine($"Trim Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "trim")}");
        Console.WriteLine($"Art Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "art")}");
        Console.WriteLine($"Bleed Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "bleed")}");
        Console.WriteLine($"Crop Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "crop")}");
        Console.WriteLine($"Media Box Size of Page 1: {pageEditor.GetPageBoxSize(1, "media")}");
    }
}
```

## 在现有 PDF 文件中设置 PDF 页面属性

为了设置页面属性，如页面旋转、缩放或原点，您需要使用 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类。该类提供了不同的方法和属性来设置这些页面属性。首先，您需要创建 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，您可以使用这些方法和属性来设置页面属性。最后，使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。

以下代码片段演示了如何在现有 PDF 文件中设置 PDF 页面属性。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var pageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pageEditor.BindPdf(dataDir + "input.pdf");

        // Set page properties
        // Move origin from (0,0)
        pageEditor.MovePosition(100, 100);

        // Set page rotations
        var pageRotations = new System.Collections.Hashtable
        {
            { 1, 90 },
            { 2, 180 },
            { 3, 270 }
        };

        // Set zoom where 1.0f = 100% zoom
        pageEditor.Zoom = 2.0f;

        // Save PDF document
        pageEditor.Save(dataDir + "SetPageProperties_out.pdf");
    }
}
```

## 调整 PDF 文件中特定页面的内容大小

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类的 ResizeContents 方法允许您调整 PDF 文件中页面内容的大小。[ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) 类用于指定用于调整页面大小的参数，例如百分比或单位等的边距。您可以调整所有页面的大小，或使用 ResizeContents 方法指定要调整大小的页面数组。

以下代码片段演示了如何调整 PDF 文件中特定页面的内容大小。

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void ResizePdfPageContents()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create PdfFileEditor Object
     var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

     // Open PDF Document
     using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
     {
         // Specify Parameters to be used for resizing
         var parameters = new Aspose.Pdf.Facades.PdfFileEditor.ContentsResizeParameters(
             // Left margin = 10% of page width
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents width calculated automatically as width - left margin - right margin (100% - 10% - 10% = 80%)
             null,
             // Right margin is 10% of page
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // Top margin = 10% of height
             PdfFileEditor.ContentsResizeValue.Percents(10),
             // New contents height is calculated automatically (similar to width)
             null,
             // Bottom margin is 10%
             PdfFileEditor.ContentsResizeValue.Percents(10)
         );

         // Resize Page Contents
         fileEditor.ResizeContents(document, new[] { 1, 2 }, parameters);

         // Save PDF document
         document.Save(dataDir + "ResizePageContents_out.pdf");
     }
 }
```