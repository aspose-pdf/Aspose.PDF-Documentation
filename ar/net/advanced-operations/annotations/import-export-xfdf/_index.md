---
title: استيراد وتصدير التعليقات التوضيحية إلى XFDF
linktitle: استيراد وتصدير التعليقات التوضيحية إلى XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ar/net/import-export-xfdf/
description: يمكنك استيراد وتصدير التعليقات التوضيحية بتنسيق XFDF باستخدام C# ومكتبة Aspose.PDF for .NET.
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
    "abstract": "تعمل وظيفة الاستيراد والتصدير الجديدة لتنسيق XFDF في مكتبة Aspose.PDF for .NET على تحسين إدارة مستندات PDF من خلال السماح بنقل بيانات التعليقات التوضيحية بسلاسة. تتيح هذه الميزة للمستخدمين دمج التعليقات التوضيحية بسهولة من ملفات XFDF وتصديرها مرة أخرى، مما يعزز تبادل البيانات الفعال وقدرات الأرشفة لنماذج PDF.",
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
    "description": "يمكنك استيراد وتصدير التعليقات التوضيحية بتنسيق XFDF باستخدام C# ومكتبة Aspose.PDF for .NET."
}
</script>

{{% alert color="primary" %}}

XFDF هو اختصار لتنسيق بيانات نماذج XML. إنه تنسيق ملف قائم على XML. يُستخدم هذا التنسيق لتمثيل بيانات النموذج أو التعليقات التوضيحية الموجودة في نموذج PDF. يمكن استخدام XFDF لأغراض مختلفة، ولكن في حالتنا، يمكن استخدامه إما لإرسال أو استلام بيانات النموذج أو التعليقات التوضيحية إلى أجهزة كمبيوتر أو خوادم أخرى، أو يمكن استخدامه لأرشفة بيانات النموذج أو التعليقات التوضيحية. في هذه المقالة، سنرى كيف أخذت Aspose.Pdf.Facades هذا المفهوم بعين الاعتبار وكيف يمكننا استيراد وتصدير بيانات التعليقات التوضيحية إلى ملف XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** هو مكون غني بالميزات عندما يتعلق الأمر بتحرير مستندات PDF. كما نعلم، فإن XFDF هو جانب مهم من جوانب معالجة نماذج PDF، وقد أخذت مساحة أسماء Aspose.Pdf.Facades في Aspose.PDF for .NET هذا بعين الاعتبار، وقدمت طرقًا لاستيراد وتصدير بيانات التعليقات التوضيحية إلى ملفات XFDF.

تحتوي فئة [PDFAnnotationEditor](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor) على طريقتين للعمل مع استيراد وتصدير التعليقات التوضيحية إلى ملف XFDF. توفر طريقة [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) الوظيفة لتصدير التعليقات التوضيحية من مستند PDF إلى ملف XFDF، بينما تتيح لك طريقة [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/ar/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) استيراد التعليقات التوضيحية من ملف XFDF موجود. لاستيراد أو تصدير التعليقات التوضيحية، نحتاج إلى تحديد أنواع التعليقات التوضيحية. يمكننا تحديد هذه الأنواع في شكل تعداد ثم تمرير هذا التعداد كوسيط إلى أي من هذه الطرق. بهذه الطريقة، سيتم استيراد أو تصدير التعليقات التوضيحية من الأنواع المحددة فقط إلى ملف XFDF.

تعمل مقتطفات الكود التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/ar/net/drawing/).

تظهر مقتطفات الكود التالية كيفية تصدير التعليقات التوضيحية إلى ملف XFDF:

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

تصف مقتطفة الكود التالية كيفية استيراد التعليقات التوضيحية من ملف XFDF:

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

## طريقة أخرى لاستيراد/تصدير التعليقات التوضيحية دفعة واحدة

في الكود أدناه، تتيح طريقة ImportAnnotations استيراد التعليقات التوضيحية مباشرة من مستند PDF آخر.

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