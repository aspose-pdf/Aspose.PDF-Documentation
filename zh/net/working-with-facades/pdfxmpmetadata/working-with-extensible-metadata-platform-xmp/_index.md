---
title: 可扩展元数据平台 - XMP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/working-with-extensible-metadata-platform-xmp/
description: 本节解释如何使用 PdfXmpMetadata 类处理可扩展元数据平台 - XMP。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extensible Metadata Platform - XMP",
    "alternativeHeadline": "Enhanced PDF Metadata Management with XMP Integration",
    "abstract": "可扩展元数据平台 (XMP) 功能允许用户高效地在 PDF 文件中嵌入和操作标准化和专有元数据。利用 PdfXmpMetadata 类，该功能简化了跟踪更改和增强 PDF 文档语义能力的过程，使其成为希望集成高级元数据管理的开发人员的宝贵工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "412",
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
    "url": "/net/working-with-extensible-metadata-platform-xmp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-extensible-metadata-platform-xmp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

可扩展元数据平台 (XMP) 是由 Adobe Systems Inc. 创建的标准。该标准旨在处理和存储标准化和专有元数据。这些元数据可以嵌入到不同的文件格式中，但在本文中我们将仅关注 PDF 文件格式。我们将看到如何使用 Aspose.Pdf.Facades 命名空间在 PDF 文件中嵌入元数据。我们将使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类来操作 PDF 文档中的 XMP。

{{% /alert %}}

## 背景

PDF 文件在其生命周期中经历多个阶段。我们创建一个 PDF 文档，然后将其传递给其他人或部门进行进一步处理。然而，在此过程中，我们需要跟踪所做更改的不同方面。XMP 旨在跟踪文件中数据的更改或其他信息。

## 解释

为了使用 Aspose.Pdf.Facades 操作 XMP，我们将使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类。我们将使用此类来操作预定义的元数据属性。[PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类将这些属性添加到 PDF 文件中。它还帮助打开和保存我们添加元数据的 PDF 文件。因此，使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类，我们可以轻松地在 PDF 文件中操作 XMP。
以下代码片段将帮助您理解如何使用 [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) 类来处理 XMP：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using (var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open))
    {
        using (var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create))
        {
            // Bind PDF document
            xmpMetaData.BindPdf(input);

            // Add base URL property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

            // Add creation date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

            // Add Metadata Date property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

            // Add Creator Tool property to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

            // Add Modify Date to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

            // Add Nick Name to xmp metadata
            xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

            // Save PDF document
            xmpMetaData.Save(output);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    // Create an object of PdfXmpMetadata class
    var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Create input and output file streams
    using var input = new FileStream(dataDir + "FilledForm.pdf", FileMode.Open);

    using var output = new FileStream(dataDir + "xmp_out.pdf", FileMode.Create);

    // Bind PDF document
    xmpMetaData.BindPdf(input);

    // Add base URL property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.BaseURL, "xmlns:pdf=http:// Ns.adobe.com/pdf/1.3/");

    // Add creation date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate, DateTime.Now.ToString());

    // Add Metadata Date property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate, DateTime.Now.ToString());

    // Add Creator Tool property to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool, "Creator Tool Name");

    // Add Modify Date to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.ModifyDate, DateTime.Now.ToString());

    // Add Nick Name to xmp metadata
    xmpMetaData.Add(Aspose.Pdf.Facades.DefaultMetadataProperties.Nickname, "Test");

    // Save PDF document
    xmpMetaData.Save(output);
}
```
{{< /tab >}}
{{< /tabs >}}

## 结论

{{% alert color="primary" %}}
在本文中，我们已经看到如何使用 Aspose.Pdf.Facades 处理 XMP。本文中使用的 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 使用户能够轻松操作 PDF 文档中的元数据。如果正确使用 [PdfXmpMetadata](http://www.aspose.com/docs/display/pdfnet/PdfXmpMetadata+Class) 类，将非常容易在 PDF 文件中融入智能，并使语义网更接近实现。
{{% /alert %}}