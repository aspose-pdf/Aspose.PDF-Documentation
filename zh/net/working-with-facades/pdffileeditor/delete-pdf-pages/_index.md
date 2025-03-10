---
title: 删除 PDF 页面
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/delete-pdf-pages/
description: 本节解释如何使用 PdfFileEditor 类通过 Aspose.PDF Facades 删除 PDF 页面。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete PDF pages",
    "alternativeHeadline": "Effortlessly Remove Pages from PDF Files",
    "abstract": "轻松使用 Aspose.PDF for .NET Facades 删除 PDF 文档中的特定页面。通过利用 PdfFileEditor 类，您可以从文件路径和流中删除不需要的页面，从而精确控制最终输出，简化 PDF 编辑过程。通过此高效的页面删除功能增强您的文档管理能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "262",
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
    "url": "/net/delete-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

如果您想从位于磁盘上的 PDF 文件中删除多个页面，则可以使用 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 方法的重载，该方法接受以下三个参数：输入文件路径、要删除的页面编号数组和输出 PDF 文件路径。第二个参数是一个整数数组，表示需要删除的所有页面。指定的页面将从输入文件中删除，结果将保存为输出文件。以下代码片段演示了如何使用文件路径删除 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## 使用流删除 PDF 页面

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) 类的 [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) 方法还提供了一个重载，允许您在输入和输出文件都在流中的情况下，从输入 PDF 文件中删除页面。此重载接受以下三个参数：输入流、要删除的 PDF 页面整数数组和输出流。以下代码片段演示了如何使用流删除 PDF 页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```