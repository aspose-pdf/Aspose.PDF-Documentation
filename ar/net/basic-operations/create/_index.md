---
title: إنشاء مستند PDF برمجيًا
linktitle: إنشاء PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/create-document/
description: تصف هذه الصفحة كيفية إنشاء مستند PDF من الصفر باستخدام مكتبة Aspose.PDF.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create PDF document programmatically",
    "alternativeHeadline": "Programmatic PDF Creation Made Easy with C#",
    "abstract": "تتيح الميزة الجديدة في Aspose.PDF for .NET للمطورين إنشاء مستندات PDF برمجيًا باستخدام C# و VB.NET، مما يسهل العملية لمجموعة متنوعة من تطبيقات .NET مثل WinForms و ASP.NET. مع طرق بسيطة لإضافة صفحات ونصوص، يمكن للمستخدمين بسهولة إنشاء ملفات PDF مخصصة من الصفر، مما يعزز من وظائف تطبيقاتهم وتجربة المستخدم.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "307",
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
    "url": "/net/create-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-document/"
    },
    "dateModified": "2024-11-25",
    "description": "يمكن لمكتبة Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

Aspose.PDF for .NET API يتيح لك إنشاء وقراءة ملفات PDF باستخدام C# و VB.NET. يمكن استخدام API في مجموعة متنوعة من تطبيقات .NET بما في ذلك WinForms و ASP.NET والعديد من التطبيقات الأخرى. في هذه المقالة، سنوضح كيفية استخدام Aspose.PDF for .NET API لتوليد وقراءة ملفات PDF بسهولة في تطبيقات .NET.

## كيفية إنشاء ملف PDF باستخدام C#

لإنشاء ملف PDF باستخدام C#، يمكن استخدام الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. إضافة كائن [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) إلى مجموعة [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) الخاصة بكائن Document.
1. إضافة [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) الخاصة بالصفحة.
1. حفظ مستند PDF الناتج.

تعمل الشيفرة البرمجية التالية أيضًا مع مكتبة [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void HelloWorld()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

في هذه الحالة، نقوم بإنشاء مستند PDF بصفحة واحدة بحجم A4، واتجاه عمودي. ستحتوي صفحتنا على "Hello, World" في الجزء العلوي الأيسر من الصفحة.