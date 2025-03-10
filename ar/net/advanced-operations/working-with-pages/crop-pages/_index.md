---
title: قص صفحات PDF برمجياً C#
linktitle: قص الصفحات
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ar/net/crop-pages/
description: يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع باستخدام Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "Crop PDF Pages Easily with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NET يقدم ميزة جديدة قوية تتيح للمطورين الوصول برمجياً والتلاعب بمختلف خصائص صفحات PDF، بما في ذلك صندوق الوسائط، صندوق النزيف، صندوق القطع، صندوق الفن، وصندوق القص. تسهل هذه الوظيفة عملية تخصيص تخطيطات PDF، مما يضمن الدقة في عرض المستندات وتحسين جودة الطباعة مع تقليل الحواف البيضاء. مع مقتطفات الشيفرة السهلة الاستخدام، يمكن للمستخدمين دمج هذه القدرات بسلاسة في تطبيقاتهم، مما يحسن إدارة PDF والتلاعب به.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "يمكنك الحصول على خصائص الصفحة، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع باستخدام Aspose.PDF for .NET."
}
</script>

## الحصول على خصائص الصفحة

كل صفحة في ملف PDF تحتوي على عدد من الخصائص، مثل العرض، الارتفاع، صندوق النزيف، صندوق القص وصندوق القطع. يتيح لك Aspose.PDF الوصول إلى هذه الخصائص.

- **صندوق الوسائط**: صندوق الوسائط هو أكبر صندوق صفحة. يتوافق مع حجم الصفحة (مثل A4، A5، US Letter، إلخ) الذي تم اختياره عند طباعة المستند إلى PostScript أو PDF. بعبارة أخرى، يحدد صندوق الوسائط الحجم الفعلي للوسائط التي يتم عرض مستند PDF عليها أو طباعته.
- **صندوق النزيف**: إذا كان المستند يحتوي على نزيف، فسيكون لدى PDF أيضاً صندوق نزيف. النزيف هو مقدار اللون (أو العمل الفني) الذي يمتد إلى ما وراء حافة الصفحة. يُستخدم لضمان أنه عند طباعة المستند وقطعه إلى الحجم ("قصه")، سيصل الحبر إلى حافة الصفحة. حتى إذا تم قص الصفحة بشكل غير دقيق - قطعها قليلاً بعيداً عن علامات القص - فلن تظهر أي حواف بيضاء على الصفحة.
- **صندوق القطع**: يشير صندوق القطع إلى الحجم النهائي للمستند بعد الطباعة والقص.
- **صندوق الفن**: صندوق الفن هو الصندوق المرسوم حول المحتويات الفعلية للصفحات في مستنداتك. يُستخدم هذا الصندوق عند استيراد مستندات PDF في تطبيقات أخرى.
- **صندوق القص**: صندوق القص هو حجم "الصفحة" الذي يتم عرض مستند PDF الخاص بك به في Adobe Acrobat. في العرض العادي، يتم عرض محتويات صندوق القص فقط في Adobe Acrobat. للحصول على أوصاف مفصلة لهذه الخصائص، اقرأ مواصفات Adobe.Pdf، وخاصة 10.10.1 حدود الصفحة.
- **Page.Rect**: التقاطع (المستطيل المرئي عادةً) بين MediaBox وDropBox. توضح الصورة أدناه هذه الخصائص.
للحصول على مزيد من التفاصيل، يرجى زيارة [هذه الصفحة](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

مقتطف الشيفرة التالي يعمل أيضاً مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

يوضح المقتطف أدناه كيفية قص الصفحة:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CropPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CropPageInput.pdf"))
    {
        Console.WriteLine(document.Pages[1].CropBox);
        Console.WriteLine(document.Pages[1].TrimBox);
        Console.WriteLine(document.Pages[1].ArtBox);
        Console.WriteLine(document.Pages[1].BleedBox);
        Console.WriteLine(document.Pages[1].MediaBox);
        // Create new Box rectangle
        var newBox = new Rectangle(200, 220, 2170, 1520);
        document.Pages[1].CropBox = newBox;
        document.Pages[1].TrimBox = newBox;
        document.Pages[1].ArtBox = newBox;
        document.Pages[1].BleedBox = newBox;
        // Save PDF document
        document.Save(dataDir + "CropPage_out.pdf");  
    }
}
```

في هذا المثال، استخدمنا ملف عينة [هنا](crop_page.pdf). في البداية، تبدو صفحتنا كما هو موضح في الشكل 1.

بعد التغيير، ستبدو الصفحة كما في الشكل 2.

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