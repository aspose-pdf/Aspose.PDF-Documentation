---
title: C#を使用した追加注釈
linktitle: 追加注釈
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ja/net/extra-annotations/
description: Aspose.PDFを使用して.NETでPDFファイルに追加の注釈を追加する方法を学びます。
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
    "abstract": "C#の追加注釈機能を紹介します。これにより、開発者はPDFドキュメントからさまざまな注釈をシームレスに追加、取得、削除できます。この堅牢な機能は、正確なテキスト編集とドキュメント操作を可能にし、キャレットおよび削除注釈を効果的に追加する能力を含むことで、PDFのインタラクションを強化します。直感的なドキュメント管理のために設計されたこれらの高度な機能を使用して、PDFの取り扱いを最適化してください。",
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
    "description": "このセクションでは、PDFドキュメントから追加の種類の注釈を追加、取得、削除する方法について説明します。"
}
</script>

## 既存のPDFファイルにキャレット注釈を追加する方法

キャレット注釈は、テキスト編集を示す記号です。キャレット注釈はマークアップ注釈でもあるため、キャレットクラスはマークアップクラスから派生し、キャレット注釈のプロパティを取得または設定する機能を提供し、キャレット注釈の外観の流れをリセットします。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

キャレット注釈を作成する手順：

1. PDFファイルをロードします - 新しい [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)。
1. 新しい [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation)を作成し、キャレットパラメータ（新しいRectangle、タイトル、件名、フラグ、色、幅、StartingStyleおよびEndingStyle）を設定します。この注釈は、テキストの挿入を示すために使用されます。
1. 新しい [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation)を作成し、キャレットパラメータ（新しいRectangle、タイトル、件名、フラグ、色、幅、StartingStyleおよびEndingStyle）を設定します。この注釈は、テキストの置き換えを示すために使用されます。
1. 新しい [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation)を作成し、パラメータ（新しいRectangle、タイトル、色、新しいQuadPointsおよび新しいポイント、件名、InReplyTo、ReplyType）を設定します。
1. その後、ページに注釈を追加できます。

次のコードスニペットは、PDFファイルにキャレット注釈を追加する方法を示しています：

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

### キャレット注釈を取得する

次のコードスニペットを使用して、PDFドキュメント内のキャレット注釈を取得してみてください：

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

### キャレット注釈を削除する

次のコードスニペットは、PDFファイルからキャレット注釈を削除する方法を示しています。

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

## Aspose.PDF for .NETを使用して特定のページ領域を削除注釈で削除する

Aspose.PDF for .NETは、既存のPDFファイルに注釈を追加および操作する機能をサポートしています。最近、顧客の一部がPDFドキュメントの特定のページ領域からテキスト、画像などの要素を削除する必要があると投稿しました。この要件を満たすために、RedactionAnnotationというクラスが提供されており、特定のページ領域を削除するために使用することができ、既存のRedactionAnnotationsを操作して削除することもできます（つまり、注釈をフラット化し、その下のテキストを削除します）。

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

### ファサードアプローチ

Aspose.Pdf.Facades名前空間には、PDFファイル内の既存の注釈を操作する機能を提供する[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor)というクラスもあります。このクラスには、特定のページ領域を削除する機能を提供する[RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea)というメソッドが含まれています。

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