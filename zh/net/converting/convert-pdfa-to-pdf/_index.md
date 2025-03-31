---
title: 将 PDF/A 转换为 PDF 格式
linktitle: 将 PDF/A 转换为 PDF 格式
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /zh/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF/A 文件转换为 PDF 文档，使用 .NET 库。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF/A to PDF format",
    "alternativeHeadline": "Remove PDF/A Compliance for Enhanced Document Flexibility in C#",
    "abstract": "Aspose.PDF 现在提供了一项功能，可以使用其 .NET 库无缝地将 PDF/A 文件转换为标准 PDF 文档。此功能允许用户去除 PDF/A 合规性限制，从而更轻松地编辑和修改 PDF 内容，而不受 PDF/A 标准的限制。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/convert-pdfa-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdfa-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 将 PDF/A 文档转换为 PDF

将 PDF/A 文档转换为 PDF 意味着从原始文档中去除 <abbr title="可移植文档格式档案">PDF/A</abbr> 限制。 
类 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 具有方法 [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/removepdfacompliance) 用于从输入/源文件中删除 PDF 合规性信息。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Remove PDF/A compliance information
        document.RemovePdfaCompliance();
    
        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Remove PDF/A compliance information
    document.RemovePdfaCompliance();
    
    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

如果您在文档中进行任何更改（例如添加页面），也可以去除 PDF/A 合规性。在以下示例中，输出文档在添加新页面后失去 PDF/A 合规性。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf"))
    {
        // Adding a new (empty) page removes PDF/A compliance information.
        document.Pages.Add();

        // Save PDF document
        document.Save(dataDir + "PDFAToPDF_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFAtoPDFAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "PDFAToPDF.pdf");

    // Adding a new (empty) page removes PDF/A compliance information.
    document.Pages.Add();

    // Save PDF document
    document.Save(dataDir + "PDFAToPDF_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}