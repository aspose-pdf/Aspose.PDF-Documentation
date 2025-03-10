---
title: 从 PDF 中提取注释
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/extract-annotation/
description: 本节解释如何使用 Aspose.PDF Facades 从 PDF 文件提取注释到 XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "通过新的提取注释功能，释放您的 PDF 文档的潜力，该功能使得能够无缝地将注释提取到 XFDF 格式。此功能允许轻松检索特定类型的注释，提高文档管理和协作效率。了解如何通过轻松提取和保存重要的注释数据来简化您的 PDF 工作流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 方法允许您从 PDF 文件中提取注释。为了提取注释，您需要创建 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 对象并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定 PDF 文件。之后，您需要创建一个要从 PDF 文件中提取的注释类型的枚举。

然后，您可以使用 [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 方法将注释提取到 ArrayList 中。之后，您可以遍历此列表并获取单个注释。最后，使用 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段向您展示如何从 PDF 文件中提取注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```