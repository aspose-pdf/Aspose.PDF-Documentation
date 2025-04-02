---
title: 导入和导出注释到 XFDF
linktitle: 导入和导出注释到 XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/import-export-xfdf/
description: 您可以使用 C# 和 Aspose.PDF for .NET 库导入和导出 XFDF 格式的注释。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Effortless XFDF Annotation Import and Export",
    "abstract": "Aspose.PDF for .NET 库中新的 XFDF 导入和导出功能通过允许无缝传输注释数据来增强 PDF 文档管理。此功能使用户能够轻松地从 XFDF 文件中集成注释并将其导出，促进 PDF 表单的数据交换和归档能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Annotations, Export Annotations, XFDF Format, Aspose.PDF for .NET, PdfAnnotationEditor, ImportAnnotationFromXfdf, ExportAnnotationsXfdf, PDF Forms Manipulation",
    "wordcount": "670",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "您可以使用 C# 和 Aspose.PDF for .NET 库导入和导出 XFDF 格式的注释。"
}
</script>

{{% alert color="primary" %}}

XFDF 代表 XML 表单数据格式。它是一种基于 XML 的文件格式。此文件格式用于表示 PDF 表单中包含的表单数据或注释。XFDF 可用于许多不同的目的，但在我们的案例中，它可以用于将表单数据或注释发送或接收至其他计算机或服务器等，或者可以用于归档表单数据或注释。在本文中，我们将看到 Aspose.Pdf.Facades 如何考虑这一概念，以及我们如何将注释数据导入和导出到 XFDF 文件。

{{% /alert %}}

**Aspose.PDF for .NET** 是一个功能丰富的组件，用于编辑 PDF 文档。正如我们所知，XFDF 是 PDF 表单操作的重要方面，Aspose.PDF for .NET 中的 Aspose.Pdf.Facades 命名空间对此进行了很好的考虑，并提供了将注释数据导入和导出到 XFDF 文件的方法。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 类包含两个方法，用于处理注释的导入和导出到 XFDF 文件。[ExportAnnotationsXfdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 方法提供了将注释从 PDF 文档导出到 XFDF 文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 方法允许您从现有的 XFDF 文件导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以以枚举的形式指定这些类型，然后将此枚举作为参数传递给这些方法中的任何一个。这样，只有指定类型的注释才会被导入或导出到 XFDF 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下代码片段向您展示了如何将注释导出到 XFDF 文件：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAnnotationsToXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationDemo1.pdf");

        // Define the annotation types to export
        var annotType = new Aspose.Pdf.Annotations.AnnotationType[] { Aspose.Pdf.Annotations.AnnotationType.Line, Aspose.Pdf.Annotations.AnnotationType.Square };

        // Export annotations to XFDF file
        using (var fileStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
        }
    }
}
```

下一个代码片段描述了如何从 XFDF 文件导入注释：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Define the export file name
            var exportFileName = dataDir + "exportannotations.xfdf";

            // Import annotations from the XFDF file
            annotationEditor.ImportAnnotationsFromXfdf(exportFileName);

            // Save PDF document
            document.Save(dataDir + "ImportAnnotationFromXfdf_out.pdf");
        }
    }
}
```

## 另一种一次性导出/导入注释的方法

在下面的代码中，ImportAnnotations 方法允许直接从另一个 PDF 文档导入注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var documentFrom = new Aspose.Pdf.Document(dataDir + "some_doc.pdf"))
    {
        // Create PDF document
        using (var documentTo = new Aspose.Pdf.Document())
        {
            // Add page
            var page = documentTo.Pages.Add();

            // Export/import
            using (var ms = new MemoryStream())
            {
                documentFrom.ExportAnnotationsToXfdf(ms);
                documentTo.ImportAnnotationsFromXfdf(ms);
            }

            // Save PDF document
            documentTo.Save(dataDir + "AnnotationDemo3_out.pdf");
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>