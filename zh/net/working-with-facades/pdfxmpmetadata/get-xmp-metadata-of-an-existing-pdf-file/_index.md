---
title: 获取 PDF 文件的 XMP 元数据
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/get-xmp-metadata-of-an-existing-pdf-file/
description: 本节解释如何使用 Aspose.PDF Facades 获取现有 PDF 的 XMP 元数据。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get XMP Metadata of PDF File",
    "alternativeHeadline": "Extract XMP Metadata from PDF Files Easily",
    "abstract": "通过 Aspose.PDF for .NET 中的新 XMP 元数据功能，从您的 PDF 文件中解锁详细见解。此功能使您能够轻松提取特定的 XMP 元数据属性，从而更好地管理和分类您的文档。简化您的工作流程，并通过精确的元数据提取增强 PDF 的实用性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "213",
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
    "url": "/net/get-xmp-metadata-of-an-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-xmp-metadata-of-an-existing-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发者的信息。"
}
</script>

为了从 PDF 文件中获取 XMP 元数据，您需要创建 [PdfXmpMetadata](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfxmpmetadata) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定 PDF 文件。您可以将特定的 XMP 元数据属性传递给 [PdfXmpMetadata](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfxmpmetadata) 对象以获取其值。以下代码片段向您展示了如何从 PDF 文件中获取 XMP 元数据。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using (var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata())
    {
        // Bind PDF document
        xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

        // Get XMP Meta Data properties
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
        Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
        Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

        Console.ReadLine();
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXmpMetadata()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

    // Create PdfXmpMetadata object
    using var xmpMetaData = new Aspose.Pdf.Facades.PdfXmpMetadata();

    // Bind PDF document
    xmpMetaData.BindPdf(dataDir + "GetXMPMetadata.pdf");

    // Get XMP Meta Data properties
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreateDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.MetadataDate].ToString());
    Console.WriteLine(": {0}", xmpMetaData[Aspose.Pdf.Facades.DefaultMetadataProperties.CreatorTool].ToString());
    Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

    Console.ReadLine();
}
```
{{< /tab >}}
{{< /tabs >}}