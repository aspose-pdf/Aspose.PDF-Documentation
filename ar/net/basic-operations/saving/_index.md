---
title: حفظ مستند PDF برمجياً
linktitle: حفظ PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ar/net/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF في مكتبة C# Aspose.PDF for .NET. حفظ مستند PDF في نظام الملفات، إلى دفق، وفي تطبيقات الويب.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Save PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Saving with C#",
    "abstract": "اكتشف كيف يقوم المطورون بحفظ مستندات PDF برمجياً بسهولة باستخدام Aspose.PDF for .NET. تدعم هذه الميزة حفظ ملفات PDF في نظام الملفات، والدفقات، وداخل تطبيقات الويب مباشرة، مما يلبي حالات الاستخدام المتنوعة مع ضمان الامتثال لمعايير PDF/A و PDF/X للأرشفة طويلة الأجل وتبادل الرسوم. قم بتحسين قدرات التعامل مع PDF الخاصة بك مع هذه الآلية القوية للحفظ",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "471",
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
    "url": "/net/save-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/save-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة ولكن أيضًا التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

الشفرة البرمجية التالية تعمل أيضًا مع مكتبة [Aspose.Drawing](/pdf/net/drawing/) .

## حفظ مستند PDF في نظام الملفات

يمكنك حفظ مستند PDF الذي تم إنشاؤه أو تعديله في نظام الملفات باستخدام طريقة `Save` من فئة `Document`.
عندما لا تقدم نوع التنسيق (الخيارات)، يتم حفظ المستند بتنسيق Aspose.PDF v.1.7 (*.pdf).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

## حفظ مستند PDF في دفق

يمكنك أيضًا حفظ مستند PDF الذي تم إنشاؤه أو تعديله في دفق باستخدام التحميلات الزائدة لطرق `Save`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Make some manipation, i.g add new empty page
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "SimpleResume_out.pdf");
    }
}
```

للحصول على شرح أكثر تفصيلاً، يرجى الانتقال إلى قسم [Showcase](/pdf/net/showcases/) .

## حفظ تنسيق PDF/A أو PDF/X

PDF/A هو إصدار موحد وفقًا لمعيار ISO من تنسيق المستندات المحمولة (PDF) للاستخدام في الأرشفة والحفاظ على المستندات الإلكترونية على المدى الطويل.
يختلف PDF/A عن PDF في أنه يمنع الميزات غير المناسبة للأرشفة طويلة الأجل، مثل ربط الخطوط (بدلاً من تضمين الخطوط) والتشفير. تشمل متطلبات ISO لمشغلات PDF/A إرشادات إدارة الألوان، ودعم الخطوط المضمنة، وواجهة مستخدم لقراءة التعليقات المضمنة.

PDF/X هو مجموعة فرعية من معيار PDF ISO. الغرض من PDF/X هو تسهيل تبادل الرسوم، وبالتالي لديه سلسلة من المتطلبات المتعلقة بالطباعة التي لا تنطبق على ملفات PDF القياسية.

في كلتا الحالتين، يتم استخدام طريقة `Save` لتخزين المستندات، بينما يجب إعداد المستندات باستخدام طريقة `Convert`.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveDocumentAsPDFx()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Add page
        document.Pages.Add();
        // Convert a document to a PDF/X-3 format
        document.Convert(new Aspose.Pdf.PdfFormatConversionOptions(Aspose.Pdf.PdfFormat.PDF_X_3));
        // Save PDF document
        document.Save(dataDir + "SimpleResume_X3.pdf");
    }
}
```