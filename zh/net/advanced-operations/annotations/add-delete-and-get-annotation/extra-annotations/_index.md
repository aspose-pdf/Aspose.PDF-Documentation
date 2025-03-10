---
title: 使用 C# 的额外注释
linktitle: 额外注释
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /zh/net/extra-annotations/
description: 了解如何使用 Aspose.PDF 在 .NET 中向 PDF 文件添加额外注释，以实现交互式文档功能。
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "Enhance PDF Annotations with C#",
    "abstract": "介绍 C# 中的额外注释功能，使开发人员能够无缝地添加、检索和删除 PDF 文档中的各种注释。这一强大的功能通过实现精确的文本编辑和文档操作来增强 PDF 交互，包括有效添加插入符和编辑注释的能力。利用这些为直观文档管理而设计的高级功能来优化您的 PDF 处理。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extra Annotations, Caret Annotation, PDF document manipulation, Aspose.PDF for .NET, Redaction Annotation, Markup annotation, Delete Caret Annotation, Get Caret Annotation, StrikeOutAnnotation, PdfAnnotationEditor",
    "wordcount": "929",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "本节描述如何从 PDF 文档中添加、获取和删除额外类型的注释。"
}
</script>

## 如何将插入符注释添加到现有 PDF 文件中

插入符注释是指示文本编辑的符号。插入符注释也是标记注释，因此插入符类派生自标记类，并提供获取或设置插入符注释属性以及重置插入符注释外观流的功能。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

创建插入符注释的步骤：

1. 加载 PDF 文件 - new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)。
1. 创建新的 [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) 并设置插入符参数（new Rectangle, title, Subject, Flags, color, width, StartingStyle 和 EndingStyle）。此注释用于指示文本的插入。
1. 创建新的 [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) 并设置插入符参数（new Rectangle, title, Subject, Flags, color, width, StartingStyle 和 EndingStyle）。此注释用于指示文本的替换。
1. 创建新的 [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) 并设置参数（new Rectangle, title, color, new QuadPoints 和 new points, Subject, InReplyTo, ReplyType）。
1. 然后我们可以将注释添加到页面。

以下代码片段演示如何将插入符注释添加到 PDF 文件中：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCaretAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create Caret Annotation for text insertion
        var caretAnnotation1 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(299.988, 713.664, 308.708, 720.769))
        {
            Title = "Aspose User",
            Subject = "Inserted text 1",
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Color = Aspose.Pdf.Color.Blue
        };

        // Create Caret Annotation for text replacement
        var caretAnnotation2 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(361.246, 727.908, 370.081, 735.107))
        {
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Subject = "Inserted text 2",
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        // Create StrikeOut Annotation
        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1],
            new Rectangle(318.407, 727.826, 368.916, 740.098))
        {
            Color = Aspose.Pdf.Color.Blue,
            QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
            Subject = "Cross-out",
            InReplyTo = caretAnnotation2,
            ReplyType = Aspose.Pdf.Annotations.ReplyType.Group
        };

        document.Pages[1].Annotations.Add(caretAnnotation1);
        document.Pages[1].Annotations.Add(caretAnnotation2);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCaretAnnotations_out.pdf");
    }
}
```

### 获取插入符注释

请尝试使用以下代码片段在 PDF 文档中获取插入符注释：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Iterate through the annotations and print their details
        foreach (var ca in caretAnnotations)
        {
            Console.WriteLine($"{ca.Rect}");
        }
    }
}
```

### 删除插入符注释

以下代码片段演示如何从 PDF 文件中删除插入符注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Delete each Caret annotation
        foreach (var ca in caretAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document after deleting annotations
        document.Save(dataDir + "DeleteCaretAnnotation_out.pdf");
    }
}
```

## 使用 Aspose.PDF for .NET 的编辑注释对特定页面区域进行编辑

Aspose.PDF for .NET 支持在现有 PDF 文件中添加和操作注释的功能。最近，我们的一些客户提出了需要对 PDF 文档的特定页面区域进行编辑（删除文本、图像等元素）。为了满足这一要求，提供了一个名为 RedactionAnnotation 的类，可以用于编辑特定页面区域，或者可以用于操作现有的 RedactionAnnotations 并对其进行编辑（即扁平化注释并删除其下方的文本）。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RedactionAnnotation instance for a specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
        annot.FillColor = Aspose.Pdf.Color.Green;
        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;

        // Text to be printed on the redact annotation
        annot.OverlayText = "REDACTED";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;

        // Repeat Overlay text over the redact Annotation
        annot.Repeat = true;

        // Add annotation to the annotations collection of the first page
        document.Pages[1].Annotations.Add(annot);

        // Flattens annotation and redacts page contents (i.e., removes text and image under the redacted annotation)
        annot.Redact();

        // Save the result document
        document.Save(dataDir + "RedactPage_out.pdf");
    }
}
```

### 外观方法

Aspose.Pdf.Facades 命名空间中还有一个名为 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 的类，提供了在 PDF 文件中操作现有注释的功能。该类包含一个名为 [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) 的方法，提供了删除特定页面区域的能力。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPageWithFacadesApproach()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Redact a specific page region
        editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);

        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");

        // Save the result document
        editor.Save(dataDir + "FacadesApproach_out.pdf");
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