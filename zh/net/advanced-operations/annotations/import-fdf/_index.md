---
title: 通过 C# 导入 FDF 格式注释到 PDF
linktitle: 通过 C# 导入 FDF 格式注释到 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/import-fdf/
description: 使用现有的 Form.ImportFdf() 或 PdfAnnotationEditor.ImportAnnotationsFromFdf() 方法将 FDF 格式注释导入 PDF，使用 Aspose.PDF for .NET。
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "使用 Aspose.PDF for .NET 无缝导入 FDF 格式注释到 PDF 文件，增强您的 PDF 管理能力。通过 Form.ImportFdf() 和 PdfAnnotationEditor.ImportAnnotationsFromFdf() 方法，您可以轻松将轻量级 FDF 文件中的表单数据和注释集成到 PDF 文档中，简化数据提交和注释过程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发者的信息。"
}
</script>

{{% alert color="primary" %}}

FDF（表单数据格式）是一种文件格式，用于存储和传输 PDF 文档中的表单数据和注释。它是一个轻量级的 PDF 版本，仅包含表单字段值或注释，而不包含原始 PDF 文件的完整内容。FDF 文件通常在向服务器提交表单数据时使用，或在无需发送整个 PDF 文件的情况下交换注释。它们可以导入回 PDF 中以填写表单字段或应用注释。

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/) 类包含用于处理从 FDF 文件导入注释的方法。[PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) 方法提供了将注释从 FDF 文档导入到 PDF 文件的功能。

此外，[Class Form](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form/) 包含 [Form.ImportFdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form/importfdf/) 方法 - 从 FDF 文件导入字段内容并将其放入新的 PDF 中。

以下代码片段演示了如何使用 Form.ImportFdf() 方法将 FDF 格式注释导入 PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFDFByForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form(dataDir + "input.pdf"))
    {
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }
        // Save PDF document
        form.Save(dataDir + "ImportDataFromPdf_Form_out.pdf");
    }
}
```

下一个代码片段演示了如何使用 PdfAnnotationEditor.ImportAnnotationsFromFdf() 方法将 FDF 格式注释导入 PDF：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFdfByPdfAnnotationEditor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");
        editor.ImportAnnotationsFromFdf(dataDir + "student.fdf");
        // Save PDF document
        editor.Save(dataDir + "ImportDataFromPdf_AnnotationEditor_out.pdf");  
    }
}
```