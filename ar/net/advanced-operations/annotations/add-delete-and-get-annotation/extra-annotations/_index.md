---
title: إضافات إضافية باستخدام C#
linktitle: إضافات إضافية
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ar/net/extra-annotations/
description: تعلم كيفية إضافة إضافات إضافية إلى ملفات PDF في .NET باستخدام Aspose.PDF لميزات الوثائق التفاعلية.
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
    "abstract": "تقديم ميزة الإضافات الإضافية في C#، والتي تتيح للمطورين إضافة واسترجاع وإزالة أنواع مختلفة من الإضافات من مستندات PDF بسلاسة. تعزز هذه الوظيفة القوية تفاعل PDF من خلال تمكين تحرير النص بدقة والتلاعب بالوثائق، بما في ذلك القدرة على إضافة إضافات المؤشر والإزالة بشكل فعال. قم بتحسين معالجة PDF الخاصة بك مع هذه القدرات المتقدمة المصممة لإدارة الوثائق بشكل بديهي.",
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
    "description": "تصف هذه القسم كيفية إضافة والحصول على وحذف أنواع إضافية من الإضافات من مستند PDF الخاص بك."
}
</script>

## كيفية إضافة إضافة المؤشر إلى ملف PDF موجود

إضافة المؤشر هي رمز يشير إلى تحرير النص. إضافة المؤشر هي أيضًا إضافة تمييز، لذا فإن فئة المؤشر تشتق من فئة التمييز وتوفر أيضًا وظائف للحصول على أو تعيين خصائص إضافة المؤشر وإعادة تعيين تدفق مظهر إضافة المؤشر.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

خطوات إنشاء إضافة المؤشر:

1. تحميل ملف PDF - new [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إنشاء إضافة مؤشر جديدة [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) وتعيين معلمات المؤشر (new Rectangle، title، Subject، Flags، color، width، StartingStyle و EndingStyle). تُستخدم هذه الإضافة للإشارة إلى إدخال النص.
1. إنشاء إضافة مؤشر جديدة [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) وتعيين معلمات المؤشر (new Rectangle، title، Subject، Flags، color، width، StartingStyle و EndingStyle). تُستخدم هذه الإضافة للإشارة إلى استبدال النص.
1. إنشاء إضافة [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) جديدة وتعيين المعلمات (new Rectangle، title، color، new QuadPoints و new points، Subject، InReplyTo، ReplyType).
1. بعد ذلك يمكننا إضافة الإضافات إلى الصفحة.

تظهر مقتطفات الكود التالية كيفية إضافة إضافة المؤشر إلى ملف PDF:

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

### الحصول على إضافة المؤشر

يرجى محاولة استخدام مقتطف الكود التالي للحصول على إضافة المؤشر في مستند PDF:

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

### حذف إضافة المؤشر

تظهر مقتطفات الكود التالية كيفية حذف إضافة المؤشر من ملف PDF.

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

## حذف منطقة معينة من الصفحة باستخدام إضافة الإزالة باستخدام Aspose.PDF for .NET

يدعم Aspose.PDF for .NET ميزة إضافة وكذلك التلاعب بالإضافات في ملف PDF موجود. مؤخرًا، نشر بعض عملائنا طلبًا لحذف (إزالة النص، الصورة، إلخ من) منطقة معينة من صفحة مستند PDF. من أجل تلبية هذا الطلب، تم توفير فئة تسمى RedactionAnnotation، والتي يمكن استخدامها لحذف مناطق معينة من الصفحة أو يمكن استخدامها للتلاعب بإضافات الإزالة الموجودة وحذفها (أي تسطيح الإضافة وإزالة النص تحتها).

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

### نهج الواجهات

تحتوي مساحة الأسماء Aspose.Pdf.Facades أيضًا على فئة تسمى [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) التي توفر ميزة التلاعب بالإضافات الموجودة داخل ملف PDF. تحتوي هذه الفئة على طريقة تسمى [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) التي توفر القدرة على إزالة مناطق معينة من الصفحة.

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