---
title: 导入和导出注释到 XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/import-export-annotations/
description: 本节解释如何使用 Aspose.PDF Facades 从 PDF 文件导入和导出注释到 XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Import and Export PDF Annotations with XFDF",
    "abstract": "Aspose.PDF for .NET 引入了一种强大的功能，用于将注释导入和导出到 XFDF，增强了 PDF 操作能力。此功能允许用户选择性地以 XML 表单数据格式传输注释数据，实现无缝集成和归档，以便更好地管理文档。通过专门的方法指定注释类型，用户可以高效地精确管理其 PDF 注释。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/import-export-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

XFDF 代表 XML 表单数据格式。它是一种基于 XML 的文件格式。该文件格式用于表示 PDF 表单中包含的表单数据或注释。XFDF 可以用于许多不同的目的，但在我们的案例中，它可以用于将表单数据或注释发送或接收至其他计算机或服务器等，或者可以用于归档表单数据或注释。在本文中，我们将看到 Aspose.Pdf.Facades 如何考虑这一概念，以及我们如何将注释数据导入和导出到 XFDF 文件。

## 导入和导出注释到 XFDF

[Aspose.PDF for .NET](/pdf/net/) 是一个功能丰富的组件，涉及 PDF 文档的编辑。正如我们所知，XFDF 是 PDF 表单操作的重要方面，[Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 在 [Aspose.PDF for .NET](/pdf/net/) 中对此进行了很好的考虑，并提供了将注释数据导入和导出到 XFDF 文件的方法。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 类包含两个方法，用于处理注释的导入和导出到 XFDF 文件。[ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 方法提供了将注释从 PDF 文档导出到 XFDF 文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 方法允许您从现有的 XFDF 文件导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以以枚举的形式指定这些类型，然后将该枚举作为参数传递给这些方法中的任何一个。这样，只有指定类型的注释才会被导入或导出到 XFDF 文件。

以下代码片段展示了如何将注释导入到 XFDF 文件：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Sources of PDF with annotations           
    var sources = new string[] { dataDir + "ImportAnnotations.pdf" };
            
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "input.pdf");
        annotationEditor.ImportAnnotations(sources);
        // Save PDF document
        annotationEditor.Save(dataDir + "ImportAnnotations_out.pdf");
    }
}
```

下一个代码片段描述了如何将注释导入/导出到 XFDF 文件：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
        }

        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "exportannotations_out.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_out.pdf");
        }
    }
}
```

这样，只有指定类型的注释才会被导入或导出到 XFDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportExportXFDF02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "ExportAnnotations.pdf");

        // Export annotations
        using (FileStream xmlOutputStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            var annotationTypes = new[] {AnnotationType.FreeText, AnnotationType.Text};
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 1, 5, annotationTypes);
        }

        // Import annotations
        using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
        {
            // Add page
            document.Pages.Add();
            // Bind PDF document
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(File.OpenRead(dataDir + "annotations.xfdf"));
            // Save PDF document
            annotationEditor.Save(dataDir + "ImportedAnnotation_XFDF02_out.pdf");
        }
    }
}
```