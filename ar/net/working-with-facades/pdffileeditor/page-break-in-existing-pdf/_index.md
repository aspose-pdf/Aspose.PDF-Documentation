---
title: فاصل صفحات في ملف PDF موجود
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/page-break-in-existing-pdf/
description: اكتشف كيفية إدراج فواصل صفحات في ملف PDF موجود في .NET باستخدام Aspose.PDF لتحسين إدارة الصفحات.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Page Break in existing PDF",
    "alternativeHeadline": "Insert Custom Page Breaks in PDF Files",
    "abstract": "تقديم وظيفة فاصل الصفحات في فئة PdfFileEditor، مما يمكّن المستخدمين من التحكم في تخطيط مستندات PDF الموجودة بدقة. تتيح هذه الميزة إدراج فواصل صفحات في مواقع محددة داخل المستند، مما يعزز التخصيص ويحسن العرض العام للمحتوى. من خلال استدعاءات طرق بسيطة، يمكن للمستخدمين تعديل ملفات PDF الخاصة بهم بسهولة لتلبية متطلبات التنسيق المحددة.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "369",
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
    "url": "/net/page-break-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-break-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

كإعداد افتراضي، يتم إضافة المحتويات داخل ملفات PDF في تخطيط من أعلى اليسار إلى أسفل اليمين. بمجرد أن يتجاوز المحتوى هامش أسفل الصفحة، يحدث فاصل الصفحة. ومع ذلك، قد تواجه متطلبات لإدراج فاصل صفحة حسب الحاجة. تم إضافة طريقة تسمى AddPageBreak(...) في فئة [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) لتحقيق هذا المتطلب.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1).
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2).
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak).

- src هو مستند المصدر/مسار إلى المستند/تدفق مع مستند المصدر.
- dest هو مستند الوجهة/مسار حيث سيتم حفظ المستند/تدفق حيث سيتم حفظ المستند.
- PageBreak هو مصفوفة من كائنات فاصل الصفحة. تحتوي على خاصيتين: فهرس الصفحة حيث يجب وضع فاصل الصفحة والموقع العمودي لفاصل الصفحة على الصفحة.

## مثال 1 (إضافة فاصل صفحة)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PageBreak.pdf"))
    {
        // Create PDF document
        using (var dest = new Aspose.Pdf.Document())
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
            fileEditor.AddPageBreak(document, dest, new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
            {
                new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
            });
            // Save PDF document
            dest.Save(dataDir + "PageBreak_out.pdf");
        }
    }
}
```

## مثال 2

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    // Create PdfFileEditor object
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    fileEditor.AddPageBreak(dataDir + "PageBreak.pdf",
        dataDir + "PageBreakWithDestPath_out.pdf",
        new Aspose.Pdf.Facades.PdfFileEditor.PageBreak[]
        {
            new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
        });
}
```

## مثال 3

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PageBrakeExample03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_PageBreak();

    using (var src = new FileStream(dataDir + "PageBreak.pdf", FileMode.Open, FileAccess.Read))
    {
        using (var dest = new FileStream(dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            // Create PdfFileEditor object
            var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();

            // Add page break
            fileEditor.AddPageBreak(src, dest,
                new[]
                {
                    new Aspose.Pdf.Facades.PdfFileEditor.PageBreak(1, 450)
                });
        }
    }
}
```