---
title: 设置 PDF 文件信息
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/set-pdf-file-information/
description: 本节解释如何使用 Aspose.PDF Facades 设置 PDF 文件信息。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set PDF File Information",
    "alternativeHeadline": "Set Custom Metadata for PDF Files Effortlessly",
    "abstract": "通过 Aspose.PDF for .NET 中的新功能增强您的 PDF 文件管理，该功能允许您轻松设置和更新特定于文件的信息，例如作者、标题和关键字。利用 PdfFileInfo 类高效修改您的 PDF，添加有价值的元数据以改善组织和可搜索性。通过使用 SaveNewInfo 方法无缝保存这些更新来简化您的工作流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "251",
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
    "url": "/net/set-pdf-file-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-pdf-file-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

[PdfFileInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo) 类允许您设置 PDF 文件的特定信息。您需要创建一个 [PdfFileInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo) 类的对象，然后设置不同的文件特定属性，如作者、标题、关键字和创建者等。最后，使用 [PdfFileInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo) 对象的 [SaveNewInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) 方法保存更新后的 PDF 文件。

以下代码片段向您展示如何设置 PDF 文件信息。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPdfInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create PdfFileInfo object to work with PDF metadata
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set PDF information
        fileInfo.Author = "Aspose";
        fileInfo.Title = "Hello World!";
        fileInfo.Keywords = "Peace and Development";
        fileInfo.Creator = "Aspose";
        
        // Save the PDF with updated information
        fileInfo.SaveNewInfo(dataDir + "SetFileInfo_out.pdf");
    }
}
```

## 设置元信息

[SetMetaInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) 方法允许您添加任何信息。在我们的示例中，我们添加了一个字段。请查看下一个代码片段：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMetaInfo()
{
    // Define the directory for input and output files
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of the PdfFileInfo object
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample.pdf"))
    {
        // Set a new custom attribute as meta info
        fileInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

        // Save the updated file
        fileInfo.SaveNewInfo(dataDir + "SetMetaInfo_out.pdf");
    }
}
```