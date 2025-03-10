---
title: 在PDF文件中更改页面尺寸
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/changing-page-sizes-in-a-pdf-file/
description: 尝试使用 PdfPageEditor 类学习如何更改 PDF 文件中的页面尺寸.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Changing page sizes in PDF file",
    "alternativeHeadline": "Effortlessly Adjust PDF Page Sizes with PdfPageEditor",
    "abstract": "Aspose.Pdf 中的 PdfPageEditor 类的功能允许用户轻松更改 PDF 文件中单个或多个页面的页面大小。通过利用 PageSize 属性和 Pages 属性，用户可以从各种预定义的页面大小中进行选择并有效应用，从而增强 PDF 文档布局的灵活性和自定义性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "197",
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
    "url": "/net/changing-page-sizes-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-page-sizes-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF不仅可以执行简单易行的任务，还能应对更复杂的目标。请查看下一部分以获取高级用户和开发者的信息。"
}
</script>

## 实现细节

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类在 [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) 中包含一个名为 [PageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagesize) 的属性，该属性可用于更改单个页面或多个页面的页面尺寸。Pages 属性可用于指定需要应用新页面尺寸的页面号码。PageSize 类包含一个不同页面尺寸的列表，作为其成员。该类的任何成员都可以分配给 [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类的 PageSize 属性。您还可以使用 GetPageSize 方法并传递页面号码来获取任意页面的页面尺寸。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePdfPageSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfPageEditor object
    using (var pdfPageEditor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        // Change page size of the selected pages
        pdfPageEditor.ProcessPages = new[] { 1 };

        // Select a predefined page size (LETTER) and assign it
        pdfPageEditor.PageSize = Aspose.Pdf.PageSize.PageLetter;

        // Save the file with the updated page size
        pdfPageEditor.Save(dataDir + "ChangePageSizes_out.pdf");

        // Get and display the page size assigned
        pdfPageEditor.BindPdf(dataDir + "FilledForm.pdf");

        var pageSize = pdfPageEditor.GetPageSize(1);
        Console.WriteLine($"Width: {pageSize.Width}, Height: {pageSize.Height}");
    }
}
```