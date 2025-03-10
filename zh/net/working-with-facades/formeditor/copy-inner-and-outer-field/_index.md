---
title: 复制内部和外部字段
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/copy-inner-and-outer-field/
description: 本节解释如何使用 FormEditor 类复制 Aspose.PDF Facades 中的内部和外部字段。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "Aspose.PDF for .NET 中的复制内部和外部字段功能通过允许用户在同一 PDF 中复制字段或从外部 PDF 文件转移字段来增强表单编辑。通过 FormEditor 类提供的易于使用的 CopyInnerField 和 CopyOuterField 方法，用户可以高效管理表单字段，确保一致性并节省文档准备时间。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) 方法允许您在同一文件中、在指定页面的相同坐标处复制字段。此方法需要您要复制的字段名称、新字段名称以及需要复制字段的页面编号。[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供了此方法。以下代码片段向您展示如何在同一文件的相同位置复制字段。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## 在现有 PDF 文件中复制外部字段

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) 方法允许您从外部 PDF 文件复制表单字段，然后将其添加到输入 PDF 文件的相同位置和指定页面编号。此方法需要从中复制字段的 PDF 文件、字段名称以及需要复制字段的页面编号。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段向您展示如何从外部 PDF 文件复制字段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```