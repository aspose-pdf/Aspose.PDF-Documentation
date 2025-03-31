---
title: PDFからXFDFへの注釈のフラット化
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/flatten-annotation/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFに注釈をエクスポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Flatten Annotation from PDF to XFDF",
    "alternativeHeadline": "Export PDF Annotations as Non-Editable XFDF Format",
    "abstract": "PDFからXFDFへの注釈のフラット化機能により、ユーザーはPDFファイルからXFDF形式に注釈をエクスポートし、その視覚的表現を保持できます。この機能により、注釈は文書内で可視のままとなりますが、編集不可となり、注釈機能をサポートしていない視聴者のためにメモやコメントを永久に適用する方法を提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "191",
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
    "url": "/net/flatten-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/flatten-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーや開発者向けの情報を確認してください。"
}
</script>

フラット化プロセスとは、文書から注釈が削除されたときに、その視覚的表現が保持されることを意味します。フラット化された注釈は依然として可視ですが、ユーザーやアプリによって編集できなくなります。これは、たとえば、文書に注釈を永久に適用したり、注釈を表示できない視聴者に注釈を可視化したりするために使用できます。指定されていない場合、エクスポートはすべての注釈をそのまま保持します。

このオプションが選択されると、注釈はエクスポートされたPDFにPDF標準の注釈として含まれます。

次のコードスニペットで使用されている[flatteningAnnotations](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations)メソッドを確認してください。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Create FlattenSettings
        var flattenSettings = new Aspose.Pdf.Forms.Form.FlattenSettings
        {
            ApplyRedactions = true,
            CallEvents = false,
            HideButtons = true,
            UpdateAppearances = true
        };
        annotationEditor.FlatteningAnnotations(flattenSettings);
        // Save PDF document
        annotationEditor.Save(dataDir + "FlattenAnnotation_out.pdf");
    }
}
```